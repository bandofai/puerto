# Accessibility Standards

**WCAG 2.1 Level AA compliance patterns and best practices**

## Core Principles

### 1. Perceivable
- Provide text alternatives for non-text content
- Provide captions and transcripts for multimedia
- Create content that can be presented in different ways
- Make it easier for users to see and hear content

### 2. Operable
- Make all functionality available from keyboard
- Give users enough time to read and use content
- Do not design content that causes seizures
- Help users navigate and find content

### 3. Understandable
- Make text readable and understandable
- Make content appear and operate in predictable ways
- Help users avoid and correct mistakes

### 4. Robust
- Maximize compatibility with current and future tools

## Implementation Patterns

### Semantic HTML
```html
<!-- ❌ BAD -->
<div onClick=handleClick>Click me</div>

<!-- ✅ GOOD -->
<button onClick={handleClick}>Click me</button>
```

### ARIA Labels
```html
<button aria-label="Close modal" onClick={onClose}>
  <XIcon />
</button>
```

### Keyboard Navigation
- Tab order should be logical
- Focus indicators must be visible
- All interactive elements accessible via keyboard
- Escape key closes modals/menus

### Color Contrast
- Normal text: 4.5:1 minimum
- Large text (18pt+): 3:1 minimum
- Interactive elements: 3:1 minimum

### Screen Reader Support
- Use proper heading hierarchy (h1-h6)
- Provide skip links
- Label form inputs properly
- Use live regions for dynamic content

## Testing Tools

- axe DevTools
- Pa11y
- Lighthouse
- NVDA/JAWS screen readers
- Keyboard-only navigation testing

## Common Patterns

### Accessible Forms
```tsx
<label htmlFor="email">
  Email Address
  <input
    id="email"
    type="email"
    aria-required="true"
    aria-describedby="email-error"
  />
</label>
{error && (
  <span id="email-error" role="alert">
    {error}
  </span>
)}
```

### Accessible Modals
```tsx
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
>
  <h2 id="dialog-title">Modal Title</h2>
  {/* Trap focus within modal */}
  {/* Close on Escape */}
</div>
```

### Accessible Tables
```html
<table>
  <caption>Monthly Sales Data</caption>
  <thead>
    <tr>
      <th scope="col">Month</th>
      <th scope="col">Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">January</th>
      <td>0,000</td>
    </tr>
  </tbody>
</table>
```

## Checklist

- [ ] Keyboard navigation works
- [ ] Screen reader announces content properly
- [ ] Color contrast meets requirements
- [ ] Focus indicators visible
- [ ] Form labels present and associated
- [ ] Headings in logical order
- [ ] Alternative text for images
- [ ] ARIA used correctly (not overused)
- [ ] Error messages clear and accessible
- [ ] No keyboard traps

