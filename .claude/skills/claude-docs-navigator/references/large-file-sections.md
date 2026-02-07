# Large File Section Maps

Section maps with line ranges for files over 600 lines. Use these to read
only the relevant section via offset and limit parameters.

## hooks.md (1,455 lines)

| Line | Section |
|-----:|:--------|
| 15 | Hook lifecycle |
| 126 | Configuration |
| 380 | Hook input and output |
| 546 | Hook events |
| 1196 | Prompt-based hooks |
| 1276 | Agent-based hooks |
| 1324 | Run hooks in the background |
| 1421 | Security considerations |
| 1441 | Debug hooks |

## changelog.md (1,423 lines)

> Note: This file may contain HTML instead of markdown if the fetcher
> encountered a redirect. Check the first few lines before grepping.
> If it's HTML, re-run `python3 fetch_claude_docs.py` to refresh.

No fixed sections — grep for a date or feature name:
```
Grep pattern="## 2026-02-06" path="docs/en/changelog.md" output_mode="content" -A=50
```

## mcp.md (1,198 lines)

| Line | Section |
|-----:|:--------|
| 217 | What you can do with MCP |
| 227 | Popular MCP servers |
| 245 | Installing MCP servers |
| 420 | MCP installation scopes |
| 530 | Practical examples |
| 588 | Authenticate with remote MCP servers |
| 682 | Add MCP servers from JSON configuration |
| 718 | Import MCP servers from Claude Desktop |
| 751 | Use Claude Code as an MCP server |
| 810 | MCP output limits and warnings |
| 836 | Use MCP resources |
| 877 | Scale with MCP Tool Search |
| 933 | Use MCP prompts as commands |
| 972 | Managed MCP configuration |

## settings.md (935 lines)

| Line | Section |
|-----:|:--------|
| 11 | Configuration scopes |
| 76 | Settings files |
| 410 | Subagent configuration |
| 419 | Plugin configuration |
| 735 | Environment variables |
| 830 | Tools available to Claude |
| 931 | See also |

## common-workflows.md (861 lines)

| Line | Section |
|-----:|:--------|
| 11 | Understand new codebases |
| 93 | Fix bugs efficiently |
| 127 | Refactor code |
| 167 | Use specialized subagents |
| 227 | Use Plan Mode for safe code analysis |
| 295 | Work with tests |
| 331 | Create pull requests |
| 369 | Handle documentation |
| 409 | Work with images |
| 469 | Reference files and directories |
| 510 | Use extended thinking (thinking mode) |
| 551 | Resume previous conversations |
| 643 | Run parallel sessions with Git worktrees |
| 714 | Use Claude as a unix-style utility |
| 799 | Ask Claude about its capabilities |
| 843 | Next steps |

## statusline.md (850 lines)

| Line | Section |
|-----:|:--------|
| 26 | Set up a status line |
| 69 | Build a status line step by step |
| 127 | How status lines work |
| 143 | Available data |
| 252 | Examples |
| 797 | Tips |
| 805 | Troubleshooting |

## sub-agents.md (786 lines)

| Line | Section |
|-----:|:--------|
| 27 | Built-in subagents |
| 77 | Quickstart: create your first subagent |
| 135 | Configure subagents |
| 465 | Work with subagents |
| 594 | Example subagents |
| 780 | Next steps |

## plugins-reference.md (741 lines)

Grep for section headings:
```
Grep pattern="^## " path="docs/en/plugins-reference.md" output_mode="content"
```
