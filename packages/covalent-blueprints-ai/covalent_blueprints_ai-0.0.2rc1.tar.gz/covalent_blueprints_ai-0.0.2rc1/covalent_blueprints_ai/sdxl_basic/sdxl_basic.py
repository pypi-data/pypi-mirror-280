"""Blueprint for an SDXL service that generates images based on a prompt."""

from covalent_blueprints import get_blueprint
from covalent_blueprints.blueprints.templates import SingleServiceBlueprint

from covalent_blueprints_ai._prefix import PREFIX


def sdxl_basic(model_name: str = "stabilityai/sdxl-turbo") -> SingleServiceBlueprint:
    """A blueprint that deploys a service to host an SDXL image generator.

    Args:
        model_name: The name of the model to deploy. Defaults to "stabilityai/sdxl-turbo".

    The service includes a single endpoint:
    - `/text-to-image`: Generate an image based on a prompt.

    The endpoint accepts the following keyword-only parameters:
    - `prompt`: The prompt to generate an image from.
    - `num_inference_steps`: The number of SDXL inference steps.

    The default executor has the following parameters:
    - `num_cpus`: 25
    - `num_gpus`: 1
    - `gpu_type`: 'l40'
    - `memory`: '56GB'
    - `time_limit`: '15 days'


    The deployment will use its default environment unless an overriding executor
    specifies a new one.

    Returns:
        Covalent blueprint that deploys an SDXL image generator.

    Example:

        ```
        sdxl_blueprint = sdxl_basic()
        sdxl_client = sdxl_blueprint.run()

        prompt = "A beautiful sunset over the ocean."
        num_inference_steps = 1

        # Generate an image based on a prompt.
        img_str = sdxl_client.text_to_image(
            prompt=prompt,
            num_inference_steps=num_inference_steps,
        )

        # Display the image.
        import base64
        import io
        from PIL import Image

        buffer = io.BytesIO(base64.b64decode(img_str))
        Image.open(buffer)
        ```
    """

    bp = get_blueprint(f"{PREFIX}/sdxl_basic", _cls=SingleServiceBlueprint)
    bp.executors.set_executor_key("text_to_image_service")
    bp.set_default_inputs(model_name)

    return bp
