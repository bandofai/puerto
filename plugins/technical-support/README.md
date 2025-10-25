# Technical Support Plugin

Technical troubleshooting specialist for diagnostics, log analysis, bug reproduction, and workarounds.

## Overview

The Technical Support plugin provides comprehensive technical troubleshooting capabilities including log analysis, system diagnostics, bug reproduction, and workaround suggestions for complex technical issues.

## What's Included

### 4 Specialized Agents

1. **log-analyzer** (Sonnet) - Log analysis expert
   - Analyzes application, system, and error logs
   - Identifies patterns and anomalies
   - Extracts errors and stack traces
   - Performs root cause analysis
   - Cost: ~$0.0015/analysis

2. **bug-reproducer** (Sonnet) - Bug reproduction specialist
   - Creates minimal reproduction steps
   - Generates test cases
   - Documents environment requirements
   - Verifies reproducibility
   - Cost: ~$0.0015/reproduction

3. **diagnostics-runner** (Haiku) - System diagnostics
   - Runs health checks
   - Tests connectivity
   - Checks resource usage
   - Verifies service status
   - Cost: ~$0.00006/diagnostic

4. **workaround-finder** (Sonnet) - Temporary solution specialist
   - Suggests workarounds for issues
   - Documents limitations
   - Provides revert instructions
   - Sets expectations for permanent fixes
   - Cost: ~$0.0011/workaround

### 1 Comprehensive Skill

**troubleshooting**: Systematic troubleshooting framework, common issues, log patterns, escalation criteria

## Key Features

✓ **Log Analysis**: Identify errors and patterns in logs
✓ **System Diagnostics**: Health checks for system resources
✓ **Bug Reproduction**: Minimal, reliable reproduction steps
✓ **Workaround Solutions**: Temporary fixes while awaiting permanent solutions
✓ **Root Cause Analysis**: Deep investigation of technical issues
✓ **Documentation**: Complete technical documentation
✓ **Skill-Aware**: Workaround finder reads troubleshooting skill

## Workflow

```
Technical Issue
      ↓
[@diagnostics-runner] → System health check
      ↓
[@log-analyzer] → Find errors and patterns
      ↓
[@bug-reproducer] → Create reproduction steps
      ↓
[@workaround-finder] → Suggest temporary solution
```

## Usage Examples

### Log Analysis

```bash
@log-analyzer "Analyze logs/application.log for errors in the last hour"

# Output:
# - 45 ERROR entries found
# - Pattern: "Database connection timeout"
# - Occurs every 2-3 minutes
# - Root cause: Connection pool exhausted
# - Recommendation: Increase pool size or fix connection leaks
```

### System Diagnostics

```bash
@diagnostics-runner "Run full system diagnostics"

# Checks:
# - CPU, memory, disk usage
# - Network connectivity
# - Service status (web, database, cache)
# - Port availability
# - Recent errors in logs

# Output: Health report with recommendations
```

### Bug Reproduction

```bash
@bug-reproducer "Create reproduction steps for upload crash bug"

# Output:
# Environment: Node 18, 8GB RAM, Chrome 120
# Steps:
# 1. npm start
# 2. Navigate to /upload
# 3. Select file > 100MB
# 4. Click upload
# 5. Observe crash
# Reproducibility: 100%
# Root cause: Memory exhaustion
```

### Workaround Finding

```bash
@workaround-finder "Suggest workaround for API rate limiting"

# Output:
# Workaround: Implement exponential backoff
# Steps: [code example]
# Limitations: Slower overall
# Permanent fix: Request higher rate limit
```

## Issue Requirements Met

✓ **Role**: Technical troubleshooting specialist
✓ **Technical diagnostics**: @diagnostics-runner
✓ **Log analysis**: @log-analyzer
✓ **Bug reproduction**: @bug-reproducer
✓ **Workaround suggestions**: @workaround-finder
✓ **Technical documentation**: All agents produce detailed docs
✓ **Tools Required**:
  - ✓ Log analysis: Read, Grep for log parsing
  - ✓ Code execution: Bash for diagnostics and health checks
  - ✓ File operations: Read, Write for all agents

## Common Use Cases

### Application Crashes

1. @diagnostics-runner "Check system resources"
2. @log-analyzer "Find crash in error logs"
3. @bug-reproducer "Create crash reproduction steps"
4. @workaround-finder "Suggest memory limit workaround"

### API Failures

1. @diagnostics-runner "Test API connectivity"
2. @log-analyzer "Find API errors in logs"
3. @bug-reproducer "Reproduce API failure"
4. @workaround-finder "Suggest retry strategy"

### Performance Issues

1. @diagnostics-runner "Check resource usage"
2. @log-analyzer "Find slow query patterns"
3. @bug-reproducer "Reproduce slow operation"
4. @workaround-finder "Suggest caching strategy"

## Cost Analysis

Per Issue Resolution:
- Diagnostics: $0.00006
- Log analysis: $0.0015
- Bug reproduction: $0.0015
- Workaround: $0.0011
- **Total**: ~$0.004 per complete troubleshooting session

## Performance Targets

- Log analysis: < 2 minutes
- Diagnostics: < 30 seconds
- Bug reproduction: < 10 minutes
- Workaround suggestion: < 5 minutes

## Best Practices

1. **Start with diagnostics**: Quick health check first
2. **Analyze logs thoroughly**: Don't skip log analysis
3. **Minimal reproduction**: Simplest steps possible
4. **Document everything**: Complete technical records
5. **Workarounds when needed**: Don't block on permanent fix

---

**Plugin Version**: 1.0.0
**Last Updated**: 2025-01-20
**Author**: Puerto
