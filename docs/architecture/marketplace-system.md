# Marketplace System
> Part of the [Architecture docs](overview.md).

Puerto packages hundreds of Claude Code plugins and publishes them as a marketplace that users can add with a single command. This page explains how the marketplace is organised, generated, and consumed.

---

## High-Level Flow

```
plugins/*/.claude-plugin/plugin.json  ─┐
                                      │  generate-catalog.js
                                      ├───────────────▶  .claude-plugin/marketplace.json
docs/plugins/*.md  ◀──────┐           │
                          │           ▼
README.md & docs/README.md └─▶ Documentation & portal
```

1. Each plugin directory contains metadata (`.claude-plugin/plugin.json`) and assets (commands, agents, skills, templates, MCP definitions).
2. `scripts/generate-catalog.js` scans the tree and produces a consolidated `.claude-plugin/marketplace.json`.
3. Documentation pages reference the generated manifest to surface categories, featured plugins, and complete listings.
4. Claude Code users add the marketplace with `/plugin marketplace add bandofai/puerto`, which pulls `marketplace.json` and exposes all plugin entries.

---

## Repository Layout

```
.
├── plugins/
│   ├── <plugin-name>/
│   │   ├── .claude-plugin/plugin.json
│   │   └── ...feature files...
│   └── ...
├── .claude-plugin/
│   └── marketplace.json
├── scripts/
│   ├── generate-catalog.js
│   └── validate-plugin.js
└── docs/
```

- **plugins/** – Source of truth for plugin content.
- **.claude-plugin/marketplace.json** – Aggregated manifest served to Claude Code.
- **scripts/** – Tooling to build and validate the marketplace.
- **docs/** – Documentation hub (the page you’re reading).

---

## Marketplace Manifest

`marketplace.json` follows Claude Code’s marketplace schema:

```json
{
  "name": "puerto",
  "owner": { "name": "Band of AI" },
  "plugins": [
    {
      "name": "engineering",
      "source": "./plugins/engineering",
      "description": "Frontend development specialist...",
      "version": "1.0.0"
    }
  ]
}
```

- **name** – Marketplace identifier for `/plugin marketplace add`.
- **owner** – Display information in Claude.
- **plugins** – Array of entries pulled from each `plugin.json`.
  - `name` defaults to manifest `name`.
  - `source` is the relative path to the plugin folder.
  - `description` mirrors the plugin manifest summary.
  - `version` (optional) can be included if manifests specify it.

The generator sorts plugins alphabetically to keep the manifest stable across commits.

---

## Distribution Model

Puerto is distributed as a standard Git repository:

1. Users clone or reference the repository via GitHub.
2. Claude Code reads `.claude-plugin/marketplace.json`.
3. Installing a plugin pulls files directly from `plugins/<name>`.

Because everything is source-controlled:

- Reviews happen through GitHub pull requests.
- Updates are transparent and diffable.
- Documentation and code live together, ensuring accuracy.

---

## Update Flow

1. Add or modify plugin content inside `plugins/`.
2. Run `node scripts/generate-catalog.js`.
3. Commit the updated `marketplace.json` and plugin files.
4. Update docs (category pages, featured lists, README) if necessary.
5. Open a PR. CI/maintainers verify validation and merge.

Once merged, users pulling the latest repo gain access to new/updated plugins immediately.

---

## Related Documentation

- [Catalog Generation](catalog-generation.md) – How the manifest is produced.
- [Plugin Loading](plugin-loading.md) – How Claude Code consumes Puerto plugins.
- [Plugin Types](plugin-types.md) – Full list of supported capabilities.
- [CI/CD](ci-cd.md) – Automation for validation and publishing.
