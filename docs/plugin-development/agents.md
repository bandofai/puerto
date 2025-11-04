# Building Agents
> Part of the [Plugin Development Guide](index.md).

Agents are specialised subagents that Claude can invoke for deep, guided work. They include metadata (frontmatter) plus rich operating procedures that teach Claude how to act like an expert.

---

## File Layout

```
plugins/<your-plugin>/
└── agents/
    ├── frontend-engineer.md
    ├── accessibility-validator.md
    └── state-architect.md
```

Each agent file is Markdown with YAML frontmatter at the top.

```markdown
---
name: frontend-engineer
description: Production-ready React/Vue/Svelte component builder
tools: Read, Write, Edit, Bash, Grep, Glob
model: haiku
---

## Operating Guide
...
```

Puerto registers agent slugs using the `name` field and the file name. The `agents` array in `plugin.json` must include the same identifiers.

---

## Frontmatter Reference

| Field | Required | Description |
|-------|----------|-------------|
| `name` | ✅ | Agent identifier (lowercase with hyphens). Must match the filename. |
| `description` | ✅ | One-line summary shown in Claude when the agent is suggested. |
| `tools` | ✅ | Comma-separated list of allowed tools (`Read`, `Write`, `Edit`, `Bash`, `Search`, `Grep`, `Glob`, etc.). Determines capabilities. |
| `model` | ▫️ | Preferred Claude model (`haiku`, `sonnet`, `opus`). Defaults to Claude’s active model if omitted. |
| `triggers` | ▫️ | Optional hints for auto-invocation (keywords, file types, etc.). |
| `timeout` | ▫️ | Time budget in seconds. |

Keep frontmatter minimal—only include fields Claude understands. Additional metadata belongs in the body.

---

## Writing Effective Agent Guides

An agent file should teach Claude how an expert performs the task. Recommended sections:

1. **Mission Brief**  
   Explain exactly what the agent does and when to use it.

2. **Non-Negotiable Steps**  
   Highlight must-do actions (e.g., “Always read the skill before coding”).

3. **Workflow**  
   Step-by-step process including diagnostic commands or heuristics.

4. **Patterns/Templates**  
   Provide code snippets and checklists for consistent output.

5. **Quality Gates**  
   Define acceptance criteria (tests to run, docs to update, reporting format).

6. **Escalation Guidance**  
   Tell Claude what to do if prerequisites are missing or the task is out of scope.

Use headings (`##`) and emphasise important instructions using bold text. Keep tone directive and authoritative.

---

## Example: Component Builder

```markdown
---
name: frontend-engineer
description: PROACTIVELY use for React/Vue component creation
tools: Read, Write, Edit, Bash, Grep, Glob
model: haiku
---

You are a frontend component specialist creating production-ready UI components.

## CRITICAL: Skills-First Approach

**MANDATORY FIRST STEP**: Read the `component-development` skill before writing any code.

```bash
if [ -f ~/.claude/skills/component-development/SKILL.md ]; then
  cat ~/.claude/skills/component-development/SKILL.md
elif [ -f .claude/skills/component-development/SKILL.md ]; then
  cat .claude/skills/component-development/SKILL.md
fi
```

## When Invoked

1. Identify framework (React/Vue/Svelte) by inspecting `package.json`.
2. Audit existing components for patterns.
3. Generate component + styles + tests following skill guidance.
4. Run type-check, lint, and unit tests.
5. Report created files with usage example.
```

This pattern keeps the agent deterministic and ensures high-quality output.

---

## Designing Agent Ecosystems

- **Single responsibility**: Each agent should excel at one job. Split giant workflows into specialised agents.
- **Skill reuse**: Move shared domain knowledge into skills such as `skills/<topic>/SKILL.md` and have agents read them.
- **Template support**: Reference templates for boilerplate (`templates/`). Agents can `cat` or `cp` them.
- **Chaining**: Document how agents hand off to each other (e.g., `frontend-engineer` → `accessibility-validator`).

---

## Testing Agents

1. Install the plugin locally and trust the folder.
2. Invoke the agent by name (`Invoke Agent` panel or `/agent agent-name` if available).
3. Verify:
   - Frontmatter renders as expected (name, description, tool access).
   - Workflow matches the documented steps.
   - External dependencies (skills, templates, commands) exist.
   - The agent gracefully handles missing prerequisites.

Capture learnings in the plugin README so users understand how the agents interact.

---

## Next Steps

- Add shared knowledge with [Skills](skills.md).
- Define automation entry points with [Commands](commands.md).
- Expose external tooling through [MCP Servers](mcp-servers.md).
- Validate everything with [Testing & Validation](testing-and-validation.md).
