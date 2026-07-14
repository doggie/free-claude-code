"""LiteLLM proxy provider (native Anthropic Messages API)."""

from __future__ import annotations

from typing import Any

from providers.anthropic_messages import AnthropicMessagesTransport
from providers.base import ProviderConfig
from providers.defaults import LITELLM_DEFAULT_BASE

from .request import build_request_body


class LiteLLMProvider(AnthropicMessagesTransport):
    """LiteLLM proxy using native Anthropic-compatible ``/messages`` endpoint."""

    def __init__(self, config: ProviderConfig):
        super().__init__(
            config,
            provider_name="LITELLM",
            default_base_url=LITELLM_DEFAULT_BASE,
        )

    def _build_request_body(
        self, request: Any, thinking_enabled: bool | None = None
    ) -> dict:
        return build_request_body(
            request,
            thinking_enabled=self._is_thinking_enabled(request, thinking_enabled),
        )
