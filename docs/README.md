# Puerto Documentation

<div align="center">
  <img src="logo.png" alt="Puerto Logo" width="200"/>
  <p><strong>Your AI-powered digital agency team for Claude Code</strong></p>
</div>

Welcome to the Puerto documentation! Choose your path based on what you want to do:

## Quick Links

| I want to... | Start here |
|-------------|-----------|
| **Use Puerto's agency team** | [Getting Started](getting-started.md) → [User Guide](user-guide/index.md) |
| **Optimize Claude for my project** | [Configuring CLAUDE.md](configuring-claude-md.md) ⭐ |
| **Create a custom plugin** | [Plugin Development Quickstart](plugin-development/quickstart.md) |
| **Browse departments & roles** | [Team Structure](../TEAM-STRUCTURE.md) |
| **Contribute to Puerto** | [Contributing Guide](contributing/index.md) |
| **Understand the architecture** | [Architecture Overview](architecture/overview.md) |
| **Look up technical details** | [Reference Index](reference/index.md) |

---

## For Users

Learn how to install and use Puerto's 8-department digital agency:

- **[Getting Started](getting-started.md)** - Install Puerto and your first department in 5 minutes
- **[User Guide Overview](user-guide/index.md)** - Task-based navigation for everyday workflows
- **[Installation Guide](installation.md)** - Installing departments and marketplace setup
  - [Browsing Departments](user-guide/browsing-plugins.md)
  - [Installing Departments](user-guide/installing-plugins.md)
  - [Configuring Plugins](user-guide/configuring-plugins.md)
  - [Configuring CLAUDE.md](configuring-claude-md.md) - Optimize Claude Code for your project ⭐
  - [Using Commands](user-guide/using-commands.md)
  - [Using Agents](user-guide/using-agents.md)
  - [Using Skills](user-guide/using-skills.md)
  - [Troubleshooting](user-guide/troubleshooting.md)
  - [FAQ](user-guide/faq.md)

---

## Puerto's Agency Structure

**8 Departments, 27 Specialized Roles**

- **[Team Structure](../TEAM-STRUCTURE.md)** - Complete org chart and department breakdown
- **[Role Matrix](../ROLE-MATRIX.md)** - RACI matrix for cross-functional collaboration
- **[Usage Examples](../EXAMPLES.md)** - 6 end-to-end project workflows
- **[Testing Guide](../TESTING.md)** - Manual and automated testing framework

### The Departments

- **🔧 Engineering** (7 roles) - Full-stack development, DevOps, QA
- **🎨 Design** (4 roles) - UX research, writing, accessibility
- **📢 Marketing** (5 roles) - Content, SEO, social, growth
- **📊 Product** (4 roles) - Product management, project delivery, analytics
- **💼 Sales** (3 roles) - Sales, customer success, partnerships
- **⚙️ Operations** (3 roles) - HR, procurement, office management
- **🎯 Leadership** (1 role) - Strategic planning and executive reporting
- **🏗️ Infrastructure** (7 plugins) - Essential tools and MCP servers

---

## For Plugin Developers

Everything you need to create custom plugins for Puerto:

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

Puerto is a curated marketplace organized as a digital agency team for Claude Code. Instead of scattered individual plugins, Puerto provides **8 functional departments with 27 specialized roles** that work together like a real 20-30 person agency.

**Key Features:**
- 8 department-level plugins covering all business functions
- 27 specialized roles from engineering to marketing to operations
- 23,307 lines of comprehensive skills (avg 860 lines per role)
- Real agency structure with clear reporting lines and collaboration patterns
- Production-ready with 193 validation checks passing
- Simple installation (global or per-project)
- Active community contributions

**Statistics:**
- **Departments:** 8
- **Specialized Roles:** 27
- **Total Skills:** 23,307 lines
- **Validation Checks:** 193 passing
- **Structure:** Based on 20-30 person digital agency best practices

---

## License

Puerto is licensed under the [MIT License](../LICENSE).
