# Plugins by Feature

Use this catalog to find plugins based on the capabilities they include—commands, agents, skills, templates, and MCP servers. For the full alphabetical list, see [Complete Plugin List](complete-list.md).

---

## At a Glance

| Feature Mix | What You Get | Examples |
|-------------|--------------|----------|
| Agents + Skills + Templates | End-to-end automation with reusable knowledge and boilerplate | `frontend-developer`, `backend-architect`, `api-developer`, `project-manager`, `seo-specialist` |
| Agents + Skills | Specialist copilots with deep domain guidance | `budget-tracker`, `compliance-officer`, `customer-support`, `habit-tracker` |
| Agents Only | Lightweight assistants for focused tasks | `goal-tracker`, `technical-writer`, `tax-assistant` |
| Documentation Playbooks | Expert playbooks packaged as reference docs | `accessibility-specialist`, `mobile-developer`, `dashboard-designer` |
| MCP Servers | External tooling powered by marketplaces | `essentials`, `chrome-devtools`, `figma` |
| Command Workflows | Slash commands for orchestration | `essentials` (`/brainstorm`, `/implement`, `/req-*`) |

---

## Full-Stack Automation (Agents + Skills + Templates)

78 plugins ship the complete toolkit: opinionated agents, curated skills, and ready-to-use templates. Perfect for spinning up production-ready workflows.

**Development & Engineering**
- `frontend-developer` — Component scaffolding, accessibility validation, responsive styling.
- `backend-architect` — ADRs, API specs, database schema templates.
- `api-developer` — Endpoint design, auth flows, OpenAPI templates.
- `database-architect` — Schema design, migration templates, query optimisation.
- `devops-engineer` — CI/CD pipelines, infrastructure blueprints, monitoring runbooks.

**Data & Analytics**
- `data-scientist` — Experiment design, notebooks, model evaluation templates.
- `ml-engineer` — Model deployment pipelines, feature store patterns.
- `data-engineer` — ETL orchestration, data quality playbooks.
- `dashboard-designer` *(playbook companion)* — Use with analytics plugins for BI deliverables.

**Product & Delivery**
- `project-manager` — Project charters, status updates, risk registers.
- `product-manager` — Product requirement docs, roadmap templates.
- `release-manager` — Change logs, deployment checklists, rollback guides.
- `qa-automation` — Test plan builders, automation suites, bug triage checklists.

**Go-To-Market & Growth**
- `seo-specialist` — Keyword research agents, on-page audit templates.
- `content-writer` — Editorial calendars, multi-channel content templates.
- `email-marketer` — Campaign sequences, segmentation frameworks.
- `social-media-manager` — Content calendars, engagement playbooks.

**Operations & Finance**
- `accounts-receivable-agent` — Invoice workflows, dunning templates.
- `billing-specialist` — Revenue recognition, compliance documentation.
- `procurement-specialist` — Vendor scorecards, negotiation scripts.
- `supply-chain-analyst` — Inventory tracking, logistics dashboards.

**Health, Lifestyle & Personal Productivity**
- `habit-tracker` — Routine building agents, habit journal templates.
- `goal-tracker` *(agent companion)* — Use with templates to monitor SMART goals.
- `meal-planning-nutrition` — Meal plans, grocery templates, nutrition skills.
- `mental-health-journal` — Guided reflection prompts and tracking templates.

> Pair these plugins with the [Essentials](../getting-started.md#understand-what-you-installed) command set for maximum productivity.

---

## Specialist Automation (Agents + Skills)

33 plugins provide expert agents backed by skills, ideal when you don’t need templates but want guided workflows.

- `budget-tracker` — Personal finance insights with automated categorisation.
- `compliance-officer` — Regulatory monitoring, policy drafting, audit prep.
- `customer-support` — Support triage, response playbooks, escalation handling.
- `habit-formation-coach` — Behaviour change frameworks and accountability routines.
- `healthcare-compliance` — HIPAA/GxP compliance coaching.
- `hr-onboarder` / `hr-recruiter` / `hr-performance-manager` — HR process specialists.
- `language-learning` / `learning-plan-generator` — Personalised learning journeys.
- `local-seo-specialist` / `localization-specialist` — Location-aware optimisation.
- `sales-engineer` / `sales-proposal-writer` / `sales-pipeline-analyst` — Revenue team copilots.

Add your own templates in-project if you want to extend these flows further.

---

## Lightweight Agents Only

17 plugins ship focused agents without additional assets—ideal for quick wins or supplementing larger stacks.

- `goal-tracker` — Daily/weekly goal check-ins and accountability prompts.
- `technical-writer` — Documentation drafting and editing support.
- `tax-assistant` / `tax-compliance-specialist` — Filing prep and compliance reminders.
- `knowledge-base-manager` — Knowledge article maintenance and taxonomy updates.
- `training-developer` — Course development outlines and learner outcomes.
- `portfolio-tracker` — Investment monitoring and performance summaries.
- `meal-planning-nutrition` *(agent mode)* — Grocery planning and nutrition checks.

Use these as building blocks with your own skills/templates when you need a lean setup.

---

## Documentation Playbooks (Reference-Only)

22 plugins package expert guidance as Markdown playbooks—perfect for teams that want strategic direction without automation.

- `accessibility-specialist` — Comprehensive WCAG remediation handbook.
- `business-strategist` — Corporate strategy frameworks and analyses.
- `conversion-optimizer` — CRO teardown scripts and experimentation roadmaps.
- `digital-transformation` — Org change frameworks and readiness assessments.
- `emergency-response-coordinator` — Crisis response and incident communication.
- `innovation-consultant` — Ideation methodologies and venture scoring rubrics.
- `mobile-developer` — Mobile app delivery lifecycle best practices.
- `qa-manager` — Quality program governance and audit checklists.
- `patent-analyst` — Prior art search strategies and patent evaluation heuristics.

Leverage these documents as skills in your own projects or pair them with automation plugins for richer workflows.

---

## MCP-Powered Integrations

| Plugin | MCP Servers | Description |
|--------|-------------|-------------|
| `essentials` | Serena, Context7, Sequential Thinking, Playwright | Semantic code navigation, live docs search, reasoning toolkit, browser automation. Also ships commands (`/brainstorm`, `/implement`, `/req-*`). |
| `chrome-devtools` | Chrome DevTools MCP | Full browser automation, debugging, and performance profiling. |
| `figma` | Figma MCP (HTTP) | Convert Figma designs into code assets and component specs. |

Install these when you need external tooling. Check each README for prerequisites (Node/UV versions, Chrome, API keys).

---

## Command-First Workflows

Currently, the [Essentials](../getting-started.md#understand-what-you-installed) plugin leads in command coverage:

- `/brainstorm <name>` — Guided requirement discovery with automatic documentation.
- `/implement <name>` — Step-by-step implementation orchestration.
- `/req-*` commands — Requirement management (list, update, status, tests).

Expect more command-focused plugins in future updates—follow the [Contributing Guide](../contributing/index.md) if you want to build your own.

---

## Next Steps

- Browse the [Complete Plugin List](complete-list.md) for an alphabetised index.
- Narrow by audience using [Plugins by Category](by-category.md).
- New here? Start with [Essential Installations](featured.md).
