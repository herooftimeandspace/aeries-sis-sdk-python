# Architecture

The SDK has three layers:

1. Contract acquisition and normalization under `contracts/` and `tools/sync_contracts.py`.
2. Generated endpoint wrappers under `src/aeries_sis_sdk/generated/`.
3. Hand-written runtime behavior under `src/aeries_sis_sdk/` for transport, errors, retries, auth, and validation.

This split keeps upstream-document parsing separate from the public SDK runtime.

## Bounded Response Handling

The hand-written sync and async clients open every response in streaming mode.
They count decoded bytes while reading and stop after the configured
`max_response_bytes` value plus one byte. Reading that one additional byte makes
the boundary precise: a body exactly at the limit remains valid, while a larger
body raises `AeriesResponseTooLargeError` before the runtime attempts JSON
decoding. The default limit is 16 MiB, and callers may set another positive
integer when constructing either client.

The limit applies to successful and unsuccessful responses. A response already
known to be oversized is not retried, even for an otherwise retry-safe generated
operation. The temporary partial body is cleared before the size exception is
created, and the exception stores only the method, status, contract path, and
configured limit.

Normal HTTP and JSON errors follow the same safe-context policy. Generated
operations record their contract path template rather than a URL containing
student identifiers or query parameters. Low-level requests record only the
query-free path. Provider `Message` text is collapsed to one line and limited to
512 characters; messages containing known credentials, URLs, query strings, or
long encoded values are discarded in favor of generic status text.
