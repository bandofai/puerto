<div align="center">
  <img src="docs/images/logo.png" alt="Puerto Logo" width="200"/>
</div>

<p align="center">
  Plugin marketplace for Claude Code
</p>

<p align="center">
  <a href="https://bandofai.com/projects/puerto/">Project Page</a>
</p>

---

## Install

```bash
/plugin marketplace add bandofai/puerto
```

## Plugins

### Essentials

MCP servers + requirements workflow for Claude Code.

```bash
/plugin install essentials@puerto
```

**MCP Servers:**
| Server | Purpose |
|--------|---------|
| **Serena** | Semantic code navigation via LSP |
| **Context7** | Up-to-date library documentation |
| **Sequential Thinking** | Structured problem-solving |

**Commands:**
| Command | Purpose |
|---------|---------|
| `/brainstorm <name>` | Gather requirements via Q&A |
| `/implement <name>` | Build from requirements |
| `/continue` | Resume interrupted work |

### Claude.md

Create effective CLAUDE.md files for Claude Code projects.

```bash
/plugin install claude-md@puerto
```

| Feature | Description |
|---------|-------------|
| **Creation** | Analyze codebases, generate optimized instructions |
| **Auditing** | Fix anti-patterns and token waste |
| **Monorepo** | Hierarchical CLAUDE.md strategy |

## Create Your Own Plugin

See [.claude/skills/plugin-management/SKILL.md](.claude/skills/plugin-management/SKILL.md)

## License

MIT
