# Plugin Development Quick Reference
> Part of the [Plugin Development Guide](index.md).

A cheat sheet for common plugin development workflows.

## Quick Commands

| Task | Command |
|------|---------|
| Create new plugin | `/plugin-manager create` |
| Validate plugin | `node scripts/validate-plugin.js path/to/plugin/` |
| Test locally | Copy to `puerto/plugins/` then restart Claude Code |
| List installed plugins | `/plugin list` |
| Install plugin | `/plugin install plugin-name@puerto` |

---

## Common Workflows

### 🚀 Create a Simple Command Plugin

**Fastest way:**
```bash
/plugin-manager create
# Choose: "command" type
# Name it, describe it
# Done!
```

**What you get:**
- `commands/your-command.md` - Ready to customize
- `plugin.json` - Auto-generated manifest
- `README.md` - Pre-filled documentation

---

### 🤖 Create an Agent Plugin

**Fastest way:**
```bash
/plugin-manager create
# Choose: "agent" type
# Specify agent purpose
```

**What you need to know:**
```markdown
---
name: agent-name
description: What the agent does
tools: Read, Write, Edit, Bash
model: sonnet  # or haiku for cost efficiency
---

Your agent's detailed instructions here...
```

**Agent file location:** `agents/agent-name.md`

---

### 📚 Create a Skill Library

**Fastest way:**
```bash
/plugin-manager create
# Choose: "skill" type
# Name your skill area
```

**Skill structure:**
```
skills/
└── your-skill-name/
    └── SKILL.md          # Main skill document
```

**Best for:**
- Reusable knowledge patterns
- Best practices documentation
- Templates and examples
- Reference guides

---

### 🔧 Add Multiple Components

**Create a full-featured plugin:**
```bash
/plugin-manager create
# Choose: "all" or select multiple types
```

**Typical structure:**
```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── README.md
├── commands/              # Slash commands
│   ├── init.md
│   └── deploy.md
├── agents/                # Specialized subagents
│   ├── planner.md
│   └── executor.md
├── skills/                # Knowledge libraries
│   └── best-practices/
│       └── SKILL.md
└── templates/             # File templates
    └── config.json
```

---

## Common Patterns

### Pattern: Add a Simple Task Command

**When to use:** User needs a quick action (e.g., format, lint, deploy)

**Example: `/format` command**

`commands/format.md`:
```markdown
When the user invokes /format, automatically format all code files in the current directory using the project's formatting rules.

Steps:
1. Detect the project type (package.json, requirements.txt, etc.)
2. Run the appropriate formatter (prettier, black, gofmt, etc.)
3. Report which files were formatted
4. Show any errors encountered

Be concise and focus on results.
```

---

### Pattern: Create a Specialist Agent

**When to use:** Need deep expertise in a domain (e.g., SEO, testing, security)

**Example: SEO Specialist**

`agents/seo-specialist.md`:
```markdown
---
name: seo-specialist
description: SEO optimization and audit specialist
tools: Read, Write, Edit, Bash, WebFetch
model: sonnet
---

You are an expert SEO specialist. When invoked, you:

1. **Audit existing content** - Analyze pages for SEO best practices
2. **Optimize content** - Improve titles, meta descriptions, headings, keywords
3. **Generate recommendations** - Provide actionable SEO improvements
4. **Track keywords** - Monitor keyword rankings and suggest new targets

Key expertise:
- Technical SEO (structured data, sitemaps, robots.txt)
- On-page optimization (content, keywords, internal linking)
- Performance optimization (Core Web Vitals)
- Local SEO (Google My Business, local citations)

Always provide data-driven recommendations with expected impact.
```

---

### Pattern: Build a Knowledge Skill

**When to use:** Agents need to reference best practices or templates

**Example: API Design Skill**

`skills/api-design/SKILL.md`:
```markdown
# API Design Best Practices

## RESTful Design Principles

### Resource Naming
- Use plural nouns: `/users`, `/products`
- Use kebab-case: `/order-items`
- Avoid verbs in URLs
- Keep URLs shallow (max 3 levels)

### HTTP Methods
- `GET` - Retrieve resources (safe, idempotent)
- `POST` - Create resources
- `PUT` - Update/replace resources (idempotent)
- `PATCH` - Partial updates
- `DELETE` - Remove resources (idempotent)

### Status Codes
- `200 OK` - Successful GET, PUT, PATCH
- `201 Created` - Successful POST
- `204 No Content` - Successful DELETE
- `400 Bad Request` - Invalid input
- `401 Unauthorized` - Auth required
- `403 Forbidden` - Authenticated but not authorized
- `404 Not Found` - Resource doesn't exist
- `500 Internal Server Error` - Server error

### Versioning
- URL versioning: `/api/v1/users`
- Header versioning: `Accept: application/vnd.api+json;version=1`
- Choose one approach and be consistent

### Pagination
```json
{
  "data": [...],
  "meta": {
    "page": 1,
    "per_page": 20,
    "total": 100,
    "total_pages": 5
  },
  "links": {
    "first": "/users?page=1",
    "last": "/users?page=5",
    "prev": null,
    "next": "/users?page=2"
  }
}
```

### Error Responses
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "message": "Must be a valid email address"
      }
    ]
  }
}
```

## OpenAPI/Swagger Documentation

Always document APIs with OpenAPI 3.0 spec:
- Clear descriptions for all endpoints
- Request/response examples
- Schema definitions
- Authentication requirements

## Security Best Practices

- Always use HTTPS
- Implement rate limiting
- Validate all inputs
- Use proper authentication (OAuth 2.0, JWT)
- Never expose sensitive data in URLs
- Implement CORS properly
- Use API keys for service-to-service auth

## Testing

- Write tests for all endpoints
- Test happy paths and error cases
- Test edge cases and validation
- Load test for performance
- Security test for vulnerabilities
```

---

## File Format Reference

### Plugin Manifest (`plugin.json`)

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "Clear, concise description",
  "author": {
    "name": "Your Name",
    "email": "you@example.com",
    "url": "https://yoursite.com"
  },
  "keywords": ["keyword1", "keyword2"],
  "license": "MIT",
  "homepage": "https://github.com/you/plugin",
  "repository": {
    "type": "git",
    "url": "https://github.com/you/plugin"
  }
}
```

### Agent Frontmatter

```markdown
---
name: agent-name
description: One-line description
tools: Read, Write, Edit, Bash
model: sonnet  # or haiku
---
```

**Available models:**
- `sonnet` - Most capable (Claude 3.5 Sonnet)
- `haiku` - Fast and cost-effective (Claude 3.5 Haiku)

**Common tool combinations:**
- Read-only: `Read, Glob, Grep`
- File editing: `Read, Write, Edit`
- Full development: `Read, Write, Edit, Bash`
- Web access: `Read, Write, WebFetch`

---

## Testing Checklist

Before publishing your plugin:

- [ ] **Validation passes** - Run `node scripts/validate-plugin.js`
- [ ] **README complete** - Installation, usage, features documented
- [ ] **Commands work** - Test all slash commands
- [ ] **Agents respond** - Verify agent behavior
- [ ] **Skills load** - Check skill files are accessible
- [ ] **No hardcoded paths** - Use relative paths only
- [ ] **Examples provided** - Show common usage patterns
- [ ] **Keywords added** - Help users discover your plugin
- [ ] **Version is 1.0.0** - For initial release
- [ ] **License specified** - Default to MIT if unsure

---

## Publishing Workflow

### 1. Create Plugin
```bash
/plugin-manager create
# OR manually create structure
```

### 2. Develop and Test
```bash
# Copy to Puerto plugins directory
cp -r my-plugin /path/to/puerto/plugins/

# Restart Claude Code
# Test your plugin
```

### 3. Validate
```bash
node scripts/validate-plugin.js plugins/my-plugin/
```

### 4. Submit
```bash
# Fork Puerto on GitHub
# Add your plugin to plugins/ directory
# Create pull request
```

### 5. Review Process
- Automated validation runs
- Maintainers review code
- Address feedback
- Merge and publish

---

## Common Issues & Solutions

### Plugin Not Loading

**Issue:** Plugin installed but commands don't work

**Solutions:**
- Restart Claude Code completely
- Check plugin name matches directory name
- Verify `.claude-plugin/plugin.json` exists
- Run validation: `node scripts/validate-plugin.js`

---

### Command Not Found

**Issue:** `/my-command` shows "command not found"

**Solutions:**
- Ensure command file is `.md` not `.txt`
- Check file is in `commands/` directory
- Verify file name matches command (e.g., `commands/my-command.md`)
- Restart Claude Code

---

### Agent Not Responding

**Issue:** Agent doesn't activate or respond correctly

**Solutions:**
- Verify frontmatter format (YAML between `---`)
- Check `name` field matches filename
- Ensure `tools` are valid tool names
- Validate `model` is either `sonnet` or `haiku`

---

### Validation Errors

**Issue:** `validate-plugin.js` reports errors

**Common fixes:**
- **Missing plugin.json**: Create `.claude-plugin/plugin.json`
- **Invalid JSON**: Check syntax (commas, quotes, braces)
- **Missing required fields**: Add `name`, `version`, `description`
- **Invalid version**: Use semver format (e.g., `1.0.0`)

---

## Useful Resources

- **[Plugin Structure Guide](plugin-structure.md)** - Detailed structure explanation
- **[Plugin Manifest Schema](../reference/plugin-json-schema.md)** - Complete JSON reference
- **[Agent Guide](agents.md)** - Building effective agents
- **[Skill Guide](skills.md)** - Creating skill libraries
- **[Examples Directory](../examples/)** - Real plugin examples
- **[Best Practices](best-practices.md)** - Quality guidelines

---

## Quick Tips

### 💡 Start Simple
Begin with one command or agent. Add complexity as needed.

### 💡 Use `/plugin-manager`
Fastest way to get started without errors.

### 💡 Copy from Examples
Browse existing plugins for inspiration and patterns.

### 💡 Test Early, Test Often
Don't wait until completion to test your plugin.

### 💡 Write Clear Descriptions
Users discover plugins through search - make descriptions specific.

### 💡 Keep Commands Focused
One command should do one thing well.

### 💡 Document Usage Examples
Show real examples in your README.

### 💡 Choose the Right Model
- Use `haiku` for simple tasks (faster, cheaper)
- Use `sonnet` for complex reasoning (more capable)

---

Need more help? Check the [Plugin Development Guide](index.md) or [FAQ](../user-guide/faq.md).
