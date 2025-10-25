<div align="center">
  <img src="docs/logo.png" alt="Puerto Logo" width="200"/>
</div>
<p align="center">
  A curated marketplace of Claude Code plugins.
</p>

<p align="center">
  <a href="docs/getting-started.md"><strong>Get Started</strong></a> •
  <a href="docs/README.md"><strong>Documentation</strong></a> •
  <a href="docs/plugins/by-category.md"><strong>Browse Plugins</strong></a> •
  <a href="CONTRIBUTING.md"><strong>Contribute</strong></a>
</p>

## What is Claude Code Plugin?

Claude Code plugins extend Claude's capabilities with custom commands, agents, skills, hooks, and MCP servers. They allow you to add specialized functionality to your Claude Code environment, from semantic code navigation to external tool integrations, making your development workflow more powerful and tailored to your needs. Learn more in the [official documentation](https://docs.claude.com/en/docs/claude-code/plugins).

## 📚 Documentation

Puerto now has **comprehensive documentation** to help you get started:

- **[Getting Started Guide](docs/getting-started.md)** - Install Puerto and your first plugin in 5 minutes
- **[Complete Documentation](docs/README.md)** - Full documentation hub
- **[Plugin Catalog](docs/plugins/by-category.md)** - Browse 140+ plugins by category
- **[Plugin Development](docs/plugin-development/quickstart.md)** - Create your own plugins
- **[Contributing Guide](CONTRIBUTING.md)** - Submit plugins and improvements

## Installation

Add Puerto marketplace:

```bash
/plugin marketplace add bandofai/puerto
```

Install a plugin:

```bash
/plugin install essentials@puerto
```

This makes the plugin available across all your projects.

Learn more in the [Getting Started Guide](docs/getting-started.md) and [Installation Documentation](docs/installation.md).

## Available Plugins

### Essentials

Essential MCP servers and requirements management commands for enhanced Claude Code development workflow.

#### MCP Servers

- **Serena** - Semantic code navigation with LSP-powered symbol search and editing
- **Context7** - Up-to-date documentation and code examples from current sources
- **Sequential Thinking** - Structured step-by-step problem-solving and reasoning
- **Playwright** - Headless browser automation with visual screenshot analysis and PDF generation

#### Commands

**Core Workflow:**
- `/brainstorm <name>` - Create requirement through interactive Q&A
- `/implement <name>` - Implement a requirement systematically
- `/continue [name]` - Resume interrupted implementation

**Management:**
- `/req-list` - Show all requirements with status
- `/req-update <name>` - Modify existing requirement
- `/req-tests <name>` - Generate test scenarios
- `/req-status [name]` - Check implementation progress

**Global installation:**
```bash
/plugin install essentials@puerto
```

**Prerequisites:**
- `uv` package manager ([install guide](https://docs.astral.sh/uv/getting-started/installation/))
- Node.js >= v18.0.0

After installing, restart Claude Code to activate the MCP servers.

---

### Chrome DevTools

Control and inspect Chrome browsers with full DevTools automation, debugging, and performance analysis.

#### MCP Servers

- **Chrome DevTools MCP** - 26+ tools for browser automation, input control, navigation, performance analysis, network monitoring, and debugging

**Global installation:**
```bash
/plugin install chrome-devtools@puerto
```

**Prerequisites:**
- Node.js >= v20.19
- Chrome browser (stable or newer)

After installing, restart Claude Code to activate the MCP server.

---

### Subagent Creator

Expert subagent architect with comprehensive skill library for creating production-ready, skill-aware Claude Code subagents.

#### Subagent

- **ultimate-subagent-creator** - Master architect for designing exceptional subagents with battle-tested patterns from 500+ deployments

#### Skills

- **subagent-creation** - Comprehensive patterns library for agent architecture, tool selection, model choice, and workflow integration

**Global installation:**
```bash
/plugin install subagent-creator@puerto
```

**Features:**
- Automatic skill integration for document creators
- Security-first design with least privilege
- Pattern recognition for different agent types
- Quality validation checklists
- Workflow coordination strategies

After installing, restart Claude Code to activate the subagent and skill.

---

### Figma

Generate code from Figma designs, extract components, variables, and maintain design-code consistency.

#### MCP Servers

- **Figma MCP** - Remote HTTP server for design-to-code generation, component extraction, and design context retrieval

**Global installation:**
```bash
/plugin install figma@puerto
```

**Prerequisites:**
- Dev or Full seat on Professional, Organization, or Enterprise Figma plan
- OAuth authentication (setup via `/mcp` command after installation)

**Authentication:** After installation, type `/mcp`, select **figma**, and choose **Authenticate**.

After installing, restart Claude Code to activate the MCP server.

---

## Plugin Squads

Pre-configured teams of related plugins designed to work together. Install entire squads to quickly set up specialized workflows.

---

### Web Development Squad

Full-stack web development team for building modern web applications

**Team Members (10 plugins):**
- Frontend Developer
- Backend Architect
- Api Developer
- Devops Engineer
- Site Reliability Engineer
- Database Architect
- Ux Researcher
- Ux Writer
- Accessibility Specialist
- Web Performance Auditor

**Global installation** (install all 10 plugins):
```bash
/plugin install frontend-developer@puerto
/plugin install backend-architect@puerto
/plugin install api-developer@puerto
/plugin install devops-engineer@puerto
/plugin install site-reliability-engineer@puerto
/plugin install database-architect@puerto
/plugin install ux-researcher@puerto
/plugin install ux-writer@puerto
/plugin install accessibility-specialist@puerto
/plugin install web-performance-auditor@puerto
```

---

### Mobile & App Squad

Mobile application development and optimization team

**Team Members (5 plugins):**
- Mobile Developer
- App Store Optimizer
- Ux Researcher
- Ux Writer
- Qa Automation

**Global installation** (install all 5 plugins):
```bash
/plugin install mobile-developer@puerto
/plugin install app-store-optimizer@puerto
/plugin install ux-researcher@puerto
/plugin install ux-writer@puerto
/plugin install qa-automation@puerto
```

---

### Data & Analytics Squad

Data engineering, analysis, and machine learning team

**Team Members (6 plugins):**
- Data Engineer
- Data Analyst
- Data Scientist
- Ml Engineer
- Quant Analyst
- Dashboard Designer

**Global installation** (install all 6 plugins):
```bash
/plugin install data-engineer@puerto
/plugin install data-analyst@puerto
/plugin install data-scientist@puerto
/plugin install ml-engineer@puerto
/plugin install quant-analyst@puerto
/plugin install dashboard-designer@puerto
```

---

### Marketing & Growth Squad

Digital marketing, growth hacking, and customer acquisition team

**Team Members (11 plugins):**
- Growth Hacker
- Seo Specialist
- Sem Specialist
- Local Seo Specialist
- Social Media Manager
- Email Marketer
- Content Writer
- Copywriter
- Brand Strategist
- Conversion Optimizer
- Affiliate Manager

**Global installation** (install all 11 plugins):
```bash
/plugin install growth-hacker@puerto
/plugin install seo-specialist@puerto
/plugin install sem-specialist@puerto
/plugin install local-seo-specialist@puerto
/plugin install social-media-manager@puerto
/plugin install email-marketer@puerto
/plugin install content-writer@puerto
/plugin install copywriter@puerto
/plugin install brand-strategist@puerto
/plugin install conversion-optimizer@puerto
/plugin install affiliate-manager@puerto
```

---

### E-commerce Squad

Complete e-commerce operations and optimization team

**Team Members (7 plugins):**
- Ecommerce Specialist
- Product Manager
- Product Analyst
- Shopping List Optimizer
- Payment Integration Specialist
- Fraud Analyst
- Inventory Management

**Global installation** (install all 7 plugins):
```bash
/plugin install ecommerce-specialist@puerto
/plugin install product-manager@puerto
/plugin install product-analyst@puerto
/plugin install shopping-list-optimizer@puerto
/plugin install payment-integration-specialist@puerto
/plugin install fraud-analyst@puerto
/plugin install inventory-management@puerto
```

---

### Finance & Accounting Squad

Financial management, accounting, and compliance team

**Team Members (11 plugins):**
- Financial Analyst
- Budget Analyst
- Accounts Payable Agent
- Accounts Receivable Agent
- Billing Specialist
- Expense Manager
- Tax Assistant
- Tax Compliance
- Tax Compliance Specialist
- Financial Compliance
- Cost Optimizer

**Global installation** (install all 11 plugins):
```bash
/plugin install financial-analyst@puerto
/plugin install budget-analyst@puerto
/plugin install accounts-payable-agent@puerto
/plugin install accounts-receivable-agent@puerto
/plugin install billing-specialist@puerto
/plugin install expense-manager@puerto
/plugin install tax-assistant@puerto
/plugin install tax-compliance@puerto
/plugin install tax-compliance-specialist@puerto
/plugin install financial-compliance@puerto
/plugin install cost-optimizer@puerto
```

---

### Business Operations Squad

Core business operations and process management team

**Team Members (9 plugins):**
- Business Analyst
- Business Strategist
- Project Manager
- Process Optimizer
- Procurement Specialist
- Supply Chain Analyst
- Office Administrator
- Compliance Officer
- Risk Analyst

**Global installation** (install all 9 plugins):
```bash
/plugin install business-analyst@puerto
/plugin install business-strategist@puerto
/plugin install project-manager@puerto
/plugin install process-optimizer@puerto
/plugin install procurement-specialist@puerto
/plugin install supply-chain-analyst@puerto
/plugin install office-administrator@puerto
/plugin install compliance-officer@puerto
/plugin install risk-analyst@puerto
```

---

### Sales & Customer Success Squad

Sales enablement and customer relationship team

**Team Members (8 plugins):**
- Sales Engineer
- Sales Lead Qualifier
- Sales Proposal Writer
- Sales Pipeline Analyst
- Customer Success
- Customer Support
- Technical Support
- Complaint Warranty Manager

**Global installation** (install all 8 plugins):
```bash
/plugin install sales-engineer@puerto
/plugin install sales-lead-qualifier@puerto
/plugin install sales-proposal-writer@puerto
/plugin install sales-pipeline-analyst@puerto
/plugin install customer-success@puerto
/plugin install customer-support@puerto
/plugin install technical-support@puerto
/plugin install complaint-warranty-manager@puerto
```

---

### HR & People Operations Squad

Human resources and people management team

**Team Members (5 plugins):**
- Hr Recruiter
- Hr Onboarder
- Hr Performance Manager
- Hr Policies Expert
- Training Developer

**Global installation** (install all 5 plugins):
```bash
/plugin install hr-recruiter@puerto
/plugin install hr-onboarder@puerto
/plugin install hr-performance-manager@puerto
/plugin install hr-policies-expert@puerto
/plugin install training-developer@puerto
```

---

### Product Development Squad

Product strategy, development, and quality assurance team

**Team Members (6 plugins):**
- Product Manager
- Product Analyst
- Qa Manager
- Qa Automation
- Release Manager
- Hotfix Developer

**Global installation** (install all 6 plugins):
```bash
/plugin install product-manager@puerto
/plugin install product-analyst@puerto
/plugin install qa-manager@puerto
/plugin install qa-automation@puerto
/plugin install release-manager@puerto
/plugin install hotfix-developer@puerto
```

---

### Content & Media Squad

Content creation, production, and publishing team

**Team Members (8 plugins):**
- Content Writer
- Copywriter
- Technical Writer
- Medical Writer
- Video Producer
- Podcast Producer
- Translator
- Localization Specialist

**Global installation** (install all 8 plugins):
```bash
/plugin install content-writer@puerto
/plugin install copywriter@puerto
/plugin install technical-writer@puerto
/plugin install medical-writer@puerto
/plugin install video-producer@puerto
/plugin install podcast-producer@puerto
/plugin install translator@puerto
/plugin install localization-specialist@puerto
```

---

### Research & Intelligence Squad

Research, analysis, and competitive intelligence team

**Team Members (6 plugins):**
- Academic Researcher
- Market Researcher
- Competitive Intelligence Analyst
- Research Brief Generator
- Patent Analyst
- Ip Specialist

**Global installation** (install all 6 plugins):
```bash
/plugin install academic-researcher@puerto
/plugin install market-researcher@puerto
/plugin install competitive-intelligence-analyst@puerto
/plugin install research-brief-generator@puerto
/plugin install patent-analyst@puerto
/plugin install ip-specialist@puerto
```

---

### Healthcare & Wellness Squad

Healthcare management and wellness tracking team

**Team Members (8 plugins):**
- Medical Appointment Tracker
- Fitness Tracking Logger
- Mental Health Journal
- Sleep Pattern Analyzer
- Medical Writer
- Clinical Research Coordinator
- Healthcare Compliance
- Insurance Underwriter

**Global installation** (install all 8 plugins):
```bash
/plugin install medical-appointment-tracker@puerto
/plugin install fitness-tracking-logger@puerto
/plugin install mental-health-journal@puerto
/plugin install sleep-pattern-analyzer@puerto
/plugin install medical-writer@puerto
/plugin install clinical-research-coordinator@puerto
/plugin install healthcare-compliance@puerto
/plugin install insurance-underwriter@puerto
```

---

### Personal Productivity Squad

Personal organization, planning, and habit management team

**Team Members (8 plugins):**
- Goal Tracker
- Habit Tracker
- Habit Formation Coach
- Smart Goal Assistant
- Calendar Optimization Engine
- Document Organizer
- Receipt Processor
- Password Security Auditor

**Global installation** (install all 8 plugins):
```bash
/plugin install goal-tracker@puerto
/plugin install habit-tracker@puerto
/plugin install habit-formation-coach@puerto
/plugin install smart-goal-assistant@puerto
/plugin install calendar-optimization-engine@puerto
/plugin install document-organizer@puerto
/plugin install receipt-processor@puerto
/plugin install password-security-auditor@puerto
```

---

### Home & Life Management Squad

Home management, planning, and life administration team

**Team Members (10 plugins):**
- Home Maintenance Tracker
- Home Inventory System
- Chore Scheduler
- Meal Planning Nutrition
- Parenting Task Manager
- Pet Care Manager
- Volunteer Time Tracker
- Event Planning Orchestrator
- Travel Planning Assistant
- Moving Coordinator

**Global installation** (install all 10 plugins):
```bash
/plugin install home-maintenance-tracker@puerto
/plugin install home-inventory-system@puerto
/plugin install chore-scheduler@puerto
/plugin install meal-planning-nutrition@puerto
/plugin install parenting-task-manager@puerto
/plugin install pet-care-manager@puerto
/plugin install volunteer-time-tracker@puerto
/plugin install event-planning-orchestrator@puerto
/plugin install travel-planning-assistant@puerto
/plugin install moving-coordinator@puerto
```

---

### Financial Planning Squad

Personal finance, investment, and insurance management team

**Team Members (8 plugins):**
- Budget Tracker
- Expense Manager
- Portfolio Tracker
- Mortgage Specialist
- Insurance Policy Manager
- Bill Reminder
- Bill Optimization Analyzer
- Subscription Management Hub

**Global installation** (install all 8 plugins):
```bash
/plugin install budget-tracker@puerto
/plugin install expense-manager@puerto
/plugin install portfolio-tracker@puerto
/plugin install mortgage-specialist@puerto
/plugin install insurance-policy-manager@puerto
/plugin install bill-reminder@puerto
/plugin install bill-optimization-analyzer@puerto
/plugin install subscription-management-hub@puerto
```

---

### All Other Plugins

Browse our complete collection of specialized agents:

**[Academic Researcher](plugins/academic-researcher)** - Academic research support specialist for literature review, methodology design, and citation mana...  

**Global installation:**
```bash
/plugin install academic-researcher@puerto
```

---

**[Accessibility Specialist](plugins/accessibility-specialist)** - Digital accessibility specialist for WCAG compliance, accessibility audits, remediation recommend...  

**Global installation:**
```bash
/plugin install accessibility-specialist@puerto
```

---

**[Accounts Payable Agent](plugins/accounts-payable-agent)** - Professional accounts payable automation for invoice processing, approval routing, payment schedu...  

**Global installation:**
```bash
/plugin install accounts-payable-agent@puerto
```

---

**[Accounts Receivable Agent](plugins/accounts-receivable-agent)** - Professional accounts receivable management with invoice generation, payment tracking, collection...  

**Global installation:**
```bash
/plugin install accounts-receivable-agent@puerto
```

---

**[Affiliate Manager](plugins/affiliate-manager)** - Affiliate program specialist for program design, affiliate recruitment, commission management, pe...  

**Global installation:**
```bash
/plugin install affiliate-manager@puerto
```

---

**[Api Developer](plugins/api-developer)** - API design and development specialist for REST/GraphQL APIs  

**Global installation:**
```bash
/plugin install api-developer@puerto
```

---

**[App Store Optimizer](plugins/app-store-optimizer)** - ASO (App Store Optimization) specialist for keyword research, app title/description optimization,...  

**Global installation:**
```bash
/plugin install app-store-optimizer@puerto
```

---

**[Backend Architect](plugins/backend-architect)** - Comprehensive backend architecture design with ADRs, API specifications, and database schemas  

**Global installation:**
```bash
/plugin install backend-architect@puerto
```

---

**[Backup Automation Manager](plugins/backup-automation-manager)** - Automated backup scheduling, verification, storage monitoring, and disaster recovery planning wit...  

**Global installation:**
```bash
/plugin install backup-automation-manager@puerto
```

---

**[Bill Optimization Analyzer](plugins/bill-optimization-analyzer)** - Utility and service bill optimization with plan analysis, provider comparison, savings calculatio...  

**Global installation:**
```bash
/plugin install bill-optimization-analyzer@puerto
```

---

**[Bill Reminder](plugins/bill-reminder)** - Bill management assistant with proactive payment reminders  

**Global installation:**
```bash
/plugin install bill-reminder@puerto
```

---

**[Billing Specialist](plugins/billing-specialist)** - Comprehensive billing and invoicing automation with SOX compliance, ASC 606 revenue recognition, ...  

**Global installation:**
```bash
/plugin install billing-specialist@puerto
```

---

**[Book Reading Tracker](plugins/book-reading-tracker)** - Reading progress and book note management specialist  

**Global installation:**
```bash
/plugin install book-reading-tracker@puerto
```

---

**[Book Tracker](plugins/book-tracker)** - A comprehensive reading management system for Claude Code that helps you track books, monitor pro...  

**Global installation:**
```bash
/plugin install book-tracker@puerto
```

---

**[Brand Strategist](plugins/brand-strategist)** - Brand strategy and positioning specialist  

**Global installation:**
```bash
/plugin install brand-strategist@puerto
```

---

**[Budget Analyst](plugins/budget-analyst)** - Budget monitoring and planning specialist for variance analysis, spend tracking, forecasting, and...  

**Global installation:**
```bash
/plugin install budget-analyst@puerto
```

---

**[Budget Tracker](plugins/budget-tracker)** - Version: 1.0.0  

**Global installation:**
```bash
/plugin install budget-tracker@puerto
```

---

**[Business Analyst](plugins/business-analyst)** - Business process and requirements analysis specialist  

**Global installation:**
```bash
/plugin install business-analyst@puerto
```

---

**[Business Strategist](plugins/business-strategist)** - Corporate strategy development specialist for strategic planning, growth strategies, market entry...  

**Global installation:**
```bash
/plugin install business-strategist@puerto
```

---

**[Calendar Optimization Engine](plugins/calendar-optimization-engine)** - Intelligent calendar management with conflict detection, meeting efficiency analysis, and time-bl...  

**Global installation:**
```bash
/plugin install calendar-optimization-engine@puerto
```

---

**[Carbon Footprint Tracker](plugins/carbon-footprint-tracker)** - Personal emissions tracking and reduction specialist with carbon calculation, reduction recommend...  

**Global installation:**
```bash
/plugin install carbon-footprint-tracker@puerto
```

---

**[Career Development Planner](plugins/career-development-planner)** - Professional career development specialist providing skill gap analysis, networking management, j...  

**Global installation:**
```bash
/plugin install career-development-planner@puerto
```

---

**[Chore Scheduler](plugins/chore-scheduler)** - Household chore coordination and task distribution manager with fair rotation, completion trackin...  

**Global installation:**
```bash
/plugin install chore-scheduler@puerto
```

---

**[Clinical Research Coordinator](plugins/clinical-research-coordinator)** - Clinical trial coordination specialist for study design, patient recruitment, and regulatory comp...  

**Global installation:**
```bash
/plugin install clinical-research-coordinator@puerto
```

---

**[Cloud Architect](plugins/cloud-architect)** - Cloud infrastructure design specialist for AWS/Azure/GCP with cost optimization and migration pla...  

**Global installation:**
```bash
/plugin install cloud-architect@puerto
```

---

**[Competitive Intelligence Analyst](plugins/competitive-intelligence-analyst)** - Competitor monitoring and analysis specialist for tracking market intelligence, feature compariso...  

**Global installation:**
```bash
/plugin install competitive-intelligence-analyst@puerto
```

---

**[Complaint Warranty Manager](plugins/complaint-warranty-manager)** - Customer service interaction and warranty claim tracking specialist for managing complaints, esca...  

**Global installation:**
```bash
/plugin install complaint-warranty-manager@puerto
```

---

**[Compliance Officer](plugins/compliance-officer)** - Regulatory compliance monitoring specialist for GDPR, SOC2, HIPAA, audit preparation, and policy ...  

**Global installation:**
```bash
/plugin install compliance-officer@puerto
```

---

**[Content Creation Pipeline](plugins/content-creation-pipeline)** - Complete content planning and publishing workflow specialist with idea capture, calendar planning...  

**Global installation:**
```bash
/plugin install content-creation-pipeline@puerto
```

---

**[Content Writer](plugins/content-writer)** - Professional content creation for blogs, SEO, marketing copy, and email campaigns  

**Global installation:**
```bash
/plugin install content-writer@puerto
```

---

**[Conversion Optimizer](plugins/conversion-optimizer)** - CRO (Conversion Rate Optimization) specialist for funnel analysis, A/B testing, user journey mapp...  

**Global installation:**
```bash
/plugin install conversion-optimizer@puerto
```

---

**[Copywriter](plugins/copywriter)** - Advertising and marketing copy specialist  

**Global installation:**
```bash
/plugin install copywriter@puerto
```

---

**[Cost Optimizer](plugins/cost-optimizer)** - Version: 1.0.0  

**Global installation:**
```bash
/plugin install cost-optimizer@puerto
```

---

**[Crisis Communications](plugins/crisis-communications)** - Crisis communication management specialist for crisis response planning, press releases, stakehol...  

**Global installation:**
```bash
/plugin install crisis-communications@puerto
```

---

**[Cross Cultural Consultant](plugins/cross-cultural-consultant)** - Cross-cultural communication specialist for cultural assessment, communication guidelines, and te...  

**Global installation:**
```bash
/plugin install cross-cultural-consultant@puerto
```

---

**[Curriculum Developer](plugins/curriculum-developer)** - Professional educational curriculum design with instructional frameworks, Bloom's taxonomy, and e...  

**Global installation:**
```bash
/plugin install curriculum-developer@puerto
```

---

**[Customer Success](plugins/customer-success)** - Customer relationship and retention specialist focused on onboarding, adoption tracking, health m...  

**Global installation:**
```bash
/plugin install customer-success@puerto
```

---

**[Customer Support](plugins/customer-support)** - First-line customer support with query classification, issue resolution, and escalation management  

**Global installation:**
```bash
/plugin install customer-support@puerto
```

---

**[Dashboard Designer](plugins/dashboard-designer)** - Dashboard and reporting design specialist for data visualization, KPI selection and tracking, vis...  

**Global installation:**
```bash
/plugin install dashboard-designer@puerto
```

---

**[Data Analyst](plugins/data-analyst)** - Business intelligence and reporting specialist  

**Global installation:**
```bash
/plugin install data-analyst@puerto
```

---

**[Data Engineer](plugins/data-engineer)** - Data pipeline and ETL specialist with data warehouse design capabilities  

**Global installation:**
```bash
/plugin install data-engineer@puerto
```

---

**[Data Scientist](plugins/data-scientist)** - Advanced analytics and statistical modeling specialist for rigorous data science workflows  

**Global installation:**
```bash
/plugin install data-scientist@puerto
```

---

**[Database Architect](plugins/database-architect)** - Database design, optimization, and migration specialist  

**Global installation:**
```bash
/plugin install database-architect@puerto
```

---

**[Devops Engineer](plugins/devops-engineer)** - DevOps and infrastructure automation specialist with CI/CD, IaC, deployment, and monitoring capab...  

**Global installation:**
```bash
/plugin install devops-engineer@puerto
```

---

**[Digital Legacy Planner](plugins/digital-legacy-planner)** - Digital estate planning and access instruction specialist for managing digital accounts, assets, ...  

**Global installation:**
```bash
/plugin install digital-legacy-planner@puerto
```

---

**[Digital Transformation](plugins/digital-transformation)** - Digital transformation planning specialist for maturity assessment, technology roadmaps, change m...  

**Global installation:**
```bash
/plugin install digital-transformation@puerto
```

---

**[Document Organizer](plugins/document-organizer)** - Document archiving and organization specialist with auto-categorization, OCR, warranty tracking, ...  

**Global installation:**
```bash
/plugin install document-organizer@puerto
```

---

**[Ecommerce Specialist](plugins/ecommerce-specialist)** - E-commerce operations specialist for online store management  

**Global installation:**
```bash
/plugin install ecommerce-specialist@puerto
```

---

**[Email Management System](plugins/email-management-system)** - Intelligent email triage, categorization, and management system with auto-categorization, respons...  

**Global installation:**
```bash
/plugin install email-management-system@puerto
```

---

**[Email Marketer](plugins/email-marketer)** - Email marketing specialist  

**Global installation:**
```bash
/plugin install email-marketer@puerto
```

---

**[Emergency Response Coordinator](plugins/emergency-response-coordinator)** - Emergency situation coordination specialist for crisis escalation, protocol activation, and stake...  

**Global installation:**
```bash
/plugin install emergency-response-coordinator@puerto
```

---

**[Energy Usage Monitor](plugins/energy-usage-monitor)** - Smart energy usage analysis and monitoring with pattern detection, cost projections, efficiency r...  

**Global installation:**
```bash
/plugin install energy-usage-monitor@puerto
```

---

**[Event Planning Orchestrator](plugins/event-planning-orchestrator)** - Comprehensive event planning and coordination system for large events (weddings, parties, confere...  

**Global installation:**
```bash
/plugin install event-planning-orchestrator@puerto
```

---

**[Executive Report Writer](plugins/executive-report-writer)** - Executive reporting specialist for board reports, executive summaries, high-level metrics, strate...  

**Global installation:**
```bash
/plugin install executive-report-writer@puerto
```

---

**[Expense Manager](plugins/expense-manager)** - Comprehensive expense management automation with OCR, policy validation, and approval workflow co...  

**Global installation:**
```bash
/plugin install expense-manager@puerto
```

---

**[Financial Analyst](plugins/financial-analyst)** - Financial modeling and analysis specialist  

**Global installation:**
```bash
/plugin install financial-analyst@puerto
```

---

**[Financial Compliance](plugins/financial-compliance)** - Financial services compliance specialist handling SEC, FINRA, AML/KYC compliance and regulatory r...  

**Global installation:**
```bash
/plugin install financial-compliance@puerto
```

---

**[Fitness Tracking Logger](plugins/fitness-tracking-logger)** - Comprehensive workout logging and fitness progress tracking system for Puerto.  

**Global installation:**
```bash
/plugin install fitness-tracking-logger@puerto
```

---

**[Fraud Analyst](plugins/fraud-analyst)** - A comprehensive fraud detection and prevention specialist for financial transactions, providing r...  

**Global installation:**
```bash
/plugin install fraud-analyst@puerto
```

---

**[Frontend Developer](plugins/frontend-developer)** - Frontend development specialist with React/Vue/Svelte component creation, responsive styling, acc...  

**Global installation:**
```bash
/plugin install frontend-developer@puerto
```

---

**[Goal Tracker](plugins/goal-tracker)** - Financial goal setting and progress tracking specialist with SMART framework  

**Global installation:**
```bash
/plugin install goal-tracker@puerto
```

---

**[Growth Hacker](plugins/growth-hacker)** - Growth strategy and experimentation specialist for viral loops, acquisition channels, retention o...  

**Global installation:**
```bash
/plugin install growth-hacker@puerto
```

---

**[Habit Formation Coach](plugins/habit-formation-coach)** - Science-based habit formation using tiny habits, behavior analysis, and compassionate coaching  

**Global installation:**
```bash
/plugin install habit-formation-coach@puerto
```

---

**[Habit Tracker](plugins/habit-tracker)** - Version: 1.0.0  

**Global installation:**
```bash
/plugin install habit-tracker@puerto
```

---

**[Healthcare Compliance](plugins/healthcare-compliance)** - Healthcare regulatory compliance specialist ensuring HIPAA, FDA, and clinical trial regulations c...  

**Global installation:**
```bash
/plugin install healthcare-compliance@puerto
```

---

**[Home Inventory System](plugins/home-inventory-system)** - Asset cataloging and insurance documentation specialist for household items  

**Global installation:**
```bash
/plugin install home-inventory-system@puerto
```

---

**[Home Maintenance Tracker](plugins/home-maintenance-tracker)** - Comprehensive home maintenance scheduling, warranty tracking, and service history management system  

**Global installation:**
```bash
/plugin install home-maintenance-tracker@puerto
```

---

**[Hotfix Developer](plugins/hotfix-developer)** - Version: 1.0.0  

**Global installation:**
```bash
/plugin install hotfix-developer@puerto
```

---

**[Hr Onboarder](plugins/hr-onboarder)** - Professional HR onboarding automation for creating comprehensive new hire experiences  

**Global installation:**
```bash
/plugin install hr-onboarder@puerto
```

---

**[Hr Performance Manager](plugins/hr-performance-manager)** - Professional performance management system with comprehensive tools for reviews, goal setting, ca...  

**Global installation:**
```bash
/plugin install hr-performance-manager@puerto
```

---

**[Hr Policies Expert](plugins/hr-policies-expert)** - Expert guidance on HR policies, employment law, benefits, and compliance  

**Global installation:**
```bash
/plugin install hr-policies-expert@puerto
```

---

**[Hr Recruiter](plugins/hr-recruiter)** - Professional recruitment assistant for candidate screening, job postings, interview coordination,...  

**Global installation:**
```bash
/plugin install hr-recruiter@puerto
```

---

**[Incident Response](plugins/incident-response)** - Security incident response specialist for breach detection, response coordination, forensic analy...  

**Global installation:**
```bash
/plugin install incident-response@puerto
```

---

**[Innovation Consultant](plugins/innovation-consultant)** - Innovation strategy and ideation specialist for generating ideas, analyzing trends, validating co...  

**Global installation:**
```bash
/plugin install innovation-consultant@puerto
```

---

**[Insurance Policy Manager](plugins/insurance-policy-manager)** - Insurance policy tracking and coverage analysis specialist with multi-policy inventory, gap ident...  

**Global installation:**
```bash
/plugin install insurance-policy-manager@puerto
```

---

**[Insurance Underwriter](plugins/insurance-underwriter)** - A comprehensive insurance underwriting system providing professional risk assessment, policy pric...  

**Global installation:**
```bash
/plugin install insurance-underwriter@puerto
```

---

**[International Expansion Specialist](plugins/international-expansion-specialist)** - Market entry planning specialist for international expansion strategy, regulatory research, and l...  

**Global installation:**
```bash
/plugin install international-expansion-specialist@puerto
```

---

**[Ip Specialist](plugins/ip-specialist)** - Intellectual property management specialist for patent tracking, prior art search, filing documen...  

**Global installation:**
```bash
/plugin install ip-specialist@puerto
```

---

**[It Support Specialist](plugins/it-support-specialist)** - Internal IT support specialist for troubleshooting, access management, and system diagnostics  

**Global installation:**
```bash
/plugin install it-support-specialist@puerto
```

---

**[Knowledge Base Manager](plugins/knowledge-base-manager)** - Knowledge base maintenance specialist  

**Global installation:**
```bash
/plugin install knowledge-base-manager@puerto
```

---

**[Language Learning](plugins/language-learning)** - Your personal AI-powered language learning companion with vocabulary management, spaced repetitio...  

**Global installation:**
```bash
/plugin install language-learning@puerto
```

---

**[Language Learning Assistant](plugins/language-learning-assistant)** - Vocabulary tracking and language immersion specialist  

**Global installation:**
```bash
/plugin install language-learning-assistant@puerto
```

---

**[Learning Plan Generator](plugins/learning-plan-generator)** - Production-ready personalized learning curriculum with spaced repetition scheduling, knowledge as...  

**Global installation:**
```bash
/plugin install learning-plan-generator@puerto
```

---

**[Legal Document Tracker](plugins/legal-document-tracker)** - > Contract expiration, legal deadline monitoring, and document version control specialist  

**Global installation:**
```bash
/plugin install legal-document-tracker@puerto
```

---

**[Legal Reviewer](plugins/legal-reviewer)** - Contract review and analysis specialist for risk identification, clause analysis, and amendment s...  

**Global installation:**
```bash
/plugin install legal-reviewer@puerto
```

---

**[Local Seo Specialist](plugins/local-seo-specialist)** - Local SEO optimization specialist for Google My Business, local listings, and review management.  

**Global installation:**
```bash
/plugin install local-seo-specialist@puerto
```

---

**[Localization Specialist](plugins/localization-specialist)** - Localization strategy and implementation specialist for market-specific content adaptation, cultu...  

**Global installation:**
```bash
/plugin install localization-specialist@puerto
```

---

**[Market Researcher](plugins/market-researcher)** - Market research and competitive analysis specialist with market sizing, competitive intelligence,...  

**Global installation:**
```bash
/plugin install market-researcher@puerto
```

---

**[Meal Planning Nutrition](plugins/meal-planning-nutrition)** - Meal planning and nutrition analysis specialist - weekly meal planning, nutrition tracking, recip...  

**Global installation:**
```bash
/plugin install meal-planning-nutrition@puerto
```

---

**[Medical Appointment Tracker](plugins/medical-appointment-tracker)** - Medical appointment and prescription management specialist - secure health record organization, a...  

**Global installation:**
```bash
/plugin install medical-appointment-tracker@puerto
```

---

**[Medical Writer](plugins/medical-writer)** - Medical and scientific writing specialist for clinical trial protocols, medical manuscripts, pati...  

**Global installation:**
```bash
/plugin install medical-writer@puerto
```

---

**[Mental Health Journal](plugins/mental-health-journal)** - Privacy-first mental health tracking and journaling. Daily mood check-ins, therapy journal, patte...  

**Global installation:**
```bash
/plugin install mental-health-journal@puerto
```

---

**[Ml Engineer](plugins/ml-engineer)** - Machine learning development specialist for model training, feature engineering, evaluation, and ...  

**Global installation:**
```bash
/plugin install ml-engineer@puerto
```

---

**[Mobile Developer](plugins/mobile-developer)** - Mobile app development specialist for iOS/Android applications, mobile UI/UX, platform-specific o...  

**Global installation:**
```bash
/plugin install mobile-developer@puerto
```

---

**[Mortgage Specialist](plugins/mortgage-specialist)** - Professional mortgage processing, credit analysis, and compliance validation for Claude Code  

**Global installation:**
```bash
/plugin install mortgage-specialist@puerto
```

---

**[Moving Coordinator](plugins/moving-coordinator)** - Moving logistics and timeline coordination specialist for stress-free relocations  

**Global installation:**
```bash
/plugin install moving-coordinator@puerto
```

---

**[Network Administrator](plugins/network-administrator)** - Network management and monitoring specialist for configuration, security, and troubleshooting  

**Global installation:**
```bash
/plugin install network-administrator@puerto
```

---

**[Office Administrator](plugins/office-administrator)** - General administrative support specialist for meeting scheduling, travel arrangements, expense pr...  

**Global installation:**
```bash
/plugin install office-administrator@puerto
```

---

**[Orchestrator](plugins/orchestrator)** - Master coordinator for complex multi-agent workflows. Intelligently decomposes tasks, creates exe...  

**Global installation:**
```bash
/plugin install orchestrator@puerto
```

---

**[Parenting Task Manager](plugins/parenting-task-manager)** - Child activity and developmental milestone tracking specialist  

**Global installation:**
```bash
/plugin install parenting-task-manager@puerto
```

---

**[Partnership Manager](plugins/partnership-manager)** - Strategic partnership specialist for partner identification, partnership proposals, deal structur...  

**Global installation:**
```bash
/plugin install partnership-manager@puerto
```

---

**[Password Security Auditor](plugins/password-security-auditor)** - Security audit and breach monitoring specialist with password strength analysis, HIBP integration...  

**Global installation:**
```bash
/plugin install password-security-auditor@puerto
```

---

**[Patent Analyst](plugins/patent-analyst)** - Patent research and analysis specialist for patent searches, prior art identification, freedom to...  

**Global installation:**
```bash
/plugin install patent-analyst@puerto
```

---

**[Payment Integration Specialist](plugins/payment-integration-specialist)** - Payment integration specialist for payment gateway integration, PCI compliance, fraud prevention,...  

**Global installation:**
```bash
/plugin install payment-integration-specialist@puerto
```

---

**[Pet Care Manager](plugins/pet-care-manager)** - Pet health and care routine management specialist  

**Global installation:**
```bash
/plugin install pet-care-manager@puerto
```

---

**[Podcast Producer](plugins/podcast-producer)** - Podcast production coordination specialist for episode planning, show notes, and distribution.  

**Global installation:**
```bash
/plugin install podcast-producer@puerto
```

---

**[Portfolio Tracker](plugins/portfolio-tracker)** - Investment portfolio monitoring and analysis specialist with real-time pricing  

**Global installation:**
```bash
/plugin install portfolio-tracker@puerto
```

---

**[Process Optimizer](plugins/process-optimizer)** - Version: 1.0.0  

**Global installation:**
```bash
/plugin install process-optimizer@puerto
```

---

**[Procurement Specialist](plugins/procurement-specialist)** - Vendor management and purchasing specialist for procurement workflows  

**Global installation:**
```bash
/plugin install procurement-specialist@puerto
```

---

**[Product Analyst](plugins/product-analyst)** - Product analytics specialist  

**Global installation:**
```bash
/plugin install product-analyst@puerto
```

---

**[Product Manager](plugins/product-manager)** - Product strategy specialist  

**Global installation:**
```bash
/plugin install product-manager@puerto
```

---

**[Project Management System](plugins/project-management-system)** - Professional project management capabilities including multi-project dashboards, task coordinatio...  

**Global installation:**
```bash
/plugin install project-management-system@puerto
```

---

**[Project Manager](plugins/project-manager)** - Project coordination and tracking specialist with comprehensive planning, timeline management, ri...  

**Global installation:**
```bash
/plugin install project-manager@puerto
```

---

**[Qa Automation](plugins/qa-automation)** - QA and test automation specialist with test generation, automation, coverage analysis, and bug re...  

**Global installation:**
```bash
/plugin install qa-automation@puerto
```

---

**[Qa Manager](plugins/qa-manager)** - Quality management system specialist for QA process design, quality standards, audits, corrective...  

**Global installation:**
```bash
/plugin install qa-manager@puerto
```

---

**[Quant Analyst](plugins/quant-analyst)** - Quantitative analysis and trading specialist  

**Global installation:**
```bash
/plugin install quant-analyst@puerto
```

---

**[Real Estate Analyst](plugins/real-estate-analyst)** - Real estate analysis and valuation specialist  

**Global installation:**
```bash
/plugin install real-estate-analyst@puerto
```

---

**[Receipt Processor](plugins/receipt-processor)** - Receipt processing and expense categorization specialist with OCR  

**Global installation:**
```bash
/plugin install receipt-processor@puerto
```

---

**[Release Manager](plugins/release-manager)** - Release coordination and deployment specialist for release planning, deployment coordination, rol...  

**Global installation:**
```bash
/plugin install release-manager@puerto
```

---

**[Research Brief Generator](plugins/research-brief-generator)** - Professional research brief generation with multi-source data gathering, comparative analysis, an...  

**Global installation:**
```bash
/plugin install research-brief-generator@puerto
```

---

**[Risk Analyst](plugins/risk-analyst)** - Risk assessment and mitigation specialist  

**Global installation:**
```bash
/plugin install risk-analyst@puerto
```

---

**[Sales Engineer](plugins/sales-engineer)** - Technical sales support specialist for demos, documents, solution architecture, and ROI calculations  

**Global installation:**
```bash
/plugin install sales-engineer@puerto
```

---

**[Sales Lead Qualifier](plugins/sales-lead-qualifier)** - Professional sales lead qualification system with BANT/MEDDIC frameworks, data enrichment, scorin...  

**Global installation:**
```bash
/plugin install sales-lead-qualifier@puerto
```

---

**[Sales Pipeline Analyst](plugins/sales-pipeline-analyst)** - Sales pipeline analysis specialist for monitoring pipeline health, forecasting, risk identificati...  

**Global installation:**
```bash
/plugin install sales-pipeline-analyst@puerto
```

---

**[Sales Proposal Writer](plugins/sales-proposal-writer)** - Sales proposal creation specialist - generates and customizes sales proposals and RFP responses  

**Global installation:**
```bash
/plugin install sales-proposal-writer@puerto
```

---

**[Sem Specialist](plugins/sem-specialist)** - Search engine marketing (PPC) specialist for Google Ads and paid search campaign management.  

**Global installation:**
```bash
/plugin install sem-specialist@puerto
```

---

**[Seo Specialist](plugins/seo-specialist)** - SEO optimization expert for keyword research, technical SEO, and content optimization  

**Global installation:**
```bash
/plugin install seo-specialist@puerto
```

---

**[Shopping List Optimizer](plugins/shopping-list-optimizer)** - Smart grocery list and pantry management specialist with intelligent shopping list generation, st...  

**Global installation:**
```bash
/plugin install shopping-list-optimizer@puerto
```

---

**[Side Hustle Manager](plugins/side-hustle-manager)** - Side business income and growth tracking specialist with revenue analysis, expense tracking, and ...  

**Global installation:**
```bash
/plugin install side-hustle-manager@puerto
```

---

**[Site Reliability Engineer](plugins/site-reliability-engineer)** - System reliability and uptime specialist for monitoring setup, incident response, performance opt...  

**Global installation:**
```bash
/plugin install site-reliability-engineer@puerto
```

---

**[Sleep Pattern Analyzer](plugins/sleep-pattern-analyzer)** - Sleep quality analysis and optimization specialist - sleep tracking, pattern recognition, quality...  

**Global installation:**
```bash
/plugin install sleep-pattern-analyzer@puerto
```

---

**[Smart Goal Assistant](plugins/smart-goal-assistant)** - A comprehensive goal-setting and tracking system that helps individuals and teams set, plan, trac...  

**Global installation:**
```bash
/plugin install smart-goal-assistant@puerto
```

---

**[Smart Home Integration Hub](plugins/smart-home-integration-hub)** - Comprehensive smart home device coordination, automation, energy monitoring, and multi-platform i...  

**Global installation:**
```bash
/plugin install smart-home-integration-hub@puerto
```

---

**[Social Coordination Manager](plugins/social-coordination-manager)** - Relationship maintenance and social event coordination specialist. Birthday tracking, gift ideas,...  

**Global installation:**
```bash
/plugin install social-coordination-manager@puerto
```

---

**[Social Media Manager](plugins/social-media-manager)** - Social media strategy and execution specialist with content calendar planning, multi-platform pos...  

**Global installation:**
```bash
/plugin install social-media-manager@puerto
```

---

**[Subscription Management Hub](plugins/subscription-management-hub)** - Comprehensive subscription tracking and cost optimization system with renewal alerts, usage analy...  

**Global installation:**
```bash
/plugin install subscription-management-hub@puerto
```

---

**[Supply Chain Analyst](plugins/supply-chain-analyst)** - Supply chain optimization specialist  

**Global installation:**
```bash
/plugin install supply-chain-analyst@puerto
```

---

**[Tax Assistant](plugins/tax-assistant)** - Tax preparation and document organization specialist for tax season  

**Global installation:**
```bash
/plugin install tax-assistant@puerto
```

---

**[Tax Compliance](plugins/tax-compliance)** - Professional tax obligation tracking, filing preparation, and regulatory compliance for Claude Code  

**Global installation:**
```bash
/plugin install tax-compliance@puerto
```

---

**[Tax Compliance Specialist](plugins/tax-compliance-specialist)** - Tax compliance support specialist - tracks tax obligations, filing preparation, and regulation up...  

**Global installation:**
```bash
/plugin install tax-compliance-specialist@puerto
```

---

**[Technical Support](plugins/technical-support)** - Technical troubleshooting specialist for diagnostics, log analysis, bug reproduction, and workaro...  

**Global installation:**
```bash
/plugin install technical-support@puerto
```

---

**[Technical Writer](plugins/technical-writer)** - Technical documentation specialist  

**Global installation:**
```bash
/plugin install technical-writer@puerto
```

---

**[Training Developer](plugins/training-developer)** - Training content creation specialist  

**Global installation:**
```bash
/plugin install training-developer@puerto
```

---

**[Translator](plugins/translator)** - Multi-language translation specialist for content translation, localization adaptation, cultural ...  

**Global installation:**
```bash
/plugin install translator@puerto
```

---

**[Travel Planning Assistant](plugins/travel-planning-assistant)** - Comprehensive travel planning companion with trip itinerary creation, weather-based packing lists...  

**Global installation:**
```bash
/plugin install travel-planning-assistant@puerto
```

---

**[Ux Researcher](plugins/ux-researcher)** - User research specialist  

**Global installation:**
```bash
/plugin install ux-researcher@puerto
```

---

**[Ux Writer](plugins/ux-writer)** - UX/UI copy and microcopy specialist for interface text, error messages, onboarding flows, and acc...  

**Global installation:**
```bash
/plugin install ux-writer@puerto
```

---

**[Video Producer](plugins/video-producer)** - Video content planning and scripting specialist for multi-platform video production.  

**Global installation:**
```bash
/plugin install video-producer@puerto
```

---

**[Volunteer Time Tracker](plugins/volunteer-time-tracker)** - Comprehensive volunteer service logging and impact measurement system with hours tracking, organi...

**Global installation:**
```bash
/plugin install volunteer-time-tracker@puerto
```

---

**[Web Performance Auditor](plugins/web-performance-auditor)** - Web performance auditing and optimization using Lighthouse with comprehensive analysis and actionable recommendations

**Global installation:**
```bash
/plugin install web-performance-auditor@puerto
```

---


## License

MIT License
