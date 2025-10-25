# Using Commands
> Part of the [User Guide](index.md).

Commands are slash commands that plugins provide. Learn how to discover and use them effectively.

## What Are Commands?

Commands are slash-invoked functions like `/brainstorm` or `/implement` that extend Claude Code's capabilities.

## Discovering Commands

### List All Commands

```bash
# List all available commands
/help

# Commands from specific plugin appear when plugin is installed
```

### From Plugin Documentation

Check plugin README or documentation for available commands.

**Example:** The `essentials` plugin provides:
- `/brainstorm <name>` - Define requirements
- `/implement <name>` - Implement requirements
- `/continue [name]` - Resume work
- `/req-list` - List requirements
- `/req-update <name>` - Update requirements
- `/req-tests <name>` - Generate tests

## Using Commands

### Basic Syntax

```bash
/command-name [arguments]
```

### With Required Arguments

```bash
/brainstorm my-feature
/implement authentication-system
/req-update user-profile
```

### With Optional Arguments

```bash
/continue              # Resume last task
/continue my-feature   # Resume specific task
```

### With Flags/Options

Some commands support options:

```bash
/command --option value
/command --flag
```

## Common Command Patterns

### Interactive Commands

Commands that start Q&A sessions:

```bash
/brainstorm feature-name
```

Claude will ask clarifying questions to gather requirements.

### Execution Commands

Commands that perform actions:

```bash
/implement feature-name
```

Claude executes the task based on defined requirements.

### Query Commands

Commands that retrieve information:

```bash
/req-list           # Show all requirements
/req-status name    # Check status
```

### Management Commands

Commands that modify state:

```bash
/req-update name    # Update requirement
/req-delete name    # Remove requirement
```

## Example Workflows

### Requirements Management (Essentials Plugin)

**Step 1: Brainstorm**
```bash
/brainstorm user-authentication
```
Answer questions to define the feature.

**Step 2: Review**
```bash
/req-list
```
See all defined requirements.

**Step 3: Implement**
```bash
/implement user-authentication
```
Claude implements the feature systematically.

**Step 4: Continue If Interrupted**
```bash
/continue
```
Resume from where you left off.

**Step 5: Generate Tests**
```bash
/req-tests user-authentication
```
Create test scenarios.

## Command Help

### Get Command Help

Most commands support help:

```bash
/command --help
/command -h
```

Or ask Claude:

```
How do I use /brainstorm?
What arguments does /implement take?
```

## Best Practices

### Name Arguments Clearly

✅ **Good:**
```bash
/brainstorm user-authentication-system
/implement shopping-cart-feature
```

❌ **Avoid:**
```bash
/brainstorm feature1
/implement test
```

### Use Consistent Naming

Stick to a naming convention:
- kebab-case: `user-profile-edit`
- snake_case: `user_profile_edit`
- camelCase: `userProfileEdit`

### Check Status Before Implementing

```bash
/req-list  # See what's already defined
```

### Save Work Frequently

Commands may create files or state. Commit to git regularly.

## Troubleshooting

### Command Not Found

**Error:** "Unknown command /xyz"

**Solutions:**
1. Verify plugin is installed: `/plugin list`
2. Check command spelling
3. Review plugin documentation

### Command Fails

**Error:** Command executes but fails

**Solutions:**
1. Check required arguments
2. Review error message
3. Try with --help flag
4. Check plugin documentation

### Unexpected Behavior

**Issue:** Command doesn't do what you expect

**Solutions:**
1. Read command documentation
2. Check argument format
3. Verify prerequisites
4. Try simpler example first

## Next Steps

- **[Use Agents](using-agents.md)** - Working with agents
- **[Use Skills](using-skills.md)** - Leveraging skills
- **[Troubleshooting](troubleshooting.md)** - Solve issues

## Need Help?

- **[FAQ](faq.md)** - Common questions
- **[Plugin Catalog](../plugins/by-category.md)** - See all plugins
