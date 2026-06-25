from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF_DIR = ROOT / "project" / "papers"


def extract_abstract(text: str) -> str:
    """Extract an abstract-like segment from a paper text."""
    normalized = re.sub(r"\s+", " ", text)
    match = re.search(
        r"(?i)\babstract\b\s*[:\-]?\s*(.+?)(?:(?:\bkeywords\b)|(?:\bindex terms\b)|(?:\bintroduction\b)|\n\n)",
        normalized,
    )
    if match:
        return match.group(1).strip()
    return normalized[:1200].strip()


def extract_title(text: str) -> str:
    """Use the first non-empty text line as a conservative title guess."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return lines[0] if lines else ""


def parse_args() -> argparse.Namespace:
    """Parse the optional PDF directory path."""
    parser = argparse.ArgumentParser(description="Extract titles and abstracts from local PDF papers.")
    parser.add_argument("--pdf-dir", default=str(DEFAULT_PDF_DIR), help="Directory containing PDF files.")
    return parser.parse_args()


def main() -> None:
    """Print title and abstract candidates for every PDF in the chosen directory."""
    args = parse_args()
    pdf_dir = Path(args.pdf_dir)
    if not pdf_dir.exists():
        print(f"PDF directory not found: {pdf_dir}")
        print("Pass --pdf-dir with the directory that contains the papers to inspect.")
        return

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
        try:
            text = extract_text(str(pdf), maxpages=3) or ""
        except Exception as exc:
            print(f"=== {pdf.name} ===")
            print(f"ERROR extracting text: {exc}")
            print()
            continue
        title = extract_title(text)
        abstract = extract_abstract(text)
        print(f"=== {pdf.name} ===")
        print(f"TITLE: {title}")
        print(f"ABSTRACT: {abstract}")
        print()


if __name__ == "__main__":
    main()
