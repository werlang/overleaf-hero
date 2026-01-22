from __future__ import annotations

import re
from pathlib import Path


def extract_cite_keys(latex_text: str) -> set[str]:
    keys: set[str] = set()
    for match in re.finditer(r"\\\\cite\w*\{([^}]+)\}", latex_text):
        chunk = match.group(1)
        for key in chunk.split(","):
            key = key.strip()
            if key:
                keys.add(key)
    return keys


def extract_bib_keys(bib_text: str) -> set[str]:
    return set(re.findall(r"@\w+\{\s*([^,\s]+)\s*,", bib_text))


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    tex = (root / "paper.tex").read_text(encoding="utf-8", errors="ignore")
    bib = (root / "references.bib").read_text(encoding="utf-8", errors="ignore")

    cite_keys = extract_cite_keys(tex)
    bib_keys = extract_bib_keys(bib)

    missing = sorted(cite_keys - bib_keys)
    extra = sorted(bib_keys - cite_keys)

    print(f"Citations in paper.tex: {len(cite_keys)}")
    print(f"Entries in references.bib: {len(bib_keys)}")
    print(f"Missing bib entries: {len(missing)}")
    for key in missing:
        print(f"  - {key}")

    print(f"\nUnused bib entries: {len(extra)}")
    for key in extra[:30]:
        print(f"  - {key}")
    if len(extra) > 30:
        print(f"  ... {len(extra) - 30} more")


if __name__ == "__main__":
    main()
