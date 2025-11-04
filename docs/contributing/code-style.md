# Code Style Guide
> Part of the [Contributing Guide](index.md).

Puerto plugins span Markdown workflows, JSON manifests, and optional code templates. Follow this style guide to keep contributions consistent and easy to review.

---

## Naming Conventions

- **Plugins, folders, files:** `lowercase-with-hyphens`
- **Commands:** `/lowercase-with-hyphens`
- **Agents:** `lowercase-with-hyphens` in `agents/<name>.md`
- **Skills:** `skills/<slug>/SKILL.md` (slug uses lowercase hyphens)
- **Templates:** Mirror target file naming (`ComponentName.tsx`, `deployment.yaml`)

Avoid spaces, underscores, or camelCase in directory and file names.

---

## JSON Files

- Two-space indentation.
- Double quotes around keys and strings.
- No trailing commas.
- Keep objects sorted logically (required fields first, optional fields grouped).
- Include newline at end of file.

Example (`plugin.json`):

```json
{
  "name": "engineering",
  "version": "1.0.0",
  "description": "Frontend development specialist...",
  "author": {
    "name": "Puerto Plugin System"
  },
  "keywords": [
    "frontend",
    "react",
    "accessibility"
  ]
}
```

---

## Markdown Files

- Use `#` for the document title, `##` for sections, `###` for subsections.
- Prefer unordered lists (`-`) for bullet points; ordered lists for sequential steps.
- Wrap code in fenced blocks with language hints (` ```bash`, ` ```json`, etc.).
- Bold key instructions for agents/commands when steps are non-negotiable.
- Limit line length to ~100 characters for readability.

### Agents & Commands

- Agents require YAML frontmatter. See [Building Agents](../plugin-development/agents.md).
- Commands start with a title and a brief description before instructions.
- Highlight safety prompts (use bold text and uppercase when crucial).

### Skills

- Start with a concise summary and guiding principles.
- Use tables and code blocks to capture patterns.
- Keep sections scannable—skills are frequently read inline.

---

## Code Templates

- Follow language-specific best practices (Prettier/ESLint defaults for JS/TS, gofmt for Go, etc.).
- Include comments sparingly—focus on actionable guidance.
- Ensure placeholders are easy to spot (`{{PLACEHOLDER}}`, `TODO:`).
- Run formatters locally before committing templates.

---

## Command Snippets

- Use bash code blocks for CLI instructions.
- Include comments explaining optional steps or environment setup.
- Prefer relative paths so snippets work in any project.

Example:

```bash
# Validate plugin structure
node scripts/validate-plugin.js plugins/engineering
```

---

## Git Hygiene

- Avoid committing generated binaries or build artefacts.
- Keep diffs minimal—exclude editor backups or OS metadata.
- Run validation scripts before pushing.
- Squash or rebase to tidy commit history when requested by maintainers.

---

## Tooling

- Recommended editor settings: trim trailing whitespace, insert final newline.
- JSON formatting tools: `npx prettier --write '**/*.json'`.
- Markdown linting (optional): `npx markdownlint-cli docs/**/*.md`.

---

## Related Docs

- [Documentation Style Guide](documentation-style.md)
- [Testing & Validation](../plugin-development/testing-and-validation.md)
- [Best Practices](../plugin-development/best-practices.md)
