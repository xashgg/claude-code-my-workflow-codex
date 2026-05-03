#!/usr/bin/env bash
# Convert a Markdown review report to PDF.
#
# Usage:
#   ./scripts/convert-review-pdf.sh quality_reports/report.md
#   ./scripts/convert-review-pdf.sh quality_reports/report.md -o quality_reports/report.pdf

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" 2>/dev/null && pwd)"
if [ -z "$SCRIPT_DIR" ] || [ ! -d "$SCRIPT_DIR" ]; then
    echo "convert-review-pdf.sh: cannot resolve script directory" >&2
    exit 2
fi

if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN="python"
else
    echo "convert-review-pdf.sh: Python 3 is required" >&2
    exit 1
fi

"$PYTHON_BIN" "$SCRIPT_DIR/convert-review-pdf.py" "$@"
