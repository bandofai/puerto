# Essentials Plugin

Essential MCP servers and requirements management commands for enhanced Claude Code development workflow.

## Installation

```bash
/plugin install essentials@puerto
```

## What's Included

### MCP Servers

Four powerful MCP servers for enhanced development:

### 1. Serena - Semantic Code Navigation

Provides IDE-like semantic code analysis and navigation using Language Server Protocol (LSP).

**Key Features:**
- Symbol-level code understanding (`find_symbol`, `find_referencing_symbols`)
- Precise code editing with `insert_after_symbol`
- Multi-language support: Python, TypeScript/JavaScript, PHP, Go, Rust, C/C++, Java, Ruby, and 15+ others
- Eliminates the need to read entire files or perform error-prone string replacements

**What it enables:**
- "Find all references to the `UserAuth` class"
- "Insert this code after the `validateUser` function"
- "Navigate to the definition of `processPayment`"

### 2. Context7 - Current Documentation

Fetches up-to-date, version-specific code documentation and examples directly from source repositories.

**Key Features:**
- Current API documentation (eliminates outdated training data)
- Real code examples from actual repositories
- Works without API key (basic rate limits apply)
- Optional API key for higher limits and private repositories

**What it enables:**
- "Show me the latest Next.js 15 app router examples"
- "Get current React 19 hook documentation"
- "Find up-to-date FastAPI security patterns"

### 3. Sequential Thinking - Structured Reasoning

Enables step-by-step problem decomposition and dynamic reasoning.

**Key Features:**
- Break down complex problems into manageable steps
- Revise and refine thinking as understanding deepens
- Explore alternative reasoning paths
- Adjust analysis scope dynamically

**What it enables:**
- "Think through this architecture decision step by step"
- "Analyze this bug systematically"
- "Plan the implementation with careful reasoning"

### 4. Playwright - Browser Automation

Provides headless browser automation with visual screenshot analysis and PDF generation capabilities.

**Key Features:**
- Headless browser automation (Chromium, Firefox, WebKit)
- True visual screenshot analysis with computer vision
- PDF generation from web pages
- Full browser interaction (click, type, navigate, fill forms)
- Network monitoring and request inspection
- JavaScript evaluation in browser context

**What it enables:**
- "Take a screenshot of this website and analyze its layout"
- "Navigate to example.com and click the login button"
- "Generate a PDF of this documentation page"
- "Fill out this form and submit it"
- "Monitor network requests on this page"

## Prerequisites

### Required Dependencies

**For Serena:**
- `uv` package manager ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))
- Python 3.8+
- Language servers auto-install for most languages
- Some languages require manual setup:
  - Go: `go install golang.org/x/tools/gopls@latest`
  - Rust: `rustup component add rust-analyzer`

**For Context7:**
- Node.js >= v18.0.0
- No API key required (optional for higher limits)

**For Sequential Thinking:**
- Node.js >= v18.0.0

**For Playwright:**
- Node.js >= v18.0.0
- Browser binaries auto-install on first use
- Requires ~200MB disk space for Chromium

### Quick Setup

1. Install uv:
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or via pip
pip install uv
```

2. Ensure Node.js is installed:
```bash
node --version  # Should be >= v18.0.0
```

## Usage

Once installed, all four MCP servers are automatically available in Claude Code.

### Serena Examples

```
"Find all references to the authenticate function"
"Show me the definition of UserController"
"Insert this logging code after the handleRequest method"
```

### Context7 Examples

```
"Get the latest documentation for Prisma 5.x migrations"
"Show me current examples of using shadcn/ui components"
"Find up-to-date examples of Next.js Server Actions"
```

### Sequential Thinking Examples

```
"Think through this refactoring step by step"
"Analyze why this test is failing using systematic reasoning"
"Plan the database migration carefully with all considerations"
```

### Playwright Examples

```
"Open https://example.com and take a screenshot"
"Navigate to the login page and fill in the form"
"Generate a PDF of the current documentation"
"Click the submit button and monitor network requests"
"Evaluate JavaScript in the browser console"
```

### Requirements Management Commands

Seven slash commands for interactive requirements management:

**Core Workflow (no prefix):**
- `/brainstorm <name>` - Create requirement through interactive Q&A
- `/implement <name>` - Implement a requirement systematically with tests
- `/continue [name]` - Resume interrupted implementation

**Management (`/req-` prefix):**
- `/req-list` - Show all requirements with status table
- `/req-update <name>` - Modify existing requirement
- `/req-tests <name>` - Generate comprehensive test scenarios
- `/req-status [name]` - Check implementation progress vs requirements

**Storage:** Creates `.requirements/` directory with individual files for each feature, allowing you to manage multiple requirements simultaneously.

#### Requirements Workflow Example

```bash
# 1. Start brainstorming a feature
/brainstorm user-authentication

# 2. Implement it
/implement user-authentication

# 3. If interrupted, resume later
/continue

# 4. Generate tests
/req-tests user-authentication

# 5. Check progress
/req-status user-authentication

# 6. List all requirements
/req-list
```

## Configuration

### Basic Configuration (Default)

The plugin works out of the box with sensible defaults. No additional configuration needed.

### Optional: Context7 API Key

For higher rate limits and private repository access:

1. Get an API key from [Context7](https://context7.com)
2. Set environment variable:
```bash
export CONTEXT7_API_KEY=your_api_key_here
```

3. Restart Claude Code

### Optional: Serena Custom Configuration

Create `~/.serena/serena_config.yml` for global settings:

```yaml
contexts:
  ide-assistant:
    enabled_tools:
      - find_symbol
      - find_referencing_symbols
      - insert_after_symbol
      - read_file_range
```

Project-specific settings are auto-generated in `.serena/project.yml`.

## Troubleshooting

### Serena Not Working

**Issue**: "uv: command not found"
- Install uv following the prerequisites above
- Restart your terminal/Claude Code

**Issue**: Language server not working for specific language
- Check if language server is installed
- See [Serena documentation](https://github.com/oraios/serena) for language-specific setup

### Context7 Rate Limits

**Issue**: "Rate limit exceeded"
- Add a Context7 API key (see Configuration section)
- Or wait a few minutes for the rate limit to reset

### Sequential Thinking Not Available

**Issue**: Tool not showing up
- Verify Node.js >= v18.0.0: `node --version`
- Reinstall the plugin: `/plugin uninstall essentials && /plugin install essentials@puerto`

### Playwright Browser Issues

**Issue**: "Executable doesn't exist" or browser not found
- Browsers auto-install on first use
- Run manually: `npx @playwright/mcp@latest --help` to trigger installation
- Ensure ~200MB disk space available

**Issue**: Permission denied errors
- Check file system permissions
- May need to run with elevated privileges on some systems

## What This Plugin Does Behind the Scenes

When you install this plugin, it:
1. Configures four MCP servers in your Claude Code environment
2. Makes their tools automatically available to Claude
3. Enables semantic code navigation, current documentation, structured reasoning, and browser automation

The MCP servers run on-demand when Claude needs them - no background processes.

## Performance Notes

- **Serena**: First run may take a moment while language servers initialize
- **Context7**: Fetches documentation on-demand (network required)
- **Sequential Thinking**: Lightweight, no performance impact
- **Playwright**: First run downloads browser binaries (~200MB), subsequent runs are fast

## Links

- [Serena Repository](https://github.com/oraios/serena)
- [Context7 Repository](https://github.com/upstash/context7)
- [Sequential Thinking Repository](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)
- [Playwright MCP Repository](https://github.com/microsoft/playwright/tree/main/utils/mcp)

## License

MIT License

Individual MCP servers retain their original licenses:
- Serena: MIT
- Context7: MIT
- Sequential Thinking: MIT
- Playwright: Apache 2.0
