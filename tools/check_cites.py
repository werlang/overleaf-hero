from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


DEFAULT_TEX_GLOB = "project/**/*.tex"
DEFAULT_BIB_PATH = "project/references.bib"
DEFAULT_CHEATSHEET_PATH = "project/citation-cheatsheet.md"
REQUIRED_CHEATSHEET_COLUMNS = {
    "bibtex key",
    "status",
    "claim supported",
    "evidence summary",
    "source url",
    "accessed at",
    "used in",
}


@dataclass(frozen=True)
class CitationOccurrence:
    """A single citation key occurrence in a TeX source file."""

    path: Path
    line_number: int
    key: str
    line_text: str


@dataclass(frozen=True)
class CheatsheetRow:
    """Normalized citation-cheatsheet evidence for one BibTeX key."""

    key: str
    status: str
    claim_supported: str
    evidence_summary: str
    source_url: str
    accessed_at: str
    used_in: str


@dataclass(frozen=True)
class CheatsheetParseResult:
    """Parsed cheatsheet rows plus structural validation errors."""

    rows: dict[str, CheatsheetRow]
    errors: list[str]


def extract_cite_keys(latex_text: str) -> set[str]:
    """Extract BibTeX keys from common LaTeX citation commands."""
    keys: set[str] = set()

    for match in re.finditer(r"\\cite\w*\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]+)\}", latex_text):
        keys.update(split_cite_chunk(match.group(1)))

    # The local template defines \apud{orig}{p1}{consulted}{p2}; only args 1 and 3
    # are BibTeX keys.
    for match in re.finditer(r"\\apud\s*\{([^}]+)\}\s*\{[^}]*\}\s*\{([^}]+)\}", latex_text):
        for key in (match.group(1).strip(), match.group(2).strip()):
            if key and not key.startswith("#"):
                keys.add(key)

    return {key for key in keys if key}


def split_cite_chunk(chunk: str) -> set[str]:
    """Split a comma-separated citation argument into normalized keys."""
    return {key.strip() for key in chunk.split(",") if key.strip() and not key.strip().startswith("#")}


def extract_bib_keys(bib_text: str) -> set[str]:
    """Extract BibTeX entry keys from a .bib file."""
    return set(re.findall(r"@\w+\{\s*([^,\s]+)\s*,", bib_text))


def normalize_cell(cell: str) -> str:
    """Normalize a Markdown table cell for structural comparison."""
    return cell.strip().strip("`")


def split_markdown_row(line: str) -> list[str]:
    """Split a simple Markdown table row into normalized cell values."""
    return [normalize_cell(cell) for cell in line.strip().strip("|").split("|")]


def is_separator_row(cells: list[str]) -> bool:
    """Return whether a Markdown row is a header separator."""
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells if cell.strip())


def parse_cheatsheet(cheatsheet_text: str) -> CheatsheetParseResult:
    """Parse required citation-cheatsheet evidence rows by BibTeX key."""
    rows: dict[str, CheatsheetRow] = {}
    errors: list[str] = []
    headers: list[str] | None = None

    for line_number, line in enumerate(cheatsheet_text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = split_markdown_row(stripped)
        if is_separator_row(cells):
            continue
        lowered = [cell.lower() for cell in cells]
        if "bibtex key" in lowered:
            headers = lowered
            missing_columns = sorted(REQUIRED_CHEATSHEET_COLUMNS - set(headers))
            if missing_columns:
                errors.append(f"line {line_number}: missing cheatsheet columns: {', '.join(missing_columns)}")
            continue
        if not headers or len(cells) < len(headers):
            continue

        row = dict(zip(headers, cells))
        key = row.get("bibtex key", "").strip()
        if not re.fullmatch(r"[A-Za-z0-9:_-]+", key):
            continue
        rows[key] = CheatsheetRow(
            key=key,
            status=row.get("status", "").strip(),
            claim_supported=row.get("claim supported", "").strip(),
            evidence_summary=row.get("evidence summary", "").strip(),
            source_url=row.get("source url", "").strip(),
            accessed_at=row.get("accessed at", "").strip(),
            used_in=row.get("used in", "").strip(),
        )

    if rows and not headers:
        errors.append("cheatsheet table header not found")
    return CheatsheetParseResult(rows=rows, errors=errors)


def validate_cheatsheet_row(row: CheatsheetRow) -> list[str]:
    """Return validation errors for evidence required by an active citation."""
    errors: list[str] = []
    if row.status != "Supported":
        errors.append(f"status is {row.status or 'empty'}, expected Supported")
    if not row.claim_supported:
        errors.append("claim supported is empty")
    if not row.evidence_summary:
        errors.append("evidence summary is empty")
    if not row.source_url:
        errors.append("source URL is empty")
    if not row.accessed_at:
        errors.append("accessed-at date is empty")
    if not row.used_in:
        errors.append("used-in path is empty")
    return errors


def extract_line_citations(latex_line: str) -> set[str]:
    """Extract BibTeX keys from citation commands in one LaTeX line."""
    return extract_cite_keys(latex_line)


def collect_tex_citations(root: Path, tex_glob: str) -> dict[Path, set[str]]:
    """Collect citation keys by TeX file using a repository-relative glob."""
    citations: dict[Path, set[str]] = {}
    for tex_path in sorted(root.glob(tex_glob)):
        if not tex_path.is_file():
            continue
        text = tex_path.read_text(encoding="utf-8", errors="ignore")
        keys = extract_cite_keys(text)
        if keys:
            citations[tex_path] = keys
    return citations


def collect_citation_occurrences(root: Path, tex_glob: str) -> list[CitationOccurrence]:
    """Collect citation keys with file and line evidence for diagnostics."""
    occurrences: list[CitationOccurrence] = []
    for tex_path in sorted(root.glob(tex_glob)):
        if not tex_path.is_file():
            continue
        text = tex_path.read_text(encoding="utf-8", errors="ignore")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for key in sorted(extract_line_citations(line)):
                occurrences.append(
                    CitationOccurrence(
                        path=tex_path,
                        line_number=line_number,
                        key=key,
                        line_text=line.strip(),
                    )
                )
    return occurrences


def parse_args() -> argparse.Namespace:
    """Parse command-line paths while keeping project/ as the default target."""
    parser = argparse.ArgumentParser(description="Check LaTeX citations against BibTeX and the citation cheatsheet.")
    parser.add_argument("--tex-glob", default=DEFAULT_TEX_GLOB, help=f"TeX glob relative to repo root (default: {DEFAULT_TEX_GLOB})")
    parser.add_argument("--bib", default=DEFAULT_BIB_PATH, help=f"BibTeX file relative to repo root (default: {DEFAULT_BIB_PATH})")
    parser.add_argument(
        "--cheatsheet",
        default=DEFAULT_CHEATSHEET_PATH,
        help=f"Citation cheatsheet path relative to repo root (default: {DEFAULT_CHEATSHEET_PATH})",
    )
    parser.add_argument(
        "--strict-unused",
        action="store_true",
        help="Fail when BibTeX entries are present but not cited.",
    )
    return parser.parse_args()


def main() -> None:
    """Report missing, unused, and not-yet-supported citation evidence."""
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    bib_path = root / args.bib
    cheatsheet_path = root / args.cheatsheet

    tex_files = sorted(path for path in root.glob(args.tex_glob) if path.is_file())
    occurrences = collect_citation_occurrences(root, args.tex_glob)
    citations_by_file = collect_tex_citations(root, args.tex_glob)
    cite_keys = set().union(*citations_by_file.values()) if citations_by_file else set()

    print(f"TeX glob: {args.tex_glob}")
    print(f"BibTeX file: {args.bib}")
    print(f"TeX files found: {len(tex_files)}")
    print(f"TeX files with citations: {len(citations_by_file)}")
    print(f"Citation occurrences in TeX: {len(occurrences)}")
    print(f"Citation keys in TeX: {len(cite_keys)}")

    if not tex_files and not bib_path.exists():
        print("\nProject is not initialized: no TeX files or BibTeX file found under the configured project paths.")
        print("Nothing to check. Add the active TCC to project/ before running citation validation.")
        return

    if not bib_path.exists() and not cite_keys:
        print("\nNo citation keys found and no BibTeX file exists.")
        print("Nothing to check until the project contains cited sources.")
        return

    if not bib_path.exists():
        print("\nCitation occurrences:")
        for occurrence in occurrences:
            rel_path = occurrence.path.relative_to(root)
            print(f"  - {rel_path}:{occurrence.line_number}: {occurrence.key}")
        raise SystemExit(f"BibTeX file not found: {bib_path.relative_to(root)}")

    bib_keys = extract_bib_keys(bib_path.read_text(encoding="utf-8", errors="ignore"))
    missing = sorted(cite_keys - bib_keys)
    extra = sorted(bib_keys - cite_keys)

    if cheatsheet_path.exists():
        cheatsheet = parse_cheatsheet(cheatsheet_path.read_text(encoding="utf-8", errors="ignore"))
    else:
        cheatsheet = CheatsheetParseResult(rows={}, errors=["citation cheatsheet not found"])

    print(f"Entries in BibTeX: {len(bib_keys)}")

    print("\nCitation occurrences:")
    for occurrence in occurrences:
        rel_path = occurrence.path.relative_to(root)
        print(f"  - {rel_path}:{occurrence.line_number}: {occurrence.key}")

    print(f"\nMissing BibTeX entries: {len(missing)}")
    for key in missing:
        print(f"  - {key}")

    print(f"\nUnused BibTeX entries: {len(extra)}")
    for key in extra[:30]:
        print(f"  - {key}")
    if len(extra) > 30:
        print(f"  ... {len(extra) - 30} more")

    print(f"\nCitation cheatsheet: {args.cheatsheet}")
    print(f"Keys in cheatsheet: {len(cheatsheet.rows)}")
    print(f"Cheatsheet structure errors: {len(cheatsheet.errors)}")
    for error in cheatsheet.errors:
        print(f"  - {error}")

    missing_cheatsheet = sorted(cite_keys - set(cheatsheet.rows))
    print(f"Cited keys missing from cheatsheet: {len(missing_cheatsheet)}")
    for key in missing_cheatsheet[:30]:
        print(f"  - {key}")
    if len(missing_cheatsheet) > 30:
        print(f"  ... {len(missing_cheatsheet) - 30} more")

    invalid_cheatsheet: dict[str, list[str]] = {}
    for key in sorted(cite_keys & set(cheatsheet.rows)):
        row_errors = validate_cheatsheet_row(cheatsheet.rows[key])
        if row_errors:
            invalid_cheatsheet[key] = row_errors

    print(f"\nCited keys with invalid cheatsheet evidence: {len(invalid_cheatsheet)}")
    for key, row_errors in invalid_cheatsheet.items():
        print(f"  - {key}: {'; '.join(row_errors)}")

    has_blocking_errors = bool(missing or missing_cheatsheet or invalid_cheatsheet)
    has_blocking_errors = has_blocking_errors or bool(cheatsheet.errors and cite_keys)
    if args.strict_unused and extra:
        has_blocking_errors = True

    if has_blocking_errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
