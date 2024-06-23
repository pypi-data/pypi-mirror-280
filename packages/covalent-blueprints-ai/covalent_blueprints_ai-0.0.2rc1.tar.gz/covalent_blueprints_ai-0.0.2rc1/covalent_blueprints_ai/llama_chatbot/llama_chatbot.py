"""Blueprint for a Llama-like LLM service that generates/streams text based on a prompt."""

from covalent_blueprints import get_blueprint
from covalent_blueprints.blueprints.templates import SingleServiceBlueprint

from covalent_blueprints_ai._prefix import PREFIX


def llama_chatbot(
    model_name: str = "NousResearch/Llama-2-7b-chat-hf",
    device_map: str = "auto",
) -> SingleServiceBlueprint:
    """A blueprint that deploys a service to host a Llama-like LLM chatbot.

    Args:
        model_name: Name of the pretrained LLM. Defaults to "NousResearch/Llama-2-7b-chat-hf".
        device_map: Device map for the pretrained LLM. Defaults to "auto".

    The deployed service includes two endpoints:
    - `/generate`: Generate a response to a prompt.
    - `/stream`: Generate a response to a prompt, streaming tokens.

    Both endpoints accept the following keyword-only parameters:
    - `prompt`: The prompt to generate a response to.
    - `max_new_tokens`: The maximum number of tokens to generate.

    The default executor has the following parameters:
    - `num_cpus`: 24
    - `num_gpus`: 1
    - `gpu_type`: 'a100-80g'
    - `memory`: '54GB'
    - `time_limit`: '15 days'

    The deployment will use its default environment unless an overriding executor
    specifies a new one.

    Returns:
       Covalent blueprint that deploys a Llama-like LLM chatbot.

    Example:

        ```
        chatbot_blueprint = llama_chatbot()
        chatbot_client = chatbot_blueprint.run()

        prompt = "Sometimes I think about "
        max_new_tokens = 50

        # Generate a response to a prompt.
        chatbot_client.generate(
            prompt=prompt,
            max_new_tokens=max_new_tokens,
        )

        # Generate a response to a prompt, streaming tokens.
        for token in chatbot_client.stream(prompt=prompt):
            print(token.decode(), end="")
        ```
    """
    bp = get_blueprint(f"{PREFIX}/llama_chatbot", _cls=SingleServiceBlueprint)
    bp.executors.set_executor_key("chatbot_backend")
    bp.set_default_inputs(model_name, device_map=device_map)

    return bp
