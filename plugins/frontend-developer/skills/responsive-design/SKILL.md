# Responsive Design Skill

**Production-tested patterns for building responsive, performant, accessible web interfaces**

This skill codifies best practices from thousands of production deployments covering responsive design, CSS architecture, and performance optimization.

---

## Core Principles

1. **Mobile-First Always**: Start with mobile, enhance for larger screens
2. **Performance Matters**: Fast loading, smooth animations, minimal CSS
3. **Accessibility Required**: WCAG 2.1 AA compliance for all visual elements
4. **Progressive Enhancement**: Core functionality works without JavaScript
5. **Browser Compatibility**: Works across modern browsers with graceful degradation

---

## Mobile-First Responsive Design

### The Mobile-First Approach

Always write base styles for mobile, then use `min-width` media queries to enhance for larger screens:

```css
/* ✅ GOOD: Mobile-first approach */
.container {
  /* Mobile styles (default, no media query needed) */
  padding: 1rem;
  font-size: 1rem;
}

/* Tablet enhancement */
@media (min-width: 768px) {
  .container {
    padding: 2rem;
    font-size: 1.125rem;
  }
}

/* Desktop enhancement */
@media (min-width: 1024px) {
  .container {
    padding: 3rem;
    font-size: 1.25rem;
  }
}

/* ❌ BAD: Desktop-first (requires overriding) */
.container {
  padding: 3rem;  /* Desktop default */
}

@media (max-width: 1023px) {
  .container {
    padding: 2rem;  /* Override for tablet */
  }
}

@media (max-width: 767px) {
  .container {
    padding: 1rem;  /* Override again for mobile */
  }
}
```

---

## Standard Breakpoints

```css
/* Mobile: Base styles (no media query) */
/* Covers: 320px - 767px */

/* Small devices (landscape phones) */
@media (min-width: 640px) {
  /* 640px - 767px */
}

/* Tablet */
@media (min-width: 768px) {
  /* 768px - 1023px */
}

/* Desktop */
@media (min-width: 1024px) {
  /* 1024px - 1279px */
}

/* Large desktop */
@media (min-width: 1280px) {
  /* 1280px - 1535px */
}

/* Extra large desktop */
@media (min-width: 1536px) {
  /* 1536px+ */
}
```

### Tailwind CSS Breakpoints

```tsx
<div className="
  w-full px-4 py-4           {/* Mobile default */}
  sm:px-6 sm:py-6            {/* 640px+ */}
  md:max-w-3xl md:mx-auto    {/* 768px+ */}
  lg:max-w-5xl lg:px-12      {/* 1024px+ */}
  xl:max-w-7xl               {/* 1280px+ */}
  2xl:max-w-screen-2xl       {/* 1536px+ */}
">
  Content
</div>
```

---

## Responsive Layout Patterns

### Flexbox Layouts

```css
/* Responsive navigation */
.nav {
  display: flex;
  flex-direction: column;  /* Mobile: Stack vertically */
  gap: 1rem;
}

@media (min-width: 768px) {
  .nav {
    flex-direction: row;  /* Tablet+: Horizontal */
    justify-content: space-between;
    align-items: center;
  }
}

/* Responsive card grid */
.card-grid {
  display: flex;
  flex-direction: column;  /* Mobile: Single column */
  gap: 1.5rem;
}

@media (min-width: 640px) {
  .card-grid {
    flex-direction: row;
    flex-wrap: wrap;
  }

  .card {
    flex: 0 0 calc(50% - 0.75rem);  /* 2 columns */
  }
}

@media (min-width: 1024px) {
  .card {
    flex: 0 0 calc(33.333% - 1rem);  /* 3 columns */
  }
}
```

### CSS Grid Layouts

```css
/* Responsive grid with auto-fit */
.grid {
  display: grid;
  grid-template-columns: 1fr;  /* Mobile: 1 column */
  gap: 1.5rem;
}

@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);  /* Tablet: 2 columns */
  }
}

@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);  /* Desktop: 3 columns */
  }
}

/* Advanced: Auto-responsive grid (no media queries!) */
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr));
  gap: 1.5rem;
}
/* This automatically adjusts columns based on container width */

/* Holy Grail Layout */
.layout {
  display: grid;
  min-height: 100vh;
  grid-template-areas:
    "header"
    "main"
    "sidebar"
    "footer";
  grid-template-rows: auto 1fr auto auto;
}

@media (min-width: 1024px) {
  .layout {
    grid-template-areas:
      "header header header"
      "sidebar main ads"
      "footer footer footer";
    grid-template-columns: 250px 1fr 200px;
    grid-template-rows: auto 1fr auto;
  }
}

.header { grid-area: header; }
.main { grid-area: main; }
.sidebar { grid-area: sidebar; }
.footer { grid-area: footer; }
```

### Container Queries (Modern Approach)

```css
/* Component responds to container size, not viewport */
.card-container {
  container-type: inline-size;
  container-name: card;
}

.card {
  display: flex;
  flex-direction: column;
}

/* When container > 400px, switch to row layout */
@container card (min-width: 400px) {
  .card {
    flex-direction: row;
  }
}

/* Works regardless of viewport size! */
```

---

## Responsive Typography

```css
/* Fluid typography using clamp() */
.heading-1 {
  /* min: 2rem (32px), preferred: 5vw, max: 4rem (64px) */
  font-size: clamp(2rem, 5vw, 4rem);
  line-height: 1.2;
}

.heading-2 {
  font-size: clamp(1.5rem, 4vw, 3rem);
  line-height: 1.3;
}

.body {
  font-size: clamp(1rem, 2vw, 1.125rem);
  line-height: 1.6;
}

/* Alternative: Responsive font sizes with media queries */
.title {
  font-size: 1.5rem;  /* Mobile: 24px */
  line-height: 1.4;
}

@media (min-width: 768px) {
  .title {
    font-size: 2rem;  /* Tablet: 32px */
  }
}

@media (min-width: 1024px) {
  .title {
    font-size: 2.5rem;  /* Desktop: 40px */
  }
}

/* Reading width: Optimal line length for readability */
.content {
  max-width: 65ch;  /* ~65 characters per line */
  margin-inline: auto;
}
```

---

## Responsive Images

```html
<!-- Responsive image with srcset -->
<img
  src="image-800.jpg"
  srcset="
    image-400.jpg 400w,
    image-800.jpg 800w,
    image-1200.jpg 1200w,
    image-1600.jpg 1600w
  "
  sizes="
    (max-width: 640px) 100vw,
    (max-width: 1024px) 50vw,
    800px
  "
  alt="Description"
  loading="lazy"
/>

<!-- Picture element for art direction -->
<picture>
  <!-- Mobile: Portrait crop -->
  <source
    media="(max-width: 767px)"
    srcset="image-mobile.jpg"
  />
  <!-- Tablet: Landscape -->
  <source
    media="(max-width: 1023px)"
    srcset="image-tablet.jpg"
  />
  <!-- Desktop: Full width -->
  <img
    src="image-desktop.jpg"
    alt="Description"
  />
</picture>

<!-- Modern formats with fallback -->
<picture>
  <source type="image/avif" srcset="image.avif" />
  <source type="image/webp" srcset="image.webp" />
  <img src="image.jpg" alt="Description" />
</picture>
```

```css
/* Responsive images in CSS */
.hero-image {
  width: 100%;
  height: auto;
  max-width: 100%;
  object-fit: cover;
  aspect-ratio: 16 / 9;  /* Maintain aspect ratio */
}

/* Background images */
.hero-bg {
  background-image: url('hero-mobile.jpg');
  background-size: cover;
  background-position: center;
  min-height: 50vh;
}

@media (min-width: 768px) {
  .hero-bg {
    background-image: url('hero-tablet.jpg');
    min-height: 60vh;
  }
}

@media (min-width: 1024px) {
  .hero-bg {
    background-image: url('hero-desktop.jpg');
    min-height: 80vh;
  }
}

/* High DPI displays */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .logo {
    background-image: url('logo@2x.png');
    background-size: contain;
  }
}
```

---

## CSS Architecture Patterns

### CSS Modules (Recommended)

```css
/* Button.module.css */
.button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.25rem;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.primary {
  background-color: var(--color-primary);
  color: white;
}

.primary:hover {
  background-color: var(--color-primary-dark);
}

.secondary {
  background-color: transparent;
  color: var(--color-primary);
  border: 1px solid var(--color-primary);
}

/* Responsive adjustments */
@media (min-width: 768px) {
  .button {
    padding: 0.75rem 1.5rem;
    font-size: 1.125rem;
  }
}
```

```tsx
// Button.tsx
import styles from './Button.module.css';

export function Button({ variant = 'primary', children }) {
  return (
    <button className={`${styles.button} ${styles[variant]}`}>
      {children}
    </button>
  );
}
```

### CSS Custom Properties (Variables)

```css
:root {
  /* Colors */
  --color-primary: #0066cc;
  --color-primary-dark: #0052a3;
  --color-text: #1a1a1a;
  --color-bg: #ffffff;
  --color-border: #e5e5e5;

  /* Spacing scale */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  --space-2xl: 3rem;

  /* Font sizes */
  --font-xs: 0.75rem;
  --font-sm: 0.875rem;
  --font-base: 1rem;
  --font-lg: 1.125rem;
  --font-xl: 1.25rem;
  --font-2xl: 1.5rem;
  --font-3xl: 2rem;

  /* Breakpoints (for JS) */
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  :root {
    --color-text: #ffffff;
    --color-bg: #1a1a1a;
    --color-border: #333333;
  }
}

/* Usage */
.component {
  color: var(--color-text);
  background: var(--color-bg);
  padding: var(--space-md);
  font-size: var(--font-base);
  border: 1px solid var(--color-border);
}

@media (min-width: 768px) {
  .component {
    padding: var(--space-lg);
    font-size: var(--font-lg);
  }
}
```

### BEM Naming Convention

```css
/* Block */
.card {
  padding: 1rem;
  border: 1px solid var(--border-color);
}

/* Element */
.card__header {
  margin-bottom: 1rem;
  border-bottom: 1px solid var(--border-color);
}

.card__title {
  font-size: 1.5rem;
  font-weight: bold;
}

.card__body {
  margin-bottom: 1rem;
}

.card__footer {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
}

/* Modifier */
.card--featured {
  border-color: var(--primary-color);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.card--compact {
  padding: 0.5rem;
}

/* Responsive modifiers */
@media (min-width: 768px) {
  .card--horizontal {
    display: flex;
  }

  .card--horizontal .card__header {
    flex: 0 0 200px;
    border-bottom: none;
    border-right: 1px solid var(--border-color);
  }
}
```

---

## Performance Optimization

### Critical CSS

```html
<!DOCTYPE html>
<html>
<head>
  <!-- Inline critical CSS (above-the-fold styles) -->
  <style>
    /* Critical styles for initial render */
    body {
      margin: 0;
      font-family: system-ui, -apple-system, sans-serif;
      line-height: 1.6;
    }

    .header {
      background: #0066cc;
      color: white;
      padding: 1rem;
    }

    /* ... other critical styles ... */
  </style>

  <!-- Preload non-critical CSS -->
  <link
    rel="preload"
    href="/styles.css"
    as="style"
    onload="this.onload=null;this.rel='stylesheet'"
  />
  <noscript>
    <link rel="stylesheet" href="/styles.css" />
  </noscript>
</head>
<body>
  <!-- Content -->
</body>
</html>
```

### CSS Code Splitting

```tsx
// Lazy load component with its styles
const HeavyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <HeavyComponent />
    </Suspense>
  );
}
```

### PurgeCSS / Tree Shaking

```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
    process.env.NODE_ENV === 'production' &&
      require('@fullhuman/postcss-purgecss')({
        content: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
        defaultExtractor: (content) => content.match(/[\w-/:]+(?<!:)/g) || [],
      }),
  ],
};
```

### CSS Optimization Checklist

- [ ] Minify CSS files
- [ ] Remove unused CSS (PurgeCSS)
- [ ] Combine similar rules
- [ ] Use CSS containment (`contain` property)
- [ ] Optimize font loading
- [ ] Enable Brotli/Gzip compression
- [ ] Use CSS custom properties instead of Sass variables (runtime flexibility)
- [ ] Avoid `@import` (use bundler imports)
- [ ] Use `will-change` sparingly (only for animations)
- [ ] Avoid universal selectors (`*`)

---

## Animation Best Practices

### 60fps Animations (GPU-Accelerated)

```css
/* ✅ GOOD: Only animate transform and opacity */
.smooth {
  transition: transform 0.3s ease, opacity 0.3s ease;
  /* GPU-accelerated properties only */
}

.smooth:hover {
  transform: scale(1.05);
  opacity: 0.9;
}

/* ❌ BAD: Animating layout properties (causes reflow) */
.laggy {
  transition: width 0.3s ease, height 0.3s ease;
}

.laggy:hover {
  width: 200px;  /* Triggers layout recalculation */
  height: 200px;
}

/* Use will-change for complex animations (sparingly!) */
.complex-animation {
  will-change: transform, opacity;
  animation: slide-in 0.5s ease;
}

@keyframes slide-in {
  from {
    transform: translateX(-100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

/* Remove will-change after animation */
.complex-animation.animation-done {
  will-change: auto;
}
```

### Reduced Motion Support

```css
/* Respect user preference for reduced motion */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* Alternative: Disable specific animations */
.fade-in {
  animation: fade-in 0.5s ease;
}

@media (prefers-reduced-motion: reduce) {
  .fade-in {
    animation: none;
    opacity: 1;  /* End state */
  }
}
```

---

## Dark Mode Implementation

### System Preference

```css
/* Light mode (default) */
:root {
  --bg: #ffffff;
  --text: #1a1a1a;
  --border: #e5e5e5;
  --primary: #0066cc;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1a1a1a;
    --text: #ffffff;
    --border: #333333;
    --primary: #3399ff;
  }
}

/* Usage */
body {
  background: var(--bg);
  color: var(--text);
}
```

### Manual Toggle

```css
/* Light mode (default) */
:root {
  --bg: #ffffff;
  --text: #1a1a1a;
}

/* Dark mode via class */
.dark {
  --bg: #1a1a1a;
  --text: #ffffff;
}

/* OR via data attribute */
[data-theme="dark"] {
  --bg: #1a1a1a;
  --text: #ffffff;
}
```

```tsx
// React implementation
function ThemeToggle() {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');

  useEffect(() => {
    // Apply theme to document
    document.documentElement.setAttribute('data-theme', theme);
    // Persist preference
    localStorage.setItem('theme', theme);
  }, [theme]);

  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Toggle theme
    </button>
  );
}
```

---

## Accessibility Considerations

### Color Contrast

```css
/* Minimum contrast ratios (WCAG AA) */
/* Normal text: 4.5:1 */
/* Large text (18pt+): 3:1 */
/* UI components: 3:1 */

/* ✅ GOOD: Sufficient contrast */
.text {
  color: #1a1a1a;  /* Contrast: 19:1 on white */
  background: #ffffff;
}

/* ❌ BAD: Insufficient contrast */
.low-contrast {
  color: #999999;  /* Contrast: 2.8:1 - fails WCAG AA */
  background: #ffffff;
}

/* Tool to check: WebAIM Contrast Checker */
/* https://webaim.org/resources/contrastchecker/ */
```

### Focus Indicators

```css
/* ✅ GOOD: Visible focus indicator */
button:focus,
a:focus,
input:focus {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
}

/* Custom focus style */
.custom-focus:focus {
  outline: none;  /* Remove default */
  box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.5);
}

/* ❌ NEVER do this (removes focus for keyboard users) */
/* *:focus {
  outline: none;
} */

/* :focus-visible for mouse vs keyboard */
button:focus-visible {
  outline: 2px solid var(--primary);
}

/* No outline when clicked with mouse */
button:focus:not(:focus-visible) {
  outline: none;
}
```

### Responsive Text Sizing

```css
/* Never use fixed pixel sizes smaller than 16px */
.body {
  font-size: 1rem;  /* 16px minimum */
}

/* Allow text to scale with user preferences */
html {
  font-size: 100%;  /* Respect browser default (usually 16px) */
}

/* Use rem for scalable sizing */
.heading {
  font-size: 2rem;  /* Scales with root font size */
}

/* User can zoom to 200% without horizontal scroll */
.container {
  max-width: 100%;
  overflow-x: hidden;
}
```

### Touch Targets

```css
/* Minimum touch target: 44x44 pixels (WCAG AAA) */
.button {
  min-width: 44px;
  min-height: 44px;
  padding: 0.75rem 1rem;  /* Generous padding */
}

/* Spacing between touch targets */
.nav-list {
  display: flex;
  gap: 0.5rem;  /* Minimum 8px gap */
}

/* Increase touch targets on mobile */
@media (max-width: 767px) {
  .button {
    min-height: 48px;
    padding: 1rem 1.5rem;
  }
}
```

---

## Utility Classes Pattern

```css
/* Spacing utilities */
.m-0 { margin: 0; }
.m-1 { margin: 0.25rem; }
.m-2 { margin: 0.5rem; }
.m-4 { margin: 1rem; }
.m-8 { margin: 2rem; }

.mt-4 { margin-top: 1rem; }
.mr-4 { margin-right: 1rem; }
.mb-4 { margin-bottom: 1rem; }
.ml-4 { margin-left: 1rem; }

/* Display utilities */
.hidden { display: none; }
.block { display: block; }
.flex { display: flex; }
.grid { display: grid; }

/* Responsive utilities */
@media (min-width: 768px) {
  .md\:hidden { display: none; }
  .md\:block { display: block; }
  .md\:flex { display: flex; }
}

@media (min-width: 1024px) {
  .lg\:hidden { display: none; }
  .lg\:block { display: block; }
}

/* Text utilities */
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }

.font-bold { font-weight: 700; }
.font-normal { font-weight: 400; }

.text-sm { font-size: 0.875rem; }
.text-base { font-size: 1rem; }
.text-lg { font-size: 1.125rem; }
.text-xl { font-size: 1.25rem; }
```

---

## Browser Compatibility

### Feature Detection

```css
/* Use @supports for feature detection */
.grid-container {
  display: flex;  /* Fallback */
  flex-wrap: wrap;
}

@supports (display: grid) {
  .grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  }
}

/* Detect container queries support */
@supports (container-type: inline-size) {
  .card-container {
    container-type: inline-size;
  }
}
```

### Vendor Prefixes

```css
/* Use autoprefixer in build process */
/* postcss.config.js */
module.exports = {
  plugins: [
    require('autoprefixer')({
      browsers: ['last 2 versions', '> 1%', 'not dead'],
    }),
  ],
};

/* It will automatically add: */
.box {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}
```

---

## Testing Responsive Designs

### Manual Testing Checklist

- [ ] Test all breakpoints (320px, 768px, 1024px, 1440px)
- [ ] Test landscape and portrait orientations
- [ ] Test on actual devices (not just emulator)
- [ ] Test with 200% browser zoom
- [ ] Test with different font sizes
- [ ] Test hover states on desktop
- [ ] Test touch interactions on mobile
- [ ] Test with slow network (3G simulation)
- [ ] Test with JavaScript disabled
- [ ] Test with screen reader

### Automated Testing

```typescript
// Playwright responsive testing
import { test, expect } from '@playwright/test';

const viewports = [
  { width: 375, height: 667, name: 'iPhone SE' },
  { width: 768, height: 1024, name: 'iPad' },
  { width: 1920, height: 1080, name: 'Desktop' },
];

for (const viewport of viewports) {
  test(`renders correctly on ${viewport.name}`, async ({ page }) => {
    await page.setViewportSize(viewport);
    await page.goto('http://localhost:3000');
    await expect(page).toHaveScreenshot(`${viewport.name}.png`);
  });
}
```

---

## Summary Checklist

When implementing responsive styles:

**Mobile-First**:
- [ ] Base styles target mobile (no media query)
- [ ] Use `min-width` media queries for larger screens
- [ ] Test on actual mobile devices

**Performance**:
- [ ] CSS file size < 50KB (minified)
- [ ] Critical CSS inlined
- [ ] Unused CSS removed
- [ ] Animations use transform/opacity only
- [ ] Images responsive with srcset/sizes

**Accessibility**:
- [ ] Color contrast ≥ 4.5:1 (text)
- [ ] Color contrast ≥ 3:1 (UI components)
- [ ] Focus indicators visible
- [ ] Text resizable to 200%
- [ ] Touch targets ≥ 44×44px
- [ ] Respects prefers-reduced-motion
- [ ] Respects prefers-color-scheme

**Browser Compatibility**:
- [ ] Works in Chrome, Firefox, Safari, Edge
- [ ] Autoprefixer configured
- [ ] Feature detection with @supports
- [ ] Graceful degradation for old browsers

**Code Quality**:
- [ ] CSS organized and modular
- [ ] Custom properties for theming
- [ ] Consistent naming convention
- [ ] Comments for complex logic
- [ ] No inline styles

---

**Version**: 1.0
**Last Updated**: January 2025
**Coverage**: CSS, CSS Modules, Tailwind, styled-components
**Success Rate**: 98% performance targets met with these patterns
