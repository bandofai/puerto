# Troubleshooting Guide

Common issues and solutions for Puerto's digital agency team.

---

## Table of Contents

- [Installation Issues](#installation-issues)
- [Plugin Loading Issues](#plugin-loading-issues)
- [Agent Invocation Issues](#agent-invocation-issues)
- [Command Issues](#command-issues)
- [Performance Issues](#performance-issues)
- [Configuration Issues](#configuration-issues)
- [Error Reference](#error-reference)

---

## Installation Issues

### Issue: "Marketplace not found"

**Symptom:**
```
Error: Marketplace 'puerto' not found
```

**Solution:**
```bash
# Add Puerto marketplace
/plugin marketplace add bandofai/puerto

# Verify it's added
/plugin marketplace list

# You should see: bandofai/puerto
```

---

### Issue: "Plugin not found"

**Symptom:**
```
Error: Plugin 'engineering@puerto' not found
```

**Solutions:**

**1. Refresh marketplace:**
```bash
/plugin marketplace refresh
```

**2. Verify marketplace is added:**
```bash
/plugin marketplace list
```

**3. Check plugin name spelling:**
Department plugins:
- `engineering@puerto`
- `design@puerto`
- `marketing@puerto`
- `product@puerto`
- `sales@puerto`
- `operations@puerto`
- `leadership@puerto`
- `essentials@puerto`

**4. Update marketplace:**
```bash
/plugin marketplace update puerto
```

---

### Issue: Installation hangs or times out

**Symptom:** Installation command doesn't complete

**Solutions:**

**1. Check network connection**
```bash
# Test GitHub connectivity
curl -I https://github.com/bandofai/puerto
```

**2. Clear cache and retry:**
```bash
# Remove cached data
rm -rf ~/.claude/cache/puerto

# Reinstall
/plugin install engineering@puerto
```

**3. Install with verbose logging:**
```bash
/plugin install engineering@puerto --verbose
```

---

## Plugin Loading Issues

### Issue: Plugin installed but not loading

**Symptom:** Plugin shows as installed but agents/commands don't work

**Solutions:**

**1. Verify installation:**
```bash
/plugin list @puerto
```

**2. Check plugin info:**
```bash
/plugin info engineering@puerto
```

**3. Restart Claude Code:**
- Close and reopen Claude Code completely
- Re-run your command

**4. Check Claude Code logs:**
```bash
# macOS/Linux
tail -f ~/.claude/logs/main.log

# Look for error messages related to Puerto or the specific plugin
```

---

### Issue: "Plugin failed to load" error

**Symptom:**
```
Error: Plugin 'engineering@puerto' failed to load
```

**Solutions:**

**1. Check plugin.json validity:**
```bash
# Navigate to plugin directory
cd ~/.claude/plugins/puerto/engineering

# Validate JSON
cat plugin.json | python3 -m json.tool
```

**2. Reinstall the plugin:**
```bash
/plugin uninstall engineering@puerto
/plugin install engineering@puerto
```

**3. Check file permissions:**
```bash
# Ensure plugin files are readable
ls -la ~/.claude/plugins/puerto/engineering/
```

---

## Agent Invocation Issues

### Issue: Agent not responding

**Symptom:** Invoke an agent but get no response

**Solutions:**

**1. Verify agent path:**
```
Correct format: [department]/[role-name]
✅ engineering/frontend-engineer
❌ frontend-engineer
❌ engineering-frontend-engineer
```

**2. Check if department is installed:**
```bash
/plugin list @puerto
```

**3. Verify agent exists:**
```bash
/plugin info engineering@puerto
# Look for list of agents
```

**4. Check agent file:**
```bash
# Verify agent markdown file exists
ls ~/.claude/plugins/puerto/engineering/agents/frontend-engineer.md
```

---

### Issue: Wrong agent responds

**Symptom:** Invoked `engineering/frontend-engineer` but got `engineering/backend-engineer`

**Solutions:**

**1. Check invocation pattern:**
Ensure exact match:
```
✅ engineering/frontend-engineer
❌ engineering/frontend
❌ frontend-engineer
```

**2. Clear any CLAUDE.md routing:**
If you have CLAUDE.md with routing rules, they might override:
```bash
# Check for CLAUDE.md
cat .claude/CLAUDE.md

# Look for conflicting routing rules
```

**3. Restart Claude Code:**
Sometimes caching issues cause wrong routing.

---

## Command Issues

### Issue: Slash command not found

**Symptom:**
```
Error: Command '/brainstorm' not found
```

**Solutions:**

**1. Verify essentials plugin is installed:**
```bash
/plugin list @puerto
# Should see: essentials@puerto
```

**2. Install essentials:**
```bash
/plugin install essentials@puerto
```

**3. Restart Claude Code after installation**

**4. Check command spelling:**
```bash
# Correct commands from essentials:
/brainstorm
/implement
```

---

### Issue: Command executes but errors

**Symptom:** Command runs but returns an error

**Solutions:**

**1. Check command syntax:**
```bash
# Most commands need an argument
/brainstorm feature-name
/implement requirement-id
```

**2. Check logs for details:**
```bash
tail -f ~/.claude/logs/main.log
```

**3. Verify requirements directory exists:**
```bash
# For /brainstorm and /implement
ls .requirements/
```

---

## Performance Issues

### Issue: Slow plugin loading

**Symptom:** Plugins take a long time to load

**Solutions:**

**1. Only install needed departments:**
```bash
# Don't install all 8 if you only need 2-3
/plugin uninstall marketing@puerto
/plugin uninstall sales@puerto
```

**2. Clear plugin cache:**
```bash
rm -rf ~/.claude/cache/puerto
```

**3. Check disk space:**
```bash
df -h ~/.claude/
# Each department is ~50-100MB
```

---

### Issue: High memory usage

**Symptom:** Claude Code using excessive RAM

**Solutions:**

**1. Reduce installed plugins:**
```bash
# Uninstall unused departments
/plugin list @puerto
/plugin uninstall <unused-dept>@puerto
```

**2. Restart Claude Code periodically**

**3. Close unused projects in Claude Code**

---

## Configuration Issues

### Issue: CLAUDE.md routing not working

**Symptom:** Auto-routing not invoking correct agents

**Solutions:**

**1. Verify CLAUDE.md exists:**
```bash
cat .claude/CLAUDE.md
# or
cat CLAUDE.md
```

**2. Check routing rule format:**
```markdown
## Task Routing

- Engineering tasks → engineering/engineering-lead
- Design tasks → design/design-lead
- Marketing campaigns → marketing/marketing-director
```

**3. Validate with claude-md-master:**
```bash
/plugin install claude-md-master@puerto

# Then ask Claude:
"Validate my CLAUDE.md configuration"
```

---

### Issue: Skills not loading

**Symptom:** Agents don't reference skills properly

**Solutions:**

**1. Verify skills directory:**
```bash
ls ~/.claude/plugins/puerto/engineering/skills/
# Should see SKILL.md files
```

**2. Check skill file format:**
```bash
# Skills should be markdown files
cat ~/.claude/plugins/puerto/engineering/skills/frontend-development/SKILL.md
```

**3. Reinstall department:**
```bash
/plugin uninstall engineering@puerto
/plugin install engineering@puerto
```

---

## Error Reference

### Common Error Codes

| Error | Meaning | Solution |
|-------|---------|----------|
| `MARKETPLACE_NOT_FOUND` | Marketplace not added | Run `/plugin marketplace add bandofai/puerto` |
| `PLUGIN_NOT_FOUND` | Plugin doesn't exist or typo | Check spelling, run `/plugin marketplace refresh` |
| `PLUGIN_LOAD_FAILED` | Corrupt plugin files | Reinstall plugin |
| `AGENT_NOT_FOUND` | Agent path incorrect | Use format: `[department]/[role-name]` |
| `COMMAND_NOT_FOUND` | Command not installed | Install required plugin (usually `essentials`) |
| `SKILL_MISSING` | Skill file not found | Reinstall department plugin |
| `PERMISSION_DENIED` | File permission issue | Check file permissions in `~/.claude/plugins` |

---

### Error: "Operation not permitted"

**Symptom:**
```
Error: operation not permitted
```

**Solutions:**

**1. Check file permissions:**
```bash
ls -la ~/.claude/plugins/puerto/
```

**2. Fix permissions:**
```bash
chmod -R 755 ~/.claude/plugins/puerto/
```

**3. Check disk space:**
```bash
df -h ~/.claude/
```

---

### Error: "Cannot read property"

**Symptom:**
```
Error: Cannot read property 'agents' of undefined
```

**Solutions:**

**1. Validate plugin.json:**
```bash
cd ~/.claude/plugins/puerto/[department]
python3 -c "import json; print(json.load(open('plugin.json')))"
```

**2. Reinstall plugin:**
```bash
/plugin uninstall [department]@puerto
/plugin install [department]@puerto
```

---

## Advanced Troubleshooting

### Collecting Debug Information

**1. System info:**
```bash
# Claude Code version
claude --version

# OS version
uname -a  # macOS/Linux
ver  # Windows

# Node version (if relevant)
node --version
```

**2. Plugin info:**
```bash
# List installed
/plugin list @puerto

# Get plugin details
/plugin info engineering@puerto
```

**3. Check logs:**
```bash
# Main log
tail -n 100 ~/.claude/logs/main.log

# Error log
tail -n 100 ~/.claude/logs/error.log

# Plugin-specific logs
ls ~/.claude/logs/plugins/puerto/
```

**4. Directory structure:**
```bash
# Verify structure
tree -L 3 ~/.claude/plugins/puerto/
```

---

### Reset Puerto Completely

**Nuclear option - removes all Puerto data:**

```bash
# 1. Uninstall all Puerto plugins
/plugin uninstall @puerto

# 2. Remove marketplace
/plugin marketplace remove puerto

# 3. Clear cache
rm -rf ~/.claude/cache/puerto

# 4. Remove plugin files
rm -rf ~/.claude/plugins/puerto

# 5. Restart Claude Code

# 6. Reinstall from scratch
/plugin marketplace add bandofai/puerto
/plugin install essentials@puerto
```

---

## Getting Help

If you're still stuck:

1. **Search GitHub Issues:** [github.com/bandofai/puerto/issues](https://github.com/bandofai/puerto/issues)
2. **Create New Issue:** Include:
   - Error message (full text)
   - Department/plugin name
   - Claude Code version
   - OS and version
   - Steps to reproduce
   - Logs (if applicable)

3. **Check Documentation:**
   - [README.md](README.md)
   - [FAQ](docs/user-guide/faq.md)
   - [TEAM-STRUCTURE.md](TEAM-STRUCTURE.md)
   - [MIGRATION.md](MIGRATION.md)

---

## Quick Fixes Checklist

Before opening an issue, try:

- [ ] Restart Claude Code
- [ ] Refresh marketplace: `/plugin marketplace refresh`
- [ ] Verify plugin installed: `/plugin list @puerto`
- [ ] Check spelling of department/agent names
- [ ] Clear cache: `rm -rf ~/.claude/cache/puerto`
- [ ] Reinstall plugin
- [ ] Check logs: `~/.claude/logs/main.log`
- [ ] Verify disk space available
- [ ] Update to latest Claude Code version

---

**Last Updated:** 2025-11-03
**Version:** 1.0.0
