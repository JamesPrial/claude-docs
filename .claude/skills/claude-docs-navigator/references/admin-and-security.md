# Administration, Security, and Miscellaneous

## Security and Permissions

| File | Lines | Covers | When to read |
|:-----|------:|:-------|:-------------|
| `permissions.md` | 344 | Allow/deny rules, permission modes, tool rules | "How permissions work" |
| `security.md` | 155 | Security model, threat boundaries | Security architecture |
| `sandboxing.md` | 291 | Docker sandbox, macOS sandbox | "How to sandbox Claude Code" |

For permission questions, start with `permissions.md`. For sandbox setup,
read `sandboxing.md`. For the overall security model, read `security.md`.

## Monitoring and Costs

| File | Lines | Covers | When to read |
|:-----|------:|:-------|:-------------|
| `monitoring-usage.md` | 509 | Usage dashboards, tracking | "How to monitor usage" |
| `costs.md` | 263 | Pricing, cost management | "How much does it cost" |
| `analytics.md` | 216 | Analytics features | Usage analytics |
| `data-usage.md` | 199 | Data usage and privacy policies | "What data is collected" |

## Troubleshooting

| File | Lines | Covers | When to read |
|:-----|------:|:-------|:-------------|
| `troubleshooting.md` | 424 | Error messages, common fixes | Any error or problem |
| `legal-and-compliance.md` | 32 | Legal/compliance guidance | Compliance questions |

## Miscellaneous

| File | Lines | Covers | When to read |
|:-----|------:|:-------|:-------------|
| `memory.md` | 210 | CLAUDE.md files, project/user/enterprise memory | "How does CLAUDE.md work" |
| `checkpointing.md` | 56 | Undo/restore, checkpoint sessions | "How to undo changes" |
| `statusline.md` | 850 | Status line customization | "Customize status line". **LARGE** — see large-file-sections.md |
| `changelog.md` | 1,423 | Official Claude Code changelog | "What changed in version X". **LARGE** — grep for date or feature |

## Cross-cutting: permissions and security

For a full picture of security, read files in this order:
1. `permissions.md` — allow/deny rules and modes
2. `security.md` — overall security model
3. `sandboxing.md` — execution isolation
4. `settings.md` (section: "Tools available to Claude", line 830)
