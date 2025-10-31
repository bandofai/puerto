# Legal Document Tracker

> Contract expiration, legal deadline monitoring, and document version control specialist

## Overview

The Legal Document Tracker is a comprehensive system for managing contracts, legal deadlines, and document versions. Never miss a critical deadline, lose track of a contract renewal, or wonder what changed between document versions.

## What's Included

### 3 Specialized Agents

1. **contract-monitor** (Haiku, Fast) - Contract tracking and expiration alerts
   - Manages contract database
   - Tracks expiration dates
   - Provides 90/60/30/7-day alerts
   - Handles auto-renewal tracking
   - Links to related documents

2. **deadline-tracker** (Haiku, Fast) - Legal deadline management
   - Critical court deadline tracking
   - Statute of limitations monitoring
   - Multi-level alert system (30/14/7/3/1/0 days)
   - Priority-based organization
   - Extension tracking

3. **document-versioner** (Sonnet) - Version control and comparison
   - Complete version history
   - Document comparison (diff analysis)
   - File integrity verification (SHA-256)
   - Attorney directory management
   - Change documentation

### 1 Comprehensive Skill

**legal-document-management** - Expert patterns for:
- Contract lifecycle management
- Expiration alert systems (90-60-30-7 protocol)
- Legal deadline best practices
- Version control conventions
- Document comparison techniques
- Attorney relationship management
- Data organization and backup
- Security and confidentiality

### 3 Templates

1. **contract-database.json**: Master contract tracking with examples
2. **deadline-calendar.json**: Legal deadline calendar with sample deadlines
3. **attorney-directory.json**: Attorney and law firm contact database

## Key Features

✅ **Never Miss Deadlines**: Multi-level alerts (90/60/30/7 days)
✅ **Auto-Renewal Tracking**: Special handling for auto-renewing contracts
✅ **Version Control**: Complete history with diff analysis
✅ **File Integrity**: SHA-256 hashing for tamper detection
✅ **Attorney Directory**: Comprehensive contact management
✅ **Court Deadline Focus**: Critical priority for time-sensitive legal deadlines
✅ **Statute of Limitations**: Special tracking for non-extendable deadlines
✅ **Cost-Optimized**: Haiku for tracking (90% cost savings vs Sonnet)

## Installation

```bash
# Copy plugin to Puerto
cp -r legal-document-tracker ~/.claude/plugins/marketplaces/puerto/plugins/

# Or for project-specific installation
cp -r legal-document-tracker .claude/plugins/
```

## Quick Start

### 1. Initialize Your Legal Document Database

```bash
# Create directory structure
mkdir -p ~/.legal-docs/contracts

# Copy templates
cp plugins/legal-document-tracker/templates/*.json ~/.legal-docs/

# Start tracking contracts
Use the @contract-monitor agent to add your first contract
```

### 2. Add Your First Contract

Invoke `@contract-monitor` and say:

> "Add new employment contract with Acme Corp, starts Jan 15 2025, ends Jan 15 2026, salary $85k, 30 days notice required"

### 3. Track a Legal Deadline

Invoke `@deadline-tracker` and say:

> "Add court filing deadline: Response to Motion to Dismiss, due Feb 15 2025 at 5pm EST, Case #2024-CV-12345, critical priority"

### 4. Compare Document Versions

Invoke `@document-versioner` and say:

> "Compare employment contract version 1.0 and 1.1"

## Usage Examples

### Contract Expiration Monitoring

```
@contract-monitor check expiring contracts

🚨 CRITICAL (≤7 days):
- Employment Agreement (Acme Corp): Expires in 5 days
  Notice required: 30 days ago (action overdue!)

⚠️  URGENT (≤30 days):
- Apartment Lease: Expires in 22 days
  Notice required: 60 days (8 days remaining to give notice)
```

### Legal Deadline Alerts

```
@deadline-tracker show upcoming deadlines

🚨🚨 EMERGENCY - TODAY:
- Response to Discovery Requests (Case #2024-CV-12345)
  DUE: Today at 5:00 PM EST
  ACTION: File response immediately!

🚨 CRITICAL (≤3 days):
- Motion to Dismiss Filing (Case #2024-CV-67890)
  DUE: January 24, 2025 at 5:00 PM EST (2 days)
```

### Document Version Comparison

```
@document-versioner compare versions 1.0 and 1.1 of employment agreement

ADDED SECTIONS:
━━━━━━━━━━━━━━━━━━
Section 7: Non-Compete Agreement
  Duration: 12 months following termination
  Geographic scope: 50-mile radius

MODIFIED TERMS:
━━━━━━━━━━━━━━━━━━
Section 3.1: Compensation
  BEFORE: Base salary of $80,000 per year
  AFTER:  Base salary of $85,000 per year
  CHANGE: +$5,000 increase
```

## Alert System

### Contract Expirations

- **90 days**: Initial planning alert
- **60 days**: Action preparation phase
- **30 days**: Critical action period (most contracts require 30-60 days notice)
- **7 days**: Emergency alert (likely too late for notice)

### Legal Deadlines

- **30 days**: Initial planning alert
- **14 days**: Active preparation phase
- **7 days**: Final week warning
- **3 days**: Urgent action required
- **1 day**: CRITICAL - immediate completion needed
- **Day of**: EMERGENCY - deadline today!

## Data Organization

```
~/.legal-docs/
├── contracts.json          # Master contract database
├── deadlines.json          # Legal deadline calendar
├── versions.json           # Document version history
└── contracts/              # Actual contract files
    ├── employment/
    ├── rental/
    ├── services/
    └── insurance/
```

## Best Practices

### Contract Management

✅ Enter contracts immediately after execution
✅ Set alerts well in advance of deadlines
✅ Review auto-renewal clauses carefully
✅ Keep complete contract history
✅ Back up regularly

❌ Don't rely on memory for important dates
❌ Don't ignore auto-renewal clauses
❌ Don't wait until last minute to review expiring contracts

### Legal Deadlines

✅ Enter deadlines immediately when received
✅ Include time and timezone
✅ Set multiple reminders
✅ Mark court deadlines as "critical"
✅ Request extensions early if needed

❌ Never assume extensions will be granted
❌ Never trust memory for court deadlines
❌ Never ignore non-court deadlines as "flexible"

### Document Versioning

✅ Keep every version indefinitely
✅ Document all changes clearly
✅ Generate file integrity hashes
✅ Compare versions before signing

❌ Never delete old versions
❌ Never assume versions are identical
❌ Never skip documenting changes

## Security Considerations

- **Encryption**: Store sensitive documents encrypted
- **Access Control**: Limit access to authorized individuals only
- **Attorney-Client Privilege**: Mark and protect privileged communications
- **Backup**: Regular automated backups with integrity verification
- **Retention**: Follow legal document retention requirements

## Automation

### Daily Deadline Check

Set up a daily cron job to check for critical deadlines:

```bash
# Add to crontab
0 9 * * * cd ~ && claude-code --agent deadline-tracker "check upcoming deadlines"
```

### Weekly Contract Review

Review contracts expiring in the next 90 days:

```bash
# Weekly on Monday mornings
0 9 * * 1 cd ~ && claude-code --agent contract-monitor "check contracts expiring in 90 days"
```

## Integration with Workflows

### Contract Renewal Workflow

1. **90 days before**: Alert received
2. **Review terms**: Use @document-versioner to check current contract
3. **Research alternatives**: Compare with market
4. **Decision point**: Renew, renegotiate, or terminate
5. **60 days before**: Begin negotiations if renewing
6. **30 days before**: Give notice if terminating (or as required)
7. **Execution**: Update contract database with new terms

### Court Deadline Workflow

1. **Receive deadline**: Enter immediately into system
2. **Multiple alerts**: 30/14/7/3/1/0 days before
3. **Daily review**: Check deadlines in morning
4. **Track progress**: Mark as "in-progress" when starting
5. **Complete**: Mark as "completed" when filed
6. **Archive**: Keep for records

## Troubleshooting

**Q: Alerts not showing up?**
A: Check date formats are YYYY-MM-DD and status is "pending" or "in-progress"

**Q: Can't compare documents?**
A: Ensure file paths are correct and files exist at specified locations

**Q: Contract marked as expired but still active?**
A: Check auto-renewal status and update endDate if renewed

**Q: Lost contract database?**
A: Restore from backup. Always maintain regular backups!

## Technical Details

### Models Used

- **contract-monitor**: Haiku (fast, cost-effective tracking)
- **deadline-tracker**: Haiku (fast, reliable alerts)
- **document-versioner**: Sonnet (intelligent comparison and analysis)

### Tools Required

- **Read, Write, Edit**: Database management
- **Bash**: File integrity (hashing), text extraction
- **Grep**: Document search and comparison

### Storage Format

All databases use JSON format for easy manipulation with `jq`:

```bash
# Count active contracts
jq '.contracts | map(select(.status == "active")) | length' ~/.legal-docs/contracts.json

# Find critical deadlines
jq '.deadlines | map(select(.priority == "critical" and .status == "pending"))' ~/.legal-docs/deadlines.json
```

## Roadmap

Future enhancements:
- [ ] Calendar integration (iCal, Google Calendar)
- [ ] Email alerts for critical deadlines
- [ ] SMS notifications for same-day deadlines
- [ ] Automated backup to cloud storage
- [ ] Mobile app integration
- [ ] OCR for scanning physical contracts

## Legal Disclaimer

This tool is for organization and tracking purposes only. It does not constitute legal advice. Always consult with a qualified attorney for legal matters. The creators are not responsible for missed deadlines or lost contracts.

## Contributing

Found a bug or have a feature request? Please file an issue in the Puerto repository.

## License

MIT License - See Puerto main repository for details

## Acknowledgments

Developed with input from legal professionals to ensure best practices in legal document management.

---

**Never miss another deadline. Track every contract. Know every change.**
