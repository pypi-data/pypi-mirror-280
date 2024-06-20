from typing import TYPE_CHECKING, Any

import importlib

if TYPE_CHECKING:
    from ffm.langchain.callbacks.ffm_callbacks import (
        FfmCallbackHandler
    )
    from ffm.langchain.callbacks.manager import (
        get_ffm_callback
    )

_module_lookup ={
    "FfmCallbackHandler": "ffm.langchain.callbacks.ffm_callbacks",
    "get_ffm_callback": "ffm.langchain.callbacks.manager"
}

def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")

__all__ = [
    "FfmCallbackHandler",
    "get_ffm_callback"
]