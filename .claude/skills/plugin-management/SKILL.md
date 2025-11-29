# Puerto Plugin Management Skill

**Complete lifecycle management for Claude Code plugins in the Puerto marketplace**

## Core Principles

1. **Skills-First**: Agents MUST read skill documents before proceeding - patterns separate from workflow
2. **Validation-First**: All plugins must pass `scripts/validate-plugin.js` before publication
3. **Consistency**: Follow established Puerto conventions across all plugins
4. **Minimal Structure**: Only create directories that will contain files
5. **Pattern Learning**: Analyze similar plugins (5-10) to maintain consistency

---

## Operations Overview

The plugin manager supports five operations:

| Operation | Description |
|-----------|-------------|
| **Create** | Generate complete plugin structures with intelligent pattern learning |
| **Modify** | Update existing plugins while preserving architectural consistency |
| **Validate** | Check plugin compliance with Puerto standards |
| **Tune** | Optimize plugin configurations (model selection, tool permissions) |
| **Document** | Auto-generate comprehensive READMEs |

---

## Operation 1: Create New Plugin

### Step 1: Gather Requirements

Ask these questions one at a time:

1. **Plugin Name** (Required)
   - Format: `/^[a-z0-9-]+$/` (lowercase-hyphens only)
   - Check if `plugins/[name]/` already exists

2. **Description** (Required)
   - Brief, 1-2 sentences

3. **Version** (Default: 1.0.0)
   - Semver format

4. **Author Name** (Required)

5. **Keywords** (Recommended)
   - Comma-separated for discovery

6. **Number of Agents** (Required, >= 0)

7. **For Each Agent**:
   - Name (lowercase-hyphens)
   - Description (starts with "PROACTIVELY use when..." or "Use when...")
   - Model (haiku/sonnet/opus)
   - Tools (comma-separated)

8. **Number of Skills** (Optional, >= 0)

9. **For Each Skill**:
   - Name (lowercase-hyphens)
   - Description

10. **Templates Needed?** (Optional)

### Step 2: Pattern Learning

Find similar plugins via keywords:

```bash
for dir in plugins/*/; do
  plugin_json="$dir/.claude-plugin/plugin.json"
  if [ -f "$plugin_json" ] && grep -qi "keyword1\|keyword2" "$plugin_json"; then
    echo "$dir"
  fi
done | head -10
```

Extract patterns from 5-10 similar plugins:
- Agent count and structure
- Model selection rationale
- Tool permission patterns
- Skill organization

### Step 3: In-Memory Validation

Before creating files, validate:

```javascript
// Name format
if (!/^[a-z0-9-]+$/.test(pluginName)) {
  error("Plugin name must be lowercase alphanumeric with hyphens only");
}

// Version format
if (!/^\d+\.\d+\.\d+/.test(version)) {
  warn("Version should follow semver format");
}

// Author format
if (typeof author === 'string') {
  error("Author must be object with 'name' property, not string");
}

// Duplicate check
if (fs.existsSync(`plugins/${pluginName}`)) {
  error(`Plugin 'plugins/${pluginName}/' already exists`);
}
```

### Step 4: Present Plan for Approval

Show user what will be created:

```
Plugin Creation Plan
====================

Plugin: my-plugin (v1.0.0)
Description: Brief description here
Author: John Doe
Keywords: frontend, react, typescript

Directory Structure:
--------------------
plugins/my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── agents/
│   ├── agent-1.md
│   └── agent-2.md
├── skills/
│   └── skill-1/
│       └── SKILL.md
└── README.md

Patterns applied from similar plugins:
- Skills-first approach in all agents
- Model selection: Haiku for CRUD, Sonnet for analysis

Does this plan look good? (yes/no):
```

### Step 5: Create Plugin Structure

```bash
# Create directories
mkdir -p "plugins/${plugin_name}/.claude-plugin"
[ $agent_count -gt 0 ] && mkdir -p "plugins/${plugin_name}/agents"
[ $skill_count -gt 0 ] && mkdir -p "plugins/${plugin_name}/skills"
[ $template_count -gt 0 ] && mkdir -p "plugins/${plugin_name}/templates"
```

### Step 6: Validate and Update Catalog

```bash
node scripts/validate-plugin.js "plugins/${plugin_name}"
node scripts/generate-catalog.js
```

### Step 7: Report Completion

```
✅ Plugin Created Successfully!

Location: plugins/my-plugin/

Files Created:
- plugins/my-plugin/.claude-plugin/plugin.json
- plugins/my-plugin/README.md
- plugins/my-plugin/agents/agent-1.md

Validation: ✅ Passed (0 errors, 0 warnings)
Catalog: ✅ Updated

Next Steps:
1. Review generated files and customize
2. Add implementation details to agents
3. Expand skill documents with domain-specific patterns
4. Commit changes: git add plugins/my-plugin .claude-plugin/marketplace.json

Installation Command:
/plugin install my-plugin@puerto
```

---

## Operation 2: Modify Existing Plugin

### Workflow

1. **List plugins**: `ls -d plugins/*/ | sed 's|plugins/||' | sed 's|/$||'`
2. **Select plugin** to modify
3. **Show components** (plugin.json, README, agents, skills, templates)
4. **Select component** to modify
5. **Perform modification** (preserve skills-first approach in agents)
6. **Re-validate**: `node scripts/validate-plugin.js "plugins/${plugin_name}"`
7. **Update catalog** if metadata changed
8. **Report completion**

---

## Operation 3: Validate Plugin

### Prerequisites Check

```bash
# Check Node.js
node_version=$(node --version 2>/dev/null)
if [ -z "$node_version" ]; then
  echo "❌ Error: Node.js not found. Required: >= v18.0.0"
  exit 1
fi

# Check validation script
if [ ! -f scripts/validate-plugin.js ]; then
  echo "❌ Error: scripts/validate-plugin.js not found"
  exit 1
fi
```

### Run Validation

```bash
node scripts/validate-plugin.js "plugins/${plugin_name}"
```

### Present Results with Fix Suggestions

```
Plugin Validation Report
========================

❌ ERRORS (must fix):
  - Missing required field: name
  - author must be object with "name" property

Suggested Fixes:
----------------
Error: "author must be an object..."
Fix: Change in plugin.json:
     Before: "author": "John Doe"
     After:  "author": { "name": "John Doe" }

Would you like me to apply these fixes automatically? (yes/no):
```

---

## Operation 4: Tune/Optimize Plugin

### Analysis Areas

1. **Model Selection**
   - Haiku for CRUD (cost-effective)
   - Sonnet for analysis (balanced)
   - Opus for architecture (deep reasoning)

2. **Tool Permissions**
   - Remove unused tools
   - Follow principle of least privilege

3. **Skills-First Approach**
   - Ensure all agents read skills first

4. **Documentation Quality**
   - Installation command format
   - Feature descriptions
   - Usage examples

### Optimization Report

```
Plugin Optimization Report
==========================

Model Selection:
----------------
✅ agent-1.md: haiku (appropriate for CRUD)
⚠️  agent-2.md: opus (may be overkill)
   Suggestion: Consider 'sonnet' (12x cost savings)

Tool Permissions:
-----------------
⚠️  agent-2.md: Has WebSearch but never uses it
   Suggestion: Remove unused tools

Skills-First:
-------------
❌ agent-1.md: Missing skills-first section
   Suggestion: Add mandatory skill reading step

Overall Score: 7/10
```

---

## Operation 5: Generate Documentation

### README Structure

```markdown
# Plugin Name

[Description from plugin.json]

## Installation

\`\`\`bash
/plugin install plugin-name@puerto
\`\`\`

## Features

- **[Agent 1 Name]**: [Agent 1 description]
- **[Agent 2 Name]**: [Agent 2 description]

## Usage

### [Agent Name]

[Description and examples]

## License

MIT
```

---

## Plugin Structure Reference

### Required Files

```
plugins/[plugin-name]/
├── .claude-plugin/
│   └── plugin.json          # REQUIRED
└── README.md                # HIGHLY RECOMMENDED
```

### Optional Directories (create only when needed)

```
plugins/[plugin-name]/
├── agents/                  # Agent definitions (.md)
├── skills/                  # Skill documents (subdirs with SKILL.md)
├── templates/               # Data templates (.json)
├── commands/                # Slash commands (.md)
└── hooks/                   # Lifecycle hooks (rarely used)
```

---

## plugin.json Format

### Complete Structure

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "Brief, clear description",
  "author": {
    "name": "Author Name"
  },
  "keywords": ["tag1", "tag2"],
  "agents": ["./agents/agent-name.md"],
  "skills": ["./skills/skill-name/SKILL.md"],
  "templates": ["./templates/template-name.json"]
}
```

### Validation Rules

| Field | Required | Format |
|-------|----------|--------|
| name | ✅ | `/^[a-z0-9-]+$/` |
| version | ✅ | Semver (e.g., `1.0.0`) |
| description | ✅ | Non-empty string |
| author | Recommended | Object with `name` property |
| keywords | Recommended | Array of strings |

### Common Mistakes

```json
// ❌ BAD: Author as string
{ "author": "John Doe" }

// ✅ GOOD: Author as object
{ "author": { "name": "John Doe" } }

// ❌ BAD: Uppercase name
{ "name": "MyPlugin" }

// ✅ GOOD: Lowercase with hyphens
{ "name": "my-plugin" }
```

---

## Agent Definition Format

### Complete Structure

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
if [ -f ~/.claude/skills/skill-name/SKILL.md ]; then
    cat ~/.claude/skills/skill-name/SKILL.md
elif [ -f .claude/skills/skill-name/SKILL.md ]; then
    cat .claude/skills/skill-name/SKILL.md
elif [ -f plugins/[plugin-name]/skills/skill-name/SKILL.md ]; then
    cat plugins/[plugin-name]/skills/skill-name/SKILL.md
fi
\`\`\`

This is NON-NEGOTIABLE.

## When Invoked

1. **Read skill** (mandatory, non-skippable)
2. [Step 2]
3. [Step 3]
```

### Model Selection Guidelines

| Model | Use For | Cost |
|-------|---------|------|
| **Haiku** | CRUD, fast processing, templates | ~$0.25/1M tokens |
| **Sonnet** | Analysis, domain expertise, code review | ~$3/1M tokens |
| **Opus** | Architecture, deep reasoning, planning | ~$15/1M tokens |

### Tool Permission Sets

```yaml
# Read-only
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

---

## Skill Document Format

### Directory Structure

```
skills/
└── skill-name/
    └── SKILL.md    # One SKILL.md per subdirectory
```

### Content Pattern

```markdown
# Skill Name

**Production patterns for [domain]**

## Core Principles

1. Principle 1
2. Principle 2

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

---

## Best Practices Checklist

- [ ] Item 1
- [ ] Item 2

---

**Version**: 1.0
**Last Updated**: [Date]
```

---

## Naming Conventions

| Type | Format | Examples |
|------|--------|----------|
| Plugin | `lowercase-hyphens` | `data-analyst`, `web-performance` |
| Agent | `action-noun` | `component-builder`, `progress-analyzer` |
| Skill | `noun-domain` | `component-development`, `api-implementation` |

---

## Validation Commands

```bash
# Validate single plugin
node scripts/validate-plugin.js plugins/my-plugin

# Validate all plugins
for dir in plugins/*/; do
  node scripts/validate-plugin.js "$dir"
done

# Update catalog after changes
node scripts/generate-catalog.js
```

---

## Edge Case Handling

### Duplicate Plugin Names

```
❌ Error: Plugin 'plugins/my-plugin/' already exists

Options:
1. Choose a different name
2. Overwrite existing plugin (WARNING: destructive!)
3. Cancel operation
```

### Invalid Plugin Names

```
❌ Error: Plugin name 'MyPlugin' is invalid

Plugin names must be lowercase alphanumeric with hyphens only.

✅ my-plugin, data-analyst, engineering
❌ MyPlugin, my_plugin, my plugin
```

### Validation Failures

```
❌ Plugin validation failed

Options:
1. Fix errors manually
2. Let me fix automatically (if possible)
3. Cancel operation
```

---

## Best Practices Checklist

### Plugin Structure
- [ ] plugin.json has all required fields
- [ ] Plugin name follows lowercase-hyphens convention
- [ ] Author is object with "name" property
- [ ] Version follows semver format
- [ ] README.md exists and is complete
- [ ] Only needed directories created

### Agent Definition
- [ ] YAML frontmatter complete (name, description, tools, model)
- [ ] Description starts with "PROACTIVELY use when..." or "Use when..."
- [ ] Skills-first approach implemented
- [ ] Model selection appropriate for task
- [ ] Tool permissions follow least privilege
- [ ] Clear numbered workflow steps

### Skill Document
- [ ] Located in `skills/[name]/SKILL.md`
- [ ] Contains production-tested patterns
- [ ] Includes ✅ GOOD / ❌ BAD examples
- [ ] Has core principles section
- [ ] Includes best practices checklist

### Documentation
- [ ] README has `/plugin install name@puerto`
- [ ] Features section lists clear benefits
- [ ] Usage section has examples
- [ ] License section included

### Validation
- [ ] Passes validate-plugin.js with no errors
- [ ] Warnings addressed
- [ ] Catalog regenerated
- [ ] Plugin appears in marketplace.json

---

## Quick Reference

### Create Plugin (Minimal)

```bash
mkdir -p plugins/my-plugin/.claude-plugin

cat > plugins/my-plugin/.claude-plugin/plugin.json <<EOF
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Brief description",
  "author": { "name": "Your Name" },
  "keywords": ["keyword1"]
}
EOF

cat > plugins/my-plugin/README.md <<EOF
# My Plugin

Description

## Installation

\`\`\`bash
/plugin install my-plugin@puerto
\`\`\`

## License

MIT
EOF

node scripts/validate-plugin.js plugins/my-plugin
node scripts/generate-catalog.js
```

---

## Important Reminders

- **NO GIT AUTOMATION**: Creates/modifies files only. User handles git.
- **INTERACTIVE ONLY**: Gather requirements via Q&A before implementing.
- **SKILLS-FIRST**: Read this skill at the start of EVERY invocation.
- **VALIDATE ALWAYS**: Run validation before presenting results.
- **PATTERN LEARNING**: Analyze 5-10 similar plugins for consistency.

---

**Version**: 2.0
**Last Updated**: January 2025
**Use Cases**: Puerto plugin creation, modification, validation, tuning, documentation
