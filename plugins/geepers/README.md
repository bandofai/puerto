# Geepers

63 specialized agents for Claude Code that handle infrastructure, deployment, development workflows, and quality assurance. Built for the dr.eamer.dev ecosystem but adaptable to any project.

## Install

```bash
/plugin install geepers@puerto
```

## Overview

Geepers provides a comprehensive suite of agents organized into categories:

- **Frontend** - CSS, React, design systems, motion, performance
- **Fullstack** - Backend-to-frontend development coordination
- **Hive** - Multi-agent coordination and refactoring
- **Quality** - Accessibility, security, testing, API auditing
- **Deploy** - Service management, Caddy configuration, validation
- **Research** - Data analysis, visualization, academic research
- **Games** - Game development and interactive experiences
- **Corpus** - Linguistics and corpus analysis
- **Web** - Express, Node.js, web development
- **Python** - Python development and tooling

## Core Agents

### Infrastructure & Deployment

#### `@geepers_caddy`
Sole authority for Caddy configuration changes. Prevents port conflicts and ensures proper proxy setup.

```
"Use geepers_caddy to add a new service route"
"Configure reverse proxy for port 5050"
```

#### `@geepers_services`
Service lifecycle management - start, stop, restart, monitor.

```
"Start the clinical service"
"Check status of all running services"
```

#### `@geepers_validator`
Pre-deployment validation for ports, proxies, and dependencies.

```
"Validate service before deploying"
"Check for port conflicts"
```

### Development Workflow

#### `@geepers_scout`
Quick project reconnaissance and analysis.

```
"Scout the lessonplanner service"
"Analyze project structure"
```

#### `@geepers_repo`
Git hygiene, commits, branch cleanup, history management.

```
"Clean up merged branches"
"Create commit for current changes"
```

#### `@geepers_janitor`
Aggressive cleanup of temporary files, cruft, and build artifacts.

```
"Clean up temporary files"
"Remove build artifacts"
```

### Quality Assurance

#### `@geepers_security`
Security audits, vulnerability scanning, secret detection.

```
"Audit codebase for security issues"
"Check for exposed secrets"
```

#### `@geepers_testing`
Test creation, execution, and coverage analysis.

```
"Generate tests for authentication module"
"Run test suite and analyze coverage"
```

#### `@geepers_accessibility`
Accessibility audits, ARIA compliance, WCAG validation.

```
"Audit accessibility of dashboard"
"Check WCAG compliance"
```

### Frontend Development

#### `@geepers_orchestrator_frontend`
Coordinates CSS, React, design systems, motion, and performance optimization.

```
"Build responsive navigation component"
"Optimize frontend performance"
```

#### `@geepers_design`
Design systems, component libraries, style guides.

```
"Create design system documentation"
"Build component library"
```

#### `@geepers_react`
React development, hooks, state management, optimization.

```
"Refactor to use React hooks"
"Optimize component rendering"
```

### Fullstack Development

#### `@geepers_orchestrator_fullstack`
Backend-to-frontend coordination for complete features.

```
"Build user authentication feature"
"Create API endpoint with frontend"
```

#### `@geepers_express`
Express.js server development and middleware.

```
"Build Express API for blog"
"Add authentication middleware"
```

## Master Orchestrator

#### `@conductor_geepers`
Intelligent routing to appropriate agents based on task complexity.

```
"Route this complex refactoring task"
"Coordinate multiple services deployment"
```

Automatically delegates to:
- Single agents for focused tasks
- Category orchestrators for moderate complexity
- Multiple agents for complex multi-step workflows

## Orchestrators

Orchestrators coordinate multiple specialized agents:

| Orchestrator | Purpose |
|--------------|---------|
| `@geepers_orchestrator_deploy` | Port/proxy deployments, service setup |
| `@geepers_orchestrator_checkpoint` | End-of-session cleanup and status |
| `@geepers_orchestrator_fullstack` | Backend + frontend feature development |
| `@geepers_orchestrator_frontend` | CSS, React, design, motion, performance |
| `@geepers_orchestrator_quality` | Accessibility, performance, API, deps audits |
| `@geepers_orchestrator_web` | Web development coordination |

## Output Structure

Geepers agents write to organized output directories:

```
~/geepers/
├── reports/by-date/YYYY-MM-DD/     # Daily operation reports
├── recommendations/by-project/      # Project-specific improvements
├── status/                          # Service and system status
├── snippets/                        # Reusable code patterns
└── logs/                           # Agent execution logs
```

## Related Tools

**MCP-Dreamwalker**: Programmatic orchestration framework for multi-agent workflows. Geepers uses Dreamwalker patterns for complex coordination.

Repository: [github.com/lukeslp/mcp-dreamwalker](https://github.com/lukeslp/mcp-dreamwalker)

## Use Cases

### Deploying a New Service
```
"Use geepers to deploy my new API on port 5055"
```
Automatically: validates port, configures Caddy, updates service manager, tests deployment.

### Frontend Feature Development
```
"Build a responsive user dashboard with charts"
```
Orchestrator coordinates: design system selection, React components, responsive CSS, accessibility, performance optimization.

### Codebase Quality Audit
```
"Run full quality audit"
```
Coordinates: security scan, test coverage, accessibility check, API validation, dependency audit.

## Agent Categories

| Category | Agent Count | Focus Area |
|----------|-------------|------------|
| Frontend | 8 | CSS, React, design, motion, perf |
| Fullstack | 5 | Full-stack development |
| Hive | 4 | Coordination, refactoring |
| Quality | 8 | Testing, security, a11y, API |
| Deploy | 6 | Services, Caddy, validation |
| Research | 12 | Data, visualization, analysis |
| Games | 4 | Game development |
| Corpus | 3 | Linguistics |
| Web | 5 | Express, Node.js |
| Python | 3 | Python development |
| Standalone | 5 | Docs, git, general |

## Configuration

Agents read from `~/geepers/recommendations/by-project/` for project-specific context. Place a `{project-name}.md` file with:

- Known issues
- Architecture notes
- Deployment requirements
- Testing strategy

## Prerequisites

- Claude Code
- Git
- Node.js >= 18 (for web agents)
- Python >= 3.8 (for research/corpus agents)

## Repository

Full agent definitions and documentation: [github.com/lukeslp/geepers](https://github.com/lukeslp/geepers)

## License

MIT
