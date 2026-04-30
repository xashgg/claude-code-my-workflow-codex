---
name: context-status
description: Summarize the current repository and session handoff state. Use when the user asks "where are we", "status", "what changed", or "what should I do next".
argument-hint: ""
allowed-tools: ["Read", "Grep", "Glob", "Bash"]
---
# Context Status

Summarize current work without making changes.

## Steps

1. Run `git status --short` and `git branch --show-current`.
2. Read the most recent files in `quality_reports/plans/`, `quality_reports/session_logs/`, and `quality_reports/checkpoints/` if present.
3. Report current branch, changed files, active plan, known blockers, and next 1-3 actions.
