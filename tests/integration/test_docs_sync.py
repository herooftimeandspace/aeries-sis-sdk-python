"""Tests for the README-to-docs landing page sync helper."""

from __future__ import annotations

from pathlib import Path

from tools import sync_docs_index


def test_sync_docs_index_copies_readme(tmp_path: Path, monkeypatch) -> None:
    """The docs landing page should be generated from the README content."""

    readme_path = tmp_path / "README.md"
    docs_index_path = tmp_path / "index.md"
    readme_path.write_text("# Example\n\nBody text.\n", encoding="utf-8")
    monkeypatch.setattr(sync_docs_index, "README_PATH", readme_path)
    monkeypatch.setattr(sync_docs_index, "DOCS_INDEX_PATH", docs_index_path)

    sync_docs_index.main()

    docs_index_text = docs_index_path.read_text(encoding="utf-8")
    assert "generated from README.md" in docs_index_text
    assert "# Example" in docs_index_text

