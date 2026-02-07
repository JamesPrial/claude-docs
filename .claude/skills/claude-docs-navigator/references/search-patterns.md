# Search Patterns

Pre-built Grep patterns for common queries. All paths are relative to repo root.

## Find which files discuss a topic

```
Grep pattern="your keyword" path="docs/en" output_mode="files_with_matches"
```

## List section headings in any file

```
Grep pattern="^## " path="docs/en/TARGET.md" output_mode="content"
```

## Find all CLI flags

```
Grep pattern="^\\| `--" path="docs/en/cli-reference.md" output_mode="content"
```

## Find a specific setting

```
Grep pattern="setting_name" path="docs/en/settings.md" output_mode="content" -C=3
```

## Find all environment variables

```
Grep pattern="^\\| `[A-Z_]+`" path="docs/en/settings.md" output_mode="content"
```

## Find hook event types

```
Grep pattern="^### " path="docs/en/hooks.md" output_mode="content"
```

## Search the changelog for a date or feature

```
Grep pattern="## 2026-02-06" path="docs/en/changelog.md" output_mode="content" -A=50
```

```
Grep pattern="feature name" path="docs/en/changelog.md" output_mode="content" -C=5
```

## Find code examples in a file

```
Grep pattern="^```" path="docs/en/TARGET.md" output_mode="content" -B=2
```

## Find frontmatter fields (skills, plugins)

```
Grep pattern="field-name" path="docs/en/skills.md" output_mode="content" -C=3
```
