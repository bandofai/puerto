# Frequently Asked Questions
> Part of the [User Guide](index.md).

Common questions about Puerto and Claude Code plugins.

## General Questions

### What is Puerto?

Puerto is a curated marketplace of Claude Code plugins, offering 140+ plugins that extend Claude's capabilities with commands, agents, skills, hooks, and MCP servers.

### What are Claude Code plugins?

Plugins extend Claude Code with specialized functionality - from semantic code navigation to design-to-code generation. See [official documentation](https://docs.claude.com/en/docs/claude-code/plugins).

### Is Puerto free?

Yes, Puerto is open source and free to use under the MIT license.

### Who maintains Puerto?

Puerto is maintained by [Band of AI](https://github.com/bandofai) with community contributions.

## Installation

### How do I install Puerto?

```bash
/plugin marketplace add bandofai/puerto
/plugin install <plugin-name>@puerto
```

See [Getting Started](../getting-started.md).


### Can I use multiple marketplaces?

Yes, add multiple marketplaces:

```bash
/plugin marketplace add bandofai/puerto
/plugin marketplace add org/other-marketplace
```

### How do I update plugins?

```bash
/plugin update <name>@puerto  # Update one
/plugin update @puerto        # Update all from Puerto
```

## Plugin Usage

### How do I know what a plugin does?

Check:
1. Plugin README in `plugins/<name>/README.md`
2. [Plugin Catalog](../plugins/by-category.md)
3. `/plugin info <name>@puerto`

### Do plugins slow down Claude?

Minimal impact. Plugins load on-demand. Only install what you need.

### Can I disable a plugin temporarily?

Uninstall it temporarily with `/plugin uninstall <name>`, then reinstall when needed.

### How many plugins should I install?

Start with essentials, add as needed. Most projects use 3-10 plugins.

## Configuration

### Can I configure plugins?

Some plugins support configuration via their own config files. Check plugin documentation for details.

## Plugin Types

### What's the difference between commands and agents?

**Commands:** Slash commands you invoke (e.g., `/brainstorm`)
**Agents:** Autonomous subagents Claude invokes (e.g., `component-builder`)

### What are skills?

Knowledge libraries that agents reference for better results. See [Using Skills](using-skills.md).

### What are MCP servers?

External tool integrations (e.g., Serena for code navigation). See [MCP Servers](../architecture/plugin-types.md#mcp-servers).

### Can one plugin have multiple types?

Yes! Many plugins combine commands, agents, skills, and templates.

## Development

### Can I create my own plugin?

Yes! See [Plugin Development Guide](../plugin-development/quickstart.md).

### How do I submit a plugin to Puerto?

See [Contributing Guide](../contributing/submitting-plugins.md).

### Do I need to know TypeScript?

No, plugins are configured with JSON and Markdown. TypeScript only if creating complex MCP servers.

### Can I fork Puerto?

Yes, it's MIT licensed. You can fork and customize.

## Troubleshooting

### Plugin not found

1. Check spelling
2. Verify marketplace: `/plugin marketplace list`
3. Update: `/plugin marketplace update puerto`
4. See [Complete Plugin List](../plugins/complete-list.md)

### Plugin not loading

1. Verify installed: `/plugin list`
2. Restart Claude Code
3. Review logs

### Command not working

1. Verify plugin installed
2. Check command syntax in plugin docs
3. Restart Claude Code

See [Troubleshooting Guide](troubleshooting.md) for more.

## Performance

### Do I need to install all plugins?

No! Only install what you need. More plugins = more to load.

### Which plugins are essential?

- **essentials** - Core MCP servers and requirements management
- **subagent-creator** - If creating agents

Beyond that, choose based on your work.

### How do I optimize performance?

✅ Only install needed plugins
✅ Disable unused plugins
✅ Keep plugins updated

## Security

### Are plugins safe?

Puerto plugins are:
- ✅ Reviewed before inclusion
- ✅ Open source (you can inspect)
- ✅ Follow security best practices
- ✅ Validated by automated checks

### Can plugins access my files?

Agents have limited tool access defined in their configuration. Review plugin documentation for tool usage.

### Do plugins send data externally?

Most don't. MCP servers may connect to external services (documented in plugin README).

### Should I trust all plugins?

Review plugin code before use in sensitive projects. Puerto reviews but doesn't guarantee security.

## Compatibility

### What Claude Code version do I need?

Most plugins work with recent Claude Code versions. Check plugin README for specific requirements.

### Do plugins work on all platforms?

Yes, plugins are platform-agnostic. MCP servers may have platform-specific requirements (documented).

### Can I use Puerto with other marketplaces?

Yes, you can add multiple marketplaces using `/plugin marketplace add`.

## Support

### Where do I get help?

1. **[Documentation](../README.md)** - Start here
2. **[Troubleshooting Guide](troubleshooting.md)** - Common issues
3. **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Report bugs
4. **Plugin README** - Plugin-specific help

### How do I report a bug?

1. Search [existing issues](https://github.com/bandofai/puerto/issues)
2. Create new issue with:
   - Plugin name/version
   - Claude Code version
   - Error message
   - Steps to reproduce

### Can I request a plugin?

Yes! Create a [feature request](https://github.com/bandofai/puerto/issues/new) or contribute one yourself.

### How do I contribute?

See [Contributing Guide](../contributing/index.md).

## Next Steps

- **[Getting Started](../getting-started.md)** - Quick start guide
- **[User Guide](browsing-plugins.md)** - Complete user documentation
- **[Plugin Catalog](../plugins/by-category.md)** - Browse plugins
- **[Troubleshooting](troubleshooting.md)** - Solve problems
