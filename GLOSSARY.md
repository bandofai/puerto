# Glossary

**Terms and definitions for Puerto's digital agency structure.**

---

## A

### Agent
A specialized AI role that performs specific tasks within Puerto. Agents are autonomous and can use tools (Read, Write, Bash, etc.) to complete their work.

**Example:** `engineering/frontend-engineer` is an agent that builds React/Vue applications.

### Agency Structure
Puerto's organizational model based on an 8-department digital agency with 27 specialized roles, mimicking a real 20-30 person company.

**Departments:** Engineering, Design, Marketing, Product, Sales, Operations, Leadership, Infrastructure

---

## C

### Chief Product Officer (CPO)
Leadership role in the Product department responsible for product vision, strategy, and roadmap. Reports to Chief Strategy Officer.

**Invocation:** `product/chief-product-officer`

### Chief Strategy Officer (CSO)
Top leadership role responsible for company vision, strategic planning, and executive reporting. All department leads report to CSO.

**Invocation:** `leadership/chief-strategy-officer`

### Command
A slash command that users invoke directly (e.g., `/brainstorm`, `/implement`). Commands provide interactive workflows.

**Example:** `/brainstorm feature-name` starts an interactive Q&A for defining requirements.

### Consolidation
The process of reorganizing Puerto from 100+ individual plugins into 8 department-based plugins with 27 roles.

**Timeline:** Completed November 2025

---

## D

### Department
A functional group containing multiple related roles. Puerto has 8 departments matching real agency structure.

**List:**
- 🔧 **Engineering** (7 roles)
- 🎨 **Design** (4 roles)
- 📢 **Marketing** (5 roles)
- 📊 **Product** (4 roles)
- 💼 **Sales** (3 roles)
- ⚙️ **Operations** (3 roles)
- 🎯 **Leadership** (1 role)
- 🏗️ **Infrastructure** (tools)

### Department Plugin
A single plugin containing all agents and skills for one department.

**Example:** `engineering@puerto` contains 7 engineering roles (Frontend Engineer, Backend Engineer, etc.)

---

## E

### Engineering Lead
Leadership role in Engineering department responsible for technical architecture and system design. Reports to Chief Strategy Officer.

**Invocation:** `engineering/engineering-lead`

---

## F

### Frontmatter
Metadata at the top of agent markdown files defining model, description, and tools.

**Example:**
```yaml
---
model: sonnet
description: React/Vue component builder
tools:
  - Read
  - Write
  - Edit
---
```

---

## H

### Hook
A shell command that executes in response to events like tool calls. Configured in settings for custom workflows.

---

## I

### Infrastructure
The collection of 7 essential plugins providing core functionality:
1. Essentials (Serena, Context7, Sequential Thinking, Playwright)
2. Chrome DevTools
3. Subagent Creator
4. CLAUDE.md Master
5. Cloudflare
6. Orchestrator
7. Figma

### Invocation Pattern
The format for calling agents: `[department]/[role-name]`

**Examples:**
- `engineering/frontend-engineer`
- `design/ux-researcher`
- `marketing/seo-specialist`

---

## M

### Marketplace
A registry of Claude Code plugins. Puerto is accessed via marketplace: `bandofai/puerto`

**Command:** `/plugin marketplace add bandofai/puerto`

### MCP Server
Model Context Protocol server providing external tool integrations (e.g., Serena for code navigation, Context7 for documentation).

**Examples:** Serena, Context7, Sequential Thinking, Playwright

### Mega-Skill
Comprehensive skill files (500-1,400 lines) consolidating knowledge from multiple previous plugins.

**Example:** `frontend-development` mega-skill combines knowledge from frontend-developer, component-builder, and style-implementer.

---

## O

### Org Chart
Visual diagram showing Puerto's 8-department structure with reporting lines. Available in TEAM-STRUCTURE.md with both Mermaid and ASCII formats.

---

## P

### Plugin
A package that extends Claude Code with commands, agents, skills, templates, or MCP servers.

**Types:**
- **Department plugins:** engineering, design, marketing, etc.
- **Infrastructure plugins:** essentials, chrome-devtools, etc.
- **Custom plugins:** User-created plugins

---

## R

### RACI Matrix
Responsibility Assignment Matrix showing who is Responsible, Accountable, Consulted, and Informed for each task across project phases.

**Available in:** ROLE-MATRIX.md

### Role
A specific position within a department (e.g., Frontend Engineer, UX Researcher, SEO Specialist).

**Total Roles:** 27 across 8 departments

---

## S

### Sequential Workflow
Multi-step process involving multiple roles across departments, following real agency collaboration patterns.

**Example:** Discovery → Design → Development → Deployment → Growth

### Skill
A knowledge library (markdown file) that agents reference for better results. Contains patterns, best practices, and examples.

**Example:** `frontend-development/SKILL.md` (1,400 lines of React/Vue expertise)

**Total Skills:** 23,307 lines across 27 skills

---

## T

### Template
Reusable code or document templates provided by plugins (e.g., React component template, API endpoint template).

**Location:** `plugins/[department]/templates/`

### Tool
Functions that agents can use to interact with the system (Read, Write, Edit, Bash, etc.).

**Common Tools:**
- **Read:** Read files
- **Write:** Create files
- **Edit:** Modify files
- **Bash:** Execute shell commands
- **Grep:** Search files
- **Glob:** Find files by pattern

---

## U

### User Guide
Documentation for end users on installing, configuring, and using Puerto's agency team.

**Location:** `docs/user-guide/`

---

## V

### Validation
Automated checks ensuring plugin structure, metadata, and content quality. Puerto has 193 validation checks.

**Script:** `node scripts/validate-agency-consolidation.js`

---

## W

### Workflow
End-to-end process involving multiple roles and departments to complete a project phase (e.g., "Building a SaaS Product").

**Examples Available in:** EXAMPLES.md

---

## Acronyms & Abbreviations

| Term | Full Name | Definition |
|------|-----------|------------|
| **ADR** | Architecture Decision Record | Document recording technical decisions |
| **API** | Application Programming Interface | System interface for integration |
| **CPO** | Chief Product Officer | Product department leader |
| **CSO** | Chief Strategy Officer | Top leadership role |
| **MCP** | Model Context Protocol | Protocol for external tool integration |
| **RACI** | Responsible, Accountable, Consulted, Informed | Responsibility assignment framework |
| **SEO** | Search Engine Optimization | Website search visibility improvement |
| **UX** | User Experience | User-centered design practice |
| **WCAG** | Web Content Accessibility Guidelines | Accessibility standards |

---

## Common Patterns

### Department Naming Convention
Format: `[noun]@puerto`

**Examples:**
- `engineering@puerto`
- `design@puerto`
- `marketing@puerto`

### Agent Naming Convention
Format: `[department]/[role-name]`

**Examples:**
- `engineering/frontend-engineer`
- `design/ux-researcher`
- `marketing/seo-specialist`

### Skill Naming Convention
Format: `[domain]-[specialty]`

**Examples:**
- `frontend-development`
- `backend-architecture`
- `ux-research`

---

## Related Resources

- **[README.md](README.md)** - Overview and quick start
- **[TEAM-STRUCTURE.md](TEAM-STRUCTURE.md)** - Complete org chart
- **[ROLE-MATRIX.md](ROLE-MATRIX.md)** - RACI matrix
- **[QUICK-REFERENCE.md](QUICK-REFERENCE.md)** - Command reference
- **[FAQ](docs/user-guide/faq.md)** - Frequently asked questions

---

**Version:** 1.0.0
**Last Updated:** 2025-11-03
