# Adding Templates
> Part of the [Plugin Development Guide](index.md).

Templates give users ready-made files they can drop into a project—component stubs, checklists, configuration files, and more. They pair perfectly with commands and agents that scaffold projects.

---

## Directory Layout

```
plugins/<your-plugin>/
└── templates/
    ├── component-template.tsx
    ├── css-module-template.module.css
    └── accessibility-checklist.md
```

Declare templates in `plugin.json` so Puerto can index and expose them:

```json
{
  "templates": [
    {
      "name": "component-template",
      "file": "templates/component-template.tsx",
      "description": "TypeScript React component with accessibility hooks"
    },
    {
      "name": "accessibility-checklist",
      "file": "templates/accessibility-checklist.md",
      "description": "WCAG 2.1 AA validation worksheet"
    }
  ]
}
```

- `name` is the slug shown to users.
- `file` is the relative path inside the plugin.
- `description` provides a quick summary (≤ 120 characters recommended).

---

## Crafting Effective Templates

1. **Start from production-ready patterns**  
   Ship best practices—linting configs, ADR skeletons, service blueprints, etc.

2. **Keep placeholders explicit**  
   Use tokens like `{{PROJECT_NAME}}` or `// TODO: Fill in ...` to signal required edits.

3. **Add inline guidance**  
   Short comments or docstrings help users understand why something exists.

4. **Match directory structure**  
   Mimic where the file should live in a project. For example, place component scaffolds under `templates/components/Button.tsx`.

5. **Provide companion docs**  
   Reference skills or README sections that explain how to use the template.

---

## Example Template (Excerpt)

```tsx
// templates/component-template.tsx
import React from 'react';
import styles from './{{COMPONENT_NAME}}.module.css';

/**
 * {{COMPONENT_NAME}} - Brief description.
 *
 * @example
 * ```tsx
 * <{{COMPONENT_NAME}} />
 * ```
 */
export function {{COMPONENT_NAME}}() {
  return (
    <div className={styles.container} role="region" aria-label="{{COMPONENT_NAME}} component">
      {/* TODO: Implement component */}
    </div>
  );
}
```

```css
/* templates/css-module-template.module.css */
.container {
  display: flex;
  width: 100%;
  gap: 1rem;
}
```

---

## Distribution Patterns

- **Command-driven scaffolding**  
  Commands can copy templates into the project (`cp templates/... ./src/...`) and then customise them.

- **Agent augmentation**  
  Agents may start from a template, adjust for the task, and explain the differences in their report.

- **Skill references**  
  Skills can reference templates. For example, instruct readers to use `templates/accessibility-checklist.md` before sign-off.

Document these interactions in your plugin README so users know how to trigger template usage.

---

## Quality Checklist

- Template files compile or render (when applicable).
- Placeholders are obvious and documented.
- `plugin.json` paths match actual file locations.
- Templates respect project conventions ( formatting, naming).
- README includes usage instructions or example commands.

---

## Next Steps

- Combine templates with automation in [Commands](commands.md) or [Agents](agents.md).
- Validate file paths using the [Testing & Validation](testing-and-validation.md) workflow.
- Reference templates in [Plugin Manifest](plugin-manifest.md) to keep metadata in sync.
