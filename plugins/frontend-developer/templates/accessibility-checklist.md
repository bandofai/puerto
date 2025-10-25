# Accessibility Validation Checklist

**WCAG 2.1 Level AA Compliance**

Use this checklist to ensure your component meets accessibility standards before deployment.

---

## Perceivable

### 1.1 Text Alternatives

- [ ] All `<img>` elements have `alt` attributes
- [ ] Decorative images use `alt=""` or `role="presentation"`
- [ ] Complex images (charts, diagrams) have detailed descriptions
- [ ] Icon buttons have accessible labels (`aria-label` or visible text)
- [ ] Form inputs have associated labels
- [ ] `<svg>` icons have `<title>` or `aria-label`

### 1.3 Adaptable

- [ ] Semantic HTML elements used (`<header>`, `<nav>`, `<main>`, `<footer>`, `<article>`, `<section>`)
- [ ] Heading hierarchy is correct (h1 → h2 → h3, no skipping levels)
- [ ] Form labels explicitly associated with inputs (`htmlFor`/`id` or wrapping)
- [ ] Tables have `<th>` elements with `scope` attribute
- [ ] Lists use proper markup (`<ul>`, `<ol>`, `<li>`)
- [ ] Content order makes sense without CSS

### 1.4 Distinguishable

- [ ] Text color contrast ≥ 4.5:1 (normal text) [Check: https://webaim.org/resources/contrastchecker/]
- [ ] Large text (18pt+) contrast ≥ 3:1
- [ ] UI component contrast ≥ 3:1 (buttons, borders, focus indicators)
- [ ] Information not conveyed by color alone
- [ ] Text can be resized to 200% without horizontal scrolling
- [ ] No images of text (use actual text with CSS styling)
- [ ] Audio/video has captions or transcripts

---

## Operable

### 2.1 Keyboard Accessible

- [ ] All interactive elements accessible via keyboard (Tab, Enter, Space)
- [ ] No keyboard traps (can always move focus away)
- [ ] Tab order is logical
- [ ] Custom widgets have proper keyboard support (arrow keys, Escape, etc.)
- [ ] Skip links provided to skip navigation
- [ ] Keyboard shortcuts don't conflict with assistive technologies

### 2.2 Enough Time

- [ ] No time limits, or user can extend/disable them
- [ ] Auto-playing content can be paused/stopped
- [ ] Session timeouts have warnings and can be extended

### 2.4 Navigable

- [ ] Page has descriptive `<title>`
- [ ] Focus order is logical and predictable
- [ ] Links have descriptive text (not "click here" or "read more")
- [ ] Multiple ways to navigate (menu, search, sitemap)
- [ ] Headings describe content sections
- [ ] Current page/location is indicated

### 2.5 Input Modalities

- [ ] Touch targets ≥ 44×44 pixels (mobile)
- [ ] Touch targets have adequate spacing (≥ 8px gap)
- [ ] No motion-only activation (shake to undo, tilt to scroll)
- [ ] Pointer cancellation available (can abort action by moving away)

---

## Understandable

### 3.1 Readable

- [ ] Page language specified (`<html lang="en">`)
- [ ] Language changes marked (`<span lang="es">`)
- [ ] Reading level appropriate for content (or simplified version available)
- [ ] Unusual words/jargon defined or avoided

### 3.2 Predictable

- [ ] Navigation is consistent across pages
- [ ] Repeated components appear in same order
- [ ] Focus doesn't trigger unexpected context changes
- [ ] Input doesn't trigger unexpected context changes (no auto-submit)
- [ ] Components behave consistently throughout site

### 3.3 Input Assistance

- [ ] Form errors clearly identified
- [ ] Labels or instructions provided for all inputs
- [ ] Error messages suggest how to fix the error
- [ ] Confirmation required for legal/financial actions
- [ ] Form data can be reviewed before submission

---

## Robust

### 4.1 Compatible

- [ ] Valid HTML (no duplicate IDs, proper nesting)
- [ ] ARIA roles used correctly (when semantic HTML isn't sufficient)
- [ ] ARIA states and properties valid
- [ ] Status messages announced to screen readers (`role="status"`, `aria-live`)
- [ ] Dynamic content changes announced appropriately
- [ ] Custom widgets have proper ARIA attributes

---

## Focus Indicators

- [ ] All interactive elements have visible focus indicators
- [ ] Focus indicators have sufficient contrast (3:1 minimum)
- [ ] Focus indicators not removed with `outline: none` (or custom visible alternative provided)
- [ ] `:focus-visible` used to differentiate mouse vs keyboard focus (optional)

---

## Forms

- [ ] Labels visible and associated with inputs
- [ ] Required fields indicated (not by color alone)
- [ ] Error messages specific and helpful
- [ ] Success messages announced to screen readers
- [ ] Inline validation doesn't interfere with form completion
- [ ] Autocomplete attributes used where appropriate
- [ ] Instructions provided before fields (not just placeholder text)

---

## Dynamic Content

- [ ] Loading states announced (`role="status"`, `aria-busy`)
- [ ] Error alerts announced (`role="alert"`)
- [ ] Live regions used appropriately (`aria-live="polite"` or `aria-live="assertive"`)
- [ ] Focus managed when content changes (modals, route changes)
- [ ] Infinite scroll has keyboard alternative

---

## Media

- [ ] Videos have captions
- [ ] Audio has transcripts
- [ ] Media players have keyboard controls
- [ ] Auto-playing media can be paused
- [ ] Flashing content doesn't exceed 3 flashes per second

---

## Testing Tools

**Automated Tools** (catch ~30% of issues):
- [ ] axe DevTools (browser extension)
- [ ] WAVE Evaluation Tool
- [ ] Lighthouse Accessibility audit
- [ ] jest-axe (in tests)

**Manual Testing** (required):
- [ ] Keyboard-only navigation tested
- [ ] Screen reader tested (NVDA/JAWS on Windows, VoiceOver on Mac/iOS, TalkBack on Android)
- [ ] Zoom to 200% tested (content still visible and usable)
- [ ] Color blindness simulation tested
- [ ] Reduced motion preference tested

**User Testing** (gold standard):
- [ ] Real users with disabilities have tested the application

---

## Quick Reference

### Minimum Contrast Ratios
- Normal text (< 18pt): **4.5:1** (WCAG AA)
- Large text (≥ 18pt or ≥ 14pt bold): **3:1** (WCAG AA)
- UI components (buttons, borders, focus): **3:1** (WCAG AA)

### Minimum Touch Targets
- Mobile: **44×44 pixels** (iOS/Android guidelines)
- Desktop: **24×24 pixels** minimum (larger is better)

### Common ARIA Roles
- `role="button"` - Custom button
- `role="dialog"` - Modal
- `role="navigation"` - Navigation section
- `role="search"` - Search form
- `role="alert"` - Important alert
- `role="status"` - Status message
- `role="tablist"`, `role="tab"`, `role="tabpanel"` - Tabs

### Common ARIA Attributes
- `aria-label` - Accessible name
- `aria-labelledby` - References label element
- `aria-describedby` - Additional description
- `aria-expanded` - Collapsed/expanded state
- `aria-hidden` - Hide from screen readers
- `aria-live` - Announce dynamic changes
- `aria-modal` - Modal dialog

---

## Resources

- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [Inclusive Components](https://inclusive-components.design/)

---

**Remember**: Accessibility is not optional. It's a legal requirement in many jurisdictions and, more importantly, it's the right thing to do to ensure everyone can use your application.

**Version**: 1.0
**Standard**: WCAG 2.1 Level AA
**Last Updated**: January 2025
