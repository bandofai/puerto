# Puerto Architecture Overview

Puerto is delivered as a Git repository that doubles as a Claude Code marketplace. This overview walks through each layer—from repository layout to runtime integration—so you know where data lives, how catalogs are generated, and what Claude does when users install or run plugins.

---

## Quick Navigation

| Topic | What you’ll learn |
|-------|-------------------|
| [Marketplace System](marketplace-system.md) | End-to-end flow from repo layout to Claude Code consumption. |
| [Catalog Generation](catalog-generation.md) | How `generate-catalog.js` produces `.claude-plugin/marketplace.json`. |
| [Plugin Loading](plugin-loading.md) | What happens when users install Puerto globally or locally. |
| [Plugin Types](plugin-types.md) | Commands, agents, skills, templates, and MCP servers in detail. |
| [CI/CD Automation](ci-cd.md) | GitHub Actions that keep the marketplace manifest updated. |

Keep this page handy as the architectural map—each deep dive above links back here.

## System Components

```
┌─────────────────────────────────────────────────────────┐
│                     Puerto Marketplace                   │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌──────────────┐    ┌──────────────┐   ┌─────────────┐│
│  │   GitHub     │    │  Validation  │   │   Catalog   ││
│  │  Repository  │───▶│   Scripts    │──▶│  Generation ││
│  └──────────────┘    └──────────────┘   └─────────────┘│
│         │                                        │       │
│         ▼                                        ▼       │
│  ┌──────────────┐                        ┌─────────────┐│
│  │   Plugins    │                        │marketplace  ││
│  │  Directory   │                        │   .json     ││
│  └──────────────┘                        └─────────────┘│
│         │                                        │       │
└─────────┼────────────────────────────────────────┼───────┘
          │                                        │
          ▼                                        ▼
    ┌──────────────────────────────────────────────────┐
    │              Claude Code Runtime                 │
    │  ┌────────────┐ ┌─────────────┐ ┌────────────┐ │
    │  │  Commands  │ │   Agents    │ │   Skills   │ │
    │  └────────────┘ └─────────────┘ └────────────┘ │
    │  ┌────────────┐ ┌─────────────┐                │
    │  │ Templates  │ │ MCP Servers │                │
    │  └────────────┘ └─────────────┘                │
    └──────────────────────────────────────────────────┘
```

## Architecture Layers

### 1. Storage Layer (GitHub)

**Location:** `https://github.com/bandofai/puerto`

**Structure:**
```
puerto/
├── plugins/              # Plugin directory
│   ├── essentials/
│   ├── frontend-developer/
│   └── [140+ more]
├── scripts/              # Automation scripts
│   ├── validate-plugin.js
│   └── generate-catalog.js
└── .claude-plugin/
    └── marketplace.json  # Generated catalog
```

**Characteristics:**
- Git-based version control
- Open source (MIT license)
- Community contributions via PRs
- Automated catalog generation

### 2. Catalog Layer

**File:** `.claude-plugin/marketplace.json`

**Purpose:** Index of all plugins with metadata

**Structure:**
```json
{
  "name": "puerto",
  "owner": {"name": "Band of AI"},
  "plugins": [
    {
      "name": "essentials",
      "source": "./plugins/essentials",
      "description": "...",
      "version": "1.0.0"
    }
  ]
}
```

**Generation:**
- Automated via GitHub Actions
- Triggers on plugin changes
- Scans all plugins
- Validates structure
- Updates catalog

### 3. Distribution Layer

**Mechanism:** Git clone/fetch

**Process:**
1. User registers marketplace: `/plugin marketplace add bandofai/puerto`
2. Claude Code clones/fetches repository
3. Reads marketplace.json
4. Lists available plugins

**Caching:**
- Local cache of marketplace
- Periodic updates
- On-demand refresh

### 4. Plugin Layer

**Types:**
- **Commands** - Markdown files in `commands/`
- **Agents** - Markdown files in `agents/` with frontmatter
- **Skills** - Documentation in `skills/`
- **Templates** - Files in `templates/`
- **MCP Servers** - `.mcp.json` configuration

**Loading:**
- On-demand by Claude Code
- Global installation available across all projects

### 5. Runtime Layer (Claude Code)

**Integration:**
- Commands registered in slash command system
- Agents available for invocation
- Skills mounted for agent reference
- Templates accessible for generation
- MCP servers start as background processes

## Data Flow

### Plugin Discovery

```
User: /plugin list puerto
  │
  ├─▶ Claude Code reads marketplace.json
  │
  ├─▶ Parses plugin list
  │
  └─▶ Displays plugins to user
```

### Plugin Installation

```
User: /plugin install essentials@puerto
  │
  ├─▶ Claude Code locates plugin in marketplace
  │
  ├─▶ Copies plugin to global plugins directory
  │
  ├─▶ Loads plugin configuration
  │
  └─▶ Registers commands/agents/etc
```

### Command Execution

```
User: /brainstorm feature-name
  │
  ├─▶ Claude Code looks up command
  │
  ├─▶ Loads command markdown
  │
  ├─▶ Executes prompt instructions
  │
  └─▶ Returns result to user
```

### Agent Invocation

```
Claude: [Invokes component-builder agent]
  │
  ├─▶ Loads agent markdown & frontmatter
  │
  ├─▶ Initializes with specified model & tools
  │
  ├─▶ Mounts referenced skills
  │
  ├─▶ Agent performs task autonomously
  │
  └─▶ Returns results
```

## Key Design Principles

### 1. Git-Native

✅ Version control built-in
✅ Easy forking and customization
✅ Familiar workflow for developers
✅ No custom infrastructure needed

### 2. Declarative Configuration

✅ JSON manifests (plugin.json, marketplace.json)
✅ Markdown for content (commands, agents, skills)
✅ Simple, readable formats
✅ No code required for basic plugins

### 3. Validation-First

✅ Automated validation scripts
✅ CI/CD enforcement
✅ Quality standards
✅ Catch errors early

### 4. Plugin Isolation

✅ Plugins don't interfere with each other
✅ Scoped tool access for agents
✅ Namespace separation
✅ Safe concurrent operation

### 5. Extensibility

✅ Multiple plugin types supported
✅ Easy to add new types
✅ Flexible structure
✅ Community-driven growth

## Component Details

### Scripts

**validate-plugin.js**
- Validates plugin structure
- Checks required files
- Verifies manifest format
- Used in CI/CD

**generate-catalog.js**
- Scans plugins directory
- Extracts metadata
- Generates marketplace.json
- Runs on every push

### GitHub Actions

**Workflow:** `.github/workflows/update-catalog.yml`

**Triggers:**
- Push to main branch
- Plugin files change
- Manual workflow dispatch

**Steps:**
1. Checkout repository
2. Run generate-catalog.js
3. Commit marketplace.json
4. Push changes

### Claude Code Integration

Puerto integrates with Claude Code's:
- **Marketplace system** - Plugin discovery
- **Plugin loader** - Plugin activation
- **Command registry** - Slash commands
- **Agent system** - Subagent invocation
- **Skill system** - Knowledge reference
- **MCP runtime** - External tool integration

## Scalability

### Current Scale

- 140+ plugins
- Multiple plugin types
- Active community
- Automated processes

### Design Capacity

- ✅ Thousands of plugins supported
- ✅ Fast catalog generation (<1s)
- ✅ Efficient Git operations
- ✅ Minimal infrastructure

### Performance Considerations

**Catalog Generation:**
- O(n) complexity where n = number of plugins
- Cached by Claude Code
- Infrequent updates

**Plugin Loading:**
- On-demand loading
- No upfront cost
- Scales with usage, not plugin count

## Security Model

### Plugin Validation

- Required fields checked
- File structure validated
- No arbitrary code execution (except MCP)

### Agent Permissions

- Explicit tool access defined
- Read-only by default
- Write requires declaration
- No Bash access for most agents

### MCP Server Isolation

- Separate processes
- Defined interfaces
- Sandboxed execution

## Next Steps

- **[Marketplace System](marketplace-system.md)** - Detailed marketplace mechanics
- **[Catalog Generation](catalog-generation.md)** - Catalog automation
- **[Plugin Loading](plugin-loading.md)** - Loading mechanism
- **[Plugin Types](plugin-types.md)** - Type specifications
- **[CI/CD](ci-cd.md)** - Automation workflow
