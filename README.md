# Codex Academic Workflow

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Changelog](https://img.shields.io/badge/See-CHANGELOG-blue.svg)](CHANGELOG.md)

This repo is a Codexized version of Prof. Pedro Sant'Anna's [Claude Code workflow](https://github.com/pedrohcgs/claude-code-my-workflow). A ready-to-fork Codex workflow for academic work: lecture slides, Quarto mirrors, research papers, R analysis, replication checks, and structured review. The reusable instructions now live in `AGENTS.md` and `.codex/`.

## Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/codex-academic-workflow.git my-project
cd my-project
./scripts/validate-setup.sh
codex
```

Suggested first prompt:

> I am starting to work on [PROJECT NAME] in this repo. Read AGENTS.md and the relevant .codex workflow files, then help me adapt the placeholders for this project.

## What's Included

- `AGENTS.md`: Codex-native project instructions loaded at session start.
- `.codex/agents/`: 14 specialized reviewer and worker profiles.
- `.codex/skills/`: 29 reusable academic workflows.
- `.codex/rules/`: 24 path-scoped and always-on working conventions.
- `.codex/references/`: discipline and journal calibration references.
- `templates/`: reusable report, spec, and response templates.
- `scripts/`: setup, quality, palette, and documentation checks.

## Common Workflows

- Slide workflow: `/create-lecture Topic` -> `Slides/Lecture.tex` -> `/compile-latex Lecture` -> `Slides/Lecture.pdf` -> `/translate-to-quarto Lecture.tex` -> `Quarto/Lecture.qmd` -> `/deploy Lecture` -> `docs/slides/`.
- Beamer `.tex` files are the source of truth; Quarto `.qmd` files are RevealJS mirrors for web deployment.
- `/review-paper path/to/paper.tex`: review a manuscript.
- `./scripts/convert-review-pdf.sh quality_reports/report.md`: convert a Markdown review report to PDF.
- `./scripts/convert-review-pdf.ps1 quality_reports/report.md`: convert a Markdown review report to PDF on Windows PowerShell.
- `/data-analysis`: run an R analysis workflow.
- `/audit-reproducibility`: compare manuscript claims against analysis outputs.
- `/checkpoint topic`: save a handoff snapshot in `quality_reports/checkpoints/`.

## Prerequisites

| Tool | Required For |
| --- | --- |
| Codex CLI | AI-assisted workflow execution |
| git | Version control |
| Python 3 | Internal checker scripts |
| Pandoc | Markdown review report PDF export |
| XeLaTeX | Beamer compilation |
| Quarto | HTML slides and docs |
| R | Analysis templates |
| GitHub CLI | PR workflow |

## Adapting For Your Field

1. Update the project placeholders in `AGENTS.md`.
2. Customize `.codex/agents/domain-reviewer.md`.
3. Fill in `.codex/rules/knowledge-base-template.md`.
4. Keep `Preambles/header.tex` and `Quarto/theme-template.scss` color palettes synchronized.
5. Add field-specific standards to `.codex/rules/r-code-conventions.md` and related rules.

## Origin

This workflow was originally developed for Claude Code and has been converted to a Codex-native layout. The reusable academic patterns came from Pedro Sant'Anna's Econ 730: Causal Panel Data workflow at Emory University; the current repository removes Claude Code runtime configuration and keeps the academic agents, skills, rules, and templates in Codex-oriented form.

## License

MIT License. See [LICENSE](LICENSE).
