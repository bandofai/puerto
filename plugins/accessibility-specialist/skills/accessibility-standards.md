# Accessibility Standards Skill

Comprehensive knowledge of digital accessibility standards, WCAG guidelines, and inclusive design principles.

## WCAG 2.1 Standards

### Level A (Minimum Conformance)

**1.1.1 Non-text Content**
- All non-text content has text alternatives
- Images: alt text describing purpose
- Decorative images: alt="" or role="presentation"
- Complex images: long descriptions (longdesc, aria-describedby)
- Form inputs: associated labels
- Icons: accessible names

**1.2.1 Audio-only and Video-only (Prerecorded)**
- Audio-only: provide transcript
- Video-only: provide transcript or audio description

**1.2.2 Captions (Prerecorded)**
- All prerecorded audio in video has captions
- Includes dialogue, sound effects, speaker identification

**1.2.3 Audio Description or Media Alternative (Prerecorded)**
- Provide audio description OR full text transcript

**1.3.1 Info and Relationships**
- Semantic HTML (headings, lists, tables, forms)
- ARIA landmarks for page regions
- Proper heading hierarchy (h1-h6)
- Table headers with scope attributes
- Form labels explicitly associated

**1.3.2 Meaningful Sequence**
- Reading order matches visual order
- DOM order is logical
- CSS doesn't disrupt reading flow

**1.3.3 Sensory Characteristics**
- Don't rely solely on shape, size, location, orientation, or sound
- Example: "Click the green button on the right" → "Click the Submit button"

**1.4.1 Use of Color**
- Color isn't the only visual means of conveying information
- Use patterns, icons, or text in addition to color
- Example: Required fields marked with * AND color

**1.4.2 Audio Control**
- Audio that plays automatically for >3 seconds has pause/stop control

**2.1.1 Keyboard**
- All functionality available via keyboard
- No keyboard traps
- Tab order is logical

**2.1.2 No Keyboard Trap**
- User can navigate away from any component using standard keys

**2.1.4 Character Key Shortcuts** (2.1 addition)
- If single-character shortcuts exist, can turn off, remap, or only active on focus

**2.2.1 Timing Adjustable**
- User can turn off, adjust, or extend time limits
- Exception: real-time events (auctions)

**2.2.2 Pause, Stop, Hide**
- Moving, blinking, scrolling content >5 seconds can be paused
- Auto-updating content can be paused/hidden

**2.3.1 Three Flashes or Below Threshold**
- Content doesn't flash more than 3 times per second
- Prevents seizures

**2.4.1 Bypass Blocks**
- Skip navigation links or ARIA landmarks
- Allows skipping repeated content

**2.4.2 Page Titled**
- Every page has descriptive <title>

**2.4.3 Focus Order**
- Keyboard focus order preserves meaning and operability

**2.4.4 Link Purpose (In Context)**
- Link purpose clear from link text alone OR link text + context
- Avoid "click here" or "read more" without context

**2.5.1 Pointer Gestures** (2.1 addition)
- Multi-point or path-based gestures have single-pointer alternative

**2.5.2 Pointer Cancellation** (2.1 addition)
- Down-event doesn't execute function (use up-event)
- Prevents accidental activation

**2.5.3 Label in Name** (2.1 addition)
- Visible label text is in accessible name
- Speech input users can activate by speaking visible label

**2.5.4 Motion Actuation** (2.1 addition)
- Functions triggered by motion have UI alternative
- Can disable motion actuation

**3.1.1 Language of Page**
- <html lang="en"> or appropriate language code

**3.2.1 On Focus**
- Focus doesn't trigger unexpected context changes
- No automatic form submission on focus

**3.2.2 On Input**
- Changing form controls doesn't cause unexpected context changes
- Warn before automatic navigation

**3.3.1 Error Identification**
- Input errors identified and described in text

**3.3.2 Labels or Instructions**
- Labels/instructions provided for user input

**4.1.1 Parsing**
- HTML is well-formed (valid start/end tags, unique IDs, proper nesting)

**4.1.2 Name, Role, Value**
- All UI components have accessible name and role
- States/properties communicated to assistive technology
- Use semantic HTML or proper ARIA

### Level AA (Enhanced Conformance)

**1.2.4 Captions (Live)**
- Live audio has captions

**1.2.5 Audio Description (Prerecorded)**
- Audio description for all prerecorded video

**1.3.4 Orientation** (2.1 addition)
- Content doesn't restrict to single orientation (portrait/landscape)
- Exception: specific orientation essential

**1.3.5 Identify Input Purpose** (2.1 addition)
- Input fields that collect user info have autocomplete attributes
- Helps password managers and autofill

**1.4.3 Contrast (Minimum)**
- Text contrast ratio 4.5:1 (18pt+ or bold 14pt+: 3:1)
- Large text: 3:1 minimum
- Exceptions: logos, inactive UI, decorative

**1.4.4 Resize Text**
- Text can be resized to 200% without loss of content/functionality
- Exception: captions and images of text

**1.4.5 Images of Text**
- Use actual text, not images of text
- Exceptions: logos, essential presentation

**1.4.10 Reflow** (2.1 addition)
- Content reflows to 320px width without horizontal scrolling
- Exception: data tables, diagrams, interfaces requiring 2D layout

**1.4.11 Non-text Contrast** (2.1 addition)
- UI components and graphical objects: 3:1 contrast
- Applies to icons, form borders, focus indicators

**1.4.12 Text Spacing** (2.1 addition)
- No loss of content when user adjusts:
  - Line height: 1.5x font size
  - Paragraph spacing: 2x font size
  - Letter spacing: 0.12x font size
  - Word spacing: 0.16x font size

**1.4.13 Content on Hover or Focus** (2.1 addition)
- Tooltips/popups are dismissible, hoverable, persistent
- Don't trap keyboard focus

**2.4.5 Multiple Ways**
- Multiple ways to find pages (nav menu, search, sitemap)

**2.4.6 Headings and Labels**
- Headings and labels are descriptive
- Clearly describe topic or purpose

**2.4.7 Focus Visible**
- Keyboard focus indicator is visible
- Clear visual indication of focus location

**3.1.2 Language of Parts**
- lang attribute for content in different language

**3.2.3 Consistent Navigation**
- Navigation mechanisms in same order across pages

**3.2.4 Consistent Identification**
- Components with same functionality labeled consistently

**3.3.3 Error Suggestion**
- If error detected, provide correction suggestions
- Exception: security/purpose compromise

**3.3.4 Error Prevention (Legal, Financial, Data)**
- Reversible, or verified, or confirmed before submission

**4.1.3 Status Messages** (2.1 addition)
- Status messages communicated to assistive tech without focus change
- Use role="status", role="alert", aria-live

### Level AAA (Optimal Conformance)

**1.2.6 Sign Language (Prerecorded)**
**1.2.7 Extended Audio Description**
**1.2.8 Media Alternative (Prerecorded)**
**1.2.9 Audio-only (Live)**
**1.4.6 Contrast (Enhanced)** - 7:1 ratio
**1.4.8 Visual Presentation** - Width, alignment, line spacing control
**2.1.3 Keyboard (No Exception)**
**2.2.3 No Timing**
**2.2.4 Interruptions**
**2.2.5 Re-authenticating**
**2.2.6 Timeouts** (2.1 addition)
**2.3.2 Three Flashes**
**2.3.3 Animation from Interactions** (2.1 addition)
**2.4.8 Location**
**2.4.9 Link Purpose (Link Only)**
**2.4.10 Section Headings**
**2.5.5 Target Size** (2.1 addition) - 44x44 CSS pixels minimum
**2.5.6 Concurrent Input Mechanisms** (2.1 addition)
**3.1.3 Unusual Words**
**3.1.4 Abbreviations**
**3.1.5 Reading Level**
**3.1.6 Pronunciation**
**3.2.5 Change on Request**
**3.3.5 Help**
**3.3.6 Error Prevention (All)**

## ARIA (Accessible Rich Internet Applications)

### ARIA Landmarks

```html
<header role="banner">          <!-- Site header -->
<nav role="navigation">         <!-- Navigation -->
<main role="main">              <!-- Main content -->
<aside role="complementary">    <!-- Complementary content -->
<footer role="contentinfo">     <!-- Site footer -->
<form role="search">            <!-- Search form -->
<section role="region" aria-labelledby="heading-id">  <!-- General region -->
```

### ARIA Roles

**Document Structure**
- article, definition, directory, document, group, heading, img, list, listitem, math, note, presentation, region, separator, toolbar

**Widget Roles**
- button, checkbox, gridcell, link, menuitem, menuitemcheckbox, menuitemradio, option, progressbar, radio, scrollbar, searchbox, slider, spinbutton, switch, tab, tabpanel, textbox, treeitem

**Composite Widget Roles**
- combobox, grid, listbox, menu, menubar, radiogroup, tablist, tree, treegrid

**Landmark Roles**
- banner, complementary, contentinfo, form, main, navigation, region, search

### ARIA States and Properties

**Widget Attributes**
- aria-autocomplete
- aria-checked (checkbox, radio, switch)
- aria-current (page, step, location, date, time, true, false)
- aria-disabled
- aria-expanded (collapsible content)
- aria-haspopup (menu, listbox, tree, grid, dialog, true, false)
- aria-hidden (true hides from screen readers)
- aria-invalid (grammar, spelling, true, false)
- aria-label (accessible name)
- aria-level (heading level)
- aria-modal (true for modal dialogs)
- aria-multiline (textarea)
- aria-multiselectable (listbox, grid, tree)
- aria-orientation (horizontal, vertical)
- aria-placeholder
- aria-pressed (toggle buttons: true, false, mixed)
- aria-readonly
- aria-required
- aria-selected (tab, option, gridcell)
- aria-sort (ascending, descending, none, other)
- aria-valuemax, aria-valuemin, aria-valuenow, aria-valuetext (range widgets)

**Live Region Attributes**
- aria-live (off, polite, assertive)
- aria-atomic (true: entire region, false: only changes)
- aria-relevant (additions, removals, text, all)
- aria-busy (true during updates)

**Relationship Attributes**
- aria-activedescendant (focus management in composite widgets)
- aria-colcount, aria-colindex (grid columns)
- aria-controls (elements controlled by this element)
- aria-describedby (detailed description)
- aria-details (complex description)
- aria-errormessage (error message ID)
- aria-flowto (reading order override)
- aria-labelledby (label reference)
- aria-owns (parent-child relationship)
- aria-posinset, aria-setsize (position in set)
- aria-rowcount, aria-rowindex (grid rows)

### ARIA Best Practices

1. **First Rule of ARIA**: Don't use ARIA if HTML element exists
   - ❌ `<div role="button">` → ✅ `<button>`
   - ❌ `<div role="navigation">` → ✅ `<nav>`

2. **Don't Override Semantics**
   - ❌ `<h1 role="button">`
   - ✅ `<h1>` or `<button>`

3. **Interactive Elements Need Keyboard Support**
   - role="button" requires Enter/Space handling
   - role="link" requires Enter handling
   - Custom widgets need full keyboard navigation

4. **Don't Use aria-label on <div> or <span>**
   - These have no semantic role
   - Use on interactive/landmark elements

5. **aria-hidden="true" Removes from Accessibility Tree**
   - Use for decorative/duplicate content
   - Don't hide focusable elements
   - Don't hide content users need

## Screen Reader Testing

### Common Screen Readers

**NVDA (Windows)** - Free
- NVDA + Down Arrow: Read next line
- NVDA + Ctrl: Stop speech
- Insert: NVDA modifier key
- Insert + F7: Elements list
- H: Next heading
- K: Next link
- F: Next form field
- T: Next table
- L: Next list

**JAWS (Windows)** - Commercial
- Down Arrow: Read next line
- Insert + Down Arrow: Say all
- Insert: JAWS modifier key
- Insert + F6: Headings list
- Insert + F5: Form fields list
- Insert + F7: Links list
- H: Next heading
- T: Next table

**VoiceOver (macOS/iOS)**
- VO = Control + Option
- VO + Right Arrow: Next item
- VO + Cmd + H: Next heading
- VO + Cmd + L: Next link
- VO + Space: Activate
- VO + A: Read all
- VO + U: Rotor (elements list)

**TalkBack (Android)**
- Swipe right: Next item
- Swipe left: Previous item
- Double-tap: Activate
- Local context menu: Swipe up then right
- Global context menu: Swipe down then right

### Testing Checklist

- [ ] Navigate page with keyboard only (Tab, Shift+Tab, Enter, Space, Arrows)
- [ ] Check focus indicators are visible
- [ ] Navigate with screen reader (headings, links, forms, landmarks)
- [ ] Verify all images have appropriate alt text
- [ ] Check form labels are associated and read correctly
- [ ] Test error messages are announced
- [ ] Verify dynamic content updates are announced
- [ ] Check modals trap focus and can be closed
- [ ] Test skip links work
- [ ] Verify tables have headers and relationships
- [ ] Check video captions and transcripts
- [ ] Test zoom to 200% without loss
- [ ] Test with high contrast mode
- [ ] Test with custom colors/dark mode

## Common Accessibility Patterns

### Button

```html
<!-- Standard button -->
<button type="button">Click Me</button>

<!-- Icon button -->
<button type="button" aria-label="Close dialog">
  <svg aria-hidden="true" focusable="false"><use xlink:href="#close-icon"/></svg>
</button>

<!-- Toggle button -->
<button type="button" aria-pressed="false">Mute</button>
```

### Links

```html
<!-- Standard link -->
<a href="/about">About Us</a>

<!-- Link with context -->
<a href="/product-1">
  View details
  <span class="sr-only">for Product 1</span>
</a>

<!-- External link -->
<a href="https://example.com" rel="external">
  External site
  <svg aria-label="(opens in new window)"><use xlink:href="#external-icon"/></svg>
</a>
```

### Forms

```html
<!-- Text input -->
<label for="email">Email address</label>
<input
  type="email"
  id="email"
  name="email"
  aria-required="true"
  aria-describedby="email-hint"
  autocomplete="email"
/>
<small id="email-hint">We'll never share your email.</small>

<!-- Error state -->
<input
  type="email"
  id="email"
  aria-invalid="true"
  aria-describedby="email-error"
/>
<span id="email-error" role="alert">Please enter a valid email address.</span>

<!-- Checkbox -->
<input type="checkbox" id="agree" name="agree">
<label for="agree">I agree to the terms</label>

<!-- Radio group -->
<fieldset>
  <legend>Shipping method</legend>
  <input type="radio" id="standard" name="shipping" value="standard">
  <label for="standard">Standard (5-7 days)</label>

  <input type="radio" id="express" name="shipping" value="express">
  <label for="express">Express (2-3 days)</label>
</fieldset>
```

### Modal Dialog

```html
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-desc"
>
  <h2 id="dialog-title">Confirm deletion</h2>
  <p id="dialog-desc">Are you sure you want to delete this item?</p>
  <button type="button">Cancel</button>
  <button type="button">Delete</button>
</div>
```

**JavaScript Requirements:**
- Trap focus within dialog
- Focus first interactive element on open
- Return focus to trigger on close
- Close on Esc key
- Prevent background scroll

### Tab Panel

```html
<div class="tabs">
  <div role="tablist" aria-label="Settings">
    <button role="tab" aria-selected="true" aria-controls="panel-1" id="tab-1">
      Profile
    </button>
    <button role="tab" aria-selected="false" aria-controls="panel-2" id="tab-2" tabindex="-1">
      Security
    </button>
    <button role="tab" aria-selected="false" aria-controls="panel-3" id="tab-3" tabindex="-1">
      Notifications
    </button>
  </div>

  <div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
    Profile content...
  </div>
  <div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>
    Security content...
  </div>
  <div role="tabpanel" id="panel-3" aria-labelledby="tab-3" hidden>
    Notifications content...
  </div>
</div>
```

**Keyboard Support:**
- Tab: Focus tab list (first or selected tab)
- Arrow Left/Right: Navigate between tabs
- Home/End: First/last tab
- Space/Enter: Activate tab

### Accordion

```html
<div class="accordion">
  <h3>
    <button
      type="button"
      aria-expanded="true"
      aria-controls="section-1"
      id="accordion-1"
    >
      Section 1 Title
    </button>
  </h3>
  <div id="section-1" role="region" aria-labelledby="accordion-1">
    Section 1 content...
  </div>
</div>
```

### Skip Link

```html
<a href="#main" class="skip-link">Skip to main content</a>
...
<main id="main">
  Main content...
</main>

<style>
.skip-link {
  position: absolute;
  left: -10000px;
  width: 1px;
  height: 1px;
  overflow: hidden;
}

.skip-link:focus {
  position: static;
  width: auto;
  height: auto;
}
</style>
```

### Alert/Status Messages

```html
<!-- Error alert -->
<div role="alert">
  Form submission failed. Please try again.
</div>

<!-- Status message (non-urgent) -->
<div role="status" aria-live="polite">
  3 items added to cart
</div>

<!-- Assertive announcement (urgent) -->
<div role="alert" aria-live="assertive" aria-atomic="true">
  Connection lost. Reconnecting...
</div>
```

## Tools & Resources

### Automated Testing Tools

- **axe DevTools** (Browser extension) - Most accurate
- **WAVE** (WebAIM) - Visual feedback
- **Lighthouse** (Chrome DevTools) - Built-in auditing
- **Pa11y** (CLI) - CI/CD integration
- **axe-core** (Library) - JavaScript API
- **jest-axe** - Jest integration
- **cypress-axe** - Cypress integration

### Manual Testing Tools

- **Color Contrast Analyzer** - Luminosity contrast
- **HeadingsMap** - Heading structure visualization
- **Accessibility Insights** - Microsoft's comprehensive tool
- **Screen Reader** - NVDA, JAWS, VoiceOver, TalkBack
- **Keyboard Only** - No mouse/trackpad

### Documentation

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [WebAIM Articles](https://webaim.org/articles/)
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [Inclusive Components](https://inclusive-components.design/)
- [A11Y Project](https://www.a11yproject.com/)

## Accessibility Statement Template

```markdown
# Accessibility Statement for [Site Name]

We are committed to ensuring digital accessibility for people with disabilities. We are continually improving the user experience for everyone and applying the relevant accessibility standards.

## Conformance Status

The Web Content Accessibility Guidelines (WCAG) defines requirements for designers and developers to improve accessibility for people with disabilities. It defines three levels of conformance: Level A, Level AA, and Level AAA. [Site Name] is [fully conformant/partially conformant/non-conformant] with WCAG 2.1 level AA.

## Feedback

We welcome your feedback on the accessibility of [Site Name]. Please let us know if you encounter accessibility barriers:

- Email: accessibility@example.com
- Phone: [Number]

We try to respond to feedback within [X business days].

## Date

This statement was created on [Date] and last reviewed on [Date].
```

---

*This skill provides comprehensive accessibility knowledge for building inclusive digital experiences.*
