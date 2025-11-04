# Plugin Types
> Part of the [Architecture docs](overview.md).

Puerto plugins can bundle multiple capability types. Understanding each type helps you design balanced plugins and makes it easier for users to discover what they need.

---

## Overview

| Type | Purpose | Source Directory | Docs |
|------|---------|------------------|------|
| Commands | Task-specific workflows executed via `/command` | `commands/` | [Building Commands](../plugin-development/commands.md) |
| Agents | Specialist subagents that take over complex tasks | `agents/` | [Building Agents](../plugin-development/agents.md) |
| Skills | Knowledge bases & checklists referenced by agents/commands | `skills/` | [Developing Skills](../plugin-development/skills.md) |
| Templates | Ready-made files users can copy into projects | `templates/` | [Adding Templates](../plugin-development/templates.md) |
| MCP Servers | Bridges to external CLIs/APIs/tools | `.mcp.json` | [Integrating MCP Servers](../plugin-development/mcp-servers.md) |

Plugins may mix and match types. Many start with commands or agents, then add skills/templates to reinforce best practices.

---

## Commands

- Triggered by `/command-name` in Claude Code.
- Written in Markdown with step-by-step instructions.
- Best for deterministic, repeatable workflows (scaffold project, run audits, generate docs).
- Can orchestrate other types (call agents, copy templates).

---

## Agents

- Include YAML frontmatter describing capabilities and model preferences.
- Provide deep operational knowledge for specialised tasks.
- Often rely on skills for domain expertise.
- Examples: `frontend-engineer`, `state-architect`, `seo-optimizer`.

---

## Skills

- Reusable reference material stored under `skills/<slug>/SKILL.md`.
- Encourage consistency; agents read them before acting.
- Ideal for checklists, architecture patterns, SOPs, interview scripts.

---

## Templates

- Starter files and checklists embedded in the plugin.
- Commands/agents can copy them into the user’s project.
- Reduces boilerplate and ensures output matches documented standards.

---

## MCP Servers

- Extend Claude with external capabilities (browser automation, documentation lookup, custom services).
- Defined declaratively in `.mcp.json`.
- May launch local binaries (`npx`, `uvx`) or connect to hosted endpoints over HTTP.
- Require extra testing and documentation to handle dependencies and authentication.

---

## Hybrid Plugins

Many Puerto plugins combine several types to deliver end-to-end workflows:

- **engineering** – Agents + skills + templates for UI engineering.
- **essentials** – Commands + MCP servers for project orchestration.
- **subagent-creator** – Specialized agents supported by a curated skill library.

When combining types:

- Keep responsibilities clear (which component does what).
- Document interactions in README (e.g., “Run `/bootstrap-ui` to copy templates and hand off to `frontend-engineer` agent”).
- Ensure validation covers every type shipped.

---

## Discovery & Documentation

- Catalog pages highlight plugin types so users know what to expect.
- Include a “Capabilities” section in your README summarising the types you ship.
- Cross-link to relevant docs so users can dive deeper (commands → user guide, agents → invocation instructions).

---

## Next Steps

- Learn how these pieces fit together in [Plugin Development Guide](../plugin-development/index.md).
- Understand runtime mechanics in [Plugin Loading](plugin-loading.md).
- Review [Best Practices](../plugin-development/best-practices.md) for combining types effectively.
