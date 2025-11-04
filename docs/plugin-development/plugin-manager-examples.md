# Using `/plugin-manager` - Examples
> Part of the [Plugin Development Guide](index.md).

Real-world examples of creating plugins using the `/plugin-manager` command.

## What is `/plugin-manager`?

The `/plugin-manager` command is an interactive wizard that helps you create Puerto plugins quickly and correctly. It:

- ✅ Guides you through plugin creation step-by-step
- ✅ Generates all required files automatically
- ✅ Ensures proper structure and validation
- ✅ Saves time and prevents common errors
- ✅ Provides templates for common patterns

---

## Example 1: Creating a Simple Command Plugin

### Scenario
You want to create a plugin that adds a `/format` command to format code files.

### Steps

**1. Invoke the plugin manager:**
```bash
/plugin-manager create
```

**2. Interactive prompts and responses:**

```
Plugin Manager: What would you like to name your plugin?
You: code-formatter

Plugin Manager: Describe your plugin (one line):
You: Automatically format code files in the current project

Plugin Manager: What should this plugin include?
  [ ] Commands (slash commands)
  [ ] Agents (specialized subagents)
  [ ] Skills (knowledge libraries)
  [ ] Templates
You: Commands

Plugin Manager: Command name (without /):
You: format

Plugin Manager: What does this command do?
You: Format all code files using the project's formatting rules

Plugin Manager: Your name:
You: Jane Developer

Plugin Manager: Your email:
You: jane@example.com

Plugin Manager: ✅ Plugin created successfully at: plugins/code-formatter/
```

**3. Generated structure:**
```
plugins/code-formatter/
├── .claude-plugin/
│   └── plugin.json
├── README.md
└── commands/
    └── format.md
```

**4. Customize the command:**

Edit `commands/format.md`:
```markdown
When the user invokes /format, automatically format all code files in the current directory.

Steps:
1. Detect project type (check for package.json, requirements.txt, etc.)
2. Identify the appropriate formatter:
   - JavaScript/TypeScript → prettier
   - Python → black
   - Go → gofmt
   - Rust → rustfmt
3. Run the formatter on all applicable files
4. Report results (files formatted, any errors)

If no formatter is available for the project type, inform the user and suggest installing one.

Always show a summary of what was formatted.
```

**5. Test it:**
```bash
# Copy to Puerto plugins directory
cp -r plugins/code-formatter /path/to/puerto/plugins/

# Restart Claude Code, then:
/format
```

---

## Example 2: Creating an Agent Plugin

### Scenario
You need a specialist SEO agent that can audit and optimize content.

### Steps

**1. Start the wizard:**
```bash
/plugin-manager create
```

**2. Responses:**
```
Plugin Manager: What would you like to name your plugin?
You: seo-specialist

Plugin Manager: Describe your plugin:
You: SEO audit and optimization specialist for content and technical SEO

Plugin Manager: What should this plugin include?
You: Agents

Plugin Manager: Agent name:
You: seo-auditor

Plugin Manager: Agent description:
You: Audits pages for SEO best practices and provides optimization recommendations

Plugin Manager: Which tools should this agent have?
  Available: Read, Write, Edit, Bash, WebFetch, Glob, Grep
You: Read, Write, WebFetch

Plugin Manager: Which model?
  [1] Sonnet (most capable)
  [2] Haiku (fast, cost-effective)
You: 1

Plugin Manager: Your name:
You: Jane Developer

Plugin Manager: ✅ Plugin created successfully!
```

**3. Generated structure:**
```
plugins/seo-specialist/
├── .claude-plugin/
│   └── plugin.json
├── README.md
└── agents/
    └── seo-auditor.md
```

**4. Customize the agent:**

Edit `agents/seo-auditor.md`:
```markdown
---
name: seo-auditor
description: SEO audit and optimization specialist
tools: Read, Write, WebFetch
model: sonnet
---

You are an expert SEO specialist with deep knowledge of search engine optimization best practices.

## Your Capabilities

### Content Auditing
- Analyze page titles, meta descriptions, heading structure
- Evaluate keyword usage and density
- Check content quality and readability
- Identify duplicate or thin content

### Technical SEO
- Review robots.txt and sitemap
- Check structured data (JSON-LD)
- Analyze Core Web Vitals
- Identify broken links
- Check mobile-friendliness

### On-Page Optimization
- Optimize titles (50-60 characters)
- Craft compelling meta descriptions (150-160 characters)
- Improve heading hierarchy (H1-H6)
- Enhance internal linking
- Optimize images (alt text, file names)

### Reporting
- Provide clear, actionable recommendations
- Prioritize fixes by impact (high/medium/low)
- Estimate expected improvement
- Include specific examples

## When Invoked

1. Ask for the URL or file path to audit
2. Fetch/read the content
3. Perform comprehensive SEO analysis
4. Generate detailed report with:
   - Current SEO score (0-100)
   - Critical issues (must fix)
   - Improvements (should fix)
   - Enhancements (nice to have)
   - Specific recommendations for each issue

Always be constructive and educational in your feedback.
```

**5. Test it:**
```bash
# In Claude Code:
Task: Launch the seo-auditor agent to audit my homepage
```

---

## Example 3: Creating a Full-Featured Plugin

### Scenario
You want to create a comprehensive deployment plugin with commands, agents, and skills.

### Steps

**1. Run the wizard:**
```bash
/plugin-manager create
```

**2. Configuration:**
```
Plugin Manager: Plugin name?
You: deployment-helper

Plugin Manager: Description?
You: Comprehensive deployment automation with multiple cloud providers

Plugin Manager: What to include?
You: All (Commands, Agents, Skills, Templates)

Plugin Manager: How many commands?
You: 2

Plugin Manager: First command name?
You: deploy

Plugin Manager: Second command name?
You: rollback

Plugin Manager: How many agents?
You: 2

Plugin Manager: First agent name?
You: deployment-executor

Plugin Manager: Second agent name?
You: deployment-monitor

Plugin Manager: Skill area name?
You: cloud-deployment

Plugin Manager: Author info?
You: [provide details]

Plugin Manager: ✅ Complete! Plugin structure created.
```

**3. Generated structure:**
```
plugins/deployment-helper/
├── .claude-plugin/
│   └── plugin.json
├── README.md
├── commands/
│   ├── deploy.md
│   └── rollback.md
├── agents/
│   ├── deployment-executor.md
│   └── deployment-monitor.md
├── skills/
│   └── cloud-deployment/
│       └── SKILL.md
└── templates/
    └── deployment-config.json
```

**4. Customize each component** (shortened for brevity):

`commands/deploy.md`:
```markdown
Deploy the current application to the specified environment.

Usage: /deploy [environment] [options]

Environments: staging, production
Options: --skip-tests, --force, --verbose
```

`agents/deployment-executor.md`:
```markdown
---
name: deployment-executor
description: Handles the deployment process across cloud providers
tools: Read, Write, Edit, Bash
model: sonnet
---

Execute deployments to AWS, GCP, Azure, or Vercel...
[detailed instructions]
```

`skills/cloud-deployment/SKILL.md`:
```markdown
# Cloud Deployment Best Practices

## Pre-Deployment Checklist
- [ ] All tests passing
- [ ] Code reviewed and approved
- [ ] Environment variables configured
- [ ] Database migrations ready
- [ ] Rollback plan prepared

## Deployment Strategies
### Blue-Green Deployment
[detailed explanation]

### Canary Deployment
[detailed explanation]

### Rolling Updates
[detailed explanation]
```

`templates/deployment-config.json`:
```json
{
  "name": "my-app",
  "environment": "production",
  "provider": "aws",
  "region": "us-east-1",
  "scaling": {
    "min": 2,
    "max": 10,
    "targetCPU": 70
  }
}
```

---

## Example 4: Creating a Skill-Only Plugin

### Scenario
You want to share API design best practices without commands or agents.

### Steps

**1. Create the plugin:**
```bash
/plugin-manager create
```

**2. Configuration:**
```
Plugin Manager: Plugin name?
You: api-design-patterns

Plugin Manager: Description?
You: Comprehensive API design best practices and patterns

Plugin Manager: What to include?
You: Skills only

Plugin Manager: Skill area name?
You: api-design

Plugin Manager: Include sub-skills?
You: Yes

Plugin Manager: Sub-skill names (comma-separated)?
You: rest-apis, graphql, authentication, versioning

Plugin Manager: Author info?
You: [provide details]

Plugin Manager: ✅ Created!
```

**3. Generated structure:**
```
plugins/api-design-patterns/
├── .claude-plugin/
│   └── plugin.json
├── README.md
└── skills/
    ├── api-design/
    │   └── SKILL.md
    ├── rest-apis/
    │   └── SKILL.md
    ├── graphql/
    │   └── SKILL.md
    ├── authentication/
    │   └── SKILL.md
    └── versioning/
        └── SKILL.md
```

**4. Populate skills** with comprehensive guides.

**5. Use in agents:**
```markdown
---
name: api-architect
skills:
  - api-design-patterns:api-design
  - api-design-patterns:rest-apis
---
```

---

## Example 5: Converting Manual Plugin to Plugin-Manager Format

### Scenario
You created a plugin manually but want to add more components using `/plugin-manager`.

### Steps

**1. Add new component:**
```bash
/plugin-manager add
```

**2. Select plugin:**
```
Plugin Manager: Which plugin?
  [1] code-formatter
  [2] seo-specialist
  [3] deployment-helper
You: 1

Plugin Manager: What would you like to add?
  [ ] Command
  [ ] Agent
  [ ] Skill
  [ ] Template
You: Agent

Plugin Manager: Agent name?
You: format-validator

Plugin Manager: Description?
You: Validates formatting before committing

Plugin Manager: Tools?
You: Read, Bash

Plugin Manager: Model?
You: Haiku

Plugin Manager: ✅ Added agents/format-validator.md to code-formatter!
```

**3. Result:**
```
plugins/code-formatter/
├── .claude-plugin/
│   └── plugin.json
├── README.md
├── commands/
│   └── format.md
└── agents/                    ← New!
    └── format-validator.md    ← New!
```

---

## Example 6: Batch Plugin Creation

### Scenario
You want to create multiple related plugins quickly.

### Steps

**Create plugins in sequence:**

```bash
# Plugin 1: Frontend tools
/plugin-manager create
# Name: frontend-tools
# Include: Commands (build, dev, preview)

# Plugin 2: Backend tools
/plugin-manager create
# Name: backend-tools
# Include: Commands (migrate, seed, test)

# Plugin 3: Full-stack agent
/plugin-manager create
# Name: fullstack-developer
# Include: Agent (full-stack expertise)
```

**Result: Three focused plugins instead of one bloated plugin.**

---

## Tips for Using `/plugin-manager`

### ✅ Do's

- **Start simple** - Create minimal plugin first, add components later
- **Use descriptive names** - Make plugin purpose clear from name
- **One purpose per plugin** - Keep plugins focused
- **Iterate quickly** - Generate → customize → test → improve
- **Follow conventions** - Use generated structure as template

### ❌ Don'ts

- **Don't over-plan** - Start creating, refine as you go
- **Don't create mega-plugins** - Split complex functionality into multiple plugins
- **Don't skip testing** - Test after each component addition
- **Don't ignore validation** - Run `validate-plugin.js` regularly
- **Don't forget documentation** - Keep README updated

---

## Troubleshooting

### Plugin-Manager Not Found

**Issue:** `/plugin-manager` command doesn't work

**Solution:**
```bash
# Ensure Puerto marketplace is added
/plugin marketplace add bandofai/puerto

# Install or update essential plugins
/plugin install essentials@puerto

# Restart Claude Code
```

### Generated Files Need Customization

**Issue:** Generated templates are too generic

**Expected:** This is normal! The plugin-manager creates scaffolding. You customize the details.

**Next steps:**
1. Review generated files
2. Add your specific logic/content
3. Test and iterate

### Want to Start Over

**Issue:** Generated plugin isn't quite right

**Solution:**
```bash
# Delete the plugin directory
rm -rf plugins/plugin-name

# Run plugin-manager again with different options
/plugin-manager create
```

---

## Advanced: Plugin-Manager Options

### Non-Interactive Mode (Future Feature)

```bash
# Create plugin with all options in one command
/plugin-manager create \
  --name my-plugin \
  --description "My awesome plugin" \
  --type command \
  --command-name hello \
  --author "Jane Developer" \
  --email "jane@example.com"
```

### Template Selection (Future Feature)

```bash
# Choose from pre-built templates
/plugin-manager create --template web-developer
/plugin-manager create --template data-analyst
/plugin-manager create --template devops-engineer
```

---

## Next Steps

After creating your plugin with `/plugin-manager`:

1. **Customize** - Edit generated files to add your logic
2. **Test** - Copy to Puerto plugins directory and test thoroughly
3. **Validate** - Run `node scripts/validate-plugin.js`
4. **Document** - Update README with examples and usage
5. **Publish** - Submit PR to Puerto repository

See [Publishing Guide](publishing.md) for submission details.

---

## Related Guides

- **[Quick Reference](quick-reference.md)** - Common patterns and workflows
- **[Plugin Structure](plugin-structure.md)** - Understanding plugin organization
- **[Best Practices](best-practices.md)** - Quality guidelines
- **[Manual Creation](quickstart.md#approach-2-manual-creation)** - Creating plugins manually

---

**Ready to create your first plugin?**

```bash
/plugin-manager create
```

Start building in under 2 minutes!
