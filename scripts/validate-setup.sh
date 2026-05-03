#!/usr/bin/env bash
set -uo pipefail

pass=0
warn=0
fail=0

check_required() {
  local name="$1"
  local cmd="$2"
  local install_url="$3"
  if command -v "$cmd" >/dev/null 2>&1; then
    echo "[ok] $name: $($cmd --version 2>&1 | head -n1)"
    pass=$((pass + 1))
  else
    echo "[missing] $name: $install_url"
    fail=$((fail + 1))
  fi
}

check_optional() {
  local name="$1"
  local cmd="$2"
  local install_url="$3"
  if command -v "$cmd" >/dev/null 2>&1; then
    echo "[ok] $name: $($cmd --version 2>&1 | head -n1)"
    pass=$((pass + 1))
  else
    echo "[optional] $name: $install_url"
    warn=$((warn + 1))
  fi
}

echo "Validating Codex Academic Workflow setup..."
check_required "Codex CLI" "codex" "Install Codex for your platform"
check_required "git" "git" "https://git-scm.com/downloads"
check_required "Python 3" "python3" "https://python.org"
check_optional "Pandoc" "pandoc" "https://pandoc.org/installing.html"
check_optional "XeLaTeX" "xelatex" "https://tug.org/texlive/"
check_optional "Quarto" "quarto" "https://quarto.org/docs/get-started/"
check_optional "R" "R" "https://www.r-project.org/"
check_optional "GitHub CLI" "gh" "https://cli.github.com/"

echo "Summary: $pass passed, $warn optional missing, $fail required missing"
if [ "$fail" -gt 0 ]; then
  exit 1
fi
exit 0
