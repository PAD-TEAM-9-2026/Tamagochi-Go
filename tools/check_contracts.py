#!/usr/bin/env python3
"""Check that README.md and docs/field-types.md stay consistent.

Verifies:
  - every relative link in README.md points at a file that exists
  - every PascalCase payload name referenced in a contract endpoint table
    in README.md has a matching "### Name" section in docs/field-types.md

Exit code is non-zero if any check fails.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "README.md"
FIELD_TYPES = REPO_ROOT / "docs" / "field-types.md"

# Words that look PascalCase but are not payload type names.
ALLOWLIST = {
    "Idempotency",
    "ETag",
    "WebSocket",
    "JSON",
    "HTTP",
    "JWT",
    "JWKS",
    "PostgreSQL",
    "PostGIS",
    "RabbitMQ",
    "Firebase",
    "GitHub",
    "ISO",
    "UUID",
    "Node",
    "Compose",
    "Two",
    "One",
    "Three",
    "Common",
    "Data",
    "Database",
    "Per",
    "Service",
    "Correlation",
    "Identifier",
    "Dead",
    "Letter",
    "Channel",
    "Competing",
    "Consumers",
    "Optimistic",
    "Offline",
    "Lock",
    "Transactional",
    "Outbox",
    "Consumer",
    "Gateway",
    "API",
    "If",
    "Match",
    "Key",
}

LINK_PATTERN = re.compile(r"\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^###\s+(\w+)\s*$", re.MULTILINE)
PASCAL_WORD = re.compile(r"\b[A-Z][a-zA-Z]*[a-z][a-zA-Z]*\b")

# Only these table columns hold payload type names; other tables in the
# contract section (conventions, events routing, etc.) use plain prose.
TYPE_COLUMNS = {"Request", "Successful response", "Response"}


def check_links(text: str) -> list[str]:
    errors = []
    for match in LINK_PATTERN.finditer(text):
        target = match.group(1).strip()
        if target.startswith(("http://", "https://", "#")):
            continue
        path = target.split("#", 1)[0]
        if not path:
            continue
        resolved = (REPO_ROOT / path).resolve()
        if not resolved.exists():
            errors.append(f"broken link: {target}")
    return errors


def extract_contract_section(text: str) -> str:
    start = text.find("## Communication contract")
    if start == -1:
        return ""
    end = text.find("\n## ", start + 1)
    return text[start:] if end == -1 else text[start:end]


def find_known_types(field_types_text: str) -> set[str]:
    return set(HEADING_PATTERN.findall(field_types_text))


def parse_table_rows(block: str) -> list[list[str]]:
    """Split a markdown table block into rows of trimmed cells, skipping
    the header separator row (the one made of --- cells)."""
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|") or not line.endswith("|"):
            continue
        cells = [cell.strip() for cell in line[1:-1].split("|")]
        if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows


def find_table_blocks(text: str) -> list[str]:
    """Group contiguous lines starting with '|' into table blocks."""
    blocks: list[str] = []
    current: list[str] = []
    for line in text.splitlines():
        if line.strip().startswith("|"):
            current.append(line)
        elif current:
            blocks.append("\n".join(current))
            current = []
    if current:
        blocks.append("\n".join(current))
    return blocks


def find_referenced_types(contract_text: str) -> set[str]:
    referenced: set[str] = set()
    for block in find_table_blocks(contract_text):
        rows = parse_table_rows(block)
        if len(rows) < 2:
            continue
        header, *body = rows
        type_col_indices = [i for i, name in enumerate(header) if name in TYPE_COLUMNS]
        if not type_col_indices:
            continue
        for row in body:
            for index in type_col_indices:
                if index >= len(row):
                    continue
                for word in PASCAL_WORD.findall(row[index]):
                    if word not in ALLOWLIST:
                        referenced.add(word)
    return referenced


def main() -> int:
    errors: list[str] = []

    if not README.exists():
        print("README.md is missing", file=sys.stderr)
        return 1
    if not FIELD_TYPES.exists():
        print("docs/field-types.md is missing", file=sys.stderr)
        return 1

    readme_text = README.read_text(encoding="utf-8")
    field_types_text = FIELD_TYPES.read_text(encoding="utf-8")

    errors.extend(check_links(readme_text))

    contract_text = extract_contract_section(readme_text)
    known_types = find_known_types(field_types_text)
    referenced_types = find_referenced_types(contract_text)
    missing = sorted(referenced_types - known_types)
    for name in missing:
        errors.append(
            f"README references payload '{name}' with no matching "
            f"'### {name}' section in docs/field-types.md"
        )

    if errors:
        print(f"check_contracts.py found {len(errors)} problem(s):\n", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(f"check_contracts.py: OK ({len(known_types)} payload types, no broken links)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
