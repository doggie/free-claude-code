"""Generic OpenAI-compatible adapter (custom base URL + API key)."""

from providers.defaults import OPENAI_DEFAULT_BASE

from .client import OpenAICompatProvider

__all__ = ["OPENAI_DEFAULT_BASE", "OpenAICompatProvider"]
