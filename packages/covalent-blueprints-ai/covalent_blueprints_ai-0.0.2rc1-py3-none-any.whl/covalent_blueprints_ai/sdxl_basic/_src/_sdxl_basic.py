import base64
import io

import covalent_cloud as cc

cc.save_api_key("your-api-key")

cc.create_env(
    name="realtime-sdxl@blueprints",
    pip=[
        "torch",
        "transformers[sentencepiece]",
        "accelerate",
        "diffusers",
    ],
    wait=True,
)

gpu_executor = cc.CloudExecutor(
    env="realtime-sdxl@blueprints",
    num_cpus=25,
    memory="56 GB",
    time_limit="15 days",
    num_gpus=1,
    gpu_type=cc.cloud_executor.GPU_TYPE.L40,
)


@cc.service(executor=gpu_executor, name="SDXL Image Generator Service")
def text_to_image_service(model_name: str = "stabilityai/sdxl-turbo"):
    """Creates an SDXL Image Generator service"""
    # pylint: disable=import-outside-toplevel
    import torch
    from diffusers import AutoPipelineForText2Image

    pipeline = AutoPipelineForText2Image.from_pretrained(
        model_name, torch_dtype=torch.float16, variant="fp16"
    ).to("cuda")

    return {"pipeline": pipeline}


@text_to_image_service.endpoint(route="/text-to-image")
def generate_image(pipeline, prompt: str, num_inference_steps: int = 1):
    """Generate an image based on a prompt"""
    image = pipeline(
        prompt=prompt, num_inference_steps=num_inference_steps, guidance_scale=0.0
    ).images[0]

    bytes_io = io.BytesIO()
    image.save(bytes_io, format='PNG')
    image_as_str = base64.b64encode(bytes_io.getvalue()).decode('utf-8')
    return image_as_str


info = cc.deploy(text_to_image_service)()
info = cc.get_deployment(info.function_id, wait=True)
print(info)
print(info.address)
