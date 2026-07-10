"""Request builder for LiteLLM proxy (delegates to generic OpenAI builder).

The LiteLLM proxy exposes a standard OpenAI ``/chat/completions`` endpoint,
so the request body is identical to the generic OpenAI-compatible format.
"""

from providers.openai.request import build_request_body

__all__ = ["build_request_body"]
