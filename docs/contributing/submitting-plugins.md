# Submitting Plugins
> Part of the [Contributing Guide](index.md).

Follow this checklist to contribute a new plugin—or major update—to Puerto. Completing every step keeps reviews fast and ensures users get a polished experience.

---

## 1. Plan Your Plugin

- Search the catalog to confirm the idea isn’t already covered.
- Scope your plugin to a single problem (commands, agents, skills as needed).
- Note any external dependencies (APIs, CLIs, credentials).

Document the value proposition in your README before writing code—clear intent makes review easier.

---

## 2. Build the Plugin

1. Create a folder under `plugins/<plugin-name>`.
2. Add `.claude-plugin/plugin.json` with metadata. Review the [Plugin Manifest guide](../plugin-development/plugin-manifest.md) for field details.
3. Implement commands/agents/skills/templates/MCP servers as required.
4. Write `README.md` covering installation, usage, features, configuration, and troubleshooting.
5. Update documentation if your plugin should appear in categories, featured lists, or examples.

---

## 3. Validate Locally

- `node scripts/validate-plugin.js plugins/<plugin-name>`
- `npm run validate-all` (optional but recommended before PR)
- Install the plugin locally and walk through README instructions
- Test commands, agents, and MCP servers
- Regenerate `.claude-plugin/marketplace.json`:
  ```bash
  node scripts/generate-catalog.js
  ```

Fix any warnings or errors before requesting review.

---

## 4. Prepare Documentation

- Cross-link your plugin in relevant docs (categories, featured, tutorials).
- Add screenshots or GIFs if they improve understanding.
- Provide installation examples and CLI snippets.
- Highlight prerequisites and known limitations.

Follow the [Documentation Style Guide](documentation-style.md) to keep tone and formatting consistent.

---

## 5. Open a Pull Request

Include the following in your PR description:

- Summary of the plugin and primary use cases
- Testing checklist (commands run, MCP validation, etc.)
- Dependencies or setup steps reviewers must perform
- Screenshots or demos (optional but appreciated)
- Checklist confirming you ran validation scripts

Reference this doc or other relevant docs so reviewers understand context.

---

## 6. Respond to Feedback

- Address review comments promptly and keep conversation in the PR.
- Update documentation when reviewers uncover missing instructions.
- Re-run validation scripts after changes.
- Mention when updates are ready for re-review.

Maintainers merge once quality, documentation, and validation meet Puerto standards.

---

## Quick Checklist

- [ ] Unique plugin idea with clear scope.
- [ ] `plugin.json` filled out correctly.
- [ ] Commands/agents/skills/templates tested in Claude.
- [ ] README covers installation, usage, configuration, troubleshooting.
- [ ] Validation scripts run without errors.
- [ ] Marketplace catalog regenerated (`node scripts/generate-catalog.js`).
- [ ] Documentation updated (categories, featured, examples).
- [ ] PR template filled out with testing notes.

---

Need help? Start in [Contributing Overview](index.md) or ask in [GitHub Discussions](https://github.com/bandofai/puerto/discussions).
