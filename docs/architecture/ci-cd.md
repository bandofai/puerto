# CI/CD Workflow
> Part of the [Architecture docs](overview.md).

Puerto automates catalog generation and validation to keep the marketplace reliable. This page outlines the GitHub Actions pipeline and recommended local workflows.

---

## GitHub Actions

Workflow file: `.github/workflows/update-catalog.yml`

### Triggers

- `push` events to `main` touching `plugins/**`
- Manual `workflow_dispatch` (run from GitHub UI)

### Steps

1. **Checkout repository**  
   Uses `actions/checkout@v4` with default permissions.

2. **Setup Node.js 18**  
   Ensures the generator script runs in a consistent environment.

3. **Generate marketplace catalog**  
   Executes `node scripts/generate-catalog.js` to rebuild `.claude-plugin/marketplace.json`.

4. **Detect changes**  
   Runs `git diff` against the catalog file. If the script modifies the manifest, the workflow marks `changed=true`.

5. **Commit & push**  
   When changes exist, the workflow commits the updated manifest with message `chore: update marketplace catalog [skip ci]`.

This automation guarantees that the published catalog always matches the source plugins—even if contributors forget to regenerate locally.

---

## Local Workflow

Before opening a pull request:

1. Install dependencies (`npm install`) if you plan to run scripts that rely on packages.
2. Run the validator on your plugin(s):  
   ```bash
   node scripts/validate-plugin.js plugins/<name>
   ```
3. Regenerate the marketplace catalog:  
   ```bash
   node scripts/generate-catalog.js
   ```
4. Review `git status` to ensure only intended files changed.

Following these steps keeps diffs small and predictable. CI will regenerate the catalog if you miss it, but it’s faster to catch issues locally.

---

## Future Improvements

Ideas on the roadmap:

- Add automated linting for documentation and templates.
- Run smoke tests for MCP servers using containerised environments.
- Publish marketplace snapshots as GitHub Releases for easier pinning.

Contributions welcome—open an issue or PR if you have automation ideas.

---

## Related Docs

- [Catalog Generation](catalog-generation.md)
- [Plugin Development – Testing & Validation](../plugin-development/testing-and-validation.md)
- [Contributing – Pull Request Guidelines](../contributing/pull-request-guidelines.md)
