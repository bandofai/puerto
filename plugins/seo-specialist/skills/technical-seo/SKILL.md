# Technical SEO Skill

**Production-tested practices for technical SEO audits and implementation**

This skill codifies technical SEO best practices from professional audits of high-performing websites.

---

## Core Principles

1. **Crawlability First**: Search engines must find and access your content
2. **Speed Matters**: Core Web Vitals directly impact rankings
3. **Mobile-First**: Google indexes mobile version primarily
4. **Structured Data**: Help search engines understand your content
5. **User Experience**: Technical SEO serves human visitors

---

## The 10 Pillars of Technical SEO

### 1. Site Architecture & Crawlability

**Optimal Site Structure**:
```
Homepage (Level 0)
├─ Category Pages (Level 1)
│  ├─ Subcategory Pages (Level 2)
│  │  └─ Individual Pages (Level 3)
```

**Best Practices**:
- Maximum 3 clicks from homepage to any page
- Logical URL hierarchy
- Clear navigation structure
- Internal linking strategy
- XML sitemap for all important pages

**robots.txt Configuration**:
```txt
# Allow all crawlers
User-agent: *
Allow: /

# Block sensitive areas
Disallow: /admin/
Disallow: /api/
Disallow: /private/
Disallow: /*.pdf$

# Block duplicate content
Disallow: /*?sort=
Disallow: /*?page=

# Sitemap location
Sitemap: https://example.com/sitemap.xml
```

**Common Mistakes**:
- Blocking important pages in robots.txt
- Orphaned pages (no internal links)
- Infinite scroll without pagination
- Deep page hierarchy (4+ levels)

### 2. Core Web Vitals & Performance

**The 3 Core Web Vitals**:

**Largest Contentful Paint (LCP)** - Loading Performance
- Target: < 2.5 seconds
- Measures: When main content loads
- Fix: Optimize images, reduce server response time, use CDN

**First Input Delay (FID)** - Interactivity
- Target: < 100 milliseconds
- Measures: Time until page is interactive
- Fix: Minimize JavaScript, code splitting, defer non-critical JS

**Cumulative Layout Shift (CLS)** - Visual Stability
- Target: < 0.1
- Measures: Unexpected layout shifts
- Fix: Set image dimensions, avoid inserting content above existing content

**Performance Optimization Checklist**:
- [ ] Images optimized (WebP/AVIF, compressed)
- [ ] Lazy loading implemented
- [ ] Critical CSS inlined
- [ ] JavaScript deferred/async
- [ ] CDN for static assets
- [ ] Server response time < 200ms
- [ ] Minified CSS/JS
- [ ] Gzip/Brotli compression enabled

### 3. Mobile-First Optimization

**Mobile SEO Checklist**:
- [ ] Responsive design (adapts to all screen sizes)
- [ ] Viewport meta tag present
- [ ] Touch targets ≥ 44x44px
- [ ] Font size ≥ 16px for body text
- [ ] No horizontal scrolling
- [ ] Mobile page speed < 3 seconds
- [ ] Tap targets well-spaced (48px spacing)
- [ ] No mobile-specific errors in Search Console

**Mobile-Friendly Meta Tag**:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### 4. URL Structure & Management

**SEO-Friendly URL Best Practices**:

**Good URLs**:
```
✅ example.com/blog/seo-best-practices
✅ example.com/products/running-shoes
✅ example.com/services/web-design
```

**Bad URLs**:
```
❌ example.com/page.php?id=123&cat=5
❌ example.com/Products_And_Services
❌ example.com/p/12345
```

**URL Guidelines**:
- Use hyphens, not underscores
- Lowercase only
- Include target keyword
- Keep short (< 60 characters)
- Logical hierarchy
- No parameters if possible
- Consistent trailing slash handling

**Redirect Best Practices**:
- Use 301 redirects for moved content
- Avoid redirect chains (A→B→C)
- Update internal links instead of redirecting
- Redirect old URLs to most relevant new page

### 5. HTML & Meta Tag Optimization

**Essential Meta Tags**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Character encoding -->
  <meta charset="UTF-8">

  <!-- Viewport for mobile -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Title (50-60 characters) -->
  <title>Page Title | Brand Name</title>

  <!-- Meta description (150-160 characters) -->
  <meta name="description" content="Compelling description with keywords">

  <!-- Canonical URL -->
  <link rel="canonical" href="https://example.com/page">

  <!-- Open Graph for social -->
  <meta property="og:title" content="Page Title">
  <meta property="og:description" content="Description">
  <meta property="og:image" content="https://example.com/og-image.jpg">
  <meta property="og:url" content="https://example.com/page">
  <meta property="og:type" content="website">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Page Title">
  <meta name="twitter:description" content="Description">
  <meta name="twitter:image" content="https://example.com/twitter-image.jpg">

  <!-- Robots meta (if needed) -->
  <meta name="robots" content="index, follow">
</head>
```

**Heading Hierarchy**:
```html
<h1>Single H1: Primary Page Topic</h1>

<h2>Main Section 1</h2>
<h3>Subsection 1.1</h3>
<h3>Subsection 1.2</h3>

<h2>Main Section 2</h2>
<h3>Subsection 2.1</h3>

<!-- Don't skip levels -->
<!-- Don't use multiple H1s -->
```

### 6. Schema Markup (Structured Data)

**Common Schema Types**:

**Organization**:
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Company Name",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "sameAs": [
    "https://facebook.com/company",
    "https://twitter.com/company",
    "https://linkedin.com/company/company"
  ]
}
```

**Article**:
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "image": "https://example.com/image.jpg",
  "author": {
    "@type": "Person",
    "name": "Author Name"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Publisher",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "datePublished": "2025-01-20",
  "dateModified": "2025-01-20"
}
```

**BreadcrumbList**:
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Category",
      "item": "https://example.com/category"
    }
  ]
}
```

### 7. Image SEO

**Image Optimization Checklist**:
- [ ] Descriptive file names (not IMG_1234.jpg)
- [ ] Alt text on all images (except decorative)
- [ ] Image dimensions specified (width/height)
- [ ] Lazy loading for below-fold images
- [ ] Modern formats (WebP, AVIF)
- [ ] Compressed (TinyPNG, ImageOptim)
- [ ] Responsive images (srcset)
- [ ] Image sitemap (for image search)

**Example**:
```html
<img
  src="blue-running-shoes-800w.webp"
  srcset="blue-running-shoes-400w.webp 400w,
          blue-running-shoes-800w.webp 800w,
          blue-running-shoes-1200w.webp 1200w"
  sizes="(max-width: 600px) 400px,
         (max-width: 1000px) 800px,
         1200px"
  alt="Blue Nike running shoes on white background"
  width="800"
  height="600"
  loading="lazy"
  decoding="async"
/>
```

### 8. Security & HTTPS

**Security Checklist**:
- [ ] SSL certificate installed and valid
- [ ] All pages served over HTTPS
- [ ] HTTP redirects to HTTPS (301)
- [ ] No mixed content (HTTP resources on HTTPS pages)
- [ ] HSTS header implemented
- [ ] Security headers configured

**Essential Security Headers**:
```
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), microphone=(), camera=()
```

### 9. International & Multi-Language SEO

**Hreflang Implementation**:

```html
<!-- Current page (English US) -->
<link rel="alternate" hreflang="en-us" href="https://example.com/en-us/page" />

<!-- Other language versions -->
<link rel="alternate" hreflang="en-gb" href="https://example.com/en-gb/page" />
<link rel="alternate" hreflang="es-es" href="https://example.com/es-es/page" />
<link rel="alternate" hreflang="fr-fr" href="https://example.com/fr-fr/page" />

<!-- Default for language selector -->
<link rel="alternate" hreflang="x-default" href="https://example.com/page" />
```

**Best Practices**:
- Use correct language-region codes (en-US, not just en)
- Include self-referential hreflang
- Include x-default for unmatched regions
- Same URL structure across languages
- Translate meta tags and structured data

### 10. Indexability & Search Console

**Indexability Checklist**:
- [ ] Important pages indexed (check: site:example.com)
- [ ] No accidental noindex tags
- [ ] Sitemap submitted to Search Console
- [ ] Sitemap includes all important pages
- [ ] No crawl errors in Search Console
- [ ] Coverage report clean
- [ ] Mobile usability issues resolved

**XML Sitemap Best Practices**:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/page</loc>
    <lastmod>2025-01-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

- Include only canonical URLs
- Update lastmod when content changes
- Split large sitemaps (> 50,000 URLs)
- Exclude noindex pages
- Include images in sitemap or separate image sitemap

---

## Technical SEO Audit Framework

### Phase 1: Discovery (30 minutes)

**Identify**:
- Site type and framework
- Number of pages
- Site structure
- Key templates
- Existing issues

**Tools**:
- Google Search Console
- Screaming Frog (crawl)
- PageSpeed Insights
- Mobile-Friendly Test

### Phase 2: Analysis (2-3 hours)

**Audit all 10 pillars**:
1. Site architecture
2. Core Web Vitals
3. Mobile optimization
4. URL structure
5. HTML/meta tags
6. Schema markup
7. Image SEO
8. Security
9. International (if applicable)
10. Indexability

**Document**:
- Specific issues with file paths
- Severity (Critical/High/Medium/Low)
- Impact on SEO
- Fix recommendations

### Phase 3: Reporting (1 hour)

**Report structure**:
- Executive summary
- Issue count by severity
- Detailed findings by category
- Priority action plan
- Expected impact

---

## Common Technical SEO Issues

### Critical Issues (Fix Immediately)

1. **Site Not Indexed**
   - Issue: noindex on all pages
   - Impact: Site invisible to search engines
   - Fix: Remove noindex tags

2. **Robots.txt Blocking Site**
   - Issue: Disallow: / in robots.txt
   - Impact: Crawlers can't access site
   - Fix: Update robots.txt

3. **No HTTPS**
   - Issue: Site on HTTP
   - Impact: Security warning, ranking penalty
   - Fix: Install SSL certificate

4. **Severe Performance Issues**
   - Issue: Page load > 10 seconds
   - Impact: High bounce rate, ranking penalty
   - Fix: Optimize images, code, server

### High Priority (Fix This Week)

1. **Missing Title Tags**
   - Impact: Poor click-through rate
   - Fix: Add unique title to every page

2. **Missing Meta Descriptions**
   - Impact: Less compelling search results
   - Fix: Add compelling descriptions

3. **Not Mobile-Friendly**
   - Impact: Mobile ranking penalty
   - Fix: Implement responsive design

4. **Broken Internal Links**
   - Impact: Poor UX, wasted crawl budget
   - Fix: Update or remove broken links

### Medium Priority (Fix This Month)

1. **Suboptimal URL Structure**
   - Impact: Missed keyword opportunity
   - Fix: Implement clean URLs (with redirects)

2. **Missing Schema Markup**
   - Impact: Missed rich snippet opportunity
   - Fix: Implement relevant schema types

3. **Images Without Alt Text**
   - Impact: Accessibility and image search
   - Fix: Add descriptive alt text

4. **Slow Page Speed (3-5s)**
   - Impact: Moderate ranking factor
   - Fix: Optimize performance

---

## Framework-Specific Considerations

### Next.js SEO Optimization

```typescript
// app/layout.tsx
export const metadata = {
  metadataBase: new URL('https://example.com'),
  title: {
    default: 'Site Name',
    template: '%s | Site Name'
  },
  description: 'Default description',
  robots: {
    index: true,
    follow: true,
  },
}

// app/page.tsx
export const metadata = {
  title: 'Page Title',
  description: 'Page description',
  openGraph: {
    title: 'Page Title',
    description: 'Page description',
    images: ['/og-image.jpg'],
  },
}

// Generate sitemap
export default function sitemap() {
  return [
    {
      url: 'https://example.com',
      lastModified: new Date(),
    },
  ]
}

// robots.txt
export default function robots() {
  return {
    rules: {
      userAgent: '*',
      allow: '/',
      disallow: '/admin/',
    },
    sitemap: 'https://example.com/sitemap.xml',
  }
}
```

### WordPress SEO

**Essential Plugins**:
- Yoast SEO or Rank Math (on-page optimization)
- WP Rocket or W3 Total Cache (performance)
- Smush or ShortPixel (image optimization)
- Redirection (301 redirects)

**wp-config.php optimizations**:
```php
// Disable file editing
define('DISALLOW_FILE_EDIT', true);

// Enable caching
define('WP_CACHE', true);

// Increase memory limit
define('WP_MEMORY_LIMIT', '256M');
```

### Static Site Generators (Gatsby, Hugo, Jekyll)

**Advantages**:
- Blazing fast (static HTML)
- Inherently secure
- Easy to cache

**SEO Setup**:
- Configure meta tags in templates
- Generate sitemap at build time
- Optimize images during build
- Implement schema in templates
- Configure redirects in netlify.toml or _redirects

---

## Testing & Validation

### Essential Tools

**Free Tools**:
- Google Search Console (indexing, errors)
- Google PageSpeed Insights (performance)
- Google Mobile-Friendly Test
- Google Rich Results Test (schema)
- Lighthouse (comprehensive audit)
- Screaming Frog (free up to 500 URLs)

**Paid Tools**:
- Screaming Frog (full site crawls)
- Ahrefs Site Audit
- SEMrush Site Audit
- Sitebulb
- OnCrawl

### Validation Checklist

After implementing fixes:
- [ ] Run PageSpeed Insights (mobile & desktop)
- [ ] Test with Mobile-Friendly Test
- [ ] Validate schema with Rich Results Test
- [ ] Check Search Console for errors
- [ ] Crawl site with Screaming Frog
- [ ] Verify redirects work correctly
- [ ] Test all critical user flows
- [ ] Check canonical tags point correctly

---

## Monitoring & Maintenance

### Monthly Checks

- [ ] Google Search Console errors
- [ ] Core Web Vitals performance
- [ ] New 404 errors
- [ ] Security issues
- [ ] Mobile usability issues
- [ ] Indexing coverage

### Quarterly Audits

- [ ] Full site crawl
- [ ] Backlink profile review
- [ ] Content freshness audit
- [ ] Technical SEO health check
- [ ] Competitor analysis

---

## Success Metrics

**Technical SEO KPIs**:
- **Crawl Efficiency**: Pages crawled / Total pages
- **Index Coverage**: Pages indexed / Total pages
- **Core Web Vitals**: LCP, FID, CLS scores
- **Mobile Usability**: Issues in Search Console
- **Page Speed**: Load time improvement
- **Error Rate**: 404s, 500s, crawl errors

**Targets**:
- 95%+ important pages indexed
- Core Web Vitals: All "Good"
- 0 critical errors in Search Console
- < 1% 404 error rate
- Mobile page speed < 3 seconds

---

**Version**: 1.0
**Last Updated**: January 2025
**Framework Coverage**: Next.js, WordPress, Static Sites
**Compliance**: Google Search Essentials, Core Web Vitals
