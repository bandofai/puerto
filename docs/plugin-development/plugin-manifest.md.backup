# Plugin Manifest
> Part of the [Plugin Development Guide](index.md).

Every Puerto plugin is defined by a manifest file located at `.claude-plugin/plugin.json`. This file tells Claude Code how to load the plugin, what capabilities it exposes, and how it should appear in the Puerto marketplace.

Use this guide whenever you add a new plugin or update metadata for an existing one.

---

## File Location

```
plugins/<your-plugin>/
├── .claude-plugin/
│   └── plugin.json  ← manifest
├── README.md
├── commands/
├── agents/
├── skills/
└── templates/
```

The manifest directory must be named `.claude-plugin` (with a leading dot). Claude Code looks for `plugin.json` inside that folder.

---

## Minimal Manifest

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Short, specific summary of what the plugin does",
  "author": {
    "name": "Your Name"
  }
}
```

This is enough for Puerto to recognise and list the plugin. From here you can describe the features you ship (commands, agents, skills, templates, MCP servers) and add marketplace metadata.

---

## Complete Example

```json
{
  "name": "frontend-developer",
  "version": "1.2.0",
  "description": "Frontend development specialist with React/Vue component generation, accessibility validation, and responsive styling",
  "author": {
    "name": "Puerto Plugin System",
    "url": "https://github.com/bandofai/puerto"
  },
  "keywords": [
    "frontend",
    "react",
    "vue",
    "accessibility",
    "typescript"
  ],
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/bandofai/puerto/tree/main/plugins/frontend-developer"
  },
  "homepage": "https://github.com/bandofai/puerto/tree/main/plugins/frontend-developer#readme",
  "bugs": {
    "url": "https://github.com/bandofai/puerto/issues"
  }
}
```

---

## Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Plugin identifier. Lowercase with hyphens only (`^[a-z0-9-]+$`). Must match folder name. |
| `version` | string | ✅ | Semantic version (`MAJOR.MINOR.PATCH`). Increments when you release updates. |
| `description` | string | ✅ | ≤ 200 character summary shown in the marketplace and docs. |
| `author.name` | string | ✅ | Display name for plugin author or organisation. |
| `author.email` | string | ▫️ | Contact email for support or questions. |
| `author.url` | string | ▫️ | Homepage for the author. |
| `keywords` | string[] | ▫️ | Search keywords to improve discoverability. |
| `license` | string | ▫️ | SPDX identifier (e.g. `MIT`, `Apache-2.0`). |
| `repository` | object | ▫️ | Source control information (`type`, `url`). |
| `bugs.url` | string | ▫️ | Issue tracker URL. |
| `homepage` | string | ▫️ | Landing page or README anchor. |

---

## Authoring Tips

- Keep descriptions crisp. The first sentence is used in marketplace listings.
- Puerto infers commands, agents, skills, templates, and MCP servers from the directory structure—no need to list them in the manifest.
- Use 1.0.0 for initial releases. Increment **PATCH** for fixes, **MINOR** for backward-compatible features, **MAJOR** for breaking changes.
- Add relevant keywords so `/plugin search` surfaces your work.
- Include repository and bug URLs if you maintain plugins outside this repo.

---

## Validation Checklist

Before submitting a plugin, confirm:

- `plugin.json` is valid JSON (no trailing commas).
- Required fields (`name`, `version`, `description`, `author.name`) are present.
- Descriptions accurately summarise the plugin.
- MCP definitions (if any) live in `.mcp.json` and are documented in README.
- License field matches the license file shipped with the plugin.

Run `node scripts/validate-plugin.js plugins/<name>` to catch mistakes automatically. Full validation is covered in [Testing & Validation](testing-and-validation.md).

---

## Next Steps

- Build your first manifest with the [Quickstart](quickstart.md).
- Dive into feature specifics: [Commands](commands.md), [Agents](agents.md), [Skills](skills.md), [Templates](templates.md), [MCP Servers](mcp-servers.md).
- Review the full schema details in the [plugin.json reference](../reference/plugin-json-schema.md).
