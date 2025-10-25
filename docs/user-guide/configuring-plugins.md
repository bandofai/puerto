# Configuring Plugins
> Part of the [User Guide](index.md).

Learn how to configure individual Puerto plugins and customize their behavior.

## Plugin-Specific Configuration

Most Puerto plugins work out-of-the-box without configuration. However, some plugins support optional configuration files for customization.

### Configuration Locations

Plugins may use their own configuration files:
- Plugin-specific config files (documented in each plugin's README)
- Environment variables
- Command-line arguments

Check each plugin's documentation for available configuration options.

## Common Configuration Patterns

### MCP Server Configuration

Plugins that include MCP servers (like Essentials) may have their own configuration:

```bash
# Example: Configure Context7 MCP server
# Check the plugin's README for specific configuration options
```

### Agent Behavior

Some agents support customization through:
- **Prompt parameters** - Pass options when invoking agents
- **Environment setup** - Configure tools and dependencies
- **Skill customization** - Edit skills in the plugin directory (advanced)

## Plugin-Specific Examples

### Essentials Plugin

The Essentials plugin includes MCP servers that auto-configure based on your environment:
- **Serena**: Auto-detects language servers
- **Context7**: Uses default documentation sources
- **Sequential Thinking**: No configuration needed
- **Playwright**: Auto-installs browser binaries on first use

### Development Plugins

Development plugins (frontend-developer, backend-architect, etc.) auto-detect your project setup from:
- `package.json` for JavaScript/TypeScript
- `pyproject.toml` for Python
- `Cargo.toml` for Rust
- Framework configuration files

No manual configuration required.

### Data Plugins

Data science and analytics plugins may support:
- Python environment detection
- Database connection strings (via environment variables)
- Output format preferences

Check each plugin's README for details.

## Best Practices

✅ **Use defaults first** - Most plugins work without configuration
✅ **Read plugin docs** - Check README for configuration options
✅ **Use environment variables** - For secrets and credentials
✅ **Document configuration** - Note any custom setup in your project README

❌ **Don't over-configure** - Keep it simple unless needed
❌ **Don't hardcode secrets** - Use environment variables instead

## Finding Configuration Options

To find configuration options for a plugin:

1. **Check the plugin README**:
   ```bash
   # View plugin info
   /plugin info <plugin-name>@puerto
   ```

2. **Browse plugin directory**:
   - Look in the plugin's README.md
   - Check for example configuration files
   - Review agent documentation

3. **Check plugin documentation**:
   - Visit the plugin's section in [Plugin Catalog](../plugins/by-category.md)
   - Read the plugin's README in the repository

## Environment Variables

Some plugins use environment variables for configuration:

```bash
# Example: Database connection
export DATABASE_URL="postgresql://localhost/mydb"

# Example: API keys
export OPENAI_API_KEY="your-key-here"
```

Check each plugin's documentation for supported environment variables.

## Troubleshooting Configuration

### Plugin Not Working as Expected

1. **Check plugin README** - Review configuration options
2. **Verify environment** - Ensure required tools are installed
3. **Check logs** - Review Claude Code error logs
4. **Reset to defaults** - Remove custom configuration and test

### Configuration Not Applied

1. **Restart Claude Code** - Reload to apply changes
2. **Check file location** - Ensure config file is in correct location
3. **Validate syntax** - Check JSON/YAML syntax if applicable
4. **Review plugin docs** - Confirm configuration format

## Next Steps

- **[Using Commands](using-commands.md)** - Invoke slash commands
- **[Using Agents](using-agents.md)** - Work with specialized agents
- **[Troubleshooting](troubleshooting.md)** - Solve common issues

## Need Help?

- **[FAQ](faq.md)** - Common questions
- **[Troubleshooting](troubleshooting.md)** - Detailed solutions
- **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Report problems
