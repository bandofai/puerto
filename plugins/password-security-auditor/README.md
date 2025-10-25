# Password & Security Auditor

Security audit and breach monitoring specialist with password strength analysis, Have I Been Pwned integration, 2FA tracking, and compliance verification.

## Features

### 3 Specialized Agents

1. **security-auditor** (Sonnet) - Strategic coordinator
   - Password strength analysis (metadata only, never stores passwords)
   - Risk scoring (0-100 scale)
   - Comprehensive audit reports
   - Compliance verification (NIST, OWASP)

2. **breach-monitor** (Haiku, Fast) - Breach specialist
   - Have I Been Pwned API integration
   - Email and password hash checking (k-anonymity for privacy)
   - Breach severity classification
   - Remediation guidance

3. **2fa-tracker** (Haiku, Fast) - Authentication specialist
   - 2FA status tracking across accounts
   - Gap analysis by priority
   - Setup guides for services
   - Method comparison (Hardware > TOTP > SMS)

### 1 Comprehensive Skill

**security-auditing** - Complete patterns for:
- Password strength algorithms (entropy, patterns, age)
- Breach monitoring best practices
- 2FA implementation strategies
- NIST SP 800-63B compliance
- OWASP security guidelines

## Quick Start

### Initialize Security Audit

```bash
@security-auditor "Initialize my security audit system"
```

### Add Accounts

```bash
@security-auditor "Add account: Gmail, user@example.com, priority=critical"
```

### Run Comprehensive Audit

```bash
@security-auditor "Run comprehensive security audit"
```

### Check for Breaches

```bash
@breach-monitor "Check user@example.com for data breaches"
```

### Review 2FA Coverage

```bash
@2fa-tracker "Show 2FA coverage status and gaps"
```

## Key Features

- **Password Analysis**: Strength assessment without storing actual passwords
- **Breach Monitoring**: HIBP integration with k-anonymity for privacy
- **2FA Tracking**: Coverage gaps and method recommendations
- **Risk Scoring**: Multi-factor security assessment (0-100)
- **Compliance**: NIST and OWASP alignment

## Privacy & Security

✅ **Never stores actual passwords** - only metadata
✅ **K-anonymity for breach checks** - only first 5 chars of hash sent
✅ **Local storage only** - no cloud uploads
✅ **Encrypted sensitive data** - recovery info protected

## Data Storage

Configuration stored in `~/.security-audit/`:
- `accounts.json` - Account inventory (NO passwords)
- `2fa-status.json` - Authentication tracking
- `breach-monitoring/` - Breach check results
- `audit-history/` - Historical reports

## License

MIT

---

**Generated as part of Puerto Plugin Collection - Issue #143**
