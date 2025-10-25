# Lighthouse Integration Skill

Expert knowledge for running Google Lighthouse audits, interpreting results, and integrating performance testing into development workflows.

## Overview

This skill provides comprehensive patterns for using Lighthouse CLI and programmatic API to audit web performance, accessibility, SEO, and best practices.

## Prerequisites

### Required Tools

1. **Lighthouse CLI** (>= 11.0.0)
   ```bash
   npm install -g lighthouse
   ```

2. **Chrome/Chromium** (>= 120)
   - Lighthouse requires a Chromium-based browser
   - Install Chrome: https://www.google.com/chrome/

3. **Node.js** (>= 18.0.0)
   ```bash
   node --version  # Should be >= v18.0.0
   ```

### Verification

```bash
# Check Lighthouse installation
lighthouse --version

# Test with a quick audit
lighthouse https://web.dev --only-categories=performance --quiet
```

## Core Concepts

### Lighthouse Architecture

```
┌─────────────────────────────────────────────┐
│          Target Website                     │
│     https://example.com                     │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│       Lighthouse Runner                     │
│  - Launches headless Chrome                 │
│  - Loads page with instrumentation          │
│  - Collects performance traces              │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│         Audits Execution                    │
│  - Performance metrics calculation          │
│  - Accessibility checks                     │
│  - SEO validation                           │
│  - Best practices analysis                  │
│  - PWA capability assessment                │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│          Report Generation                  │
│  - JSON (programmatic access)               │
│  - HTML (human-readable)                    │
│  - CSV (spreadsheet import)                 │
└─────────────────────────────────────────────┘
```

### Audit Categories

**1. Performance** (Weight: Critical)
- First Contentful Paint (FCP)
- Largest Contentful Paint (LCP)
- Total Blocking Time (TBT)
- Cumulative Layout Shift (CLS)
- Speed Index (SI)
- Time to Interactive (TTI)

**2. Accessibility** (Weight: High)
- Color contrast
- ARIA attributes
- Form labels
- Image alt text
- Semantic HTML

**3. Best Practices** (Weight: Medium)
- HTTPS usage
- Console errors
- Image aspect ratios
- Deprecated APIs
- Vulnerable libraries

**4. SEO** (Weight: Medium)
- Meta descriptions
- Crawlability
- Mobile friendliness
- Structured data
- Page titles

**5. PWA** (Weight: Optional)
- Service worker
- Manifest file
- Offline capability
- Install prompts
- HTTPS enforcement

## Audit Patterns

### Pattern 1: Basic Performance Audit

```bash
# Mobile audit (default)
lighthouse https://example.com \
  --only-categories=performance \
  --output=json \
  --output=html \
  --output-path=./lighthouse-mobile \
  --chrome-flags="--headless"

# Desktop audit
lighthouse https://example.com \
  --preset=desktop \
  --only-categories=performance \
  --output=json \
  --output-path=./lighthouse-desktop \
  --chrome-flags="--headless"
```

**When to use:**
- Quick performance check during development
- Before/after optimization comparisons
- Daily monitoring of key pages

**Output:**
- JSON report for programmatic analysis
- HTML report for visual inspection
- Performance score 0-100

---

### Pattern 2: Comprehensive Multi-Category Audit

```bash
# Full audit with all categories
lighthouse https://example.com \
  --output=json \
  --output=html \
  --output-path=./lighthouse-full \
  --chrome-flags="--headless" \
  --only-categories=performance,accessibility,best-practices,seo,pwa
```

**When to use:**
- Weekly comprehensive site health checks
- Pre-release validation
- Compliance audits (WCAG, etc.)

**What it checks:**
- All 100+ individual audits
- Comprehensive scoring across 5 categories
- Detailed recommendations for each failing audit

---

### Pattern 3: CI/CD Performance Gate

```bash
#!/bin/bash
# lighthouse-ci.sh

URL="https://staging.example.com"
THRESHOLD=90

# Run audit
lighthouse "$URL" \
  --only-categories=performance \
  --output=json \
  --output-path=./lighthouse-ci \
  --chrome-flags="--headless" \
  --quiet

# Extract score
SCORE=$(cat lighthouse-ci.report.json | jq -r '.categories.performance.score * 100')

# Compare against threshold
if (( $(echo "$SCORE < $THRESHOLD" | bc -l) )); then
    echo "❌ Performance score $SCORE is below threshold of $THRESHOLD"
    echo "Deployment blocked until performance improves"
    exit 1
else
    echo "✅ Performance score $SCORE meets threshold"
    exit 0
fi
```

**When to use:**
- Automated testing in CI/CD pipelines
- Preventing performance regressions
- Enforcing performance budgets

**Integration examples:**
- GitHub Actions
- GitLab CI
- CircleCI
- Jenkins

---

### Pattern 4: Multi-Page Audit Suite

```bash
#!/bin/bash
# audit-all-pages.sh

URLS=(
  "https://example.com"
  "https://example.com/about"
  "https://example.com/products"
  "https://example.com/contact"
)

mkdir -p ./audits

for URL in "${URLS[@]}"; do
  PAGE_NAME=$(echo "$URL" | sed 's/https:\/\///' | sed 's/\//-/g')

  echo "Auditing: $URL"

  lighthouse "$URL" \
    --output=json \
    --output-path="./audits/$PAGE_NAME" \
    --chrome-flags="--headless" \
    --quiet

  SCORE=$(cat "./audits/$PAGE_NAME.report.json" | jq -r '.categories.performance.score * 100')
  echo "  → Score: $SCORE/100"
done

# Generate summary
echo ""
echo "Multi-Page Audit Summary"
echo "========================"
for REPORT in ./audits/*.report.json; do
  PAGE=$(basename "$REPORT" .report.json)
  PERF=$(cat "$REPORT" | jq -r '.categories.performance.score * 100')
  A11Y=$(cat "$REPORT" | jq -r '.categories.accessibility.score * 100')
  SEO=$(cat "$REPORT" | jq -r '.categories.seo.score * 100')

  printf "%-30s | Perf: %3d | A11y: %3d | SEO: %3d\n" "$PAGE" "$PERF" "$A11Y" "$SEO"
done
```

**When to use:**
- Full site audits
- Identifying page-specific issues
- Comparing performance across pages

---

### Pattern 5: Custom Configuration Audit

```javascript
// lighthouse-config.js
module.exports = {
  extends: 'lighthouse:default',
  settings: {
    // Only run specific categories
    onlyCategories: ['performance', 'accessibility'],

    // Custom throttling (fast 3G)
    throttling: {
      rttMs: 150,
      throughputKbps: 1638.4,
      requestLatencyMs: 150,
      downloadThroughputKbps: 1638.4,
      uploadThroughputKbps: 675,
      cpuSlowdownMultiplier: 4
    },

    // Mobile emulation
    screenEmulation: {
      mobile: true,
      width: 375,
      height: 667,
      deviceScaleFactor: 2,
      disabled: false
    },

    // Form factor
    formFactor: 'mobile',
    maxWaitForLoad: 45000,
    skipAudits: ['uses-http2'] // Skip specific audits
  }
};
```

```bash
# Use custom config
lighthouse https://example.com \
  --config-path=./lighthouse-config.js \
  --output=json \
  --output-path=./custom-audit
```

**When to use:**
- Testing specific network conditions
- Simulating different devices
- Focusing on specific audit subsets

---

### Pattern 6: Programmatic Lighthouse (Node.js)

```javascript
// audit.js
const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');

async function runAudit(url) {
  // Launch Chrome
  const chrome = await chromeLauncher.launch({
    chromeFlags: ['--headless']
  });

  // Run Lighthouse
  const options = {
    logLevel: 'info',
    output: 'json',
    onlyCategories: ['performance'],
    port: chrome.port
  };

  const runnerResult = await lighthouse(url, options);

  // Extract metrics
  const { lhr } = runnerResult;
  const performanceScore = lhr.categories.performance.score * 100;
  const metrics = lhr.audits.metrics.details.items[0];

  console.log(`Performance Score: ${performanceScore}/100`);
  console.log(`FCP: ${metrics.firstContentfulPaint}ms`);
  console.log(`LCP: ${metrics.largestContentfulPaint}ms`);
  console.log(`TBT: ${metrics.totalBlockingTime}ms`);
  console.log(`CLS: ${metrics.cumulativeLayoutShift}`);

  // Cleanup
  await chrome.kill();

  return runnerResult;
}

// Usage
runAudit('https://example.com')
  .then(result => {
    // Save or process result
    console.log('Audit complete');
  })
  .catch(err => console.error(err));
```

**When to use:**
- Building custom performance dashboards
- Automated monitoring systems
- Integration with existing tools

---

## Interpreting Audit Results

### Performance Score Calculation

Lighthouse calculates performance score as a weighted average:

```
Performance Score =
  FCP  * 10% +
  SI   * 10% +
  LCP  * 25% +
  TTI  * 10% +
  TBT  * 30% +
  CLS  * 15%
```

**Score Ratings:**
- 90-100: Good (Green)
- 50-89: Needs Improvement (Orange)
- 0-49: Poor (Red)

### Core Web Vitals Thresholds

**LCP (Largest Contentful Paint):**
- Good: ≤ 2.5s
- Needs Improvement: ≤ 4.0s
- Poor: > 4.0s

**FID/TBT (First Input Delay / Total Blocking Time):**
- FID Good: ≤ 100ms
- TBT Good: ≤ 200ms
- FID Needs Improvement: ≤ 300ms
- Poor: > 300ms

**CLS (Cumulative Layout Shift):**
- Good: ≤ 0.1
- Needs Improvement: ≤ 0.25
- Poor: > 0.25

### Parsing JSON Reports

```bash
# Extract performance score
cat report.json | jq '.categories.performance.score * 100'

# Get all Core Web Vitals
cat report.json | jq '{
  lcp: .audits["largest-contentful-paint"].numericValue,
  fid: .audits["max-potential-fid"].numericValue,
  cls: .audits["cumulative-layout-shift"].numericValue,
  fcp: .audits["first-contentful-paint"].numericValue,
  tti: .audits["interactive"].numericValue,
  tbt: .audits["total-blocking-time"].numericValue
}'

# Find all failed audits (score < 0.9)
cat report.json | jq '
  .audits |
  to_entries |
  map(select(.value.score != null and .value.score < 0.9)) |
  map({id: .key, title: .value.title, score: .value.score})
'
```

---

## Common Issues and Solutions

### Issue 1: "Chrome not found"

**Error:**
```
Error: Lighthouse requires Chrome to run
```

**Solutions:**
1. Install Google Chrome
2. Set CHROME_PATH environment variable:
   ```bash
   export CHROME_PATH=/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome
   ```
3. Use system Chromium:
   ```bash
   export CHROME_PATH=/usr/bin/chromium
   ```

---

### Issue 2: "Connection refused / Timeout"

**Error:**
```
Error: connect ECONNREFUSED
```

**Solutions:**
1. Verify URL is accessible:
   ```bash
   curl -I https://example.com
   ```
2. Increase timeout:
   ```bash
   lighthouse https://example.com --max-wait-for-load=60000
   ```
3. Check firewall/proxy settings
4. Test with --disable-network-throttling flag

---

### Issue 3: Inconsistent Scores

**Problem:** Same page, different scores each run

**Solutions:**
1. Run multiple audits and average:
   ```bash
   for i in {1..5}; do
     lighthouse https://example.com --output=json --output-path="./run-$i" --quiet
   done

   # Calculate average
   jq -s 'map(.categories.performance.score) | add / length * 100' run-*.report.json
   ```

2. Use consistent throttling settings
3. Disable browser extensions (use --chrome-flags="--disable-extensions")
4. Clear cache between runs (--chrome-flags="--disable-cache")

---

## Best Practices

### 1. Audit Consistency

**Do:**
- Use same device/network settings for comparisons
- Run audits multiple times and average
- Audit at consistent times of day
- Use headless mode for automation

**Don't:**
- Compare mobile vs desktop scores directly
- Run audits during active deployments
- Mix throttled and unthrottled results
- Test on shared/unstable networks

### 2. Performance Budgets

```javascript
// budget.json
{
  "timings": [
    {
      "metric": "interactive",
      "budget": 5000
    },
    {
      "metric": "first-contentful-paint",
      "budget": 2000
    }
  ],
  "resourceSizes": [
    {
      "resourceType": "script",
      "budget": 250
    },
    {
      "resourceType": "image",
      "budget": 500
    },
    {
      "resourceType": "total",
      "budget": 1000
    }
  ]
}
```

```bash
# Test against budgets
lighthouse https://example.com --budget-path=./budget.json
```

### 3. Automated Monitoring

Set up regular audits:

```yaml
# .github/workflows/lighthouse.yml
name: Lighthouse CI
on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Lighthouse
        uses: treosh/lighthouse-ci-action@v10
        with:
          urls: |
            https://example.com
            https://example.com/about
          uploadArtifacts: true
```

## Resources

- **Lighthouse Docs**: https://developers.google.com/web/tools/lighthouse
- **Lighthouse Scoring**: https://web.dev/performance-scoring/
- **Core Web Vitals**: https://web.dev/vitals/
- **Lighthouse CI**: https://github.com/GoogleChrome/lighthouse-ci
- **Web.dev**: https://web.dev/
- **Chrome DevTools**: https://developer.chrome.com/docs/devtools/
