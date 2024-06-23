"""Fine-tuning a model using the PEFT-LoRA method and serving it as a text generation service."""
import shutil
from pathlib import Path
from typing import Any, Callable, Union
from uuid import uuid4

import covalent as ct
import covalent_cloud as cc
from covalent_cloud.function_serve.deployment import Deployment

FT_ENV = "lora_fine_tuning@blueprints"

cc.create_env(
    name=FT_ENV,
    pip=[
        "accelerate==0.29.1",
        "bitsandbytes==0.43.0",
        "datasets==2.18.0",
        "peft==0.10.0",
        "scipy==1.12.0",
        "sentencepiece==0.2.0",
        "torch==2.2.2",
        "transformers==4.39.3",
        "trl==0.8.1",
    ],
    wait=True,
)

service_executor = cc.CloudExecutor(
    env=FT_ENV,
    num_cpus=6,
    num_gpus=1,
    gpu_type=cc.cloud_executor.GPU_TYPE.L40,
    memory="48GB",
    time_limit="6 hours"
)

lattice_executor = cc.CloudExecutor(
    env=FT_ENV,
    num_cpus=6,
    memory="12GB",
    time_limit="4 hours",
)

fine_tuning_executor = cc.CloudExecutor(
    env=FT_ENV,
    num_cpus=6,
    num_gpus=1,
    gpu_type=cc.cloud_executor.GPU_TYPE.A100,
    memory="32GB",
    time_limit="4 hours",
)


lora_fine_tuning_volume = cc.volume("lora-fine-tuning")


@ct.electron(executor=fine_tuning_executor)
def peft_fine_tuning(
    model_id,
    data,
    dataset_map_func,
    split,
    ft_args,
    device_map,
    save_volume,
    model_kwargs,
):
    """Fine tune a model using the PEFT-LoRA method and save it to a volume."""

    import torch
    from datasets import Dataset, DatasetDict, load_dataset, load_from_disk
    from peft import LoraConfig
    from transformers import (AutoModelForCausalLM, AutoTokenizer,
                            BitsAndBytesConfig, TrainingArguments)
    from trl import SFTTrainer

    if not ft_args.get("use_quantization", False):
        quantization_config = None
    else:
        bnb_4bit_compute_dtype = getattr(torch, ft_args["bnb_4bit_compute_dtype"])
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=ft_args["load_in_4bit"],
            bnb_4bit_quant_type=ft_args["bnb_4bit_quant_type"],
            bnb_4bit_compute_dtype=bnb_4bit_compute_dtype,
            bnb_4bit_use_double_quant=ft_args["bnb_4bit_use_double_quant"],
        )

    # Load and configure the downloaded model from pretrained
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=quantization_config,
        device_map=device_map,
        do_sample=True,
        **model_kwargs,
    )
    model.config.use_cache = False
    model.config.pretraining_tp = 1

    # Load and configure the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        model_id, trust_remote_code=True
    )
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    # Try download dataset else try to load from disk
    if isinstance(data, (Dataset, DatasetDict)):
        dataset = data
    else:
        try:
            dataset = load_dataset(data, split=split)
        except Exception:
            dataset_path_ = Path("/tmp") / Path(data).name
            shutil.copytree(data, dataset_path_)
            data = dataset_path_
            dataset = load_from_disk(data, keep_in_memory=True)

    if dataset_map_func:
        dataset = dataset.map(dataset_map_func)

    # Set up supervised fine-tuning trainer
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=LoraConfig(
            lora_alpha=ft_args["lora_alpha"],
            lora_dropout=ft_args["lora_dropout"],
            r=ft_args["r"],
            bias=ft_args["bias"],
            task_type=ft_args["task_type"],
        ),
        tokenizer=tokenizer,
        args=TrainingArguments(
            output_dir=ft_args["output_dir"],
            num_train_epochs=ft_args["num_train_epochs"],
            per_device_train_batch_size=ft_args["per_device_train_batch_size"],
            gradient_accumulation_steps=ft_args["gradient_accumulation_steps"],
            optim=ft_args["optim"],
            save_strategy=ft_args["save_strategy"],
            save_total_limit=ft_args["save_total_limit"],
            learning_rate=ft_args["learning_rate"],
            weight_decay=ft_args["weight_decay"],
            fp16=ft_args["fp16"],
            bf16=ft_args["bf16"],
            max_grad_norm=ft_args["max_grad_norm"],
            max_steps=ft_args["max_steps"],
            warmup_ratio=ft_args["warmup_ratio"],
            group_by_length=ft_args["group_by_length"],
            lr_scheduler_type=ft_args["lr_scheduler_type"],
            report_to=ft_args["report_to"],
        ),
        dataset_text_field=ft_args["dataset_text_field"],
        max_seq_length=ft_args["max_seq_length"],
        packing=ft_args["packing"],
        dataset_batch_size=ft_args["dataset_batch_size"],
    )

    # Run training
    trainer.train()

    # Save trained model
    new_model_filename = model_id.split("/")[-1] + f"_{uuid4()}"
    new_model_path = save_volume / new_model_filename
    trainer.model.save_pretrained(new_model_path)
    trainer.tokenizer.save_pretrained(new_model_path)

    return new_model_path


@cc.service(
    executor=service_executor,
    name="LoRA Fine-Tuned LLM",
    volume=lora_fine_tuning_volume
)
def llm_service(ft_model_path, device_map):
    """Serves a LoRA fine-tuned LLM for text generation."""

    from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

    ft_model_path_ = Path("/tmp") / Path(ft_model_path).name
    if ft_model_path_.exists():
        shutil.rmtree(ft_model_path_)
    shutil.copytree(ft_model_path, ft_model_path_)

    # Load and configure saved model
    model = AutoModelForCausalLM.from_pretrained(
        ft_model_path_, device_map=device_map, do_sample=True
    )

    # Load and configure tokenizer
    tokenizer = AutoTokenizer.from_pretrained(ft_model_path_)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    # Combine model and tokenizer into a pipeline
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )

    return {"pipe": pipe, "model": model, "tokenizer": tokenizer}


@llm_service.endpoint("/generate")
def generate_endpoint(pipe, prompt, max_new_tokens=400):
    """Generate text from a prompt."""

    output = pipe(
        prompt,
        truncation=True,
        max_new_tokens=max_new_tokens,
        num_return_sequences=1
    )
    return output[0]["generated_text"]


@llm_service.endpoint("/stream")
def generate_endpoint_stream(model, tokenizer, prompt, prepend_prompt=False, max_tokens=100):
    """Generate text from a prompt and stream the response."""

    import torch

    def _starts_with_space(_tokenizer, _token_id):
        token = _tokenizer.convert_ids_to_tokens(_token_id)
        return token.startswith('▁')

    _input = tokenizer(prompt, return_tensors='pt')
    _input = _input.to("cuda")

    if prepend_prompt:
        yield prompt

    for output_length in range(max_tokens):
        output = model.generate(**_input, max_new_tokens=1)
        current_token_id = output[0][-1]
        if current_token_id == tokenizer.eos_token_id:
            break

        current_token = tokenizer.decode(
            current_token_id, skip_special_tokens=True
        )
        if _starts_with_space(tokenizer, current_token_id.item()) and output_length > 1:
            current_token = ' ' + current_token
        yield current_token

        _input = {
            'input_ids': output.to("cuda"),
            'attention_mask': torch.ones(1, len(output[0])).to("cuda"),
        }


@ct.lattice(
    executor=lattice_executor,
    workflow_executor=lattice_executor,
)
def workflow_fine_tune_and_deploy_service(
    model_id: str,
    data: Union[str, Path, Any],
    split: str,
    device_map: Union[str, dict],
    ft_args: dict,
    model_kwargs: dict,
    deploy: bool,
    dataset_map_func: Union[Callable, None],
) -> Union[Deployment, str]:
    """Fine-tune a model using the PEFT-LoRA method and serve it as a text generation service."""

    ft_model_path = peft_fine_tuning(
        model_id=model_id,
        data=data,
        dataset_map_func=dataset_map_func,
        split=split,
        ft_args=ft_args,
        device_map=device_map,
        save_volume=lora_fine_tuning_volume,
        model_kwargs=model_kwargs,
    )
    if deploy:
        return llm_service(ft_model_path, device_map)

    return ft_model_path


dispatch_func = cc.dispatch(
    workflow_fine_tune_and_deploy_service,
    volume=lora_fine_tuning_volume,
)

dispatch_id = dispatch_func(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    data="imdb",
    split="train[:5%]",
    ft_args={
        "use_quantization": False,
        "load_in_4bit": True,
        "bnb_4bit_quant_type": "nf4",
        "bnb_4bit_compute_dtype": "float16",
        "bnb_4bit_use_double_quant": False,
        "output_dir": "./outputs",
        "learning_rate": 2e-3,
        "num_train_epochs": 5,
        "save_total_limit": 1,
        "save_strategy": "epoch",
        "per_device_train_batch_size": 2,
        "gradient_accumulation_steps": 1,
        "optim": "paged_adamw_32bit",
        "weight_decay": 0.001,
        "fp16": False,
        "bf16": False,
        "max_grad_norm": 0.3,
        "max_steps": -1,
        "warmup_ratio": 0.03,
        "group_by_length": True,
        "lr_scheduler_type": "cosine",
        "report_to": "none",
        "lora_alpha": 32,
        "lora_dropout": 0.05,
        "r": 32,
        "bias": "none",
        "task_type": "CAUSAL_LM",
        "dataset_text_field": "text",
        "max_seq_length": 1024,
        "packing": True,
        "dataset_batch_size": 10,
    },
    model_kwargs={},
    deploy=True,
    dataset_map_func=None,
    device_map="auto",
)

res = cc.get_result(dispatch_id, wait=True)
res.result.load()
print(res.result.value)
