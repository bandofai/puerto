# Using Skills
> Part of the [User Guide](index.md).

Skills are reusable knowledge libraries that agents reference. Learn how they enhance your workflow.

## What Are Skills?

Skills are documented knowledge that agents can reference to perform tasks better.

**Examples:**
- `accessibility-guidelines` - WCAG standards and patterns
- `api-design-patterns` - REST API best practices
- `responsive-design` - Mobile-first design patterns
- `reading-management` - Book tracking strategies

## How Skills Work

### Automatic Reference

Agents automatically reference relevant skills:

```
You: "Create an accessible form"
Agent: [References accessibility-guidelines skill]
```

### Skill Content

Skills contain:
- **Best practices** - Industry standards
- **Patterns** - Proven solutions
- **Guidelines** - How-to instructions
- **Examples** - Real-world code
- **Checklists** - Quality criteria

## Skills vs Agents

| Agents | Skills |
|--------|--------|
| Do work | Provide knowledge |
| Execute tasks | Document patterns |
| Use tools | Store expertise |
| Autonomous | Referenced |

**Together:** Agents use skills to do work better.

## Discovering Skills

### Check Plugin Documentation

Plugin READMEs list included skills:

**Example:** `engineering` plugin:
- `frontend-development` - Component architecture and patterns
- `backend-architecture` - API design and patterns
- `testing-practices` - Test automation frameworks

### Skills Benefit Users Indirectly

You don't invoke skills directly - agents reference them automatically to provide better results.

## How Skills Improve Results

### Consistent Quality

Skills ensure agents follow best practices:

```
"Create a navigation component"
→ Agent references frontend-development skill
→ Applies consistent architecture
→ Follows naming conventions
→ Includes proper documentation
```

### Domain Expertise

Skills encode specialized knowledge:

```
"Analyze churn prediction data"
→ Agent references data-analysis skill (from product plugin)
→ Applies appropriate algorithms
→ Uses correct metrics
→ Follows statistical best practices
```

### Up-to-Date Standards

Skills maintain current practices:

```
"Make this form accessible"
→ Agent references accessibility skill (from design plugin)
→ Uses latest ARIA patterns (WCAG 2.2)
→ Applies modern testing approaches
```

## Skill Examples

### Development Skills

**Frontend Development** (engineering)
- Component architecture
- Props design
- State management
- Composition patterns

**Backend Architecture** (engineering)
- REST conventions
- Error handling
- Authentication flows
- Versioning strategies

**Testing Practices** (engineering)
- Unit testing patterns
- Integration testing
- Test automation
- Quality assurance

### Domain Skills

**UX Research** (design)
- User research methods
- Persona development
- Journey mapping
- Usability testing

**Content Strategy** (marketing)
- Content planning
- SEO optimization
- Editorial guidelines
- Brand voice

**Project Management** (product)
- Agile methodologies
- Sprint planning
- Backlog management
- Team coordination

## Benefits for Users

### Better Agent Output

Agents produce higher-quality results:

✅ Follows industry standards
✅ Applies proven patterns
✅ Avoids common pitfalls
✅ Includes proper documentation

### Consistency

All agents using the same skill produce consistent results:

- Same code style
- Same patterns
- Same documentation format
- Same quality level

### Learning

Skills document best practices you can learn from:

1. Request work from agent
2. Review generated code/output
3. See patterns applied
4. Learn best practices

## Skill-Aware Plugins

All Puerto department plugins include comprehensive skills:

| Plugin | Example Skills |
|--------|----------------|
| **engineering** | frontend-development, backend-architecture, testing-practices |
| **design** | ux-research, accessibility, visual-design |
| **marketing** | content-strategy, seo-optimization, social-media |
| **product** | product-management, data-analysis, user-research |
| **sales** | sales-process, proposal-writing, customer-relationship |
| **operations** | project-management, process-optimization, risk-management |
| **leadership** | team-management, strategic-planning, decision-making |

Check [Plugin Catalog](../plugins/by-category.md) for complete skill listings.

## For Plugin Developers

Want to create skills for your plugins?

See [Developing Skills](../plugin-development/skills.md) in the Plugin Development Guide.

## Next Steps

- **[Troubleshooting](troubleshooting.md)** - Solve issues
- **[FAQ](faq.md)** - Common questions
- **[Plugin Catalog](../plugins/by-category.md)** - Browse plugins

## Need Help?

- **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Get support
