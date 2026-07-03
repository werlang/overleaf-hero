from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF_DIR = ROOT / "project" / "papers"


def clean(text: str) -> str:
    """Normalize whitespace in extracted PDF text."""
    return re.sub(r"\s+", " ", text).strip()


def section(text: str, start: str, end: str | None = None) -> str:
    """Extract a section-like span using case-insensitive heading patterns."""
    start_pattern = re.compile(start, re.I)
    end_pattern = re.compile(end, re.I) if end else None
    start_match = start_pattern.search(text)
    if not start_match:
        return ""
    section_start = start_match.end()
    if end_pattern:
        end_match = end_pattern.search(text, section_start)
        if end_match:
            return clean(text[section_start:end_match.start()])
    return clean(text[section_start:])


def extract_info(text: str) -> dict[str, str]:
    """Extract coarse research-paper fields for literature triage."""
    lines = text.splitlines()
    return {
        "title": clean(lines[0]) if lines else "",
        "abstract": section(text, r"\babstract\b", r"\bkeywords\b|\bindex terms\b|\bintroduction\b"),
        "dataset": section(text, r"\bdataset\b|\bdata set\b|\bdatasets\b", r"\bmethod\b|\bmethodology\b|\bmaterials\b|\bexperimental\b"),
        "method": section(text, r"\bmethod\b|\bmethodology\b", r"\bexperiment\b|\bresults\b|\bevaluation\b"),
        "results": section(text, r"\bresults\b|\bevaluation\b|\bexperimental results\b", r"\bdiscussion\b|\bconclusion\b"),
    }


def parse_args() -> argparse.Namespace:
    """Parse the optional PDF directory path."""
    parser = argparse.ArgumentParser(description="Extract coarse method/result fields from local PDF papers.")
    parser.add_argument("--pdf-dir", default=str(DEFAULT_PDF_DIR), help="Directory containing PDF files.")
    return parser.parse_args()


def main() -> None:
    """Print coarse structured fields for local PDF triage."""
    args = parse_args()
    pdf_dir = Path(args.pdf_dir)
    if not pdf_dir.exists():
        print(f"PDF directory not found: {pdf_dir}")
        print("Pass --pdf-dir with the directory that contains the papers to inspect.")
        print("PDF triage only: no citation support was verified.")
        return

    print("PDF triage only: this output does not verify that a source supports a citation claim.")
    print("Use bibtex-verified-citations before citing any candidate in the TCC.")
    print()

    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if not pdfs:
        print(f"No PDF files found in: {pdf_dir}")
        return

    try:
        from pdfminer.high_level import extract_text
    except ModuleNotFoundError:
        print("Missing dependency: pdfminer.six")
        print("Install pdfminer.six or run this script in an environment that provides it.")
        return

    for pdf in pdfs:
        print(f"=== {pdf.name} ===")
        try:
            text = extract_text(str(pdf)) or ""
        except Exception as exc:
            print(f"ERROR extracting text: {exc}")
            print()
            continue
        info = extract_info(text)
        for key in ["title", "abstract", "dataset", "method", "results"]:
            value = info.get(key, "")
            if value:
                suffix = "..." if len(value) > 1500 else ""
                print(f"{key.upper()}: {value[:1500]}{suffix}")
        print()


if __name__ == "__main__":
    main()
