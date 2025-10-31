# Pull Request Guidelines
> Part of the [Contributing Guide](index.md).

Puerto receives a high volume of contributions. These guidelines keep reviews fast, friendly, and focused on shipping high-quality plugins and docs.

---

## 1. Pre-flight Checklist

Do these before you open a pull request.

| Task | Why it matters | Command / Reference |
|------|----------------|---------------------|
| Sync with `main` | Avoids merge conflicts and outdated catalogs | `git pull --rebase origin main` |
| Branch from main | Keeps history clean | `git checkout -b feat/<topic>` |
| Validate plugin structure | Catches manifest and layout issues | `node scripts/validate-plugin.js plugins/<name>` |
| Run full validation (multi-plugin changes) | Ensures catalog and docs stay healthy | `npm run validate-all` |
| Regenerate marketplace manifest (if metadata changed) | Keeps `.claude-plugin/marketplace.json` in sync | `node scripts/generate-catalog.js` |
| Update docs & README | PR is reviewable without guessing context | Follow [Documentation Style](documentation-style.md) |
| Capture evidence | Screenshots, logs, or recordings speed up review | Attach to the PR description |

> Tip: If you are touching several plugins or large docs, drop a short note in Discussions before you start. Maintainers can confirm priorities and reduce duplication.

---

## 2. Branch & Commit Strategy

- Create descriptive branches (`feat/frontend-dev-accessibility`, `fix/data-analyst-typo`).
- Use [Conventional Commits](https://www.conventionalcommits.org/) for every commit (`feat:`, `fix:`, `docs:`, `chore:`). This keeps release notes and search results crisp.
- Keep commits scoped—one logical change per commit. If you need to revive history later, focused commits help.
- Rebase (not merge) with the latest `main` before opening or updating a PR:  
  ```bash
  git fetch origin
  git rebase origin/main
  ```

---

## 3. Writing the Pull Request

Structure your description like this:

```markdown
## Summary
- What changed and why the user cares.
- Mention breaking changes or migrations if any.

## Testing
- [x] `node scripts/validate-plugin.js plugins/<name>`
- [x] Installed locally and exercised commands/agents
- [x] Verified MCP servers (if applicable)
- [ ] Additional manual or automated tests (describe)

## Documentation
- [x] README updated
- [x] Docs catalogue updated (if applicable)

## Screenshots / Evidence
- Drag-and-drop images, GIFs, or include log snippets.

## Notes for Reviewers
- Dependencies, test data, feature flags, credentials, or special instructions.
```

Tailor the checklist—remove irrelevant lines, add anything unique to your change (e.g., “Validated on macOS Sonoma”).

---

## 4. Scope Expectations

- **One feature per PR**: Avoid bundling unrelated plugins or sweeping refactors. Splitting work yields faster reviews.
- **Complete documentation**: README, docs, and examples reflect the new behaviour before reviewers look.
- **Tests & validation**: Note manual exercises, link to automated test runs, and mention edge cases you verified.
- **Catalog refresh**: If you added or renamed plugins, commit the regenerated `.claude-plugin/marketplace.json`.

For large or multi-phase initiatives, open an issue or discussion first so maintainers can help sequence the work.

---

## 5. During Review

- Respond quickly and kindly. If feedback needs discussion, start a threaded conversation rather than resolving prematurely.
- Push follow-up commits with clear messages (`fix: address reviewer feedback on validation script`).
- Resolve reviewer comments once addressed, and leave a short summary (“Reworded README paragraph + added CLI example”).
- If feedback reveals bigger scope creep, pause and align with maintainers before continuing.

---

## 6. Merge Criteria

Your PR is ready when:

- ✅ Validation scripts pass with no errors or warnings left unaddressed.
- ✅ Documentation and manifests align with the implementation.
- ✅ Links and assets (screenshots, attachments) resolve correctly.
- ✅ `.claude-plugin/marketplace.json` is current (where applicable).
- ✅ CI succeeds (catalog generator workflow + any additional checks).

Maintainers may squash commits for a tidy history. If you prefer a different merge strategy, mention it in the PR.

---

## 7. After Merge

- Monitor GitHub Issues for bug reports or follow-up questions tied to your change.
- Bump plugin versions when releasing updates and keep release notes current.
- Share noteworthy features in Discussions or marketing channels so users adopt them quickly.

---

## Related Docs

- [Contributing Overview](index.md)
- [Submitting Plugins](submitting-plugins.md)
- [Review Process](review-process.md)
- [Testing & Validation](../plugin-development/testing-and-validation.md)
