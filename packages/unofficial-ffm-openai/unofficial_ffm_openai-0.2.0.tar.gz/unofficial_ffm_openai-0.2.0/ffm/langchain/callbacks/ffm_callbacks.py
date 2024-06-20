
import threading
from typing import Any, Dict, List
from langchain.schema import LLMResult
from langchain_core.callbacks import BaseCallbackHandler
import logging

logger = logging.getLogger(__name__)

class FfmCallbackHandler(BaseCallbackHandler):
    """Callback Handler that tracks FFM info. 

    Args:
        BaseCallbackHandler (_type_): _description_
    """

    total_tokens: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    successful_requests: int = 0
    total_cost: float = 0.0

    def __init__(self) -> None:
        super().__init__()
        self._lock = threading.Lock()
    
    def __repr__(self) -> str:
        return (
            f"Tokens Used: {self.total_tokens}\n"
            f"\tPrompt Tokens: {self.prompt_tokens}\n"
            f"\tCompletion Tokens: {self.completion_tokens}\n"
            f"Successful Requests: {self.successful_requests}\n"
            f"Total Cost (USD): ${self.total_cost}"
        )
    
    @property
    def always_verbose(self) -> bool:
        """Whether to call verbose callbacks even if verbose is False."""
        return True

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Print out the prompts."""
        pass

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Print out the token."""
        pass

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Collect token usage."""
        if not response:
            return None
        
        generation = response.generations[0][0]
        generation_info = generation.generation_info
        
        if not generation_info:
            return None
        
        completion_tokens = generation_info['generated_tokens']
        prompt_tokens = generation_info['prompt_tokens']
        total_tokens = generation_info['total_tokens']

        with self._lock:
            self.successful_requests += 1
            self.total_tokens += total_tokens
            self.prompt_tokens = prompt_tokens
            self.completion_tokens = completion_tokens
    
    def __copy__(self) -> "FfmCallbackHandler":
        """Return a copy of the callback handler."""
        return self
    
    def __deepcopy__(self, memo: Any) -> "FfmCallbackHandler":
        """Return a deep copy of the callback handler."""
        return self
