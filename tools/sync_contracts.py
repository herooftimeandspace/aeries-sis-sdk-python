"""Fetch Aeries support articles and normalize them into a committed contract.

The Aeries docs are human-written support articles rather than an OpenAPI file.
This script turns those articles into a stable JSON contract the SDK can use
for generation, runtime behavior, and offline tests.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

import httpx
from bs4 import BeautifulSoup, Tag

ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = ROOT / "src" / "aeries_sis_sdk"

from aeries_sis_sdk.contract_types import (  # noqa: E402
    ContractDocument,
    ContractExample,
    ContractField,
    ContractOperation,
    ContractParameter,
    ContractSource,
)
from aeries_sis_sdk.naming import pascal_case, snake_case, unique_name  # noqa: E402

SOURCES_PATH = ROOT / "contracts" / "sources.json"
OVERRIDES_PATH = ROOT / "contracts" / "overrides" / "operations.json"
RAW_DIR = ROOT / "contracts" / "raw"
NORMALIZED_PATH = ROOT / "contracts" / "normalized" / "aeries_api_contract.json"
PACKAGED_CONTRACT_PATH = SRC_ROOT / "generated" / "contract_snapshot.json"

HEADING_MAP = {
    "url": "urls",
    "url(s)": "urls",
    "notes": "notes",
    "note": "notes",
    "query string filters": "query_filters",
    "field documentation": "field_docs",
    "errors": "errors",
    "request body": "request_body",
}
PARAM_LINE_PATTERN = re.compile(
    r"(?P<name>[A-Za-z][A-Za-z0-9_]*)\s*\((?P<required>required|optional)\)\s*[\u2013-]\s*(?P<description>.+)",
    re.IGNORECASE,
)
PATH_LINE_PATTERN = re.compile(
    r"^(?:(GET|POST|PUT|DELETE)\s+)?(?P<path>/api/v5[^\s]*)\s*(?P<description>.*)$",
    re.IGNORECASE,
)


def load_json(path: Path) -> Any:
    """Load a JSON file with UTF-8 encoding."""

    return json.loads(path.read_text(encoding="utf-8"))


def normalize_text(value: str) -> str:
    """Collapse whitespace so doc parsing is less sensitive to HTML formatting."""

    return " ".join(value.replace("\xa0", " ").split())


def fetch_source_html(url: str) -> str:
    """Download one upstream Aeries support article."""

    response = httpx.get(url, follow_redirects=True, timeout=30.0)
    response.raise_for_status()
    return response.text


def article_body(html: str) -> Tag:
    """Return the main article body from the Freshdesk page HTML."""

    soup = BeautifulSoup(html, "html.parser")
    body = soup.select_one("article.article-body")
    if body is None:
        raise RuntimeError("Could not find article.article-body in Aeries support page.")
    return body


def article_title(html: str) -> str:
    """Extract the page title shown in the browser title tag."""

    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.select_one("title")
    if title_tag is None or not title_tag.text.strip():
        return "Unknown Aeries Article"
    return normalize_text(title_tag.text.replace(": Aeries Software", ""))


def section_nodes(body: Tag) -> list[tuple[str, list[Tag], list[str]]]:
    """Split an article body into top-level endpoint sections.

    Each Aeries endpoint page uses `h2` or `h3` headings for operation groups,
    then `h4` headings such as `URL(s)` or `Field Documentation` within them.
    """

    sections: list[tuple[str, list[Tag], list[str]]] = []
    current_title: str | None = None
    current_nodes: list[Tag] = []
    intro_paragraphs: list[str] = []
    for child in body.children:
        if not isinstance(child, Tag):
            continue
        if child.name in {"h2", "h3"}:
            if current_title is not None:
                sections.append((current_title, current_nodes, intro_paragraphs))
            current_title = normalize_text(child.get_text(" ", strip=True))
            current_nodes = []
            intro_paragraphs = []
            continue
        if current_title is None:
            if child.name == "p":
                text = normalize_text(child.get_text(" ", strip=True))
                if text:
                    intro_paragraphs.append(text)
            continue
        current_nodes.append(child)
    if current_title is not None:
        sections.append((current_title, current_nodes, intro_paragraphs))
    return sections


def split_subsections(nodes: list[Tag]) -> tuple[list[str], dict[str, list[Tag]]]:
    """Group sibling nodes under their nearest `h4` heading."""

    summary: list[str] = []
    grouped: dict[str, list[Tag]] = {}
    current_key = "summary"
    grouped[current_key] = []
    for node in nodes:
        if node.name == "h4":
            key = normalize_text(node.get_text(" ", strip=True)).rstrip(":").lower()
            current_key = HEADING_MAP.get(key, snake_case(key))
            grouped.setdefault(current_key, [])
            continue
        grouped.setdefault(current_key, []).append(node)
    for node in grouped.pop("summary", []):
        text = normalize_text(node.get_text(" ", strip=True))
        if text:
            summary.append(text)
    return summary, grouped


def list_texts(nodes: list[Tag]) -> list[str]:
    """Extract text from lists, paragraphs, and code blocks in order."""

    values: list[str] = []
    for node in nodes:
        if node.name == "table":
            continue
        if node.name in {"ul", "ol"}:
            for item in node.find_all("li", recursive=False):
                text = normalize_text(item.get_text(" ", strip=True))
                if text:
                    values.append(text)
            continue
        text = normalize_text(node.get_text(" ", strip=True))
        if text:
            values.append(text)
    return values


def table_rows(nodes: list[Tag]) -> list[dict[str, str]]:
    """Convert the first table in a subsection into a list of row dictionaries."""

    for node in nodes:
        if node.name != "table":
            continue
        rows = node.find_all("tr")
        if not rows:
            return []
        headers = [
            normalize_text(cell.get_text(" ", strip=True))
            for cell in rows[0].find_all(["th", "td"])
        ]
        parsed_rows: list[dict[str, str]] = []
        for row in rows[1:]:
            cells = [
                normalize_text(cell.get_text(" ", strip=True))
                for cell in row.find_all(["th", "td"])
            ]
            if not any(cells):
                continue
            padded = cells + [""] * (len(headers) - len(cells))
            parsed_rows.append(dict(zip(headers, padded, strict=False)))
        return parsed_rows
    return []


def infer_type(field_name: str, description: str) -> str:
    """Infer a conservative Python type name from field documentation text."""

    combined = f"{field_name} {description}".lower()
    if "date" in combined and "datetime" not in combined:
        return "str"
    if "time" in combined:
        return "str"
    if "count" in combined or "number" in combined or "code" in combined:
        return "int | str"
    if (
        "flag" in combined
        or combined.startswith("is ")
        or "true" in combined
        or "false" in combined
    ):
        return "bool"
    return "str"


def parse_field_docs(nodes: list[Tag]) -> list[ContractField]:
    """Parse a field-documentation table into normalized field records."""

    rows = table_rows(nodes)
    fields: list[ContractField] = []
    for row in rows:
        name = row.get("Name") or row.get("Field Name") or ""
        description = row.get("Description") or ""
        source_column = row.get("Aeries Table.Column") or row.get("Aeries Table/Column")
        if not name:
            continue
        fields.append(
            ContractField(
                name=name,
                python_name=snake_case(name),
                source_column=source_column,
                description=description,
                inferred_type=infer_type(name, description),
            )
        )
    return fields


def parse_parameters(lines: list[str], *, location: str) -> list[ContractParameter]:
    """Parse parameter descriptions from bullet lines."""

    parameters: list[ContractParameter] = []
    seen: set[tuple[str, str]] = set()
    for line in lines:
        match = PARAM_LINE_PATTERN.search(line)
        if match is None:
            continue
        name = match.group("name")
        key = (location, name)
        if key in seen:
            continue
        seen.add(key)
        parameters.append(
            ContractParameter(
                name=name,
                python_name=snake_case(name),
                location=location,  # type: ignore[arg-type]
                required=match.group("required").lower() == "required",
                description=match.group("description").strip(),
            )
        )
    return parameters


def response_kind_from_examples(examples: list[ContractExample]) -> str:
    """Infer whether an endpoint returns an object or list from example content."""

    for example in examples:
        stripped = example.content.lstrip()
        if stripped.startswith("["):
            return "list"
        if stripped.startswith("{"):
            return "object"
    return "unknown"


def parse_examples(
    section_title: str, grouped_nodes: dict[str, list[Tag]]
) -> list[ContractExample]:
    """Extract example blocks from subsection groups."""

    examples: list[ContractExample] = []
    for heading, nodes in grouped_nodes.items():
        if not heading.startswith("example"):
            continue
        for node in nodes:
            if node.name == "pre":
                content = node.get_text("\n", strip=True)
                examples.append(
                    ContractExample(label=section_title, content=content, format="json")
                )
                continue
            text = normalize_text(node.get_text(" ", strip=True))
            if text.startswith("http"):
                examples.append(ContractExample(label=section_title, content=text, format="url"))
            elif text:
                examples.append(ContractExample(label=section_title, content=text, format="text"))
    return examples


def operation_variants(url_lines: list[str]) -> list[dict[str, str]]:
    """Split a URL subsection into one or more method/path variants."""

    variants: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in url_lines:
        match = PATH_LINE_PATTERN.match(line)
        if match:
            current = {
                "method": (match.group(1) or "GET").upper(),
                "path_template": match.group("path"),
                "description": match.group("description").strip(),
            }
            variants.append(current)
            continue
        if current is not None:
            current["description"] = f'{current["description"]} {line}'.strip()
    return variants


def base_method_name(section_title: str, method: str) -> str:
    """Create a readable Python method name from a section title and HTTP method."""

    base = snake_case(section_title)
    if method == "GET" and not base.startswith(("get_", "list_", "trigger_", "pre_enroll_")):
        return f"get_{base}"
    if method == "POST" and not base.startswith(("create_", "add_")):
        return f"create_{base}"
    if method == "PUT" and not base.startswith("update_"):
        return f"update_{base}"
    if method == "DELETE" and not base.startswith("delete_"):
        return f"delete_{base}"
    return base


def variant_suffix(base_path: str, variant_path: str) -> str:
    """Return a deterministic suffix that distinguishes multiple path variants."""

    base_tokens = [token for token in base_path.strip("/").split("/") if token]
    variant_tokens = [token for token in variant_path.strip("/").split("/") if token]
    common_length = 0
    for left, right in zip(base_tokens, variant_tokens, strict=False):
        if left != right:
            break
        common_length += 1
    suffix_tokens = variant_tokens[common_length:]
    if not suffix_tokens:
        return ""
    return "_" + snake_case("_".join(token.strip("{}") for token in suffix_tokens))


def path_parameter_docs(
    path_template: str, url_description: str, extra_lines: list[str]
) -> list[ContractParameter]:
    """Create path parameter records from placeholders and doc bullet lines."""

    placeholder_names = re.findall(r"{([^}]+)}", path_template)
    parameters = parse_parameters([url_description, *extra_lines], location="path")
    existing = {parameter.name for parameter in parameters}
    optional_names = {
        match.group("name")
        for line in [url_description, *extra_lines]
        for match in [PARAM_LINE_PATTERN.search(line)]
        if match is not None and match.group("required").lower() == "optional"
    }
    for placeholder_name in placeholder_names:
        if placeholder_name in existing:
            continue
        parameters.append(
            ContractParameter(
                name=placeholder_name,
                python_name=snake_case(placeholder_name),
                location="path",
                required=placeholder_name not in optional_names,
                description=f"Path parameter extracted from {path_template}.",
            )
        )
    return parameters


def apply_overrides(operation: ContractOperation, overrides: dict[str, Any]) -> ContractOperation:
    """Apply manual override data to an operation after parsing."""

    override = overrides.get(operation.operation_id)
    if not override:
        return operation
    payload = operation.model_dump()
    payload.update(override)
    return ContractOperation.model_validate(payload)


def category_for_operation(source_category: str, section_title: str, path_template: str) -> str:
    """Return the namespace category that should own one parsed operation."""

    if path_template == "/api/v5/systeminfo" or "installation information" in section_title.lower():
        return "system"
    return source_category


def build_request_defaults(meta_source: ContractSource, html: str) -> dict[str, Any]:
    """Extract the cross-endpoint request rules from the request-building page."""

    body = article_body(html)
    text = normalize_text(body.get_text(" ", strip=True))
    return {
        "source_key": meta_source.key,
        "source_url": meta_source.url,
        "response_format": "json",
        "certificate_header": "AERIES-CERT",
        "accept_header": "application/json",
        "database_year_parameter": "DatabaseYear",
        "notes": [
            "The Aeries API is a REST API.",
            "Current endpoints use primarily the HTTP GET verb.",
            "Certain endpoints also support POST, PUT, and DELETE.",
            text[:500],
        ],
    }


def build_contract() -> ContractDocument:
    """Fetch upstream docs, parse them, and return a normalized contract."""

    source_payloads = load_json(SOURCES_PATH)
    overrides = load_json(OVERRIDES_PATH)
    document = ContractDocument()
    seen_operation_names: set[str] = set()
    meta_source: ContractSource | None = None
    meta_html: str | None = None
    for source_payload in source_payloads:
        source = ContractSource.model_validate(source_payload)
        html = fetch_source_html(source.url)
        body = article_body(html)
        html_hash = hashlib.sha256(html.encode("utf-8")).hexdigest()
        raw_path = RAW_DIR / f"{source.key}.html"
        raw_path.write_text(html, encoding="utf-8")
        source.article_title = article_title(html)
        source.content_hash = html_hash
        source.raw_path = str(raw_path.relative_to(ROOT))
        document.sources.append(source)
        if source.category == "meta":
            meta_source = source
            meta_html = html
            continue
        if source.category == "index":
            continue
        for section_title, nodes, intro_paragraphs in section_nodes(body):
            summary, grouped = split_subsections(nodes)
            url_lines = list_texts(grouped.get("urls", []))
            variants = operation_variants(url_lines)
            if not variants:
                continue
            query_parameters = parse_parameters(
                list_texts(grouped.get("query_filters", [])),
                location="query",
            )
            field_docs = parse_field_docs(grouped.get("field_docs", []))
            errors = list_texts(grouped.get("errors", []))
            examples = parse_examples(section_title, grouped)
            notes = intro_paragraphs + summary + list_texts(grouped.get("notes", []))
            security_area_values = list_texts(grouped.get("security_area", []))
            security_area = security_area_values[0] if security_area_values else None
            first_path = variants[0]["path_template"]
            for variant in variants:
                method_name = base_method_name(section_title, variant["method"])
                method_name = method_name + variant_suffix(first_path, variant["path_template"])
                method_name = unique_name(method_name, seen_operation_names)
                model_name = pascal_case(f"{source.category} {method_name} response")
                extra_lines = [line for line in url_lines if not PATH_LINE_PATTERN.match(line)]
                operation_category = category_for_operation(
                    source.category, section_title, variant["path_template"]
                )
                operation = ContractOperation(
                    operation_id=f"{operation_category}.{method_name}",
                    category=operation_category,
                    section_title=section_title,
                    python_name=method_name,
                    summary=summary[0] if summary else None,
                    source_key=source.key,
                    source_url=source.url,
                    method=variant["method"],  # type: ignore[arg-type]
                    path_template=variant["path_template"],
                    security_area=security_area,
                    side_effect=(
                        variant["method"] != "GET"
                        or "/commands/" in variant["path_template"].lower()
                    ),
                    response_kind=response_kind_from_examples(examples),  # type: ignore[arg-type]
                    response_model_name=model_name,
                    path_parameters=path_parameter_docs(
                        variant["path_template"], variant["description"], extra_lines
                    ),
                    query_parameters=query_parameters,
                    field_docs=field_docs,
                    notes=notes,
                    errors=errors,
                    examples=examples,
                )
                document.operations.append(apply_overrides(operation, overrides))
    if meta_source is not None and meta_html is not None:
        document.request_defaults = build_request_defaults(meta_source, meta_html)
    return document


def write_contract(document: ContractDocument) -> None:
    """Persist the normalized contract both in the repo and inside the package."""

    payload = json.loads(document.model_dump_json(indent=2))
    NORMALIZED_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    PACKAGED_CONTRACT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    """Entry point for syncing upstream docs into committed contract files."""

    document = build_contract()
    write_contract(document)
    print(
        f"Synced {len(document.sources)} sources and {len(document.operations)} operations "
        f"to {NORMALIZED_PATH.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
