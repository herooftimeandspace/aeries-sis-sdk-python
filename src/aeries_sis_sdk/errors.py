"""Exception types used by the Aeries SIS SDK.

The goal of this module is to give callers predictable exceptions with enough
context to understand what failed without leaking secrets like the certificate.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, init=False)
class ErrorContext:
    """Carry safe context while preserving the original ``url`` API.

    The ``url`` field now stores only a query-free path or contract template.
    ``path`` is an equivalent alias for code that wants the safer name. The
    custom initializer accepts either spelling while keeping positional calls
    from earlier SDK versions compatible.
    """

    method: str
    url: str
    status_code: int | None = None
    detail: str | None = None

    def __init__(
        self,
        method: str,
        url: str | None = None,
        status_code: int | None = None,
        detail: str | None = None,
        *,
        path: str | None = None,
    ) -> None:
        """Store one query-free location supplied as ``url`` or ``path``."""

        if url is None and path is None:
            raise TypeError("ErrorContext requires url or path.")
        if url is not None and path is not None and url != path:
            raise ValueError("ErrorContext url and path must match when both are provided.")
        self.method = method
        self.url = url if url is not None else path or ""
        self.status_code = status_code
        self.detail = detail

    @property
    def path(self) -> str:
        """Return the query-free value stored by the compatible ``url`` field."""

        return self.url

    @path.setter
    def path(self, value: str) -> None:
        """Update the safe location through the preferred ``path`` alias."""

        self.url = value


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


class AeriesResponseTooLargeError(AeriesError):
    """Raised when a response crosses the client's configured byte limit."""


class AeriesHTTPError(AeriesError):
    """Raised for non-auth HTTP errors returned by the API."""


class AeriesTransportError(AeriesError):
    """Raised for local networking issues before a response is received."""
