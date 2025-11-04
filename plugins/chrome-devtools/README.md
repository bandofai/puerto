# Chrome DevTools Plugin

Control and inspect Chrome browsers with full DevTools automation, debugging, and performance analysis capabilities.

## Installation

```bash
/plugin install chrome-devtools@puerto
```

After installing, restart Claude Code to activate the MCP server.

## What It Does

This plugin enables Claude to control and inspect live Chrome browsers, providing access to the full power of Chrome DevTools for:

- **Browser Automation** - Click, type, drag, fill forms, navigate pages
- **Debugging** - Evaluate JavaScript, inspect elements, capture screenshots
- **Performance Analysis** - Measure page load times, analyze traces, profile performance
- **Network Monitoring** - Inspect requests, responses, and network activity
- **Emulation** - Test different viewports, device types, and conditions

## MCP Server

**Chrome DevTools MCP** - Provides 26+ tools for comprehensive browser control and inspection.

## Prerequisites

- Node.js >= v20.19
- Chrome browser (stable version or newer)

## Example Usage

After installation, you can ask Claude:

```
"Take a screenshot of https://example.com"
"Check the performance of my website"
"Click the login button and fill in the form"
"Evaluate this JavaScript code in the browser console"
"Analyze the network requests on this page"
```

The MCP server automatically launches Chrome when browser tools are needed.

## Configuration Options

The plugin works with default settings, but you can customize behavior:

- Headless mode (run without UI)
- Custom viewport sizes
- Specific Chrome channels (stable, canary, beta, dev)
- Isolated browsing sessions

## License

MIT License
