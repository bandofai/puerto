# Technical Troubleshooting Skill

## Purpose

Systematic approach to diagnosing and resolving technical issues through log analysis, diagnostics, bug reproduction, and workaround development.

## Troubleshooting Framework

### 1. Gather Information

**Collect**:
- Error messages and codes
- Log files (application, system, database)
- Environment details (OS, versions, config)
- Reproduction steps
- When issue started
- What changed recently

**Questions**:
- Is it reproducible?
- Does it affect all users or specific subset?
- Any error messages or codes?
- When did it start?
- What was the last change?

### 2. Analyze Symptoms

**Look for**:
- Error patterns in logs
- Resource usage spikes
- Failed operations
- Timeout issues
- Connection problems

**Methods**:
- Log analysis: grep for ERROR, EXCEPTION, FATAL
- System metrics: CPU, memory, disk, network
- Application health: process status, port listening
- Dependency status: database, cache, APIs

### 3. Form Hypothesis

**Consider**:
- Recent changes (code, config, infrastructure)
- Known issues with symptoms
- Common failure modes
- Resource constraints
- External dependencies

### 4. Test Hypothesis

**Verify**:
- Reproduce the issue
- Check proposed root cause
- Eliminate alternative explanations
- Test in isolated environment

### 5. Find Solution

**Options**:
- **Immediate workaround**: Temporary fix
- **Permanent fix**: Address root cause
- **Escalation**: If beyond capability

### 6. Document

**Record**:
- Issue description
- Root cause
- Solution applied
- Workaround (if temporary)
- Prevention measures

---

## Common Issue Categories

### Configuration Issues

**Symptoms**:
- Works in one environment, not another
- "File not found" errors
- "Invalid configuration" messages

**Check**:
- Config files present and valid
- Environment variables set
- Permissions correct
- Paths absolute vs relative

**Fix**:
- Correct configuration
- Add missing settings
- Fix file permissions

---

### Resource Exhaustion

**Symptoms**:
- Out of memory errors
- Disk full errors
- Too many open files
- Connection pool exhausted

**Check**:
```bash
# Memory
free -h
ps aux --sort=-%mem | head

# Disk
df -h
du -sh /*

# File descriptors
lsof | wc -l
ulimit -n

# Connections
netstat -an | grep ESTABLISHED | wc -l
```

**Fix**:
- Increase resource limits
- Clean up unused resources
- Fix resource leaks
- Scale infrastructure

---

### Network Issues

**Symptoms**:
- Connection timeout
- Connection refused
- DNS resolution failures
- Slow API responses

**Diagnose**:
```bash
# Connectivity
ping example.com

# DNS
nslookup example.com

# Port
nc -zv host port

# Trace route
traceroute example.com

# Check firewall
iptables -L
```

**Fix**:
- Check firewall rules
- Verify DNS settings
- Test network connectivity
- Check service status

---

### Authentication/Authorization

**Symptoms**:
- 401 Unauthorized
- 403 Forbidden
- Invalid credentials
- Token expired

**Check**:
- Credentials valid
- Token not expired
- Permissions correct
- API keys active

**Fix**:
- Regenerate keys/tokens
- Update credentials
- Fix permissions
- Check expiration

---

### Performance Issues

**Symptoms**:
- Slow response times
- Timeouts
- High CPU/memory
- Queue backing up

**Diagnose**:
```bash
# CPU usage
top -o %CPU

# Memory
top -o %MEM

# Slow queries
# (database-specific tools)

# Request timing
curl -w "@curl-format.txt" url
```

**Fix**:
- Optimize queries
- Add caching
- Scale resources
- Fix performance bottlenecks

---

## Log Analysis Patterns

### Error Levels

**FATAL/CRITICAL**: Immediate attention required
**ERROR**: Operation failed, investigate
**WARN**: Potential issue, monitor
**INFO**: Normal operation
**DEBUG**: Detailed information

### Common Error Messages

**"Connection refused"**:
→ Service not running or port blocked

**"Timeout"**:
→ Service slow or unreachable

**"Out of memory"**:
→ Memory leak or insufficient resources

**"Permission denied"**:
→ File/directory permissions incorrect

**"File not found"**:
→ Path wrong or file missing

---

## Bug Reproduction

### Good Reproduction Steps

✅ **Specific**: Exact commands, not vague descriptions
✅ **Minimal**: Fewest steps possible
✅ **Complete**: All prerequisites included
✅ **Reproducible**: Works consistently

### Example: Good vs Bad

**Bad**:
```
1. Use the app
2. Click some buttons
3. It crashes
```

**Good**:
```
1. Start app: `npm start`
2. Navigate to http://localhost:3000/upload
3. Select file larger than 100MB
4. Click "Upload" button
5. Observe: Browser tab crashes
Environment: Chrome 120, macOS 14, 8GB RAM
Reproducibility: 100% with files >100MB
```

---

## Workaround Strategies

### When Permanent Fix Not Immediate

1. **Alternative approach**: Different way to achieve goal
2. **Configuration change**: Adjust settings temporarily
3. **Manual process**: Steps to do manually
4. **Version rollback**: Use previous working version
5. **Rate limiting**: Reduce load on failing component
6. **Retry logic**: Add retries for intermittent failures

### Workaround Template

```markdown
**Problem**: [Description]

**Workaround**: [Solution]

**Steps**:
1. [Step 1]
2. [Step 2]

**Limitations**: [What doesn't work]

**Permanent Fix**: [Status/Timeline]
```

---

## Escalation Criteria

Escalate when:
- ❌ Root cause unclear after analysis
- ❌ Fix requires code changes
- ❌ Infrastructure/permissions needed
- ❌ Security implications
- ❌ Data loss risk
- ❌ Affects multiple customers
- ❌ Beyond technical capability

---

## Best Practices

✅ **Start simple**: Check obvious things first
✅ **Use tools**: Don't guess, measure
✅ **Document findings**: Keep notes throughout
✅ **Test changes**: Verify fix works
✅ **Learn patterns**: Build knowledge base
✅ **Automate checks**: Create health check scripts
✅ **Monitor trends**: Watch for recurring issues

---

## Summary

Effective troubleshooting:
1. Gather complete information
2. Analyze systematically
3. Form testable hypothesis
4. Verify root cause
5. Provide solution or workaround
6. Document for future reference

**Goal**: Rapid, accurate issue resolution with minimal disruption
