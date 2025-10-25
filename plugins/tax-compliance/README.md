# Tax Compliance Specialist Plugin

Professional tax obligation tracking, filing preparation, and regulatory compliance for Claude Code.

## Overview

The Tax Compliance Specialist Plugin provides a comprehensive suite of agents and skills for managing tax obligations, preparing filings, ensuring compliance, and monitoring regulatory changes across multiple jurisdictions.

## What's Included

### Agents

#### tax-tracker
Monitors tax deadlines, obligations, and filing requirements with multi-level alerts.

**Key Features**:
- Multi-jurisdiction deadline tracking
- Automated alert generation (30/14/7/1 day warnings)
- Obligation status monitoring
- Calendar integration
- Multi-entity support

**Activation**: `@tax-tracker` or automatic for deadline queries

**Model**: Haiku (fast, cost-effective for deterministic tracking)

#### filing-preparer
Prepares complete filing documentation packages with validation.

**Key Features**:
- Skill-aware document generation
- Template-based filing packages
- Completeness validation
- Multi-format support (Excel, PDF, Word)
- Audit trail creation

**Activation**: `@filing-preparer` or automatic when preparing filings

**Model**: Sonnet (judgment required for document preparation)

#### compliance-checker
Validates compliance against current regulations (read-only).

**Key Features**:
- Comprehensive compliance validation
- Priority-based findings
- Actionable recommendations
- Regulation citations
- Gap analysis

**Activation**: `@compliance-checker` or automatic for compliance reviews

**Model**: Sonnet (regulatory expertise required)

**Security**: Read-only access (cannot modify files under review)

#### regulation-monitor
Tracks and reports on regulation changes with impact analysis.

**Key Features**:
- Multi-jurisdiction monitoring
- Impact assessment
- Change notifications
- Historical tracking
- Action item generation

**Activation**: `@regulation-monitor` or automatic for regulation queries

**Model**: Sonnet (interpretation and analysis required)

### Skills

#### tax-tracking
Comprehensive patterns for obligation and deadline tracking including jurisdiction mapping, alert strategies, and status tracking.

**Location**: `skills/tax-tracking/SKILL.md`

**Key Patterns**:
- Deadline calculation algorithms
- Multi-level alert thresholds (30/14/7/1 days)
- Status tracking taxonomy
- Multi-jurisdiction coordination
- Dashboard design patterns

#### filing-preparation
Standards for preparing tax filing documentation with quality assurance procedures and audit trail requirements.

**Location**: `skills/filing-preparation/SKILL.md`

**Key Patterns**:
- Document assembly workflows
- Filing package structure
- Form completion standards
- Quality assurance procedures
- Audit trail documentation

#### compliance-validation
Frameworks for validating regulatory compliance with risk assessment and remediation strategies.

**Location**: `skills/compliance-validation/SKILL.md`

**Key Patterns**:
- Three-tier validation framework
- Risk classification matrix
- Finding classification standards
- Remediation guidance templates
- Prior year comparison framework

## Installation

```bash
# Install the plugin
/plugin install tax-compliance@puerto
```

After installation, restart Claude Code to activate all agents and skills.

## Usage

### Basic Workflow

1. **Track Obligations**: `@tax-tracker show all upcoming deadlines`
2. **Prepare Filing**: `@filing-preparer prepare Q1 2025 federal return`
3. **Validate Compliance**: `@compliance-checker review federal filing package`
4. **Monitor Changes**: `@regulation-monitor check for Q1 2025 updates`

### Example Scenarios

#### Scenario 1: Quarterly Filing Cycle

```
User: @tax-tracker what are my Q1 2025 deadlines?

Response: Lists federal, state, local obligations with dates:
- Federal Form 941 Q1: Due April 30, 2025
- Federal Form 1065: Due March 15, 2025
- State CA DE-9 Q1: Due April 30, 2025
...

User: @filing-preparer prepare federal Form 1120 for Q1 2025

Response: Generates complete filing package with:
- Primary Form 1120
- All required schedules (A, C, J, K, L, M-1, M-2)
- Supporting forms (4562, 4797, etc.)
- Validation checklist
- Audit trail

User: @compliance-checker validate Form 1120 package

Response: Reviews for compliance, provides report with:
- Completeness: 85%
- Accuracy: 90%
- Compliance: 75%
- 7 findings identified (2 critical, 2 high, 2 medium, 1 low)
- Specific remediation steps for each issue

User: (after fixing issues) @tax-tracker mark federal 1120 Q1 as filed

Response: Updates tracking:
- Status changed to "filed"
- Next deadline set (Q2 941 due July 31)
- Dashboard updated
```

#### Scenario 2: Multi-State Compliance

```
User: @tax-tracker track obligations for entities in CA, NY, TX

Response: Creates multi-state tracking dashboard showing:
- Federal obligations (all entities)
- California obligations (CA entities only)
- New York obligations (NY entities only)
- Texas obligations (TX entities only)
- Deadlines coordinated by conformity rules

User: @compliance-checker validate nexus determination for TX

Response: Reviews business activities, determines:
- Physical nexus: Yes (office location)
- Economic nexus: Yes (sales exceed threshold)
- Filing obligations: Franchise tax, sales tax
- Registration requirements: Texas Comptroller
- Annual report requirements

User: @regulation-monitor any state tax changes affecting my entities?

Response: Summarizes relevant state law changes:
- California AB 123: New business incentive credit (affects 2 entities)
- New York TSB-M-25-5C: Apportionment clarification (affects 3 entities)
- Texas: Disaster relief available per IRS Notice 2025-15
- Action items generated for each change
```

#### Scenario 3: Regulation Update Response

```
User: @regulation-monitor summarize IRS Notice 2025-XX impact

Response: Analyzes notice, provides:
- What changed: Extended deadlines for disaster areas
- Who's affected: 4 entities in TX/LA
- Which obligations: 6 deadlines extended
- Financial benefit: $15K penalty avoidance, $75K cash flow
- Action items: Update tracking, notify stakeholders

User: @tax-tracker update deadlines based on Notice 2025-XX

Response: Adjusts tracking:
- 6 deadlines extended to September 15, 2025
- Alert schedule recalculated
- Dashboard updated with new dates
- Status changed to "extended - disaster relief"

User: @filing-preparer update templates for new requirements

Response: Modifies filing templates:
- New Schedule K questions added
- Disclosure requirements updated
- Supporting statement templates revised
- Documented in audit trail
```

## Agent Coordination

The agents work together in coordinated workflows:

```
tax-tracker → filing-preparer → compliance-checker → tax-tracker
    ↓                                                      ↑
    └────────────────────→ regulation-monitor ────────────┘
```

**Example Flow**:
1. **tax-tracker** identifies upcoming deadline (30-day alert)
2. **filing-preparer** creates documentation package
3. **compliance-checker** validates for compliance
4. **regulation-monitor** checks for any deadline/requirement changes
5. **tax-tracker** updates status to "filed" when complete

**Status Progression**:
```
pending → documentation_gathering → in_preparation → ready_for_review
    → under_review → revision_required (if issues) → approved → filed → completed
```

## Configuration

### Data Storage

The plugin uses structured storage:

```
.claude/
└── tax-compliance/
    ├── config.json                    # Entity and jurisdiction config
    ├── obligations/
    │   ├── federal.json
    │   ├── state-ca.json
    │   ├── state-ny.json
    │   └── state-tx.json
    ├── filings/
    │   └── 2025/
    │       ├── q1/
    │       │   ├── federal-1120-acme/
    │       │   └── federal-941-acme/
    │       └── q2/
    ├── compliance/
    │   └── reports/
    └── regulations/
        ├── sources.json
        └── updates/
            └── 2025/
```

### Jurisdiction Configuration

Configure monitored jurisdictions in `.claude/tax-compliance/config.json`:

```json
{
  "entities": [
    {
      "name": "Acme Corp",
      "ein": "12-3456789",
      "entity_type": "c-corp",
      "fiscal_year_end": "12-31",
      "jurisdictions": ["federal", "CA", "NY"],
      "addresses": {
        "principal": "123 Main St, San Francisco, CA 94102",
        "ca_location": "123 Main St, San Francisco, CA 94102",
        "ny_location": "456 Broadway, New York, NY 10013"
      }
    }
  ],
  "alert_thresholds": {
    "advance": 30,
    "urgent": 7,
    "critical": 1
  },
  "monitoring": {
    "federal": "weekly",
    "state": "monthly",
    "local": "quarterly"
  }
}
```

## Skills Integration

All agents leverage the skills library for consistent, professional quality:

**filing-preparer** workflow:
```markdown
1. Read filing-preparation skill
2. Apply document assembly patterns
3. Use standardized structure
4. Follow quality assurance procedures
5. Create complete audit trail
```

**tax-tracker** workflow:
```markdown
1. Read tax-tracking skill
2. Apply deadline calculation algorithms
3. Use multi-level alert thresholds
4. Follow status taxonomy
5. Generate dashboard per design patterns
```

**compliance-checker** workflow:
```markdown
1. Read compliance-validation skill
2. Apply three-tier validation framework
3. Use risk classification matrix
4. Generate findings with remediation guidance
5. Provide regulatory citations
```

This ensures consistent, professional quality across all operations.

## Benefits

### For Tax Professionals
- **Automated deadline tracking** reduces missed filings
- **Standardized preparation** ensures completeness
- **Validation catches issues** before submission
- **Regulation monitoring** keeps you current
- **Audit trails** provide defensible documentation

### For Finance Teams
- **Multi-entity coordination** across jurisdictions
- **Compliance assurance** through systematic validation
- **Reduced manual effort** via automation
- **Better deadline management** with proactive alerts
- **Complete documentation** for audit defense

### For Businesses
- **Risk reduction** through validation and compliance
- **Cost savings** through automation and efficiency
- **Improved compliance posture** with systematic approach
- **Penalty avoidance** via proactive deadline management
- **Peace of mind** with professional-grade processes

## Best Practices

### Deadline Tracking
✓ Review tracking dashboard weekly
✓ Respond to 30-day alerts immediately (begin preparation)
✓ Use 14-day alert for progress confirmation
✓ 7-day alert triggers completion priority
✓ 1-day alert = emergency status

### Filing Preparation
✓ Start 30 days before deadline
✓ Read filing-preparation skill before starting
✓ Use skill-based document generation
✓ Validate with compliance-checker before filing
✓ Maintain complete audit trail

### Compliance Validation
✓ Run compliance-checker before every filing
✓ Address critical findings immediately (same day)
✓ Resolve high-priority findings before filing
✓ Document all remediation steps
✓ Re-validate after corrections

### Regulation Monitoring
✓ Check monthly for updates (or per schedule)
✓ Assess impact on obligations immediately
✓ Update templates and procedures as needed
✓ Document all compliance changes
✓ Communicate changes to stakeholders

## Model Usage & Performance

| Agent | Model | Avg Time | Token Usage | Cost/Run | Use Case |
|-------|-------|----------|-------------|----------|----------|
| tax-tracker | Haiku | 5s | ~2K | $0.001 | Fast deadline tracking |
| filing-preparer | Sonnet | 30s | ~8K | $0.024 | Document judgment |
| compliance-checker | Sonnet | 20s | ~6K | $0.018 | Regulatory expertise |
| regulation-monitor | Sonnet | 15s | ~5K | $0.015 | Change interpretation |

**Full compliance cycle**: ~70s, ~21K tokens, ~$0.06

**Cost Optimization**:
- Haiku for tax-tracker saves 90% vs Sonnet
- Sonnet required where judgment/expertise needed
- Batch similar operations for efficiency
- Cache skill content when possible

## Security & Compliance

### Data Protection
- **Local storage only** - No external transmission
- **Read-only compliance-checker** - Cannot modify data under review
- **Audit trail** for all operations
- **Secure credential handling**
- **Access control** via agent permissions

### Access Control
- **Agent-level restrictions** - Least privilege principle
- **Tool whitelisting** - Each agent has minimum required tools
- **File access limitations** - Agents cannot access unrelated files
- **Operation logging** - All actions logged for audit

### Independence
- **compliance-checker** operates read-only (cannot modify files)
- **Separation of duties** - Preparer ≠ Validator
- **Objective validation** - Independent review ensures quality

## Troubleshooting

### Agent Not Activating
**Problem**: Agent doesn't respond to query
**Solution**:
- Use explicit @mention: `@tax-tracker show deadlines`
- Check that query matches agent description
- Verify plugin installed and Claude Code restarted

### Missing Jurisdiction Data
**Problem**: Tracking not showing state obligations
**Solution**:
```
@tax-tracker initialize jurisdiction: CA
```
Configure entities in `.claude/tax-compliance/config.json`

### Filing Package Incomplete
**Problem**: Missing forms or schedules
**Solution**:
```
@compliance-checker validate filing: filings/2025/q1/federal-1120-acme/
```
Review findings report for missing items

### Regulation Updates Not Showing
**Problem**: No regulation changes detected
**Solution**:
- Verify `.claude/tax-compliance/regulations/sources.json` configured
- Check monitoring schedule in config.json
- Manually trigger: `@regulation-monitor check for updates`

## Advanced Usage

### Custom Jurisdictions

Add custom jurisdiction tracking:

```
@tax-tracker add jurisdiction: "County XYZ" with obligations: "Property Tax, Business License"
```

### Batch Processing

Process multiple entities efficiently:

```
@filing-preparer batch prepare Q1 2025 for all entities
```

This will:
- Identify all entities with Q1 obligations
- Prepare filings in efficient order
- Group similar forms together
- Generate consolidated audit trail

### Integration with External Tools

The plugin can integrate with:

**Calendar Systems**:
- Export deadlines to iCal format
- Sync with Google Calendar, Outlook
- Automated reminders via calendar

**Accounting Software**:
- Import financial data from QuickBooks, Xero
- Pull general ledger exports
- Automate data gathering phase

**Document Management**:
- Store filings in SharePoint, Dropbox
- Version control for filing packages
- Centralized document repository

**Notification Systems**:
- Email alerts for critical deadlines
- Slack/Teams notifications
- SMS for emergency alerts

## Examples

### Example 1: New Entity Setup

```
User: I need to track tax obligations for a new Delaware C-corp

@tax-tracker initialize entity: "NewCo Inc" ein: "98-7654321"
  jurisdiction: DE, federal fiscal_year_end: "12-31"

Response: Creates obligation tracking structure:
- Entity profile created
- Federal obligations identified (1120, 941, 940)
- Delaware obligations identified (Franchise Tax, Annual Report)
- Deadlines calculated for current year
- Alert schedule established

@regulation-monitor what are Delaware C-corp filing requirements?

Response: Lists DE and federal obligations:
- Federal Form 1120: Due 4/15 (can extend to 10/15)
- Delaware Franchise Tax: Due 3/1
- Delaware Annual Report: Due 3/1
- Federal Form 941: Quarterly (4/30, 7/31, 10/31, 1/31)
- Delaware Withholding: Monthly if >$500
- Detailed requirements for each

@tax-tracker set deadlines for NewCo Inc

Response: Populates calendar with all deadlines:
- Next 12 months of obligations created
- Alert schedule set for each deadline
- Dashboard updated with NewCo obligations
- Email notification preferences configured
```

### Example 2: Annual Filing Preparation

```
User: Prepare our 2024 federal return

@filing-preparer prepare Form 1120 for TY 2024 entity: "Acme Corp"

Response: Initiates filing package preparation:
- Read filing-preparation skill patterns
- Created package structure: filings/2024/federal-1120-acme/
- Documentation gathering checklist generated
- Estimated completion time: 2-3 hours
- Status: documentation_gathering (0% complete)

(After gathering documentation)

Response: Forms prepared:
- Primary Form 1120 completed
- Schedule A (COGS) completed
- Schedule J (Tax) completed
- Schedule K (Other info) completed
- Schedule L (Balance sheet) completed
- Schedule M-1 (Reconciliation) completed
- Schedule M-2 (Retained earnings) completed
- Validation checklist created
- Audit trail documented
- Status: ready_for_review (100% complete)

@compliance-checker validate 1120 package: filings/2024/federal-1120-acme/

Response: Comprehensive compliance review:
- Completeness: 85% (issues identified)
- Accuracy: 90% (minor issues)
- Compliance: 75% (critical issues found)

**Critical Findings**:
1. Missing Form 4562 (Depreciation) - MUST attach
2. Missing Payment Voucher 1120-V - MUST include

**Recommendation**: DO NOT FILE - Resolve critical issues first

User: Found issue with Schedule M-1

@filing-preparer update Schedule M-1 with correction:
  "Correct depreciation difference from $5,000 to $7,000"

Response: Schedule M-1 revised:
- Depreciation adjustment corrected ($7,000)
- Book-tax reconciliation recalculated
- Taxable income still ties to Form 1120, Line 28 ✓
- Audit trail updated with change documentation
- Reason: Depreciation calculation error discovered

@compliance-checker re-validate 1120 package: filings/2024/federal-1120-acme/

Response: Final validation:
- Completeness: 100% ✓
- Accuracy: 100% ✓
- Compliance: 100% ✓
- All critical issues resolved ✓
- **Status: APPROVED FOR FILING** ✓

@tax-tracker mark federal 1120 as filed confirmation: "IRS-2025-XXXXXX"

Response: Tracking updated:
- Status: filed (filed date: 2025-04-10)
- Confirmation: IRS-2025-XXXXXX recorded
- Next deadline: Q1 941 due 2025-04-30 (20 days)
- Dashboard updated
- Filing archived
```

### Example 3: Multi-State Expansion

```
User: We're expanding to California, what tax obligations do we have?

@regulation-monitor analyze California tax requirements for C-corporation

Response: Comprehensive CA analysis:

**Registration Requirements**:
- CA Secretary of State: Foreign qualification
- CA Franchise Tax Board: Tax registration
- CA EDD: Payroll tax registration
- Local business licenses

**Tax Obligations**:
- CA Form 100 (Franchise Tax): Annual, due 4/15
- CA Minimum Tax: $800/year
- CA DE-9 (Payroll Tax): Quarterly
- CA Sales Tax: If selling tangible goods
- San Francisco Payroll Expense Tax: If SF location

**Nexus Factors Present**:
- Physical presence (office planned)
- Employee presence (hiring CA employees)
- Sales into CA (existing customers)

**Estimated Annual Tax Burden**: $5,000 - $15,000

@tax-tracker add CA obligations for entity: "Acme Corp"

Response: CA obligations added:
- CA Form 100: Added (due 4/15/2026 for TY 2025)
- CA DE-9 Q1: Added (due 4/30/2025)
- CA DE-9 Q2: Added (due 7/31/2025)
- CA DE-9 Q3: Added (due 10/31/2025)
- CA DE-9 Q4: Added (due 1/31/2026)
- SF Payroll Tax Q1: Added (due 4/30/2025)
- Alert schedule established for all obligations
- Dashboard updated with CA obligations

@compliance-checker validate nexus determination for CA

Response: Nexus validation:
**Physical Nexus**: YES ✓
- Office location: 123 Main St, San Francisco, CA
- Employees: 5 (planned)
- Property: Leased office space

**Economic Nexus**: YES ✓
- Sales into CA: $500,000 (exceeds $500K threshold)
- Transactions: 200+ (exceeds threshold)

**Conclusion**: Filing obligations confirmed
**Action Required**:
1. Register with CA FTB (within 15 days)
2. Register with CA EDD (before first payroll)
3. Obtain business licenses
4. Begin CA tax compliance

**Risk Assessment**: High risk if not registered promptly
**Estimated Penalties**: $2,000 - $10,000 if delayed
```

## File Structure

```
tax-compliance/
├── .claude-plugin/
│   └── plugin.json                    # Plugin metadata
├── agents/
│   ├── tax-tracker.md                 # Deadline tracking agent (Haiku)
│   ├── filing-preparer.md             # Document preparation agent (Sonnet)
│   ├── compliance-checker.md          # Validation agent (Sonnet, read-only)
│   └── regulation-monitor.md          # Regulation tracking agent (Sonnet)
├── skills/
│   ├── tax-tracking/
│   │   └── SKILL.md                   # Obligation tracking patterns
│   ├── filing-preparation/
│   │   └── SKILL.md                   # Document preparation standards
│   └── compliance-validation/
│       └── SKILL.md                   # Compliance validation frameworks
├── templates/
│   ├── tracking-dashboard.json        # Dashboard template
│   ├── filing-checklist.md            # Validation checklist template
│   └── compliance-report.md           # Compliance report template
└── README.md                          # This file
```

## Support & Feedback

For issues or suggestions:
- Review the skills library for comprehensive patterns
- Check agent definitions for specific capabilities
- Refer to [Claude Code documentation](https://docs.claude.com/en/docs/claude-code)
- Submit issues to Puerto repository

## Disclaimer

⚠️ **Important**: This plugin provides automation tools for tax compliance tracking and documentation preparation. **It does not constitute tax advice.**

Always consult with qualified tax professionals for:
- Specific tax situations and guidance
- Final review before filing
- Tax planning and strategy
- Complex or unusual circumstances
- Legal interpretations

The plugin is designed to assist tax professionals and finance teams in managing compliance workflows, not to replace professional judgment.

## Contributing

Contributions welcome! To improve this plugin:

1. Review existing agents and skills
2. Identify gaps or enhancement opportunities
3. Submit pull requests with improvements
4. Follow Puerto's plugin architecture standards
5. Maintain comprehensive documentation

## License

MIT License - See main repository for details

---

**Professional tax compliance automation. Track smarter, file confidently, stay compliant.**

**Version**: 1.0.0
**Author**: bandofai
**Repository**: [Puerto](https://github.com/bandofai/puerto)
