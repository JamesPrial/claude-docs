# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A tool for downloading Claude Code documentation from https://code.claude.com for offline reference. The downloaded markdown files are stored in `docs/en/`.

## Answering Questions About Claude Code

For any question about Claude Code features, configuration, plugins, hooks, MCP, sub-agents, skills, IDE integration, CI/CD, permissions, settings, troubleshooting, or any other Claude Code topic: **use the `claude-docs-navigator` skill**. It routes to the correct file(s) among the 55 docs in `docs/en/` using a topic table and reference files in `.claude/skills/claude-docs-navigator/references/`. Do not manually search the docs when this skill is available.

## Commands

```bash
# Download/refresh all Claude Code docs
python3 fetch_claude_docs.py

# Generate changelog entry (requires staged changes in docs/)
git add docs/ && python3 generate_changelog.py
```

No dependencies required - uses Python standard library only.

## Architecture

Two Python scripts, glued together by a GitHub Actions workflow:

**`fetch_claude_docs.py`** - Fetches the doc index from `https://code.claude.com/docs/llms.txt`, extracts paths via regex, downloads each `.md` file (User-Agent header required or 403), and saves to `docs/en/`. Transforms internal links so they work locally: `/en/slug` becomes `slug.md` and `/en/slug#anchor` becomes `slug.md#anchor` (handles both markdown `[]()` and HTML `href=""` formats).

**`generate_changelog.py`** - Reads staged diffs (`git diff --cached`) for files under `docs/`. Detects `## ` header additions/removals to report section-level changes (not just "file modified"). Extracts document titles from `# ` headers. Prepends a dated entry to `CHANGELOG.md`.

**`.github/workflows/update-docs.yml`** - Runs daily at midnight UTC. Sequence: fetch docs → `git add docs/` → if changes exist: generate changelog → stage changelog → commit → push. Only commits when docs actually changed. Pull before pushing—the workflow may have committed changes.
