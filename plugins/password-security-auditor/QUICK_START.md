# Password & Security Auditor - Quick Start Guide

## Installation

```bash
/plugin install password-security-auditor@puerto
```

After installation, restart Claude Code to activate agents.

---

## First Time Setup (2 minutes)

### Step 1: Initialize
```
@security-auditor Initialize my security audit system
```

This creates the directory structure at `~/.security-audit/`

### Step 2: Add Your First Account
```
@security-auditor Add account: Gmail, user@example.com, priority=critical
```

### Step 3: Configure (Optional)
```
@security-auditor Show current security policy
```

Review and adjust if needed (defaults follow NIST/OWASP guidelines).

---

## Common Tasks

### Run Comprehensive Audit

```
@security-auditor Run comprehensive security audit
```

**What it does**:
- Analyzes all account password metadata
- Checks breach exposure via @breach-monitor
- Reviews 2FA coverage via @2fa-tracker
- Generates prioritized report with top 3 actions

**Time**: ~1 minute

---

### Check for Data Breaches

```
@breach-monitor Check if user@example.com has been in any breaches
```

**What it does**:
- Queries Have I Been Pwned API
- Shows which breaches affected your email
- Classifies severity (critical/high/medium/low)
- Provides specific remediation steps

**Time**: ~2 seconds per email

**Batch check**:
```
@breach-monitor Check these emails: email1@example.com, email2@example.com
```

---

### Review 2FA Coverage

```
@2fa-tracker Show my 2FA status
```

**What it does**:
- Lists all accounts with 2FA status
- Identifies critical accounts without 2FA
- Shows weak implementations (SMS-only)
- Provides setup guides

**Time**: ~5 seconds

**Find gaps only**:
```
@2fa-tracker Which accounts are missing 2FA?
```

---

### Analyze Password Strength

```
@security-auditor Analyze password strength for: Banking Account
```

**What it provides**:
- Interactive analysis (you provide characteristics, not password)
- Entropy calculation
- Pattern detection
- Specific improvement recommendations

**Important**: Never provides actual password - only metadata

---

### Add New Account

```
@security-auditor Add account: [Service], [Email], priority=[critical|high|medium|low]
```

**Examples**:
```
@security-auditor Add account: GitHub, dev@example.com, priority=high
@security-auditor Add account: Netflix, user@example.com, priority=medium
```

---

### Update 2FA Status

```
@2fa-tracker Update 2FA for Gmail: enabled, method=TOTP, backup=Recovery Codes
```

**Methods**: TOTP, Hardware, SMS, Biometric, Email, None

---

## Recommended Schedule

### Monthly (5 minutes)
```
@breach-monitor Check all emails for breaches
```

### Quarterly (15 minutes)
```
@security-auditor Run comprehensive security audit
```

### Semi-Annual (30 minutes)
```
@2fa-tracker Review 2FA coverage
@security-auditor Generate compliance report
```

### Annual (1 hour)
```
@security-auditor Full security audit with policy review
@2fa-tracker Compare 2FA methods and upgrade where needed
@breach-monitor Historical breach analysis
```

---

## Understanding Reports

### Security Scores

**90-100**: Excellent - Strong security posture
**75-89**: Good - Minor improvements needed
**60-74**: Fair - Some gaps to address
**40-59**: Poor - Multiple security issues
**0-39**: Critical - Immediate action required

### Risk Levels

**Critical** (Red): Immediate action required (today)
**High** (Orange): Address this week
**Medium** (Yellow): Address this month
**Low** (Green): Address next quarter

### Finding Categories

**Password Strength**: Weak passwords, low entropy, patterns detected
**Breach Exposure**: Email/password found in data breaches
**2FA**: Missing 2FA, weak methods (SMS), no backup
**Recovery**: Missing backup methods, weak security questions
**Compliance**: Not meeting NIST/OWASP standards

---

## Sample Outputs

### Security Audit Summary
```markdown
Security Audit Complete

Overall Score: 72/100 (Good)
Risk Level: Medium

Critical Issues: 1
- Banking Backup Account: No 2FA enabled

High Priority: 3
- 3 passwords over 90 days old
- Secondary email found in breach

Medium Priority: 5
- 5 accounts using SMS-only 2FA

Top 3 Recommendations:
1. Enable TOTP on Banking Backup Account
2. Check breach exposure for secondary@example.com
3. Rotate 3 passwords over policy limit

Report: ~/.security-audit/audit-history/2025-01-15-audit.md
```

### Breach Check Result
```markdown
Breach Monitoring Complete

Checked: user@example.com
Breaches Found: 2 (HIGH severity)

Breaches:
1. Adobe (2013) - CRITICAL
   - Data Exposed: Passwords, Email addresses
   - Action: Change password immediately

2. LinkedIn (2012) - MEDIUM
   - Data Exposed: Email addresses, Passwords
   - Action: Change if reusing password

Recommendations:
1. Change password on Adobe if still using service
2. Change password anywhere else you used same password
3. Enable 2FA on all affected accounts

Report: ~/.security-audit/breach-monitoring/breach-report-2025-01-15.md
```

### 2FA Coverage Report
```markdown
2FA Status Review Complete

Coverage: 12/15 accounts (80%)

Critical Gaps (2 accounts):
- Banking Backup: No 2FA enabled
- Password Manager: No 2FA enabled

Weak Implementation (3 accounts):
- Facebook: SMS-only (upgrade to TOTP)
- Twitter: SMS-only (upgrade to TOTP)
- Amazon: SMS-only (upgrade to TOTP)

Recommendations:
1. Enable TOTP on Banking Backup (setup guide provided)
2. Enable Hardware Key on Password Manager
3. Upgrade 3 accounts from SMS to TOTP

Next Review: 2025-07-15 (Semi-annual)
```

---

## Configuration

### Set HIBP API Key (Optional but Recommended)

```
@security-auditor Configure HIBP API key: your-key-here
```

Get free API key: https://haveibeenpwned.com/API/Key

**Benefits**:
- Automated breach monitoring
- No rate limiting issues
- Support Troy Hunt's project

### Adjust Password Policy

```
@security-auditor Update password policy: min_length=18, rotation_days=120
```

### Set Audit Reminders

```
@security-auditor Set reminder: breach_check=monthly, full_audit=quarterly
```

---

## Privacy & Security

### What Gets Stored?
✅ Account names and emails
✅ Password metadata (length, entropy, character types)
✅ 2FA status and methods
✅ Breach check results
✅ Audit history

### What NEVER Gets Stored?
❌ Actual passwords
❌ Recovery codes (unless explicitly saved encrypted)
❌ Security question answers

### Where Is Data Stored?
📁 `~/.security-audit/` (local only, never cloud)

### Can I Delete Data?
```bash
rm -rf ~/.security-audit/
```

### Can I Export Data?
```
@security-auditor Export all data to ~/Desktop/security-export.json
```

---

## Troubleshooting

### "API key required" error
**Solution**: Get free HIBP API key and configure:
```
@security-auditor Configure HIBP API key: your-key
```

### "Rate limit exceeded"
**Solution**: Wait 2 seconds between requests, or get API key for higher limits

### "No accounts found"
**Solution**: Add accounts first:
```
@security-auditor Add account: [Service], [Email], priority=[level]
```

### Report not generating
**Solution**: Check permissions on `~/.security-audit/` directory:
```bash
ls -la ~/.security-audit/
chmod -R u+w ~/.security-audit/
```

---

## Advanced Usage

### Batch Import from CSV

```
@security-auditor Import accounts from ~/Downloads/accounts.csv
```

**CSV Format**:
```csv
service,email,priority,has_2fa,2fa_method
Gmail,user@example.com,critical,true,TOTP
GitHub,dev@example.com,high,true,TOTP
Netflix,user@example.com,medium,false,
```

### Custom Compliance Report

```
@security-auditor Generate NIST compliance report
@security-auditor Generate OWASP compliance report
```

### Compare Security Over Time

```
@security-auditor Show security trend: last 6 months
```

### Export for Team Review

```
@security-auditor Generate executive summary for security review meeting
```

---

## Getting Help

### Check Plugin Status
```
@security-auditor Status check
```

### View Documentation
- README.md: Full documentation
- DESIGN.md: Technical design
- SUMMARY.md: Quick overview
- SKILL.md: Security patterns library

### Example Workflows
```
@security-auditor Show example workflows
```

---

## Tips for Best Results

### 1. Accurate Account Inventory
Keep your account list current. Remove old accounts, add new ones.

### 2. Regular Checks
Set calendar reminders for monthly breach checks and quarterly audits.

### 3. Act on Findings
Prioritize critical/high findings. Address within recommended timeframes.

### 4. Update After Changes
When you change a password or enable 2FA, update the plugin:
```
@security-auditor Password changed for Gmail
@2fa-tracker 2FA enabled for GitHub: TOTP
```

### 5. Use Strong Passwords
The plugin can analyze, but you must create strong passwords. Use a password manager.

### 6. Enable 2FA Everywhere
Especially on critical accounts (email, banking, password manager).

### 7. Don't Ignore Breaches
If your email appears in a breach, act immediately. Don't wait.

---

## Quick Reference Commands

```bash
# Setup
@security-auditor Initialize
@security-auditor Add account: [Service], [Email], priority=[level]

# Auditing
@security-auditor Run comprehensive audit
@breach-monitor Check [email]
@2fa-tracker Show status

# Updates
@security-auditor Password changed for [Service]
@2fa-tracker 2FA enabled for [Service]: [method]

# Reports
@security-auditor Generate compliance report
@breach-monitor Show breach history
@2fa-tracker Coverage statistics

# Configuration
@security-auditor Show config
@security-auditor Update policy: [settings]
@security-auditor Set reminder: [schedule]
```

---

**You're now ready to audit your security! Start with:**

```
@security-auditor Run comprehensive security audit
```

**Questions?** Check README.md or ask the agents directly - they're here to help!
