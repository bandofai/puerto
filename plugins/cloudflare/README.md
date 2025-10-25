# Cloudflare Pages Plugin

Deploy and manage Cloudflare Pages projects using Wrangler CLI with intelligent automation and monitoring.

## Overview

The Cloudflare Pages plugin provides specialized agents and comprehensive skills for deploying static sites to Cloudflare's global CDN, monitoring deployments, and managing project configuration.

### Key Features

- **Automated Deployments** - Deploy static sites with pre-flight checks and validation
- **Real-Time Log Monitoring** - Stream and analyze deployment logs
- **Project Management** - Handle projects, domains, and environment variables
- **Multi-Framework Support** - Works with React, Vue, Next.js, Astro, Hugo, and more
- **CI/CD Ready** - Includes GitHub Actions workflow template
- **Comprehensive Error Handling** - Clear troubleshooting guidance

### Why This Plugin?

Cloudflare does **not provide an official Pages MCP server**. This plugin uses **Wrangler CLI** (Cloudflare's official command-line tool) - the recommended approach for programmatic deployments.

## Prerequisites

### Required Software

1. **Node.js** >= 18.0.0
   ```bash
   node --version  # Should be v18.0.0 or higher
   ```

2. **Wrangler CLI** >= 3.0.0
   ```bash
   npm install -g wrangler
   wrangler --version
   ```

3. **Cloudflare Account** (Free tier available)
   - Sign up: https://dash.cloudflare.com/sign-up
   - Pages included in all plans

### Authentication Setup

```bash
# Method 1: OAuth (recommended for local use)
wrangler login
# Opens browser for authentication

# Method 2: API Token (recommended for CI/CD)
# Generate at: https://dash.cloudflare.com/profile/api-tokens
export CLOUDFLARE_API_TOKEN=your-token-here

# Verify authentication
wrangler whoami
```

## Installation

```bash
# Install the plugin
/plugin install cloudflare@puerto
```

## Quick Start

### 1. Deploy Your First Site

```
Deploy my website to Cloudflare Pages
```

The `pages-deployer` agent will:
- ✅ Check Wrangler installation
- ✅ Verify authentication
- ✅ Build your project (if needed)
- ✅ Deploy to Cloudflare Pages
- ✅ Provide deployment URL

### 2. Monitor Deployment Logs

```
Show me the deployment logs for my-website
```

The `log-monitor` agent will:
- Stream real-time logs
- Highlight errors and warnings
- Explain what's happening
- Suggest fixes if issues found

### 3. Manage Projects

```
List all my Cloudflare Pages projects
```

The `project-manager` agent will:
- Show all your projects
- Display deployment history
- Help configure settings
- Manage environment variables

## Plugin Components

### Agents

#### 1. pages-deployer (Sonnet)
**PROACTIVELY use when deploying to Cloudflare Pages**

Handles complete deployment workflow:
- Pre-flight system checks
- Build execution
- Deployment to Cloudflare Pages
- Progress monitoring
- Result reporting

**Example prompts:**
- "Deploy my React app to Cloudflare Pages"
- "Deploy the dist folder to my-website project"
- "Build and deploy to production"

#### 2. log-monitor (Haiku - Fast)
**PROACTIVELY use when monitoring deployment logs**

Monitors and analyzes logs:
- Real-time log streaming
- Error detection
- Log explanation
- Troubleshooting suggestions

**Example prompts:**
- "Show me deployment logs for my-website"
- "Why did my last deployment fail?"
- "Monitor the current deployment"

#### 3. project-manager (Haiku - Fast)
**PROACTIVELY use when managing Pages projects**

Manages project configuration:
- List all projects
- View project details
- Manage environment variables
- Configure custom domains
- Review deployment history

**Example prompts:**
- "List all my Cloudflare Pages projects"
- "Set API_KEY secret for my-website"
- "Show deployment history"

### Skills

#### 1. wrangler-deployment
Comprehensive deployment patterns:
- Framework-specific configurations
- CI/CD integration patterns
- Environment variable management
- Troubleshooting guides
- Performance optimization

#### 2. cloudflare-pages-config
Project configuration expertise:
- wrangler.toml structure
- Custom domain setup
- Headers and redirects
- Pages Functions configuration
- Security best practices

### Templates

#### 1. wrangler.toml
Project configuration template with:
- Framework-specific examples
- Build configuration
- Environment settings
- Upload configuration
- Advanced options

#### 2. .env.example
Environment variables guide:
- Build-time vs runtime variables
- Security best practices
- Framework-specific prefixes
- Secret management instructions
- Bulk setup scripts

#### 3. github-actions-deploy.yml
CI/CD workflow template:
- Automated deployments
- Multi-environment support
- Test integration
- PR preview deployments
- Deployment notifications

## Usage Examples

### Basic Deployment

```
User: Deploy my website to Cloudflare Pages

Agent: I'll deploy your website to Cloudflare Pages. Let me start with pre-flight checks...

[Runs checks]
✓ Wrangler CLI found (v3.15.0)
✓ Authenticated as user@example.com
✓ Node.js version 18.19.0 is compatible

What directory contains your built assets?
(Common: dist/, build/, out/, public/)

User: dist

Agent: Building your project...
npm run build
✓ Build complete!

Deploying to Cloudflare Pages...
wrangler pages deploy ./dist --project-name=my-website

✅ Deployment successful!
Project: my-website
URL: https://my-website.pages.dev
```

### Monitor Logs

```
User: Show me the deployment logs

Agent: Streaming deployment logs for my-website...

[build] > my-website@1.0.0 build
[build] > vite build
[build] ✓ 234 modules transformed
[build] ✓ built in 1.23s

[upload] ✨ Uploading...
[upload] ✅ Success! Uploaded 42 files

[deploy] 🌍 Deployment complete!
Production URL: https://my-website.pages.dev
```

### Manage Environment Variables

```
User: Set my API_KEY secret

Agent: I'll set the API_KEY secret for your project.

wrangler pages secret put API_KEY --project-name=my-website

Enter a secret value: **********************

✅ Secret API_KEY created successfully

You can now access this in Pages Functions:
const apiKey = context.env.API_KEY;
```

### Configure Custom Domain

```
User: How do I add a custom domain?

Agent: To add a custom domain to your Cloudflare Pages project:

1. Go to Cloudflare Dashboard:
   https://dash.cloudflare.com/

2. Navigate to: Workers & Pages → my-website → Custom domains

3. Click "Set up a custom domain"

4. Enter your domain (e.g., www.example.com)

5. Update DNS with provided records:
   Type: CNAME
   Name: www
   Content: my-website.pages.dev
   Proxy: Enabled (orange cloud)

6. Wait for SSL certificate (up to 24 hours)

Would you like me to verify your DNS configuration?
```

## Framework Support

### React (Create React App)

```bash
# Build output: build/
npm run build
wrangler pages deploy ./build --project-name=my-react-app
```

### Vue.js

```bash
# Build output: dist/
npm run build
wrangler pages deploy ./dist --project-name=my-vue-app
```

### Next.js (Static Export)

```json
{
  "scripts": {
    "build": "next build && next export"
  }
}
```

```bash
# Build output: out/
npm run build
wrangler pages deploy ./out --project-name=my-nextjs-app
```

### Svelte/SvelteKit

```bash
# Build output: build/ or dist/
npm run build
wrangler pages deploy ./build --project-name=my-svelte-app
```

### Astro

```bash
# Build output: dist/
npm run build
wrangler pages deploy ./dist --project-name=my-astro-site
```

### Hugo

```bash
# Build output: public/
hugo --minify
wrangler pages deploy ./public --project-name=my-hugo-blog
```

## Configuration

### Project Configuration (wrangler.toml)

```toml
name = "my-pages-project"
compatibility_date = "2025-01-15"

[build]
command = "npm run build"
cwd = "."
watch_dirs = ["src", "public"]

[[build.upload]]
format = "directory"
dir = "dist"

[env.production]
# Production settings

[env.preview]
# Preview settings
```

### Environment Variables

**Build-time (public):**
```bash
# .env
VITE_API_URL=https://api.example.com
NEXT_PUBLIC_GA_ID=UA-XXXXXXX
```

**Runtime (secrets):**
```bash
# Set via Wrangler
wrangler pages secret put API_KEY --project-name=my-website
wrangler pages secret put DATABASE_URL --project-name=my-website
```

### Custom Headers (_headers file)

```
# Place in your build output directory

/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin

/assets/*
  Cache-Control: public, max-age=31536000, immutable
```

### Redirects (_redirects file)

```
# Place in your build output directory

# Redirect old URLs
/old-page  /new-page  301

# SPA fallback
/*  /index.html  200

# Redirect apex to www
https://example.com/*  https://www.example.com/:splat  301
```

## CI/CD Integration

### GitHub Actions

1. Add workflow file: `.github/workflows/deploy.yml`
   (Use template from `templates/github-actions-deploy.yml`)

2. Add secrets to repository:
   - `CLOUDFLARE_API_TOKEN` - Your API token
   - `CLOUDFLARE_ACCOUNT_ID` - Your account ID

3. Push to trigger deployment:
   ```bash
   git push origin main
   ```

### GitLab CI

```yaml
# .gitlab-ci.yml
deploy:
  image: node:18
  script:
    - npm ci
    - npm run build
    - npx wrangler pages deploy ./dist --project-name=my-website
  only:
    - main
```

### Other CI Systems

Install Wrangler and run:
```bash
npm ci
npm run build
npx wrangler pages deploy ./dist --project-name=my-website
```

Set `CLOUDFLARE_API_TOKEN` environment variable in CI settings.

## Troubleshooting

### "Wrangler not found"

```bash
# Install Wrangler globally
npm install -g wrangler

# Or use with npx
npx wrangler pages deploy ./dist --project-name=my-website
```

### "Not authenticated"

```bash
# Login via OAuth
wrangler login

# Or set API token
export CLOUDFLARE_API_TOKEN=your-token-here
```

### "Build directory not found"

```bash
# Run build first
npm run build

# Check if build directory exists
ls -la dist/  # or build/ or out/
```

### "Project not found"

```bash
# List existing projects
wrangler pages project list

# Create new project (happens automatically on first deploy)
wrangler pages deploy ./dist --project-name=my-new-project
```

### "Rate limit exceeded"

Wait 60 seconds and retry. Avoid concurrent deployments.

### "File too large"

Cloudflare Pages has a 25MB per file limit. Optimize large files:
- Use modern image formats (WebP, AVIF)
- Enable code splitting
- Host large files on Cloudflare R2 or external CDN

### "Deployment successful but site not updating"

```bash
# Hard refresh browser
# Chrome/Firefox: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)

# Check deployment is active
wrangler pages deployment list --project-name=my-website
```

## Best Practices

### 1. Version Control

- ✅ Commit `wrangler.toml`
- ✅ Commit `.env.example`
- ❌ Never commit `.env` or `.env.production`
- ❌ Never commit secrets

### 2. Security

- Use different secrets for production vs development
- Rotate API tokens regularly
- Use API tokens with minimal required permissions
- Store production secrets in secure password manager

### 3. Deployment Strategy

- Test locally before deploying: `wrangler pages dev ./dist`
- Use preview deployments for feature branches
- Deploy production from `main` branch only
- Include commit hash in deployments for traceability

### 4. Performance

- Enable compression (automatic)
- Set appropriate cache headers
- Optimize images and assets
- Use code splitting
- Pre-compress large text files

### 5. Monitoring

- Monitor deployment logs
- Check Cloudflare Analytics
- Set up alerts for failures
- Review deployment history regularly

## Resources

### Official Documentation

- **Cloudflare Pages**: https://developers.cloudflare.com/pages/
- **Wrangler CLI**: https://developers.cloudflare.com/workers/wrangler/
- **Direct Upload**: https://developers.cloudflare.com/pages/get-started/direct-upload/
- **Framework Guides**: https://developers.cloudflare.com/pages/framework-guides/

### Community

- **Cloudflare Community**: https://community.cloudflare.com/
- **Discord**: https://discord.cloudflare.com/
- **Status Page**: https://www.cloudflarestatus.com/

### Tools

- **Cloudflare Dashboard**: https://dash.cloudflare.com/
- **API Token Generator**: https://dash.cloudflare.com/profile/api-tokens
- **Pages Documentation**: https://pages.cloudflare.com/

## Contributing

Found a bug or have a feature request? Please open an issue on the Puerto repository.

## License

MIT

## Author

Puerto Plugin System

---

**Need Help?**

Ask the agents:
- "How do I deploy to Cloudflare Pages?"
- "Show me my deployment logs"
- "How do I configure a custom domain?"
- "What environment variables do I need?"
