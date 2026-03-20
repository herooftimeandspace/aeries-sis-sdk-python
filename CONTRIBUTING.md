# Contributing

## Ground Rules

- Follow `IMPLEMENTATION_PLAN.md`. If the plan changes, update the plan file first.
- Add or update tests before changing behavior.
- Keep docstrings and teaching-oriented comments current with the code.
- Do not commit generated artifacts that do not come from `make sync-contracts` or `make generate-sdk`.

## Local Setup

```bash
python -m venv .venv
./.venv/bin/python -m pip install -e '.[dev]'
make sync-contracts
make generate-sdk
make check
```

## Pull Request Checklist

- Tests pass with `make test`
- Docs build with `make docs`
- Lint and type checks pass with `make lint` and `make typecheck`
- Coverage stays at or above 95%
- Docstring coverage stays at 100%
