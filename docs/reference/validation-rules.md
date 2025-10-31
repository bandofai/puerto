# Validation Rules
> Part of the [Reference](index.md).

Puerto uses automated and manual checks to ensure every plugin installs cleanly and behaves as documented. This reference lists the validation rules enforced by tooling and reviewers.

---

## Automated Checks (`scripts/validate-plugin.js`)

Run locally with:

```bash
node scripts/validate-plugin.js plugins/<plugin-name>
```

### Hard Failures (Errors)

- Plugin directory exists.
- `.claude-plugin/` directory present.
- `.claude-plugin/plugin.json` exists and is valid JSON.
- `plugin.json` contains required fields:
  - `name` (lowercase with hyphens)
  - `version` (semver format)
  - `description`
- `author` field (if present) is an object with a `name` property (not a string).
- Optional directories (`commands`, `agents`, `skills`, `hooks`) are directories (not files).

### Soft Failures (Warnings)

- `version` not strictly semver (warns but does not block).
- Missing `author` field.
- `commands/` directory exists but contains no `.md` files.
- README.md missing.

The script exits with non-zero status if any errors occur.

---

## Catalog Consistency

- `.claude-plugin/marketplace.json` regenerated after adding or updating plugins.
- Each catalog entry references an existing plugin directory.
- Descriptions are concise (≤ 200 characters recommended) and match plugin purpose.

Use `node scripts/generate-catalog.js` to rebuild the catalog automatically.

---

## Documentation Requirements

Reviewers check that:

- Plugin README includes installation, usage, configuration, and troubleshooting sections.
- New or renamed plugins update relevant docs (category listings, featured lists, quickstarts).
- Links within docs resolve correctly.
- Instructions match actual behaviour observed during testing.

---

## Manual Functional Testing

Before approval, maintainers validate that:

- Commands execute as described and handle error cases gracefully.
- Agents respect tool permissions, read required skills, and follow documented workflows.
- Skills and templates exist at referenced paths and contain up-to-date guidance.
- MCP servers launch successfully and document prerequisites (Node/UV versions, API keys, browsers, etc.).

Provide a testing checklist in your PR description to streamline this process.

---

## Security & Safety Review

Reviewers consider:

- External dependencies (CLI tools, APIs) are trustworthy and documented.
- Sensitive actions (overwriting files, running destructive commands) include confirmation prompts.
- Plugins do not collect or transmit data without consent.
- Licenses of bundled assets and dependencies are compatible (MIT recommended).

---

## Submission Checklist

Before opening a PR, confirm:

- [ ] `node scripts/validate-plugin.js plugins/<name>` passes.
- [ ] `.claude-plugin/marketplace.json` regenerated if metadata changed.
- [ ] README and docs updated.
- [ ] Manual testing completed (note results in PR).
- [ ] Plugin follows naming, directory, and documentation conventions.

---

## Related Docs

- [Testing & Validation](../plugin-development/testing-and-validation.md)
- [Plugin Manifest](plugin-json-schema.md)
- [Directory Structure](directory-structure.md)
- [Submitting Plugins](../contributing/submitting-plugins.md)
