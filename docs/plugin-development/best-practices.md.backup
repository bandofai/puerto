# Best Practices
> Part of the [Plugin Development Guide](index.md).

These principles keep Puerto plugins consistent, reliable, and delightful to use. Treat this page as your north star when designing new features or updating existing plugins.

---

## Design Philosophy

- **Solve one problem well** – Focus each plugin on a clear use case. Compose multiple plugins for broader workflows.
- **Prefer declarative workflows** – Describe desired outcomes; let Claude handle implementation details guided by your instructions.
- **Layer responsibilities** – Combine commands, agents, skills, and templates so each layer reinforces the others.
- **Document the “why”** – Explain reasoning in README files and skills so users (and future you) understand intent.

---

## Structure & Naming

- Plugin folder and manifest `name` must match (`frontend-developer`).
- Use `lowercase-with-hyphens` for folders, command files, agents, and skills.
- Keep directory layout minimal: remove unused directories (`templates/`, `skills/`) when not needed.
- Store reusable knowledge in `skills/` instead of repeating instructions across agents/commands.

---

## Commands

- Make prompts deterministic: specify validation steps, decision branches, and completion criteria.
- Ask clarifying questions when input is ambiguous; never guess silently.
- Provide safety checks for destructive actions (overwriting files, modifying infrastructure).
- Offer next-step suggestions once the command finishes.

---

## Agents

- Start with a mission statement and non-negotiable rules.
- Read relevant skills or templates before acting.
- Reference concrete tooling (commands to run, files to inspect) instead of vague guidance.
- Limit scope: hand off specialised tasks to other agents when appropriate.
- Conclude with a concise report (what changed, tests executed, follow-up items).

---

## Skills

- Write actionable, production-tested advice—avoid generic blog post content.
- Keep skills scannable using bullets, tables, and code snippets.
- Update them as practices evolve; version them if breaking changes occur.
- Encourage agents and commands to rely on skills so improvements propagate automatically.

---

## Templates

- Ship high-quality starting points that compile or lint cleanly.
- Highlight placeholders with clear markers (`{{PLACEHOLDER}}`, `TODO:`).
- Pair templates with documentation explaining when and how to use them.
- Avoid over-templating—keep files focused on the core use case.

---

## MCP Servers

- Be explicit about external dependencies and data flows.
- Fail fast with descriptive errors when prerequisites are missing.
- Pin versions or provide guidance for keeping dependencies up to date.
- Document authentication steps and expected latency/resource usage.

---

## Documentation

- README should mirror actual usage, not aspirational features.
- Include copy-pasteable commands, configuration snippets, and GIFs/screenshots where helpful.
- Link to relevant docs (user guides, architecture, reference) to provide deeper context.
- Keep docs in sync with releases—update them as soon as functionality changes.

---

## Quality & Maintenance

- Run validation scripts before every commit.
- Dogfood your plugin in real projects to catch edge cases.
- Encourage issue reporting in README and respond promptly.
- Version responsibly: follow semver and document changes in CHANGELOGs or README.

---

## Community Etiquette

- Align with Puerto’s [Community Guidelines](../contributing/community-guidelines.md).
- Credit inspiration or upstream projects in README.
- Accept feedback graciously—collaboration makes the ecosystem stronger.
- Encourage contributions via issues, discussions, and TODO lists in documentation.

---

## Quick Checklist

- [ ] Clear purpose and scope
- [ ] Deterministic commands and agents
- [ ] Reusable skills for domain knowledge
- [ ] Templates that accelerate adoption
- [ ] MCP integrations documented and safe
- [ ] README mirrors reality
- [ ] Validation script passes
- [ ] Marketplace manifest updated

Following these practices keeps Puerto plugins consistent and trustworthy, giving users the “it just works” experience we aim for.
