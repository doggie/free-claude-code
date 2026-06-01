"""LiteLLM proxy provider - forwards to a LiteLLM proxy via OpenAI-compatible API."""

from providers.defaults import LITELLM_DEFAULT_BASE

from .client import LiteLLMProvider

__all__ = ["LITELLM_DEFAULT_BASE", "LiteLLMProvider"]