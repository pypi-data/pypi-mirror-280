# pylint: disable=import-outside-toplevel, import-error

import covalent_cloud as cc

cc.save_api_key("your-api-key")

cc.create_env(
    name="vllm-basic@blueprints",
    pip=["vllm"],
    wait=True,
)

service_executor = cc.CloudExecutor(
    env="vllm-basic@blueprints",
    num_cpus=6,
    memory="25GB",
    num_gpus=1,
    gpu_type=cc.cloud_executor.GPU_TYPE.A5000,
    time_limit="04:00:00",
)


@cc.service(executor=service_executor, name="vLLM Service")
# gpu_memory_utilization: float):
def vllm_service(
    model: str = "facebook/opt-125m",
    dtype: str = "auto",
    **llm_kwargs,
):
    """Serves a a vLLM-compatible model."""
    from vllm import LLM

    return {"llm": LLM(model=model, dtype=dtype, **llm_kwargs)}


@vllm_service.endpoint(route="/generate", name="Generate Text")
def generate(llm=None, prompt=None, temperature=0.8, top_p=0.95) -> str:
    """Generate text based on a prompt."""
    from vllm import SamplingParams

    sampling_params = SamplingParams(
        temperature=temperature,
        top_p=top_p
    )
    return llm.generate(prompt, sampling_params)[0].outputs[0].text


vllm_client = cc.deploy(vllm_service)(gpu_memory_utilization=0.9)
vllm_client = cc.get_deployment(vllm_client, wait=True)
print(vllm_client)
