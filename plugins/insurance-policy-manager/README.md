# Insurance Policy Manager Plugin

> Comprehensive insurance policy tracking, coverage analysis, and claims management for complete financial protection

## Overview

The Insurance Policy Manager plugin provides a complete insurance management system with specialized agents for policy cataloging, coverage gap analysis, and claims tracking across all insurance types. Built on proven insurance management frameworks and industry best practices.

## Features

### Core Capabilities

- **Multi-Policy Inventory**: Track health, auto, home, life, disability, and umbrella insurance
- **Coverage Gap Analysis**: Identify protection gaps using industry-standard formulas (DIME, etc.)
- **Claims Management**: Document and track claims from filing through settlement
- **Renewal Tracking**: Automated reminders for policy renewals
- **Beneficiary Management**: Critical tracking and annual review reminders
- **Premium Optimization**: Compare coverage costs and identify savings opportunities
- **Document Organization**: Centralized storage for all policy and claims documents
- **Coverage Adequacy Scoring**: Objective assessment of insurance protection level

### Key Benefits

- **Financial Protection**: Ensure comprehensive coverage across all risk areas
- **Proactive Management**: Never miss a renewal or beneficiary review
- **Claims Excellence**: Systematic documentation improves claim outcomes
- **Cost Optimization**: Identify overlaps and gaps to optimize spending
- **Peace of Mind**: Confidence in complete, organized insurance portfolio

## Plugin Structure

### Agents (3)

#### 1. policy-inventory-manager (Haiku)
**Role**: Policy cataloging and document organization

**Responsibilities**:
- Catalog all insurance policies with complete details
- Track renewal dates and expiration warnings
- Manage beneficiary information
- Organize policy documents and insurance cards
- Monitor premium payments and payment schedules
- Maintain agent and company contact information

**When to Use**:
- "Add my health insurance policy"
- "Show all my insurance policies"
- "What policies are expiring soon?"
- "Update beneficiary information"
- "Track premium payments"

**Key Features**:
- Comprehensive policy data structure
- Renewal date monitoring (30/60/90-day alerts)
- Beneficiary tracking and annual review reminders
- Document organization by policy type
- Premium payment tracking

#### 2. coverage-analyzer (Sonnet)
**Role**: Coverage adequacy assessment and gap identification

**Responsibilities**:
- Perform comprehensive coverage analysis
- Identify protection gaps and overlaps
- Calculate recommended coverage using industry formulas
- Generate personalized recommendations
- Assess life event impacts on insurance needs
- Provide coverage adequacy scoring

**When to Use**:
- "Analyze my insurance coverage"
- "Do I have enough life insurance?"
- "What insurance am I missing?"
- "Just got married - review coverage needs"
- "Am I over-insured or under-insured?"

**Key Features**:
- DIME method for life insurance calculation
- Income replacement analysis for disability
- Asset protection evaluation for umbrella
- Comprehensive gap identification
- Personalized recommendations with cost estimates
- Coverage adequacy score (0-100)

#### 3. claims-tracker (Haiku)
**Role**: Claims documentation and follow-up management

**Responsibilities**:
- Record all insurance claims with complete details
- Track claim status through resolution
- Organize claim documentation (photos, receipts, reports)
- Log all communications with insurance companies
- Monitor settlement offers and payments
- Provide follow-up reminders for pending actions

**When to Use**:
- "File an insurance claim"
- "Update claim status"
- "Show my claims history"
- "What claims need follow-up?"
- "Track claim settlement"

**Key Features**:
- Comprehensive claims database
- Timeline tracking from filing to settlement
- Document management by claim
- Communication logging
- Follow-up alerts for stale claims
- Settlement tracking and analysis

### Skill (1)

#### insurance-management
**Purpose**: Expert knowledge for insurance portfolio management

**Contents**:
- Policy types and coverage standards (health, auto, home, life, disability, umbrella)
- Coverage calculation formulas (DIME, income replacement, asset protection)
- Claims management best practices
- Life event insurance checklists (marriage, baby, home purchase, retirement)
- Annual review procedures
- Common insurance mistakes and fixes
- Shopping and comparison strategies

**Key Sections**:
- Part 1: Policy Types and Coverage Standards
- Part 2: Coverage Analysis Frameworks
- Part 3: Claims Management Best Practices
- Part 4: Life Events and Insurance Updates
- Part 5: Common Insurance Mistakes
- Part 6: Annual Insurance Review Checklist
- Part 7: Insurance Shopping Best Practices
- Part 8: Coverage Optimization Strategies

### Templates (3)

#### 1. policy-inventory.json
Complete policy inventory structure with examples for all insurance types.

**Included Policy Types**:
- Health Insurance (PPO, HMO, HDHP)
- Auto Insurance (liability, collision, comprehensive)
- Home Insurance (dwelling, property, liability)
- Life Insurance (term, whole, universal)
- Disability Insurance (short-term, long-term)
- Umbrella Insurance (excess liability)

**Key Data Points**:
- Policy identification and dates
- Premium and payment tracking
- Coverage details and limits
- Beneficiary information
- Agent and claims contacts
- Document references
- Review schedule

#### 2. coverage-analysis.json
Comprehensive coverage analysis template with gap identification and recommendations.

**Analysis Components**:
- User profile and financial situation
- Current coverage assessment by type
- Recommended coverage levels
- Gap analysis (critical, important, minor)
- Coverage adequacy scoring
- Action plan (immediate, short-term, long-term)
- Financial impact analysis
- Comparative analysis vs peers and benchmarks

**Calculation Methods**:
- DIME method for life insurance
- 60-70% income replacement for disability
- Asset-based umbrella recommendations
- Industry benchmarks and peer comparisons

#### 3. claims-log.json
Complete claims tracking database with examples for auto and home claims.

**Claim Record Structure**:
- Claim identification and status
- Incident details and documentation
- Timeline from filing to settlement
- Communication log with insurance
- Document management
- Settlement details and payments
- Lessons learned

**Statistics and Analysis**:
- Claims history by type and year
- Settlement time analysis
- Impact on premiums and insurability
- Best practices and tips

## Installation

### Prerequisites

- Claude Code CLI installed
- Puerto plugin system configured
- Bash shell access
- jq for JSON processing (optional but recommended)

### Quick Install

```bash
# Clone or copy plugin to Puerto plugins directory
cp -r insurance-policy-manager ~/.claude/plugins/

# Or use Puerto's plugin installation system
puerto install insurance-policy-manager
```

### Directory Structure

```
insurance-policy-manager/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── agents/
│   ├── policy-inventory-manager.md
│   ├── coverage-analyzer.md
│   └── claims-tracker.md
├── skills/
│   └── insurance-management/
│       └── SKILL.md          # Insurance management knowledge
├── templates/
│   ├── policy-inventory.json
│   ├── coverage-analysis.json
│   └── claims-log.json
└── README.md
```

### Data Storage

The plugin stores data in `~/.insurance-policies/`:

```
~/.insurance-policies/
├── policy-inventory.json        # All policies
├── claims-log.json              # All claims
├── analysis/
│   └── coverage-analysis.json   # Latest analysis
├── documents/
│   ├── health/                  # Policy documents by type
│   ├── auto/
│   ├── home/
│   ├── life/
│   ├── disability/
│   └── umbrella/
└── claims-documents/
    ├── active/                  # Active claims
    ├── closed/                  # Closed claims
    └── denied/                  # Denied claims
```

## Usage Examples

### Starting Your Insurance Portfolio

```bash
# 1. Create initial policy inventory
@policy-inventory-manager Add my health insurance policy

# 2. Add all other policies
@policy-inventory-manager Add auto insurance
@policy-inventory-manager Add home insurance
@policy-inventory-manager Add life insurance

# 3. View complete inventory
@policy-inventory-manager Show all policies

# 4. Analyze coverage
@coverage-analyzer Analyze my insurance coverage

# 5. Review recommendations
# Follow the prioritized action plan from analysis
```

### Comprehensive Coverage Review

```bash
# Get detailed coverage analysis
@coverage-analyzer Perform comprehensive portfolio review

# The analyzer will:
# 1. Request your profile information (age, income, dependents, etc.)
# 2. Load your policy inventory
# 3. Analyze each insurance type
# 4. Calculate recommended coverage using proven formulas
# 5. Identify gaps and overlaps
# 6. Generate prioritized action plan
# 7. Provide coverage adequacy score

# Example output:
# Coverage Score: 68/100 (Fair)
# Critical Gaps: Life insurance $1.3M under-insured
# Recommendations:
#   1. Add $1M term life (HIGH priority)
#   2. Purchase $2M umbrella (MEDIUM-HIGH priority)
#   3. Add spouse disability coverage (MEDIUM priority)
```

### Filing and Tracking Claims

```bash
# 1. File new claim
@claims-tracker File auto insurance claim

# Provide details:
# - Date of incident
# - Location
# - Description
# - Estimated damage
# - Police report info (if applicable)

# 2. Update claim as it progresses
@claims-tracker Update claim CLAIM-20251023-a7b3
# - Claim number received
# - Adjuster assigned
# - Inspection scheduled
# - Settlement offered

# 3. Add documentation
@claims-tracker Add document to claim CLAIM-20251023-a7b3
# Upload photos, estimates, receipts

# 4. Check follow-up items
@claims-tracker What claims need follow-up?
# Shows stale claims, missing info, pending actions

# 5. View claims history
@claims-tracker Show all claims
@claims-tracker Show active claims only
```

### Policy Renewal Management

```bash
# Check upcoming renewals
@policy-inventory-manager What renewals are coming up?

# Output:
# === Policy Renewal Status ===
#
# Home Insurance - Allstate
#   Renewal: 2025-12-01 (38 days)
#   Action: Contact agent to review coverage
#   Agent: John Smith - (555) 123-4567
#
# Auto Insurance - State Farm
#   Renewal: 2026-04-15 (174 days)
#   No immediate action needed

# Set up renewal reminders
# - 60 days: Start shopping for quotes
# - 30 days: Contact current agent
# - 14 days: Make decision
# - 7 days: Ensure payment method current
```

### Annual Insurance Review

```bash
# January: Annual review process

# 1. Review all policies
@policy-inventory-manager Show inventory summary

# 2. Update life changes
# Marriage, births, home purchase, income changes, etc.

# 3. Review beneficiaries (CRITICAL)
@policy-inventory-manager Review beneficiaries for all life policies

# 4. Analyze coverage adequacy
@coverage-analyzer Perform annual coverage review

# 5. Shop for better rates
# Get quotes from 3-5 companies
# Compare coverage levels and costs

# 6. Update documentation
# Home inventory, policy documents, contact info

# 7. Review claim history
@claims-tracker Show claims from last year
# Consider impact on premiums and deductibles
```

### Life Event Reviews

```bash
# Marriage
@coverage-analyzer Just got married - review coverage needs
# - Combine or separate health insurance
# - Increase life insurance
# - Update beneficiaries
# - Combine auto/home policies
# - Update all policy names

# New Baby
@coverage-analyzer Had a baby - what insurance changes?
# - Add to health insurance (30 days)
# - Increase life insurance ($100k-$250k per child)
# - Update beneficiaries (use trust, not minor directly)
# - Consider stay-at-home parent term life

# Home Purchase
@coverage-analyzer Bought a house - review insurance
# - Purchase homeowners insurance (required)
# - Evaluate flood insurance
# - Consider umbrella policy
# - Increase life insurance (mortgage)
# - Cancel renters insurance

# Job Change
@coverage-analyzer Changed jobs - insurance review
# - Health insurance transition (COBRA vs new employer)
# - Review group life/disability changes
# - Update disability if income increased
# - Verify all policies still active
```

## Workflows

### 1. New Policy Setup Workflow

```
Start
  ↓
policy-inventory-manager: Add policy
  ↓
Gather policy details
  ↓
Create policy record
  ↓
Upload policy documents
  ↓
Set renewal reminders
  ↓
[If life insurance]
  ↓
Designate beneficiaries
  ↓
coverage-analyzer: Evaluate adequacy
  ↓
End
```

### 2. Comprehensive Coverage Analysis Workflow

```
Start
  ↓
coverage-analyzer: Initiate analysis
  ↓
Load policy inventory
  ↓
Gather user profile
  ↓
Analyze each coverage type:
  - Health
  - Auto
  - Home
  - Life (DIME method)
  - Disability
  - Umbrella
  ↓
Identify gaps and overlaps
  ↓
Calculate coverage score
  ↓
Generate recommendations
  ↓
Create action plan
  ↓
Save analysis report
  ↓
Present findings to user
  ↓
End
```

### 3. Claims Management Workflow

```
Incident Occurs
  ↓
Document damage (photos/videos)
  ↓
claims-tracker: File claim
  ↓
Contact insurance company
  ↓
Get claim number
  ↓
claims-tracker: Update with claim number
  ↓
Adjuster assigned
  ↓
claims-tracker: Add adjuster info
  ↓
Schedule inspection
  ↓
Upload documentation
  ↓
Receive estimate/settlement
  ↓
claims-tracker: Record settlement
  ↓
Complete repairs/resolution
  ↓
claims-tracker: Close claim
  ↓
Move docs to closed folder
  ↓
End
```

### 4. Annual Review Workflow

```
January (or anniversary date)
  ↓
policy-inventory-manager: Generate inventory
  ↓
Review all policies for changes
  ↓
coverage-analyzer: Perform analysis
  ↓
Identify any gaps or overlaps
  ↓
Review beneficiaries (CRITICAL)
  ↓
Update for life events
  ↓
Shop for better rates
  ↓
Adjust coverage as needed
  ↓
Update documentation
  ↓
Schedule next review
  ↓
End
```

## Best Practices

### Policy Management

1. **Complete Inventory**: Catalog ALL policies (don't miss disability, umbrella, etc.)
2. **Regular Updates**: Update after any policy change or life event
3. **Document Everything**: Store all policy docs, declarations pages, insurance cards
4. **Beneficiary Reviews**: Review annually and after major life events (CRITICAL)
5. **Renewal Monitoring**: Set reminders 30-60 days before renewal
6. **Contact Information**: Keep agent and claims contacts current

### Coverage Analysis

1. **Annual Review**: Perform comprehensive analysis yearly
2. **Life Event Triggers**: Review immediately after major life changes
3. **Use Proven Formulas**: DIME for life, 60-70% for disability, asset-based for umbrella
4. **Address Critical Gaps First**: Prioritize life insurance with dependents
5. **Consider Costs**: Balance adequate coverage with affordability
6. **Peer Comparison**: Compare to industry benchmarks and peer averages

### Claims Management

1. **Immediate Documentation**: Photos/videos at time of incident
2. **File Promptly**: Contact insurance within 24-48 hours
3. **Organized Records**: One folder per claim with all documents
4. **Communication Log**: Track all calls, emails, conversations
5. **Follow-Up**: Weekly check-ins if no updates from adjuster
6. **Consider Deductible**: Self-insure claims <2x deductible amount

### Security and Privacy

1. **Encrypt Storage**: Use encrypted cloud storage for digital copies
2. **Physical Security**: Store paper docs in fireproof safe or safe deposit box
3. **Access Control**: Share access info with trusted family/executor only
4. **Regular Backups**: Backup digital files regularly
5. **Secure Transmission**: Use secure methods when sharing with agents
6. **Redact Sensitive Info**: Remove SSNs when sharing documents

## Coverage Formulas

### Life Insurance (DIME Method)

```
D = Debt (all non-mortgage debt)
I = Income (10-15x annual income, based on age)
M = Mortgage balance
E = Education costs for children ($100k-$200k each)

Total Recommended = D + I + M + E

Example:
Age 35, $100k income, $20k debt, $300k mortgage, 2 kids
D = $20,000
I = $100,000 × 12 = $1,200,000
M = $300,000
E = 2 × $150,000 = $300,000
Total = $1,820,000 recommended coverage
```

### Disability Insurance

```
Monthly Benefit = Gross Monthly Income × 0.60 to 0.70
Elimination Period = Emergency Fund Coverage Period

Example:
$90,000 annual income = $7,500/month
Recommended benefit: $7,500 × 0.65 = $4,875/month
Elimination period: 90 days (if 3-month emergency fund)
Benefit period: To age 65
Definition: Own occupation (preferred)
```

### Umbrella Insurance

```
Recommended Coverage = Greater of:
1. Total liquid assets + home equity
2. 2-3× annual income for high earners

Example:
$200k income, $400k investments, $300k home equity
Method 1: $400k + $300k = $700k → Round to $1M
Method 2: $200k × 2.5 = $500k
Recommendation: $1M umbrella policy
```

## Coverage Standards

### Minimum Recommended Coverage

| Insurance Type | Minimum Recommended |
|----------------|---------------------|
| **Health** | Essential health benefits (ACA minimum) |
| **Auto Liability** | 100/300/100 ($100k per person, $300k per accident, $100k property) |
| **Home Dwelling** | 100% replacement cost (not market value) |
| **Life** | 10x annual income (with dependents) |
| **Disability** | 60% of income to age 65 |
| **Umbrella** | $1M if income >$100k or assets >$250k |

### Optimal Coverage

| Insurance Type | Optimal Coverage |
|----------------|------------------|
| **Auto Liability** | 250/500/100 or higher |
| **Home Liability** | $500,000 minimum |
| **Life** | DIME method calculation |
| **Disability** | 70% income, own occupation, to age 65, COLA rider |
| **Umbrella** | 2-3x annual income or total net worth protection |

## Troubleshooting

### Common Issues

**Issue**: Policies not loading
**Solution**: Check file permissions on `~/.insurance-policies/` directory

**Issue**: Coverage analysis showing gaps despite adequate coverage
**Solution**: Verify policy amounts entered correctly in inventory, ensure all policies cataloged

**Issue**: Claims documents not organizing
**Solution**: Ensure claims-documents folders exist, check claim status (active/closed)

**Issue**: Renewal reminders not working
**Solution**: Verify renewal dates in YYYY-MM-DD format, check expiration_date field

**Issue**: Beneficiary warnings even after update
**Solution**: Ensure beneficiaries.last_reviewed date is recent, check all life insurance policies

### Data Validation

```bash
# Validate policy inventory structure
jq empty ~/.insurance-policies/policy-inventory.json
# No output = valid JSON

# Check policy count
jq '.statistics.total_policies' ~/.insurance-policies/policy-inventory.json

# List all policy types
jq '.policies[].policy_type' ~/.insurance-policies/policy-inventory.json

# Find policies missing beneficiaries
jq '.policies[] | select(.policy_type == "life" and (.beneficiaries.primary | length == 0))' ~/.insurance-policies/policy-inventory.json
```

## Integration

### With Other Puerto Plugins

**Digital Legacy Planner**:
- Policy inventory feeds into estate planning
- Beneficiary information critical for legacy
- Insurance policies part of asset inventory

**Financial Planning Plugins**:
- Premium costs feed into budget planning
- Coverage analysis informs financial security
- Life insurance tied to estate value

### External Systems

**Password Managers**:
- Store insurance portal logins
- Link to policy records

**Cloud Storage**:
- Backup policy documents
- Share with family/executor

**Calendar Apps**:
- Renewal date reminders
- Annual review scheduling
- Claims follow-up alerts

## Maintenance

### Regular Tasks

**Weekly**:
- Check active claims for updates
- Review follow-up items

**Monthly**:
- Verify premium payments processed
- Update any policy changes

**Quarterly**:
- Review upcoming renewals (60-day lookout)
- Check for new discounts

**Annually** (January recommended):
- Comprehensive coverage review
- Update beneficiaries
- Shop for better rates
- Update documentation
- Recalculate coverage needs

### Life Event Triggers

Perform immediate review after:
- Marriage or divorce
- Birth or adoption
- Home purchase or sale
- Job change or promotion
- Significant income change (>20%)
- Starting or closing business
- Major health diagnosis
- Inheritance or windfall
- Retirement

## Security Considerations

### Sensitive Data

This plugin handles highly sensitive information:
- Social Security numbers (last 4 digits)
- Policy numbers and account details
- Beneficiary information
- Financial data (income, assets)
- Claims documentation

### Protection Measures

1. **Encryption**: Encrypt `~/.insurance-policies/` directory
2. **Access Control**: Restrict file permissions (`chmod 700`)
3. **Backup Security**: Encrypt backups before cloud storage
4. **Sharing**: Never email unencrypted policy info
5. **Disposal**: Securely delete old policy documents

### Compliance

- HIPAA: Health insurance information protected
- GLBA: Financial insurance data protected
- State Insurance Privacy Laws: Varies by state
- Estate Planning: Executor needs access info

## FAQ

**Q: How often should I review my insurance coverage?**
A: Annually, plus immediately after major life events (marriage, baby, home purchase, job change).

**Q: What's the most critical insurance gap?**
A: Life insurance when you have dependents. Use DIME method to calculate needs.

**Q: Should I file a claim for small damages?**
A: Generally no if damages are less than 2x your deductible. Claims can increase premiums.

**Q: How do I know if I need umbrella insurance?**
A: If household income >$100k or net worth >$250k, umbrella insurance is recommended.

**Q: What's the biggest insurance mistake people make?**
A: Outdated beneficiary designations. Review annually and after major life events.

**Q: How much disability insurance do I need?**
A: 60-70% of your gross income, to age 65, with "own occupation" definition preferred.

**Q: Should I get life insurance through my employer only?**
A: No. Supplement group coverage with individual term life - it's portable and usually more coverage.

**Q: What documents should I keep for claims?**
A: Photos/videos of damage, all receipts, estimates, police reports, communication logs, and settlement paperwork. Keep for 7 years minimum.

## Support and Contributing

### Getting Help

- Review insurance-management skill for detailed guidance
- Check templates for proper data structure
- Consult agent descriptions for specific capabilities

### Contributing

Contributions welcome:
- Coverage analysis improvements
- Additional insurance types
- Enhanced claim tracking
- Better formulas and benchmarks

### Feedback

Report issues or suggestions for:
- Missing coverage types
- Calculation formula improvements
- New features or agents
- Documentation clarifications

## License

MIT License - See LICENSE file for details

## Credits

**Developed by**: bandofai
**Version**: 1.0.0
**Based on**: Puerto plugin architecture and subagent-creation skill patterns
**Insurance Expertise**: Industry-standard formulas and best practices from professional insurance and financial planning

## Changelog

### Version 1.0.0 (2025-10-23)
- Initial release
- 3 specialized agents (policy-inventory-manager, coverage-analyzer, claims-tracker)
- Comprehensive insurance-management skill
- 3 JSON templates (policy inventory, coverage analysis, claims log)
- Support for 6 insurance types (health, auto, home, life, disability, umbrella)
- DIME method life insurance calculation
- Coverage adequacy scoring system
- Claims workflow management

---

**Protect what matters. Manage your insurance with confidence.**
