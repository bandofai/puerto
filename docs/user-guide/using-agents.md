# Using Agents
> Part of the [User Guide](index.md).

Agents are specialized subagents that handle specific tasks autonomously. Learn how to work with them effectively.

## What Are Agents?

Agents are AI assistants specialized for specific tasks, packaged within plugins.

**Examples:**
- `component-builder` (frontend-developer) - Create React components
- `api-tester` (api-developer) - Test API endpoints
- `data-analyzer` (data-scientist) - Analyze datasets

## How Agents Work

### Automatic Invocation

Claude automatically invokes agents when needed:

```
You: "Create a React button component with accessibility support"
Claude: [Invokes component-builder agent]
```

### Manual Invocation

Explicitly request an agent:

```
You: "Use the accessibility-auditor agent to check my component"
Claude: [Invokes accessibility-auditor]
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

**Example:** The `component-builder` agent references:
- `component-patterns` skill
- `accessibility-guidelines` skill
- `responsive-design` skill

## Working with Agents

### Request Specific Agent

```
"Use the accessibility-auditor agent to review my form"
"Have the api-tester agent check these endpoints"
"Ask the data-analyzer agent to examine this dataset"
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
1. [component-builder] Creates component structure
2. [accessibility-auditor] Checks accessibility
3. [responsive-designer] Adds responsive styles
```

## Common Agent Types

### Builder Agents

Create code or artifacts:
- `component-builder` - Build UI components
- `endpoint-builder` - Create API endpoints
- `pipeline-builder` - Build data pipelines

### Analyzer Agents

Examine and report:
- `accessibility-auditor` - Check accessibility
- `data-analyzer` - Analyze datasets
- `performance-analyzer` - Profile performance

### Tester Agents

Validate functionality:
- `api-tester` - Test APIs
- `integration-tester` - Test integrations
- `unit-test-generator` - Create tests

### Manager Agents

Coordinate work:
- `project-planner` - Plan projects
- `requirement-manager` - Manage requirements
- `workflow-coordinator` - Coordinate tasks

## Agent Examples

### Frontend Development

**Available Agents:**
- `component-builder` - Create components
- `accessibility-auditor` - Check compliance
- `responsive-designer` - Implement responsive design
- `state-manager` - Manage application state

**Usage:**
```
"Create an accessible navigation component with mobile menu"
```
→ Invokes `component-builder` and `accessibility-auditor`

### API Development

**Available Agents:**
- `endpoint-builder` - Build endpoints
- `auth-implementer` - Add authentication
- `api-tester` - Test APIs
- `openapi-generator` - Generate docs

**Usage:**
```
"Create a REST endpoint for user registration with JWT auth"
```
→ Invokes `endpoint-builder` and `auth-implementer`

### Data Science

**Available Agents:**
- `data-analyzer` - Analyze data
- `model-trainer` - Train ML models
- `feature-engineer` - Engineer features
- `experiment-runner` - Run experiments

**Usage:**
```
"Analyze this customer churn dataset and suggest features"
```
→ Invokes `data-analyzer` and `feature-engineer`

## Agent Configuration

### Agent Models

Agents may use different Claude models:

- **Sonnet** - Complex analysis, architecture
- **Haiku** - Fast CRUD operations, simple tasks
- **Opus** - Deep reasoning, critical tasks

Check plugin documentation for agent model info.

### Agent Tools

Agents have access to specific tools:

**Example:** `component-builder` agent:
- Read, Write, Edit tools
- Glob, Grep for searching
- No Bash (security)

### Agent Skills

Agents reference plugin skills:

**Example:** `accessibility-auditor` references:
- WCAG guidelines
- ARIA patterns
- Testing strategies

## Best Practices

### Be Specific

✅ **Good:**
```
"Use the data-analyzer agent to find correlations in sales data"
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

✅ "Check my API security using the auth-implementer agent"
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
- **[Plugin Catalog](../plugins/by-feature.md)** - See agents by plugin
- **[Troubleshooting](troubleshooting.md)** - Solve issues

## Need Help?

- **[FAQ](faq.md)** - Common questions
- **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Get support
