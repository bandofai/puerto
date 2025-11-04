# Figma Plugin

Generate code from Figma designs, extract components, variables, and maintain design-code consistency.

## Installation

```bash
/plugin install figma@puerto
```

After installing, restart Claude Code to activate the MCP server.

## Authentication

After installation, you need to authenticate with Figma:

1. Type `/mcp` in Claude Code
2. Select **figma** from the server list
3. Choose **Authenticate**
4. Grant access when prompted
5. Verify connection with `/mcp` again

## What It Does

This plugin enables Claude to work directly with your Figma designs:

- **Generate Code from Designs** - Extract selected Figma frames and convert them to code
- **Component Extraction** - Retrieve design variables, components, and layout data
- **Design Context** - Provide complete design context to Claude for accurate code generation
- **Code Connect Integration** - Maintain consistency with existing component libraries

## MCP Server

**Figma MCP** - Remote HTTP server that connects to Figma's API for design data extraction.

## Prerequisites

- Dev or Full seat on Professional, Organization, or Enterprise Figma plan
- Link-based access to Figma frames or layers
- OAuth authentication (handled during setup)

## Example Usage

After authentication, you can ask Claude:

```
"Generate React code from this Figma frame: [frame-url]"
"Extract the design tokens from my Figma file"
"Create components based on this Figma design"
"What colors and typography are used in this design?"
```

## Configuration

The plugin uses Figma's remote HTTP server at `https://mcp.figma.com/mcp`. No additional configuration needed beyond authentication.

## License

MIT License
