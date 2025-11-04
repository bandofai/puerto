# Debugging Plugins
> Part of the [Plugin Development Guide](index.md).

Even well-designed plugins can misbehave—commands skip steps, agents forget skills, MCP servers refuse to start. Use this guide to diagnose and resolve issues quickly.

---

## 1. Reproduce the Issue

- **Start fresh** – Restart Claude Code and clear previous context.
- **Isolate the plugin** – Disable other plugins to rule out conflicts.
- **Capture exact steps** – Note commands run, prompts given, files touched.
- **Record environment** – OS, Node version, Claude model, plugin version.

Document everything in the issue or PR so others can reproduce.

---

## 2. Validate Structure

Run structural checks to catch obvious problems:

```bash
node scripts/validate-plugin.js plugins/<plugin-name>
```

Fix manifest errors, missing directories, or malformed JSON. Many runtime issues disappear once the plugin structure is correct.

---

## 3. Inspect Commands & Agents

### Commands
- Ensure instructions handle optional parameters and edge cases.
- Confirm file paths are relative to the user’s project.
- Add prompts reminding Claude to confirm before destructive actions.

### Agents
- Check frontmatter (`tools`, `model`) for required capabilities.
- Verify agents explicitly read the right skills/templates.
- Make critical steps bold so Claude doesn’t skip them.
- Break apart overly long agents—smaller specialists perform better.

---

## 4. Verify Skills & Templates

- **Skills missing?** Agents referencing `skills/<name>/SKILL.md` must have the file present.
- **Outdated guidance?** Update skills when best practices evolve.
- **Template mismatch?** Ensure template file names match what commands/agents expect.

When in doubt, open the file inside Claude Code and review it with the agent to synchronise expectations.

---

## 5. MCP Server Troubleshooting

1. Run the command manually outside Claude to confirm it launches.
2. Check prerequisites (Node/UV version, Chrome, API keys).
3. Review stdout/stderr logs shown in Claude when the server starts.
4. Use verbose flags (`--verbose`, `DEBUG=*`) when available.
5. For HTTP transports, verify TLS certificates and connectivity.

Document fixes or workarounds in the plugin README’s troubleshooting section.

---

## 6. Logging & Diagnostics

- Add logging statements (stdout prints) in CLI wrappers to show progress.
- Encourage users to enable Claude’s debug logs if available.
- Maintain a `TROUBLESHOOTING.md` or README section for recurring issues.

For agent/command debugging, temporarily add “Report current step” instructions to track progress.

---

## 7. Regression Prevention

- Write regression notes in the README or repository issues.
- Add checklist items to ensure the bug won’t reappear.
- Update skills/templates so future agents follow the corrected workflow.
- Consider adding automated validation (e.g., scripts that lint templates).

---

## 8. Getting Help

- Search existing issues in the Puerto repo.
- Open a new issue with:
  - Plugin name & version
  - Claude Code version
  - Reproduction steps
  - Expected vs actual behaviour
  - Logs or screenshots
- Tag maintainers or authors if urgent.

Participate in GitHub Discussions to learn tips from other plugin authors.

---

## Debugging Checklist

- [ ] Structural validation passes.
- [ ] README instructions reproduce the issue.
- [ ] Commands/agents reviewed for missing steps.
- [ ] Skills/templates verified and updated.
- [ ] MCP server prerequisites confirmed.
- [ ] Logs captured and analysed.
- [ ] Fix documented for future contributors.

---

Need community support? Start with the [Troubleshooting Guide](../user-guide/troubleshooting.md) for user-facing issues, then escalate via GitHub if deeper changes are required.
