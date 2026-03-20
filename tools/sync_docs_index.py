"""Mirror README content into the MkDocs landing page."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README_PATH = ROOT / "README.md"
DOCS_INDEX_PATH = ROOT / "docs" / "index.md"


def main() -> None:
    """Copy README content into the docs landing page with a generated note."""

    readme_text = README_PATH.read_text(encoding="utf-8").strip()
    generated_note = (
        "<!-- This file is generated from README.md by tools/sync_docs_index.py. -->\n\n"
    )
    DOCS_INDEX_PATH.write_text(f"{generated_note}{readme_text}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
