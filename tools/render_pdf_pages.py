from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = ROOT / "tmp" / "pdfs"


def slugify_stem(stem: str) -> str:
    """Return a filesystem-friendly ASCII slug for generated render artifacts."""
    normalized = unicodedata.normalize("NFKD", stem).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", normalized)
    slug = re.sub(r"-{2,}", "-", slug).strip("-._")
    return slug.lower() or "pdf"


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for rendering one PDF page range to image files."""
    parser = argparse.ArgumentParser(description="Render PDF pages to PNG files with Poppler pdftoppm.")
    parser.add_argument("pdf", help="PDF file to render.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help=f"Output directory (default: {DEFAULT_OUTPUT_DIR}).")
    parser.add_argument("--prefix", help="Output filename prefix without extension.")
    parser.add_argument("--first", type=int, default=1, help="First page to render (default: 1).")
    parser.add_argument("--last", type=int, help="Last page to render (default: same as --first).")
    parser.add_argument("--dpi", type=int, default=150, help="Render resolution in DPI (default: 150).")
    parser.add_argument("--pdftoppm", help="Explicit path to the pdftoppm executable.")
    return parser.parse_args()


def resolve_pdftoppm(explicit_path: str | None) -> str:
    """Resolve the Poppler executable path from an explicit flag or PATH."""
    if explicit_path:
        return explicit_path
    found = shutil.which("pdftoppm")
    if found:
        return found
    raise SystemExit("pdftoppm not found. Install Poppler or pass --pdftoppm with the executable path.")


def validate_page_range(first: int, last: int, dpi: int) -> None:
    """Validate render bounds before invoking Poppler."""
    if first < 1:
        raise SystemExit("--first must be greater than zero.")
    if last < first:
        raise SystemExit("--last must be greater than or equal to --first.")
    if dpi < 1:
        raise SystemExit("--dpi must be greater than zero.")


def collect_generated_files(output_dir: Path, prefix: str) -> list[Path]:
    """Collect generated PNGs for the selected output prefix."""
    return sorted(output_dir.glob(f"{prefix}-*.png"))


def collect_mtimes(paths: list[Path]) -> dict[Path, int]:
    """Collect modification times so overwritten renders are still reported."""
    return {path: path.stat().st_mtime_ns for path in paths if path.exists()}


def main() -> None:
    """Render selected PDF pages for visual verification during review."""
    args = parse_args()
    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")

    first = args.first
    last = args.last if args.last is not None else first
    validate_page_range(first, last, args.dpi)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.prefix or f"{slugify_stem(pdf_path.stem)}-page"
    output_prefix = output_dir / prefix
    before = collect_mtimes(collect_generated_files(output_dir, prefix))

    command = [
        resolve_pdftoppm(args.pdftoppm),
        "-png",
        "-r",
        str(args.dpi),
        "-f",
        str(first),
        "-l",
        str(last),
        str(pdf_path),
        str(output_prefix),
    ]
    subprocess.run(command, check=True)

    generated = [
        path
        for path in collect_generated_files(output_dir, prefix)
        if path not in before or path.stat().st_mtime_ns != before[path]
    ]
    print(f"rendered_pages={last - first + 1}")
    for path in generated:
        print(path)


if __name__ == "__main__":
    main()
