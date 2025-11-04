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

**For Puerto Prompt Analyzer Hook:**
- Node.js >= v18.0.0 (same as above)
- No additional dependencies required

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

### Puerto Prompt Analyzer Hook (Optional)

**Automatic prompt analyzer that helps you discover relevant plugins and improve instruction quality.**

The instruction analysis hook runs before Claude processes your prompts, providing:

- **Task Classification:** Automatically identifies if you're doing research, implementation, or mixed tasks
- **Plugin Recommendations:** Suggests top 2-3 relevant Puerto marketplace plugins based on your request
- **Instruction Validation:** Detects vague or unclear prompts and provides improvement suggestions
- **Transparent Analysis:** Shows recommendations directly in Claude's response with install commands

#### Manual Setup Required

**⚠️ Important:** Due to security restrictions, hooks cannot be automatically configured. You must manually add the hook to your Claude Code settings.

#### Quick Install (Recommended)

Use the automated install script:

**macOS/Linux:**
```bash
cd ~/.claude/plugins/marketplaces/puerto/plugins/essentials/hooks
./install-hook.sh
```

**Windows (PowerShell):**
```powershell
cd $env:USERPROFILE\.claude\plugins\marketplaces\puerto\plugins\essentials\hooks
.\install-hook.ps1
```

The script will:
- ✅ Find the hook location automatically
- ✅ Verify Node.js is installed
- ✅ Backup your settings.json
- ✅ Add the hook configuration
- ✅ Validate the JSON

#### Manual Installation

If you prefer manual setup:

**Setup Steps:**

1. **Install the essentials plugin** (if not already installed):
   ```bash
   /plugin install essentials@puerto
   ```

2. **Find your plugin installation path:**

   The path depends on how you installed the marketplace and your OS:

   **macOS/Linux:**
   ```bash
   # Find your essentials plugin location
   find ~/.claude/plugins -name "puerto-prompt-analyzer.js" 2>/dev/null
   ```

   **Windows (PowerShell):**
   ```powershell
   # Find your essentials plugin location
   Get-ChildItem -Path "$env:USERPROFILE\.claude\plugins" -Recurse -Filter "puerto-prompt-analyzer.js" | Select-Object -First 1 -ExpandProperty FullName
   ```

   **Windows (Command Prompt):**
   ```cmd
   dir /s /b "%USERPROFILE%\.claude\plugins\*puerto-prompt-analyzer.js"
   ```

   This will output something like:
   - **macOS:** `/Users/yourname/.claude/plugins/marketplaces/puerto/plugins/essentials/hooks/puerto-prompt-analyzer.js`
   - **Linux:** `/home/yourname/.claude/plugins/marketplaces/puerto/plugins/essentials/hooks/puerto-prompt-analyzer.js`
   - **Windows:** `C:\Users\yourname\.claude\plugins\marketplaces\puerto\plugins\essentials\hooks\puerto-prompt-analyzer.js`

   Copy this full path for the next step.

3. **Edit your Claude Code settings file:**

   **macOS/Linux:**
   ```bash
   # Open settings in your editor
   code ~/.claude/settings.json
   # or
   nano ~/.claude/settings.json
   ```

   **Windows:**
   ```powershell
   # Open settings in notepad
   notepad "$env:USERPROFILE\.claude\settings.json"
   # or in VS Code
   code "$env:USERPROFILE\.claude\settings.json"
   ```

4. **Add the hook configuration:**

   Add this to your `settings.json` (merge with existing content), replacing `YOUR_PATH_HERE` with the path you found in step 2:

   ```json
   {
     "hooks": {
       "UserPromptSubmit": [
         {
           "hooks": [
             {
               "type": "command",
               "command": "node YOUR_PATH_HERE",
               "timeout": 60
             }
           ]
         }
       ]
     }
   }
   ```

   **Example:**
   ```json
   "command": "node /Users/yourname/.claude/plugins/marketplaces/puerto/plugins/essentials/hooks/puerto-prompt-analyzer.js"
   ```

5. **Verify your JSON is valid:**

   **macOS/Linux:**
   ```bash
   # Check for JSON syntax errors
   cat ~/.claude/settings.json | python3 -m json.tool > /dev/null && echo "✅ Valid JSON" || echo "❌ Invalid JSON"
   ```

   **Windows (PowerShell):**
   ```powershell
   # Check for JSON syntax errors
   Get-Content "$env:USERPROFILE\.claude\settings.json" | ConvertFrom-Json | Out-Null
   if ($?) { Write-Host "✅ Valid JSON" } else { Write-Host "❌ Invalid JSON" }
   ```

6. **Restart Claude Code** - This is **required** for the hook to take effect

7. **Test the hook is working:**

   Submit any non-command prompt (e.g., "help me build a feature"). You should see an "🔍 Instruction Analysis" section in Claude's response with plugin recommendations.

   If you don't see it:
   - Check Claude Code logs for errors
   - Verify the path in your settings.json exists
   - Ensure Node.js is in your PATH: `which node`
   - See troubleshooting section below

#### How it works:

1. You submit any non-command prompt
2. Hook analyzes your request in < 1 second
3. Claude receives your prompt + intelligent recommendations
4. You see suggested plugins with install commands in the response

#### Example output:

```markdown
## 🔍 Instruction Analysis

**Task Type:** Implementation

**📦 Recommended Plugins:**

### 1. `fitness-tracking-logger`
**Description:** Comprehensive fitness tracking plugin
**Why:** Matches keywords: fitness, tracking
**Install:** `/plugin install fitness-tracking-logger`
```

#### Features:
- ✅ Fast (< 1 second analysis)
- ✅ Fail-safe (never blocks your workflow)
- ✅ No external dependencies
- ✅ Smart plugin scoring based on keywords and task type

#### Troubleshooting the Hook

**Hook not running:**
1. Verify the path exists: `ls [your-path]/puerto-prompt-analyzer.js`
2. Check Node.js is available: `node --version` (should be >= v18.0.0)
3. Test the hook manually:
   ```bash
   echo '{"prompt": "test", "hook_event_name": "UserPromptSubmit"}' | node [your-path]/puerto-prompt-analyzer.js
   ```
   Should output JSON with recommendations

**Node.js not found:**
- Find node path: `which node`
- Use full path in settings: `"command": "/usr/local/bin/node /path/to/script.js"`

**Invalid JSON error:**
- Validate JSON: `cat ~/.claude/settings.json | python3 -m json.tool`
- Common issues: missing commas, trailing commas, unescaped quotes

**Hook crashes or timeouts:**
- Check Claude Code logs for error messages
- Ensure marketplace.json exists: `ls ~/.claude/plugins/marketplaces/puerto/.claude-plugin/marketplace.json`
- Hook timeout is 60 seconds (should be more than enough)

**Still not working:**
- The hook is fail-safe and won't block your workflow
- Check for typos in the settings.json
- Ensure you restarted Claude Code after configuration
- See detailed [hooks/README.md](hooks/README.md) for more troubleshooting

#### Disabling the Hook

To disable the hook, simply remove the `UserPromptSubmit` section from your `~/.claude/settings.json` file and restart Claude Code.

For detailed documentation, see [hooks/README.md](hooks/README.md)

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
