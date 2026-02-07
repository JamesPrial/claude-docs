# Configuration

Files covering settings, model selection, and environment setup.

| File | Lines | Covers | When to read |
|:-----|------:|:-------|:-------------|
| `settings.md` | 935 | All settings: scopes, files, env vars, tool permissions | Any settings question. **LARGE** — see large-file-sections.md |
| `model-config.md` | 142 | Model selection, custom models, thinking budget | "Which model", "how to change model" |
| `keybindings.md` | 277 | Keyboard shortcut customization | "Rebind keys", "custom shortcuts" |
| `terminal-config.md` | 66 | tmux, screen, font setup | Terminal display issues |
| `network-config.md` | 63 | Proxy, TLS, firewall, certificates | Network/connectivity issues |
| `authentication.md` | 83 | OAuth, API keys, login methods | "How to log in", API key setup |
| `output-styles.md` | 82 | Markdown, JSON, streaming output formats | "Change output format" |

## Cross-cutting: environment variables

Environment variables are primarily documented in `settings.md` (line 735,
"Environment variables" section). Also check:
- `model-config.md` for CLAUDE_MODEL
- `network-config.md` for proxy-related env vars
- `authentication.md` for ANTHROPIC_API_KEY
