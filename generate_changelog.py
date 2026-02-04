#!/usr/bin/env python3
"""Generate detailed changelog entries from staged git changes."""

import os
import re
import subprocess
from datetime import datetime


def run_git(args):
    """Run a git command and return stdout."""
    result = subprocess.run(
        ["git"] + args,
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout


def get_staged_changes():
    """Get dict of staged file changes: {filepath: status}."""
    output = run_git(["diff", "--cached", "--name-status"])
    changes = {}
    for line in output.strip().split("\n"):
        if not line:
            continue
        parts = line.split("\t")
        status = parts[0][0]  # A, M, D (ignore rename details)
        filepath = parts[-1]  # Use last part for renames
        if filepath.startswith("docs/"):
            changes[filepath] = status
    return changes


def get_file_diff(filepath):
    """Get the diff content for a staged file."""
    return run_git(["diff", "--cached", "--", filepath])


def parse_section_changes(diff):
    """Parse diff to find added/removed/modified sections.

    Returns dict with 'added', 'removed', 'modified' lists of section names.
    """
    added = []
    removed = []

    # Find all ## header changes in the diff
    for line in diff.split("\n"):
        # Added section header
        if line.startswith("+## ") and not line.startswith("+++"):
            section = line[4:].strip()
            added.append(section)
        # Removed section header
        elif line.startswith("-## ") and not line.startswith("---"):
            section = line[4:].strip()
            removed.append(section)

    # Sections that appear in both are "modified" (header text changed)
    # Sections only added are "new", only removed are "removed"
    modified = []
    final_added = []
    final_removed = []

    for section in added:
        if section in removed:
            modified.append(section)
            removed.remove(section)
        else:
            final_added.append(section)

    final_removed = removed

    # If there are changes but no section headers changed, note content was updated
    has_content_changes = "+" in diff or "-" in diff

    return {
        "added": final_added,
        "removed": final_removed,
        "modified": modified,
        "has_content_changes": has_content_changes
    }


def extract_title(filepath):
    """Extract the first # header from a file as its title."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("# "):
                    return line[2:].strip()
    except FileNotFoundError:
        pass
    return None


def generate_entry(changes):
    """Generate a changelog entry from the changes dict."""
    date = datetime.now().strftime("%Y-%m-%d")
    lines = [f"## {date}", ""]

    added_files = [(f, s) for f, s in changes.items() if s == "A"]
    modified_files = [(f, s) for f, s in changes.items() if s == "M"]
    removed_files = [(f, s) for f, s in changes.items() if s == "D"]

    if added_files:
        lines.append("### Added")
        for filepath, _ in sorted(added_files):
            title = extract_title(filepath)
            filename = os.path.basename(filepath)
            if title:
                lines.append(f"- `{filename}` - {title}")
            else:
                lines.append(f"- `{filename}`")
        lines.append("")

    if modified_files:
        lines.append("### Modified")
        for filepath, _ in sorted(modified_files):
            filename = os.path.basename(filepath)
            diff = get_file_diff(filepath)
            section_changes = parse_section_changes(diff)

            lines.append(f"- `{filename}`")

            for section in section_changes["added"]:
                lines.append(f"  - New section: \"{section}\"")
            for section in section_changes["removed"]:
                lines.append(f"  - Removed section: \"{section}\"")
            for section in section_changes["modified"]:
                lines.append(f"  - Updated section: \"{section}\"")

            # If no section-level changes but file was modified
            if (not section_changes["added"] and
                not section_changes["removed"] and
                not section_changes["modified"] and
                section_changes["has_content_changes"]):
                lines.append("  - Content updated")
        lines.append("")

    if removed_files:
        lines.append("### Removed")
        for filepath, _ in sorted(removed_files):
            filename = os.path.basename(filepath)
            lines.append(f"- `{filename}`")
        lines.append("")

    return "\n".join(lines)


def update_changelog(entry):
    """Prepend entry to CHANGELOG.md, creating it if needed."""
    changelog_path = "CHANGELOG.md"

    header = "# Changelog\n\nDocumentation updates from [Claude Code docs](https://code.claude.com).\n\n"

    if os.path.exists(changelog_path):
        with open(changelog_path, "r", encoding="utf-8") as f:
            existing = f.read()
        # Remove the header if present to avoid duplication
        if existing.startswith("# Changelog"):
            # Find where the first ## entry starts
            match = re.search(r"^## ", existing, re.MULTILINE)
            if match:
                existing = existing[match.start():]
            else:
                existing = ""
        content = header + entry + "\n" + existing
    else:
        content = header + entry

    with open(changelog_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    changes = get_staged_changes()

    if not changes:
        print("No staged changes in docs/ directory")
        return 0

    print(f"Found {len(changes)} changed file(s)")

    entry = generate_entry(changes)
    update_changelog(entry)

    print("Updated CHANGELOG.md")
    return 0


if __name__ == "__main__":
    exit(main())
