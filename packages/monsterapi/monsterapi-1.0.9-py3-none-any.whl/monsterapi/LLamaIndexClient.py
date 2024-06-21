from typing import Any, Callable, Dict, Optional, Sequence

import logging
import sys
import os

level = os.environ.get('LOGGING_LEVEL', 'INFO')

if level == 'DEBUG':
    logging.basicConfig(level=logging.DEBUG)
elif level == 'INFO':
    logging.basicConfig(level=logging.INFO)
elif level == 'WARNING':
    logging.basicConfig(level=logging.WARNING)
elif level == 'ERROR':
    logging.basicConfig(level=logging.ERROR)
elif level == 'CRITICAL':
    logging.basicConfig(level=logging.CRITICAL)

logger = logging.getLogger(__name__)

try:
    from llama_index.core.base.llms.types import ChatMessage, LLMMetadata
    from llama_index.core.callbacks import CallbackManager
    from llama_index.core.constants import DEFAULT_NUM_OUTPUTS, DEFAULT_TEMPERATURE
    from llama_index.core.base.llms.generic_utils import get_from_param_or_env
    from llama_index.core.types import BaseOutputParser, PydanticProgramMode
    from llama_index.llms.openai import OpenAI
except ImportError:
    logger.warning("Please import llama_index with pip install llama_index to use the LLAMA Index LLM Client")
    sys.exit(1)

DEFAULT_API_BASE = "https://llm.monsterapi.ai/v1"
DEFAULT_MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"

class MonsterLLM(OpenAI):
    """MonsterAPI LLM
    LLama Index Usable OpenAI LLM Adapter
    """

    def __init__(
        self,
        model: str = DEFAULT_MODEL,
        temperature: float = DEFAULT_TEMPERATURE,
        max_tokens: int = DEFAULT_NUM_OUTPUTS,
        additional_kwargs: Optional[Dict[str, Any]] = None,
        max_retries: int = 10,
        api_base: Optional[str] = DEFAULT_API_BASE,
        api_key: Optional[str] = None,
        callback_manager: Optional[CallbackManager] = None,
        system_prompt: Optional[str] = None,
        messages_to_prompt: Optional[Callable[[Sequence[ChatMessage]], str]] = None,
        completion_to_prompt: Optional[Callable[[str], str]] = None,
        pydantic_program_mode: PydanticProgramMode = PydanticProgramMode.DEFAULT,
        output_parser: Optional[BaseOutputParser] = None,
    ) -> None:
        additional_kwargs = additional_kwargs or {}
        callback_manager = callback_manager or CallbackManager([])

        api_base = get_from_param_or_env("api_base", api_base, "MONSTER_API_BASE")
        api_key = get_from_param_or_env("api_key", api_key, "MONSTER_API_KEY")

        super().__init__(
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            api_base=api_base,
            api_key=api_key,
            additional_kwargs=additional_kwargs,
            max_retries=max_retries,
            callback_manager=callback_manager,
            system_prompt=system_prompt,
            messages_to_prompt=messages_to_prompt,
            completion_to_prompt=completion_to_prompt,
            pydantic_program_mode=pydantic_program_mode,
            output_parser=output_parser,
        )

    @classmethod
    def class_name(cls) -> str:
        return "MonsterAPI LLMs"

    @property
    def metadata(self) -> LLMMetadata:
        return LLMMetadata(
            context_window=modelname_to_contextsize(self.model),
            num_output=self.max_tokens,
            is_chat_model=True,
            model_name=self.model,
            is_function_calling_model=False,
        )

    @property
    def _is_chat_model(self) -> bool:
        return True


def modelname_to_contextsize(model_name):
    model_to_context = {
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0": 2048,
        "meta-llama/Meta-Llama-3-8B-Instruct": 4096,
        "microsoft/Phi-3-mini-4k-instruct": 4096,
        "mistralai/Mistral-7B-Instruct-v0.2": 4096*2
    }
    return model_to_context.get(model_name)