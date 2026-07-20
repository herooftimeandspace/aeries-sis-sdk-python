# Architecture

The SDK has three layers:

1. Contract acquisition and normalization under `contracts/` and `tools/sync_contracts.py`.
2. Generated endpoint wrappers under `src/aeries_sis_sdk/generated/`.
3. Hand-written runtime behavior under `src/aeries_sis_sdk/` for transport, errors, retries, auth, and validation.

This split keeps upstream-document parsing separate from the public SDK runtime.

## Bounded Response Handling

The hand-written sync and async clients force `Accept-Encoding: identity`, open
every response in streaming mode, and reject any encoded response before its
body is read. They count raw identity bytes while reading and stop after the
configured `max_response_bytes` value plus one byte. Reading that one additional byte makes
the boundary precise: a body exactly at the limit remains valid, while a larger
body raises `AeriesResponseTooLargeError` before the runtime attempts JSON
decoding. The default limit is 16 MiB, and callers may set another positive
integer when constructing either client.

The limit applies to successful and unsuccessful responses. A response already
known to be oversized is not retried, even for an otherwise retry-safe generated
operation. Retryable responses are read through the same bound and their stream
is closed before backoff begins, so sleeping requests do not hold connections.
The runtime reads raw identity chunks so httpx cannot expand compressed data
before the limit check. It clears the temporary buffer, live chunk, iterator,
and response reference before creating the size exception. The
exception stores only the method, status, contract path, and configured limit.

Normal HTTP and JSON errors follow the same safe-context policy. Generated
operations record their contract path template rather than a URL containing
student identifiers or query parameters. Low-level requests record only the
query-free path. For compatibility, `ErrorContext.url` continues to exist but
contains that same safe path; `ErrorContext.path` is an equivalent alias.
Provider `Message` text is collapsed to one line and limited to 512 characters.
Messages containing actual request query/header values, identifiers substituted
into generated contract paths, known credentials, URLs, query strings, or long
encoded values are discarded in favor of generic status text. Sanitized
transport and malformed-JSON errors are raised without the original exception
chain because httpx requests and JSON parser errors can retain complete
credentials or response documents. Before an SDK error propagates, transport
and validation frames also clear client, request, response, header, parameter,
request-body, and response-body references that traceback-local collectors
might otherwise preserve.
