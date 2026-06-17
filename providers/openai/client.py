"""Generic OpenAI-compatible chat completions provider.

Uses the standard OpenAI ``/chat/completions`` endpoint with a user-specified
base URL and API key.  Set ``OPENAI_BASE_URL`` and ``OPENAI_API_KEY`` in .env.
"""

from __future__ import annotations

from typing import Any

from providers.base import ProviderConfig
from providers.openai_compat import OpenAIChatTransport

from .request import build_request_body


class OpenAIProvider(OpenAIChatTransport):
    """Generic OpenAI-compatible provider (custom URL + API key)."""

    def __init__(self, config: ProviderConfig):
        base_url = config.base_url
        if not base_url:
            raise ValueError(
                "OPENAI_BASE_URL is required for the openai provider. "
                "Set it in your .env file."
            )
        super().__init__(
            config,
            provider_name="OPENAI",
            base_url=base_url,
            api_key=config.api_key,
        )

    def _build_request_body(
        self, request: Any, thinking_enabled: bool | None = None
    ) -> dict:
        return build_request_body(
            request,
            thinking_enabled=self._is_thinking_enabled(request, thinking_enabled),
        )
