# Testing & Validation
> Part of the [Plugin Development Guide](index.md).

Before submitting a plugin, verify that it installs cleanly, exposes the right capabilities, and behaves as documented. This guide covers automated validation scripts and manual testing workflows used by Puerto maintainers.

---

## 1. Automated Validation

Puerto ships a Node script that checks plugin structure and manifest syntax.

### Validate a Single Plugin

```bash
node scripts/validate-plugin.js plugins/<plugin-name>
```

Checks performed:
- `.claude-plugin/plugin.json` exists and is valid JSON
- Required manifest fields (`name`, `version`, `description`)
- `author` object (if present) has a `name`
- Plugin name matches lowercase-hyphen convention
- Optional directories (`commands`, `agents`, `skills`, `hooks`) are folders
- Warns when README.md is missing

Example output:

```
Validating plugin: /Users/me/puerto/plugins/frontend-developer

✅ Plugin validation passed!
```

### Validate All Plugins

Install dependencies (`npm install`) once, then run:

```bash
npm run validate-all
```

This script iterates through each plugin directory and reports errors/warnings. Run it before opening a pull request to catch regressions.

---

## 2. Manual Functional Testing

Automated checks only cover structure. Always test the user experience:

1. **Install the plugin locally**
   ```bash
   /plugin install <plugin-name>@/absolute/path/to/plugins/<plugin-name>
   ```

2. **Verify commands**
   - Execute each command (`/brainstorm`, `/generate-sitemap`, etc.).
   - Confirm prompts, outputs, and file writes match documentation.

3. **Exercise agents**
   - Invoke agents individually (Claude → “Invoke Agent” panel).
   - Check they read required skills/templates and follow the workflow.
   - Validate tool permissions (`Read`, `Write`, `Edit`, `Bash`) are sufficient.

4. **Check skills/templates**
   - Ensure skills contain current best practices.
   - Review templates compile/lint when copied into a fresh project.

5. **Validate MCP servers**
   - Launch the plugin from a clean environment.
   - Confirm `.mcp.json` commands install successfully.
   - Document auth steps or prerequisite tooling.

6. **Smoke test README**
   - Follow installation instructions exactly.
   - Run sample commands provided in docs to ensure they succeed.

Record findings in the PR description if anything notable occurs.

---

## 3. Marketplace Manifest

Puerto hosts a `.claude-plugin/marketplace.json` catalog. After adding or renaming plugins:

1. Run `node scripts/generate-catalog.js`.
2. Commit the updated manifest.
3. Spot-check the new entry (name, description, path).

The catalog powers the documentation and marketplace listings.

---

## 4. Continuous Integration Expectations

Maintainers run automated validation in CI. Plugins are merged only if:

- Validation script passes (no errors).
- README is present and coherent.
- New files follow naming conventions.
- Tests/manual checks described above are complete.

If your plugin depends on external services (APIs, CLIs), provide mock or demo credentials where practical so reviewers can test.

---

## 5. Troubleshooting Common Issues

| Symptom | Fix |
|---------|-----|
| `Missing .claude-plugin/plugin.json` | Add the manifest folder and file. |
| `Plugin name must be lowercase` | Rename plugin directory and update `name`. |
| `author must be an object` | Use `"author": { "name": "..." }` instead of a string. |
| `commands directory exists but contains no .md files` | Remove the folder or add command files. |
| MCP server fails to start | Check Node/UV version, package availability, environment variables. |
| Command tries to use missing skill/template | Update instructions or ship supporting files. |

---

## 6. Submission Checklist

- [ ] `plugin.json` validated locally.
- [ ] README includes installation, usage, and features.
- [ ] Commands/agents/skills/templates tested manually.
- [ ] `.mcp.json` (if present) launches all servers successfully.
- [ ] `node scripts/generate-catalog.js` run if metadata changed.
- [ ] Screenshots/GIFs optional but encouraged for complex workflows.

Completing this checklist speeds up the review process and keeps Puerto reliable for users.

---

## Next Steps

- Document your release in [Publishing](publishing.md).
- Share best practices with other authors via [Best Practices](best-practices.md).
- Learn how reviewers evaluate submissions in [Review Process](../contributing/review-process.md).
