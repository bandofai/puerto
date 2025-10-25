# Review Process
> Part of the [Contributing Guide](index.md).

Puerto’s review process ensures every plugin feels polished, safe, and consistent before reaching users. This page explains what maintainers look for and how contributors can prepare.

---

## Review Stages

1. **Triage**
   - Maintainer verifies the PR description follows guidelines.
   - Validation script output is checked (locally or via CI).
   - Obvious blockers (missing files, failing tests) are flagged immediately.

2. **Functional Review**
   - Reviewer installs the plugin, runs documented commands, and exercises agents.
   - MCP servers are launched to confirm dependencies and authentication steps.
   - Behaviour is compared against README promises.

3. **Documentation Review**
   - README clarity, formatting, and completeness.
   - Cross-links in global docs (catalog, featured lists) confirmed.
   - Troubleshooting and prerequisites verified.

4. **Quality & Safety Review**
   - Naming conventions respected.
   - Instructions do not encourage unsafe actions without confirmation.
   - External dependencies vetted (licensing, source, security posture).
   - Versioning and changelog (if provided) make sense.

5. **Final Approval**
   - All comments resolved.
   - Validation re-run if files changed during review.
   - Maintainer merges once satisfied.

---

## What Reviewers Expect

- Clean diffs with only necessary files changed.
- Validation scripts executed before requesting review.
- Clear testing notes (commands, agents, MCP usage).
- Documentation that matches the actual behaviour.
- Transparent disclosure of external services/APIs.

When major revisions are needed, reviewers summarise required changes. Smaller tweaks may be suggested with inline comments or `nit:` notes.

---

## Turnaround Time

- Simple documentation updates: typically 1–2 business days.
- New plugins or major features: 3–5 business days depending on complexity.
- Critical fixes may be prioritised.

If your PR hasn’t received attention within a week, feel free to ping maintainers or comment with additional context.

---

## Tips for Fast Approvals

- Provide screenshots or recordings of the plugin in action.
- Include sample prompts that reviewers can reuse.
- Attach logs from validation commands or MCP server runs.
- Keep PR scope limited and feature-complete.
- Resolve comments quickly and summarise changes after each revision.

---

## After Approval

- PR is merged; catalog workflow runs if necessary.
- Contributors can delete feature branches (optional).
- Announce the update in Discussions or release notes.
- Stay available for follow-up questions in the PR or issues.

---

## Related Docs

- [Pull Request Guidelines](pull-request-guidelines.md)
- [Submitting Plugins](submitting-plugins.md)
- [Testing & Validation](../plugin-development/testing-and-validation.md)
- [Community Guidelines](community-guidelines.md)
