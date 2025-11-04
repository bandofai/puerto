# Plugin Development Guide

Welcome to the Puerto Plugin Development Guide. Learn how to create powerful Claude Code plugins for the Puerto marketplace.

## Quick Navigation

### Getting Started
- **[Quickstart Guide](quickstart.md)** - Create your first plugin in 10 minutes (with `/plugin-manager` or manually)
- **[Quick Reference](quick-reference.md)** - Cheat sheet for common workflows and patterns
- **[Plugin Manager Examples](plugin-manager-examples.md)** - Real-world examples using `/plugin-manager`
- **[Plugin Structure](plugin-structure.md)** - Understanding the file organization
- **[Plugin Manifest](plugin-manifest.md)** - Configuring plugin.json
  - Need exact field definitions? See the [Reference Index](../reference/index.md).

### Plugin Types
- **[Commands](commands.md)** - Creating slash commands
- **[Agents](agents.md)** - Building specialized subagents
- **[Skills](skills.md)** - Developing knowledge libraries
- **[Templates](templates.md)** - Adding file templates
- **[MCP Servers](mcp-servers.md)** - Integrating external tools

### Quality & Publishing
- **[Testing & Validation](testing-and-validation.md)** - Ensuring plugin quality
- **[Publishing](publishing.md)** - Submitting to Puerto
- **[Best Practices](best-practices.md)** - Patterns and anti-patterns
- **[Debugging](debugging.md)** - Troubleshooting plugin issues

## What You Can Build

### Command Plugins
Slash commands that extend Claude's capabilities:
- `/brainstorm` - Requirement gathering
- `/analyze-performance` - Performance analysis
- `/generate-docs` - Documentation generation

### Agent Plugins
Specialized subagents for specific tasks:
- `frontend-engineer` - Build React components
- `api-tester` - Test REST APIs
- `data-analyzer` - Analyze datasets

### Skill Plugins
Knowledge libraries that enhance agents:
- `accessibility-guidelines` - WCAG standards
- `api-design-patterns` - REST best practices
- `testing-strategies` - QA methodologies

### MCP Server Plugins
External tool integrations:
- Serena - Semantic code navigation
- Context7 - Library documentation
- Custom integrations - Your external tools

### Hybrid Plugins
Combine multiple types:
- Commands + Agents + Skills + Templates
- Example: `engineering` plugin

## Development Path

### 1. Learn the Basics
Start here if you're new to plugin development:

**🚀 Fastest Start:**
1. **[Plugin Manager Examples](plugin-manager-examples.md)** - Use `/plugin-manager` to create plugins in < 2 minutes
2. **[Quick Reference](quick-reference.md)** - Common patterns and workflows

**📚 Detailed Learning:**
1. **[Quickstart Guide](quickstart.md)** - Build minimal plugin (with `/plugin-manager` or manually)
2. **[Plugin Structure](plugin-structure.md)** - Understand organization
3. **[Plugin Manifest](plugin-manifest.md)** - Configure metadata

### 2. Choose Your Plugin Type
Pick what you want to build:

**Simple → Complex**
1. **Commands** - Easiest, markdown files
2. **Templates** - Static file templates
3. **Agents** - More complex, requires understanding subagents
4. **Skills** - Documentation-focused
5. **MCP Servers** - Most complex, TypeScript/JavaScript

### 3. Build Your Plugin
Follow the relevant guides:

- **[Creating Commands](commands.md)** - Step-by-step command creation
- **[Building Agents](agents.md)** - Agent architecture and patterns
- **[Developing Skills](skills.md)** - Skill documentation strategies
- **[Adding Templates](templates.md)** - Template organization
- **[Integrating MCP](mcp-servers.md)** - MCP server development

### 4. Test & Validate
Ensure quality:

- **[Testing & Validation](testing-and-validation.md)** - Validation tools and testing strategies
- **[Debugging](debugging.md)** - Fix common issues

### 5. Publish
Share with the community:

- **[Publishing Guide](publishing.md)** - Submission process
- **[Contributing Guidelines](../contributing/submitting-plugins.md)** - PR requirements

## Prerequisites

### Required Knowledge
- Basic understanding of Claude Code
- Markdown (for commands, agents, skills)
- JSON (for configuration)

### Optional Knowledge
- TypeScript/JavaScript (for MCP servers)
- Node.js (for testing locally)
- Git (for version control)

### Tools
- **Claude Code** - For testing plugins
- **Text Editor** - VS Code, Cursor, etc.
- **Git** - For version control (optional but recommended)
- **Node.js >= 18.0.0** - For validation scripts (optional)

## Plugin Development Workflow

### 1. Plan
- Define plugin purpose
- Choose plugin type(s)
- Sketch feature list
- Review existing similar plugins

### 2. Create Structure
```bash
my-plugin/
├── .claude-plugin/
│   └── plugin.json       # Required
├── README.md             # Recommended
├── commands/             # Optional
├── agents/               # Optional
├── skills/               # Optional
└── templates/            # Optional
```

### 3. Implement
- Write plugin.json manifest
- Create commands/agents/skills
- Add templates if needed
- Write README documentation

### 4. Test Locally
```bash
# Validate structure
node scripts/validate-plugin.js my-plugin/

# Test in Claude Code
# Copy to local plugins directory or use local path
```

### 5. Document
- Complete README with:
  - Installation instructions
  - Usage examples
  - Feature list
  - Configuration options

### 6. Submit
- Create Pull Request to Puerto
- Follow review process
- Address feedback
- Celebrate inclusion!

## Examples

Learn from real plugins:

- **[Minimal Plugin](../examples/minimal-plugin/)** - Simplest possible plugin
- **[Command Plugin](../examples/command-plugin/)** - Command-only example
- **[Agent Plugin](../examples/agent-plugin/)** - Agent-based example
- **[Skill Plugin](../examples/skill-plugin/)** - Skill library example
- **[Full-Featured Plugin](../examples/full-featured-plugin/)** - Complete example

Browse Puerto's 140+ plugins for inspiration:
[Plugin Catalog](../plugins/by-category.md)

## Best Practices Preview

✅ **Single Responsibility** - One plugin, one purpose
✅ **Clear Naming** - Descriptive, lowercase-with-hyphens
✅ **Good Documentation** - Detailed README
✅ **Quality Testing** - Validate before submitting
✅ **Follow Conventions** - Match Puerto patterns

Read full [Best Practices Guide](best-practices.md).

## Getting Help

### Resources
- **[Examples Directory](../examples/)** - Working plugin examples
- **[API Reference](../reference/plugin-json-schema.md)** - Complete schemas
- **[Architecture Docs](../architecture/overview.md)** - System internals
- **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Ask questions

### Community
- Review existing plugins for patterns
- Ask questions in GitHub Issues
- Submit PRs with improvements
- Share your plugins!

## Next Steps

Ready to build?

**Want to start right now:**
→ Type `/plugin-manager create` in Claude Code (< 2 minutes)

**New to plugin development:**
→ Start with [Quickstart Guide](quickstart.md) or [Plugin Manager Examples](plugin-manager-examples.md)

**Need a quick reference:**
→ Check the [Quick Reference](quick-reference.md) for common patterns

**Know the basics:**
→ Choose your type: [Commands](commands.md) | [Agents](agents.md) | [Skills](skills.md)

**Ready to publish:**
→ Review [Publishing Guide](publishing.md)

**Need inspiration:**
→ Browse [Plugin Catalog](../plugins/by-category.md)

---

**Happy building!** We're excited to see what you create.
