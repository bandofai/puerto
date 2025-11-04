# Publishing Your Plugin
> Part of the [Plugin Development Guide](index.md).

Ready to share your plugin with the Puerto community? Follow this workflow to package, document, and submit your work for review.

---

## 1. Prepare Your Plugin Folder

```
plugins/<plugin-name>/
├── .claude-plugin/
│   └── plugin.json
├── README.md
├── commands/
├── agents/
├── skills/
├── templates/
└── .mcp.json
```

- Ensure folder name matches the `name` field in `plugin.json`.
- Remove unused directories to keep the repository tidy.

---

## 2. Document Everything

Create a README that mirrors what users will experience:

1. **Overview** – What problem the plugin solves.
2. **Installation** – `/plugin install plugin-name@puerto` and project configuration.
3. **Features** – Commands, agents, skills, templates, MCP servers.
4. **Usage Examples** – Copy-ready prompts or command sequences.
5. **Configuration** – Required environment variables, API keys, project setup.
6. **Prerequisites** – Node version, external services, OS requirements.
7. **Support** – Links to issues or contact details.

Follow the [Documentation Style Guide](../contributing/documentation-style.md) for tone and formatting.

---

## 3. Validate Locally

- Run the automated validator:  
  ```bash
  node scripts/validate-plugin.js plugins/<plugin-name>
  ```
- Install locally and walk through the README instructions.
- Confirm MCP servers start successfully, commands behave as expected, and agents read required skills/templates.
- Generate the marketplace manifest if this is a new plugin:  
  ```bash
  node scripts/generate-catalog.js
  ```

Record testing notes—they help reviewers reproduce your setup quickly.

---

## 4. Update Metadata

- Add your plugin to `.claude-plugin/marketplace.json` (via script above).
- Update documentation entry points if relevant:
  - [Plugin Catalog](../plugins/by-category.md)
  - [Featured plugins](../plugins/featured.md)
  - README quick links or examples in other docs

---

## 5. Submit a Pull Request

1. Fork the repository and create a feature branch (`feat/<plugin-name>`).
2. Commit plugin files, docs, and updated manifests.
3. Push and open a PR with:
   - High-level summary
   - Testing checklist
   - Screenshots/GIFs (optional but helpful)
   - Notes on external dependencies or credentials
4. Request review from maintainers.

Use [Pull Request Guidelines](../contributing/pull-request-guidelines.md) to structure your submission.

---

## 6. Respond to Review

Maintainers will provide feedback based on:
- Accuracy of documentation
- Code/manifest structure
- Safety/security considerations
- Adherence to naming conventions and style guides
- Testability of the plugin

Update your branch, re-run validation, and reply to comments. Keep the conversation in the PR so future contributors can learn from it.

---

## 7. After Merge

- Celebrate! 🎉 Your plugin becomes part of Puerto’s catalog.
- Monitor issues for bug reports or feature requests.
- Follow semantic versioning for updates (`1.0.1`, `1.1.0`, etc.).
- Maintain documentation as behaviours change.

---

## Resources

- [Contributing Overview](../contributing/index.md)
- [Submitting Plugins Checklist](../contributing/submitting-plugins.md)
- [Review Process](../contributing/review-process.md)
- [Best Practices](best-practices.md)
- [Testing & Validation](testing-and-validation.md)

---

**Tip:** Join the discussion on GitHub Discussions to showcase your plugin, gather feedback, and coordinate roadmap ideas.
