# Puerto Marketplace Discovery & Integration

**Version**: 1.0.0
**Last Updated**: 2025-11-01
**Purpose**: Comprehensive guide to discovering and integrating Puerto marketplace plugins

---

## Purpose of This Skill

This skill provides knowledge for autonomously discovering installed Puerto plugins and generating appropriate CLAUDE.md integration sections. Use this when the marketplace-integrator agent needs to scan plugins and create routing rules.

**Key Learning Objectives**:
- Understand Puerto marketplace structure (140+ plugins, 27 squads)
- Learn how to discover installed plugins via filesystem
- Extract agent descriptions from plugin manifests
- Generate routing rules from agent descriptions
- Create comprehensive "Installed Puerto Plugins" sections

---

## Puerto Marketplace Overview

### Structure

- **Total Plugins**: 140+
- **Organization**: 27 specialized squads
- **Installation Locations**:
  - Global: `~/.claude/plugins/`
  - Project-local: `.claude/plugins/`

### Plugin Structure

Every Puerto plugin follows this consistent structure:

```
~/.claude/plugins/[plugin-name]/
├── .claude-plugin/
│   └── plugin.json           # Plugin manifest
├── agents/
│   ├── agent1.md            # Agent markdown files
│   ├── agent2.md
│   └── agent3.md
├── skills/
│   └── skill-name/
│       └── SKILL.md         # Skill content
├── commands/                # Optional
│   └── command.md
└── README.md
```

---

## Plugin Discovery Process

### Step 1: Scan Installation Directories

Check both global and project-local plugin directories:

```bash
# Discover installed plugins
for plugin_dir in ~/.claude/plugins/* .claude/plugins/*; do
    if [ -d "$plugin_dir" ]; then
        plugin_json="$plugin_dir/.claude-plugin/plugin.json"
        if [ -f "$plugin_json" ]; then
            # Plugin found - extract info
            echo "Found plugin: $plugin_dir"
        fi
    fi
done
```

### Step 2: Read Plugin Manifest

Extract key information from `plugin.json`:

```bash
# Read plugin.json
plugin_name=$(jq -r '.name' "$plugin_json")
plugin_description=$(jq -r '.description' "$plugin_json")
agent_files=$(jq -r '.agents[]' "$plugin_json")
```

**Example plugin.json**:
```json
{
  "name": "engineering",
  "version": "1.0.0",
  "description": "Frontend development specialist for React/Vue/Svelte",
  "agents": [
    "./agents/frontend-engineer.md",
    "./agents/state-architect.md",
    "./agents/style-implementer.md"
  ],
  "skills": [
    "./skills/component-patterns.md"
  ],
  "author": {
    "name": "Puerto Plugin Collection"
  }
}
```

### Step 3: Extract Agent Information

Read agent frontmatter from markdown files:

```bash
# For each agent file, extract frontmatter
for agent_file in $agent_files; do
    full_path="$plugin_dir/$agent_file"

    # Extract name from frontmatter
    agent_name=$(grep '^name:' "$full_path" | sed 's/name: //')

    # Extract description (contains trigger conditions)
    agent_description=$(grep '^description:' "$full_path" | sed 's/description: //')

    echo "Agent: $agent_name"
    echo "Description: $agent_description"
done
```

**Example agent frontmatter**:
```markdown
---
name: frontend-engineer
description: PROACTIVELY use when implementing React/Vue/Svelte components. Skill-aware builder that produces production-ready components with TypeScript and tests.
tools: Read, Write, Edit, Bash, Grep, Glob
model: sonnet
---
```

### Step 4: Generate Routing Rules from Descriptions

Parse agent descriptions to extract trigger conditions:

**Pattern**: Descriptions often contain "PROACTIVELY use when [trigger condition]"

**Example**:
- Description: "PROACTIVELY use when implementing React/Vue/Svelte components"
- Generated rule: `WHEN implementing components → AUTOMATICALLY invoke: engineering/frontend-engineer`

---

## Puerto Plugin Categories (27 Squads)

### 1. Frontend Development Squad
- **engineering**: React/Vue/Svelte component development
- **ux-researcher**: User research and usability testing
- **ux-writer**: UX writing and microcopy
- **accessibility-specialist**: WCAG compliance and a11y

### 2. Backend Development Squad
- **engineering**: REST/GraphQL endpoint development
- **engineering**: API design, database schemas, system architecture

### 3. Database Squad
- **engineering**: Query optimization, migrations, schema design

### 4. DevOps Squad
- **engineering/devops-engineer**: CI/CD, deployment, infrastructure
- **site-reliability-engineer**: SRE practices, monitoring, incident response

### 5. Testing Squad
- **test-runner**: Test execution
- **code-reviewer**: Code quality review

### 6. Security Squad
- **security-auditor**: Security scanning and audits

### 7. Performance Squad
- **web-performance-auditor**: Lighthouse audits, performance optimization

### 8. Documentation Squad
- **technical-writer**: Documentation generation

### 9. Business Squad
- **business-analyst**: Business analysis and requirements
- **sales-proposal-writer**: Sales proposal creation

### 10. Data Squad
- **data-analyst**: Data analysis
- **ml-engineer**: Machine learning engineering

### 11-27. Additional Squads
(Add more as discovered during scanning)

---

## Generating "Installed Puerto Plugins" Section

### Format Template

```markdown
## Installed Puerto Plugins

### [plugin-name]
- [agent-name]: [Brief description of what it does]
- [agent-name]: [Brief description]
- [agent-name]: [Brief description]

### [plugin-name]
- [agent-name]: [Brief description]
```

### Example Generation

**Input** (discovered plugins):
- engineering (3 agents)
- engineering (3 agents)
- engineering (3 agents)

**Output** (CLAUDE.md section):
```markdown
## Installed Puerto Plugins

### engineering
- frontend-engineer: Create React/Vue/Svelte components with TypeScript
- state-architect: Implement state management (Redux, Zustand, Context)
- style-implementer: Responsive design and styling with CSS/Tailwind

### engineering
- backend-engineer: Create REST/GraphQL endpoints with validation
- auth-implementer: Implement JWT, OAuth 2.0, API key authentication
- api-tester: Create comprehensive API integration tests

### engineering
- query-optimizer: Analyze and optimize slow database queries
- migration-manager: Create zero-downtime database migrations
- schema-designer: Design normalized database schemas and ER diagrams
```

---

## Generating Routing Rules from Plugin Discovery

### Process

1. **Extract trigger conditions** from agent descriptions
2. **Map to WHEN/AUTOMATICALLY pattern**
3. **Group by category** (Frontend, Backend, Database, etc.)
4. **Add variations** for common phrasings

### Example: Frontend-Developer Plugin

**Discovered Agents**:
1. frontend-engineer: "PROACTIVELY use when creating React/Vue/Svelte components"
2. state-architect: "PROACTIVELY use when implementing state management"
3. style-implementer: "PROACTIVELY use for responsive design and styling"

**Generated Routing Rules**:
```markdown
## Automatic Task Routing

### Frontend Development

WHEN user says "create [component name] component"
→ AUTOMATICALLY invoke: engineering/frontend-engineer

WHEN user says "implement state management" OR "add [Redux/Zustand/Context]"
→ AUTOMATICALLY invoke: engineering:state-architect

WHEN user says "style [component]" OR "make [component] responsive"
→ AUTOMATICALLY invoke: engineering:style-implementer
```

### Example: API-Developer Plugin

**Discovered Agents**:
1. backend-engineer: "PROACTIVELY use when implementing REST or GraphQL endpoints"
2. auth-implementer: "PROACTIVELY use when implementing API authentication"
3. api-tester: "PROACTIVELY use when creating API integration tests"

**Generated Routing Rules**:
```markdown
### Backend Development

WHEN user says "create [endpoint name] endpoint" OR "add API route for [resource]"
→ AUTOMATICALLY invoke: engineering/backend-engineer

WHEN user says "implement authentication" OR "add login/signup"
→ AUTOMATICALLY invoke: engineering/backend-engineer

WHEN user says "write tests for [API]" OR "add API tests"
→ AUTOMATICALLY invoke: engineering:api-tester
```

---

## Common Plugin Patterns

### Pattern 1: Multi-Agent Specialist Plugins

Plugins with 3-5 agents covering different aspects of a domain:

**Examples**:
- **engineering**: frontend-engineer, state-architect, style-implementer, accessibility-validator
- **engineering**: backend-engineer, auth-implementer, api-tester, openapi-generator
- **engineering/devops-engineer**: cicd-builder, deployment-orchestrator, infrastructure-manager, monitoring-setup

**Integration Strategy**: Create subsections for each aspect:
```markdown
### [Plugin] Tasks

#### Component Creation
WHEN... → AUTOMATICALLY invoke: [plugin]:[agent1]

#### State Management
WHEN... → AUTOMATICALLY invoke: [plugin]:[agent2]

#### Styling
WHEN... → AUTOMATICALLY invoke: [plugin]:[agent3]
```

### Pattern 2: Single-Purpose Auditor Plugins

Plugins with 1-2 agents focused on specific analysis:

**Examples**:
- **accessibility-specialist**: accessibility-auditor, remediation-consultant
- **security-auditor**: security-scanner
- **web-performance-auditor**: lighthouse-auditor, performance-analyzer

**Integration Strategy**: Simple routing rules:
```markdown
### Quality Assurance

WHEN user says "audit accessibility"
→ AUTOMATICALLY invoke: accessibility-specialist:accessibility-auditor

WHEN user says "check security"
→ AUTOMATICALLY invoke: security-auditor:security-scanner
```

### Pattern 3: Workflow Plugins

Plugins with agents representing workflow stages:

**Examples**:
- **engineering**: api-designer (design) → engineering (schema) → system-architect (infrastructure)

**Integration Strategy**: Sequential routing:
```markdown
### Architecture & Design

WHEN designing new feature
→ First invoke: engineering:system-architect (architecture)
→ Then invoke: engineering:engineering (schema)
→ Then invoke: engineering:api-designer (API spec)
```

---

## Plugin Discovery Bash Script

Complete script for discovering and analyzing installed plugins:

```bash
#!/bin/bash

# PLUGIN DISCOVERY SCRIPT
# Scans ~/.claude/plugins/ and .claude/plugins/ for installed Puerto plugins

echo "=== Discovering Installed Puerto Plugins ==="
echo ""

# Array to store discovered plugins
declare -a discovered_plugins

# Scan global plugins
if [ -d ~/.claude/plugins ]; then
    echo "Scanning global plugins: ~/.claude/plugins/"
    for plugin_dir in ~/.claude/plugins/*; do
        if [ -d "$plugin_dir" ]; then
            plugin_json="$plugin_dir/.claude-plugin/plugin.json"
            if [ -f "$plugin_json" ]; then
                plugin_name=$(jq -r '.name' "$plugin_json")
                plugin_description=$(jq -r '.description' "$plugin_json")
                agent_count=$(jq '.agents | length' "$plugin_json")

                echo "  ✓ Found: $plugin_name ($agent_count agents)"
                discovered_plugins+=("$plugin_name|$plugin_dir|$agent_count")
            fi
        fi
    done
fi

# Scan project-local plugins
if [ -d .claude/plugins ]; then
    echo "Scanning project plugins: .claude/plugins/"
    for plugin_dir in .claude/plugins/*; do
        if [ -d "$plugin_dir" ]; then
            plugin_json="$plugin_dir/.claude-plugin/plugin.json"
            if [ -f "$plugin_json" ]; then
                plugin_name=$(jq -r '.name' "$plugin_json")
                plugin_description=$(jq -r '.description' "$plugin_json")
                agent_count=$(jq '.agents | length' "$plugin_json")

                echo "  ✓ Found: $plugin_name ($agent_count agents)"
                discovered_plugins+=("$plugin_name|$plugin_dir|$agent_count")
            fi
        fi
    done
fi

echo ""
echo "=== Total Plugins Found: ${#discovered_plugins[@]} ==="
echo ""

# Extract agent details for each plugin
for plugin_info in "${discovered_plugins[@]}"; do
    IFS='|' read -r plugin_name plugin_dir agent_count <<< "$plugin_info"

    echo "## $plugin_name ($agent_count agents)"

    plugin_json="$plugin_dir/.claude-plugin/plugin.json"
    agent_files=$(jq -r '.agents[]' "$plugin_json")

    for agent_file in $agent_files; do
        full_path="$plugin_dir/$agent_file"

        if [ -f "$full_path" ]; then
            # Extract agent name and description from frontmatter
            agent_name=$(grep '^name:' "$full_path" | head -1 | sed 's/name: //')
            agent_description=$(grep '^description:' "$full_path" | head -1 | sed 's/description: //')

            echo "  - $agent_name: $agent_description"
        fi
    done

    echo ""
done
```

---

## Integration Workflow

### Step-by-Step Process for marketplace-integrator Agent

1. **Run Discovery Script**
   - Execute bash script to scan plugin directories
   - Collect plugin names, descriptions, and agent details

2. **Read Existing CLAUDE.md** (if it exists)
   - Check if "Installed Puerto Plugins" section exists
   - Identify plugins already documented

3. **Generate New Content**
   - Create "Installed Puerto Plugins" section with discovered plugins
   - Generate routing rules based on agent descriptions
   - Group rules by logical categories

4. **Merge with Existing Content**
   - Preserve existing Project Type, Tech Stack, Patterns
   - Replace/update "Installed Puerto Plugins" section
   - Replace/update "Automatic Task Routing" section
   - Keep Domain Knowledge intact

5. **Output Enhanced CLAUDE.md**
   - Return complete updated file
   - Highlight what was added/changed

---

## Example: Complete Integration Output

**Before** (user's existing CLAUDE.md):
```markdown
# My React App

## Project Type
React SPA with Express backend

## Tech Stack
- Frontend: React 18, Tailwind
- Backend: Express, PostgreSQL
```

**After** (marketplace-integrator enhancement):
```markdown
# My React App

## Project Type
React SPA with Express backend

## Tech Stack
- Frontend: React 18, Tailwind CSS
- Backend: Express, PostgreSQL

## Installed Puerto Plugins

### engineering
- frontend-engineer: Create React components with TypeScript
- state-architect: Implement state management
- style-implementer: Responsive design with Tailwind

### engineering
- backend-engineer: Create REST endpoints
- auth-implementer: Implement authentication
- api-tester: Create API tests

### engineering
- engineering: Design database schemas

## Automatic Task Routing

### Frontend Development

WHEN user says "create [component name] component"
→ AUTOMATICALLY invoke: engineering/frontend-engineer

WHEN user says "implement state management"
→ AUTOMATICALLY invoke: engineering:state-architect

WHEN user says "style [component]"
→ AUTOMATICALLY invoke: engineering:style-implementer

### Backend Development

WHEN user says "create [endpoint] endpoint"
→ AUTOMATICALLY invoke: engineering/backend-engineer

WHEN user says "implement authentication"
→ AUTOMATICALLY invoke: engineering/backend-engineer

WHEN user says "write API tests"
→ AUTOMATICALLY invoke: engineering:api-tester

### Database Work

WHEN user says "design database schema"
→ AUTOMATICALLY invoke: engineering:engineering
```

---

## Handling Edge Cases

### Case 1: No Plugins Installed

**Detection**: Discovery script returns empty array

**Action**: Inform user and suggest installing plugins:
```markdown
## Installed Puerto Plugins

No Puerto plugins detected. Install plugins with:
`/plugin install [plugin-name]`

Popular plugins for this project type:
- engineering (for React development)
- engineering (for Express APIs)
- engineering (for PostgreSQL schemas)
```

### Case 2: Plugin Without Agents

**Detection**: `plugin.json` has empty agents array

**Action**: Skip plugin or note it in comments:
```markdown
<!-- Plugin 'example-plugin' found but has no agents -->
```

### Case 3: Malformed plugin.json

**Detection**: `jq` fails to parse

**Action**: Log error and skip plugin:
```bash
if ! jq empty "$plugin_json" 2>/dev/null; then
    echo "Warning: Malformed plugin.json in $plugin_dir (skipping)"
    continue
fi
```

### Case 4: Agent File Missing Frontmatter

**Detection**: `grep` returns empty for name/description

**Action**: Use fallback values:
```bash
if [ -z "$agent_name" ]; then
    # Extract from filename: "./agents/frontend-engineer.md" → "frontend-engineer"
    agent_name=$(basename "$agent_file" .md)
fi

if [ -z "$agent_description" ]; then
    agent_description="No description available"
fi
```

---

## Best Practices for Plugin Integration

1. **Always scan both global and project-local directories**
   - Users might have plugins in either location
   - Project-local plugins take precedence

2. **Preserve existing CLAUDE.md content**
   - Don't overwrite Project Patterns or Domain Knowledge
   - Only update "Installed Puerto Plugins" and "Automatic Task Routing"

3. **Generate routing rules from agent descriptions**
   - Parse "PROACTIVELY use when..." patterns
   - Add common trigger variations (create/add/implement)

4. **Group routing rules logically**
   - Frontend, Backend, Database, DevOps, Testing, etc.
   - Match categories to installed plugin types

5. **Include agent descriptions in plugin listings**
   - Helps users understand what each agent does
   - Creates self-documenting CLAUDE.md

6. **Handle errors gracefully**
   - Skip malformed plugins
   - Provide fallback descriptions
   - Log warnings for users

---

## Summary: Plugin Discovery Checklist

When running marketplace-integrator agent:

- [ ] Scan `~/.claude/plugins/` for global plugins
- [ ] Scan `.claude/plugins/` for project-local plugins
- [ ] Read `plugin.json` for each discovered plugin
- [ ] Extract plugin name, description, agent list
- [ ] Read agent frontmatter for each agent
- [ ] Extract agent names and descriptions
- [ ] Generate "Installed Puerto Plugins" section
- [ ] Generate routing rules from agent descriptions
- [ ] Group routing rules by category
- [ ] Preserve existing CLAUDE.md sections
- [ ] Output enhanced CLAUDE.md

---

**End of Marketplace Discovery Skill**

This skill should be used by the marketplace-integrator agent when scanning installed plugins and generating CLAUDE.md integration sections.
