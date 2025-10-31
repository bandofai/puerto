# Command File Format
> Part of the [Reference](index.md).

Commands live in `commands/<command>.md` and describe deterministic workflows Claude should execute when users run `/command-name`. This reference documents the expected structure and conventions.

---

## File Layout

```
plugins/<plugin-name>/
└── commands/
    ├── brainstorm.md
    └── req-list.md
```

Each command file is Markdown. A common template:

```markdown
# Short, imperative title

One-line description displayed in the Claude UI.

# Instructions

When the user runs `/command-name [options]`:

1. Validate inputs and gather missing context.
2. Perform the core workflow (use numbered steps).
3. Add conditional branches for edge cases.
4. Save or modify files as needed.
5. Report results back to the user.

# Best Practices

- Optional callouts, safety checks, or follow-up tasks.
```

Sections beyond `# Instructions` are flexible—use additional headings for checklists, templates, or troubleshooting guidance.

---

## Naming Conventions

- File name = command slug. For example, `commands/generate-sitemap.md` maps to `/generate-sitemap`.
- Slugs must be lowercase with hyphens.
- Use imperative language (`Generate`, `Audit`, `Sync`) for titles and instructions.

---

## Instruction Patterns

| Pattern | Example |
|---------|---------|
| Input validation | “If `<path>` is missing, ask the user to provide a repository-relative path.” |
| Conditional logic | “If `sitemap.xml` exists, ask whether to overwrite before proceeding.” |
| Shell execution | ``` ```bash<br/>npm run lint<br/>``` ``` |
| File operations | “Create `.requirements/<name>.md` using the template below.” |
| Reporting | “Summarise changes and suggest `/implement <name>` as the next step.” |

Use bold text for non-negotiable rules (`**Never overwrite files without confirmation.**`).

---

## Templates & Snippets

Embed reusable code or document structures using fenced code blocks:

```markdown
```markdown
# Requirement Template
**Created:** {{DATE}}
**Status:** draft
...
```
```

Claude will copy these verbatim when executing the command.

---

## Linking to Skills & Templates

- Reference skills for domain knowledge. Example: “Read `skills/component-development/SKILL.md` before writing code.”
- Mention template files. Example: “Copy `templates/api-spec-template.md` into the project.”

Cross-linking keeps commands concise and makes maintenance easier.

---

## Testing Checklist

- [ ] Command slug matches file name.
- [ ] Instructions cover happy path and error handling.
- [ ] File paths exist or will be created.
- [ ] Shell commands succeed in a clean project.
- [ ] README includes usage examples and prerequisites.

Test commands locally by installing the plugin (`/plugin install name@/path/to/plugin`) and triggering `/command-name`.

---

## Related Docs

- [Building Commands](../plugin-development/commands.md)
- [Skill Format](skill-format.md)
- [Agent Frontmatter](agent-frontmatter.md)
- [Validation Rules](validation-rules.md)
