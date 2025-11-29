# Essentials

MCP servers and requirements workflow for Claude Code.

## Install

```bash
/plugin install essentials@puerto
```

## MCP Servers

### Serena
Semantic code navigation via LSP.

```
"Find all references to UserAuth class"
"Navigate to processPayment definition"
```

**Requires:** [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Context7
Up-to-date library documentation.

```
"Get latest Next.js 15 app router examples"
"Show React 19 hook documentation"
```

### Sequential Thinking
Structured problem-solving.

```
"Think through this architecture step by step"
"Analyze this bug systematically"
```

## Commands

### `/brainstorm <name>`
Gather requirements through interactive Q&A. Read-only analysis.

```bash
/brainstorm user-authentication
```

Creates `.requirements/YYYY-MM-DD-HHMM-<name>/` with:
- Discovery Q&A
- Codebase analysis
- Implementation spec

### `/implement <name>`
Build from requirements document.

```bash
/implement user-authentication
```

### `/continue`
Resume interrupted implementation.

```bash
/continue                    # Most recent
/continue user-authentication  # Specific
```

## Prerequisites

| Dependency | Required For |
|------------|--------------|
| [uv](https://docs.astral.sh/uv/getting-started/installation/) | Serena |
| Node.js >= 18 | Context7, Sequential Thinking |

## License

MIT
