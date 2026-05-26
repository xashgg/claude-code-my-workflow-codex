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

> I am starting to work on [PROJECT NAME] in this repo. [Describe your project in 2–3 sentences — what you’re building, who it’s for, what tools you use (e.g., LaTeX/Beamer, R, Quarto).]
>
> I want our collaboration to be structured, precise, and rigorous — even if it takes more time. When creating visuals, everything must be polished and publication-ready. I don’t want to repeat myself, so our workflow should be smart about remembering decisions and learning from corrections.
>
>I’ve set up the Codex academic workflow (forked from pedrohcgs/claude-code-my-workflow). The configuration files are already in this repo (.codex/, AGENTS.md, templates, scripts). Please read them, understand the workflow, and then update all configuration files to fit my project — fill in placeholders in AGENTS.md, adjust rules if needed, and propose any customizations specific to my use case.
>
>After that, use the plan-first workflow for all non-trivial tasks. Once I approve a plan, switch to contractor mode — coordinate everything autonomously and only come back to me when there’s ambiguity or a decision to make. For our first few sessions, check in with me a bit more often so I can learn how the workflow operates.
>
>Enter plan mode and start by adapting the workflow configuration for this project.

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

## License

MIT License. See [LICENSE](LICENSE).
