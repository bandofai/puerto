# Plugin Loading
> Part of the [Architecture docs](overview.md).

When a user installs Puerto, Claude Code pulls metadata from the marketplace manifest, fetches plugin files, and makes capabilities available in the IDE. Understanding this pipeline helps you troubleshoot installations and design plugins that load instantly.

---

## Loading Pipeline

1. **Marketplace registration**
   ```bash
   /plugin marketplace add bandofai/puerto
   ```
   Claude downloads `.claude-plugin/marketplace.json` and caches the plugin list.

2. **Plugin installation**
   ```bash
   /plugin install essentials@puerto
   ```
   Claude retrieves `plugins/essentials/**` from the repository.

3. **Manifest ingestion**
   - Reads `.claude-plugin/plugin.json` for metadata.
   - Registers commands, agents, skills, and templates by scanning directories.
   - Loads `.mcp.json` (if present) to expose MCP servers.

4. **Activation**
   - Commands become available via `/command-name`.
   - Agents show up in the “Invoke Agent” palette.
   - Skills/templates are accessible to Claude’s tooling.
   - MCP servers can be started on demand.

---

## Directory Scanning Rules

When a plugin loads, Claude looks for well-known directories:

| Folder | Behaviour |
|--------|-----------|
| `commands/` | Markdown files become `/command-name` entries. |
| `agents/` | Markdown with YAML frontmatter registers agents. |
| `skills/` | `*/SKILL.md` files provide reusable knowledge. |
| `templates/` | Files referenced in docs/commands/agents. |
| `.mcp.json` | Defines external MCP servers. |

Missing folders are ignored gracefully.

---

## Updates & Versioning

- Re-installing (`/plugin update name@puerto`) pulls the latest repository state.
- Claude compares manifest versions if provided; otherwise the repository commit is the source of truth.
- Semantic versioning in `plugin.json` helps communicate breaking changes, but Claude always downloads the latest copy of the plugin from the repo. Keep release notes in README to inform users.

---

## Caching & Trust

- Claude caches downloaded plugins. If you edit a plugin locally, use `/plugin install name@/absolute/path` to point Claude to the working copy during development.
- Users must “trust” the project before local settings apply. Document trust requirements in your README to reduce confusion.

---

## Failure Modes

| Stage | Symptoms | Fix |
|-------|----------|-----|
| Marketplace download | `/plugin marketplace add` fails | Check network access or repo URL. |
| Manifest parse | Plugin missing from catalog | Update `.claude-plugin/marketplace.json`. |
| Installation | Files missing or outdated | Run `/plugin update` or reinstall. |
| Activation | Commands/agents absent | Ensure directories exist and contain `.md` files. |
| MCP server start | Errors on launch | Validate `.mcp.json` entries and prerequisites. |

Use logs in Claude and repository validation scripts to pinpoint issues.

---

## Related Docs

- [Installation Guide](../installation.md)
- [Testing & Validation](../plugin-development/testing-and-validation.md)
- [Troubleshooting](../user-guide/troubleshooting.md)
- [Catalog Generation](catalog-generation.md)
