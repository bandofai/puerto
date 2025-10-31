# Skill File Format
> Part of the [Reference](index.md).

Skills capture reusable knowledge that agents and commands rely on. They live under `skills/<slug>/SKILL.md` and should be written for quick scanning.

---

## Directory Layout

```
plugins/<plugin-name>/
└── skills/
    ├── component-development/
    │   └── SKILL.md
    └── accessibility-standards/
        ├── SKILL.md
        └── resources.md   # optional supporting files
```

Reference skills in `plugin.json` using the directory name:

```json
{
  "skills": ["component-development", "responsive-design"]
}
```

---

## Recommended Structure

```markdown
# Skill Title

**One-sentence summary describing what the skill covers.**

---

## Core Principles

1. Guiding principle
2. Guiding principle

## Patterns & Playbooks

- Pattern explanation with code blocks or tables.
- Decision trees or heuristics.

## Checklists

- [ ] Step-by-step validation list.

## Reference

- External links or additional notes.
```

Feel free to add more sections (e.g., Glossary, Templates) as needed.

---

## Writing Guidelines

- Target 200–800 lines: long enough to be thorough, short enough to scan.
- Use headings, bullets, and tables; avoid dense paragraphs.
- Highlight critical rules with bold text or callouts.
- Embed copy-ready snippets (code, commands, templates) when helpful.
- Keep tone directive (“Do X before Y”) to drive consistent behaviour.

---

## Pairing with Automation

- **Agents** should explicitly read relevant skills before taking action.
- **Commands** can reference skills to provide context or checklists.
- **Templates** complement skills by providing ready-made file scaffolds.

Document these relationships in the plugin README so users know how the pieces connect.

---

## Validation Checklist

- [ ] Folder named with lowercase hyphenated slug.
- [ ] `SKILL.md` exists and follows Markdown guidelines.
- [ ] Links to templates or external resources are valid.
- [ ] Content reflects current best practices; update when patterns evolve.
- [ ] Agents and commands referencing the skill exist (or instructions clarify optional usage).

---

## Related Docs

- [Developing Skills](../plugin-development/skills.md)
- [Agent Frontmatter](agent-frontmatter.md)
- [Command Format](command-format.md)
- [Validation Rules](validation-rules.md)
