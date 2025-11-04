# Security Policy

---

## Reporting a Vulnerability

**Please do NOT report security vulnerabilities through public GitHub issues.**

### How to Report

1. **Email:** Send details to [security@bandofai.com](mailto:security@bandofai.com)
2. **Subject:** `[SECURITY] Brief description`
3. **Include:**
   - Type of vulnerability
   - Affected component (department/plugin/agent)
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)
   - Your contact information

### Response Timeline

- **Initial Response:** Within 48 hours
- **Status Update:** Within 7 days
- **Resolution Target:** 30 days for critical issues

### What Happens Next

1. **Acknowledgment:** We'll confirm receipt within 48 hours
2. **Assessment:** We'll evaluate severity and impact
3. **Fix Development:** We'll develop and test a patch
4. **Disclosure:** Coordinated disclosure after fix is available
5. **Credit:** Security researchers will be credited (if desired)

---

## Security Best Practices

### For Plugin Users

#### 1. Review Plugin Code

Before using in sensitive projects:
```bash
# View plugin contents
ls ~/.claude/plugins/puerto/engineering/

# Review agent definitions
cat ~/.claude/plugins/puerto/engineering/agents/frontend-engineer.md
```

#### 2. Limit Plugin Permissions

- Only install departments you actively use
- Review tool access in agent frontmatter
- Uninstall unused plugins immediately

#### 3. Keep Plugins Updated

```bash
# Check for updates
/plugin update @puerto

# Stay on latest version for security patches
```

#### 4. Audit Third-Party Dependencies

For plugins with MCP servers:
```bash
# Check package.json dependencies
cat ~/.claude/plugins/puerto/essentials/package.json
```

#### 5. Use Project-Level Installation for Sensitive Work

```bash
# Install locally instead of globally
cd /path/to/sensitive/project
/plugin install engineering@puerto --project
```

---

### For Plugin Developers

#### 1. Never Hardcode Secrets

❌ **Don't do this:**
```javascript
const API_KEY = "sk-1234567890abcdef";
```

✅ **Do this:**
```javascript
const API_KEY = process.env.API_KEY;
```

#### 2. Validate All Inputs

```typescript
// Always validate user inputs
function processUserInput(input: string) {
  if (!input || input.length > 1000) {
    throw new Error('Invalid input');
  }
  // Sanitize input
  const sanitized = input.replace(/[<>]/g, '');
  return sanitized;
}
```

#### 3. Follow Least Privilege Principle

Only request tool access that's absolutely necessary:

```yaml
# Agent frontmatter - minimal tools
tools:
  - Read
  - Write
# Don't add Bash unless truly needed
```

#### 4. Sanitize File Paths

```typescript
// Prevent path traversal
import path from 'path';

function safeReadFile(userPath: string) {
  const normalized = path.normalize(userPath);
  if (normalized.includes('..')) {
    throw new Error('Invalid path');
  }
  // Proceed with read
}
```

#### 5. Keep Dependencies Updated

```bash
# Regular dependency audits
npm audit
npm audit fix

# For Python
pip-audit
```

#### 6. Use Security Linters

```bash
# For JavaScript/TypeScript
npm install --save-dev eslint-plugin-security

# For Python
pip install bandit
bandit -r .
```

---

## Security Features

### Puerto Marketplace

#### 1. Code Review Process

All plugins undergo review before inclusion:
- ✅ Manual code review
- ✅ Automated security scanning
- ✅ Dependency vulnerability checks
- ✅ Best practices validation

#### 2. Validation Checks

193 automated checks including:
- Plugin structure validation
- JSON schema compliance
- File permission checks
- Dependency version verification

#### 3. Transparency

- ✅ All plugins are open source
- ✅ Source code available on GitHub
- ✅ Change history tracked in git
- ✅ Community can review and audit

### Plugin Isolation

Plugins run with limited permissions:
- Sandboxed execution environment
- Explicit tool access declaration
- No network access by default (except MCP servers)
- File system access restricted to project directory

---

## Known Security Considerations

### 1. Agent Tool Access

**Risk:** Agents have access to tools (Read, Write, Bash, etc.)

**Mitigation:**
- Tools explicitly declared in agent frontmatter
- Users can review before use
- Limited to necessary operations
- Sandboxed execution

### 2. MCP Server Connections

**Risk:** MCP servers may connect to external services

**Mitigation:**
- Connections documented in plugin README
- Requires user permission for sensitive operations
- HTTPS/TLS for all external connections
- No credentials stored in plugins

### 3. Code Execution

**Risk:** Some agents use Bash tool for code execution

**Mitigation:**
- Sandbox mode by default
- User approval required for sensitive operations
- No automatic execution without confirmation
- Logged for audit trail

### 4. Data Privacy

**Risk:** Agents process user code and data

**Mitigation:**
- All processing happens locally
- No telemetry or analytics collection
- No data sent to external services (except documented MCP servers)
- User data never leaves local machine without explicit action

---

## Security Checklist for New Plugins

Before submitting a plugin:

- [ ] No hardcoded secrets or API keys
- [ ] All inputs validated and sanitized
- [ ] Dependencies up to date (`npm audit` clean)
- [ ] File paths validated (no path traversal)
- [ ] Minimal tool access requested
- [ ] External connections documented
- [ ] Error messages don't leak sensitive info
- [ ] Security linter passes (eslint-plugin-security)
- [ ] README documents security considerations
- [ ] Tests include security test cases

---

## Vulnerability Disclosure Policy

### Coordinated Disclosure

We follow responsible disclosure:

1. **Private Report:** Security issues reported privately
2. **Acknowledgment:** We confirm within 48 hours
3. **Fix Development:** Patch developed privately
4. **Testing:** Thorough testing before release
5. **Release:** Security patch released
6. **Public Disclosure:** Details published after fix is available

### Disclosure Timeline

- **Critical:** 7-14 days
- **High:** 30 days
- **Medium:** 60 days
- **Low:** 90 days

We may request extension if issue is complex.

---

## Security Updates

Security updates are released as:

- **Patch versions:** 1.0.x for security fixes
- **Changelogs:** Documented in [CHANGELOG.md](CHANGELOG.md)
- **GitHub Security Advisories:** For critical issues
- **Release Notes:** Security fixes highlighted

Subscribe to releases:
```bash
# Watch releases on GitHub
https://github.com/bandofai/puerto/releases
```

---

## Security Resources

### OWASP Top 10

We follow OWASP guidelines for:
- Injection prevention
- Authentication & session management
- Cross-site scripting (XSS) prevention
- Security misconfiguration prevention
- Sensitive data exposure prevention

### CWE Top 25

We mitigate Common Weakness Enumerations:
- CWE-79: XSS
- CWE-89: SQL Injection
- CWE-20: Improper Input Validation
- CWE-78: OS Command Injection
- CWE-22: Path Traversal

---

## Bug Bounty Program

**Status:** Not currently active

We're considering a bug bounty program for:
- Critical vulnerabilities
- Novel attack vectors
- Significant security improvements

Stay tuned for updates.

---

## Security Contacts

- **Email:** security@bandofai.com
- **PGP Key:** Available on request
- **Response Time:** Within 48 hours
- **GitHub:** [@bandofai/puerto-security](https://github.com/orgs/bandofai/teams/puerto-security)

---

## Acknowledgments

We thank the security research community for helping keep Puerto secure.

**Hall of Fame:** Security researchers who have responsibly disclosed vulnerabilities will be listed here (with permission).

---

**Last Updated:** 2025-11-03
**Version:** 1.0.0
**Policy Version:** 1.0

---

## Additional Resources

- [GitHub Security Advisories](https://github.com/bandofai/puerto/security/advisories)
- [Dependency Graph](https://github.com/bandofai/puerto/network/dependencies)
- [Security Insights](https://github.com/bandofai/puerto/security)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
