# Integrating MCP Servers
> Part of the [Plugin Development Guide](index.md).

Marketplace Control Plane (MCP) servers let your plugin connect Claude Code to external tools—CLI utilities, hosted services, or custom processes. Puerto ships several MCP-powered plugins (Essentials, Chrome DevTools, Figma), and you can build your own using the same pattern.

---

## File Structure

Place an `.mcp.json` file in the plugin root:

```
plugins/<your-plugin>/
├── .mcp.json          ← MCP server definitions
├── .claude-plugin/
│   └── plugin.json
├── README.md
└── ...
```

The file maps MCP server names to configuration objects.

```json
{
  "serena": {
    "command": "uvx",
    "args": [
      "--from",
      "git+https://github.com/oraios/serena",
      "serena",
      "start-mcp-server",
      "--project",
      "{{CWD}}"
    ],
    "description": "Semantic code retrieval with LSP-powered symbol navigation"
  }
}
```

Puerto automatically detects this file and surfaces the servers during installation.

---

## Configuration Options

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `command` | string | ✅ | Executable to launch (e.g., `uvx`, `npx`, `node`). |
| `args` | string[] | ✅ (for command-based servers) | Arguments passed to the command. Supports placeholders like `{{CWD}}` (current project directory). |
| `description` | string | ✅ | Appears in Claude when browsing available MCP servers. |
| `transport` | string | ▫️ | Use `"http"` for remote MCP servers (no command/args). |
| `url` | string | ✅ when `transport: "http"` | Endpoint for HTTP-based MCP servers. |
| `env` | object | ▫️ | Environment variables to set before launching the command. |

Two common patterns:

1. **Command-based servers** — Download and run a Node/UV package when invoked (Essentials, Chrome DevTools).
2. **Hosted servers** — Connect to a hosted MCP endpoint over HTTP (Figma).

---

## Examples

### 1. CLI-Launched Servers (`command` + `args`)

```json
{
  "chrome-devtools": {
    "command": "npx",
    "args": ["-y", "chrome-devtools-mcp@latest"],
    "description": "Control Chrome browser with DevTools automation and debugging"
  },
  "context7": {
    "command": "npx",
    "args": ["-y", "@upstash/context7-mcp"],
    "description": "Live documentation lookup for popular libraries"
  }
}
```

- Use package managers (`npx`, `uvx`, `bunx`) for zero-install distribution.
- Pin versions if you need deterministic behaviour (e.g., `chrome-devtools-mcp@1.4.0`).
- Include prerequisites in the plugin README (Chrome version, Node version, API keys).

### 2. Hosted HTTP Servers

```json
{
  "figma": {
    "transport": "http",
    "url": "https://mcp.figma.com/mcp",
    "description": "Generate code from Figma designs and extract component data"
  }
}
```

- Claude will open a persistent HTTP connection.
- Use this pattern when you run the MCP server yourself or via partner APIs.
- Document authentication (tokens, OAuth) in README so users can configure credentials.

---

## Packaging Guidelines

- **Keep runtime light** — Rely on cloud-hosted binaries or package managers for installation-time fetching.
- **Security first** — Explain what the server does, what data it accesses, and any external services involved.
- **Graceful failures** — The command should exit with informative errors if prerequisites are missing.
- **Version discipline** — Bump versions when underlying MCP behaviour changes.
- **Testing** — Confirm the server launches from a clean environment (fresh machine or container).

---

## README Checklist

Document MCP usage clearly:

- Installation prerequisites (Node version, Chrome, CLI tools).
- Required environment variables or API keys.
- Example commands to start/stop the server (if applicable).
- Troubleshooting tips (common errors, logs to inspect).
- Safety considerations (data sent outside Claude, third-party services).

---

## Validation & QA

1. Install the plugin.
2. Trust the folder or add to global configuration.
3. Trigger the MCP server from Claude Code (`/connect`, `Invoke Tools`, or automatic invocation).
4. Observe logs (Claude will show stdout/stderr) to ensure the server starts.
5. Run representative commands to validate responses.
6. Document remediation steps for expected failures (missing dependencies, auth errors).

---

## Next Steps

- Describe the plugin metadata in [Plugin Manifest](plugin-manifest.md).
- Write companion automation in [Commands](commands.md) or [Agents](agents.md).
- Ensure tasks are covered in [Testing & Validation](testing-and-validation.md).
