# Security Auditing Skill

Comprehensive patterns for password analysis, breach monitoring, and 2FA tracking.

## Password Strength Analysis

### Entropy Calculation
- Minimum: 50 bits (acceptable)
- Recommended: 75+ bits (strong)
- Excellent: 100+ bits (very strong)

### Pattern Detection
- Dictionary words: Weakness
- Common substitutions (@ for a): Weakness
- Predictable sequences (123, abc): Weakness
- Random characters: Strength

### Age Tracking
- 0-90 days: Fresh
- 90-180 days: Good
- 180-365 days: Should rotate
- 365+ days: Must rotate

**CRITICAL**: Never store actual passwords, only metadata (length, age, last-changed date).

## Have I Been Pwned API

### K-Anonymity for Privacy
1. Hash password with SHA-1
2. Send only first 5 characters of hash
3. Receive list of matching hashes
4. Compare locally for match

Example:
- Password: "P@ssw0rd"
- SHA-1: "21BD12DC183F740EE76F27B78EB39C8AD972A757"
- Send: "21BD1"
- Receive: List of hashes starting with "21BD1"
- Compare: Find full match locally

### Breach Severity
- Critical: Password exposed, active account
- High: Email in major breach
- Medium: Old breach, account inactive
- Low: Related email exposed

## 2FA Methods Ranking

1. **Hardware Keys** (YubiKey, Titan): Most secure, phishing-resistant
2. **Authenticator Apps** (Google Authenticator, Authy): Secure, convenient
3. **SMS**: Better than nothing, vulnerable to SIM swapping
4. **Email**: Weakest, not recommended

## NIST SP 800-63B Guidelines

- Minimum 8 characters (12+ recommended)
- No complexity requirements (random > complex)
- No periodic rotation (change only if compromised)
- Screen against breached passwords
- Enable 2FA for all accounts

## OWASP Best Practices

- Use password managers
- Unique password per account
- Enable 2FA everywhere possible
- Monitor for breaches regularly
- Secure password recovery options

## Risk Scoring (0-100)

### Components
- Password strength: 0-40 points
- 2FA status: 0-30 points
- Breach exposure: 0-30 points (negative)

### Calculation
```
score = password_strength + 2fa_bonus - breach_penalty
if score < 0: score = 0
if score > 100: score = 100
```

### Risk Levels
- 80-100: Low risk (green)
- 60-79: Medium risk (yellow)
- 40-59: High risk (orange)
- 0-39: Critical risk (red)

## Data Storage

### What to Store
✅ Account names and usernames
✅ Password metadata (length, age)
✅ 2FA status
✅ Breach check dates and results
✅ Risk scores

### What NOT to Store
❌ Actual passwords
❌ Password hints
❌ Security question answers (unless encrypted)

## Privacy Protection

1. Store locally only (`~/.security-audit/`)
2. Encrypt sensitive fields
3. Use k-anonymity for breach checks
4. No external uploads without consent
5. Easy data export/deletion

---

**All agents must follow these patterns for secure, privacy-preserving security auditing.**
