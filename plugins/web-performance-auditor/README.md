# Web Performance Auditor Plugin

Comprehensive web performance auditing and optimization using Google Lighthouse with actionable recommendations and automated monitoring capabilities.

## Overview

This plugin provides a complete toolkit for auditing, analyzing, and optimizing web application performance. It leverages Google Lighthouse for industry-standard performance metrics and Core Web Vitals tracking, with specialized agents for different aspects of performance optimization.

## Features

### 3 Specialized Agents

1. **lighthouse-auditor** (Sonnet) - Lighthouse audit execution
   - Runs comprehensive Lighthouse audits
   - Supports mobile and desktop testing
   - Multiple output formats (JSON, HTML, CSV)
   - Pre-flight system checks
   - Trend tracking and historical comparison
   - CI/CD integration support

2. **performance-analyzer** (Sonnet) - Deep performance analysis
   - Analyzes Lighthouse report data
   - Interprets Core Web Vitals metrics
   - Identifies performance patterns and issues
   - Prioritizes optimizations by impact
   - Trend analysis over time
   - Competitive benchmarking

3. **optimization-recommender** (Haiku, Cost-Effective) - Actionable recommendations
   - Generates specific code examples
   - Framework-specific guidance (React, Next.js, Vue)
   - Prioritized implementation plans
   - Effort estimation for each fix
   - Before/after validation steps

### 2 Comprehensive Skills

1. **lighthouse-integration** - Lighthouse CLI and API mastery
   - Installation and setup
   - Audit execution patterns
   - Configuration customization
   - Report parsing and analysis
   - CI/CD integration
   - MCP server integration
   - Troubleshooting guide

2. **web-performance-optimization** - Modern performance best practices
   - Critical rendering path optimization
   - Image optimization strategies
   - JavaScript optimization techniques
   - Layout stability (CLS) fixes
   - Caching and delivery optimization
   - Framework-specific patterns
   - Real User Monitoring (RUM)

### 3 Templates

1. **lighthouse-config.json** - Custom Lighthouse configuration
2. **performance-budget.json** - Performance budget thresholds
3. **github-actions-lighthouse.yml** - CI/CD automation workflow

## Installation

### Prerequisites

```bash
# Install Lighthouse CLI globally
npm install -g lighthouse

# Verify installation
lighthouse --version

# Install Chrome/Chromium (required by Lighthouse)
# macOS: Download from https://www.google.com/chrome/
# Linux: sudo apt-get install chromium-browser
```

### Plugin Installation

This plugin is part of the Puerto plugin system. It will be automatically available when Puerto is installed.

## Quick Start

### Running a Basic Audit

```bash
# Use the lighthouse-auditor agent
claude-code
> Use lighthouse-auditor to audit https://example.com
```

The agent will:
1. Check Lighthouse installation
2. Verify Chrome availability
3. Run a comprehensive audit
4. Generate HTML and JSON reports
5. Display a summary of results

### Analyzing Results

```bash
> Use performance-analyzer to analyze the latest Lighthouse report
```

The agent will:
1. Load the most recent audit report
2. Extract and analyze metrics
3. Identify critical issues
4. Prioritize optimizations
5. Generate a detailed analysis report

### Getting Recommendations

```bash
> Use optimization-recommender to fix the performance issues
```

The agent will:
1. Review failed audits
2. Generate specific code examples
3. Provide implementation guides
4. Estimate effort for each fix
5. Create a prioritized action plan

## Usage Examples

### Example 1: Quick Performance Check

```bash
# Audit a single page
lighthouse https://example.com \
  --only-categories=performance \
  --output=json \
  --output=html \
  --chrome-flags="--headless"
```

**Use Case:** Daily development workflow, quick performance validation

### Example 2: Comprehensive Site Audit

```bash
# Full audit with all categories
lighthouse https://example.com \
  --output=json \
  --output=html \
  --chrome-flags="--headless"
```

**Use Case:** Weekly health checks, pre-release validation

### Example 3: Multi-Page Audit

```bash
# Audit multiple critical pages
for url in \
  "https://example.com" \
  "https://example.com/products" \
  "https://example.com/checkout"; do

  lighthouse "$url" \
    --output=json \
    --output-path="./audit-$(basename $url)" \
    --chrome-flags="--headless"
done
```

**Use Case:** Comprehensive site performance overview

### Example 4: CI/CD Performance Gate

```yaml
# .github/workflows/lighthouse.yml
name: Performance Check
on: [pull_request]

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Lighthouse
        run: |
          lighthouse https://staging.example.com \
            --output=json \
            --chrome-flags="--headless"
      - name: Check threshold
        run: |
          SCORE=$(cat lighthouse-report.json | jq '.categories.performance.score * 100')
          if [ "$SCORE" -lt 90 ]; then exit 1; fi
```

**Use Case:** Prevent performance regressions in CI/CD

## Agent Details

### lighthouse-auditor

**When to Use:**
- Running new performance audits
- Setting up automated monitoring
- Comparing before/after optimization

**Capabilities:**
- ✅ Pre-flight system checks
- ✅ Mobile and desktop audits
- ✅ Custom configuration support
- ✅ Multiple output formats
- ✅ Trend tracking
- ✅ CI/CD integration

**Example Invocation:**
```
Use lighthouse-auditor to:
- Audit https://example.com for mobile and desktop
- Generate HTML and JSON reports
- Compare with last week's results
```

---

### performance-analyzer

**When to Use:**
- Understanding Lighthouse results
- Identifying root causes of poor performance
- Prioritizing optimization efforts

**Capabilities:**
- ✅ Core Web Vitals assessment
- ✅ Metric interpretation
- ✅ Issue categorization
- ✅ Impact prioritization
- ✅ Trend analysis
- ✅ Competitive benchmarking

**Example Invocation:**
```
Use performance-analyzer to:
- Analyze the latest audit report
- Identify why LCP is failing
- Compare performance vs last month
```

---

### optimization-recommender

**When to Use:**
- Implementing performance fixes
- Need specific code examples
- Planning optimization sprints

**Capabilities:**
- ✅ Actionable code examples
- ✅ Framework-specific guidance
- ✅ Effort estimation
- ✅ Priority ranking
- ✅ Implementation plans
- ✅ Validation steps

**Example Invocation:**
```
Use optimization-recommender to:
- Fix the CLS issues
- Provide Next.js-specific optimizations
- Create a 2-week implementation plan
```

## Performance Metrics Explained

### Core Web Vitals

**LCP (Largest Contentful Paint)**
- **What:** Time to render the largest visible element
- **Target:** ≤ 2.5s (good), ≤ 4s (needs improvement)
- **Impact:** Loading performance perception

**FID (First Input Delay)**
- **What:** Time from first user interaction to browser response
- **Target:** ≤ 100ms (good), ≤ 300ms (needs improvement)
- **Impact:** Interactivity and responsiveness

**CLS (Cumulative Layout Shift)**
- **What:** Visual stability, unexpected layout shifts
- **Target:** ≤ 0.1 (good), ≤ 0.25 (needs improvement)
- **Impact:** Visual stability and user frustration

### Other Key Metrics

**FCP (First Contentful Paint)**
- Time to first visible content
- Target: ≤ 1.8s

**TTI (Time to Interactive)**
- When page becomes fully interactive
- Target: ≤ 3.8s

**TBT (Total Blocking Time)**
- Main thread blocking time
- Target: ≤ 200ms

**Speed Index**
- How quickly content is visually displayed
- Target: ≤ 3.4s

## Optimization Strategies

### Quick Wins (1-2 days)

1. **Add lazy loading to images**
   ```html
   <img src="image.jpg" loading="lazy" alt="Description">
   ```

2. **Defer non-critical JavaScript**
   ```html
   <script defer src="analytics.js"></script>
   ```

3. **Set explicit image dimensions**
   ```html
   <img src="hero.jpg" width="1200" height="600" alt="Hero">
   ```

4. **Enable compression**
   ```javascript
   // Express.js
   app.use(compression());
   ```

**Expected Impact:** +10-15 performance score points

### Medium Effort (1 week)

1. **Convert images to WebP/AVIF**
2. **Implement responsive images (srcset)**
3. **Inline critical CSS**
4. **Fix CLS issues**
5. **Code splitting**

**Expected Impact:** +15-20 performance score points

### Major Refactoring (2-3 weeks)

1. **Remove unused JavaScript**
2. **Implement service worker caching**
3. **Optimize third-party scripts**
4. **Web Workers for heavy computation**

**Expected Impact:** +10-15 performance score points

## Templates

### Lighthouse Configuration

Use `templates/lighthouse-config.json` for custom audit settings:

```json
{
  "extends": "lighthouse:default",
  "settings": {
    "onlyCategories": ["performance", "accessibility"],
    "throttling": {
      "rttMs": 40,
      "throughputKbps": 10240
    }
  }
}
```

### Performance Budget

Use `templates/performance-budget.json` to enforce budgets:

```json
{
  "timings": [
    {
      "metric": "interactive",
      "budget": 5000
    }
  ],
  "resourceSizes": [
    {
      "resourceType": "script",
      "budget": 250
    }
  ]
}
```

### CI/CD Integration

Use `templates/github-actions-lighthouse.yml` for automated testing:

```yaml
name: Lighthouse CI
on: [push, pull_request]
jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Lighthouse
        run: lighthouse https://example.com
```

## Best Practices

### 1. Audit Consistency

- Run audits multiple times and average results
- Use same device/network settings for comparisons
- Test at consistent times of day
- Use headless mode for automation

### 2. Metric Prioritization

**Focus Order:**
1. Core Web Vitals (LCP, FID, CLS) - Google ranking signals
2. Time to Interactive - User experience
3. Total Blocking Time - Interactivity
4. Resource optimization - Page weight

### 3. Continuous Monitoring

- Set up daily automated audits
- Track trends over time
- Alert on regressions
- Monitor competitor performance

### 4. Development Workflow

```
Development → Audit → Analyze → Optimize → Validate → Deploy
     ↑                                                      ↓
     ←───────────────── Monitor Performance ←──────────────┘
```

## Troubleshooting

### Lighthouse Installation Issues

**Error:** "Lighthouse not found"
```bash
# Install globally
npm install -g lighthouse

# Verify
lighthouse --version
```

**Error:** "Chrome not found"
```bash
# macOS
export CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Linux
export CHROME_PATH=/usr/bin/google-chrome
```

### Inconsistent Scores

**Problem:** Different scores each run

**Solutions:**
1. Run multiple audits and average
2. Use consistent throttling settings
3. Clear cache between runs: `--chrome-flags="--disable-cache"`
4. Disable extensions: `--chrome-flags="--disable-extensions"`

### Timeout Issues

**Error:** "Lighthouse timed out"

**Solutions:**
```bash
# Increase timeout
lighthouse https://example.com --max-wait-for-load=60000

# Disable network throttling
lighthouse https://example.com --throttling-method=provided
```

## Resources

### Official Documentation
- **Lighthouse**: https://developers.google.com/web/tools/lighthouse
- **Core Web Vitals**: https://web.dev/vitals/
- **Web.dev**: https://web.dev/performance/

### Tools
- **PageSpeed Insights**: https://pagespeed.web.dev/
- **Chrome DevTools**: https://developer.chrome.com/docs/devtools/
- **Lighthouse CI**: https://github.com/GoogleChrome/lighthouse-ci
- **web-vitals.js**: https://github.com/GoogleChrome/web-vitals

### Learning Resources
- **Web Performance**: https://web.dev/fast/
- **Image Optimization**: https://web.dev/fast/#optimize-your-images
- **JavaScript Performance**: https://web.dev/fast/#optimize-your-javascript
- **Performance Budgets**: https://web.dev/performance-budgets-101/

## Contributing

This plugin is part of the Puerto ecosystem. Contributions are welcome!

## License

MIT

---

**Part of the Puerto Plugin System**
For more information, visit: https://github.com/yourusername/puerto
