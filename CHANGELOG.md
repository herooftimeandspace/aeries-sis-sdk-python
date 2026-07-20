# Changelog

## Unreleased

- Initial project scaffolding for the Aeries SIS Python SDK.
- Add equivalent sync and async streaming response limits, with a 16 MiB default
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
