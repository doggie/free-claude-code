"""LiteLLM proxy provider - OpenAI-compatible local API."""

from providers.defaults import LITELLM_DEFAULT_BASE

from .client import LiteLLMProvider

__all__ = ["LITELLM_DEFAULT_BASE", "LiteLLMProvider"]
