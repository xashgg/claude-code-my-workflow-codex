# Troubleshooting

## `codex` Not Found

Install the Codex CLI, then re-run `./scripts/validate-setup.sh`. If your executable has a different name, update `scripts/validate-setup.sh` for your environment.

## LaTeX Does Not Compile

Run the command from `Slides/` and make sure XeLaTeX can find `Preambles/header.tex`:

```bash
cd Slides
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode HelloWorld.tex
```

## Quarto Does Not Render

Check that Quarto is installed and that the source exists:

```bash
quarto --version
quarto render Quarto/HelloWorld.qmd
```

## Palette Drift

Run:

```bash
./scripts/check-palette-sync.sh
```

Keep color definitions synchronized between `Preambles/header.tex` and `Quarto/theme-template.scss`.

## Count Drift

Run:

```bash
./scripts/check-surface-sync.sh
```

The checker counts `.codex/agents`, `.codex/skills`, and `.codex/rules` and compares public documentation claims.

## Quality Score Fails

Run:

```bash
python scripts/quality_score.py path/to/file.qmd
```

Fix critical findings first, then rerun the checker.
