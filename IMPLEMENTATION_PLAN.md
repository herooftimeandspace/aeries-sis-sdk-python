# Aeries SIS Python SDK (`aeries-sis-sdk-python`) Implementation Plan

## Summary
- Build a production-ready Python package inside `./aeries-sis-sdk-python`, modeled after the implementation-plan structure used in the existing repo plans, with `Summary`, public-interface constraints, implementation changes, test plan, and docs/CI sections.
- The first tracked artifact in execution mode is `IMPLEMENTATION_PLAN.md` at the repo root. It becomes the authoritative plan and must be updated before any plan-affecting code change.
- The SDK is TDD-first, schema-first, and documentation-first: write failing tests before code, derive a normalized contract from the linked Aeries docs, keep total coverage at or above 95%, and make the codebase understandable to a junior engineer or someone unfamiliar with Python.
- Primary contract sources are the linked Aeries support articles for full documentation, request building, and the school, student, grades, attendance, staff, scheduling, gradebook, alerts, and pre-enrollment endpoint groups. Treat those linked v5 docs as the only supported contract source for v1.

## Key Constraints And Public Interfaces
- Runtime target is Python 3.12+; distribution name is `aeries-sis-sdk-python`; import package is `aeries_sis_sdk`.
- Public entry points are `aeries_sis_sdk.Client` and `aeries_sis_sdk.AsyncClient`.
- Both clients expose `request(method, path, *, path_params=None, params=None, json=None, headers=None, database_year=None, timeout=None) -> dict | list | None` plus generated namespaces for `.system`, `.schools`, `.students`, `.grades`, `.attendance`, `.staff`, `.scheduling`, `.gradebook`, `.alerts`, and `.pre_enrollment`.
- Client config is `base_url`, `certificate`, `default_database_year=None`, `timeout=30.0`, `user_agent`, `max_response_bytes=16777216`, and optional injected `httpx` transport or session. The response limit must be a positive integer. Clients require identity content encoding and apply the limit to raw identity response bytes before JSON parsing so compressed data cannot expand ahead of the SDK-owned bound.
- Wire behavior is JSON-only for v1. Always send `Accept: application/json` and `AERIES-CERT`, and never expose the certificate in logs, reprs, exceptions, comments, docs examples, or test fixtures.
- Every module, class, public function, private helper, and non-trivial method must include a human-readable docstring that explains intent, inputs, outputs, side effects, and failure behavior for readers unfamiliar with Python and with this codebase.
- Non-trivial function bodies must also include inline or short block comments that explain why a step exists, what assumption it relies on, or how it maps to the Aeries contract. Comments must prefer plain language over jargon and must teach intent rather than restate syntax.
- Error handling uses typed exceptions rooted at `AeriesError`, with parsed `Message` payload support when the API returns documented error bodies.
- Retry policy is contract-aware. Only operations marked idempotent in the normalized contract may be retried automatically; command-like GET endpoints and other state-changing operations are never auto-retried.

## Implementation Changes
- Repo layout under `./aeries-sis-sdk-python`:
  - `src/aeries_sis_sdk` for transport, auth, errors, generated API modules, generated Pydantic models, and shared utilities
  - `contracts` for committed normalized contract snapshots, source metadata, and content hashes
  - `tools` for doc sync, contract normalization, SDK generation, and documentation helpers
  - `tests` split into `unit`, `contract`, `integration`, and `live`
  - root `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `SECURITY.md`, `.env.example`, `mkdocs.yml`, `docs/`, `Makefile`, GitHub workflows, and `IMPLEMENTATION_PLAN.md`
- Contract acquisition uses a checked-in manifest of the provided Aeries URLs. The sync tool fetches article HTML, parses headings and endpoint sections, and emits a normalized JSON contract with operation metadata, parameters, example payloads, field documentation, security area, side-effect classification, and source links.
- Add a small version-controlled override layer for doc inconsistencies, cross-linked models, naming mismatches, and side-effect classifications that cannot be derived safely from the docs alone.
- Generated SDK modules are created from the normalized contract at update time, not scraped at runtime. Human-authored code owns transport, auth, retries, validation, exceptions, and user-facing helpers.
- Response validation is conservative: documented fields get typed models, ambiguous fields fall back to optional permissive types, and extra undocumented response fields are allowed unless the docs explicitly declare a closed shape.
- Sync and async transports require `Accept-Encoding: identity`, reject encoded responses before reading their bodies, read raw identity responses incrementally, and stop after `max_response_bytes + 1` bytes. Responses at the configured limit are valid; larger success or error responses raise `AeriesResponseTooLargeError` without retaining the partial body or retrying the known-oversized response.
- Exception context contains the HTTP method and contract path without query parameters. Provider `Message` text is bounded, stripped of control characters, and discarded when it contains request credentials, substituted contract-path identifiers, or URL-like data that would be unsafe to log. Path-identifier matching remains aligned when optional contract placeholders are omitted. SDK transport and validation frames clear request, response, client, parsed payload, and body references before errors propagate, including model-validation and injected-stream failures.
- Documentation style is a hard requirement, not a cleanup task:
  - every function ships with a teaching-oriented docstring
  - modules begin with a short overview explaining their role in the SDK
  - generated code includes preserved header comments explaining that the file is generated, where it came from, and where to edit behavior safely
  - hand-written complex flows include brief block comments before parsing, normalization, retry, or schema-mapping logic
- GitHub Pages documentation is a first-class deliverable:
  - build one docs site that combines `README.md`, task-oriented guides, architecture notes, contract-sync docs, testing instructions, and API reference generated from code docstrings
  - use MkDocs Material with Python API reference generation so narrative docs and code docs live in one site
  - the docs landing page is sourced from or mirrored from `README.md` so package docs and repo docs do not diverge
  - publish the built site to GitHub Pages from CI on the default branch and on tagged releases

## Test Plan
- Unit tests:
  - base URL normalization, header injection, certificate redaction, `DatabaseYear` merging, timeout handling, bounded response reads, safe error context, retry behavior, and sync/async parity
  - parser extraction for each supported Aeries doc subsection and override application
  - model inference, error parsing, and side-effect classification for command-style GET endpoints
  - doc helper and API reference generation glue where custom code is used
- Contract tests:
  - every provided Aeries article parses into normalized operations with stable snapshots
  - generated operation inventory matches the normalized contract
  - field documentation and example payloads map to generated models and wrapper signatures
  - content-hash drift is detected when upstream doc content changes
- Integration tests:
  - always-on integration tests run against a local mock transport or mock server generated from the normalized contract so serialization, query handling, error surfaces, and generated wrappers are exercised end-to-end without a live tenant
  - opt-in live tests run with `@pytest.mark.live` using `AERIES_TEST_BASE_URL`, `AERIES_TEST_CERT`, and any required fixture IDs; read-only scenarios are default and skip cleanly when inputs are absent
  - live mutation or command tests require an explicit opt-in flag plus disposable tenant data; otherwise they are skipped
- Documentation and packaging tests:
  - enforce `pytest --cov=aeries_sis_sdk --cov-fail-under=95`
  - enforce docstring coverage for SDK source at 100%
  - enforce docs build in strict mode so broken links, missing API docs, or README/docs drift fail CI
  - verify bundled contract files and generated API docs are available from built wheel and sdist
- Scenario tests:
  - school and system discovery
  - student retrieval with and without `DatabaseYear`
  - representative read-only operations for grades, attendance, staff, scheduling, gradebook, and alerts
  - pre-enrollment command wrapper proving non-retry semantics and correct request and response mapping
  - documentation site generation from README plus code docstrings

## Docs, CI/CD, And Artifact
- Docs:
  - `README.md` is the concise package entry point and is also included in the GitHub Pages site
  - `docs/` contains onboarding guides, architecture notes, contract-sync behavior, testing guidance, live-test setup, and troubleshooting written for junior engineers
  - API reference is generated from source docstrings so code comments and published docs stay aligned
- CI:
  - quality workflow runs ruff, mypy, unit tests, contract tests, integration tests, coverage gates, docstring coverage checks, package build, and strict docs build
  - live workflow is secrets-gated and runs the opt-in live suite with merged coverage reporting
  - GitHub Pages workflow publishes the combined docs site
- Plan artifact:
  - `IMPLEMENTATION_PLAN.md` is the authoritative document for execution and change control

## Assumptions And Defaults
- The implementation target is Python, not Go.
- Full linked Aeries API surface is in scope for v1, though implementation may be staged internally behind one generated contract and one published SDK.
- The linked Aeries support articles are the sole contract source of truth for v1; undocumented endpoints or inferred fields are out of scope unless later added to the plan.
- JSON is the only supported response mode in v1.
- Code comments are instructional by default. When choosing between brevity and clarity for an unfamiliar junior engineer, prefer clarity.
- GitHub Pages is the required public documentation surface for v1, and docs must be generated from a mix of README content, curated guides, and API reference from code docstrings.
