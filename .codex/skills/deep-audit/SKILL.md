---
name: deep-audit
description: Run a repository-wide consistency audit for the Codex academic workflow. Checks docs, scripts, skill/rule references, count claims, and verification gaps.
argument-hint: "[optional scope]"
allowed-tools: ["Read", "Grep", "Glob", "Bash", "Write", "Edit", "Task"]
effort: high
---
# Deep Audit

Audit the repository for consistency after workflow changes.

## Scope

- Public docs: `README.md`, `AGENTS.md`, `guide/`, `docs/`, `TROUBLESHOOTING.md`.
- Codex workflow files: `.codex/agents/`, `.codex/skills/`, `.codex/rules/`, `.codex/references/`.
- Scripts and templates: `scripts/`, `templates/`, `.github/`.

## Checks

1. Run `./scripts/check-surface-sync.sh`.
2. Search for stale paths or deleted files.
3. Confirm every referenced skill, rule, agent, and template exists.
4. Check scripts touched by the change for obvious shell/Python failures.
5. Verify public docs describe the current workflow shape.

## Report

Write findings to `quality_reports/deep_audit/YYYY-MM-DD_audit.md` when the audit is substantial. Include severity, file path, issue, and recommended fix.
