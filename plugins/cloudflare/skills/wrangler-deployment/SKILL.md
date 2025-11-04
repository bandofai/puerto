# Wrangler Deployment Skill

Expert knowledge for deploying static sites to Cloudflare Pages using Wrangler CLI.

## Overview

This skill provides comprehensive patterns, best practices, and troubleshooting guidance for deploying web applications to Cloudflare Pages using the official Wrangler CLI tool.

## Prerequisites

### Required Tools

1. **Wrangler CLI** (>= 3.0.0)
   ```bash
   npm install -g wrangler
   ```

2. **Node.js** (>= 18.0.0)
   ```bash
   node --version  # Should be >= v18.0.0
   ```

3. **Cloudflare Account**
   - Free account sufficient for most use cases
   - Pages included in all plans
   - Sign up: https://dash.cloudflare.com/sign-up

### Authentication Setup

```bash
# Method 1: OAuth (recommended for local development)
wrangler login
# Opens browser for authentication

# Method 2: API Token (recommended for CI/CD)
export CLOUDFLARE_API_TOKEN=your-token-here
wrangler whoami  # Verify authentication

# Verify authentication
wrangler whoami
# Output should show: "You are logged in as user@example.com"
```

## Core Concepts

### Cloudflare Pages Architecture

```
┌─────────────────────────────────────────────┐
│           Your Source Code                  │
│  (React, Vue, Svelte, Next.js, etc.)       │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│         Build Process (Local)               │
│  npm run build → generates static files     │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│       Wrangler CLI Upload                   │
│  wrangler pages deploy ./dist               │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│     Cloudflare Global CDN                   │
│  300+ Edge locations worldwide              │
│  Automatic HTTPS, DDoS protection           │
└─────────────────────────────────────────────┘
```

### Deployment Types

**1. Production Deployment**
- Triggered from main/master branch
- Gets production URL: `https://project-name.pages.dev`
- Visible to all users
- Should be stable and tested

**2. Preview Deployment**
- Triggered from any other branch
- Gets unique preview URL: `https://abc123.project-name.pages.dev`
- Used for testing before production
- Automatically cleaned up after branch deletion

## Deployment Patterns

### Pattern 1: Basic Deployment

```bash
# Step 1: Build your project
npm run build

# Step 2: Deploy to Cloudflare Pages
wrangler pages deploy ./dist --project-name=my-website
```

**When to use:**
- First deployment
- Simple static sites
- Quick prototyping
- Manual deployments

### Pattern 2: Branch-Based Deployment

```bash
# Production deployment (main branch)
git checkout main
npm run build
wrangler pages deploy ./dist \
  --project-name=my-website \
  --branch=main

# Preview deployment (feature branch)
git checkout feature/new-design
npm run build
wrangler pages deploy ./dist \
  --project-name=my-website \
  --branch=feature/new-design
```

**When to use:**
- Git-based workflows
- Multiple environments
- Preview before production
- Team collaboration

### Pattern 3: CI/CD Deployment

```yaml
# GitHub Actions example
name: Deploy to Cloudflare Pages

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build project
        run: npm run build

      - name: Deploy to Cloudflare Pages
        uses: cloudflare/wrangler-action@v3
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          command: pages deploy ./dist --project-name=my-website --branch=${{ github.ref_name }}
```

**When to use:**
- Automated deployments
- Continuous deployment
- Team workflows
- Production systems

### Pattern 4: Monorepo Deployment

```bash
# Deploy specific workspace from monorepo
cd packages/website
npm run build
wrangler pages deploy ./dist \
  --project-name=my-website-frontend \
  --branch=main

cd ../admin
npm run build
wrangler pages deploy ./dist \
  --project-name=my-website-admin \
  --branch=main
```

**When to use:**
- Multiple related projects
- Shared dependencies
- Coordinated deployments
- Large applications

## Build Configuration

### Common Framework Patterns

#### React (Create React App)

```json
{
  "scripts": {
    "build": "react-scripts build"
  }
}
```

Build output: `build/`

```bash
npm run build
wrangler pages deploy ./build --project-name=my-react-app
```

#### Vue.js

```json
{
  "scripts": {
    "build": "vue-cli-service build"
  }
}
```

Build output: `dist/`

```bash
npm run build
wrangler pages deploy ./dist --project-name=my-vue-app
```

#### Next.js (Static Export)

```json
{
  "scripts": {
    "build": "next build && next export"
  }
}
```

Build output: `out/`

```bash
npm run build
wrangler pages deploy ./out --project-name=my-nextjs-app
```

#### Svelte

```json
{
  "scripts": {
    "build": "vite build"
  }
}
```

Build output: `dist/`

```bash
npm run build
wrangler pages deploy ./dist --project-name=my-svelte-app
```

#### Astro

```json
{
  "scripts": {
    "build": "astro build"
  }
}
```

Build output: `dist/`

```bash
npm run build
wrangler pages deploy ./dist --project-name=my-astro-app
```

#### Hugo

```bash
# Hugo generates static files directly
hugo --minify

# Deploy
wrangler pages deploy ./public --project-name=my-hugo-blog
```

Build output: `public/`

## Advanced Deployment Options

### Include Git Metadata

```bash
wrangler pages deploy ./dist \
  --project-name=my-website \
  --branch=$(git branch --show-current) \
  --commit-hash=$(git rev-parse HEAD) \
  --commit-message="$(git log -1 --pretty=%B)"
```

**Benefits:**
- Trace deployments to source code
- Better deployment history
- Easier debugging
- Audit trail

### Specify Compatibility Date

```bash
wrangler pages deploy ./dist \
  --project-name=my-website \
  --compatibility-date=2025-01-15
```

**Use when:**
- Using Cloudflare-specific features
- Ensuring consistent behavior
- Testing new platform features

### Custom Headers

Create `_headers` file in your build output:

```
# _headers file
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin

/api/*
  Access-Control-Allow-Origin: *

/assets/*
  Cache-Control: public, max-age=31536000, immutable
```

Then deploy normally - Cloudflare Pages automatically applies headers.

### Redirects & Rewrites

Create `_redirects` file in your build output:

```
# _redirects file

# Redirect old blog to new location
/blog/* https://blog.example.com/:splat 301

# SPA fallback
/* /index.html 200

# Temporary redirect
/old-page /new-page 302

# Domain redirect
https://www.example.com/* https://example.com/:splat 301
```

## Environment Variables & Secrets

### Setting Secrets

```bash
# Interactive prompt (recommended for sensitive data)
wrangler pages secret put API_KEY --project-name=my-website

# From file
cat api-key.txt | wrangler pages secret put API_KEY --project-name=my-website

# From environment variable
echo "$MY_SECRET" | wrangler pages secret put API_KEY --project-name=my-website
```

### Listing Secrets

```bash
# List all secrets (values are hidden)
wrangler pages secret list --project-name=my-website
```

Output:
```
Secret Name       Uploaded At
API_KEY           2025-01-15T10:30:00Z
DATABASE_URL      2025-01-14T15:20:00Z
STRIPE_KEY        2025-01-13T09:45:00Z
```

### Accessing Secrets in Pages Functions

```javascript
// functions/api/hello.js
export async function onRequest(context) {
  const apiKey = context.env.API_KEY;

  return new Response(JSON.stringify({
    message: 'Hello from Cloudflare Pages!',
    authenticated: !!apiKey
  }), {
    headers: { 'Content-Type': 'application/json' }
  });
}
```

### Build-Time vs Runtime Variables

**Build-time** (set during `npm run build`):
```bash
# .env file
VITE_API_URL=https://api.example.com
NEXT_PUBLIC_GA_ID=UA-XXXXXXX
```

**Runtime** (set via Wrangler):
```bash
# Secrets accessible in Pages Functions
wrangler pages secret put STRIPE_SECRET_KEY --project-name=my-website
```

## Troubleshooting

### Issue: "Command not found: wrangler"

**Cause:** Wrangler CLI not installed or not in PATH

**Solution:**
```bash
# Install globally
npm install -g wrangler

# Or use with npx
npx wrangler pages deploy ./dist --project-name=my-website

# Verify installation
which wrangler
wrangler --version
```

### Issue: "You are not authenticated"

**Cause:** Not logged in to Cloudflare

**Solution:**
```bash
# Login via OAuth
wrangler login

# Or set API token
export CLOUDFLARE_API_TOKEN=your-token-here

# Verify authentication
wrangler whoami
```

### Issue: "Build directory not found"

**Cause:** Build hasn't run or wrong directory specified

**Solution:**
```bash
# Check if build directory exists
ls -la dist/  # or build/ or out/

# Run build command
npm run build

# Verify build output
ls -lah dist/

# Check common locations
for dir in dist build out public .next/out; do
  [ -d "$dir" ] && echo "Found: $dir"
done
```

### Issue: "Project not found"

**Cause:** Project doesn't exist in Cloudflare account

**Solution:**
```bash
# List existing projects
wrangler pages project list

# Create new project (happens automatically on first deploy)
wrangler pages deploy ./dist --project-name=my-new-project

# Or create via dashboard:
# https://dash.cloudflare.com/pages
```

### Issue: "Rate limit exceeded"

**Cause:** Too many API requests in short time

**Solution:**
```bash
# Wait indicated time (usually 60 seconds)
sleep 60

# Retry deployment
wrangler pages deploy ./dist --project-name=my-website

# Check for concurrent deployments
ps aux | grep wrangler

# Verify API token isn't being used elsewhere
```

### Issue: "File too large"

**Cause:** Individual file exceeds 25MB limit

**Solution:**
```bash
# Find large files
find dist/ -type f -size +25M

# Optimize images
# - Use modern formats (WebP, AVIF)
# - Compress with tools like imagemin
# - Use responsive images

# Split large bundles
# - Code splitting in webpack/vite
# - Dynamic imports
# - Lazy loading

# Use external hosting for large files
# - Cloudflare R2
# - AWS S3
# - CDN for media files
```

### Issue: "Deployment successful but site not updating"

**Cause:** Browser cache or CDN cache

**Solution:**
```bash
# Hard refresh browser
# Chrome/Firefox: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)

# Check deployment was successful
wrangler pages deployment list --project-name=my-website

# Verify latest deployment is active
curl -I https://my-website.pages.dev

# Purge Cloudflare cache (if using custom domain)
# Via dashboard: Cache → Purge Everything
```

### Issue: "404 errors after deployment"

**Cause:** SPA routing not configured

**Solution:**
```bash
# Create _redirects file
cat > dist/_redirects <<EOF
/* /index.html 200
EOF

# Or create _routes.json for more control
cat > dist/_routes.json <<EOF
{
  "version": 1,
  "include": ["/*"],
  "exclude": ["/api/*"]
}
EOF

# Redeploy
wrangler pages deploy ./dist --project-name=my-website
```

## Performance Optimization

### Enable Compression

Cloudflare automatically compresses responses, but you can pre-compress:

```bash
# Pre-compress files with gzip
find dist/ -type f \( -name "*.js" -o -name "*.css" -o -name "*.html" \) -exec gzip -k {} \;

# Pre-compress with brotli
find dist/ -type f \( -name "*.js" -o -name "*.css" -o -name "*.html" \) -exec brotli -k {} \;
```

### Optimize Assets

```bash
# Minify JavaScript and CSS (usually done by build tool)
npm run build  # with production mode

# Optimize images
npx @squoosh/cli --output-dir dist/images optimized/ *.{jpg,png}

# Remove source maps in production
# (configure in webpack/vite config)
```

### Cache Control Headers

```
# _headers file
/static/*
  Cache-Control: public, max-age=31536000, immutable

/*.html
  Cache-Control: public, max-age=0, must-revalidate

/api/*
  Cache-Control: private, no-cache
```

## Deployment Verification

### Automated Checks

```bash
#!/bin/bash
# deploy-verify.sh

PROJECT_NAME="my-website"
DEPLOY_URL="https://$PROJECT_NAME.pages.dev"

# Deploy
wrangler pages deploy ./dist --project-name=$PROJECT_NAME

# Wait for deployment to propagate
sleep 10

# Check HTTP status
STATUS=$(curl -o /dev/null -s -w "%{http_code}" $DEPLOY_URL)
if [ "$STATUS" -eq 200 ]; then
  echo "✅ Deployment successful: $DEPLOY_URL"
else
  echo "❌ Deployment failed: HTTP $STATUS"
  exit 1
fi

# Check critical pages
for page in "/about" "/contact" "/blog"; do
  STATUS=$(curl -o /dev/null -s -w "%{http_code}" "$DEPLOY_URL$page")
  if [ "$STATUS" -eq 200 ]; then
    echo "✅ $page is accessible"
  else
    echo "⚠️  $page returned HTTP $STATUS"
  fi
done
```

### Manual Verification Checklist

- [ ] Deployment URL accessible
- [ ] Homepage loads correctly
- [ ] All pages render properly
- [ ] Images load
- [ ] Forms work
- [ ] API endpoints respond
- [ ] Mobile layout correct
- [ ] HTTPS enabled
- [ ] Performance acceptable (Lighthouse check)
- [ ] No console errors

## Best Practices

### 1. Version Control Integration

```bash
# Tag releases
git tag -a v1.0.0 -m "Production release v1.0.0"
git push --tags

# Deploy with version info
wrangler pages deploy ./dist \
  --project-name=my-website \
  --commit-hash=$(git rev-parse HEAD)
```

### 2. Environment-Specific Builds

```bash
# Development build
NODE_ENV=development npm run build
wrangler pages deploy ./dist --project-name=my-website --branch=dev

# Production build
NODE_ENV=production npm run build
wrangler pages deploy ./dist --project-name=my-website --branch=main
```

### 3. Security Headers

```
# _headers file
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  X-XSS-Protection: 1; mode=block
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: accelerometer=(), camera=(), geolocation=(), microphone=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

### 4. Clean Build Before Deploy

```bash
# Remove old build artifacts
rm -rf dist/

# Fresh build
npm run build

# Verify build output
ls -lah dist/

# Deploy
wrangler pages deploy ./dist --project-name=my-website
```

### 5. Rollback Strategy

```bash
# List recent deployments
wrangler pages deployment list --project-name=my-website

# Save deployment IDs
# Production: abc123def456
# Previous: xyz789ghi012

# Rollback if needed
wrangler pages deployment promote xyz789ghi012 --project-name=my-website
```

## Resources

- **Wrangler CLI Docs**: https://developers.cloudflare.com/workers/wrangler/
- **Pages Platform Docs**: https://developers.cloudflare.com/pages/
- **Direct Upload Guide**: https://developers.cloudflare.com/pages/get-started/direct-upload/
- **Framework Guides**: https://developers.cloudflare.com/pages/framework-guides/
- **Cloudflare Community**: https://community.cloudflare.com/
- **Status Page**: https://www.cloudflarestatus.com/
