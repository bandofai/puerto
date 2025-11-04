# Plugin Development Quickstart
> Part of the [Plugin Development Guide](index.md).

Create your first Puerto plugin in 10 minutes\!

## What We'll Build

A simple plugin called `hello-world` that provides a slash command `/hello` to greet users.

## Two Approaches

There are two ways to create a Puerto plugin:

1. **🚀 Recommended: Use `/plugin-manager`** - Fast, guided, and error-free (< 2 minutes)
2. **Manual Creation** - Full control, educational (10 minutes)

---

## Approach 1: Using `/plugin-manager` (Recommended)

The fastest way to create a plugin is using the `/plugin-manager` command:

### Step 1: Create Your Plugin

```bash
/plugin-manager create
```

This launches an interactive wizard that will:
- Guide you through naming your plugin
- Set up the correct directory structure
- Generate all required files (plugin.json, README.md)
- Create your first command/agent/skill based on your choice

### Step 2: Follow the Prompts

The plugin-manager will ask:
1. **Plugin name** (e.g., "hello-world")
2. **Description** (e.g., "A simple greeting plugin")
3. **What to include** (commands, agents, skills, or templates)
4. **Author information**

### Step 3: Review Generated Files

The plugin-manager creates:
```
hello-world/
├── .claude-plugin/
│   └── plugin.json       ✅ Auto-generated manifest
├── README.md             ✅ Pre-filled documentation
├── commands/             ✅ If you chose commands
│   └── hello.md
└── agents/               ✅ If you chose agents
    └── greeter.md
```

### Step 4: Customize and Test

Edit the generated files to match your needs, then test:

```bash
/hello
```

**That's it\!** You now have a working plugin.

Jump to [Next Steps](#next-steps) to learn how to enhance it.

---

## Approach 2: Manual Creation

Want to understand every detail? Create the plugin manually:

### Step 1: Create Directory Structure

```bash
mkdir -p hello-world/.claude-plugin
cd hello-world
```

## Step 2: Create Plugin Manifest

Create `.claude-plugin/plugin.json`:

```json
{
  "name": "hello-world",
  "version": "1.0.0",
  "description": "A simple hello world plugin demonstrating basic functionality",
  "author": {
    "name": "Your Name",
    "email": "you@example.com"
  },
  "keywords": ["example", "tutorial", "hello-world"],
  "license": "MIT"
}
```

## Step 3: Create Commands Directory

```bash
mkdir commands
```

## Step 4: Create Your First Command

Create `commands/hello.md`:

```markdown
When the user invokes /hello, greet them warmly and introduce yourself as a helpful Claude Code assistant.

If they provide a name (e.g., /hello Alice), personalize the greeting.

Example responses:
- "/hello" → "Hello\! I'm Claude, your AI coding assistant. How can I help you today?"
- "/hello Alice" → "Hello Alice\! I'm Claude, your AI coding assistant. How can I help you today?"

Be friendly and helpful\!
```

## Step 5: Create README

Create `README.md`:

```markdown
# Hello World Plugin

A simple example plugin demonstrating basic Puerto plugin structure.

## Installation

\`\`\`bash
/plugin install hello-world@puerto
\`\`\`

## Usage

\`\`\`bash
/hello          # Generic greeting
/hello YourName # Personalized greeting
\`\`\`

## Features

- Simple slash command
- Personalized greetings
- Example of plugin structure

## License

MIT
```

## Step 6: Validate Your Plugin

If you have Node.js installed:

```bash
# From Puerto root directory
node scripts/validate-plugin.js path/to/hello-world/
```

Expected output:
```
✅ Plugin validation passed\!
```

## Step 7: Test Locally

Copy your plugin to Puerto's plugins directory:

```bash
cp -r hello-world /path/to/puerto/plugins/
```

## Step 8: Try It Out

In Claude Code:

```bash
/hello
/hello World
```

## Your Plugin Structure

```
hello-world/
├── .claude-plugin/
│   └── plugin.json       ✅ Required manifest
├── README.md             ✅ Documentation
└── commands/
    └── hello.md          ✅ Your command
```

## What You Built

✅ **Valid plugin structure** - Follows Puerto conventions
✅ **Plugin manifest** - Proper metadata
✅ **Working command** - Functional `/hello` command
✅ **Documentation** - README for users

## Next Steps

### Add More Features

**Add Another Command:**

Create `commands/goodbye.md`:

```markdown
When the user invokes /goodbye, wish them well and offer to help again soon.

Be warm and friendly\!
```

**Add an Agent:**

Create `agents/greeter.md`:

```markdown
---
name: greeter
description: A friendly greeting agent
tools: Read, Write
model: haiku
---

You are a friendly greeting specialist. When invoked, create warm, personalized greetings based on context.
```

**Add a Skill:**

Create `skills/greeting-patterns/SKILL.md` with greeting best practices.

### Learn More

- **[Plugin Structure](plugin-structure.md)** - Understand organization
- **[Plugin Manifest](plugin-manifest.md)** - Complete manifest reference
- **[Creating Commands](commands.md)** - Advanced command patterns
- **[Building Agents](agents.md)** - Agent development
- **[Examples](../examples/)** - More plugin examples

### Publish Your Plugin

Ready to share?

1. **Fork Puerto** - Create your fork
2. **Add plugin** - Copy to `plugins/` directory
3. **Create PR** - Submit for review
4. **Get feedback** - Address reviewer comments

See [Publishing Guide](publishing.md) for details.

## Common Issues

### Validation Fails

**"Missing .claude-plugin directory"**
→ Ensure `.claude-plugin/` exists (with dot prefix)

**"Missing plugin.json"**
→ Create `.claude-plugin/plugin.json`

**"Invalid plugin.json"**
→ Validate JSON syntax (check commas, quotes)

### Command Not Found

→ Restart Claude Code
→ Verify plugin installed: `/plugin list`
→ Check command file is `.md` not `.txt`

## Congratulations\!

You've created your first Puerto plugin\! 

**What to build next:**
- Add more commands
- Create specialized agents
- Build skill libraries
- Integrate external tools

Happy building\!
