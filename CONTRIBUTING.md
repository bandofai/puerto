# Contributing to Puerto

Thank you for your interest in contributing to Puerto\! This guide will help you get started.

## Quick Links

- **[Full Contributing Guide](docs/contributing/index.md)** - Complete documentation
- **[Submitting Plugins](docs/contributing/submitting-plugins.md)** - Plugin submission process
- **[Plugin Development](docs/plugin-development/quickstart.md)** - Create plugins
- **[Code of Conduct](docs/contributing/community-guidelines.md)** - Community guidelines

## Ways to Contribute

### 1. Submit a New Plugin

Create and submit your own plugin:

1. **Develop** - Follow [Plugin Development Guide](docs/plugin-development/quickstart.md)
2. **Test** - Validate with `node scripts/validate-plugin.js`
3. **Document** - Include comprehensive README
4. **Submit** - Create PR with your plugin

See [Plugin Submission Guide](docs/contributing/submitting-plugins.md) for details.

### 2. Improve Existing Plugins

Enhance current plugins:

- Fix bugs
- Add features
- Improve documentation
- Update dependencies

### 3. Improve Documentation

Help others learn:

- Fix typos and errors
- Add examples
- Clarify explanations
- Translate documentation

### 4. Report Bugs

Found an issue?

1. **Search** existing issues
2. **Create** new issue with details:
   - Plugin name/version
   - Claude Code version
   - Steps to reproduce
   - Expected vs actual behavior

[Report Bug](https://github.com/bandofai/puerto/issues/new)

### 5. Request Features

Have an idea?

1. **Search** existing requests
2. **Create** feature request with:
   - Use case description
   - Proposed solution
   - Alternatives considered

[Request Feature](https://github.com/bandofai/puerto/issues/new)

## Plugin Submission Checklist

Before submitting a plugin:

- [ ] Plugin structure follows conventions
- [ ] `.claude-plugin/plugin.json` is valid
- [ ] Plugin passes validation: `node scripts/validate-plugin.js`
- [ ] README.md includes:
  - [ ] Installation instructions
  - [ ] Usage examples
  - [ ] Feature list
  - [ ] License information
- [ ] Code follows [style guidelines](docs/contributing/code-style.md)
- [ ] Plugin is tested and working
- [ ] No duplicate functionality
- [ ] Commit messages are clear

## Pull Request Process

### 1. Fork & Clone

```bash
# Fork on GitHub, then:
git clone https://github.com/YOUR-USERNAME/puerto.git
cd puerto
```

### 2. Create Branch

```bash
git checkout -b feature/my-plugin-name
# or
git checkout -b fix/bug-description
```

### 3. Make Changes

Add your plugin to `plugins/` directory:

```
plugins/
└── my-plugin/
    ├── .claude-plugin/
    │   └── plugin.json
    ├── README.md
    └── [commands/agents/skills/templates/]
```

### 4. Validate

```bash
# Validate your plugin
node scripts/validate-plugin.js plugins/my-plugin/

# Validate all plugins
npm run validate-all
```

### 5. Commit

```bash
git add plugins/my-plugin/
git commit -m "feat: add my-plugin for [functionality]"
```

Use conventional commits:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `chore:` - Maintenance

### 6. Push & Create PR

```bash
git push origin feature/my-plugin-name
```

Then create Pull Request on GitHub with:
- Clear title
- Description of changes
- Link to related issues
- Testing performed

### 7. Review Process

- Maintainers review your PR
- Address feedback
- Make requested changes
- PR merged when approved

## Plugin Quality Standards

All plugins must meet:

✅ **Functional** - Works as documented
✅ **Documented** - Clear README with examples
✅ **Validated** - Passes validation script
✅ **Original** - Not duplicate of existing plugin
✅ **Licensed** - Includes license (MIT recommended)
✅ **Safe** - No malicious code
✅ **Tested** - Verified in Claude Code

## Code Style

### Naming Conventions

- **Plugins:** `lowercase-with-hyphens`
- **Files:** Use standard names (README.md, SKILL.md, etc.)
- **Commands:** `/lowercase-with-hyphens`
- **Agents:** `lowercase-with-hyphens`

### File Organization

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json
├── README.md
├── commands/           # Optional
├── agents/             # Optional
├── skills/             # Optional
└── templates/          # Optional
```

### plugin.json Format

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "Clear, concise description",
  "author": {
    "name": "Your Name"
  },
  "keywords": ["relevant", "keywords"],
  "license": "MIT"
}
```

## Documentation Standards

### README.md Must Include

1. **Title & Description**
2. **Installation**
   ```bash
   /plugin install plugin-name@puerto
   ```
3. **Usage Examples**
4. **Features List**
5. **License**

### Example README Structure

```markdown
# Plugin Name

Brief description.

## Installation

\`\`\`bash
/plugin install plugin-name@puerto
\`\`\`

## Usage

### Commands

- `/command-one` - Description
- `/command-two` - Description

### Agents

- `agent-name` - Description

## Features

- Feature 1
- Feature 2
- Feature 3

## License

MIT
```

## Getting Help

- **[Documentation](docs/README.md)** - Complete guides
- **[GitHub Discussions](https://github.com/bandofai/puerto/discussions)** - Ask questions
- **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Report problems

## Code of Conduct

Be respectful and inclusive. See [Community Guidelines](docs/contributing/community-guidelines.md).

## License

By contributing, you agree that your contributions will be licensed under Puerto's MIT License.

## Thank You\!

Your contributions make Puerto better for everyone. We appreciate your help\!

---

**Ready to contribute?**

- [Create Your First Plugin](docs/plugin-development/quickstart.md)
- [Submit a Plugin](docs/contributing/submitting-plugins.md)
- [Browse Examples](docs/examples/)
