# Building Commands
> Part of the [Plugin Development Guide](index.md).

Commands are the fastest way to extend Claude Code with repeatable workflows. A command turns a Markdown script into an executable action that users trigger with `/command-name`.

Use this guide to design, structure, and validate command files for Puerto plugins.

---

## Command Anatomy

Each command is a Markdown file inside `commands/`:

```
plugins/<your-plugin>/
└── commands/
    └── command-name.md
```

Puerto converts the contents into instructions for Claude Code. The recommended structure:

```markdown
# Short command title

One-line description that appears in Claude Code when users browse commands.

# Instructions

Step-by-step guidance written for Claude. Use ordered lists for clear sequencing.

# Best Practices (optional)

Additional rules, tips, or quality checks.
```

### Naming Guidelines

- File name matches the command slug (`commands/generate-sitemap.md` → `/generate-sitemap`).
- Use lowercase with hyphens.
- Start your Markdown with a human-readable title and description—Claude surfaces these in the UI.

---

## Writing Great Instructions

Focus on clarity, determinism, and context.

**1. Describe the trigger**
> “When the user runs `/generate-sitemap <path>`…”

**2. Define required inputs**
> “If `<path>` is missing, ask for the project root before continuing.”

**3. Outline the workflow**
Use numbered lists for sequential steps. Include code fences for commands Claude should run.

```markdown
1. Validate the path exists.
2. Run `tree` to map directories.
3. Generate sitemap.xml content.
4. Write the file and report the location.
```

**4. Handle decisions**
Provide conditional logic so Claude can adapt:

```markdown
- If the project already contains `sitemap.xml`, ask whether to overwrite.
- If the project uses Next.js, link to dynamic routing documentation.
```

**5. End with success criteria**
> “Confirm completion by showing the generated sitemap path and size.”

---

## Example Command

```markdown
# Interactive requirements brainstorming

Start an interactive Q&A session to build comprehensive requirements for a feature.

# Instructions

When the user runs `/brainstorm <name>`:

1. Validate the name parameter. If missing, prompt for a kebab-case requirement name.
2. Check `.requirements/<name>.md`. If it exists, ask whether to overwrite.
3. Guide the user through five sections: Overview, Functionality, Technical Context, Constraints, Success Criteria.
4. Save the answers to `.requirements/<name>.md` using the provided template.
5. Update `.requirements/_index.json` with timestamps.
6. Confirm completion and propose `/implement <name>` as the next step.

# Best Practices

- Ask follow-up questions when answers are vague.
- Suggest edge cases often missed for the selected domain.
- Provide examples if the user seems uncertain.
```

---

## Reusing Content with Skills

If multiple commands share domain knowledge—checklists, templates, standards—move the reusable guidance to a skill such as `skills/<name>/SKILL.md` and reference it from the command. See [Developing Skills](skills.md) for details.

---

## Testing Commands

1. Install your plugin locally (`/plugin install <name>@/path/to/plugin`).
2. Trigger the command in Claude Code.
3. Verify that:
   - Claude follows the steps as expected.
   - Prompts are clear and actionable.
   - Files are created/updated correctly.
   - Edge cases (missing inputs, existing files) behave as documented.

Document any special requirements in the plugin README so users know what to expect.

---

## Next Steps

- Add richer automation with [Agents](agents.md) or [MCP Servers](mcp-servers.md).
- Ensure the plugin passes validation: [Testing & Validation](testing-and-validation.md).
- Document your command in the plugin README with usage examples.
