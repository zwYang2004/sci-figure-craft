#!/usr/bin/env python3
"""Render selected pages (default: pages 1-3) of a PDF paper to high-res PNGs
so an AI agent can visually inspect Figure 1 / architecture diagrams and extract
their layout, color palette, and visual hierarchy.

Usage:
    python extract_paper_figures.py paper.pdf --pages 1-3 --dpi 200 --out ./extracted_figs
"""

import argparse
from pathlib import Path


def parse_pages(spec: str, max_pages: int) -> list[int]:
    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            for p in range(int(start), int(end) + 1):
                if 1 <= p <= max_pages:
                    pages.add(p)
        elif part.isdigit():
            p = int(part)
            if 1 <= p <= max_pages:
                pages.add(p)
    return sorted(pages)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render PDF pages to PNG for figure style inspection.")
    parser.add_argument("pdf", type=Path, help="Path to the input PDF file.")
    parser.add_argument("--pages", default="1-3", help="1-indexed page numbers or ranges (e.g. '1-3,5').")
    parser.add_argument("--dpi", type=int, default=200, help="Output image DPI (default: 200).")
    parser.add_argument("--out", type=Path, default=Path("./extracted_figs"), help="Output directory.")
    args = parser.parse_args()

    try:
        import fitz  # PyMuPDF
    except ImportError as exc:
        raise SystemExit("PyMuPDF is required. Install it with: pip install pymupdf") from exc

    if not args.pdf.exists():
        raise SystemExit(f"PDF not found: {args.pdf}")

    args.out.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(args.pdf)
    selected = parse_pages(args.pages, len(doc))

    for page_num in selected:
        page = doc[page_num - 1]
        pix = page.get_pixmap(dpi=args.dpi)
        out_file = args.out / f"{args.pdf.stem}_page{page_num}.png"
        pix.save(out_file)
        print(f"Saved: {out_file}")


if __name__ == "__main__":
    main()
