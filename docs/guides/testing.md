# Testing

The project uses several test layers:

- Unit tests for small behavior.
- Contract tests for parser and generator stability.
- Integration tests that exercise the generated SDK through a mock transport.
- Live tests that call a real tenant only when credentials are available.

The default suite enforces at least 95% coverage and 100% docstring coverage for SDK source.

