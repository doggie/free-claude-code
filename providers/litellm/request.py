"""Request builder for LiteLLM proxy (native Anthropic Messages API)."""

from __future__ import annotations

from typing import Any

from config.constants import ANTHROPIC_DEFAULT_MAX_OUTPUT_TOKENS
from core.anthropic.native_messages_request import (
    build_base_native_anthropic_request_body,
)


def build_request_body(request_data: Any, *, thinking_enabled: bool) -> dict:
    """Build an Anthropic-format request body for LiteLLM's messages API."""
    return build_base_native_anthropic_request_body(
        request_data,
        default_max_tokens=ANTHROPIC_DEFAULT_MAX_OUTPUT_TOKENS,
        thinking_enabled=thinking_enabled,
    )
