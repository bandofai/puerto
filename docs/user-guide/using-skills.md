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

**Example:** `frontend-developer` plugin:
- `component-patterns` - Component architecture
- `accessibility-guidelines` - WCAG compliance
- `responsive-design` - Mobile-first patterns

### Skills Benefit Users Indirectly

You don't invoke skills directly - agents reference them automatically to provide better results.

## How Skills Improve Results

### Consistent Quality

Skills ensure agents follow best practices:

```
"Create a navigation component"
→ Agent references component-patterns skill
→ Applies consistent architecture
→ Follows naming conventions
→ Includes proper documentation
```

### Domain Expertise

Skills encode specialized knowledge:

```
"Analyze churn prediction data"
→ Agent references data-science-patterns skill
→ Applies appropriate algorithms
→ Uses correct metrics
→ Follows statistical best practices
```

### Up-to-Date Standards

Skills maintain current practices:

```
"Make this form accessible"
→ Agent references accessibility-guidelines skill (WCAG 2.2)
→ Uses latest ARIA patterns
→ Applies modern testing approaches
```

## Skill Examples

### Development Skills

**Component Patterns** (frontend-developer)
- Component architecture
- Props design
- State management
- Composition patterns

**API Design Patterns** (api-developer)
- REST conventions
- Error handling
- Authentication flows
- Versioning strategies

**Database Design** (database-architect)
- Normalization patterns
- Index strategies
- Migration patterns
- Performance optimization

### Domain Skills

**Reading Management** (book-reading-tracker)
- Tracking approaches
- Note-taking strategies
- Progress metrics
- Goal setting

**Exercise Library** (fitness-tracking-logger)
- Exercise categorization
- Form guidelines
- Progression patterns
- Recovery protocols

**Home Maintenance** (home-maintenance-tracker)
- Maintenance schedules
- Seasonal checklists
- Warranty tracking
- Service documentation

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

Many Puerto plugins include skills:

| Plugin | Skills |
|--------|--------|
| **book-reading-tracker** | reading-management, note-taking, book-analytics |
| **home-maintenance-tracker** | home-maintenance |
| **language-learning-assistant** | vocabulary-learning, language-practice, immersion-tracking |
| **parenting-task-manager** | child-activities, school-management, developmental-tracking |
| **pet-care-manager** | daily-care, veterinary-care, pet-health |

Check [Plugin Catalog](../plugins/by-feature.md) for skill-enabled plugins.

## For Plugin Developers

Want to create skills for your plugins?

See [Developing Skills](../plugin-development/skills.md) in the Plugin Development Guide.

## Next Steps

- **[Troubleshooting](troubleshooting.md)** - Solve issues
- **[FAQ](faq.md)** - Common questions
- **[Plugin Catalog](../plugins/by-category.md)** - Browse plugins

## Need Help?

- **[GitHub Issues](https://github.com/bandofai/puerto/issues)** - Get support
