# Puerto Plugin Management Skill

**Production patterns for creating, modifying, validating, and documenting Claude Code plugins in the Puerto marketplace**

## Core Principles

1. **Consistency**: Follow established Puerto conventions across all plugins
2. **Validation**: All plugins must pass `scripts/validate-plugin.js` before publication
3. **Skills-First**: Agents should always reference skill documents for battle-tested patterns
4. **Documentation**: Comprehensive README with installation, features, usage, and license
5. **Quality**: Proper model selection, tool permissions, and architectural patterns

---

## Plugin Structure

### Required Files

Every Puerto plugin MUST have:

```
plugins/[plugin-name]/
├── .claude-plugin/
│   └── plugin.json          # REQUIRED: Plugin metadata
└── README.md                # HIGHLY RECOMMENDED: Documentation
```

### Optional Directories

Create only when needed:

```
plugins/[plugin-name]/
├── agents/                  # Agent definitions (.md files)
├── skills/                  # Skill documents (subdirs with SKILL.md)
├── templates/               # Data templates (.json files)
├── commands/                # Slash commands (.md files)
└── hooks/                   # Lifecycle hooks (rarely used)
```

**✅ GOOD**: Create `agents/` only if plugin has agents
**❌ BAD**: Create all directories even if empty

---

## plugin.json Format

### Complete Structure

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "Brief, clear description of plugin purpose",
  "author": {
    "name": "Author Name"
  },
  "keywords": ["tag1", "tag2", "tag3"],
  "agents": [
    "./agents/agent-name.md",
    "./agents/another-agent.md"
  ],
  "skills": [
    "./skills/skill-name/SKILL.md"
  ],
  "templates": [
    "./templates/template-name.json"
  ]
}
```

### Required Fields

```json
{
  "name": "plugin-name",          // REQUIRED: lowercase-hyphens only
  "version": "1.0.0",             // REQUIRED: semver format
  "description": "Description"    // REQUIRED: brief and clear
}
```

### Recommended Fields

```json
{
  "author": {                     // RECOMMENDED: object, not string!
    "name": "Author Name"
  },
  "keywords": ["keyword1"],       // RECOMMENDED: for discovery
  "agents": ["./agents/..."],     // Optional: explicit agent list
  "skills": ["./skills/..."]      // Optional: explicit skill list
}
```

### Validation Rules

**Name Validation:**
```javascript
// ✅ GOOD
"my-plugin-name"
"data-analyst"
"engineering"

// ❌ BAD
"MyPlugin"           // No uppercase
"my_plugin"          // No underscores
"my plugin"          // No spaces
"my-plugin!"         // No special chars (except hyphens)
```

**Author Format:**
```json
// ✅ GOOD: Object with "name" property
{
  "author": {
    "name": "John Doe",
    "email": "john@example.com"  // optional
  }
}

// ❌ BAD: String
{
  "author": "John Doe"  // Will cause validation error!
}
```

**Version Format:**
```json
// ✅ GOOD: Semver
"1.0.0"
"2.1.3"
"0.1.0-beta"

// ❌ BAD: Non-semver
"1.0"
"v1.0.0"
"1"
```

---

## Agent Definition Format

### Complete Agent Structure

```markdown
---
name: agent-name
description: PROACTIVELY use when [trigger]. [What it does].
tools: Read, Write, Edit, Bash, Grep, Glob
model: haiku
---

You are a [role] specializing in [domain].

## CRITICAL: Skills-First Approach

**MANDATORY FIRST STEP**: Read skill before proceeding.

\`\`\`bash
# Priority order for skill location
if [ -f ~/.claude/skills/skill-name/SKILL.md ]; then
    cat ~/.claude/skills/skill-name/SKILL.md
elif [ -f .claude/skills/skill-name/SKILL.md ]; then
    cat .claude/skills/skill-name/SKILL.md
elif [ -f plugins/[plugin-name]/skills/skill-name/SKILL.md ]; then
    cat plugins/[plugin-name]/skills/skill-name/SKILL.md
fi
\`\`\`

This is NON-NEGOTIABLE. The skill contains battle-tested patterns.

## When Invoked

1. **Read skill** (mandatory, non-skippable)

2. [Step 2 of workflow]

3. [Step 3 of workflow]

...
```

### YAML Frontmatter

**Required Fields:**
```yaml
---
name: agent-name              # REQUIRED: Agent identifier
description: Description      # REQUIRED: When to use + what it does
tools: Read, Write, Edit      # REQUIRED: Tool permissions
model: haiku                  # REQUIRED: haiku, sonnet, or opus
---
```

**Description Best Practices:**
```yaml
# ✅ GOOD: Clear trigger + action
description: PROACTIVELY use when creating React components. Skill-aware builder that produces production-ready components with TypeScript and tests.

# ✅ GOOD: Use when pattern
description: Use when implementing API authentication and authorization. Creates secure JWT, OAuth 2.0, and API key authentication with proper security best practices.

# ❌ BAD: Vague
description: Helps with React stuff

# ❌ BAD: No trigger
description: Builds React components
```

### Model Selection Guidelines

**Haiku** (Fast, Cost-Effective):
- CRUD operations
- Fast processing
- Structured tasks
- File operations
- Template-based generation
- **Cost**: ~$0.25 per 1M input tokens

**Sonnet** (Balanced, Domain Expertise):
- Domain expertise required
- Analysis and reasoning
- Complex decisions
- Interactive workflows
- Code review
- **Cost**: ~$3 per 1M input tokens

**Opus** (Powerful, Deep Reasoning):
- Deep reasoning required
- Architecture design
- Complex problem-solving
- Multi-step planning
- **Cost**: ~$15 per 1M input tokens

**Examples:**
```yaml
# ✅ GOOD: CRUD task uses Haiku
name: record-tracker
model: haiku
description: Fast workout entry with volume calculations

# ✅ GOOD: Analysis task uses Sonnet
name: progress-analyzer
model: sonnet
description: Progress visualization and trend analysis

# ✅ GOOD: Architecture design uses Opus
name: system-architect
model: opus
description: Creates ADRs, architecture diagrams, and technology recommendations

# ❌ BAD: CRUD task uses Opus (wasteful)
name: data-logger
model: opus  # Should be haiku!
description: Logs data entries
```

### Tool Permissions (Principle of Least Privilege)

**Common Tool Sets:**
```yaml
# Read-only agent
tools: Read, Grep, Glob, Bash

# File creator
tools: Read, Write, Bash, Grep, Glob

# File editor
tools: Read, Edit, Bash, Grep, Glob

# Full file operations
tools: Read, Write, Edit, Bash, Grep, Glob

# With web research
tools: Read, Write, Edit, Bash, Grep, Glob, WebSearch, WebFetch
```

**✅ GOOD**: Only request tools actually needed
**❌ BAD**: Request all tools "just in case"

### Skills-First Approach (Mandatory)

**Multi-Location Check Pattern:**
```bash
# Priority order:
# 1. User's global skills (~/.claude/skills/)
# 2. Project skills (.claude/skills/)
# 3. Plugin skills (plugins/[name]/skills/)

if [ -f ~/.claude/skills/skill-name/SKILL.md ]; then
    cat ~/.claude/skills/skill-name/SKILL.md
elif [ -f .claude/skills/skill-name/SKILL.md ]; then
    cat .claude/skills/skill-name/SKILL.md
elif [ -f plugins/[plugin-name]/skills/skill-name/SKILL.md ]; then
    cat plugins/[plugin-name]/skills/skill-name/SKILL.md
fi
```

**Why Skills-First?**
- Separates patterns (skill) from workflow (agent)
- Enables independent updates to patterns
- Reusable across multiple agents
- Battle-tested patterns from production

**✅ GOOD**: Agent reads skill before proceeding
**❌ BAD**: Agent embeds all knowledge inline

---

## Skill Document Format

### Directory Structure

```
skills/
└── skill-name/
    └── SKILL.md              # One SKILL.md per subdirectory
```

**✅ GOOD**: `skills/component-development/SKILL.md`
**❌ BAD**: `skills/component-development.md` (no subdirectory)
**❌ BAD**: `skills/SKILL.md` (should be in subdirectory)

### Skill Content Pattern

```markdown
# Skill Name

**Production patterns for [domain]**

## Core Principles

1. Principle 1
2. Principle 2
3. Principle 3

---

## Pattern 1

### Description

[Explanation]

### Example

\`\`\`[language]
// ✅ GOOD
[good example]

// ❌ BAD
[bad example]
\`\`\`

## Pattern 2

...

---

## Best Practices Checklist

- [ ] Checklist item 1
- [ ] Checklist item 2

---

**Version**: 1.0
**Last Updated**: January 2025
```

**✅ GOOD**: Production-tested patterns with examples
**❌ BAD**: Theoretical patterns without examples

---

## Template Format

### JSON Template Structure

```json
{
  "name": "Template Name",
  "description": "What this template is for",
  "version": "1.0.0",
  "schema": {
    "field1": "string",
    "field2": "number",
    "field3": "array"
  },
  "example": {
    "field1": "example value",
    "field2": 42,
    "field3": ["item1", "item2"]
  }
}
```

**✅ GOOD**: Include schema and example
**❌ BAD**: Template without documentation

---

## README Format

### Required Sections

```markdown
# Plugin Name

Brief, compelling description (1-2 sentences).

## Installation

\`\`\`bash
/plugin install plugin-name@puerto
\`\`\`

## Features

- Feature 1: Clear benefit
- Feature 2: Clear benefit
- Feature 3: Clear benefit

## Usage

### [Operation/Use Case]

[Description]

\`\`\`[language]
[Example]
\`\`\`

## License

MIT
```

### Installation Command Format

**✅ GOOD**:
```bash
/plugin install my-plugin@puerto
```

**❌ BAD**:
```bash
# Wrong marketplace
/plugin install my-plugin@marketplace

# Missing marketplace
/plugin install my-plugin

# Wrong command
npm install my-plugin
```

### Features Section Best Practices

**✅ GOOD**: Clear benefits
```markdown
## Features

- **Smart Component Generation**: Creates production-ready React/Vue/Svelte components with TypeScript
- **Accessibility Built-in**: WCAG 2.1 AA compliance validation
- **Performance Optimized**: Automatic code splitting and lazy loading
```

**❌ BAD**: Vague features
```markdown
## Features

- Makes components
- Checks accessibility
- Improves performance
```

---

## Naming Conventions

### Plugin Names

**Format**: `lowercase-with-hyphens`

**✅ GOOD**:
```
data-analyst
engineering
engineering
web-performance-auditor
```

**❌ BAD**:
```
DataAnalyst           // No PascalCase
data_analyst          // No underscores
data analyst          // No spaces
data-analyst-plugin   // Don't add "plugin" suffix
```

### Agent Names

**Format**: `descriptive-action-noun`

**✅ GOOD**:
```
component-builder
api-tester
progress-analyzer
workout-logger
```

**❌ BAD**:
```
builder              // Too vague
BuildComponent       // No PascalCase
build_component      // No underscores
```

### Skill Names

**Format**: `noun-focused` (describes domain, not action)

**✅ GOOD**:
```
component-development
api-implementation
workout-logging
state-management
```

**❌ BAD**:
```
building-components  // Should be component-development
how-to-api          // Should be api-implementation
```

---

## Validation Requirements

### Required Field Validation

From `scripts/validate-plugin.js`:

1. **Directory Structure**:
   - `.claude-plugin/` directory must exist
   - `.claude-plugin/plugin.json` must exist
   - Optional dirs (agents/, skills/, commands/) must be directories, not files

2. **plugin.json Fields**:
   - `name`: Required, lowercase-hyphens only, regex: `/^[a-z0-9-]+$/`
   - `version`: Required, semver format (e.g., `1.0.0`)
   - `description`: Required, non-empty string
   - `author`: Recommended, must be object with `name` property (NOT string!)

3. **README.md**:
   - Highly recommended (warning if missing)
   - Should include installation, features, usage, license

### Validation Commands

```bash
# Validate single plugin
node scripts/validate-plugin.js plugins/my-plugin

# Validate all plugins
for dir in plugins/*/; do
  node scripts/validate-plugin.js "$dir"
done
```

### Validation Output

```
✅ Plugin validation passed!

❌ ERRORS:
  - Missing required field in plugin.json: name
  - Plugin name must be lowercase alphanumeric with hyphens only
  - author must be an object with a "name" property, not a string

⚠️  WARNINGS:
  - Missing README.md - highly recommended for documentation
  - Version should follow semver format (e.g., 1.0.0)
```

**Errors**: MUST fix before plugin is valid
**Warnings**: SHOULD fix for quality

---

## Catalog Integration

### Catalog Generation

After creating/modifying plugins, regenerate catalog:

```bash
node scripts/generate-catalog.js
```

This updates `.claude-plugin/marketplace.json` with plugin entries.

### Marketplace Manifest Structure

```json
{
  "plugins": [
    {
      "name": "plugin-name",
      "version": "1.0.0",
      "description": "Description",
      "author": { "name": "Author" },
      "keywords": ["tag1", "tag2"],
      "source": "./plugins/plugin-name"
    }
  ]
}
```

**✅ GOOD**: Run catalog generation after plugin changes
**❌ BAD**: Forget to update catalog (plugin won't be discoverable)

---

## Pattern Learning from Existing Plugins

### Keyword-Based Filtering

When creating similar plugins, analyze relevant examples:

```bash
# Example: Creating frontend plugin
# Search for plugins with "frontend", "react", "component" keywords

for dir in plugins/*/; do
  if grep -q '"frontend"\|"react"\|"component"' "$dir/.claude-plugin/plugin.json"; then
    echo "$dir"
  fi
done
```

**✅ GOOD**: Analyze 5-10 similar plugins
**❌ BAD**: Analyze all 150+ plugins (excessive tokens/time)

### Patterns to Extract

From similar plugins, identify:

1. **Agent Count**: How many agents? (1 agent vs. 4 agents)
2. **Model Selection**: Which models for which agents?
3. **Tool Permissions**: What tools do agents need?
4. **Skill Structure**: How are skills organized?
5. **Template Formats**: What template structures exist?

---

## Best Practices Summary

### Plugin Structure
- [ ] plugin.json has all required fields
- [ ] Plugin name follows lowercase-hyphens convention
- [ ] Author is object with "name" property (not string)
- [ ] Version follows semver format (e.g., 1.0.0)
- [ ] README.md exists and is complete
- [ ] Only needed directories created (no empty agents/, skills/)

### Agent Definition
- [ ] YAML frontmatter with name, description, tools, model
- [ ] Description starts with "PROACTIVELY use when..." or "Use when..."
- [ ] Skills-first approach implemented (multi-location check)
- [ ] Model selection appropriate for task complexity
- [ ] Tool permissions follow principle of least privilege
- [ ] Clear numbered workflow steps

### Skill Document
- [ ] Located in `skills/[name]/SKILL.md` subdirectory
- [ ] Contains production-tested patterns
- [ ] Includes code examples (✅ GOOD / ❌ BAD)
- [ ] Has core principles section
- [ ] Includes best practices checklist

### Documentation
- [ ] README has installation section with `/plugin install name@puerto`
- [ ] Features section lists clear benefits
- [ ] Usage section has examples
- [ ] License section included (typically MIT)

### Validation
- [ ] Passes `scripts/validate-plugin.js` with no errors
- [ ] No validation warnings (or warnings addressed)
- [ ] Catalog regenerated via `scripts/generate-catalog.js`
- [ ] Plugin appears in `.claude-plugin/marketplace.json`

---

## Common Mistakes to Avoid

### ❌ BAD: Author as String
```json
{
  "author": "John Doe"  // WRONG! Will fail validation
}
```

### ✅ GOOD: Author as Object
```json
{
  "author": {
    "name": "John Doe"
  }
}
```

---

### ❌ BAD: Uppercase Plugin Name
```json
{
  "name": "MyPlugin"  // WRONG! Must be lowercase-hyphens
}
```

### ✅ GOOD: Lowercase with Hyphens
```json
{
  "name": "my-plugin"
}
```

---

### ❌ BAD: Empty Optional Directories
```
plugins/my-plugin/
├── agents/          # Empty directory - wasteful!
├── skills/          # Empty directory - wasteful!
└── templates/       # Empty directory - wasteful!
```

### ✅ GOOD: Only Needed Directories
```
plugins/my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── agents/          # Has agents
│   └── my-agent.md
└── README.md
```

---

### ❌ BAD: Agent Without Skills-First
```markdown
---
name: my-agent
---

You are a specialist.

## When Invoked

1. Do the task immediately
```

### ✅ GOOD: Agent With Skills-First
```markdown
---
name: my-agent
---

You are a specialist.

## CRITICAL: Skills-First Approach

**MANDATORY FIRST STEP**: Read skill before proceeding.

\`\`\`bash
if [ -f ~/.claude/skills/my-skill/SKILL.md ]; then
    cat ~/.claude/skills/my-skill/SKILL.md
fi
\`\`\`

## When Invoked

1. **Read skill** (mandatory, non-skippable)
2. Proceed with task
```

---

### ❌ BAD: Wrong Model for Task
```yaml
name: data-logger
model: opus          # Overkill for simple CRUD!
description: Logs data entries to database
```

### ✅ GOOD: Appropriate Model
```yaml
name: data-logger
model: haiku         # Fast and cost-effective for CRUD
description: Fast data entry with validation
```

---

### ❌ BAD: Vague Agent Description
```yaml
description: Helps with stuff
```

### ✅ GOOD: Clear Trigger and Action
```yaml
description: PROACTIVELY use when creating database schemas. Generates ER diagrams, migration files, and indexing strategies.
```

---

## Quick Reference

### Plugin Creation Checklist

```bash
# 1. Create plugin directory
mkdir -p plugins/my-plugin/.claude-plugin

# 2. Create plugin.json
cat > plugins/my-plugin/.claude-plugin/plugin.json <<EOF
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Brief description",
  "author": { "name": "Your Name" },
  "keywords": ["keyword1", "keyword2"]
}
EOF

# 3. Create README.md
cat > plugins/my-plugin/README.md <<EOF
# My Plugin

Description

## Installation
\`\`\`bash
/plugin install my-plugin@puerto
\`\`\`
EOF

# 4. Create agents (if needed)
mkdir -p plugins/my-plugin/agents

# 5. Validate
node scripts/validate-plugin.js plugins/my-plugin

# 6. Update catalog
node scripts/generate-catalog.js
```

### Validation Quick Check

```bash
# Must pass (no errors)
node scripts/validate-plugin.js plugins/my-plugin

# Should address warnings
# - Missing README.md
# - Missing author field
# - Non-semver version
```

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: Puerto plugin creation, modification, validation, documentation
