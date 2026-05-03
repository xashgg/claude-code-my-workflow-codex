#!/usr/bin/env python3
"""Convert a Markdown review report to PDF with Pandoc/XeLaTeX.

Usage:
    python scripts/convert-review-pdf.py quality_reports/report.md
    python scripts/convert-review-pdf.py quality_reports/report.md -o out.pdf
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


DEFAULT_CJK_FONTS = [
    "Microsoft YaHei",
    "SimSun",
    "Noto Sans CJK SC",
    "Source Han Sans SC",
    "Arial Unicode MS",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a Markdown review report to PDF using pandoc and xelatex."
    )
    parser.add_argument("input", type=Path, help="Path to the .md review report.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output PDF path. Defaults to the input path with .pdf extension.",
    )
    parser.add_argument(
        "--font",
        default=None,
        help="CJK-capable font to pass to XeLaTeX. Defaults to an installed common font.",
    )
    parser.add_argument(
        "--margin",
        default="1in",
        help="PDF page margin passed to pandoc geometry. Default: 1in.",
    )
    return parser.parse_args()


def require_tool(name: str) -> None:
    if shutil.which(name) is None:
        raise SystemExit(f"Error: required tool not found on PATH: {name}")


def font_exists(font_name: str) -> bool:
    if shutil.which("fc-match") is None:
        # Windows TeX installs often lack fc-match, so let XeLaTeX try it.
        return True
    result = subprocess.run(
        ["fc-match", font_name],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0 and result.stdout.strip() != ""


def choose_font(requested: str | None) -> str:
    if requested:
        return requested
    for font in DEFAULT_CJK_FONTS:
        if font_exists(font):
            return font
    return DEFAULT_CJK_FONTS[0]


def main() -> int:
    args = parse_args()
    input_path = args.input
    output_path = args.output or input_path.with_suffix(".pdf")

    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 1
    if input_path.suffix.lower() != ".md":
        print(f"Error: expected a .md input file, got: {input_path}", file=sys.stderr)
        return 1

    require_tool("pandoc")
    require_tool("xelatex")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    font = choose_font(args.font)
    command = [
        "pandoc",
        str(input_path),
        "-o",
        str(output_path),
        "--pdf-engine=xelatex",
        "-V",
        f"CJKmainfont={font}",
        "-V",
        f"geometry:margin={args.margin}",
        "-V",
        "colorlinks=true",
    ]

    print(f"Converting {input_path} -> {output_path}")
    print(f"Using CJK font: {font}")
    subprocess.run(command, check=True)
    print(f"PDF written: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
