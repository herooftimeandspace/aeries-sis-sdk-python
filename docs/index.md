<!-- This file is generated from README.md by tools/sync_docs_index.py. -->

# Aeries SIS Python SDK

`aeries-sis-sdk-python` is a schema-first Python SDK for the Aeries SIS API. The project is designed to be understandable to a junior engineer, so the codebase favors clear names, strong docstrings, and comments that explain intent instead of assuming deep Python knowledge.

## What This SDK Provides

- Sync and async API clients.
- A committed contract snapshot generated from the published Aeries API support articles.
- Generated endpoint namespaces for system, school, student, grades, attendance, staff, scheduling, gradebook, alerts, and pre-enrollment APIs.
- Typed exceptions, response models, and contract-aware retry behavior.
- A documentation site published to GitHub Pages that combines this README, onboarding guides, architecture notes, and API reference built from source docstrings.

## Quick Start

```bash
python -m venv .venv
./.venv/bin/python -m pip install -e '.[dev]'
make sync-contracts
make generate-sdk
make test
```

```python
from aeries_sis_sdk import Client

client = Client(
    base_url="https://district.example.edu/aeries",
    certificate="replace-me",
)

schools = client.schools.list_schools()
print(schools)
```

## Configuration

- `base_url`: The Aeries tenant root URL or the `/api/v5` URL.
- `certificate`: The API certificate sent through the `AERIES-CERT` header.
- `default_database_year`: Optional database year added to requests when supported.
- `timeout`: Request timeout in seconds. Default is `30.0`.
- `user_agent`: Optional user agent override.

Environment variables used by docs, tests, and live checks:

- `AERIES_TEST_BASE_URL`
- `AERIES_TEST_CERT`
- `AERIES_TEST_SCHOOL_CODE`
- `AERIES_TEST_STUDENT_ID`

## Development Workflow

1. Keep `IMPLEMENTATION_PLAN.md` current before changing plan-level behavior.
2. Sync the upstream docs into committed contract artifacts with `make sync-contracts`.
3. Regenerate endpoint wrappers with `make generate-sdk`.
4. Run `make check` before committing.

## Documentation

The GitHub Pages documentation site is built with MkDocs Material and includes:

- This README as the landing page.
- Beginner-focused guides in `docs/guides/`.
- API reference generated from docstrings in `src/aeries_sis_sdk/`.

Build locally with:

```bash
make docs
```
