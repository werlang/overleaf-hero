from __future__ import annotations

from pathlib import Path
import re
from pdfminer.high_level import extract_text

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def section(text: str, start: str, end: str | None = None) -> str:
    pat_start = re.compile(start, re.I)
    pat_end = re.compile(end, re.I) if end else None
    m = pat_start.search(text)
    if not m:
        return ""
    s = m.end()
    if pat_end:
        m2 = pat_end.search(text, s)
        if m2:
            return clean(text[s:m2.start()])
    return clean(text[s:])


def extract_info(text: str) -> dict:
    info = {}
    info["title"] = clean(text.splitlines()[0]) if text.splitlines() else ""
    info["abstract"] = section(text, r"\babstract\b", r"\bkeywords\b|\bindex terms\b|\bintroduction\b")
    info["dataset"] = section(text, r"\bdataset\b|\bdata set\b|\bdatasets\b", r"\bmethod\b|\bmethodology\b|\bmaterials\b|\bexperimental\b")
    info["method"] = section(text, r"\bmethod\b|\bmethodology\b", r"\bexperiment\b|\bresults\b|\bevaluation\b")
    info["results"] = section(text, r"\bresults\b|\bevaluation\b|\bexperimental results\b", r"\bdiscussion\b|\bconclusion\b")
    return info


def main() -> None:
    pdfs = sorted(PAPERS.glob("*.pdf"))
    for pdf in pdfs:
        print(f"=== {pdf.name} ===")
        text = extract_text(str(pdf)) or ""
        info = extract_info(text)
        for k in ["title", "abstract", "dataset", "method", "results"]:
            val = info.get(k, "")
            if val:
                print(f"{k.upper()}: {val[:1500]}{'...' if len(val) > 1500 else ''}")
        print()


if __name__ == "__main__":
    main()
