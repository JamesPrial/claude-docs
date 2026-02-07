---
name: claude-docs-navigator
description: >
  This skill should be used when the user asks about Claude Code features,
  configuration, plugins, hooks, MCP, sub-agents, skills, IDE integration,
  CI/CD, permissions, settings, troubleshooting, or any other Claude Code
  topic. Also use when the user says "check the docs", "what do the docs say",
  "how does Claude Code handle X", or asks how to set up or configure
  Claude Code. Navigates local documentation in docs/en/ to find answers.
---

# Claude Code Documentation Navigator

This repository contains 54 markdown files in `docs/en/` mirroring
https://code.claude.com. The docs update daily via GitHub Actions.
Use this skill to find the right file(s) for any Claude Code question.

## Topic routing

Find the user's topic below, then read the corresponding reference file
for the detailed file-by-file guide.

| Topic area | Reference file |
|:-----------|:---------------|
| Getting started, quickstart, setup, CLI, workflows, best practices | `references/core-features.md` |
| Settings, model config, keybindings, network, auth, output styles | `references/configuration.md` |
| Plugins, skills, hooks, MCP, sub-agents, agent teams | `references/extensibility.md` |
| VS Code, JetBrains, Chrome, desktop app, headless, web | `references/ide-and-platform.md` |
| GitHub Actions, GitLab CI/CD, Slack, Bedrock, Vertex, cloud | `references/cicd-and-cloud.md` |
| Permissions, security, monitoring, costs, troubleshooting | `references/admin-and-security.md` |

## Search strategy

### Small files (under 300 lines)

Read the entire file with the Read tool. Most docs are under 300 lines.

### Large files (over 600 lines)

Do not read these files whole. Instead:

1. Consult `references/large-file-sections.md` for the section map with
   line ranges.
2. Read only the relevant section using offset and limit parameters.
3. If the section heading is unknown, grep for it first:
   ```
   Grep pattern="^## " path="docs/en/TARGET.md" output_mode="content"
   ```

Large files in this repo:

| File | Lines |
|:-----|------:|
| hooks.md | 1,455 |
| changelog.md | 1,423 |
| mcp.md | 1,198 |
| settings.md | 935 |
| common-workflows.md | 861 |
| statusline.md | 850 |
| sub-agents.md | 786 |
| plugins-reference.md | 741 |

### Unknown topic

When no obvious file matches, search across all docs:

```
Grep pattern="keyword" path="docs/en" output_mode="files_with_matches"
```

Then read the most relevant match. For pre-built grep patterns, see
`references/search-patterns.md`.

## Utility references

| Reference file | Contents |
|:---------------|:---------|
| `references/large-file-sections.md` | Section maps with line ranges for files >600 lines |
| `references/search-patterns.md` | Pre-built Grep patterns for common queries |
