<div align="center">
  <img src="docs/logo.png" alt="Puerto Logo" width="200"/>
</div>
<p align="center">
  Your AI-powered digital agency team for Claude Code
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="Version" />
  <img src="https://img.shields.io/badge/departments-8-green" alt="Departments" />
  <img src="https://img.shields.io/badge/roles-27-orange" alt="Roles" />
  <img src="https://img.shields.io/badge/skills-23,307_lines-purple" alt="Skills" />
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License" />
  <img src="https://img.shields.io/badge/status-production-brightgreen" alt="Status" />
</p>

<p align="center">
  <a href="#quick-start"><strong>Quick Start</strong></a> •
  <a href="TEAM-STRUCTURE.md"><strong>Team Structure</strong></a> •
  <a href="EXAMPLES.md"><strong>Usage Examples</strong></a> •
  <a href="ROLE-MATRIX.md"><strong>Role Matrix</strong></a> •
  <a href="docs/README.md"><strong>Documentation</strong></a>
</p>

<p align="center">
  <strong>⭐ Star us on GitHub if Puerto helps your workflow!</strong>
</p>

---

## What is Puerto?

**Puerto is a curated marketplace of specialized AI agents organized as a digital agency team.** Instead of 100+ scattered plugins, Puerto provides **8 functional departments with 27 specialized roles** that work together like a real agency.

### The Team

```
🔧 Engineering (7 roles)   🎨 Design (4 roles)      📢 Marketing (5 roles)
📊 Product (4 roles)        💼 Sales (3 roles)       ⚙️  Operations (3 roles)
🎯 Leadership (1 role)      🏗️  Infrastructure (7 plugins)
```

**Total: 27 specialized roles + essential infrastructure**

---

## Prerequisites

- **Claude Code:** v1.0.0 or higher
- **Operating System:** macOS 11+, Linux (Ubuntu 20.04+), or Windows 10+
- **Disk Space:** 500MB minimum (2GB recommended for all departments)
- **Internet:** Required for plugin downloads and updates

---

## Quick Start

### 1. Install Puerto Marketplace

```bash
/plugin marketplace add bandofai/puerto
```

### 2. Install Essential Infrastructure

```bash
# Core MCP servers + requirements management
/plugin install essentials@puerto
```

This installs:
- **Serena** - Semantic code navigation
- **Context7** - Up-to-date documentation
- **Sequential Thinking** - Structured problem-solving
- **Playwright** - Browser automation
- **Requirements Management** - `/brainstorm`, `/implement` commands

### 3. Install Department Teams

Install the departments you need:

```bash
# Full-stack development
/plugin install engineering@puerto

# UX and design
/plugin install design@puerto

# Marketing and growth
/plugin install marketing@puerto

# Product and analytics
/plugin install product@puerto

# Sales and customer success
/plugin install sales@puerto

# HR and operations
/plugin install operations@puerto

# Strategic planning
/plugin install leadership@puerto
```

### 4. Configure Auto-Routing (Optional)

Enable automatic agent invocation with CLAUDE.md:

```bash
/plugin install claude-md-master@puerto

# Then ask Claude:
"Create a CLAUDE.md for my project"
```

---

## The 8-Department Structure

### 🔧 Engineering Department

**7 specialized roles for full-stack development**

- **Engineering Lead** - Technical architecture and system design
- **Frontend Engineer** - React, Vue, UI/UX implementation
- **Backend Engineer** - APIs, databases, services
- **DevOps Engineer** - CI/CD, infrastructure, deployments
- **Mobile Engineer** - iOS, Android, React Native
- **Data Engineer** - Data pipelines, ML ops, analytics infrastructure
- **QA Engineer** - Testing, automation, quality assurance

**Install:**
```bash
/plugin install engineering@puerto
```

**Example usage:**
```
"Design the technical architecture for a SaaS application"
→ Uses: engineering/engineering-lead

"Build a React dashboard with real-time data updates"
→ Uses: engineering/frontend-engineer

"Set up CI/CD pipeline and deploy to AWS"
→ Uses: engineering/devops-engineer
```

**[View engineering workflows →](EXAMPLES.md#engineering-department)**

---

### 🎨 Design Department

**4 specialized roles for user experience**

- **Design Lead** - Creative direction and design strategy
- **UX Researcher** - User research, testing, insights
- **UX Writer** - Content strategy, microcopy, voice/tone
- **Accessibility Specialist** - WCAG compliance, inclusive design

**Install:**
```bash
/plugin install design@puerto
```

**Example usage:**
```
"Conduct user research to understand pain points"
→ Uses: design/ux-researcher

"Write microcopy for a checkout flow"
→ Uses: design/ux-writer

"Audit our application for WCAG 2.1 Level AA compliance"
→ Uses: design/accessibility-specialist
```

**[View design workflows →](EXAMPLES.md#design-department)**

---

### 📢 Marketing Department

**5 specialized roles for growth**

- **Marketing Director** - Strategy, campaigns, go-to-market
- **Content Strategist** - Content planning, creation, distribution
- **SEO Specialist** - Technical SEO, optimization, rankings
- **Social Media Manager** - Social strategy, community, engagement
- **Growth Marketer** - Experiments, conversion, optimization

**Install:**
```bash
/plugin install marketing@puerto
```

**Example usage:**
```
"Plan a go-to-market strategy for product launch"
→ Uses: marketing/marketing-director

"Create a content strategy to drive organic growth"
→ Uses: marketing/content-strategist

"Run growth experiments to improve conversion rate"
→ Uses: marketing/growth-marketer
```

**[View marketing workflows →](EXAMPLES.md#marketing-department)**

---

### 📊 Product Department

**4 specialized roles for product management**

- **Chief Product Officer** - Product vision, strategy, roadmap
- **Project Manager** - Planning, coordination, delivery
- **Business Analyst** - Requirements, stakeholder management
- **Data Analyst** - Metrics, dashboards, insights

**Install:**
```bash
/plugin install product@puerto
```

**Example usage:**
```
"Define product vision and 2-year roadmap"
→ Uses: product/chief-product-officer

"Manage a 3-month product development project"
→ Uses: product/project-manager

"Analyze user behavior and create insights dashboard"
→ Uses: product/data-analyst
```

**[View product workflows →](EXAMPLES.md#product-department)**

---

### 💼 Sales Department

**3 specialized roles for revenue**

- **Sales Director** - Sales process, pipeline, forecasting
- **Customer Success Manager** - Onboarding, retention, expansion
- **Partnership Manager** - Alliances, integrations, channels

**Install:**
```bash
/plugin install sales@puerto
```

**Example usage:**
```
"Build sales process and manage team to hit targets"
→ Uses: sales/sales-director

"Onboard new customers and ensure retention"
→ Uses: sales/customer-success-manager

"Identify and negotiate strategic partnerships"
→ Uses: sales/partnership-manager
```

**[View sales workflows →](EXAMPLES.md#sales-department)**

---

### ⚙️ Operations Department

**3 specialized roles for internal operations**

- **Operations Lead** - Process optimization, vendor management
- **HR Manager** - Recruitment, talent management, culture
- **Office Manager** - Procurement, facilities, administration

**Install:**
```bash
/plugin install operations@puerto
```

**Example usage:**
```
"Recruit for senior engineering role"
→ Uses: operations/hr-manager

"Optimize operations and improve efficiency"
→ Uses: operations/operations-lead

"Manage office operations and procurement"
→ Uses: operations/office-manager
```

**[View operations workflows →](EXAMPLES.md#operations-department)**

---

### 🎯 Leadership

**1 executive role for strategy**

- **Chief Strategy Officer** - Vision, strategic planning, executive reporting

**Install:**
```bash
/plugin install leadership@puerto
```

**Example usage:**
```
"Define 5-year company strategy and vision"
→ Uses: leadership/chief-strategy-officer
```

**[View leadership workflows →](EXAMPLES.md#leadership)**

---

## Infrastructure & Tools

### Essential Infrastructure

**Essentials** - Core MCP servers and requirements management
- Serena (semantic code navigation)
- Context7 (up-to-date docs)
- Sequential Thinking (structured reasoning)
- Playwright (browser automation)
- Requirements commands (`/brainstorm`, `/implement`)

```bash
/plugin install essentials@puerto
```

---

### Additional Tools

**Chrome DevTools** - Browser automation and debugging
```bash
/plugin install chrome-devtools@puerto
```

**Subagent Creator** - Build custom agents
```bash
/plugin install subagent-creator@puerto
```

**CLAUDE.md Master** - Auto-routing configuration
```bash
/plugin install claude-md-master@puerto
```

**Cloudflare** - Deploy to Cloudflare Pages
```bash
/plugin install cloudflare@puerto
```

**Figma** - Design-to-code generation
```bash
/plugin install figma@puerto
```

**Orchestrator** - Multi-agent workflow coordination
```bash
/plugin install orchestrator@puerto
```

---

## Complete Documentation

### Core Documentation

- **[Team Structure](TEAM-STRUCTURE.md)** - Org chart and department breakdown
- **[Role Matrix (RACI)](ROLE-MATRIX.md)** - Who does what across project phases
- **[Usage Examples](EXAMPLES.md)** - 6 end-to-end project workflows
- **[Testing Guide](TESTING.md)** - Validation and quality assurance

### Setup & Configuration

- **[Getting Started](docs/getting-started.md)** - 5-minute quickstart
- **[Configuring CLAUDE.md](docs/configuring-claude-md.md)** - Auto-routing setup
- **[Installation Guide](docs/installation.md)** - Detailed installation options

### For Developers

- **[Plugin Development](docs/plugin-development/quickstart.md)** - Create plugins
- **[Contributing Guide](CONTRIBUTING.md)** - Submit improvements
- **[Migration Guide](MIGRATION.md)** - Understanding the team structure

---

## Real-World Workflows

### Building a SaaS Product (End-to-End)

**Phase 1: Discovery** (2 weeks)
```
1. leadership/chief-strategy-officer - Define vision
2. design/ux-researcher - User research
3. product/business-analyst - Requirements
4. engineering/engineering-lead - Technical feasibility
```

**Phase 2: Design** (3 weeks)
```
5. design/design-lead - Information architecture
6. design/ux-researcher - Wireframes and testing
7. design/ux-writer - Content strategy
```

**Phase 3: Development** (6 weeks)
```
8. engineering/backend-engineer - Build APIs
9. engineering/frontend-engineer - Build UI
10. engineering/qa-engineer - Testing
```

**Phase 4: Deployment** (1 week)
```
11. engineering/devops-engineer - Deploy to production
12. marketing/marketing-director - Launch plan
```

**Phase 5: Growth** (Ongoing)
```
13. marketing/growth-marketer - Run experiments
14. product/data-analyst - Track metrics
```

**[View 5 more complete workflows →](EXAMPLES.md)**

---

## Why Puerto?

### Before: 100+ Scattered Plugins
❌ Hard to discover the right plugin
❌ No coordination between plugins
❌ Unclear which agent to use when
❌ Complex maintenance

### After: 8 Departments, 27 Roles
✅ **Clear organization** - Find the right role instantly
✅ **Real agency structure** - Like a 20-30 person digital agency
✅ **Comprehensive skills** - 23,307 lines of expertise (avg 860 lines per role)
✅ **Production-ready** - 193 validation checks passing

---

## Key Features

### 🎯 Department-Based Organization
8 functional departments matching real agency structure

### 👥 27 Specialized Roles
From engineering to marketing to operations

### 📚 Comprehensive Knowledge
23,307 lines of skills across 27 mega-skills

### 🔄 Sequential Workflows
Roles designed to work together across project phases

### ✅ Validated Structure
193 automated checks ensure quality

### 📖 Complete Documentation
Team structure, role matrix, usage examples, testing guide

---

## Quick Reference

### Installation Commands

```bash
# Add marketplace
/plugin marketplace add bandofai/puerto

# Core infrastructure
/plugin install essentials@puerto

# Install departments
/plugin install engineering@puerto
/plugin install design@puerto
/plugin install marketing@puerto
/plugin install product@puerto
/plugin install sales@puerto
/plugin install operations@puerto
/plugin install leadership@puerto

# Additional tools
/plugin install claude-md-master@puerto
/plugin install chrome-devtools@puerto
/plugin install subagent-creator@puerto
```

### Agent Invocation Pattern

```
[department]/[role-name]

Examples:
- engineering/frontend-engineer
- design/ux-researcher
- marketing/seo-specialist
- product/data-analyst
- sales/customer-success-manager
```

### Common Workflows

- **Building features** → Engineering → Design → QA → DevOps
- **Marketing campaigns** → Marketing Director → Content → SEO → Social → Growth
- **Product planning** → Product Officer → Business Analyst → Data Analyst
- **Strategic planning** → Chief Strategy Officer → Product → Engineering → Marketing

---

## Performance & Resources

### Installation Size
- **Base marketplace:** 10MB
- **Average department:** 50-100MB per department
- **All departments:** ~500MB total

### Runtime Impact
- **Memory overhead:** <50MB per installed department
- **Plugin loading:** <100ms per department
- **Agent invocation:** <500ms cold start, <50ms warm start

### Benchmarks
Tested on M1 MacBook Air, 8GB RAM:
- **Engineering department** (7 roles): 23ms avg invocation
- **Design department** (4 roles): 18ms avg invocation
- **Full agency** (27 roles): 31ms avg invocation (parallel loading)

---

## Statistics

| Metric | Value |
|--------|-------|
| Departments | 8 |
| Specialized Roles | 27 |
| Total Skills (lines) | 23,307 |
| Avg Skills per Role | 860 lines |
| Comprehensive Skills | 19 (500+ lines) |
| Validation Checks | 193 passing |
| Documentation Files | 11 core docs |

---

## Community & Support

- 💬 **[GitHub Discussions](https://github.com/bandofai/puerto/discussions)** - Ask questions, share ideas
- 🐛 **[Report Issues](https://github.com/bandofai/puerto/issues)** - Bug reports and feature requests
- 📖 **[Documentation](docs/README.md)** - Complete documentation
- 📚 **[Examples](EXAMPLES.md)** - Real-world workflows
- 📋 **[Quick Reference](QUICK-REFERENCE.md)** - Command cheat sheet
- ❓ **[FAQ](docs/user-guide/faq.md)** - Common questions
- 🔧 **[Troubleshooting](TROUBLESHOOTING.md)** - Solve common issues

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

<a href="https://github.com/bandofai/puerto/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=bandofai/puerto" alt="Contributors" />
</a>

---

## License

MIT License

---

**Welcome to Puerto - Your AI-powered digital agency team!** 🚀
