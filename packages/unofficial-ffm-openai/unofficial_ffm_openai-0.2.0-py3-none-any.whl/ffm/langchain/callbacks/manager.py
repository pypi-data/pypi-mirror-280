from contextvars import ContextVar
from typing import Generator, Optional

from langchain_core.tracers.context import register_configure_hook
from ffm.langchain.callbacks import FfmCallbackHandler
from contextlib import contextmanager

ffm_callback_var: (ContextVar)[
    Optional[FfmCallbackHandler]
] = ContextVar("ffm_callback", default=None)

register_configure_hook(ffm_callback_var, True)
@contextmanager
def get_ffm_callback() -> (
    Generator[FfmCallbackHandler, None, None]
):    
    cb = FfmCallbackHandler()
    ffm_callback_var.set(cb)
    yield cb
    ffm_callback_var.set(None)