# Installing Plugins
> Part of the [User Guide](index.md).

Learn how to install Puerto plugins in Claude Code.

## Quick Reference

| Action | Command |
|--------|---------|
| Install plugin | `/plugin install <name>@puerto` |
| List installed | `/plugin list` |
| Update plugin | `/plugin update <name>@puerto` |
| Uninstall plugin | `/plugin uninstall <name>` |

## Prerequisites

Before installing plugins, ensure:

1. **Puerto marketplace is registered:**
   ```bash
   /plugin marketplace add bandofai/puerto
   ```

2. **Verify registration:**
   ```bash
   /plugin marketplace list
   ```

   You should see `puerto` in the list.

## Installing Plugins

Install plugins to make them available across all your projects.

### Install a Single Plugin

```bash
/plugin install essentials@puerto
```

**What happens:**
- Plugin downloads from Puerto marketplace
- Installs to Claude Code plugin directory
- Available immediately in all projects
- Persists across Claude Code restarts

### Install Multiple Plugins

```bash
/plugin install essentials@puerto
/plugin install engineering@puerto
/plugin install design@puerto
```

Or in one line (if supported):

```bash
/plugin install essentials@puerto engineering@puerto design@puerto
```

## Managing Installed Plugins

### List All Installed Plugins

```bash
/plugin list
```

Shows:
- Plugin name
- Version
- Marketplace

### List Plugins from Puerto

```bash
/plugin list puerto
```

### Check Plugin Details

```bash
/plugin info essentials@puerto
```

Shows:
- Description
- Version
- Author
- Features (commands, agents, skills, etc.)
- Installation status

### Update a Plugin

```bash
# Update specific plugin
/plugin update essentials@puerto

# Update all plugins from Puerto
/plugin update @puerto

# Update all plugins
/plugin update
```

### Uninstall a Plugin

```bash
/plugin uninstall essentials
```

## Installation Examples

### Minimal Setup

Just the essentials:

```bash
/plugin install essentials@puerto
```

### Full-Stack Web Development

```bash
/plugin install essentials@puerto
/plugin install engineering@puerto
/plugin install design@puerto
```

### Data Science & Analytics

```bash
/plugin install essentials@puerto
/plugin install engineering@puerto
/plugin install product@puerto
```

### Marketing Team

```bash
/plugin install essentials@puerto
/plugin install marketing@puerto
/plugin install design@puerto
```

## Troubleshooting Installation

### Plugin Not Found

**Error:** "Plugin 'xyz' not found in marketplace 'puerto'"

**Solutions:**
1. Verify plugin name: [Complete Plugin List](../plugins/complete-list.md)
2. Check typos in command/config
3. Update marketplace cache: `/plugin marketplace update puerto`

### Installation Fails

**Error:** Plugin download or installation fails

**Solutions:**
1. Check internet connection
2. Verify GitHub access
3. Try again (temporary network issue)
4. Check Claude Code logs for details

### Plugin Not Loading

**Error:** Plugin installed but not active

**Solutions:**
1. Restart Claude Code
2. Verify installation: `/plugin list`
3. Review Claude Code error logs

### Permission Errors

**Error:** Cannot write to plugin directory

**Solutions:**
1. Check file permissions
2. Run Claude Code with appropriate access

## Best Practices

✅ Install essentials first
✅ Add tools as you need them
✅ Keep plugins updated
✅ Only install plugins you actually use
✅ Review plugin documentation before installing

## Next Steps

- **[Configure Plugins](configuring-plugins.md)** - Plugin options
- **[Use Commands](using-commands.md)** - Command usage
- **[Use Agents](using-agents.md)** - Working with agents
- **[Troubleshooting](troubleshooting.md)** - Solve issues

## Need Help?

- **[FAQ](faq.md)** - Common questions
- **[Troubleshooting](troubleshooting.md)** - Detailed solutions
- **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Report problems
