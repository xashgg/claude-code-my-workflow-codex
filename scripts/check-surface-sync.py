#!/usr/bin/env python3
"""Check public count claims against the .codex workflow surface."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GROUND_TRUTH = {
    "agents": len(list((REPO / ".codex/agents").glob("*.md"))),
    "skills": len(list((REPO / ".codex/skills").glob("*/SKILL.md"))),
    "rules": len(list((REPO / ".codex/rules").glob("*.md"))),
}
SURFACES = [
    REPO / "README.md",
    REPO / "AGENTS.md",
    REPO / "guide/workflow-guide.qmd",
    REPO / "docs/index.html",
    REPO / "docs/workflow-guide.html",
]
PATTERNS = [
    (r"(\d+)\s+agents?,\s+(\d+)\s+skills?,\s+and\s+(\d+)\s+rules?", ["agents", "skills", "rules"]),
    (r"(\d+)\s+agents?", ["agents"]),
    (r"(\d+)\s+skills?", ["skills"]),
    (r"(\d+)\s+rules?", ["rules"]),
]

def main() -> int:
    drift: list[str] = []
    for surface in SURFACES:
        if not surface.exists():
            drift.append(f"missing surface: {surface.relative_to(REPO)}")
            continue
        for lineno, line in enumerate(surface.read_text(encoding="utf-8").splitlines(), 1):
            for pattern, kinds in PATTERNS:
                for match in re.finditer(pattern, line):
                    for index, kind in enumerate(kinds, 1):
                        value = int(match.group(index))
                        if value != GROUND_TRUTH[kind]:
                            drift.append(
                                f"{surface.relative_to(REPO)}:{lineno} asserts {value} {kind}; actual {GROUND_TRUTH[kind]}"
                            )
    if drift:
        print("DRIFT DETECTED:", file=sys.stderr)
        print("\n".join(drift), file=sys.stderr)
        return 1
    print("Count assertions match .codex surface:")
    for key, value in GROUND_TRUTH.items():
        print(f"  {key}: {value}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
