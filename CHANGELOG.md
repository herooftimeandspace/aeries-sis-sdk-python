# Changelog

## Unreleased

## 0.2.0 - 2026-09-28

- Initial project scaffolding for the Aeries SIS Python SDK.
- Bump the default user agent to `aeries-sis-sdk-python/0.2.0`.
- Add equivalent sync and async streaming response limits, with a 32 MiB default
  and a typed `AeriesResponseTooLargeError` for oversized bodies.
- Sanitize exception context so it contains query-free contract paths and only
  bounded provider messages that are safe to retain.
- Move the development test stack to patched pytest 9 and pytest-asyncio 1
  releases so the release audit does not retain a known pytest vulnerability.
- Close review-discovered retention and retry gaps by bounding httpx chunks,
  checking response size before retries, releasing streams before backoff,
  detaching unsafe exception causes, and sanitizing actual request values.
- Preserve `ErrorContext.url` compatibility while exposing the same query-free
  value through the preferred `ErrorContext.path` alias.
- Require identity content encoding and count raw response bytes so compressed
  content cannot expand before the configured limit; reject encoded responses
  without reading their bodies.
- Remove request, response, client, and body objects from SDK error tracebacks,
  and suppress provider details that echo generated path identifiers.
- Align identifiers across omitted optional path placeholders, detach generated
  model-validation failures from their input documents, and scrub partial sync
  and async bodies when custom response streams fail.
- Add a `make audit` target that runs `pip check` and `pip-audit`, pin
  `pip-audit` in the dev extra, and run the target in CI so the release
  security gate is reproducible instead of depending on ad hoc local installs.
- Require `pip>=26.2.0` in the dev extra so the release audit gate does not
  resolve a pip release affected by PYSEC-2026-3721.
- Match the Go SDK's response hardening: a 32 MiB default limit with a 1 TiB
  ceiling, structured `limit` and `retryable` attributes on
  `AeriesResponseTooLargeError`, a typed `AeriesResponseDecodeError` that keeps
  the observed status, blank success bodies reported as empty results, and no
  provider detail retained for requests that carried a JSON body.
