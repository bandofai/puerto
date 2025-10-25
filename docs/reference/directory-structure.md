# Directory Structure Reference
> Part of the [Reference](index.md).

Complete file layout reference for Puerto plugins.

## Plugin Directory Structure

\`\`\`
plugin-name/
├── .claude-plugin/           # Required
│   └── plugin.json          # Plugin manifest [REQUIRED]
│
├── README.md                 # Documentation [HIGHLY RECOMMENDED]
├── LICENSE                   # License file [RECOMMENDED]
│
├── commands/                 # Slash commands [OPTIONAL]
│   ├── command-one.md
│   ├── command-two.md
│   └── ...
│
├── agents/                   # Subagents [OPTIONAL]
│   ├── agent-one.md
│   ├── agent-two.md
│   └── ...
│
├── skills/                   # Knowledge libraries [OPTIONAL]
│   ├── skill-one/
│   │   └── SKILL.md
│   ├── skill-two/
│   │   └── SKILL.md
│   └── ...
│
├── templates/                # File templates [OPTIONAL]
│   ├── template-one.md
│   ├── template-two.ts
│   └── ...
│
└── .mcp.json                 # MCP server config [OPTIONAL]
\`\`\`

## Required Files

### .claude-plugin/plugin.json
- Plugin manifest
- Contains metadata
- Must be valid JSON
- See [plugin.json Schema](plugin-json-schema.md)

## Recommended Files

### README.md
- Plugin documentation
- Usage instructions
- Examples

### LICENSE
- Software license
- MIT recommended
- SPDX identifier

## Optional Directories

### commands/
- Markdown files
- One file per command
- Filename = command name

### agents/
- Markdown files with YAML frontmatter
- One file per agent
- See [Agent Frontmatter](agent-frontmatter.md)

### skills/
- Subdirectories
- Each contains SKILL.md
- Referenced by agents

### templates/
- Any file type
- Used for generation
- Organized by purpose

## File Patterns

### Naming Conventions
- **Plugins:** lowercase-with-hyphens
- **Commands:** lowercase-with-hyphens.md
- **Agents:** lowercase-with-hyphens.md
- **Skills:** lowercase-with-hyphens/SKILL.md
- **Templates:** descriptive-name.ext

### File Extensions
- Commands: `.md` (Markdown)
- Agents: `.md` (Markdown with frontmatter)
- Skills: `.md` (Markdown)
- Templates: Any extension
- Config: `.json`

## Example Structures

### Minimal Plugin
\`\`\`
minimal-plugin/
├── .claude-plugin/
│   └── plugin.json
└── README.md
\`\`\`

### Command Plugin
\`\`\`
command-plugin/
├── .claude-plugin/
│   └── plugin.json
├── README.md
└── commands/
    ├── hello.md
    └── goodbye.md
\`\`\`

### Full-Featured Plugin
\`\`\`
full-plugin/
├── .claude-plugin/
│   └── plugin.json
├── README.md
├── LICENSE
├── commands/
│   └── analyze.md
├── agents/
│   ├── analyzer.md
│   └── reporter.md
├── skills/
│   └── analysis-patterns/
│       └── SKILL.md
└── templates/
    └── report-template.md
\`\`\`

## Validation

Use validation script to check structure:

\`\`\`bash
node scripts/validate-plugin.js path/to/plugin/
\`\`\`

## Next Steps

- [Plugin Structure](../plugin-development/plugin-structure.md) - Detailed explanation
- [plugin.json Schema](plugin-json-schema.md) - Manifest reference
- [Validation Rules](validation-rules.md) - All checks
