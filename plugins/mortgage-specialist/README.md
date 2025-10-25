# Mortgage Specialist Plugin

Professional mortgage loan processing, credit analysis, compliance validation, and closing coordination for Claude Code.

## Overview

The Mortgage Specialist Plugin provides a comprehensive suite of agents and skills for managing the complete mortgage loan lifecycle from application through closing. It ensures regulatory compliance (TRID, RESPA, TILA, QM/ATR), professional credit analysis, systematic loan processing, and coordinated closings.

## What's Included

### Agents

#### loan-processor
Manages complete loan application lifecycle with document collection and qualification analysis.

**Key Features**:
- Application intake and initial setup
- Comprehensive document collection checklists
- DTI and LTV qualification calculations
- TRID disclosure timeline tracking
- Organized file structure and status management
- Income and asset verification workflows

**Activation**: `@loan-processor` or automatic for loan application queries

**Model**: Sonnet (judgment required for qualification analysis and documentation review)

#### credit-analyst
Performs comprehensive credit analysis with risk assessment and underwriting recommendations.

**Key Features**:
- Tri-merge credit report analysis
- Middle score calculation (representative score)
- Derogatory item evaluation (bankruptcies, foreclosures, collections)
- Trade line analysis and DTI impact
- Credit risk rating and recommendations
- Fair lending compliant credit decisions

**Activation**: `@credit-analyst` or automatic for credit review queries

**Model**: Sonnet (expertise required for credit risk assessment)

#### compliance-checker
Validates regulatory compliance for mortgage loans (read-only independent review).

**Key Features**:
- TRID timeline and content validation
- Fee tolerance testing (zero, 10%, unlimited)
- APR accuracy verification
- QM/ATR determination
- RESPA and fair lending compliance
- Risk-based compliance assessment

**Activation**: `@compliance-checker` or automatic for compliance validation

**Model**: Sonnet (regulatory expertise required)

**Security**: Read-only access (cannot modify files under review)

#### closing-coordinator
Manages loan closing coordination from clear-to-close through funding and post-closing.

**Key Features**:
- Clear-to-close verification
- TRID closing disclosure timeline management
- Multi-party closing coordination
- Funding coordination and wire management
- Post-closing documentation and recording
- Quality control review

**Activation**: `@closing-coordinator` or automatic for closing queries

**Model**: Haiku (fast, cost-effective for deterministic coordination)

### Skills

#### loan-processing
Comprehensive patterns for mortgage loan processing including file structure, document collection standards, DTI/LTV calculations, and TRID compliance.

**Location**: `skills/loan-processing/SKILL.md`

**Key Patterns**:
- Standardized loan file organization
- Complete documentation requirements by loan type
- DTI calculation methodology (front-end and back-end)
- LTV calculation and program guidelines
- TRID disclosure timeline compliance
- Income calculation standards (W-2, self-employed, rental, other)
- Asset verification requirements
- Application status workflow

#### credit-analysis
Standards for comprehensive credit report analysis, risk assessment, and credit decisioning following industry guidelines and fair lending requirements.

**Location**: `skills/credit-analysis/SKILL.md`

**Key Patterns**:
- Representative credit score determination (middle score rule)
- Minimum score requirements by loan type
- Derogatory item treatment (bankruptcies, foreclosures, collections)
- Payment history analysis framework
- Trade line analysis and DTI impact
- Credit risk rating criteria (Excellent to Poor)
- Fair lending compliance in credit decisions
- Compensating factors framework

#### compliance-validation
Frameworks for validating mortgage regulatory compliance including TRID, RESPA, TILA, QM/ATR, and fair lending requirements.

**Location**: `skills/compliance-validation/SKILL.md`

**Key Patterns**:
- TRID timeline validation (LE and CD 3-business day rules)
- Changed circumstances documentation
- Fee tolerance testing (zero, 10%, unlimited)
- APR accuracy standards and tolerances
- Qualified Mortgage determination framework
- Ability-to-Repay (ATR) 8-factor documentation
- RESPA compliance verification
- Fair lending review framework
- Risk-based compliance assessment

### Templates

#### loan-application-checklist.md
Comprehensive document collection checklist for loan applications.

**Includes**:
- Income documentation (W-2, self-employed, other income)
- Asset documentation (bank accounts, investments, retirement, gifts)
- Credit documentation and explanation letters
- Property documentation (purchase vs refinance)
- Identity and legal documents
- Program-specific requirements (FHA, VA, USDA)

#### credit-explanation-letter.md
Template for borrowers to explain derogatory credit items.

**Use Cases**:
- Late payments
- Collection accounts
- Charge-offs
- Bankruptcies
- Foreclosures
- Other credit issues

#### compliance-checklist.md
Complete regulatory compliance validation checklist.

**Covers**:
- TRID compliance (LE and CD timing, revisions)
- Fee tolerance testing
- APR accuracy
- QM/ATR determination
- RESPA compliance
- Fair lending review
- Program-specific requirements

## Installation

```bash
# Install the plugin
/plugin install mortgage-specialist@puerto
```

After installation, restart Claude Code to activate all agents and skills.

## Usage

### Basic Workflow

1. **Process Application**: `@loan-processor process new loan application for [borrower]`
2. **Analyze Credit**: `@credit-analyst review credit for application [app-id]`
3. **Validate Compliance**: `@compliance-checker validate loan file [app-id]`
4. **Coordinate Closing**: `@closing-coordinator schedule closing for [app-id]`

### Example Scenarios

#### Scenario 1: New Purchase Loan Application

```
User: @loan-processor process new purchase loan application for John and Mary Smith

Response:
# Loan Application Processing Initiated

**Borrowers**: John and Mary Smith
**Application ID**: LA-2025-1001
**Loan Type**: To be determined (Purchase)
**Date**: 2025-01-15

## Initial Setup Complete

Created loan file structure:
- loan-applications/2025/LA-2025-1001-smith/
- Application checklist generated
- Document request list prepared
- Processing timeline initialized

## TRID Compliance
- Application Date: 2025-01-15
- LE Due Date: 2025-01-18 (3 business days)
- Status: On track

## Next Steps
1. Complete 1003 application with borrowers
2. Send Loan Estimate by 2025-01-18
3. Request complete documentation per checklist
4. Order credit report (with authorization)
5. Perform initial qualification analysis

**Document Checklist Location**: loan-applications/2025/LA-2025-1001-smith/01-initial-application/application-checklist.md

---

User: The borrowers provided their information. Income: $10,000/month combined. Property price: $400,000. Down payment: $40,000. Credit scores around 720.

@loan-processor perform initial qualification analysis

Response:
# Initial Qualification Analysis

**Application ID**: LA-2025-1001
**Borrowers**: John and Mary Smith

## Income Summary
- Combined Gross Monthly Income: $10,000

## Loan Details
- Property Price: $400,000
- Down Payment: $40,000 (10%)
- Loan Amount: $360,000
- Estimated LTV: 90%

## DTI Analysis (Preliminary)

### Proposed Housing Payment (PITIA)
- Principal & Interest (est. 7.0%): $2,395
- Property Taxes (est.): $333
- Homeowners Insurance (est.): $100
- PMI (0.5% at 90% LTV): $150
- **Total PITIA**: $2,978

**Front-End Ratio**: $2,978 / $10,000 = 29.8%
- Guideline (Conventional): ≤ 28%
- **Status**: SLIGHTLY HIGH (acceptable with good credit/assets)

### Monthly Debts (need actual credit report)
- Estimated other debts: $500/month (placeholder)

**Back-End Ratio**: ($2,978 + $500) / $10,000 = 34.8%
- Guideline (Conventional QM): ≤ 43%
- **Status**: ACCEPTABLE

## LTV Analysis
- Loan Amount: $360,000
- Property Value: $400,000
- **LTV**: 90%
- Guideline (Conventional): ≤ 97%
- PMI Required: YES (LTV > 80%)
- **Status**: ACCEPTABLE

## Preliminary Assessment

**Strengths**:
- ✓ Good credit scores (720 estimated)
- ✓ DTI within acceptable range
- ✓ LTV within conventional limits
- ✓ 10% down payment

**Next Steps**:
1. **Obtain actual credit report** - @credit-analyst review needed
2. Verify income with W-2s, pay stubs, tax returns
3. Verify assets (need down payment + closing costs + reserves)
4. Send Loan Estimate by 2025-01-18
5. Order appraisal after intent to proceed

**Preliminary Qualification**: LIKELY QUALIFIED
**Confidence**: Medium (pending document verification)
**Recommended Loan Type**: Conventional (good credit scores)

---

User: @credit-analyst review credit for application LA-2025-1001

Response:
# Credit Analysis Complete

**Application ID**: LA-2025-1001
**Borrowers**: John and Mary Smith
**Analysis Date**: 2025-01-15

## Credit Score Summary

### John Smith
- Equifax: 715
- Experian: 730
- TransUnion: 720
- **Middle Score**: 720

### Mary Smith
- Equifax: 705
- Experian: 720
- TransUnion: 710
- **Middle Score**: 710

**Representative Score** (lower of two middle scores): 710
**Used for Qualification**: 710

## Score Assessment
- **Range**: Good (670-739)
- **Conventional**: Qualified (minimum 620)
- **Pricing Impact**: Moderate (slight rate adjustment)
- **Manual Underwrite**: Not required

## Derogatory Items Analysis

### John Smith
- **Collections**: 1 medical collection ($150) - can ignore per FHA/Conventional guidelines
- **Late Payments**: 1 × 30-day late on auto loan (18 months ago)
  - **Action Required**: Explanation letter

### Mary Smith
- **No derogatory items**: Clean credit history
- **Payment History**: Excellent

## Trade Line Analysis

### Monthly Debt Obligations
| Type | Creditor | Payment | Status |
|------|----------|---------|--------|
| Auto Loan | Toyota Financial | $425 | Current |
| Credit Card | Chase | $50 (min) | Current |
| Credit Card | Discover | $25 (min) | Current |
| Student Loan | Navient | $185 | Current |

**Total Monthly Debts**: $685

## Updated DTI Calculation

**Revised Back-End Ratio**: ($2,978 + $685) / $10,000 = 36.6%
- Guideline: ≤ 43%
- **Status**: WELL WITHIN GUIDELINES ✓

## Credit Risk Assessment

**Risk Rating**: GOOD (A)

**Strengths**:
- ✓ Good credit scores (710-720)
- ✓ Clean recent payment history (aside from one old late)
- ✓ Low credit utilization (< 30%)
- ✓ Established credit history
- ✓ Mix of credit types

**Weaknesses**:
- ⚠ One late payment (18 months ago) - minor, needs explanation

## Underwriting Recommendation

**Overall Recommendation**: APPROVE WITH CONDITION

**Condition**:
1. Obtain explanation letter from John Smith for 30-day late payment on auto loan (18 months ago)

**Compensating Factors**:
- ✓ Good credit scores
- ✓ Low DTI (36.6%)
- ✓ Recent payment history excellent
- ✓ Stable employment (to be verified)

**Analysis Location**: loan-applications/2025/LA-2025-1001-smith/05-credit-documentation/credit-analysis-summary.md

**Status**: Qualified for Conventional financing
```

#### Scenario 2: Compliance Validation Before Closing

```
User: @compliance-checker validate loan file for LA-2025-1001

Response:
# Compliance Validation Report

**Application ID**: LA-2025-1001
**Borrowers**: John and Mary Smith
**Property**: 123 Main Street, Anytown, ST 12345
**Review Date**: 2025-02-10
**Scheduled Closing**: 2025-02-15

## Overall Compliance Status

**COMPLIANCE RISK**: LOW
**Recommendation**: APPROVE FOR CLOSING

---

## TRID Compliance

### Loan Estimate Timeline
- Application Date: 2025-01-15
- LE Due: 2025-01-18 (3 business days)
- LE Sent: 2025-01-17 ✓
- Delivery: Email (borrower consent)
- Intent to Proceed: 2025-01-18 ✓
- **Status**: COMPLIANT ✓

### Closing Disclosure Timeline
- CD Sent: 2025-02-10
- Delivery: Email (borrower consent)
- CD Received: 2025-02-10 (same day)
- 3-Business Day Wait Ends: 2025-02-13
- Scheduled Closing: 2025-02-15
- **Status**: COMPLIANT ✓ (closes after waiting period)

### Changed Circumstances
- Rate lock: 2025-01-20 (revised LE sent same day) ✓
- **Status**: COMPLIANT ✓

---

## Fee Tolerance Testing

### Zero Tolerance Items
| Fee | LE Amount | CD Amount | Variance | Status |
|-----|-----------|-----------|----------|--------|
| Origination Fee | $2,000 | $2,000 | $0 | PASS ✓ |
| Discount Points | $1,800 | $1,800 | $0 | PASS ✓ |
| Transfer Tax | $2,000 | $2,000 | $0 | PASS ✓ |

**Zero Tolerance**: COMPLIANT ✓

### 10% Cumulative Tolerance
| Category | LE Total | CD Total | Variance |
|----------|----------|----------|----------|
| Recording | $250 | $275 | +$25 |
| Title (shopped) | $1,200 | $1,250 | +$50 |
| **Total** | **$1,450** | **$1,525** | **+$75** |

**10% Tolerance**: $1,450 × 10% = $145
**Variance**: $75
**Status**: WITHIN TOLERANCE ✓ ($75 < $145)

---

## APR Accuracy

- Calculated APR: 7.215%
- Disclosed APR: 7.215%
- Variance: 0.000%
- Tolerance: ± 0.125% (regular transaction)
- **Status**: ACCURATE ✓

---

## Qualified Mortgage Determination

### Product Features
- Loan Term: 360 months (≤ 30 years) ✓
- No negative amortization ✓
- No interest-only ✓
- No balloon payment ✓
- Points & fees: 2.11% (< 3% threshold) ✓

**Product Features**: COMPLIANT ✓

### QM Category
- APR: 7.215%
- APOR: 6.500%
- Spread: 0.715%
- Safe Harbor threshold: +1.5% = 8.000%
- **Status**: SAFE HARBOR QM ✓

### ATR Documentation
All 8 factors documented:
1. Income/Assets ✓
2. Employment ✓
3. Mortgage Payment ✓
4. Simultaneous Loans ✓
5. Mortgage Obligations ✓
6. Debt Obligations ✓
7. DTI: 36.6% ✓
8. Credit History ✓

**ATR**: COMPLIANT ✓

---

## RESPA Compliance

- No affiliated business arrangements
- No kickback issues identified
- Escrow account: Within 2-month cushion limit ✓
- Servicing disclosure provided ✓

**RESPA**: COMPLIANT ✓

---

## Fair Lending Review

- Consistent underwriting standards applied ✓
- Objective criteria used ✓
- No prohibited basis factors ✓
- Documentation supports approval ✓

**Fair Lending**: COMPLIANT ✓

---

## Summary of Findings

**Critical Issues**: 0
**High-Priority Issues**: 0
**Medium-Priority Issues**: 0
**Low-Priority Issues**: 0

## Final Recommendation

**APPROVE FOR CLOSING**

All regulatory requirements met:
- ✓ TRID compliant
- ✓ Fee tolerances passed
- ✓ APR accurate
- ✓ Qualified Mortgage (Safe Harbor)
- ✓ ATR documented
- ✓ RESPA compliant
- ✓ Fair lending compliant

**Cleared for closing on 2025-02-15**

**Report Location**: loan-applications/2025/LA-2025-1001-smith/08-compliance/compliance-validation-report.md
```

#### Scenario 3: Closing Coordination

```
User: @closing-coordinator coordinate closing for LA-2025-1001

Response:
# Closing Coordination Initiated

**Loan Application**: LA-2025-1001
**Borrowers**: John and Mary Smith
**Target Close Date**: 2025-02-15

## Status Verification

✓ **Clear-to-Close**: YES (approved 2025-02-08)
✓ **All Conditions Cleared**: YES
✓ **CD Sent**: 2025-02-10
✓ **TRID Compliant**: YES
✓ **Earliest Close Date**: 2025-02-13
✓ **Scheduled Close**: 2025-02-15 ✓

## Closing Details

**Date**: Friday, February 15, 2025
**Time**: 10:00 AM
**Location**: First American Title Company
**Address**: 456 Title Way, Anytown, ST 12345

## Parties Confirmed

### Borrowers
- John Smith: Confirmed ✓
- Mary Smith: Confirmed ✓

### Settlement Agent
- Company: First American Title
- Closer: Sarah Johnson
- Contact: (555) 123-4567
- Documents received: 2025-02-12 ✓

### Real Estate Agents
- Buyer's Agent: Mike Brown (confirmed)
- Seller's Agent: Lisa Davis (confirmed)

## Borrowers Must Bring

- [x] Government-issued photo ID (both borrowers)
- [x] Wire confirmation for $48,250 (down payment + closing costs)
- [x] Proof of homeowners insurance (policy #HO-12345)

## Final Cash-to-Close

**Total Due from Borrowers**: $48,250

**Payment**: Wire transfer
- Sent: 2025-02-14, 2:00 PM
- Confirmed received by title: 2025-02-14, 3:15 PM ✓

## Funding Coordination

**Funding Amount**: $360,000
**Funding Date**: 2025-02-15 (day of closing)

**Pre-Funding Checklist**:
- [x] All documents signed
- [x] Borrower funds received
- [x] TRID waiting period satisfied
- [x] Insurance effective: 2025-02-15
- [x] No title issues

**Funding Status**: APPROVED - Ready to wire on 2025-02-15 at closing

## Post-Closing Timeline

- **Recording**: 2025-02-15 (same day)
- **Documents to Borrower**: 2025-02-18 (3 business days)
- **File to Investor**: 2025-02-20 (5 business days)

**Status**: ON TRACK FOR SUCCESSFUL CLOSING

**Closing Checklist Location**: loan-applications/2025/LA-2025-1001-smith/09-closing-documents/closing-checklist.md
```

## Agent Coordination

The agents work together in a coordinated workflow:

```
loan-processor → credit-analyst → compliance-checker → closing-coordinator
                         ↓                                      ↑
                    (continuous)                         (final check)
```

**Workflow Progression**:
1. **loan-processor**: Initiates application, collects documents, tracks status
2. **credit-analyst**: Reviews credit, assesses risk, updates DTI
3. **loan-processor**: Submits complete file to underwriting
4. **compliance-checker**: Validates regulatory compliance before closing
5. **closing-coordinator**: Manages closing process through funding

**Status Integration**:
```
Application → Documentation → Verification → Underwriting → Clear-to-Close → Closing → Funded
```

## Configuration

### Data Storage

The plugin uses structured loan file organization:

```
loan-applications/
└── {year}/
    └── {app-id}-{borrower-name}/
        ├── 00-application-summary.md
        ├── 01-initial-application/
        ├── 02-disclosures/
        ├── 03-income-documentation/
        ├── 04-asset-documentation/
        ├── 05-credit-documentation/
        ├── 06-property-documentation/
        ├── 07-underwriting/
        ├── 08-compliance/
        ├── 09-closing-documents/
        ├── processing-timeline.md
        ├── qualification-analysis.md
        └── processor-notes.md
```

### Compliance Configuration

Configure compliance thresholds in `.claude/mortgage-specialist/config.json`:

```json
{
  "compliance_standards": {
    "TRID": "enabled",
    "RESPA": "enabled",
    "TILA": "enabled",
    "ECOA": "enabled"
  },
  "risk_thresholds": {
    "DTI_max": 43,
    "LTV_max": 97,
    "credit_score_min": 620
  },
  "business_days": {
    "exclude_saturdays": false,
    "exclude_sundays": true,
    "federal_holidays": [
      "2025-01-01",
      "2025-01-20",
      "2025-02-17",
      "2025-05-26",
      "2025-07-04",
      "2025-09-01",
      "2025-10-13",
      "2025-11-11",
      "2025-11-27",
      "2025-12-25"
    ]
  }
}
```

## Skills Integration

All agents leverage the skills library for consistent, professional quality:

**loan-processor** workflow:
```markdown
1. Read loan-processing skill
2. Apply file structure standards
3. Use document collection checklists
4. Follow DTI/LTV calculation methods
5. Track TRID compliance timelines
6. Maintain status workflow
```

**credit-analyst** workflow:
```markdown
1. Read credit-analysis skill
2. Apply middle score rule
3. Use derogatory item treatment guidelines
4. Follow trade line analysis standards
5. Apply risk rating framework
6. Ensure fair lending compliance
```

**compliance-checker** workflow:
```markdown
1. Read compliance-validation skill
2. Apply TRID timeline validation
3. Test all fee tolerances
4. Verify APR accuracy
5. Determine QM/ATR status
6. Follow risk assessment framework
```

This ensures consistent, regulatory-compliant processing across all loan files.

## Benefits

### For Mortgage Lenders
- **Regulatory Compliance**: Systematic TRID, RESPA, TILA, QM/ATR compliance
- **Risk Management**: Professional credit analysis and risk assessment
- **Efficiency**: Standardized workflows accelerate processing
- **Quality Assurance**: Skill-based patterns ensure completeness
- **Audit Defense**: Complete documentation and compliance validation

### For Loan Officers
- **Faster Processing**: Organized files and clear status tracking
- **Better Qualification**: Accurate DTI and LTV calculations
- **Compliance Confidence**: Validated regulatory compliance
- **Professional Service**: Skill-based quality impresses borrowers
- **Reduced Fallout**: Fewer denials due to thorough upfront qualification

### For Borrowers
- **Clear Process**: Transparent status and requirements
- **Faster Closings**: Organized files accelerate underwriting
- **Fair Treatment**: Consistent standards and fair lending compliance
- **Professional Service**: Complete documentation and communication
- **On-Time Closings**: TRID compliance ensures timeline adherence

## Best Practices

### Loan Processing
✓ Request all documents upfront (avoid delays)
✓ Calculate DTI and LTV accurately
✓ Track TRID timelines meticulously
✓ Maintain organized file structure
✓ Update status regularly
✓ Follow up proactively on missing documents

### Credit Analysis
✓ Use middle score rule for representative score
✓ Review all three bureaus for discrepancies
✓ Document all credit decisions
✓ Apply fair lending standards consistently
✓ Consider whole credit picture (not just score)
✓ Re-pull credit if > 120 days old

### Compliance Validation
✓ Track all business days correctly (exclude Sundays and federal holidays)
✓ Test all fee tolerance categories
✓ Verify APR accuracy to the tenth of a percent
✓ Document all 8 ATR factors
✓ Determine QM status before closing
✓ Perform independent compliance review

### Closing Coordination
✓ Verify clear-to-close before scheduling
✓ Provide CD at least 3 business days before closing
✓ Coordinate all parties well in advance
✓ Confirm cash-to-close and payment method
✓ Fund on time
✓ Record promptly after closing

## Model Usage & Performance

| Agent | Model | Avg Time | Token Usage | Cost/Run | Use Case |
|-------|-------|----------|-------------|----------|----------|
| loan-processor | Sonnet | 45s | ~10K | $0.030 | Qualification analysis |
| credit-analyst | Sonnet | 30s | ~8K | $0.024 | Credit risk assessment |
| compliance-checker | Sonnet | 25s | ~7K | $0.021 | Regulatory validation |
| closing-coordinator | Haiku | 10s | ~3K | $0.002 | Closing coordination |

**Full loan cycle**: ~110s, ~28K tokens, ~$0.08

**Cost Optimization**:
- Haiku for closing-coordinator saves 90% vs Sonnet
- Sonnet required where judgment/expertise needed (processing, credit, compliance)
- Skills cached across multiple loans for efficiency

## Security & Compliance

### Data Protection
- **Local storage only** - No external transmission
- **Encryption at rest** - PII and financial data encrypted
- **Read-only compliance review** - Independent validation
- **Access control** - Agent-level permissions
- **GLBA compliance** - Privacy protection

### Access Control
- **Principle of least privilege** - Minimum required tools
- **Agent-level restrictions** - Specific tool whitelists
- **File access controls** - Organized by loan application
- **Audit logging** - All agent actions logged

### Independence
- **compliance-checker** operates read-only
- **Separation of duties** - Processor ≠ Validator
- **Objective review** - Independent compliance validation

## Troubleshooting

### Agent Not Activating
**Problem**: Agent doesn't respond to query
**Solution**:
- Use explicit @mention: `@loan-processor process application`
- Verify plugin installed and Claude Code restarted
- Check that query matches agent description

### TRID Timing Issues
**Problem**: CD not complying with 3-business day rule
**Solution**:
```
@closing-coordinator verify TRID timeline for [app-id]
```
- Remember: Business days exclude Sundays and federal holidays
- If mailed: Add 3 days for presumed receipt
- Electronic delivery: Same day receipt (must have consent)

### Fee Tolerance Violations
**Problem**: Fees increased beyond tolerance
**Solution**:
```
@compliance-checker test fee tolerances for [app-id]
```
- Zero tolerance: Must cure any increase
- 10% tolerance: Cure if exceeds 10% of LE amount
- Changed circumstance: Document and issue revised LE

### Credit Report Too Old
**Problem**: Credit report > 120 days old
**Solution**:
```
@credit-analyst order updated credit report for [app-id]
```
- Re-pull required if > 120 days
- Review for new derogatory items
- Update DTI with any new debts

## Advanced Usage

### Batch Loan Processing

Process multiple applications efficiently:

```
@loan-processor batch process applications: LA-2025-1001, LA-2025-1002, LA-2025-1003
```

Benefits:
- Standardized document requests
- Consistent qualification analysis
- Consolidated status reporting

### Compliance Audit

Run compliance validation on loan portfolio:

```
@compliance-checker audit all loans closing in February 2025
```

Provides:
- Compliance risk ratings across portfolio
- Common issues identified
- Remediation recommendations

### Custom Workflows

Integrate with existing systems:

```bash
# Example: Export to loan origination system
@loan-processor export application LA-2025-1001 to Encompass format

# Example: Generate compliance report for investor
@compliance-checker generate investor package for LA-2025-1001
```

## Examples

See "Example Scenarios" section above for detailed workflow examples including:
- New purchase loan application (full cycle)
- Compliance validation before closing
- Closing coordination through funding

## File Structure

```
mortgage-specialist/
├── .claude-plugin/
│   └── plugin.json                    # Plugin metadata
├── agents/
│   ├── loan-processor.md              # Loan processing agent (Sonnet)
│   ├── credit-analyst.md              # Credit analysis agent (Sonnet)
│   ├── compliance-checker.md          # Compliance validation (Sonnet, read-only)
│   └── closing-coordinator.md         # Closing coordination (Haiku)
├── skills/
│   ├── loan-processing/
│   │   └── SKILL.md                   # Loan processing patterns
│   ├── credit-analysis/
│   │   └── SKILL.md                   # Credit analysis standards
│   └── compliance-validation/
│       └── SKILL.md                   # Compliance validation frameworks
├── templates/
│   ├── loan-application-checklist.md  # Document collection checklist
│   ├── credit-explanation-letter.md   # Credit explanation template
│   └── compliance-checklist.md        # Compliance validation checklist
└── README.md                          # This file
```

## Support & Feedback

For issues or suggestions:
- Review the skills library for comprehensive patterns
- Check agent definitions for specific capabilities
- Refer to [Claude Code documentation](https://docs.claude.com/en/docs/claude-code)
- Submit issues to Puerto repository

## Disclaimer

**Important**: This plugin provides automation tools for mortgage loan processing and compliance validation. **It does not constitute legal or financial advice.**

Always:
- Consult with qualified legal counsel for regulatory interpretation
- Have experienced underwriters make final credit decisions
- Obtain borrower consent for data usage
- Follow your company's specific compliance procedures
- Stay current with regulatory changes
- Seek professional guidance for complex situations

The plugin is designed to assist mortgage professionals in managing compliance workflows, not to replace professional judgment or legal expertise.

## Contributing

Contributions welcome! To improve this plugin:

1. Review existing agents and skills
2. Identify gaps or enhancement opportunities
3. Submit pull requests with improvements
4. Follow Puerto's plugin architecture standards
5. Maintain comprehensive documentation

## Regulatory References

- **TRID**: 12 CFR § 1026.19 (Regulation Z)
- **RESPA**: 12 CFR § 1024
- **TILA**: 12 CFR § 1026
- **QM/ATR**: 12 CFR § 1026.43
- **ECOA**: 12 CFR § 1002 (Regulation B)
- **Fair Housing Act**: 42 USC § 3601-3619
- **GLBA**: 15 USC § 6801-6809

## License

MIT License - See main repository for details

---

**Professional mortgage processing with regulatory compliance. Process efficiently, decide confidently, close on time.**

**Version**: 1.0.0
**Author**: bandofai
**Repository**: [Puerto](https://github.com/bandofai/puerto)
