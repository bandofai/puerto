# plugin.json Schema Reference
> Part of the [Reference](index.md).

Complete specification for the `plugin.json` manifest file.

## Location

`.claude-plugin/plugin.json`

## Full Example

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "A comprehensive plugin demonstrating all features",
  "author": {
    "name": "Your Name",
    "email": "you@example.com",
    "url": "https://yoursite.com"
  },
  "keywords": ["keyword1", "keyword2", "keyword3"],
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/user/repo"
  },
  "bugs": {
    "url": "https://github.com/user/repo/issues"
  },
  "homepage": "https://github.com/user/repo#readme"
}
```

## Required Fields

### name

**Type:** `string`
**Required:** Yes
**Pattern:** `^[a-z0-9-]+$`

Plugin identifier. Must be:
- Lowercase
- Alphanumeric with hyphens only
- Unique within Puerto
- Descriptive of functionality

**Examples:**
```json
"name": "frontend-developer"
"name": "api-tester"
"name": "data-scientist"
```

**Invalid:**
```json
"name": "Frontend Developer"  ❌ No spaces
"name": "frontend_dev"         ❌ No underscores
"name": "FrontendDev"          ❌ No uppercase
```

### version

**Type:** `string`
**Required:** Yes
**Pattern:** Semantic versioning (semver)

Plugin version in `MAJOR.MINOR.PATCH` format.

**Examples:**
```json
"version": "1.0.0"    // Initial release
"version": "1.2.3"    // Patch update
"version": "2.0.0"    // Breaking changes
```

**Versioning Rules:**
- **MAJOR** - Breaking changes
- **MINOR** - New features (backward compatible)
- **PATCH** - Bug fixes (backward compatible)

### description

**Type:** `string`
**Required:** Yes
**Max Length:** 200 characters (recommended)

Brief, clear description of plugin functionality.

**Guidelines:**
- ✅ Describe WHAT the plugin does
- ✅ Be concise and specific
- ✅ Mention key features
- ❌ Don't use marketing language
- ❌ Don't include installation instructions

**Examples:**
```json
"description": "Build modern, accessible web interfaces with React and Vue"
"description": "Semantic code navigation with LSP-powered symbol search and editing"
"description": "Track workouts, analyze progress, and detect overtraining"
```

## Recommended Fields

### author

**Type:** `object`
**Recommended:** Yes

Author information. **Must be object**, not string.

**Structure:**
```json
{
  "author": {
    "name": "Your Name",           // Required
    "email": "you@example.com",    // Optional
    "url": "https://yoursite.com"  // Optional
  }
}
```

**Valid:**
```json
"author": {"name": "Band of AI"}
"author": {"name": "John Doe", "email": "john@example.com"}
```

**Invalid:**
```json
"author": "John Doe"  ❌ Must be object, not string
```

### keywords

**Type:** `array<string>`
**Recommended:** Yes

Search keywords for discoverability.

**Guidelines:**
- 3-10 keywords recommended
- Lowercase
- Single words or short phrases
- Include: domain, technology, features

**Example:**
```json
"keywords": [
  "frontend",
  "react",
  "vue",
  "accessibility",
  "components",
  "responsive-design"
]
```

### license

**Type:** `string`
**Recommended:** Yes

Software license identifier.

**Common Values:**
```json
"license": "MIT"
"license": "Apache-2.0"
"license": "GPL-3.0"
"license": "ISC"
```

Use SPDX license identifiers: https://spdx.org/licenses/

## Optional Fields

### repository

**Type:** `object`

Source code repository information.

**Structure:**
```json
{
  "repository": {
    "type": "git",
    "url": "https://github.com/username/repository"
  }
}
```

### bugs

**Type:** `object`

Issue tracker URL.

## Feature Discovery Note

Puerto detects commands, agents, skills, templates, and MCP servers by scanning the plugin directory. You do **not** need to list them inside `plugin.json`. Keep the manifest focused on metadata; maintain supporting assets in their respective folders (`commands/`, `agents/`, `skills/`, `templates/`, `.mcp.json`).

**Structure:**
```json
{
  "bugs": {
    "url": "https://github.com/username/repository/issues"
  }
}
```

### homepage

**Type:** `string`

Plugin documentation or project homepage URL.

**Example:**
```json
"homepage": "https://github.com/username/repository#readme"
```

## Validation Rules

The validation script checks:

✅ **File exists** - `.claude-plugin/plugin.json`
✅ **Valid JSON** - Proper syntax
✅ **Required fields** - name, version, description present
✅ **Name format** - Matches `^[a-z0-9-]+$`
✅ **Version format** - Matches semver pattern
✅ **Author format** - Object with name property (not string)

## Minimal Valid Example

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "A simple plugin for demonstration"
}
```

## Complete Example

```json
{
  "name": "frontend-developer",
  "version": "1.2.0",
  "description": "Build modern, accessible web interfaces with comprehensive component generation and design system integration",
  "author": {
    "name": "Band of AI",
    "email": "hello@bandofai.com",
    "url": "https://bandofai.com"
  },
  "keywords": [
    "frontend",
    "react",
    "vue",
    "angular",
    "accessibility",
    "wcag",
    "responsive-design",
    "components",
    "ui",
    "web-development"
  ],
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/bandofai/puerto"
  },
  "bugs": {
    "url": "https://github.com/bandofai/puerto/issues"
  },
  "homepage": "https://github.com/bandofai/puerto/tree/main/plugins/frontend-developer"
}
```

## Versioning Strategy

### Initial Release

```json
"version": "1.0.0"
```

### Patch Update (Bug fixes)

```json
"version": "1.0.1"  // Fix command error
"version": "1.0.2"  // Update documentation
```

### Minor Update (New features)

```json
"version": "1.1.0"  // Add new command
"version": "1.2.0"  // Add new agent
```

### Major Update (Breaking changes)

```json
"version": "2.0.0"  // Redesign command interface
"version": "3.0.0"  // Remove deprecated features
```

## Common Errors

### Missing Required Field

```
❌ Missing required field in plugin.json: name
```

**Fix:** Add all required fields: name, version, description

### Invalid Name Format

```
❌ Plugin name must be lowercase alphanumeric with hyphens only
```

**Fix:** Use only `a-z`, `0-9`, and `-`
```json
"name": "my-plugin"  ✅
"name": "My Plugin"  ❌
```

### Author is String

```
❌ author must be an object with a "name" property, not a string
```

**Fix:**
```json
"author": {"name": "Your Name"}  ✅
"author": "Your Name"             ❌
```

### Invalid Version

```
⚠️  Version should follow semver format (e.g., 1.0.0)
```

**Fix:** Use `MAJOR.MINOR.PATCH` format
```json
"version": "1.0.0"  ✅
"version": "1.0"    ❌
"version": "v1.0.0" ❌
```

## Testing Your Manifest

### Manual Validation

```bash
# Check JSON syntax
cat .claude-plugin/plugin.json | json_pp
```

### Automated Validation

```bash
# From Puerto root
node scripts/validate-plugin.js path/to/your-plugin/
```

### IDE Validation

Use an IDE with JSON schema support for real-time validation.

## Next Steps

- **[Plugin Structure](../plugin-development/plugin-structure.md)** - File organization
- **[Directory Structure](directory-structure.md)** - Complete layout reference
- **[Validation Rules](validation-rules.md)** - All validation checks
- **[Publishing](../plugin-development/publishing.md)** - Submit your plugin

## See Also

- [marketplace.json Schema](marketplace-json-schema.md) - Marketplace manifest
- [Agent Frontmatter](agent-frontmatter.md) - Agent metadata format
- [Command Format](command-format.md) - Command file format
