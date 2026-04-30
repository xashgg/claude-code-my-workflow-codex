# AGENTS.md -- Academic Project Development With Codex

**Project:** [YOUR PROJECT NAME]
**Institution:** [YOUR INSTITUTION]
**Branch:** main

## Core Principles

- Plan first for non-trivial work; save durable plans to `quality_reports/plans/`.
- Verify after edits by compiling, rendering, testing, or running the relevant checker.
- Treat Beamer `.tex` as the source of truth when a Quarto `.qmd` mirror exists.
- Keep quality review honest: `/commit` can halt below threshold, but direct git commits bypass the workflow.
- Record durable lessons as `[LEARN:category]` entries in `MEMORY.md` only when they help future sessions.

## Repo Map

- `.codex/agents/`: specialized reviewer and worker profiles.
- `.codex/skills/`: reusable academic workflows.
- `.codex/rules/`: persistent working conventions.
- `.codex/references/`: journal and discipline calibration notes.
- `Slides/`: Beamer sources.
- `Quarto/`: RevealJS sources and theme.
- `Preambles/`: LaTeX headers and palette definitions.
- `scripts/`: utility checks and R pipeline templates.
- `quality_reports/`: plans, session logs, checkpoints, decisions, and merge reports.
- `templates/`: report and workflow templates.

## Commands

```bash
./scripts/validate-setup.sh
./scripts/check-palette-sync.sh
./scripts/check-surface-sync.sh
python scripts/quality_score.py Quarto/file.qmd
./scripts/sync_to_docs.sh LectureN
```

## Skills Quick Reference

Use the relevant `.codex/skills/*/SKILL.md` file when a task matches its name or description. Common entry points include `/compile-latex`, `/deploy`, `/review-paper`, `/review-r`, `/data-analysis`, `/audit-reproducibility`, `/validate-bib`, `/slide-excellence`, `/respond-to-referees`, `/checkpoint`, and `/preregister`.

## Quality Thresholds

| Score | Meaning |
| --- | --- |
| 80 | Good enough to save |
| 90 | Ready for deployment or PR review |
| 95 | Excellence target |

## Current Project State

| Artifact | Source | Mirror/Output | Notes |
| --- | --- | --- | --- |
| HelloWorld | `Slides/HelloWorld.tex` | `Quarto/HelloWorld.qmd` | Sample deck; delete when the project is initialized |
