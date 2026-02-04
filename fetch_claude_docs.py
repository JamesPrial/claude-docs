#!/usr/bin/env python3
"""Download Claude Code documentation for offline reference."""

import os
import re
import time
import urllib.request
import urllib.error

BASE_URL = "https://code.claude.com"
INDEX_URL = "https://code.claude.com/docs/llms.txt"
OUTPUT_DIR = "./docs"
DELAY = 0.5  # seconds between requests


def make_request(url):
    """Make HTTP request with proper headers."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; ClaudeDocsDownloader/1.0)"}
    )
    return urllib.request.urlopen(req)


def fetch_index():
    """Fetch llms.txt and extract doc paths."""
    try:
        with make_request(INDEX_URL) as response:
            content = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print(f"Error fetching index: {e}")
        return None

    # Extract URLs from markdown links like [Title](https://code.claude.com/docs/en/foo.md)
    pattern = r"\(https://code\.claude\.com(/docs/en/[^)]+\.md)\)"
    paths = re.findall(pattern, content)
    return paths


def download_doc(path):
    """Download a single markdown doc."""
    url = f"{BASE_URL}{path}"
    try:
        with make_request(url) as response:
            return response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print(f"  Warning: Failed to fetch {path}: {e}")
        return None


def save_doc(path, content):
    """Save content to local file, mirroring URL structure."""
    # path is like /docs/en/overview.md, save to ./docs/en/overview.md
    local_path = f".{path}"
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    with open(local_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    print("Fetching documentation index...")
    paths = fetch_index()

    if paths is None:
        print("Failed to fetch index. Exiting.")
        return 1

    if not paths:
        print("No documentation paths found in index.")
        return 1

    print(f"Found {len(paths)} docs to download\n")

    success = 0
    failed = 0

    for i, path in enumerate(paths, 1):
        print(f"[{i}/{len(paths)}] {path[1:]}", end=" ")  # strip leading /

        content = download_doc(path)
        if content:
            save_doc(path, content)
            print("✓")
            success += 1
        else:
            failed += 1

        if i < len(paths):
            time.sleep(DELAY)

    print(f"\nDone! Downloaded {success} files to {OUTPUT_DIR}/")
    if failed:
        print(f"Failed: {failed} files")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    exit(main())
