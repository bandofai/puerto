# Installation Guide

This guide covers everything you need to know about installing and configuring Puerto and its plugins.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installing Puerto Marketplace](#installing-puerto-marketplace)
- [Installing Plugins](#installing-plugins)
- [Configuration](#configuration)
- [Managing Plugins](#managing-plugins)
- [Troubleshooting](#troubleshooting)

## Prerequisites

### Required
- **Claude Code** - Puerto is a marketplace for Claude Code plugins
- Internet connection for downloading plugins

### Optional (for plugin development)
- **Node.js >= 18.0.0** - Required only if you're creating or testing plugins
- **Git** - For cloning the Puerto repository

## Installing Puerto Marketplace

### Method 1: Using Claude Code CLI (Recommended)

Add Puerto to your marketplace list:

```bash
/plugin marketplace add bandofai/puerto
```

This registers Puerto as an available marketplace in Claude Code.

### Method 2: Manual Configuration

Add Puerto to your Claude Code configuration manually:

1. Open your Claude Code settings
2. Add to marketplaces:

```json
{
  "marketplaces": [
    {
      "name": "puerto",
      "url": "https://github.com/bandofai/puerto"
    }
  ]
}
```

### Verify Installation

List available marketplaces:

```bash
/plugin marketplace list
```

You should see `puerto` in the list.

## Installing Plugins

Install plugins globally to make them available across all projects.

### Installing a Plugin

```bash
/plugin install <plugin-name>@puerto
```

**Examples:**

```bash
# Install essentials plugin
/plugin install essentials@puerto

# Install multiple plugins
/plugin install frontend-developer@puerto
/plugin install backend-architect@puerto
/plugin install data-scientist@puerto
```

### How It Works

- Plugin is downloaded to your Claude Code global plugin directory
- Available immediately in all projects
- Updates are manual (you control when to update)

## Configuration

### Multiple Marketplaces

You can add multiple marketplaces to Claude Code:

```bash
/plugin marketplace add bandofai/puerto
/plugin marketplace add org/other-marketplace
```

Then install plugins from any marketplace:

```bash
/plugin install essentials@puerto
/plugin install some-plugin@other-marketplace
```

## Managing Plugins

### List Installed Plugins

```bash
# All installed plugins
/plugin list

# Plugins from specific marketplace
/plugin list puerto
```

### Update Plugins

```bash
# Update a specific plugin
/plugin update essentials@puerto

# Update all plugins from Puerto
/plugin update @puerto
```

### Uninstall Plugins

```bash
# Uninstall a plugin
/plugin uninstall essentials
```

### Check Plugin Info

```bash
# View plugin details
/plugin info essentials@puerto
```

### Search for Plugins

```bash
# Search Puerto marketplace
/plugin search frontend @puerto
```

Or browse the [Plugin Catalog](plugins/by-category.md) in documentation.

## Troubleshooting

### Plugin Not Found

**Problem:** `/plugin install myname@puerto` says plugin not found.

**Solutions:**
1. Verify plugin exists: [Complete Plugin List](plugins/complete-list.md)
2. Check marketplace is registered: `/plugin marketplace list`
3. Update marketplace cache: `/plugin marketplace update puerto`

### Plugin Not Loading

**Problem:** Plugin installed but commands/agents not available.

**Solutions:**
1. Restart Claude Code
2. Check plugin is installed: `/plugin list`
3. Check Claude Code logs for errors

### Permission Errors

**Problem:** Cannot install plugin due to permissions.

**Solutions:**
1. Check file permissions on Claude Code plugin directory
2. Run Claude Code with appropriate permissions

### Network Issues

**Problem:** Plugin download fails.

**Solutions:**
1. Check internet connection
2. Verify GitHub access (Puerto is hosted on GitHub)
3. Check corporate firewall/proxy settings
4. Try again later (GitHub may be temporarily unavailable)

## Advanced Configuration

### Custom Plugin Sources

While not common, you can fork Puerto and use your custom fork:

```bash
/plugin marketplace add myorg/puerto-fork
```

## Next Steps

- **[Browse Plugins](plugins/by-category.md)** - Discover available plugins
- **[User Guide](user-guide/index.md)** - Learn how to use plugins
- **[Configuration Guide](user-guide/configuring-plugins.md)** - Advanced configuration
- **[Troubleshooting](user-guide/troubleshooting.md)** - Solve common issues
- **[FAQ](user-guide/faq.md)** - Frequently asked questions

## Need More Help?

- **[Troubleshooting Guide](user-guide/troubleshooting.md)** - Detailed problem-solving
- **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Report bugs
- **[Official Claude Code Docs](https://docs.claude.com/en/docs/claude-code/plugins)** - Plugin system documentation
