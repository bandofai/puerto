# CLAUDE.md Master Plugin

**Version**: 1.0.0
**Status**: Production Ready

Master CLAUDE.md configuration specialist. Creates, validates, and optimizes CLAUDE.md files with Puerto marketplace integration for automatic task routing.

---

## What This Plugin Does

This plugin helps you create and maintain CLAUDE.md configuration files that enable Claude Code to automatically use your installed Puerto plugins. With proper CLAUDE.md configuration, Claude will proactively invoke the right expert agents without you having to specify them every time.

### The Problem

When you install Puerto department plugins (like `engineering`, `design`, or `marketing`), Claude Code gains access to specialized agents. However, **Claude won't automatically know WHEN to use these agents unless you guide it** with a CLAUDE.md configuration file.

### The Solution

This plugin provides three specialized agents that work together to:

1. **Generate** complete CLAUDE.md files from scratch (interactive Q&A)
2. **Validate** existing CLAUDE.md files for best practices
3. **Integrate** installed Puerto plugins automatically (scan & generate routing rules)

---

## What's Included

### 3 Specialized Agents

#### 1. `claude-md-generator` (Sonnet)
**Use when**: Creating CLAUDE.md from scratch

**What it does**:
- Interactive Q&A to gather project information
- Discovers installed Puerto plugins automatically
- Generates production-ready CLAUDE.md with routing rules
- Includes project patterns and domain knowledge

**Invocation**: Claude will use this when you ask to "create CLAUDE.md" or "set up CLAUDE.md"

**Example Usage**:
```
You: "Help me create a CLAUDE.md for my React project"
Claude: [Invokes claude-md-generator]
        "What type of project is this?"
        1. React SPA
        2. Next.js full-stack
        ...
```

---

#### 2. `claude-md-validator` (Haiku - Fast & Cost-Effective)
**Use when**: Validating existing CLAUDE.md files

**What it does**:
- Checks CLAUDE.md best practices (not pedantic syntax)
- Validates WHEN/AUTOMATICALLY routing rule format
- Detects common mistakes (vague rules, missing plugins)
- Provides specific, actionable fixes with line numbers

**Invocation**: Claude will use this when you ask to "validate CLAUDE.md" or "check my CLAUDE.md"

**Example Usage**:
```
You: "Is my CLAUDE.md following best practices?"
Claude: [Invokes claude-md-validator]

        # Validation Report
        Status: NEEDS IMPROVEMENT

        ❌ Critical: Vague routing rule (Line 25)
        Current: "Use frontend agents for frontend work"
        Fix: WHEN user says "create [component name] component"
             → AUTOMATICALLY invoke: engineering/frontend-engineer
```

---

#### 3. `marketplace-integrator` (Sonnet)
**Use when**: Optimizing CLAUDE.md for installed Puerto plugins

**What it does**:
- Scans `~/.claude/plugins/` for installed plugins
- Extracts agent information from plugin manifests
- Generates routing rules from agent descriptions
- Enhances existing CLAUDE.md with marketplace integration

**Invocation**: Claude will use this when you ask to "integrate my plugins into CLAUDE.md" or "update CLAUDE.md with installed plugins"

**Example Usage**:
```
You: "I just installed engineering and engineering plugins. Update my CLAUDE.md to use them."
Claude: [Invokes marketplace-integrator]

        🔍 Scanning for installed Puerto plugins...
        ✓ Found: engineering (4 agents)
        ✓ Found: engineering (4 agents)

        Generated routing rules:
        - Frontend Development (4 rules)
        - Backend Development (4 rules)

        Would you like me to save the enhanced CLAUDE.md?
```

---

### 3 Comprehensive Skills

#### 1. `claude-md-syntax`
Complete CLAUDE.md specification including:
- All sections and structure
- WHEN/AUTOMATICALLY routing pattern (THE CRITICAL FEATURE)
- Complete examples by project type (React SPA, Next.js, microservices)
- Common mistakes and fixes
- Best practices

#### 2. `task-routing-patterns`
Routing patterns for Puerto plugins:
- WHEN/AUTOMATICALLY syntax and variations
- Trigger phrases by plugin category
- Pattern templates for different task types
- Examples for all major Puerto plugins

#### 3. `marketplace-discovery`
Puerto marketplace knowledge:
- Plugin discovery via filesystem scanning
- Agent description parsing
- Routing rule generation from descriptions
- 140+ plugins across 27 squads

---

## Installation

```bash
/plugin install claude-md-master
```

Or manually:
```bash
# Global installation
cp -r plugins/claude-md-master ~/.claude/plugins/

# Project-local installation
cp -r plugins/claude-md-master .claude/plugins/
```

---

## Usage Examples

### Example 1: Create CLAUDE.md from Scratch

**Scenario**: You have a new React + Express project and want to set up CLAUDE.md.

```
You: "Create a CLAUDE.md for my React e-commerce app with Express backend"

Claude: [Invokes claude-md-generator automatically]

Agent: "I'll help you create a comprehensive CLAUDE.md. Let me ask a few questions..."

Agent: "What type of project is this?"
       1. React SPA
       2. Next.js full-stack
       3. Node.js backend API
       ...

You: 1

Agent: "What frontend technologies are you using?"
       Examples: React 18, TypeScript, Tailwind CSS

You: React 18, TypeScript, Tailwind CSS, React Query

Agent: "What backend technologies are you using?"

You: Node.js 20, Express, PostgreSQL, Prisma

Agent: "Which Puerto plugins have you installed?"
       1. Let me scan automatically (recommended)
       2. I'll list them manually
       3. I haven't installed any yet

You: 1

Agent: [Scans system]
       🔍 Scanning for installed Puerto plugins...
       ✓ Found: engineering (4 agents)
       ✓ Found: engineering (4 agents)
       ✓ Found: engineering (3 agents)

Agent: "Excellent! Do you have specific project patterns I should document?"
       1. Yes, I'll describe them
       2. No, use common conventions for React + Express

You: 2

Agent: [Generates complete CLAUDE.md]

       ## Generated CLAUDE.md Preview

       # My React E-commerce App

       ## Project Type
       React SPA with Express backend

       ## Tech Stack
       - Frontend: React 18, TypeScript, Tailwind CSS, React Query
       - Backend: Node.js 20, Express, PostgreSQL, Prisma

       ## Installed Puerto Plugins
       - engineering (frontend-engineer, backend-engineer, devops-engineer, ...)
       - design (ux-researcher, ux-writer, accessibility-specialist, ...)
       - product (product-manager, data-analyst, ...)

       ## Automatic Task Routing

       ### Frontend Development
       WHEN user says "create [component name] component"
       → AUTOMATICALLY invoke: engineering/frontend-engineer
       ...

       Would you like me to save this to CLAUDE.md?

You: Yes

Agent: ✅ CLAUDE.md created successfully!
```

**Result**: Complete, production-ready CLAUDE.md with 10+ routing rules.

---

### Example 2: Validate Existing CLAUDE.md

**Scenario**: You have a CLAUDE.md but want to check if it follows best practices.

```
You: "Check if my CLAUDE.md is properly configured"

Claude: [Invokes claude-md-validator automatically]

Agent: [Reads CLAUDE.md]

       # CLAUDE.md Validation Report

       Status: NEEDS IMPROVEMENT

       ## Summary
       - Total Issues: 3
         - ❌ Critical: 1
         - ⚠️  Warning: 2

       ## Critical Issues

       ❌ Issue 1: Vague routing rule (Line 25)

       Current:
       ```
       Use frontend agents for frontend work
       ```

       Problem: Not using WHEN/AUTOMATICALLY pattern

       Fix:
       ```markdown
       WHEN user says "create [component name] component"
       → AUTOMATICALLY invoke: engineering/frontend-engineer
       ```

       ## Warnings

       ⚠️  Warning 1: No code examples in Project Patterns (Line 50)

       Suggestion: Add concrete TypeScript/React examples

       ## What's Good ✅
       - ✅ Has Project Type and Tech Stack sections
       - ✅ Plugins are properly listed

       ## Next Steps
       1. Fix critical routing rule format
       2. Add code examples to patterns
       3. Re-run validation after fixes

You: "Can you fix those issues?"

Claude: [Updates CLAUDE.md with proper WHEN/AUTOMATICALLY patterns]
```

**Result**: Specific, actionable validation report with fixes.

---

### Example 3: Integrate Newly Installed Plugins

**Scenario**: You just installed `engineering` plugin and want to add it to your existing CLAUDE.md.

```
You: "I just installed engineering plugin. Update my CLAUDE.md to use it."

Claude: [Invokes marketplace-integrator automatically]

Agent: [Scans plugins]

       🔍 Scanning for installed Puerto plugins...
       ✓ Found: engineering (4 agents)
       ✓ Found: engineering (4 agents)
       ✓ Found: engineering (3 agents)
       ✓ Found: engineering (4 agents) ← NEW

       ## Enhancement Summary

       New Plugins Detected:
       ✓ engineering (4 agents)

       Generated Routing Rules:
       - DevOps & Deployment (4 new rules)

       Preserved Sections:
       ✓ Project Type, Tech Stack, Patterns, Domain Knowledge

       Preview of additions:

       ### engineering
       - cicd-builder: Set up CI/CD pipelines (GitHub Actions, GitLab CI)
       - deployment-orchestrator: Implement deployment strategies
       - infrastructure-manager: Create Infrastructure as Code
       - monitoring-setup: Implement observability and monitoring

       ### DevOps & Deployment

       WHEN user says "set up CI/CD"
       → AUTOMATICALLY invoke: engineering/devops-engineer

       WHEN user says "deploy to [environment]"
       → AUTOMATICALLY invoke: engineering/devops-engineer
       ...

       Save enhanced CLAUDE.md?

You: Yes

Agent: ✅ CLAUDE.md enhanced successfully!
       ✓ Backed up original to CLAUDE.md.backup
       ✓ Added engineering plugin
       ✓ Generated 4 new routing rules
```

**Result**: CLAUDE.md updated with new plugin integration, original backed up.

---

## How It Works

### The WHEN/AUTOMATICALLY Pattern

The most critical feature of CLAUDE.md is the **WHEN/AUTOMATICALLY** routing pattern. This tells Claude exactly when to invoke specific agents:

```markdown
WHEN user says "create [component name] component"
→ AUTOMATICALLY invoke: engineering/frontend-engineer
```

**Why this matters**: Without explicit routing rules, Claude won't know when to use your installed Puerto plugins. The WHEN/AUTOMATICALLY pattern creates automatic agent invocation.

### Skills-First Architecture

All three agents follow a **skills-first** approach:

1. **First action**: Load comprehensive skill files
2. **Use knowledge**: Apply patterns from skills
3. **Generate output**: Production-ready CLAUDE.md

This ensures agents have complete, offline knowledge of CLAUDE.md syntax and best practices.

### Plugin Discovery Process

The `marketplace-integrator` agent:

1. Scans `~/.claude/plugins/` (global) and `.claude/plugins/` (project-local)
2. Reads `plugin.json` manifests to find agents
3. Extracts agent descriptions from markdown frontmatter
4. Parses "PROACTIVELY use when [condition]" patterns
5. Generates WHEN/AUTOMATICALLY rules automatically
6. Categorizes rules (Frontend, Backend, Database, DevOps, etc.)

**No manual plugin listing required** - completely autonomous discovery.

---

## Key Features

✅ **Interactive Generation**: Q&A approach for creating CLAUDE.md (like `/brainstorm` command)
✅ **Autonomous Plugin Discovery**: Scans filesystem for installed plugins
✅ **Best Practice Validation**: Checks routing rule format and specificity
✅ **Smart Merge**: Preserves existing content when enhancing CLAUDE.md
✅ **Specific Fixes**: Provides exact fixes with line numbers
✅ **Cost Optimized**: Haiku for fast validation (90% cheaper than Sonnet)
✅ **Production Ready**: Generated CLAUDE.md works immediately
✅ **Skills-First**: Comprehensive offline knowledge base
✅ **Safe Operations**: Always backs up existing CLAUDE.md

---

## File Structure

```
plugins/claude-md-master/
├── .claude-plugin/
│   └── plugin.json                     # Plugin manifest
├── agents/
│   ├── claude-md-generator.md          # Sonnet - Interactive generation
│   ├── claude-md-validator.md          # Haiku - Fast validation
│   └── marketplace-integrator.md       # Sonnet - Plugin discovery
├── skills/
│   ├── claude-md-syntax/
│   │   └── SKILL.md                    # Complete CLAUDE.md spec
│   ├── task-routing-patterns/
│   │   └── SKILL.md                    # Routing patterns
│   └── marketplace-discovery/
│       └── SKILL.md                    # Plugin discovery methods
├── templates/
│   └── [Future: Template files]
└── README.md                           # This file
```

---

## Requirements

- **Claude Code**: Latest version
- **jq**: For JSON parsing (plugin discovery)
  ```bash
  # macOS
  brew install jq

  # Ubuntu/Debian
  apt-get install jq
  ```

---

## Troubleshooting

### Issue: "ERROR: claude-md-syntax skill not found"

**Cause**: Skills not installed in expected locations

**Fix**: Ensure plugin is installed properly:
```bash
# Check installation
ls -la ~/.claude/plugins/claude-md-master/skills/

# Or for project-local
ls -la .claude/plugins/claude-md-master/skills/
```

### Issue: Plugin discovery finds no plugins

**Cause**: Plugins installed in non-standard location or not installed

**Fix**:
1. Check plugin installation:
   ```bash
   ls ~/.claude/plugins/
   ```
2. Install plugins if missing:
   ```bash
   /plugin install engineering
   /plugin install engineering
   ```

### Issue: Generated routing rules are too generic

**Cause**: Agent descriptions in plugins lack specific trigger conditions

**Fix**: Manually refine routing rules in CLAUDE.md after generation. The validator will help identify vague rules.

---

## Best Practices

1. **Create CLAUDE.md early**: Set it up when starting a new project
2. **Validate regularly**: Run validator after making changes
3. **Update when installing plugins**: Use marketplace-integrator to add new plugins
4. **Keep it concise**: CLAUDE.md should be 100-500 lines (not thousands)
5. **Test routing rules**: Ask Claude to perform tasks and verify agent invocation
6. **Version control**: Commit CLAUDE.md to your repository
7. **Review quarterly**: Ensure tech stack and plugins are up to date

---

## Integration with Other Plugins

This plugin enhances CLAUDE.md for **all Puerto marketplace plugins**:

- **Frontend**: engineering, design, design
- **Backend**: engineering, engineering
- **Database**: database-architect
- **DevOps**: engineering, engineering
- **Testing**: code-reviewer, test-runner
- **Security**: security-auditor
- **Performance**: web-performance-auditor
- **And 130+ more plugins**

Generate routing rules automatically for any installed plugin.

---

## Roadmap

### Future Enhancements

- [ ] Template library for common project types
- [ ] CLAUDE.md diff viewer (compare before/after)
- [ ] Interactive routing rule refinement
- [ ] Plugin recommendation based on tech stack
- [ ] CLAUDE.md analytics (which rules are used most)

---

## Contributing

Found a bug or have a suggestion? Open an issue in the Puerto marketplace repository.

---

## License

Part of the Puerto Plugin Collection

---

## Support

- **Documentation**: See `docs/configuring-claude-md.md` in Puerto repo
- **Examples**: This README contains complete usage examples
- **Issues**: Report issues to Puerto marketplace repository
- **Community**: Share your CLAUDE.md configurations with other users

---

## Summary

The **CLAUDE.md Master Plugin** is your expert assistant for creating, validating, and optimizing CLAUDE.md configuration files. It enables Claude Code to automatically use your installed Puerto plugins through intelligent task routing rules.

**Three agents, one goal**: Production-ready CLAUDE.md that makes Claude proactively use the right expert agents for every task.

**Get Started**:
```
/plugin install claude-md-master
"Help me create a CLAUDE.md for my project"
```
