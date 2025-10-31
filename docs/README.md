# Puerto Documentation

<div align="center">
  <img src="logo.png" alt="Puerto Logo" width="200"/>
  <p><strong>A curated marketplace of Claude Code plugins</strong></p>
</div>

Welcome to the Puerto documentation! Choose your path based on what you want to do:

## Quick Links

| I want to... | Start here |
|-------------|-----------|
| **Use plugins in my projects** | [Getting Started](getting-started.md) → [User Guide](user-guide/index.md) |
| **Create a new plugin** | [Plugin Development Quickstart](plugin-development/quickstart.md) |
| **Browse available plugins** | [Plugin Catalog](plugins/by-category.md) |
| **Contribute to Puerto** | [Contributing Guide](contributing/index.md) |
| **Understand the architecture** | [Architecture Overview](architecture/overview.md) |
| **Look up technical details** | [Reference Index](reference/index.md) |
| **See everything at a glance** | [Documentation Map](DOCUMENTATION_SUMMARY.md) |

---

## For Users

Learn how to discover, install, and use Puerto plugins:

- **[Getting Started](getting-started.md)** - Install Puerto and your first plugin in 5 minutes
- **[User Guide Overview](user-guide/index.md)** - Task-based navigation for everyday workflows
- **[Installation Guide](installation.md)** - Installing plugins and marketplace setup
  - [Browsing Plugins](user-guide/browsing-plugins.md)
  - [Installing Plugins](user-guide/installing-plugins.md)
  - [Configuring Plugins](user-guide/configuring-plugins.md)
  - [Using Commands](user-guide/using-commands.md)
  - [Using Agents](user-guide/using-agents.md)
  - [Using Skills](user-guide/using-skills.md)
  - [Troubleshooting](user-guide/troubleshooting.md)
  - [FAQ](user-guide/faq.md)

---

## For Plugin Developers

Everything you need to create plugins for Puerto:

- **[Development Quickstart](plugin-development/quickstart.md)** - Create your first plugin in 10 minutes
- **[Quick Reference](plugin-development/quick-reference.md)** - Cheat sheet for common workflows ⚡
- **[Plugin Manager Examples](plugin-development/plugin-manager-examples.md)** - Real-world `/plugin-manager` usage
- **[Plugin Development Guide](plugin-development/index.md)** - Complete developer documentation
  - [Plugin Structure](plugin-development/plugin-structure.md)
  - [Plugin Manifest](plugin-development/plugin-manifest.md)
  - [Creating Commands](plugin-development/commands.md)
  - [Building Agents](plugin-development/agents.md)
  - [Developing Skills](plugin-development/skills.md)
  - [Using Templates](plugin-development/templates.md)
  - [Integrating MCP Servers](plugin-development/mcp-servers.md)
  - [Testing & Validation](plugin-development/testing-and-validation.md)
  - [Publishing](plugin-development/publishing.md)
  - [Best Practices](plugin-development/best-practices.md)
  - [Debugging](plugin-development/debugging.md)
- **[Examples](examples/)** - Real plugin examples
  - [Minimal Plugin](examples/minimal-plugin/)
  - [Command Plugin](examples/command-plugin/)
  - [Agent Plugin](examples/agent-plugin/)
  - [Skill Plugin](examples/skill-plugin/)
  - [MCP Plugin](examples/mcp-plugin/)
  - [Full-Featured Plugin](examples/full-featured-plugin/)

---

## Plugin Catalog

Browse 140+ available plugins:

- **[By Category](plugins/by-category.md)** - Organized by squad (Web Dev, Data, Marketing, etc.)
- **[By Feature](plugins/by-feature.md)** - Filter by commands, agents, skills, or MCP servers
- **[Featured Plugins](plugins/featured.md)** - Essential plugins to get started
- **[Complete List](plugins/complete-list.md)** - Alphabetical list of all plugins

---

## For Contributors

Help make Puerto better:

- **[Contributing Guide](contributing/index.md)** - How to contribute overview
- **[Submitting Plugins](contributing/submitting-plugins.md)** - Plugin submission process
- **[Pull Request Guidelines](contributing/pull-request-guidelines.md)** - PR requirements
- **[Review Process](contributing/review-process.md)** - What reviewers look for
- **[Code Style](contributing/code-style.md)** - Coding conventions
- **[Documentation Style](contributing/documentation-style.md)** - Doc writing standards
- **[Community Guidelines](contributing/community-guidelines.md)** - Code of conduct

---

## Technical Documentation

Deep dive into Puerto's architecture:

- **[Architecture Overview](architecture/overview.md)** - System design and components
- **[Marketplace System](architecture/marketplace-system.md)** - How the marketplace works
- **[Catalog Generation](architecture/catalog-generation.md)** - Auto-catalog process
- **[Plugin Loading](architecture/plugin-loading.md)** - Plugin loading mechanism
- **[Plugin Types](architecture/plugin-types.md)** - Commands, agents, skills, hooks, MCP
- **[CI/CD](architecture/ci-cd.md)** - GitHub Actions workflow

---

## Reference Library

Complete technical specifications:

- **[Reference Index](reference/index.md)** - Quick links to every schema and format guide
- **[plugin.json Schema](reference/plugin-json-schema.md)** - Plugin manifest specification
- **[marketplace.json Schema](reference/marketplace-json-schema.md)** - Marketplace manifest
- **[Agent Frontmatter](reference/agent-frontmatter.md)** - Agent metadata format
- **[Command Format](reference/command-format.md)** - Command file format
- **[Skill Format](reference/skill-format.md)** - Skill file format
- **[Directory Structure](reference/directory-structure.md)** - Standard file layout
- **[Validation Rules](reference/validation-rules.md)** - Plugin validation requirements

---

## Getting Help

- **[FAQ](user-guide/faq.md)** - Common questions and answers
- **[Troubleshooting](user-guide/troubleshooting.md)** - Solve common issues
- **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Report bugs or request features
- **[Official Claude Code Docs](https://docs.claude.com/en/docs/claude-code/plugins)** - Claude Code plugin system

---

## About Puerto

Puerto is a curated marketplace that makes it easy to discover and use Claude Code plugins. With 140+ plugins covering everything from web development to data analysis to personal productivity, Puerto helps you extend Claude's capabilities to match your workflow.

**Key Features:**
- 140+ curated plugins organized by category
- Simple installation (global or per-project)
- Automatic catalog updates via CI/CD
- Built-in validation and quality standards
- Active community contributions

---

## License

Puerto is licensed under the [MIT License](../LICENSE).
