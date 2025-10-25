# Troubleshooting
> Part of the [User Guide](index.md).

Common issues and solutions for Puerto plugins.

## Installation Issues

### Plugin Not Found

**Symptom:** `/plugin install xyz@puerto` fails with "not found"

**Solutions:**
1. **Verify plugin name** - Check [Complete Plugin List](../plugins/complete-list.md)
2. **Update marketplace** - `/plugin marketplace update puerto`
3. **Check marketplace** - `/plugin marketplace list` (should show puerto)
4. **Register marketplace** - `/plugin marketplace add bandofai/puerto`

### Cannot Install Plugin

**Symptom:** Installation command fails

**Solutions:**
1. **Check internet** - Ensure GitHub access
2. **Check permissions** - Verify write access to Claude Code directory
3. **Check logs** - Review Claude Code error logs

### Plugin Not Loading

**Symptom:** Plugin installed but not active

**Solutions:**
1. **Restart Claude Code** - Reload to activate plugin
2. **Verify installation** - `/plugin list` should show plugin
3. **Check version** - Ensure compatible Claude Code version


## Usage Issues

### Command Not Found

**Symptom:** `/command` not recognized

**Solutions:**
1. **Verify plugin installed** - `/plugin list`
2. **Check command name** - Review plugin documentation
3. **Restart Claude Code** - Reload command registry
4. **Check spelling** - Commands are case-sensitive

### Agent Not Working

**Symptom:** Agent doesn't respond or fails

**Solutions:**
1. **Be specific** - Provide clear task description
2. **Check context** - Provide necessary information
3. **Simplify request** - Break into smaller tasks
4. **Review error** - Check Claude's error message

### Unexpected Behavior

**Symptom:** Plugin works but results unexpected

**Solutions:**
1. **Review documentation** - Check plugin README
2. **Check examples** - See usage examples
3. **Provide context** - Give agent more information
4. **Report issue** - [GitHub Issues](https://github.com/bandofai/puerto/issues)

## Performance Issues

### Slow Plugin Loading

**Symptom:** Plugins take long to load

**Solutions:**
1. **Reduce plugin count** - Only install needed plugins
2. **Check network** - Slow GitHub access affects loading
3. **Update Claude Code** - Ensure latest version

### High Resource Usage

**Symptom:** Claude Code using too much CPU/memory

**Solutions:**
1. **Limit active plugins** - Disable unused plugins
2. **Close unused projects** - Each project loads plugins
3. **Restart Claude Code** - Clear memory leaks
4. **Check plugin issues** - Some plugins may have bugs

## Compatibility Issues

### Claude Code Version

**Symptom:** Plugin incompatible with Claude Code version

**Solutions:**
1. **Update Claude Code** - Get latest version
2. **Check requirements** - Review plugin documentation
3. **Pin older version** - Use compatible plugin version
4. **Report issue** - Plugin may need update

### Plugin Conflicts

**Symptom:** Two plugins interfere with each other

**Solutions:**
1. **Uninstall one** - `/plugin uninstall <name>`
2. **Check command names** - Commands may conflict
3. **Review logs** - Look for error messages
4. **Report issue** - May need plugin updates

## Network Issues

### Cannot Reach GitHub

**Symptom:** "Failed to download plugin"

**Solutions:**
1. **Check internet** - Verify connectivity
2. **Check firewall** - Corporate firewall may block GitHub
3. **Use proxy** - Configure proxy if needed
4. **Try later** - GitHub may be temporarily down

### SSL/Certificate Errors

**Symptom:** Certificate validation fails

**Solutions:**
1. **Update certificates** - System certificate update
2. **Check date/time** - Incorrect system time causes errors
3. **Corporate proxy** - May need proxy configuration
4. **Contact IT** - Corporate network may require setup

## Error Messages

### "Marketplace not found"

**Solution:**
```bash
/plugin marketplace add bandofai/puerto
```

### "Plugin already installed"

**Solution:**
```bash
# Update instead
/plugin update <name>@puerto

# Or uninstall first
/plugin uninstall <name>
/plugin install <name>@puerto
```

### "Permission denied"

**Solution:**
- Check file permissions on Claude Code directory
- Run with appropriate user permissions

### "Cannot parse plugin.json"

**Solution:**
- Plugin has malformed manifest
- Update marketplace: `/plugin marketplace update puerto`
- Report issue if persists

## Getting Help

### Check Documentation

1. **[Installation Guide](../installation.md)** - Installation help
2. **[Configuration Guide](configuring-plugins.md)** - Config help
3. **[FAQ](faq.md)** - Common questions
4. **Plugin README** - Plugin-specific docs

### Search Issues

Check if your issue is already reported:

[Puerto GitHub Issues](https://github.com/bandofai/puerto/issues)

### Report New Issue

If you found a bug:

1. **Search existing issues** - Avoid duplicates
2. **Gather information:**
   - Claude Code version
   - Plugin name and version
   - Error message (if any)
   - Steps to reproduce
3. **Create issue** with details
4. **Be responsive** to questions

### Template for Bug Reports

```markdown
**Plugin:** <plugin-name>
**Version:** <version>
**Claude Code Version:** <version>

**Issue:**
Describe the problem clearly.

**Steps to Reproduce:**
1. Step one
2. Step two
3. Step three

**Expected Behavior:**
What should happen.

**Actual Behavior:**
What actually happens.

**Error Message:**
```
Paste any error messages
```

## Prevention Tips

### Before Installing

✅ **Read documentation** - Know what plugin does
✅ **Check compatibility** - Verify Claude Code version
✅ **Start small** - Install one plugin at a time
✅ **Test thoroughly** - Verify each plugin works

### Best Practices

✅ **Keep backups** - Commit configs to git
✅ **Document setup** - Record plugin choices in README
✅ **Test updates** - Don't auto-update production configs
✅ **Monitor issues** - Watch GitHub for known problems

## Next Steps

- **[FAQ](faq.md)** - Frequently asked questions
- **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Report problems
- **[Plugin Development](../plugin-development/debugging.md)** - Debug plugins
