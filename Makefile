PYTHON ?= ./.venv/bin/python
PIP ?= $(PYTHON) -m pip

.PHONY: install sync-contracts generate-sdk test lint typecheck docs check build live-test

install:
	$(PIP) install -e '.[dev]'

sync-contracts:
	$(PYTHON) tools/sync_contracts.py

generate-sdk:
	$(PYTHON) tools/generate_sdk.py

test:
	$(PYTHON) -m pytest

lint:
	$(PYTHON) -m ruff check src tests tools

typecheck:
	$(PYTHON) -m mypy src

docs:
	$(PYTHON) tools/sync_docs_index.py
	$(PYTHON) -m mkdocs build --strict

check: lint typecheck test docs

build:
	$(PYTHON) -m build --no-isolation

live-test:
	$(PYTHON) -m pytest -m live
