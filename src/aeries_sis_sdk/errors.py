"""Exception types used by the Aeries SIS SDK.

The goal of this module is to give callers predictable exceptions with enough
context to understand what failed without leaking secrets like the certificate.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ErrorContext:
    """Carry a small amount of safe context about a failed HTTP request."""

    method: str
    url: str
    status_code: int | None = None
    detail: str | None = None


class AeriesError(RuntimeError):
    """Base class for every exception raised by this SDK."""

    def __init__(self, message: str, *, context: ErrorContext | None = None) -> None:
        """Store the message and optional request context for debugging."""

        super().__init__(message)
        self.context = context


class AeriesAuthError(AeriesError):
    """Raised when the request is unauthorized or forbidden."""


class AeriesNotFoundError(AeriesError):
    """Raised when the API reports that a resource does not exist."""


class AeriesValidationError(AeriesError):
    """Raised when the API rejects the request or the response shape is invalid."""


class AeriesHTTPError(AeriesError):
    """Raised for non-auth HTTP errors returned by the API."""


class AeriesTransportError(AeriesError):
    """Raised for local networking issues before a response is received."""

