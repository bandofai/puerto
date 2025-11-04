# Using Agents
> Part of the [User Guide](index.md).

Agents are specialized subagents that handle specific tasks autonomously. Learn how to work with them effectively.

## What Are Agents?

Agents are AI assistants specialized for specific tasks, packaged within plugins.

**Examples:**
- `frontend-engineer` (engineering) - Create React components and UI
- `backend-engineer` (engineering) - Build APIs and services
- `data-analyst` (product) - Analyze datasets and metrics

## How Agents Work

### Automatic Invocation

Claude automatically invokes agents when needed:

```
You: "Create a React button component with accessibility support"
Claude: [Invokes engineering/frontend-engineer agent]
```

### Manual Invocation

Explicitly request an agent:

```
You: "Use the accessibility specialist to check my component"
Claude: [Invokes design/accessibility-specialist]
```

## Agent Capabilities

### Specialized Knowledge

Agents have deep expertise in their domain:

- **Technical knowledge** - Best practices, patterns, APIs
- **Code templates** - Pre-built structures
- **Validation rules** - Quality checks
- **Domain skills** - Referenced knowledge libraries

### Autonomous Operation

Agents work independently:

1. Analyze the task
2. Access necessary skills
3. Use appropriate tools
4. Execute the work
5. Report results

### Skill Integration

Agents can reference plugin skills:

**Example:** The `frontend-engineer` agent references:
- `frontend-development` skill (component patterns, responsive design)
- `accessibility` skill (from design department)
- `testing-practices` skill

## Working with Agents

### Request Specific Agent

```
"Use the design/accessibility-specialist agent to review my form"
"Have the engineering/backend-engineer agent check these endpoints"
"Ask the product/data-analyst agent to examine this dataset"
```

### Let Claude Choose

```
"Audit my component for accessibility"
"Test my REST API"
"Analyze this sales data"
```

Claude selects the appropriate agent based on the task.

### Agent Workflows

Agents can work in sequence:

```
You: "Build a user profile component"

Claude:
1. [engineering/frontend-engineer] Creates component structure
2. [design/accessibility-specialist] Checks accessibility
3. [design/ux-researcher] Adds responsive styles
```

## Common Agent Types

### Builder Agents

Create code or artifacts:
- `engineering/frontend-engineer` - Build UI components
- `engineering/backend-engineer` - Create API endpoints
- `engineering/data-engineer` - Build data pipelines

### Analyzer Agents

Examine and report:
- `design/accessibility-specialist` - Check accessibility
- `product/data-analyst` - Analyze datasets
- `engineering/devops-engineer` - Profile performance

### Tester Agents

Validate functionality:
- `engineering/backend-engineer` - Test APIs
- `engineering/qa-engineer` - Test integrations
- `engineering/qa-engineer` - Create tests

### Manager Agents

Coordinate work:
- `product/project-manager` - Plan projects
- `product/product-manager` - Manage requirements
- `operations/project-manager` - Coordinate tasks

## Agent Examples

### Frontend Development

**Available Agents:**
- `engineering/frontend-engineer` - Create components
- `design/accessibility-specialist` - Check compliance
- `design/ux-researcher` - Implement responsive design
- `engineering/frontend-engineer` - Manage application state

**Usage:**
```
"Create an accessible navigation component with mobile menu"
```
→ Invokes `engineering/frontend-engineer` and `design/accessibility-specialist`

### API Development

**Available Agents:**
- `engineering/backend-engineer` - Build endpoints
- `engineering/backend-engineer` - Add authentication
- `engineering/backend-engineer` - Test APIs
- `engineering/backend-engineer` - Generate docs

**Usage:**
```
"Create a REST endpoint for user registration with JWT auth"
```
→ Invokes `engineering/backend-engineer`

### Data Science

**Available Agents:**
- `product/data-analyst` - Analyze data
- `engineering/data-engineer` - Train ML models
- `engineering/data-engineer` - Engineer features
- `engineering/data-engineer` - Run experiments

**Usage:**
```
"Analyze this customer churn dataset and suggest features"
```
→ Invokes `product/data-analyst` and `engineering/data-engineer`

## Agent Configuration

### Agent Models

Agents may use different Claude models:

- **Sonnet** - Complex analysis, architecture
- **Haiku** - Fast CRUD operations, simple tasks
- **Opus** - Deep reasoning, critical tasks

Check plugin documentation for agent model info.

### Agent Tools

Agents have access to specific tools:

**Example:** `engineering/frontend-engineer` agent:
- Read, Write, Edit tools
- Glob, Grep for searching
- No Bash (security)

### Agent Skills

Agents reference plugin skills:

**Example:** `design/accessibility-specialist` references:
- WCAG guidelines
- ARIA patterns
- Testing strategies

## Best Practices

### Be Specific

✅ **Good:**
```
"Use the product/data-analyst agent to find correlations in sales data"
```

❌ **Vague:**
```
"Analyze data"
```

### Provide Context

✅ **Good:**
```
"Create an accessible form component following WCAG 2.1 AA"
```

❌ **Insufficient:**
```
"Make a form"
```

### Trust Agent Expertise

Agents are specialized - let them work:

✅ "Check my API security using the engineering/backend-engineer agent"
❌ "Add a check for X, Y, Z..." (micro-management)

### Review Agent Output

Always review what agents produce:
- Check code quality
- Verify functionality
- Test thoroughly

## Troubleshooting

### Agent Not Available

**Issue:** Request an agent that doesn't exist

**Solution:**
- Check plugin documentation
- Verify plugin is installed
- Use correct agent name

### Agent Fails

**Issue:** Agent encounters an error

**Solutions:**
- Provide more context
- Check prerequisites
- Simplify the request
- Review error details

### Unexpected Results

**Issue:** Agent output isn't what you expected

**Solutions:**
- Clarify requirements
- Provide examples
- Reference specific patterns
- Break into smaller tasks

## Next Steps

- **[Use Skills](using-skills.md)** - Leveraging skills
- **[Plugin Catalog](../plugins/by-category.md)** - See all plugins
- **[Troubleshooting](troubleshooting.md)** - Solve issues

## Need Help?

- **[FAQ](faq.md)** - Common questions
- **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Get support
