# Quick Reference

**Puerto Digital Agency Team - Essential Commands & Patterns**

---

## Installation

### Add Marketplace
```bash
/plugin marketplace add bandofai/puerto
```

### Install Departments
```bash
# Essential infrastructure (install first)
/plugin install essentials@puerto

# Department plugins
/plugin install engineering@puerto
/plugin install design@puerto
/plugin install marketing@puerto
/plugin install product@puerto
/plugin install sales@puerto
/plugin install operations@puerto
/plugin install leadership@puerto
```

### Update Plugins
```bash
/plugin update @puerto              # Update all Puerto plugins
/plugin update engineering@puerto  # Update specific department
```

### Uninstall
```bash
/plugin uninstall engineering@puerto  # Remove department
/plugin uninstall @puerto             # Remove all Puerto plugins
```

---

## Department Overview

| Department | Roles | When to Use |
|-----------|-------|-------------|
| **🔧 Engineering** | 7 | Technical work, coding, infrastructure |
| **🎨 Design** | 4 | UX research, design, accessibility |
| **📢 Marketing** | 5 | Content, SEO, social, growth campaigns |
| **📊 Product** | 4 | Product strategy, project management, analytics |
| **💼 Sales** | 3 | Revenue, customer success, partnerships |
| **⚙️ Operations** | 3 | HR, procurement, office management |
| **🎯 Leadership** | 1 | Strategic planning, executive reporting |
| **🏗️ Infrastructure** | 7 | Essential tools, MCP servers |

---

## Agent Invocation

### Pattern
```
[department]/[role-name]
```

### Examples
```
engineering/frontend-engineer
design/ux-researcher
marketing/seo-specialist
product/data-analyst
sales/customer-success-manager
operations/hr-manager
leadership/chief-strategy-officer
```

---

## Engineering Department

**7 Roles:**
```
engineering/engineering-lead          # Architecture, technical strategy
engineering/frontend-engineer         # React, Vue, UI/UX
engineering/backend-engineer          # APIs, databases, services
engineering/devops-engineer           # CI/CD, infrastructure, deployments
engineering/mobile-engineer           # iOS, Android, React Native
engineering/data-engineer             # Data pipelines, ML ops
engineering/qa-engineer               # Testing, quality assurance
```

**Common Use Cases:**
```
"Design the technical architecture for a SaaS app"
→ engineering/engineering-lead

"Build a React dashboard with real-time updates"
→ engineering/frontend-engineer

"Create REST API with authentication"
→ engineering/backend-engineer

"Set up CI/CD pipeline and deploy to AWS"
→ engineering/devops-engineer
```

---

## Design Department

**4 Roles:**
```
design/design-lead                    # Creative direction, design strategy
design/ux-researcher                  # User research, testing, insights
design/ux-writer                      # Content strategy, microcopy
design/accessibility-specialist       # WCAG compliance, inclusive design
```

**Common Use Cases:**
```
"Conduct user research to understand pain points"
→ design/ux-researcher

"Write microcopy for checkout flow"
→ design/ux-writer

"Audit application for WCAG 2.1 Level AA compliance"
→ design/accessibility-specialist
```

---

## Marketing Department

**5 Roles:**
```
marketing/marketing-director          # Strategy, campaigns, go-to-market
marketing/content-strategist          # Content planning, writing
marketing/seo-specialist              # Technical SEO, optimization
marketing/social-media-manager        # Social strategy, community
marketing/growth-marketer             # Experiments, conversion, retention
```

**Common Use Cases:**
```
"Plan go-to-market strategy for product launch"
→ marketing/marketing-director

"Create content strategy to drive organic growth"
→ marketing/content-strategist

"Optimize website for search engines"
→ marketing/seo-specialist
```

---

## Product Department

**4 Roles:**
```
product/chief-product-officer         # Product vision, strategy, roadmap
product/project-manager               # Planning, coordination, delivery
product/business-analyst              # Requirements, stakeholder management
product/data-analyst                  # Metrics, dashboards, insights
```

**Common Use Cases:**
```
"Define product vision and 2-year roadmap"
→ product/chief-product-officer

"Manage a 3-month product development project"
→ product/project-manager

"Analyze user behavior and create insights dashboard"
→ product/data-analyst
```

---

## Sales Department

**3 Roles:**
```
sales/sales-director                  # Sales process, pipeline, forecasting
sales/customer-success-manager        # Onboarding, retention, expansion
sales/partnership-manager             # Alliances, integrations, channels
```

**Common Use Cases:**
```
"Build sales process and manage team to hit targets"
→ sales/sales-director

"Onboard new customers and ensure retention"
→ sales/customer-success-manager
```

---

## Operations Department

**3 Roles:**
```
operations/operations-lead            # Process optimization, vendor management
operations/hr-manager                 # Recruitment, talent, culture
operations/office-manager             # Procurement, facilities, administration
```

**Common Use Cases:**
```
"Recruit for senior engineering role"
→ operations/hr-manager

"Optimize operations and improve efficiency"
→ operations/operations-lead
```

---

## Leadership

**1 Role:**
```
leadership/chief-strategy-officer     # Vision, strategic planning, executive reporting
```

**Common Use Cases:**
```
"Define 5-year company strategy and vision"
→ leadership/chief-strategy-officer
```

---

## Essential Commands

*From essentials@puerto plugin:*

### /brainstorm
```bash
/brainstorm feature-name
```
Start interactive Q&A to define new feature requirements.

### /implement
```bash
/implement requirement-id
```
Execute implementation based on defined requirement.

---

## Common Workflows

### 1. Building a Feature
```
1. product/chief-product-officer    # Define requirements
2. design/ux-researcher             # User research
3. design/design-lead               # Design
4. engineering/engineering-lead     # Architecture
5. engineering/frontend-engineer    # Build UI
6. engineering/backend-engineer     # Build API
7. engineering/qa-engineer          # Test
8. engineering/devops-engineer      # Deploy
```

### 2. Marketing Campaign
```
1. marketing/marketing-director     # Strategy
2. marketing/content-strategist     # Content plan
3. design/ux-writer                 # Copy
4. marketing/seo-specialist         # Optimization
5. marketing/social-media-manager   # Distribution
6. marketing/growth-marketer        # Experiments
7. product/data-analyst             # Analytics
```

### 3. Product Launch
```
1. leadership/chief-strategy-officer  # Vision
2. product/chief-product-officer      # Roadmap
3. engineering/engineering-lead       # Build
4. marketing/marketing-director       # Launch plan
5. sales/sales-director               # Sales strategy
6. operations/operations-lead         # Operations ready
```

---

## Plugin Management

### List Installed
```bash
/plugin list @puerto
```

### Get Info
```bash
/plugin info engineering@puerto
```

### Refresh Marketplace
```bash
/plugin marketplace refresh
```

### Update All
```bash
/plugin update @puerto
```

---

## Project Configuration

### Create CLAUDE.md

```bash
/plugin install claude-md-master@puerto

# Then ask Claude:
"Create a CLAUDE.md for my project"
```

### Sample CLAUDE.md Routing

```markdown
## Task Routing

- Technical architecture → engineering/engineering-lead
- React/Vue development → engineering/frontend-engineer
- API development → engineering/backend-engineer
- CI/CD and deployment → engineering/devops-engineer
- User research → design/ux-researcher
- Marketing campaigns → marketing/marketing-director
- SEO optimization → marketing/seo-specialist
- Product strategy → product/chief-product-officer
- Data analysis → product/data-analyst
```

---

## Troubleshooting

### Plugin Not Found
```bash
/plugin marketplace refresh
/plugin install engineering@puerto
```

### Agent Not Responding
```
Check invocation pattern: [department]/[role-name]
✅ engineering/frontend-engineer
❌ frontend-engineer
```

### Command Not Working
```bash
# Ensure essentials is installed
/plugin install essentials@puerto

# Restart Claude Code
```

---

## File Locations

### Plugins Directory
```
~/.claude/plugins/puerto/
```

### Logs
```
~/.claude/logs/main.log
~/.claude/logs/error.log
```

### Cache
```
~/.claude/cache/puerto/
```

---

## Documentation

- **[README.md](README.md)** - Overview and quick start
- **[TEAM-STRUCTURE.md](TEAM-STRUCTURE.md)** - Org chart and department breakdown
- **[ROLE-MATRIX.md](ROLE-MATRIX.md)** - RACI matrix for collaboration
- **[EXAMPLES.md](EXAMPLES.md)** - 6 end-to-end workflows
- **[TESTING.md](TESTING.md)** - Testing framework
- **[MIGRATION.md](MIGRATION.md)** - Migration from old structure
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues and solutions
- **[GLOSSARY.md](GLOSSARY.md)** - Terms and definitions

---

## Support

- **GitHub Issues:** [github.com/bandofai/puerto/issues](https://github.com/bandofai/puerto/issues)
- **Documentation:** [docs/README.md](docs/README.md)
- **FAQ:** [docs/user-guide/faq.md](docs/user-guide/faq.md)

---

**Version:** 1.0.0
**Last Updated:** 2025-11-03
