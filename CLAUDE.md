# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A tool for downloading Claude Code documentation from https://code.claude.com for offline reference. The downloaded markdown files are stored in `docs/en/`.

## Commands

```bash
# Download/refresh all Claude Code docs
python3 fetch_claude_docs.py
```

No dependencies required - uses Python standard library only.

## How It Works

The script fetches the documentation index from `https://code.claude.com/docs/llms.txt`, parses out all doc paths, then downloads each `.md` file. A User-Agent header is required or the server returns 403. Files are saved mirroring the URL structure (`/docs/en/overview.md` → `./docs/en/overview.md`).
