# Getting Started with Puerto

Get up and running with Puerto in less than 5 minutes! This guide will walk you through installing Puerto and your first plugin.

## Prerequisites

- Claude Code installed
- Node.js >= 18.0.0 (only needed for plugin development)

## Quick Start (5 Minutes)

### Step 1: Add Puerto Marketplace

Add Puerto as a marketplace so you can browse and install plugins:

```bash
/plugin marketplace add bandofai/puerto
```

This registers Puerto in your Claude Code environment.

### Step 2: Install Your First Plugin

Let's install the **Essentials** plugin, which provides powerful MCP servers for semantic code navigation, documentation lookup, and structured reasoning:

```bash
/plugin install essentials@puerto
```

That's it! The plugin is now available globally across all your projects.

### Step 3: Try It Out

The Essentials plugin includes several useful commands. Try one:

```bash
/brainstorm my-feature
```

This starts an interactive Q&A session to help you define a new feature requirement.

## What Just Happened?

1. **Marketplace Registration**: Puerto was added to your marketplace list
2. **Plugin Installation**: The essentials plugin was downloaded and activated
3. **Global Availability**: The plugin's commands, agents, and MCP servers are now available everywhere

## Next Steps

### Explore More Plugins

Browse the [Plugin Catalog](plugins/by-category.md) to discover 140+ plugins organized by category:

- **Web Development**: frontend-developer, backend-architect, api-developer
- **Data & Analytics**: data-scientist, ml-engineer, data-engineer
- **Marketing**: seo-specialist, content-writer, social-media-manager
- **And many more...**


### Understand What You Installed

The **Essentials** plugin includes:

**MCP Servers:**
- **Serena**: Semantic code navigation with LSP-powered symbol search
- **Context7**: Up-to-date documentation from current library versions
- **Sequential Thinking**: Structured reasoning and problem-solving
- **Playwright**: Browser automation with visual testing and PDF generation

**Commands:**
- `/brainstorm <name>` - Define requirements interactively
- `/implement <name>` - Implement requirements systematically
- `/continue [name]` - Resume interrupted work
- `/req-list` - View all requirements
- `/req-update <name>` - Modify requirements
- `/req-tests <name>` - Generate test scenarios

### Explore Plugin Types

Puerto plugins can provide:

- **Commands**: Slash commands like `/brainstorm` or `/implement`
- **Agents**: Specialized subagents for specific tasks
- **Skills**: Reusable knowledge libraries agents can reference
- **MCP Servers**: External tool integrations (like Serena or Context7)
- **Templates**: Pre-built file templates

Learn more in [Plugin Types](architecture/plugin-types.md).

## Common First Steps

### Browse Available Plugins

```bash
# List all plugins from Puerto
/plugin list puerto
```

Or browse visually in the [Plugin Catalog](plugins/by-category.md).

### Install Multiple Plugins

```bash
/plugin install frontend-developer@puerto
/plugin install backend-architect@puerto
/plugin install data-scientist@puerto
```

### Check Installed Plugins

```bash
/plugin list
```

### Update a Plugin

```bash
/plugin update essentials@puerto
```

### Remove a Plugin

```bash
/plugin uninstall essentials
```


## Need Help?

- **[User Guide](user-guide/index.md)** - Complete usage navigation
- **[FAQ](user-guide/faq.md)** - Common questions
- **[Troubleshooting](user-guide/troubleshooting.md)** - Solve common issues
- **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Report problems

## Ready for More?

### For Users:
- [Browse the Plugin Catalog](plugins/by-category.md)
- [Learn about Configuration](user-guide/configuring-plugins.md)
- [Read the User Guide](user-guide/index.md)

### For Developers:
- [Create Your First Plugin](plugin-development/quickstart.md)
- [Understand Plugin Structure](plugin-development/plugin-structure.md)
- [View Example Plugins](examples/)

### For Contributors:
- [Contributing Guide](contributing/index.md)
- [Submission Process](contributing/submitting-plugins.md)
- [Community Guidelines](contributing/community-guidelines.md)

---

**Congratulations!** You're ready to supercharge your Claude Code workflow with Puerto plugins.
