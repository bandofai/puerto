# Agent Frontmatter Reference
> Part of the [Reference](index.md).

Agent files (`agents/<name>.md`) start with YAML frontmatter that Claude Code uses to register capabilities. This reference lists every supported field and recommended conventions.

---

## Required Structure

```markdown
---
name: component-builder
description: Production-ready React/Vue/Svelte component builder
tools: Read, Write, Edit, Bash, Grep, Glob
model: haiku
triggers:
  - react component
  - vue component
timeout: 600
---

## Operating Guide
...
```

- Frontmatter must appear at the very top of the file.
- Use YAML format (two-dash `---` fence, key/value pairs, indent lists by two spaces).

---

## Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Agent identifier. Lowercase with hyphens. Should match filename. |
| `description` | string | ✅ | Short summary shown in Claude UI. |
| `tools` | comma-separated list | ✅ | Tooling Claude may use (`Read`, `Write`, `Edit`, `Execute`, `Bash`, `Search`, `Grep`, `Glob`, etc.). |
| `model` | string | ▫️ | Preferred Claude model (`haiku`, `sonnet`, `opus`). Defaults to active model if omitted. |
| `triggers` | string[] | ▫️ | Keywords/phrases used by Claude for auto-suggesting the agent. |
| `timeout` | number | ▫️ | Time budget in seconds. Helps Claude manage long-running tasks. |
| `confidence` | number | ▫️ | Optional hint (0–1) for how confident Claude should be before invoking automatically. |

Additional custom keys are discouraged—Claude ignores unknown fields.

---

## Tool Permissions

| Tool | Purpose |
|------|---------|
| `Read` | Read files from the project. |
| `Write` | Create files. |
| `Edit` | Modify existing files. |
| `Execute` / `Bash` | Run shell commands. |
| `Search` / `Grep` / `Glob` | Search codebase. |

Grant only the tools the agent actually needs. Limiting permissions improves safety and reduces accidental changes.

---

## Best Practices

- **Match filename + `name`**: pair `agents/design-auditor.md` with `name: design-auditor`.
- **Be descriptive**: `description` should explain what the agent does in plain language.
- **Call out models**: choose `haiku` for fast iterations, `sonnet` for balanced quality, `opus` for complex reasoning.
- **List triggers**: helps Claude auto-suggest the agent when relevant keywords appear in the conversation.
- **Keep frontmatter short**: save detailed instructions for the Markdown body.

---

## Validation Tips

- YAML must be valid—run through a YAML linter if unsure.
- Ensure tools listed exist; misspelled entries are ignored silently.
- Avoid duplicate agents with the same `name` across plugins. Namespaces are per plugin but clarity matters.
- Document agent behaviour thoroughly in the Markdown body. See [Building Agents](../plugin-development/agents.md).

---

## Related Docs

- [Directory Structure](directory-structure.md)
- [Command Format](command-format.md)
- [Skill Format](skill-format.md)
- [Testing & Validation](../plugin-development/testing-and-validation.md)
