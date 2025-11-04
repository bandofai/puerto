# Browsing Plugins
> Part of the [User Guide](index.md).

Puerto offers 140+ plugins across diverse categories. This guide helps you discover the right plugins for your needs.

## Quick Browse Options

### By Category (Recommended)

Browse plugins organized into "squads" by domain:

📖 **[Plugin Catalog by Category](../plugins/by-category.md)**

**Major Categories:**
- **Web Development** - Frontend, backend, full-stack tools
- **Mobile & App** - iOS, Android, cross-platform development
- **Data & Analytics** - Data science, ML, analytics, visualization
- **Marketing & Growth** - SEO, content, social media, growth hacking
- **E-commerce** - Online store management, inventory, fulfillment
- **Finance & Accounting** - Financial analysis, accounting, compliance
- **Business Operations** - Project management, process optimization
- **Sales & Customer Success** - CRM, proposals, customer success
- **HR & People** - Recruiting, onboarding, performance management
- **Product Development** - Product management, QA, release management
- **Content & Media** - Writing, video, podcast production
- **Research & Intelligence** - Market research, competitive analysis
- **Healthcare & Wellness** - Medical, clinical, wellness tracking
- **Personal Productivity** - Habits, goals, time management
- **Home & Life** - Home management, family organization
- **And more...**

### By Feature Type

Filter plugins by what they provide:

📖 **[Plugin Catalog](../plugins/by-category.md)**

- **Commands** - Slash commands (e.g., `/brainstorm`, `/implement`)
- **Agents** - Specialized subagents for specific tasks
- **Skills** - Knowledge libraries for agents
- **MCP Servers** - External tool integrations
- **Templates** - Pre-built file templates

### Featured Plugins

Start with the most essential plugins:

📖 **[Featured Plugins](../plugins/featured.md)**

**Essentials:**
- **essentials** - MCP servers (Serena, Context7, Sequential Thinking, Playwright) and requirements management
- **subagent-creator** - Expert subagent architect with skill library

**Popular Departments:**
- **engineering** - Full-stack development (7 agents)
- **design** - UX research, writing, accessibility (4 agents)
- **marketing** - Content, SEO, social, growth (5 agents)
- **product** - Product management and analytics (4 agents)

### Complete Alphabetical List

Browse all plugins alphabetically:

📖 **[Complete Plugin List](../plugins/complete-list.md)**

## Using Claude Code CLI

### List All Puerto Plugins

```bash
/plugin list puerto
```

### Search for Plugins

```bash
# Search by keyword
/plugin search frontend @puerto
/plugin search data @puerto
/plugin search marketing @puerto
```

### View Plugin Details

```bash
/plugin info essentials@puerto
```

Shows:
- Plugin description
- Version
- Author
- Included features (commands, agents, skills, etc.)

## Choosing the Right Plugin

### By Role/Job Function

**I'm a...**
- **Frontend Developer** → engineering, design, figma
- **Backend Developer** → engineering
- **Full-Stack Developer** → engineering, design
- **Data Scientist** → engineering (data-engineer), product (data-analyst)
- **Product Manager** → product, design
- **Designer** → design, figma
- **Marketer** → marketing, design
- **DevOps Engineer** → engineering (devops-engineer)

### By Task

**I want to...**
- **Build an API** → engineering (backend-engineer)
- **Analyze data** → product (data-analyst)
- **Write content** → marketing (content-strategist)
- **Manage projects** → product (project-manager)
- **Improve SEO** → marketing (seo-specialist)
- **Create subagents** → subagent-creator
- **Design UX** → design (ux-researcher, ux-writer)
- **Manage sales** → sales

### By Technology

**I work with...**
- **React/Vue/Angular** → engineering (frontend-engineer)
- **Node.js/Express** → engineering (backend-engineer)
- **Python/Django** → engineering (backend-engineer, data-engineer)
- **Kubernetes/Docker** → engineering (devops-engineer)
- **PostgreSQL/MySQL** → engineering (backend-engineer)
- **TensorFlow/PyTorch** → engineering (data-engineer)
- **Figma** → figma

## Understanding Plugin Capabilities

### What Plugins Can Do

#### 1. Commands

Slash commands you can invoke directly:

```bash
# From essentials plugin
/brainstorm feature-name     # Start requirement definition
/implement feature-name      # Implement requirement
/req-list                    # List all requirements
```

#### 2. Agents

Specialized subagents that handle specific tasks autonomously:

**Example:** The `engineering` department includes agents like:
- `frontend-engineer` - React/Vue UI development
- `backend-engineer` - APIs and databases
- `devops-engineer` - CI/CD and infrastructure

#### 3. Skills

Reusable knowledge libraries that agents can reference:

**Example:** The `engineering` department includes:
- `frontend-development` - Component patterns, responsive design
- `backend-architecture` - API design, database schemas
- `testing-practices` - Test automation frameworks

#### 4. MCP Servers

External tool integrations:

**Example:** The `essentials` plugin provides:
- **Serena** - Semantic code navigation with LSP
- **Context7** - Up-to-date library documentation
- **Sequential Thinking** - Structured reasoning
- **Playwright** - Browser automation and visual testing

#### 5. Templates

Pre-built file templates:

**Example:** The `engineering` department includes:
- Component templates (React/Vue)
- Test templates
- Code style guides

### Reading Plugin Descriptions

Plugin descriptions follow a pattern:

**Format:**
```
[plugin-name] - [brief description]

Includes:
- [feature-count] specialized agents
- [skill-count] comprehensive skills
- [template-count] templates

Key Features:
- [main capability 1]
- [main capability 2]
- [main capability 3]
```

**Example:**
```
engineering - Build modern, accessible web interfaces

Includes:
- 4 specialized agents
- 3 comprehensive skills
- 5+ templates

Key Features:
- React/Vue component generation
- Accessibility compliance
- Responsive design implementation
```

## Finding Plugins for Your Project

### For a Web App Project

```json
{
  "plugins": [
    {"name": "essentials", "marketplace": "puerto"},
    {"name": "engineering", "marketplace": "puerto"},
    {"name": "engineering", "marketplace": "puerto"},
    {"name": "engineering", "marketplace": "puerto"},
    {"name": "engineering", "marketplace": "puerto"},
    {"name": "devops-engineer", "marketplace": "puerto"}
  ]
}
```

### For a Data Science Project

```json
{
  "plugins": [
    {"name": "essentials", "marketplace": "puerto"},
    {"name": "data-scientist", "marketplace": "puerto"},
    {"name": "ml-engineer", "marketplace": "puerto"},
    {"name": "data-analyst", "marketplace": "puerto"}
  ]
}
```

### For a Marketing Team

```json
{
  "plugins": [
    {"name": "essentials", "marketplace": "puerto"},
    {"name": "seo-specialist", "marketplace": "puerto"},
    {"name": "content-writer", "marketplace": "puerto"},
    {"name": "social-media-manager", "marketplace": "puerto"},
    {"name": "email-marketer", "marketplace": "puerto"}
  ]
}
```

### For Personal Productivity

```json
{
  "plugins": [
    {"name": "essentials", "marketplace": "puerto"},
    {"name": "goal-tracker", "marketplace": "puerto"},
    {"name": "habit-tracker", "marketplace": "puerto"},
    {"name": "budget-tracker", "marketplace": "puerto"},
    {"name": "book-reading-tracker", "marketplace": "puerto"}
  ]
}
```

## Plugin Quality Indicators

All Puerto plugins meet quality standards:

✅ **Validated Structure** - Passes automated validation
✅ **Complete Manifest** - Proper plugin.json with all fields
✅ **Documentation** - README with usage instructions
✅ **Consistent Naming** - Follows naming conventions
✅ **Tested** - Validated before catalog inclusion

## Next Steps

- **[Install Plugins](installing-plugins.md)** - Install the plugins you found
- **[Configure Plugins](configuring-plugins.md)** - Set up plugin options
- **[Use Commands](using-commands.md)** - Learn command usage
- **[Use Agents](using-agents.md)** - Work with agents
- **[Plugin Catalog](../plugins/by-category.md)** - Browse all plugins

## Need Help?

- **[FAQ](faq.md)** - Common questions
- **[Troubleshooting](troubleshooting.md)** - Solve issues
- **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Get support
