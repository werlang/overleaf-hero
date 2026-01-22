from __future__ import annotations

from pathlib import Path
import re
from pdfminer.high_level import extract_text

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"


def extract_abstract(text: str) -> str:
    # Normalize whitespace
    t = re.sub(r"\s+", " ", text)
    # Common markers
    m = re.search(r"(?i)\babstract\b\s*[:\-]?\s*(.+?)(?:(?:\bkeywords\b)|(?:\bindex terms\b)|(?:\bintroduction\b)|\n\n)", t)
    if m:
        return m.group(1).strip()
    # Fallback: first 1200 chars
    return t[:1200].strip()


def extract_title(text: str) -> str:
    # Try first non-empty line from the first page
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return lines[0] if lines else ""


def main() -> None:
    pdfs = sorted(PAPERS.glob("*.pdf"))
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
