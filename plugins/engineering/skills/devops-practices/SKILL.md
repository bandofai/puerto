# DevOps Practices

**CI/CD, Infrastructure, Deployment, and Monitoring**

Consolidated from:
- devops-engineer skills
- cloud-architect skills
- site-reliability-engineer skills
- release-manager skills

# CI/CD Patterns Skill

**Expert-level CI/CD pipeline design patterns and best practices**

## Core Principles

1. **Pipeline as Code**: All pipeline configuration in version control
2. **Fast Feedback**: Fail fast, provide clear error messages
3. **Build Once**: Build artifacts once, deploy everywhere
4. **Idempotent**: Running twice produces same result
5. **Secure by Default**: Security scanning integrated, not optional

## Multi-Stage Pipeline Pattern

```
┌─────────┐   ┌──────┐   ┌──────────┐   ┌────────┐   ┌────────┐
│  Build  │──>│ Test │──>│ Security │──>│ Deploy │──>│ Verify │
└─────────┘   └──────┘   └──────────┘   └────────┘   └────────┘
    Fast        Medium        Slow          Manual      Quick
   (<2 min)    (<5 min)    (<10 min)    (Approval)   (<2 min)
```

### Stage Ordering
1. **Build**: Compile code, create artifacts (fast fail)
2. **Test**: Unit → Integration → E2E (fastest first)
3. **Security**: SAST → Dependency scan → Container scan
4. **Deploy**: Dev → Staging → Prod (progressive)
5. **Verify**: Smoke tests, health checks

## Optimization Strategies

### 1. Caching
```yaml
# Cache dependencies
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .pip/
    - .m2/
    - .gradle/
```

**Impact**: 50-80% faster builds

### 2. Parallelization
```yaml
# Run tests in parallel
test:
  parallel: 4
  script:
    - npm test -- --shard=${CI_NODE_INDEX}/${CI_NODE_TOTAL}
```

**Impact**: 4x faster test execution

### 3. Conditional Execution
```yaml
# Skip unnecessary steps
deploy:
  only:
    - main
    - /^release-.*$/
  changes:
    - src/**
    - Dockerfile
```

**Impact**: Reduce unnecessary runs by 70%

### 4. Docker Layer Caching
```dockerfile
# Multi-stage build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

FROM node:18-alpine
COPY --from=builder /app/dist /app/dist
COPY --from=builder /app/node_modules /app/node_modules
```

**Impact**: 10x faster Docker builds

## Security Scanning Integration

### SAST (Static Application Security Testing)
```yaml
sast:
  stage: security
  image: returntocorp/semgrep
  script:
    - semgrep --config=auto --json --output=sast-report.json .
  artifacts:
    reports:
      sast: sast-report.json
```

**Tools**:
- **Semgrep**: Fast, customizable (free)
- **SonarQube**: Comprehensive code quality
- **CodeQL**: GitHub's semantic analysis

### Dependency Scanning
```yaml
dependency_scan:
  stage: security
  script:
    - npm audit --audit-level=high
    - snyk test --severity-threshold=high
  allow_failure: false  # Fail on critical vulnerabilities
```

**Tools**:
- **Snyk**: Comprehensive, auto-fix (free tier)
- **Dependabot**: GitHub native
- **npm audit**: Built-in Node.js
- **safety**: Python packages

### Container Scanning
```yaml
container_scan:
  stage: security
  image: aquasec/trivy
  script:
    - trivy image --severity HIGH,CRITICAL myapp:${CI_COMMIT_SHA}
```

**Tools**:
- **Trivy**: Fast, accurate (free)
- **Clair**: CoreOS project
- **Anchore**: Policy-based

### Secret Detection
```yaml
secrets_scan:
  stage: security
  image: zricethezav/gitleaks
  script:
    - gitleaks detect --source . --verbose
```

**Tools**:
- **Gitleaks**: Fast, configurable
- **TruffleHog**: High accuracy
- **git-secrets**: AWS focus

## Testing Strategies

### Test Pyramid
```
        /\
       /  \     E2E Tests (5%)
      /____\    Slow, brittle
     /      \
    / Integration \ (15%)
   /________________\
  /                  \
 /   Unit Tests (80%) \ Fast, reliable
/______________________\
```

### Test Execution Order
1. **Linting**: Fastest, catches syntax errors
2. **Unit tests**: Fast, isolated
3. **Integration tests**: Medium, database/API
4. **E2E tests**: Slow, full system

### Coverage Requirements
```yaml
test:
  script:
    - npm test -- --coverage --coverageThreshold='{"global":{"branches":80,"functions":80,"lines":80}}'
```

**Thresholds**:
- **Unit**: ≥80% coverage (enforce)
- **Integration**: ≥60% coverage (goal)
- **E2E**: Critical paths only

## Artifact Management

### Build Artifacts
```yaml
build:
  script:
    - npm run build
  artifacts:
    name: "build-${CI_COMMIT_SHA}"
    paths:
      - dist/
    expire_in: 1 week
```

### Docker Images
```yaml
build_image:
  script:
    - docker build -t ${REGISTRY}/${IMAGE}:${CI_COMMIT_SHA} .
    - docker tag ${REGISTRY}/${IMAGE}:${CI_COMMIT_SHA} ${REGISTRY}/${IMAGE}:latest
    - docker push ${REGISTRY}/${IMAGE}:${CI_COMMIT_SHA}
    - docker push ${REGISTRY}/${IMAGE}:latest
```

**Tagging Strategy**:
- **Commit SHA**: Immutable, traceable
- **Semantic version**: v1.2.3 (releases)
- **Branch name**: develop, staging
- **latest**: Most recent (use with caution)

## Deployment Patterns

### Environment Progression
```
Commit → Dev (auto) → Staging (auto) → Prod (manual)
```

### Deployment with Approval
```yaml
deploy_prod:
  stage: deploy
  environment:
    name: production
    url: https://app.example.com
  when: manual  # Require manual trigger
  only:
    - main
  script:
    - ./deploy.sh production
```

### Deployment with Verification
```yaml
deploy:
  script:
    - ./deploy.sh
    - |
      # Wait for deployment
      for i in {1..30}; do
        if curl -f https://app.example.com/health; then
          echo "Deployment successful!"
          exit 0
        fi
        sleep 10
      done
      echo "Deployment failed!"
      exit 1
```

### Rollback on Failure
```yaml
deploy:
  script:
    - ./deploy.sh || (./rollback.sh && exit 1)
```

## Notification Patterns

### Slack Notifications
```yaml
notify_slack:
  stage: .post
  when: on_failure
  script:
    - |
      curl -X POST -H 'Content-type: application/json' \
        --data "{
          \"text\": \"Pipeline failed for ${CI_PROJECT_NAME} on ${CI_COMMIT_BRANCH}\",
          \"attachments\": [{
            \"color\": \"danger\",
            \"fields\": [{
              \"title\": \"Commit\",
              \"value\": \"${CI_COMMIT_SHORT_SHA}: ${CI_COMMIT_MESSAGE}\"
            }, {
              \"title\": \"Author\",
              \"value\": \"${CI_COMMIT_AUTHOR}\"
            }, {
              \"title\": \"Pipeline\",
              \"value\": \"${CI_PIPELINE_URL}\"
            }]
          }]
        }" \
        ${SLACK_WEBHOOK_URL}
```

### Email on Production Deploy
```yaml
notify_email:
  stage: .post
  only:
    - main
  script:
    - |
      echo "Deployed ${CI_COMMIT_SHORT_SHA} to production" | \
        mail -s "Production Deployment" team@example.com
```

## Branch Protection

### Required Checks
```yaml
# .github/workflows/required-checks.yml
name: Required Checks
on: [pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run lint

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm test

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm audit
```

### GitHub Branch Protection Rules
- Require pull request reviews (1-2 reviewers)
- Require status checks to pass
- Require branches to be up to date
- Include administrators
- Restrict force pushes

## Common Patterns by Platform

### GitHub Actions
```yaml
name: CI/CD
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: 18
  REGISTRY: ghcr.io

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm run build
      - run: npm test -- --coverage
      - uses: codecov/codecov-action@v3
```

### GitLab CI
```yaml
stages:
  - build
  - test
  - security
  - deploy

variables:
  DOCKER_DRIVER: overlay2
  SECURE_ANALYZERS_PREFIX: "registry.gitlab.com/security-products"

build:
  stage: build
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/

test:
  stage: test
  script:
    - npm test -- --coverage
  coverage: '/All files[^|]*\|[^|]*\s+([\d\.]+)/'
```

### Jenkins
```groovy
pipeline {
    agent any

    environment {
        NODE_VERSION = '18'
        REGISTRY = 'registry.example.com'
    }

    stages {
        stage('Build') {
            steps {
                sh 'npm ci'
                sh 'npm run build'
            }
        }

        stage('Test') {
            parallel {
                stage('Unit') {
                    steps {
                        sh 'npm test'
                    }
                }
                stage('Lint') {
                    steps {
                        sh 'npm run lint'
                    }
                }
            }
        }

        stage('Security') {
            steps {
                sh 'npm audit'
                sh 'snyk test'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh './deploy.sh'
            }
        }
    }

    post {
        always {
            junit 'reports/**/*.xml'
            publishHTML([
                reportDir: 'coverage',
                reportFiles: 'index.html',
                reportName: 'Coverage'
            ])
        }
        failure {
            emailext(
                subject: "Build Failed: ${env.JOB_NAME}",
                body: "Check ${env.BUILD_URL}",
                to: "${env.CHANGE_AUTHOR_EMAIL}"
            )
        }
    }
}
```

## Cost Optimization

### GitHub Actions
- Use caching (50% faster, free)
- Use matrix builds sparingly
- Self-hosted runners for private repos
- **Cost**: $0.008/minute (Linux)

### GitLab CI
- Use shared runners (free tier: 400 minutes/month)
- Cache dependencies
- Limit parallel jobs
- **Cost**: Free tier available, $19/user/month Pro

### Jenkins
- Use spot instances for agents
- Shut down idle agents
- Containerized agents
- **Cost**: Infrastructure only

## Troubleshooting

### Slow Builds
1. Profile pipeline (which stage is slow?)
2. Add caching for dependencies
3. Parallelize independent jobs
4. Optimize Docker layers
5. Use smaller base images

### Flaky Tests
1. Identify flaky tests (run 100x)
2. Add explicit waits (not sleep)
3. Mock external dependencies
4. Isolate test data
5. Retry failed tests (max 3x)

### Failed Deployments
1. Check deployment logs
2. Verify health checks
3. Check resource constraints
4. Validate configuration
5. Rollback if needed

## Best Practices Summary

✅ **DO**:
- Keep pipelines fast (<10 min total)
- Fail fast (lint first, slow tests last)
- Cache dependencies
- Use semantic versioning
- Scan for vulnerabilities
- Require manual approval for prod
- Send notifications on failure
- Monitor pipeline performance

❌ **DON'T**:
- Hardcode secrets (use secrets management)
- Skip tests in CI
- Deploy without verification
- Use latest tag in prod
- Ignore security warnings
- Run unnecessary jobs
- Leave old artifacts

## Quick Reference

| Task | GitHub Actions | GitLab CI | Jenkins |
|------|----------------|-----------|---------|
| **Syntax** | YAML | YAML | Groovy |
| **Caching** | `cache:` key | `cache:` section | Pipeline plugin |
| **Artifacts** | `actions/upload-artifact` | `artifacts:` section | `archiveArtifacts` |
| **Secrets** | Repository secrets | CI/CD variables | Credentials plugin |
| **Matrix** | `strategy: matrix:` | `parallel:` | `matrix {}` |
| **Conditions** | `if:` | `only:` / `except:` | `when {}` |

---

## 🚀 MCP Integration: GitHub + Context7 for CI/CD Automation

### Runtime Detection & Usage

The skill automatically detects available MCPs for CI/CD workflow enhancement:

```typescript
const hasGitHub = typeof mcp__github__create_or_update_file !== 'undefined';
const hasContext7 = typeof mcp__context7__get_library_docs !== 'undefined';

if (hasGitHub && hasContext7) {
  // Get latest CI/CD framework documentation
  const githubActionsDocs = await mcp__context7__get_library_docs({
    context7CompatibleLibraryID: "/actions/toolkit",
    topic: "GitHub Actions workflow syntax caching artifacts",
    tokens: 3000
  });

  // Create optimized workflow directly in repository
  await mcp__github__create_or_update_file({
    owner: "myorg",
    repo: "myapp",
    path: ".github/workflows/ci.yml",
    content: generatedWorkflow,
    message: "Add optimized CI/CD pipeline with caching"
  });
} else {
  console.log("ℹ️  GitHub/Context7 MCP not available");
  console.log("   GitHub: npx @modelcontextprotocol/create-server github");
  console.log("   Context7: npm install -g @context7/mcp-server");
}
```

### Real-World Workflow Examples

**Example 1: Multi-Stage Pipeline Generation with Best Practices**

```typescript
// Without MCP: Manual workflow writing (3 hours)
// 1. Read GitHub Actions docs
// 2. Research caching strategies
// 3. Write YAML from scratch
// 4. Test and debug
// 5. Optimize

// With GitHub + Context7 MCP: AI-assisted generation (15 minutes)
const actionsDocs = await mcp__context7__get_library_docs({
  context7CompatibleLibraryID: "/actions/toolkit",
  topic: "caching dependencies matrix builds artifacts security scanning",
  tokens: 4000
});

const securityDocs = await mcp__context7__get_library_docs({
  context7CompatibleLibraryID: "/returntocorp/semgrep",
  topic: "CI integration security scanning",
  tokens: 2500
});

// Generate optimized workflow
const workflow = generateGitHubActionsWorkflow({
  language: "node",
  stages: ["build", "test", "security", "deploy"],
  patterns: actionsDocs,
  securityScan: securityDocs
});

// Deploy directly to repository
await mcp__github__create_or_update_file({
  owner: "myorg",
  repo: "myapp",
  path: ".github/workflows/ci.yml",
  content: workflow,
  message: "feat: add optimized CI/CD pipeline

- Multi-stage build with caching
- Parallel test execution
- Security scanning (SAST + dependency)
- Conditional deployment"
});

// ✅ 12x faster pipeline creation
// ✅ Latest best practices applied
// ✅ Automatic repository integration
```

**Example 2: GitLab CI to GitHub Actions Migration**

```typescript
// Analyze existing GitLab CI configuration
const gitlabConfig = await mcp__github__get_file_contents({
  owner: "myorg",
  repo: "legacy-app",
  path: ".gitlab-ci.yml"
});

// Get GitHub Actions patterns
const migrationDocs = await mcp__context7__get_library_docs({
  context7CompatibleLibraryID: "/actions/toolkit",
  topic: "GitLab CI migration GitHub Actions equivalents",
  tokens: 3500
});

// Convert GitLab CI → GitHub Actions
const convertedWorkflow = convertGitLabToGitHubActions({
  gitlabConfig: gitlabConfig.content,
  patterns: migrationDocs
});

// Create PR with converted workflow
await mcp__github__create_pull_request({
  owner: "myorg",
  repo: "legacy-app",
  title: "Migrate from GitLab CI to GitHub Actions",
  body: `## Migration Summary
- Converted all stages to GitHub Actions jobs
- Preserved caching strategy
- Maintained deployment logic
- Added security scanning

## Changes
- \`.gitlab-ci.yml\` → \`.github/workflows/ci.yml\`
- Updated cache paths for GitHub Actions
- Converted variables to GitHub secrets
`,
  head: "feat/github-actions-migration",
  base: "main",
  files: [
    { path: ".github/workflows/ci.yml", content: convertedWorkflow }
  ]
});

// ✅ Migration (1 hour vs 1 day)
// ✅ Automatic PR creation
// ✅ Best practices applied
```

**Example 3: CI/CD Performance Optimization**

```typescript
// Analyze current pipeline performance
const workflows = await mcp__github__list_workflows({
  owner: "myorg",
  repo: "myapp"
});

const runs = await mcp__github__list_workflow_runs({
  owner: "myorg",
  repo: "myapp",
  workflow_id: workflows[0].id,
  per_page: 100
});

// Get optimization patterns
const optimizationDocs = await mcp__context7__get_library_docs({
  context7CompatibleLibraryID: "/actions/toolkit",
  topic: "workflow optimization caching parallelization",
  tokens: 3500
});

// Analyze bottlenecks
const analysis = analyzeWorkflowPerformance(runs);
// Results: Test stage takes 15 min (80% of total time)

// Optimize with parallelization
const optimizedWorkflow = await optimizeWorkflow({
  currentWorkflow: workflow,
  bottlenecks: analysis.bottlenecks,
  patterns: optimizationDocs,
  strategies: ["parallelize-tests", "cache-dependencies", "matrix-builds"]
});

// Deploy optimized workflow
await mcp__github__create_or_update_file({
  owner: "myorg",
  repo: "myapp",
  path: ".github/workflows/ci.yml",
  content: optimizedWorkflow,
  message: "perf: optimize CI pipeline

- Parallelize tests across 4 runners
- Add dependency caching
- Use matrix strategy for multi-version testing

Reduces pipeline time: 18 min → 5 min (72% faster)"
});

// ✅ Pipeline time: 18 min → 5 min (72% faster)
// ✅ Cost reduction: 4x less compute time
// ✅ Faster feedback for developers
```

**Example 4: Automated Security Scanning Integration**

```typescript
// Get security tool documentation
const securityTools = [
  "/returntocorp/semgrep",
  "/aquasecurity/trivy",
  "/zricethezav/gitleaks"
];

const securityDocs = await Promise.all(
  securityTools.map(tool =>
    mcp__context7__get_library_docs({
      context7CompatibleLibraryID: tool,
      topic: "CI integration security scanning",
      tokens: 2500
    })
  )
);

// Generate comprehensive security workflow
const securityWorkflow = generateSecurityWorkflow({
  sast: securityDocs[0],        // Semgrep
  container: securityDocs[1],   // Trivy
  secrets: securityDocs[2]      // Gitleaks
});

// Add to repository
await mcp__github__create_or_update_file({
  owner: "myorg",
  repo: "myapp",
  path: ".github/workflows/security.yml",
  content: securityWorkflow,
  message: "security: add comprehensive security scanning

- SAST: Semgrep for code analysis
- Container: Trivy for image scanning
- Secrets: Gitleaks for credential detection

Fails pipeline on HIGH/CRITICAL vulnerabilities"
});

// ✅ Comprehensive security (30 min vs 4 hours)
// ✅ Multiple scan types integrated
// ✅ Production-ready thresholds
```

### Available Library IDs for CI/CD

**GitHub Actions**:
- `/actions/toolkit` - GitHub Actions core
- `/actions/cache` - Caching action
- `/actions/upload-artifact` - Artifact uploads
- `/actions/download-artifact` - Artifact downloads

**GitLab CI**:
- `/gitlab-org/gitlab` - GitLab CI/CD
- `/gitlab-org/gitlab-runner` - GitLab Runner

**Jenkins**:
- `/jenkinsci/jenkins` - Jenkins core
- `/jenkinsci/pipeline-plugin` - Pipeline as Code

**CI/CD Tools**:
- `/circleci/circleci-docs` - CircleCI
- `/travis-ci/travis-ci` - Travis CI
- `/drone/drone` - Drone CI

**Security Scanning**:
- `/returntocorp/semgrep` - SAST
- `/aquasecurity/trivy` - Container scanning
- `/zricethezav/gitleaks` - Secret detection
- `/snyk/cli` - Dependency scanning

**Build Tools**:
- `/docker/build-push-action` - Docker builds
- `/docker/metadata-action` - Docker metadata

### Benefits Comparison

| Task | Without MCP | With GitHub + Context7 MCP | Time Saved |
|------|-------------|---------------------------|------------|
| New pipeline creation | 3 hours (manual docs + trial/error) | 15 min (AI-assisted) | 92% faster |
| GitLab → GitHub migration | 1 day (conversion + testing) | 1 hour (automated) | 88% faster |
| Pipeline optimization | 4 hours (profiling + research) | 30 min (analysis + apply) | 87% faster |
| Security integration | 4 hours (tool research + setup) | 30 min (multi-tool setup) | 87% faster |
| Branch protection setup | 30 min (manual clicking) | 2 min (API automation) | 93% faster |

### When to Use GitHub + Context7 MCP

**Ideal for**:
- ✅ Creating new CI/CD pipelines from scratch
- ✅ Migrating between CI/CD platforms
- ✅ Optimizing existing pipeline performance
- ✅ Integrating security scanning tools
- ✅ Setting up branch protection rules
- ✅ Automating PR workflows
- ✅ Multi-repo pipeline standardization

**Not needed for**:
- ❌ Simple one-stage builds
- ❌ Basic linting workflows
- ❌ Trivial pipeline modifications

### Installation

```bash
# Install GitHub MCP
npx @modelcontextprotocol/create-server github

# Install Context7 MCP
npm install -g @context7/mcp-server

# Configure in Claude Code MCP settings
# Both servers will auto-detect and enable integration
```

### Security Best Practices

When using GitHub + Context7 MCP for CI/CD:
- Never commit secrets to workflow files (use GitHub Secrets)
- Validate all security scanner configurations
- Use pinned versions for actions (not `@main`)
- Review generated workflows before merging
- Enable branch protection on main branches
- Require status checks before merging
- Use least privilege for CI/CD service accounts

---

**Version**: 1.0.0
**Last Updated**: 2025-01-20
**Patterns**: 20+
**Best Practices**: Production-tested


