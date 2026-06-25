from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_TEX_GLOB = "project/**/*.tex"
DEFAULT_BIB_PATH = "project/references.bib"
DEFAULT_CHEATSHEET_PATH = "project/citation-cheatsheet.md"


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


def extract_cheatsheet_keys(cheatsheet_text: str) -> set[str]:
    """Extract keys from the first column of Markdown table rows."""
    keys: set[str] = set()
    for line in cheatsheet_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "---" in stripped:
            continue
        cells = [cell.strip().strip("`") for cell in stripped.strip("|").split("|")]
        if not cells or cells[0].lower() in {"bibtex key", "key", "chave"}:
            continue
        if re.fullmatch(r"[A-Za-z0-9:_-]+", cells[0]):
            keys.add(cells[0])
    return keys


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
    return parser.parse_args()


def main() -> None:
    """Report missing, unused, and not-yet-cheatsheeted citation keys."""
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    bib_path = root / args.bib
    cheatsheet_path = root / args.cheatsheet

    citations_by_file = collect_tex_citations(root, args.tex_glob)
    cite_keys = set().union(*citations_by_file.values()) if citations_by_file else set()

    if not bib_path.exists():
        raise SystemExit(f"BibTeX file not found: {bib_path.relative_to(root)}")

    bib_keys = extract_bib_keys(bib_path.read_text(encoding="utf-8", errors="ignore"))
    missing = sorted(cite_keys - bib_keys)
    extra = sorted(bib_keys - cite_keys)

    if cheatsheet_path.exists():
        cheatsheet_keys = extract_cheatsheet_keys(cheatsheet_path.read_text(encoding="utf-8", errors="ignore"))
        missing_cheatsheet = sorted(cite_keys - cheatsheet_keys)
    else:
        cheatsheet_keys = set()
        missing_cheatsheet = sorted(cite_keys)

    print(f"TeX glob: {args.tex_glob}")
    print(f"BibTeX file: {args.bib}")
    print(f"TeX files with citations: {len(citations_by_file)}")
    print(f"Citation keys in TeX: {len(cite_keys)}")
    print(f"Entries in BibTeX: {len(bib_keys)}")

    print(f"\nMissing BibTeX entries: {len(missing)}")
    for key in missing:
        print(f"  - {key}")

    print(f"\nUnused BibTeX entries: {len(extra)}")
    for key in extra[:30]:
        print(f"  - {key}")
    if len(extra) > 30:
        print(f"  ... {len(extra) - 30} more")

    print(f"\nCitation cheatsheet: {args.cheatsheet}")
    print(f"Keys in cheatsheet: {len(cheatsheet_keys)}")
    print(f"Cited keys missing from cheatsheet: {len(missing_cheatsheet)}")
    for key in missing_cheatsheet[:30]:
        print(f"  - {key}")
    if len(missing_cheatsheet) > 30:
        print(f"  ... {len(missing_cheatsheet) - 30} more")


if __name__ == "__main__":
    main()
