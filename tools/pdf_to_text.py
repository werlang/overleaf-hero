from __future__ import annotations

import argparse
import re
import unicodedata
from collections.abc import Callable
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = ROOT / "tmp" / "pdfs"
Extractor = Callable[[Path, int | None], list[str]]


def slugify_stem(stem: str) -> str:
    """Return a filesystem-friendly ASCII slug for generated PDF artifacts."""
    normalized = unicodedata.normalize("NFKD", stem).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", normalized)
    slug = re.sub(r"-{2,}", "-", slug).strip("-._")
    return slug.lower() or "pdf"


def extract_with_pdfplumber(pdf_path: Path, max_pages: int | None) -> list[str]:
    """Extract page text using pdfplumber, preserving a practical reading order."""
    try:
        import pdfplumber
    except ModuleNotFoundError as exc:
        raise RuntimeError("Missing dependency: pdfplumber") from exc

    pages: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        selected_pages = pdf.pages[:max_pages] if max_pages else pdf.pages
        for page in selected_pages:
            pages.append((page.extract_text(x_tolerance=1, y_tolerance=3) or "").strip())
    return pages


def extract_with_pypdf(pdf_path: Path, max_pages: int | None) -> list[str]:
    """Extract page text with pypdf as a lighter fallback when pdfplumber is unavailable."""
    try:
        from pypdf import PdfReader
    except ModuleNotFoundError as exc:
        raise RuntimeError("Missing dependency: pypdf") from exc

    reader = PdfReader(pdf_path)
    selected_pages = reader.pages[:max_pages] if max_pages else reader.pages
    return [(page.extract_text() or "").strip() for page in selected_pages]


def resolve_extractor(engine: str) -> Extractor:
    """Choose the requested extraction backend, preferring pdfplumber in auto mode."""
    if engine == "pdfplumber":
        return extract_with_pdfplumber
    if engine == "pypdf":
        return extract_with_pypdf

    def auto_extract(pdf_path: Path, max_pages: int | None) -> list[str]:
        """Try higher-fidelity extraction first, then fall back to pypdf."""
        errors: list[str] = []
        for extractor in (extract_with_pdfplumber, extract_with_pypdf):
            try:
                return extractor(pdf_path, max_pages)
            except RuntimeError as exc:
                errors.append(str(exc))
        raise RuntimeError("; ".join(errors))

    return auto_extract


def build_pages_text(pages: list[str]) -> str:
    """Format extracted text with page markers suitable for review evidence."""
    parts = []
    for index, text in enumerate(pages, start=1):
        parts.append(f"===== PAGE {index} =====\n\n{text}")
    return "\n\n".join(parts).strip() + "\n"


def build_full_text(pages: list[str]) -> str:
    """Format extracted text without page markers for continuous reading."""
    return "\n\n".join(page for page in pages if page).strip() + "\n"


def output_paths(args: argparse.Namespace, pdf_path: Path) -> tuple[Path, Path | None]:
    """Resolve generated output paths from CLI flags and the PDF stem."""
    output_dir = Path(args.output_dir)
    slug = slugify_stem(pdf_path.stem)
    pages_output = Path(args.pages_output) if args.pages_output else output_dir / f"{slug}-pages.txt"
    full_output = None if args.no_full else Path(args.full_output) if args.full_output else output_dir / f"{slug}-full.txt"
    return pages_output, full_output


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for converting a PDF into reviewable text files."""
    parser = argparse.ArgumentParser(description="Extract text from a PDF into page-marked and full text files.")
    parser.add_argument("pdf", help="PDF file to convert.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help=f"Default output directory (default: {DEFAULT_OUTPUT_DIR}).")
    parser.add_argument("--pages-output", help="Explicit page-marked text output path.")
    parser.add_argument("--full-output", help="Explicit continuous text output path.")
    parser.add_argument("--no-full", action="store_true", help="Only write the page-marked output file.")
    parser.add_argument("--max-pages", type=int, help="Extract only the first N pages.")
    parser.add_argument(
        "--engine",
        choices=("auto", "pdfplumber", "pypdf"),
        default="auto",
        help="Text extraction backend to use (default: auto).",
    )
    return parser.parse_args()


def main() -> None:
    """Convert a PDF to local text artifacts for academic review workflows."""
    args = parse_args()
    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")
    if args.max_pages is not None and args.max_pages < 1:
        raise SystemExit("--max-pages must be greater than zero.")

    extractor = resolve_extractor(args.engine)
    try:
        pages = extractor(pdf_path, args.max_pages)
    except RuntimeError as exc:
        raise SystemExit(
            f"{exc}\nInstall pdfplumber or pypdf, or run with the bundled Codex Python runtime when available."
        ) from exc

    pages_output, full_output = output_paths(args, pdf_path)
    pages_output.parent.mkdir(parents=True, exist_ok=True)
    pages_output.write_text(build_pages_text(pages), encoding="utf-8")

    if full_output:
        full_output.parent.mkdir(parents=True, exist_ok=True)
        full_output.write_text(build_full_text(pages), encoding="utf-8")

    print(f"pages={len(pages)}")
    print(f"chars={sum(len(page) for page in pages)}")
    print(f"pages_output={pages_output}")
    if full_output:
        print(f"full_output={full_output}")


if __name__ == "__main__":
    main()
