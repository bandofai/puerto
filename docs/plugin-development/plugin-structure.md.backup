# Plugin Structure
> Part of the [Plugin Development Guide](index.md).

Understanding the file organization of Puerto plugins.

## Standard Structure

```
my-plugin/
├── .claude-plugin/           # Required: Plugin metadata
│   └── plugin.json          # Plugin manifest
├── README.md                 # Recommended: Documentation
├── LICENSE                   # Recommended: License file
├── commands/                 # Optional: Slash commands
│   ├── command-one.md
│   └── command-two.md
├── agents/                   # Optional: Specialized agents
│   ├── agent-one.md
│   └── agent-two.md
├── skills/                   # Optional: Knowledge libraries
│   └── skill-name/
│       └── SKILL.md
├── templates/                # Optional: File templates
│   ├── template-one.md
│   └── template-two.ts
└── .mcp.json                 # Optional: MCP server config
```

## Required Components

### .claude-plugin/plugin.json

**Required for all plugins.**

Minimal example:
\`\`\`json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Brief description"
}
\`\`\`

See [Plugin Manifest](plugin-manifest.md) for complete reference.

## Recommended Components

### README.md

**Highly recommended.**

Should include:
- Plugin description
- Installation instructions
- Usage examples
- Feature list
- License

## Optional Components

### commands/

Slash commands users can invoke.

- Each command is a `.md` file
- Filename becomes command name
- Contains prompt instructions

Example: `commands/hello.md` → `/hello` command

### agents/

Specialized subagents.

- Each agent is a `.md` file with YAML frontmatter
- Frontmatter defines name, model, tools
- Body contains system prompt

See [Building Agents](agents.md).

### skills/

Knowledge libraries for agents.

- Each skill is a subdirectory
- Contains `SKILL.md` with documentation
- Agents reference skills automatically

See [Developing Skills](skills.md).

### templates/

File templates.

- Any file type
- Used for code generation
- Organized by purpose

See [Using Templates](templates.md).

### .mcp.json

MCP server configuration.

- Defines external tool integration
- Requires additional setup

See [MCP Servers](mcp-servers.md).

## Directory Naming

✅ **Use:** Lowercase with hyphens
✅ **Examples:** `my-plugin`, `api-developer`, `data-scientist`
❌ **Avoid:** Uppercase, spaces, underscores

## File Naming

### Commands
- `command-name.md` → `/command-name`
- Use lowercase with hyphens

### Agents
- `agent-name.md`
- Matches name in frontmatter

### Skills
- `skill-name/SKILL.md`
- Directory name identifies skill

### Templates
- Any valid filename
- Keep descriptive
- Include file extension

## Examples

See [Examples Directory](../examples/) for complete plugin examples.

## Next Steps

- [Plugin Manifest](plugin-manifest.md) - Configure plugin.json
- [Creating Commands](commands.md) - Build commands
- [Building Agents](agents.md) - Create agents
- [Quickstart](quickstart.md) - Build first plugin
