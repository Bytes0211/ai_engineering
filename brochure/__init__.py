"""Brochure module for generating company brochures using LLMs."""

# Defer imports to avoid dependency issues during testing
__all__ = ["BrochureGenerator", "LINK_SYSTEM_PROMPT", "BROCHURE_SYSTEM_PROMPT"]

def __getattr__(name):
    if name in __all__:
        from .brochure import BrochureGenerator, LINK_SYSTEM_PROMPT, BROCHURE_SYSTEM_PROMPT
        return locals()[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
