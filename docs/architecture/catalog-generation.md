# Catalog Generation
> Part of the [Architecture docs](overview.md).

Puerto’s marketplace catalog is built automatically by scanning every plugin folder and aggregating metadata into `.claude-plugin/marketplace.json`. This keeps the catalog consistent with the source files and guarantees that new plugins appear everywhere at once.

---

## Source of Truth

- Each plugin stores metadata in `.claude-plugin/plugin.json`.
- The catalog generator reads the manifest, extracts core fields, and writes a combined marketplace manifest.

```
plugins/<name>/.claude-plugin/plugin.json
        │
        ▼
scripts/generate-catalog.js
        │
        ▼
.claude-plugin/marketplace.json
```

---

## Running the Generator

```bash
node scripts/generate-catalog.js
```

This script:

1. Lists all directories under `plugins/`.
2. Looks for `.claude-plugin/plugin.json` in each directory.
3. Parses the manifest and pushes a new entry into the catalog array.
4. Sorts entries alphabetically by plugin name.
5. Writes `.claude-plugin/marketplace.json` with two-space indentation.

You must commit the updated `marketplace.json` when:
- Adding a new plugin
- Renaming a plugin
- Changing `description` or other catalog-facing metadata

Running the script is idempotent—it rewrites the manifest from scratch each time to avoid merge conflicts.

---

## Validation & Error Handling

- Missing manifest → plugin skipped with a warning in the console.
- Invalid JSON → error message including the plugin folder.
- No plugins found → script exits with an error.

The generator doesn’t validate schema details (that’s handled by `scripts/validate-plugin.js`); it focuses on catalog aggregation.

---

## Marketplace Schema Snippet

```json
{
  "name": "puerto",
  "owner": { "name": "Band of AI" },
  "plugins": [
    {
      "name": "frontend-developer",
      "source": "./plugins/frontend-developer",
      "description": "Frontend development specialist...",
      "version": "1.0.0"
    }
  ]
}
```

- `source` points to the plugin folder, allowing Claude Code to fetch assets directly.
- Additional fields (author, keywords) can be added later if Claude’s marketplace schema expands—`generate-catalog.js` is straightforward to update.

---

## Development Tips

- Run the generator after modifying any manifest to ensure the catalog stays in sync.
- Use `git diff` to verify only the intended entries changed.
- If you maintain multiple plugins, commit related catalog changes together with doc updates (e.g., featured lists).
- For large batch updates, consider running the generator in `--watch` mode (easy to add) to regenerate automatically.

---

## Related Docs

- [Marketplace System](marketplace-system.md) – Full marketplace architecture.
- [Plugin Loading](plugin-loading.md) – How Claude Code interprets the generated catalog.
- [Testing & Validation](../plugin-development/testing-and-validation.md) – Ensuring manifests are valid before generation.
