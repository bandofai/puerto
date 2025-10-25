# Compliance Validation Skill

Professional frameworks and methodologies for validating tax filing packages against regulatory requirements, identifying compliance gaps, and providing actionable remediation guidance.

## Purpose

This skill provides standardized frameworks for:
- Comprehensive compliance validation
- Risk assessment and prioritization
- Finding classification and reporting
- Remediation guidance
- Regulatory citation standards
- Quality assurance procedures

## Core Concepts

### 1. Three-Tier Validation Framework

All filing packages must undergo three-tier validation:

#### Tier 1: Completeness Validation
Verify all required components are present:

```markdown
## Primary Form Completeness
- [ ] All pages included (no missing pages)
- [ ] All required fields completed (no blanks)
- [ ] Entity information complete (name, EIN, address)
- [ ] Tax period correctly stated
- [ ] All required signatures obtained
- [ ] Filing method indicated

## Schedule Completeness
For each required schedule:
- [ ] Schedule present in filing package
- [ ] All sections of schedule completed
- [ ] Schedule properly labeled and referenced

## Supporting Documentation
- [ ] All W-2s attached/available
- [ ] All 1099s attached/available
- [ ] Required supporting statements prepared
- [ ] Source documentation organized

## Filing Materials
- [ ] Payment voucher (if balance due)
- [ ] Extension documentation (if applicable)
- [ ] Prior year return for comparison
- [ ] State conformity documentation
```

#### Tier 2: Accuracy Validation
Verify calculations and cross-references:

```markdown
## Mathematical Accuracy
- [ ] All additions/subtractions correct
- [ ] All multiplications/divisions correct
- [ ] All percentages calculated correctly
- [ ] Tax table/rate lookups accurate

## Cross-Reference Accuracy
- [ ] Schedule amounts tie to primary form
- [ ] Related forms cross-reference correctly
- [ ] Prior year carryforwards accurate
- [ ] Multi-page totals carry forward correctly

## Source Document Tie-Out
- [ ] Income items tie to books/records
- [ ] Deductions tie to source documents
- [ ] Balance sheet ties to financials
- [ ] Reconciliation (M-1) balances

## Reasonability Assessment
- [ ] Compare to prior year (variance analysis)
- [ ] Compare to industry benchmarks (if available)
- [ ] Assess significant changes for explanation
- [ ] Verify consistency in treatment
```

#### Tier 3: Regulatory Compliance
Verify adherence to regulations:

```markdown
## Substantive Requirements
- [ ] Filing under correct form type
- [ ] Correct filing status (if applicable)
- [ ] Proper accounting method applied
- [ ] Depreciation methods compliant
- [ ] Deduction limitations applied (meals, entertainment, etc.)
- [ ] Income recognition rules followed

## Disclosure Requirements
- [ ] All required questions answered
- [ ] Related party transactions disclosed
- [ ] Foreign accounts disclosed (FBAR)
- [ ] Uncertain tax positions assessed
- [ ] Elections properly made and documented

## Procedural Requirements
- [ ] Proper signatures obtained
- [ ] Preparer information complete (PTIN)
- [ ] Required attachments included
- [ ] Appropriate filing method used
- [ ] Payment properly documented
```

### 2. Risk Classification Matrix

Classify all findings by risk level:

#### Critical Risk
**Definition**: Issues that will cause rejection or significant penalties

**Characteristics**:
- Form rejection highly likely
- Penalties >$1,000
- Criminal implications possible
- Must be fixed before filing

**Examples**:
- Missing required forms (Form 4562 when depreciation claimed)
- Unsigned return
- Missing payment voucher with balance due
- EIN mismatch with IRS records
- Math errors in tax calculation

**Response Time**: IMMEDIATE (same day)

---

#### High Risk
**Definition**: Compliance violations with significant consequences

**Characteristics**:
- Penalties $100-$1,000
- Audit risk elevation
- Regulatory non-compliance
- Should be fixed before filing

**Examples**:
- Foreign account question unanswered
- Missing preparer PTIN
- Related party transactions not disclosed
- Required schedules incomplete
- Material misclassification of income/deductions

**Response Time**: URGENT (within 24-48 hours)

---

#### Medium Risk
**Definition**: Documentation gaps or procedural issues

**Characteristics**:
- Penalties <$100 or none
- Audit defense difficulties
- Professional quality concerns
- Recommended to fix

**Examples**:
- Missing supporting statements for "other" categories
- Incomplete documentation
- Prior year inconsistencies without explanation
- Missing schedule attachments (not required but helpful)
- Uncertain tax position assessment needed

**Response Time**: RECOMMENDED (before filing)

---

#### Low Risk
**Definition**: Quality enhancements, no compliance impact

**Characteristics**:
- No penalties
- No regulatory violation
- Best practice improvements
- Optional to fix

**Examples**:
- Documentation organization
- File naming consistency
- Additional explanatory notes
- Enhanced audit trail
- Minor formatting improvements

**Response Time**: OPTIONAL (nice to have)

---

### 3. Finding Classification Standards

Use consistent finding structure:

```markdown
## Finding Template

### [Number]. [Short Title]
**Priority**: CRITICAL | HIGH | MEDIUM | LOW
**Category**: Completeness | Accuracy | Regulatory Compliance
**Location**: [Specific form, line, schedule]

**Issue**:
[Clear description of what is wrong or missing]

**Regulatory Citation**:
[IRC section, Treasury Regulation, Form Instructions]

**Impact**:
[Specific consequences if not corrected]
- Bullet list of impacts
- Include penalties, risks, compliance issues

**Remediation**:
[Step-by-step instructions to fix]
1. Numbered steps
2. Specific actions required
3. Resources needed

**Timeline**: [IMMEDIATE | URGENT | RECOMMENDED | OPTIONAL]

**Status**: OPEN | IN PROGRESS | RESOLVED
```

**Example Finding**:

```markdown
### 1. Missing Form 4562 (Depreciation)
**Priority**: CRITICAL
**Category**: Completeness / Regulatory
**Location**: Form 1120, Line 20 references $45,000 depreciation

**Issue**:
Form 4562 is required when depreciation is claimed but is not attached to the filing package. IRS will reject return without this form.

**Regulatory Citation**:
IRC §167, Treas. Reg. §1.167(a)-1, Form 1120 Instructions (Line 20)

**Impact**:
- Return will be rejected by IRS e-file system
- Filing deadline may be missed due to rejection
- Late filing penalties: $435/month (for corporations)
- Penalty up to $270 for missing forms
- Depreciation deduction may be disallowed without substantiation

**Remediation**:
1. Prepare Form 4562 showing all depreciation calculations
2. Include:
   - Section 179 expense election (if any)
   - MACRS depreciation by asset class
   - Listed property depreciation (if any)
   - Amortization (if any)
3. Verify Form 4562 total ties to Form 1120, Line 20 ($45,000)
4. Attach to filing package as document 09-form-4562-depreciation.pdf
5. Re-submit entire package for compliance review

**Timeline**: IMMEDIATE - must be completed before filing

**Status**: OPEN
```

### 4. Jurisdiction-Specific Compliance Frameworks

#### Federal (IRS) Compliance Checklist

**Form 1120 (C-Corporation)**:

```markdown
## Income Section Compliance
- [ ] Gross receipts properly sourced (not inflated/deflated)
- [ ] Returns/allowances reasonable
- [ ] COGS inventory method consistent with prior year
- [ ] Dividend income properly classified (Schedule C)
- [ ] Capital gains/losses properly reported (Schedule D)
- [ ] No constructive dividends misclassified as expenses

## Deduction Section Compliance
- [ ] Officer compensation reasonable (IRS scrutiny area)
- [ ] Meals/entertainment limited to 50%
- [ ] Travel substantiation adequate
- [ ] Auto expenses substantiated (mileage logs)
- [ ] Charitable contributions within 10% limitation
- [ ] Depreciation using proper method and life
- [ ] No personal expenses deducted
- [ ] Related party transactions at arm's length

## Schedule K Compliance (Other Information)
- [ ] Line 1: Accounting method properly stated
- [ ] Line 2: Business activity code correct (NAICS)
- [ ] Line 3: Product/service accurately described
- [ ] Line 4: Ownership of other entities disclosed
- [ ] Line 14a: Foreign financial accounts question answered
- [ ] Line 14b: Foreign trusts question answered
- [ ] Line 19: IRC §465 at-risk answered
- [ ] Line 20: IRC §1244 stock election indicated

## Critical Disclosures
- [ ] Related party transactions (Schedule K, various lines)
- [ ] Foreign accounts (FBAR requirement if >$10,000)
- [ ] Foreign entities ownership (Form 5471/8865 if applicable)
- [ ] Uncertain tax positions (Schedule UTP if assets ≥$10M)
- [ ] Reportable transactions (Form 8886 if applicable)

## Special Situations
- [ ] NOL carryforward properly calculated and applied
- [ ] IRC §382 limitations assessed (if ownership change)
- [ ] Passive activity limitations (if applicable)
- [ ] At-risk limitations (if applicable)
- [ ] Excess business loss limitation (if applicable)
```

**Form 1040 (Individual)**:

```markdown
## Filing Status Compliance
- [ ] Correct filing status selected
- [ ] Married filing separately implications considered
- [ ] Head of household qualification verified (>50% support, qualifying person)
- [ ] Qualifying widow(er) status verified (within 2 years of spouse death)

## Dependent Compliance
- [ ] All dependents qualify under IRC §152
- [ ] SSNs provided for all dependents
- [ ] Dependent ages verified
- [ ] Support test met (>50% support provided)
- [ ] Residency test met (>6 months)
- [ ] No dependent claimed on multiple returns

## Income Compliance
- [ ] All W-2 income reported
- [ ] All 1099 income reported
- [ ] Cryptocurrency transactions reported
- [ ] Foreign income reported (worldwide income)
- [ ] State tax refunds properly included (if itemized prior year)
- [ ] Social Security benefits taxation calculated correctly

## Deduction Compliance
- [ ] Standard vs itemized analysis performed (take greater)
- [ ] Itemized deductions properly substantiated
- [ ] Medical expenses exceed 7.5% AGI threshold
- [ ] SALT deduction limited to $10,000
- [ ] Mortgage interest properly allocated (acquisition/home equity)
- [ ] Charitable contributions substantiated (>$250 requires acknowledgment)

## Tax Credit Compliance
- [ ] Earned Income Tax Credit eligibility verified
- [ ] Child Tax Credit eligibility verified (age, residency, support)
- [ ] Education credits verified (Form 1098-T, qualified expenses)
- [ ] Energy credits properly claimed (qualified improvements)
- [ ] Credits not duplicated (e.g., same expense for multiple credits)

## Critical Disclosures
- [ ] Foreign financial accounts (FBAR if >$10,000 aggregate)
- [ ] Foreign financial assets (Form 8938 if thresholds met)
- [ ] Foreign trusts (Form 3520/3520-A)
- [ ] Cryptocurrency transactions (Schedule 1 question answered)
- [ ] Presidential Election Campaign Fund preference
```

**Form 1065 (Partnership)**:

```markdown
## Partnership-Specific Compliance
- [ ] Partnership agreement reviewed for allocation rules
- [ ] Partner capital accounts properly tracked
- [ ] Capital account method indicated (tax, GAAP, 704(b), other)
- [ ] Allocation substantial economic effect test met (IRC §704(b))
- [ ] No special allocations without proper documentation
- [ ] Built-in gain/loss allocation (if contributed property)

## Schedule K-1 Compliance
- [ ] K-1 prepared for each partner
- [ ] Partner identifying information complete (SSN/EIN)
- [ ] Profit/loss/capital percentages correct
- [ ] Beginning and ending capital accounts accurate
- [ ] Partner basis adequate for losses (outside basis check)
- [ ] At-risk and passive activity limitations noted

## Partnership Allocations
- [ ] Income/loss allocated per partnership agreement
- [ ] Special allocations have substantial economic effect
- [ ] Section 704(c) allocations proper (contributed property)
- [ ] Section 743(b) adjustments calculated (if election made)
- [ ] Section 754 election considered (step-up/step-down)

## Critical Disclosures
- [ ] Related party transactions disclosed
- [ ] Foreign partners identified
- [ ] Foreign operations disclosed (Form 8865 if controlled foreign partnership)
- [ ] Uncertain tax positions (Schedule UTP if applicable)
```

#### State Compliance Considerations

**California (Form 100)**:

```markdown
## CA-Specific Adjustments
- [ ] CA-federal income differences identified
- [ ] Depreciation differences (if CA differs from federal)
- [ ] Interest income differences (municipal bonds)
- [ ] NOL differences (CA has different rules)
- [ ] IRC §179 expense differences (CA limits differ)

## Apportionment Compliance
- [ ] Single-sales factor formula applied (CA uses sales only)
- [ ] Sales assigned to CA if customer located in CA
- [ ] Throwback rule considered (if applicable)
- [ ] Market assignment properly determined

## CA-Specific Requirements
- [ ] Water's-edge election (if foreign operations)
- [ ] Unitary group determination (if affiliated entities)
- [ ] Minimum franchise tax paid ($800)
- [ ] E-file requirement met (generally required)
```

**New York (Form CT-3)**:

```markdown
## NY-Specific Adjustments
- [ ] Federal taxable income starting point
- [ ] NY addbacks/subtractions properly applied
- [ ] Depreciation differences accounted for
- [ ] Interest income differences (municipal bonds)

## Apportionment Compliance
- [ ] Business allocation percentage calculated
- [ ] Investment allocation percentage calculated
- [ ] Property/payroll/sales factors properly computed
- [ ] Sales factor double-weighted (PPSS formula)

## NY-Specific Requirements
- [ ] Metropolitan Commuter Transportation Mobility Tax (if NYC)
- [ ] Minimum tax calculation ($25 or actual, whichever greater)
- [ ] Article 9-A requirements (most corporations)
```

### 5. Prior Year Comparison Framework

Always compare to prior year and explain material changes:

```markdown
## Prior Year Comparison Analysis

### Variance Threshold
Material variance: ±20% AND ±$10,000 (whichever is less restrictive)

### Income Items Comparison

| Item | Prior Year | Current Year | Change | Variance % | Material? |
|------|-----------|--------------|--------|------------|-----------|
| Gross receipts | $1,100,000 | $1,250,000 | +$150,000 | +13.6% | No |
| COGS | $400,000 | $450,000 | +$50,000 | +12.5% | No |
| Gross profit | $700,000 | $800,000 | +$100,000 | +14.3% | **Yes** |
| Other income | $5,000 | $25,000 | +$20,000 | +400% | **Yes** |

### Deduction Items Comparison

| Item | Prior Year | Current Year | Change | Variance % | Material? |
|------|-----------|--------------|--------|------------|-----------|
| Officer comp | $300,000 | $320,000 | +$20,000 | +6.7% | No |
| Rent | $48,000 | $52,000 | +$4,000 | +8.3% | No |
| Depreciation | $50,000 | $45,000 | -$5,000 | -10% | **Yes** |
| Professional fees | $10,000 | $25,000 | +$15,000 | +150% | **Yes** |

### Material Variances - Explanations Required

**Gross Profit Increase (+$100,000, +14.3%)**
Explanation: Business expansion and new product line introduction in Q2 2024 increased sales volume. Gross margin improved due to favorable vendor pricing.
Documentation: Sales reports, vendor contracts
Assessment: Reasonable, well-documented ✓

**Other Income Increase (+$20,000, +400%)**
Explanation: One-time sale of equipment (Form 4797), gain of $18,000
Documentation: Form 4797, sale agreement, asset records
Assessment: Reasonable, properly reported ✓

**Depreciation Decrease (-$5,000, -10%)**
Explanation: Fewer asset acquisitions in 2024 compared to 2023. Some assets became fully depreciated during year.
Documentation: Depreciation schedule showing fully depreciated assets
Assessment: Reasonable ✓

**Professional Fees Increase (+$15,000, +150%)**
Explanation: Legal fees for lease negotiation ($8,000) and contract dispute resolution ($7,000)
Documentation: Legal invoices, case documentation
Assessment: Reasonable, properly substantiated ✓

### Tax Computation Comparison

| Item | Prior Year | Current Year | Change | Variance % |
|------|-----------|--------------|--------|------------|
| Taxable income | $55,000 | $60,000 | +$5,000 | +9.1% |
| Tax rate | 21% | 21% | - | - |
| Tax liability | $11,550 | $12,600 | +$1,050 | +9.1% |
| Effective rate | 10.5% | 10.1% | -0.4% | - |

**Assessment**: Effective tax rate consistent, slight decrease due to proportional income mix changes. Reasonable ✓

### Red Flags to Investigate

Common red flag patterns:
- [ ] Gross receipts decrease but expenses increase significantly
- [ ] Unusually high officer compensation relative to profit
- [ ] Meals/entertainment disproportionate to business size
- [ ] Travel expenses excessive
- [ ] Home office deduction without proper substantiation
- [ ] Auto expenses without mileage logs
- [ ] Large "other" categories without supporting statements
- [ ] Sudden changes in accounting method
- [ ] Loss years followed by sale of assets
- [ ] Consistent losses without exit strategy

**Red Flags in This Return**: None identified ✓
```

### 6. Common Violation Patterns

Be alert for these common compliance violations:

#### Income Reporting Violations

```markdown
## Unreported Income
- Cash receipts not deposited/reported
- Cryptocurrency transactions omitted
- Barter transactions not valued/reported
- Cancelled debt not reported as income
- State tax refunds not reported (if itemized prior year)

## Income Misclassification
- Capital gains reported as ordinary income (or vice versa)
- Dividend income classified as return of capital improperly
- Compensation misclassified as distributions (S-corps)
- Guaranteed payments misclassified (partnerships)
```

#### Deduction Violations

```markdown
## Non-Deductible Expenses Claimed
- Personal expenses deducted
- Traffic tickets/penalties
- Political contributions
- Life insurance premiums (if corp is beneficiary)
- Lobbying expenses
- Club dues (country club, etc.)
- Commuting expenses

## Improperly Claimed Deductions
- Meals/entertainment not limited to 50%
- Auto expenses without substantiation
- Home office not meeting exclusive-use test
- Charitable contributions without substantiation
- Travel without business purpose
- Education not maintaining/improving skills

## Timing Violations
- Cash basis taxpayer deducting prepaid expenses
- Accrual basis inconsistent application
- Depreciation claimed in wrong year
- Election to capitalize vs expense made incorrectly
```

#### Disclosure Violations

```markdown
## Missing Disclosures
- Foreign financial accounts (FBAR threshold $10,000)
- Foreign entities ownership (Form 5471/8865)
- Related party transactions
- Uncertain tax positions (Schedule UTP)
- Reportable transactions (Form 8886)
- Cryptocurrency holdings/transactions

## Incomplete Disclosures
- Schedule K questions left blank
- Partial responses to yes/no questions
- Missing supporting schedules referenced
- Unsigned forms
- Missing preparer information
```

### 7. Remediation Guidance Standards

Provide specific, actionable remediation steps:

**Remediation Template**:

```markdown
## Remediation Steps for [Issue]

### Immediate Actions (Today)
1. [First specific action]
   - Who: [Responsible party]
   - What: [Exact task]
   - Resources needed: [Documents, information, tools]

2. [Second action]
   [...]

### Short-term Actions (This Week)
3. [Next action]
   [...]

### Validation
4. After completing remediation:
   - [ ] Verify issue fully resolved
   - [ ] Check for related issues
   - [ ] Update audit trail
   - [ ] Re-submit for compliance review

### Prevention
5. For future filings:
   - [ ] Update procedures to prevent recurrence
   - [ ] Add checklist item for this issue
   - [ ] Document lessons learned
```

**Example Remediation**:

```markdown
## Remediation Steps for Missing Form 4562

### Immediate Actions (Today)
1. Gather depreciation data
   - Who: Preparer + Accounting
   - What: Collect all fixed asset records for 2024
   - Resources needed:
     - Fixed asset register
     - Prior year Form 4562
     - Purchase invoices for new assets
     - Sale documents for disposed assets

2. Prepare Form 4562
   - Who: Preparer
   - What: Complete all sections:
     - Part I: Section 179 expense (if any)
     - Part II: Special depreciation allowance
     - Part III: MACRS depreciation
     - Part IV: Summary
     - Part V: Listed property (if any)
     - Part VI: Amortization (if any)
   - Resources needed: IRS Form 4562 instructions

### Short-term Actions (This Week)
3. Verify tie-out to Form 1120
   - Who: Preparer
   - What: Confirm Form 4562 total equals Form 1120, Line 20 ($45,000)
   - If not equal: Investigate and reconcile difference

4. Quality check
   - Who: Reviewer
   - What:
     - Verify all assets included
     - Check depreciation methods and lives
     - Confirm calculations accurate
     - Ensure proper categorization

### Validation
5. After completing Form 4562:
   - [ ] Form 4562 total = $45,000 (ties to Form 1120, Line 20)
   - [ ] All depreciable assets included
   - [ ] Calculations verified
   - [ ] Attached to filing package as 09-form-4562-depreciation.pdf
   - [ ] Update validation checklist
   - [ ] Update audit trail
   - [ ] Re-submit entire package to @compliance-checker

### Prevention
6. For future filings:
   - [ ] Add "Form 4562 required?" to initial scope checklist
   - [ ] Trigger Form 4562 prep when any depreciation claimed
   - [ ] Include Form 4562 in validation checklist
   - [ ] Document in procedures manual
```

## Best Practices Summary

✓ Apply three-tier validation framework (completeness, accuracy, compliance)
✓ Classify all findings by risk level (Critical/High/Medium/Low)
✓ Use consistent finding format with regulatory citations
✓ Provide specific, actionable remediation guidance
✓ Compare to prior year and explain material variances
✓ Watch for common violation patterns
✓ Maintain read-only independence (don't modify files under review)
✓ Document all findings with clear impact assessment
✓ Set appropriate timelines based on risk
✓ Re-validate after remediation before final approval

## Common Validation Pitfalls to Avoid

✗ Focusing only on completeness, ignoring accuracy/compliance
✗ Vague findings without specific remediation steps
✗ Missing regulatory citations
✗ Inconsistent risk classification
✗ Not comparing to prior year
✗ Approving filing with critical issues outstanding
✗ Modifying files during review (breaks independence)
✗ Generic checklists not specific to form type
✗ No follow-up to verify issues resolved
✗ Inadequate impact assessment

---

**This skill ensures thorough, professional, risk-based compliance validation that prevents costly errors, penalties, and audit issues.**
