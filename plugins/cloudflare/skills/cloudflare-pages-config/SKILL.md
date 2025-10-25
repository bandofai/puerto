# Cloudflare Pages Configuration Skill

Expert knowledge for configuring Cloudflare Pages projects, managing environment variables, custom domains, and build settings.

## Overview

This skill provides comprehensive patterns and best practices for configuring and managing Cloudflare Pages projects through Wrangler CLI and the Cloudflare Dashboard.

## Configuration File: wrangler.toml

### Basic Structure

```toml
# Project identification
name = "my-pages-project"

# Compatibility date (use latest for new features)
compatibility_date = "2025-01-15"

# Build configuration
[build]
command = "npm run build"
cwd = "."
watch_dirs = ["src", "public"]

# Upload configuration
[[build.upload]]
format = "directory"
dir = "dist"

# Production environment
[env.production]
# Production-specific settings

# Preview environment
[env.preview]
# Preview-specific settings
```

### Advanced Configuration

```toml
name = "advanced-pages-project"
compatibility_date = "2025-01-15"

# Build configuration with custom Node version
[build]
command = "npm ci && npm run build"
cwd = "."
watch_dirs = ["src", "public", "content"]

# Node.js version selection
[build.env_vars]
NODE_VERSION = "18"
NODE_ENV = "production"

# Upload multiple directories
[[build.upload]]
format = "directory"
dir = "dist"
exclusions = ["*.map", "*.md"]

# Production environment configuration
[env.production]
workers_dev = false
route = "example.com/*"

# Staging environment
[env.staging]
workers_dev = false
route = "staging.example.com/*"

# Preview environment
[env.preview]
workers_dev = true
```

## Environment Variables

### Types of Variables

**1. Build-Time Variables** (Set during build)
- Embedded in compiled code
- Public (visible in browser)
- Set via `.env` files or build scripts
- Examples: API URLs, feature flags, public IDs

**2. Runtime Variables** (Secrets)
- Accessed in Pages Functions
- Private (not visible in browser)
- Set via Wrangler CLI
- Examples: API keys, database credentials

### Setting Build-Time Variables

```bash
# .env file (for local development)
VITE_API_URL=https://api.example.com
NEXT_PUBLIC_GA_ID=UA-XXXXXXX-1
PUBLIC_FEATURE_FLAG=true

# Build with variables
npm run build
```

Common frameworks:
- **Vite**: `VITE_*` prefix
- **Next.js**: `NEXT_PUBLIC_*` prefix
- **Create React App**: `REACT_APP_*` prefix
- **Nuxt**: `NUXT_PUBLIC_*` prefix
- **SvelteKit**: `PUBLIC_*` prefix

### Setting Runtime Secrets

```bash
# Set individual secret
wrangler pages secret put API_KEY --project-name=my-website

# Set multiple secrets
wrangler pages secret put DATABASE_URL --project-name=my-website
wrangler pages secret put STRIPE_SECRET --project-name=my-website
wrangler pages secret put AUTH_SECRET --project-name=my-website

# List secrets (values are hidden)
wrangler pages secret list --project-name=my-website

# Delete secret
wrangler pages secret delete API_KEY --project-name=my-website
```

### Bulk Secret Management

```bash
# Script to set multiple secrets from file
#!/bin/bash
PROJECT_NAME="my-website"

# Read from .env.production (DO NOT commit this file!)
while IFS='=' read -r key value; do
  # Skip empty lines and comments
  [[ -z "$key" || "$key" =~ ^#.* ]] && continue

  # Set secret
  echo "$value" | wrangler pages secret put "$key" --project-name="$PROJECT_NAME"
  echo "✓ Set secret: $key"
done < .env.production

echo "✅ All secrets configured"
```

### Accessing Secrets in Pages Functions

```javascript
// functions/api/data.js

export async function onRequest(context) {
  // Access runtime secrets
  const apiKey = context.env.API_KEY;
  const dbUrl = context.env.DATABASE_URL;

  // Use in API calls
  const response = await fetch('https://api.example.com/data', {
    headers: {
      'Authorization': `Bearer ${apiKey}`
    }
  });

  return response;
}
```

## Custom Domains

### Adding Custom Domain

**Via Cloudflare Dashboard:**
1. Navigate to: https://dash.cloudflare.com/
2. Select your account
3. Go to: Workers & Pages → Your Project → Custom domains
4. Click "Set up a custom domain"
5. Enter domain name (e.g., `www.example.com`)
6. Follow DNS instructions

### DNS Configuration

**Option 1: CNAME (Recommended)**
```
Type: CNAME
Name: www
Content: your-project.pages.dev
Proxy: Enabled (orange cloud)
```

**Option 2: A Record (Apex domain)**
```
Type: A
Name: @
Content: [Cloudflare IP provided in dashboard]
Proxy: Enabled (orange cloud)
```

**Option 3: AAAA Record (IPv6)**
```
Type: AAAA
Name: @
Content: [Cloudflare IPv6 provided in dashboard]
Proxy: Enabled (orange cloud)
```

### Redirecting Apex to www

```
# _redirects file
https://example.com/* https://www.example.com/:splat 301
```

### Multiple Custom Domains

You can add multiple custom domains to one project:

```
Primary: www.example.com
Additional:
  - example.com (redirects to www)
  - app.example.com
  - beta.example.com
```

Each gets automatic HTTPS certificate.

## Headers Configuration

### Creating _headers File

```
# _headers file (place in build output directory)

# Global headers (apply to all pages)
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  X-XSS-Protection: 1; mode=block
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()

# Security headers for HTML pages
/*.html
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'
  X-Frame-Options: SAMEORIGIN

# Cache static assets aggressively
/assets/*
  Cache-Control: public, max-age=31536000, immutable

/static/*
  Cache-Control: public, max-age=31536000, immutable

# Don't cache HTML
/*.html
  Cache-Control: public, max-age=0, must-revalidate

# API route headers
/api/*
  Access-Control-Allow-Origin: *
  Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
  Access-Control-Allow-Headers: Content-Type, Authorization
  Content-Type: application/json

# Font files
/*.woff2
  Cache-Control: public, max-age=31536000, immutable
  Access-Control-Allow-Origin: *
```

### Common Header Patterns

#### Security Headers (Recommended)

```
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  X-XSS-Protection: 1; mode=block
  Referrer-Policy: strict-origin-when-cross-origin
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

#### CORS Headers

```
/api/*
  Access-Control-Allow-Origin: https://example.com
  Access-Control-Allow-Methods: GET, POST, OPTIONS
  Access-Control-Allow-Headers: Content-Type, Authorization
  Access-Control-Max-Age: 86400
```

#### Cache Headers

```
# Static assets - cache forever
/assets/*
  Cache-Control: public, max-age=31536000, immutable

# HTML - never cache
/*.html
  Cache-Control: public, max-age=0, must-revalidate

# API responses - don't cache
/api/*
  Cache-Control: no-store, no-cache, must-revalidate
```

## Redirects & Rewrites

### Creating _redirects File

```
# _redirects file (place in build output directory)

# Redirect old URLs
/old-page       /new-page       301
/blog/old-post  /blog/new-post  301

# Redirect with splat (wildcard)
/blog/*         /posts/:splat   301

# Redirect entire domain
https://old-domain.com/*  https://new-domain.com/:splat  301

# Force HTTPS (Cloudflare does this by default, but explicit)
http://example.com/*  https://example.com/:splat  301

# Redirect apex to www
https://example.com/*  https://www.example.com/:splat  301

# SPA fallback (serve index.html for all routes)
/*  /index.html  200

# API proxy (rewrite without redirect)
/api/*  https://backend.example.com/:splat  200

# Temporary redirect
/maintenance  /503.html  302

# Redirect based on path parameter
/user/:id  /users/:id  301
```

### Advanced Redirect Patterns

#### Country-Based Redirects

```
# _redirects
/  /en  302  Country=US
/  /fr  302  Country=FR
/  /de  302  Country=DE
/  /es  302  Country=ES
```

#### Language Redirects

```
# _redirects
/  /en  302  Language=en
/  /fr  302  Language=fr
/  /es  302  Language=es
```

#### Conditional Redirects

```
# _redirects
# Redirect mobile users to mobile site
/  /mobile  302  Condition=mobile

# A/B testing
/  /variant-a  302  Cookie=ab_test=variant_a
/  /variant-b  302  Cookie=ab_test=variant_b
```

## Build Configuration Patterns

### Framework-Specific Configurations

#### Next.js Static Export

```toml
name = "nextjs-pages-site"
compatibility_date = "2025-01-15"

[build]
command = "npm run build && npm run export"

[[build.upload]]
format = "directory"
dir = "out"
```

```json
// package.json
{
  "scripts": {
    "build": "next build",
    "export": "next export"
  }
}
```

#### Vite + React

```toml
name = "vite-react-site"
compatibility_date = "2025-01-15"

[build]
command = "npm run build"

[[build.upload]]
format = "directory"
dir = "dist"
```

#### Astro

```toml
name = "astro-site"
compatibility_date = "2025-01-15"

[build]
command = "npm run build"

[[build.upload]]
format = "directory"
dir = "dist"
```

#### Hugo

```toml
name = "hugo-blog"
compatibility_date = "2025-01-15"

[build]
command = "hugo --minify"

[[build.upload]]
format = "directory"
dir = "public"
```

### Monorepo Configuration

```toml
name = "frontend-monorepo"
compatibility_date = "2025-01-15"

[build]
command = "cd packages/website && npm run build"
cwd = "../.."
watch_dirs = ["packages/website/src"]

[[build.upload]]
format = "directory"
dir = "packages/website/dist"
```

## Pages Functions Configuration

### Function Routes

Create `functions` directory in your project:

```
project/
├── public/           # Static files
├── functions/        # Pages Functions (API routes)
│   ├── api/
│   │   ├── hello.js
│   │   └── users/
│   │       └── [id].js
│   └── _middleware.js
└── wrangler.toml
```

### Function Example

```javascript
// functions/api/hello.js
export async function onRequest(context) {
  return new Response(JSON.stringify({
    message: 'Hello from Cloudflare Pages!',
    timestamp: new Date().toISOString()
  }), {
    headers: {
      'Content-Type': 'application/json'
    }
  });
}
```

### Dynamic Routes

```javascript
// functions/api/users/[id].js
export async function onRequest(context) {
  const id = context.params.id;

  return new Response(JSON.stringify({
    userId: id,
    name: `User ${id}`
  }), {
    headers: {
      'Content-Type': 'application/json'
    }
  });
}
```

### Middleware

```javascript
// functions/_middleware.js
export async function onRequest(context) {
  // Add custom header to all requests
  const response = await context.next();
  response.headers.set('X-Custom-Header', 'My Value');
  return response;
}
```

## Project Organization Best Practices

### Directory Structure

```
cloudflare-pages-project/
├── .env.example           # Template for environment variables
├── .env                   # Local development (git-ignored)
├── .env.production        # Production secrets (git-ignored)
├── .gitignore            # Exclude secrets and build artifacts
├── wrangler.toml         # Cloudflare Pages configuration
├── package.json          # Dependencies and scripts
├── src/                  # Source code
│   ├── components/
│   ├── pages/
│   └── utils/
├── public/               # Static assets (copied as-is)
│   ├── _headers          # Custom headers
│   ├── _redirects        # Redirects and rewrites
│   ├── robots.txt
│   └── favicon.ico
├── functions/            # Pages Functions (API routes)
│   ├── api/
│   │   └── endpoint.js
│   └── _middleware.js
└── dist/                 # Build output (git-ignored)
```

### gitignore Configuration

```gitignore
# Environment variables (CRITICAL - never commit secrets!)
.env
.env.local
.env.production
.env.*.local

# Build outputs
dist/
build/
out/
.next/
.output/

# Dependencies
node_modules/

# Logs
*.log
npm-debug.log*

# OS files
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Wrangler
.wrangler/
```

### Environment Variable Templates

```bash
# .env.example (commit this)
# Copy to .env for local development

# Build-time variables (public)
VITE_API_URL=https://api.example.com
VITE_GA_ID=UA-XXXXXXX-X

# Runtime secrets (private) - set via: wrangler pages secret put
# API_KEY=your-api-key-here
# DATABASE_URL=your-database-url
# STRIPE_SECRET=your-stripe-secret
```

## Multi-Environment Setup

### Environment Strategy

```
Production (main branch)
├── URL: https://project.pages.dev
├── Custom domain: https://www.example.com
└── Secrets: Production API keys

Staging (staging branch)
├── URL: https://staging.project.pages.dev
├── Custom domain: https://staging.example.com
└── Secrets: Staging API keys

Preview (all other branches)
├── URL: https://[commit-hash].project.pages.dev
└── Secrets: Shared preview secrets
```

### Branch-Based Configuration

```toml
# wrangler.toml

name = "my-multi-env-project"
compatibility_date = "2025-01-15"

[build]
command = "npm run build"

[[build.upload]]
dir = "dist"

[env.production]
# Production-specific config
route = "www.example.com/*"

[env.staging]
# Staging-specific config
route = "staging.example.com/*"
```

## Monitoring & Analytics

### Built-in Analytics

View analytics in Cloudflare Dashboard:
- Requests per second
- Bandwidth usage
- Cache hit rate
- Unique visitors
- Geographic distribution

Access: https://dash.cloudflare.com/ → Pages → Your Project → Analytics

### Custom Analytics Integration

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>

<!-- Plausible Analytics (privacy-friendly) -->
<script defer data-domain="example.com" src="https://plausible.io/js/script.js"></script>
```

### Real User Monitoring (RUM)

```javascript
// functions/_middleware.js
export async function onRequest(context) {
  const start = Date.now();
  const response = await context.next();
  const duration = Date.now() - start;

  // Log performance metric
  console.log(`Request took ${duration}ms`);

  // Add timing header
  response.headers.set('Server-Timing', `total;dur=${duration}`);

  return response;
}
```

## Security Configuration

### Content Security Policy

```
# _headers
/*
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.example.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self' data:; connect-src 'self' https://api.example.com; frame-ancestors 'none'; base-uri 'self'; form-action 'self'
```

### Rate Limiting (via Pages Functions)

```javascript
// functions/_middleware.js
const rateLimitMap = new Map();

export async function onRequest(context) {
  const clientIP = context.request.headers.get('CF-Connecting-IP');
  const now = Date.now();
  const windowMs = 60000; // 1 minute
  const maxRequests = 100;

  if (!rateLimitMap.has(clientIP)) {
    rateLimitMap.set(clientIP, { count: 1, resetTime: now + windowMs });
  } else {
    const record = rateLimitMap.get(clientIP);

    if (now > record.resetTime) {
      record.count = 1;
      record.resetTime = now + windowMs;
    } else {
      record.count++;
      if (record.count > maxRequests) {
        return new Response('Too Many Requests', { status: 429 });
      }
    }
  }

  return context.next();
}
```

## Troubleshooting Common Configuration Issues

### Issue: Environment Variables Not Working

**Build-time variables:**
```bash
# Check framework prefix
VITE_API_URL=...      # Vite
NEXT_PUBLIC_API=...   # Next.js
REACT_APP_API=...     # CRA

# Verify build includes variables
npm run build
grep -r "api.example.com" dist/
```

**Runtime secrets:**
```bash
# Verify secrets are set
wrangler pages secret list --project-name=my-website

# Check function can access
cat > functions/test.js <<EOF
export async function onRequest(context) {
  return new Response(JSON.stringify({
    hasApiKey: !!context.env.API_KEY
  }));
}
EOF
```

### Issue: Custom Domain Not Working

**Checklist:**
1. DNS records added? (Check Dashboard)
2. DNS propagated? (Check with `dig` or `nslookup`)
3. SSL certificate issued? (Can take up to 24 hours)
4. Proxying enabled? (Orange cloud in DNS settings)

```bash
# Check DNS
dig www.example.com +short

# Check HTTPS
curl -I https://www.example.com
```

### Issue: _headers or _redirects Not Applied

**Verify file location:**
```bash
# Must be in build output directory
ls -la dist/_headers
ls -la dist/_redirects

# Check after build
npm run build
ls -la dist/
```

**Test redirect:**
```bash
curl -I https://my-website.pages.dev/old-page
# Should show: Location: /new-page
```

## Resources

- **Pages Configuration**: https://developers.cloudflare.com/pages/configuration/
- **Build Configuration**: https://developers.cloudflare.com/pages/platform/build-configuration/
- **Custom Domains**: https://developers.cloudflare.com/pages/platform/custom-domains/
- **Headers**: https://developers.cloudflare.com/pages/platform/headers/
- **Redirects**: https://developers.cloudflare.com/pages/platform/redirects/
- **Pages Functions**: https://developers.cloudflare.com/pages/platform/functions/
- **Environment Variables**: https://developers.cloudflare.com/pages/platform/build-configuration/#environment-variables
