# Claude Code Documentation Mirror

An automated mirror of the [Claude Code](https://claude.ai/code) documentation from [code.claude.com](https://code.claude.com).

## Why This Exists

This repository maintains an offline, searchable copy of Claude Code's documentation. A GitHub Actions workflow runs daily to fetch the latest docs and track changes in a detailed changelog.

## Usage

Browse the docs in [`docs/en/`](./docs/en/) or clone locally:

```bash
git clone https://github.com/JamesPrial/claude-docs.git
```

### Manual Refresh

```bash
python3 fetch_claude_docs.py
```

No dependencies required—uses Python standard library only.

## How It Works

1. **`fetch_claude_docs.py`** - Downloads all markdown files from the official docs
2. **`generate_changelog.py`** - Creates detailed changelog entries showing what changed (new sections, removed content, etc.)
3. **GitHub Actions** - Runs daily at midnight UTC, auto-commits any updates

Check [`CHANGELOG.md`](./CHANGELOG.md) to see documentation changes over time.

## Credits & Acknowledgments

**All documentation content belongs to [Anthropic](https://www.anthropic.com/).**

This is an unofficial mirror for convenience and offline access. The original documentation is available at [code.claude.com](https://code.claude.com).

Thank you to Anthropic for creating Claude Code and providing comprehensive, well-written documentation. Claude Code has genuinely changed how I work with code, and I'm grateful for the tool and the team behind it.

## License

The mirroring scripts in this repository are provided as-is. The documentation content is © Anthropic and subject to their terms of use.
