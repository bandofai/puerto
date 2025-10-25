# Developing Skills
> Part of the [Plugin Development Guide](index.md).

Skills capture reusable knowledge—checklists, standards, patterns—that agents and commands can reference before doing work. Think of them as lightweight playbooks stored in your plugin.

---

## Directory Layout

```
plugins/<your-plugin>/
└── skills/
    ├── component-development/
    │   └── SKILL.md
    └── accessibility-standards/
        ├── SKILL.md
        └── reference-links.md
```

Each skill lives in its own folder and must include a `SKILL.md` file. Supporting assets (cheat-sheets, templates, data files) can sit alongside it.

In `plugin.json`, reference the skill by the folder name:

```json
{
  "skills": [
    "component-development",
    "responsive-design"
  ]
}
```

---

## Content Structure

Skills are Markdown documents written for humans **and** Claude. Use them to encode best practices you want enforced consistently.

Recommended template:

```markdown
# Skill Title

**One-sentence summary** describing what the skill covers.

---

## Core Principles

1. Guiding rule
2. Guiding rule

## Key Patterns

- Pattern explanation with code snippets
- Decision tables or heuristics

## Checklists

- [ ] Step-by-step validation list

## Reference Material

- Links, tables, or embedded snippets
```

Keep sections scannable—agents usually `cat` the skill and apply the content immediately.

---

## Best Practices

- **Single topic per skill**. If the document grows beyond ~500 lines, split it.
- **Action-oriented language**. Describe what to do, not just theory.
- **Use headings liberally** so Claude can jump to relevant sections quickly.
- **Pair with agents**. Agents should explicitly read the skill before acting.
- **Update regularly**. Skills are living documents; revisit them as patterns evolve.

---

## Example: Component Development

```markdown
# Component Development Skill

**Production-tested patterns for building professional React/Vue/Svelte components**

---

## Core Principles

1. **Type Safety First**
2. **Accessibility by Default**
3. **Performance Matters**
4. **Test Everything**
5. **Document Clearly**

## Component Architecture Patterns

### Single Responsibility Principle
...code samples...

### Container vs Presentational Pattern
...examples...

## React Component Template (TypeScript)
```tsx
import React from 'react';
...
```
```

The skill gives agents a ready-made playbook and example snippets they can reuse.

---

## Linking Skills with Agents & Commands

- **Agents**: Add mandatory steps (“Read `component-development` skill before writing code”).
- **Commands**: Reference skills to surface checklists or standards as part of a workflow.
- **Templates**: Store canonical boilerplate alongside the skill (`templates/`) and mention the path.

Agents and commands may check multiple locations for skills (user-specific, project-level, then plugin fallback). Document this behaviour so users know where to customise skills.

---

## Quality Checklist

- Skill folder named with lowercase hyphenated slug.
- `SKILL.md` provides clear guidance and actionable steps.
- Examples compile (if code) and follow documented style guides.
- Cross-links to related docs (templates, external references) are accurate.
- Referenced files (images, additional markdown) exist in the same folder.

---

## Next Steps

- Teach the skill to an agent in [Building Agents](agents.md).
- Include supporting automation via [Commands](commands.md).
- Share validation workflows in [Testing & Validation](testing-and-validation.md).
