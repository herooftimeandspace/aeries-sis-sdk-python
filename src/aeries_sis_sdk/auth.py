"""Header helpers for authenticating with the Aeries API."""

from __future__ import annotations

from collections.abc import Mapping


def redact_secret(secret: str) -> str:
    """Return a redacted representation of a secret for safe error messages."""

    if len(secret) <= 4:
        return "*" * len(secret)
    return f"{secret[:2]}{'*' * (len(secret) - 4)}{secret[-2:]}"


def build_headers(
    *,
    certificate: str,
    user_agent: str,
    extra_headers: Mapping[str, str] | None = None,
) -> dict[str, str]:
    """Build the default request headers for JSON Aeries API calls."""

    headers = {
        "Accept": "application/json",
        "AERIES-CERT": certificate,
        "User-Agent": user_agent,
    }
    if extra_headers:
        headers.update(extra_headers)
    return headers

