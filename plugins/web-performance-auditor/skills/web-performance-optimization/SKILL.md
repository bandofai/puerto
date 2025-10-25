# Web Performance Optimization Skill

Expert knowledge for optimizing web application performance, improving Core Web Vitals, and implementing modern performance best practices.

## Overview

This skill provides battle-tested optimization techniques for improving website performance across all metrics: loading speed, interactivity, visual stability, and runtime performance.

## Core Performance Concepts

### Performance Metrics Hierarchy

```
User Experience Impact (Highest to Lowest)
│
├─ Core Web Vitals (Google ranking signals)
│  ├─ LCP - Largest Contentful Paint (Loading)
│  ├─ FID - First Input Delay (Interactivity)
│  └─ CLS - Cumulative Layout Shift (Visual Stability)
│
├─ Other Key Metrics
│  ├─ FCP - First Contentful Paint
│  ├─ TTI - Time to Interactive
│  ├─ TBT - Total Blocking Time
│  └─ SI - Speed Index
│
└─ Resource Metrics
   ├─ Page Size
   ├─ Request Count
   └─ Resource Load Times
```

### Performance Budget Philosophy

**1% Rule:** Users perceive performance improvements of 20% or more
- Target 20%+ improvement in each optimization
- Small gains (< 5%) may not be worth the effort
- Focus on high-impact optimizations first

**Performance Budget Template:**
- Initial Load: < 3s (Mobile 3G)
- Time to Interactive: < 5s
- Total Page Size: < 1MB
- JavaScript Bundle: < 200KB
- Images: < 500KB
- First Input Delay: < 100ms

## Optimization Strategies

### Strategy 1: Critical Rendering Path Optimization

**Goal:** Show meaningful content as fast as possible

```
Critical Rendering Path
│
├─ 1. HTML parsing
│  └─ Minimize HTML size
│     • Remove comments
│     • Minify HTML
│     • Use semantic, lean markup
│
├─ 2. CSS loading and parsing
│  └─ Eliminate render-blocking CSS
│     • Inline critical CSS
│     • Defer non-critical CSS
│     • Remove unused CSS
│
├─ 3. JavaScript execution
│  └─ Defer non-critical JS
│     • Async attribute
│     • Defer attribute
│     • Dynamic imports
│
└─ 4. First paint
   └─ Optimize LCP element
      • Preload hero images
      • Optimize fonts
      • Remove layout shifts
```

#### Implementation: Inline Critical CSS

```html
<!-- Before: Render-blocking stylesheet -->
<link rel="stylesheet" href="styles.css">

<!-- After: Inline critical CSS -->
<head>
  <style>
    /* Critical above-the-fold CSS */
    .header { ... }
    .hero { ... }
    .cta-button { ... }
  </style>

  <!-- Async load full stylesheet -->
  <link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="styles.css"></noscript>
</head>
```

**Tools for extraction:**
```bash
# Using Critical package
npm install critical

# Extract critical CSS
critical index.html --base dist/ --inline --minify > index-critical.html
```

---

### Strategy 2: Image Optimization

**Impact:** Images typically account for 50-70% of page weight

#### Technique 1: Modern Image Formats

**Format Selection Matrix:**

| Use Case | Format | Savings vs JPEG |
|----------|--------|-----------------|
| Photos (lossy) | WebP | 25-35% |
| Photos (next-gen) | AVIF | 40-50% |
| Graphics/logos | SVG | 60-80% |
| Animations | WebP animated | 60-75% vs GIF |

**Implementation:**
```html
<picture>
  <!-- Best: AVIF (newest, smallest) -->
  <source srcset="hero.avif" type="image/avif">

  <!-- Good: WebP (wide support) -->
  <source srcset="hero.webp" type="image/webp">

  <!-- Fallback: JPEG (universal) -->
  <img src="hero.jpg" alt="Hero image" width="1200" height="600">
</picture>
```

#### Technique 2: Responsive Images

**Problem:** Serving 2400px image to 375px mobile screen = 84% waste

```html
<!-- Responsive srcset -->
<img
  srcset="
    product-400w.webp 400w,
    product-800w.webp 800w,
    product-1200w.webp 1200w,
    product-1600w.webp 1600w
  "
  sizes="
    (max-width: 600px) 100vw,
    (max-width: 900px) 50vw,
    33vw
  "
  src="product-800w.webp"
  alt="Product"
  loading="lazy"
>
```

**Automated generation:**
```javascript
// Using Sharp (Node.js)
const sharp = require('sharp');

const widths = [400, 800, 1200, 1600];

async function generateResponsiveImages(input) {
  for (const width of widths) {
    await sharp(input)
      .resize(width)
      .webp({ quality: 80 })
      .toFile(`output-${width}w.webp`);

    await sharp(input)
      .resize(width)
      .avif({ quality: 65 })
      .toFile(`output-${width}w.avif`);
  }
}
```

#### Technique 3: Lazy Loading

**Native lazy loading:**
```html
<!-- Browser handles lazy loading -->
<img src="image.jpg" alt="Description" loading="lazy">
```

**Custom Intersection Observer (more control):**
```javascript
const lazyImages = document.querySelectorAll('img[data-src]');

const imageObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.removeAttribute('data-src');
      imageObserver.unobserve(img);
    }
  });
}, {
  rootMargin: '50px' // Start loading 50px before viewport
});

lazyImages.forEach(img => imageObserver.observe(img));
```

---

### Strategy 3: JavaScript Optimization

**Problem:** JavaScript is the #1 cause of slow Time to Interactive

#### Technique 1: Code Splitting

**Route-based splitting (React):**
```javascript
import { lazy, Suspense } from 'react';

// Before: All routes loaded upfront
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import Settings from './pages/Settings';

// After: Load routes on demand
const Home = lazy(() => import('./pages/Home'));
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Settings = lazy(() => import('./pages/Settings'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Suspense>
  );
}
```

**Component-based splitting:**
```javascript
// Load heavy component only when needed
const HeavyChart = lazy(() => import('./HeavyChart'));

function Dashboard() {
  const [showChart, setShowChart] = useState(false);

  return (
    <div>
      <button onClick={() => setShowChart(true)}>
        Load Chart
      </button>

      {showChart && (
        <Suspense fallback={<Spinner />}>
          <HeavyChart data={data} />
        </Suspense>
      )}
    </div>
  );
}
```

#### Technique 2: Tree Shaking

**Before:**
```javascript
// Imports entire library (500KB)
import _ from 'lodash';
const unique = _.uniq(array);
```

**After:**
```javascript
// Imports only what's needed (2KB)
import uniq from 'lodash/uniq';
const unique = uniq(array);

// Or use modern ESM version
import { uniq } from 'lodash-es';
```

**Webpack configuration:**
```javascript
// webpack.config.js
module.exports = {
  mode: 'production',
  optimization: {
    usedExports: true, // Enable tree shaking
    sideEffects: false // Mark all files as side-effect free
  }
};
```

#### Technique 3: Reduce Main Thread Blocking

**Problem:** Long tasks block user interaction

```javascript
// ❌ Bad: Blocks main thread
function processItems(items) {
  items.forEach(item => {
    heavyProcessing(item); // Blocks for 500ms
  });
}

// ✅ Good: Yield to main thread
async function processItems(items) {
  for (const item of items) {
    heavyProcessing(item);

    // Yield every 50ms to allow user interaction
    if (performance.now() % 50 < 16) {
      await new Promise(resolve => setTimeout(resolve, 0));
    }
  }
}

// ✅ Better: Use Web Worker
// worker.js
self.addEventListener('message', (e) => {
  const result = heavyProcessing(e.data);
  self.postMessage(result);
});

// main.js
const worker = new Worker('worker.js');
worker.postMessage(items);
worker.onmessage = (e) => {
  displayResults(e.data);
};
```

#### Technique 4: Third-Party Script Optimization

**Problem:** Third-party scripts often block rendering and slow TTI

```html
<!-- ❌ Bad: Blocking analytics -->
<script src="https://analytics.com/script.js"></script>

<!-- ✅ Good: Async analytics -->
<script async src="https://analytics.com/script.js"></script>

<!-- ✅ Better: Self-host and defer -->
<script defer src="/local-analytics.js"></script>

<!-- ✅ Best: Load after page interactive -->
<script>
  window.addEventListener('load', () => {
    const script = document.createElement('script');
    script.src = 'https://analytics.com/script.js';
    script.async = true;
    document.body.appendChild(script);
  });
</script>
```

**Facade pattern for heavy embeds:**
```html
<!-- Instead of loading full YouTube embed immediately -->
<div class="youtube-facade" data-video-id="dQw4w9WgXcQ">
  <img src="https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg" alt="Video">
  <button class="play-button">Play</button>
</div>

<script>
document.querySelectorAll('.youtube-facade').forEach(facade => {
  facade.addEventListener('click', () => {
    const iframe = document.createElement('iframe');
    iframe.src = `https://www.youtube.com/embed/${facade.dataset.videoId}?autoplay=1`;
    iframe.allow = 'autoplay';
    facade.replaceWith(iframe);
  });
});
</script>
```

---

### Strategy 4: Layout Stability (CLS Optimization)

**Problem:** Unexpected layout shifts frustrate users and hurt rankings

#### Technique 1: Reserve Space for Images

```css
/* ❌ Bad: No dimensions */
img {
  width: 100%;
}

/* ✅ Good: Aspect ratio box */
.image-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
}

.image-container img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

**HTML with explicit dimensions:**
```html
<!-- Browser can reserve space before image loads -->
<img
  src="hero.jpg"
  alt="Hero"
  width="1200"
  height="675"
  style="max-width: 100%; height: auto;"
>
```

#### Technique 2: Font Loading Optimization

**Problem:** Font swapping causes text to shift

```css
/* ❌ Bad: Flash of invisible text (FOIT) */
@font-face {
  font-family: 'CustomFont';
  src: url('custom.woff2');
  /* Default font-display: auto */
}

/* ✅ Good: Use fallback immediately */
@font-face {
  font-family: 'CustomFont';
  src: url('custom.woff2');
  font-display: swap; /* Show fallback, then swap */
}

/* ✅ Better: Match fallback metrics */
@font-face {
  font-family: 'CustomFont';
  src: url('custom.woff2');
  font-display: swap;
  size-adjust: 95%; /* Adjust to match fallback size */
  ascent-override: 90%;
  descent-override: 20%;
}
```

**Preload critical fonts:**
```html
<link
  rel="preload"
  href="/fonts/custom.woff2"
  as="font"
  type="font/woff2"
  crossorigin
>
```

#### Technique 3: Dynamic Content Placeholders

```html
<!-- Skeleton loader prevents layout shift -->
<div class="article-list">
  <div class="skeleton-card"></div>
  <div class="skeleton-card"></div>
  <div class="skeleton-card"></div>
</div>

<style>
.skeleton-card {
  height: 200px;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
  border-radius: 8px;
  margin-bottom: 16px;
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
</style>
```

---

### Strategy 5: Caching and Delivery Optimization

#### Technique 1: HTTP Caching Headers

```javascript
// Node.js/Express
app.use('/assets', express.static('public', {
  maxAge: '1y',
  immutable: true
}));

// Different cache for HTML
app.use((req, res, next) => {
  if (req.url.endsWith('.html')) {
    res.setHeader('Cache-Control', 'public, max-age=3600, must-revalidate');
  } else if (req.url.match(/\.(css|js|jpg|png|svg|woff2)$/)) {
    res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
  }
  next();
});
```

**Cache Strategy Matrix:**

| Resource Type | Cache Duration | Versioning |
|---------------|----------------|------------|
| HTML | 1 hour | N/A |
| CSS/JS (versioned) | 1 year | Hash in filename |
| Images (versioned) | 1 year | Hash in filename |
| Images (user-uploaded) | 1 week | N/A |
| API responses | 5 minutes | ETag |

#### Technique 2: Service Worker Caching

```javascript
// sw.js - Cache-first strategy
const CACHE_NAME = 'v1';
const urlsToCache = [
  '/',
  '/styles.css',
  '/app.js',
  '/logo.svg'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Return cached version or fetch from network
        return response || fetch(event.request);
      })
  );
});
```

#### Technique 3: CDN and Edge Caching

**Cloudflare Workers example:**
```javascript
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  const cache = caches.default;

  // Check cache first
  let response = await cache.match(request);

  if (!response) {
    // Fetch from origin
    response = await fetch(request);

    // Cache for 1 day
    const headers = new Headers(response.headers);
    headers.set('Cache-Control', 'public, max-age=86400');

    response = new Response(response.body, {
      status: response.status,
      headers: headers
    });

    event.waitUntil(cache.put(request, response.clone()));
  }

  return response;
}
```

---

## Performance Monitoring

### Real User Monitoring (RUM)

```javascript
// web-vitals library
import { getCLS, getFID, getLCP } from 'web-vitals';

function sendToAnalytics(metric) {
  const body = JSON.stringify(metric);

  // Use sendBeacon if available
  if (navigator.sendBeacon) {
    navigator.sendBeacon('/analytics', body);
  } else {
    fetch('/analytics', { body, method: 'POST', keepalive: true });
  }
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getLCP(sendToAnalytics);
```

### Performance Observer API

```javascript
// Monitor long tasks
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (entry.duration > 50) {
      console.warn('Long task detected:', entry.duration, 'ms');
      // Send to monitoring service
    }
  }
});

observer.observe({ type: 'longtask', buffered: true });
```

---

## Framework-Specific Optimizations

### Next.js

```javascript
// next.config.js
module.exports = {
  images: {
    formats: ['image/avif', 'image/webp'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920],
  },
  compiler: {
    removeConsole: process.env.NODE_ENV === 'production',
  },
  swcMinify: true, // Faster minification
  experimental: {
    optimizeCss: true,
  },
};

// Image optimization
import Image from 'next/image';

<Image
  src="/hero.jpg"
  alt="Hero"
  width={1200}
  height={600}
  priority // For LCP images
  placeholder="blur"
/>

// Dynamic imports
import dynamic from 'next/dynamic';

const Chart = dynamic(() => import('./Chart'), {
  loading: () => <Skeleton />,
  ssr: false // Client-only
});
```

### React

```jsx
// Code splitting
import { lazy, Suspense } from 'react';
const Heavy = lazy(() => import('./Heavy'));

// Memoization
import { memo, useMemo, useCallback } from 'react';

const ExpensiveComponent = memo(({ data }) => {
  const processed = useMemo(() => process(data), [data]);
  const handler = useCallback(() => {}, []);

  return <div>{processed}</div>;
});

// Virtualization for long lists
import { FixedSizeList } from 'react-window';

<FixedSizeList
  height={600}
  itemCount={1000}
  itemSize={50}
>
  {({ index, style }) => (
    <div style={style}>Row {index}</div>
  )}
</FixedSizeList>
```

---

## Performance Checklist

### Critical Path Optimization
- [ ] Inline critical CSS (< 14KB)
- [ ] Defer non-critical CSS
- [ ] Async/defer non-critical JavaScript
- [ ] Minimize render-blocking resources
- [ ] Preload key resources (fonts, hero images)

### Image Optimization
- [ ] Use WebP/AVIF formats
- [ ] Implement responsive images (srcset)
- [ ] Lazy load off-screen images
- [ ] Explicit width/height on images
- [ ] Optimize image compression

### JavaScript Optimization
- [ ] Code splitting (route + component level)
- [ ] Tree shaking (remove unused code)
- [ ] Minimize third-party scripts
- [ ] Defer non-essential scripts
- [ ] Use Web Workers for heavy computation

### Layout Stability
- [ ] Reserve space for images
- [ ] Optimize font loading (font-display: swap)
- [ ] Skeleton loaders for dynamic content
- [ ] No layout-shifting ads

### Caching
- [ ] Set appropriate cache headers
- [ ] Implement service worker
- [ ] Use CDN for static assets
- [ ] Enable compression (gzip/brotli)

---

## Resources

- **Web.dev Performance**: https://web.dev/performance/
- **Core Web Vitals**: https://web.dev/vitals/
- **MDN Performance**: https://developer.mozilla.org/en-US/docs/Web/Performance
- **Performance Budgets**: https://web.dev/performance-budgets-101/
- **HTTP Caching**: https://web.dev/http-cache/
