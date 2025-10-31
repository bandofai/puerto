# Filing Preparation Skill

Professional standards and methodologies for preparing complete, accurate tax filing packages with proper documentation, validation, and audit trail maintenance.

## Purpose

This skill provides standardized frameworks for:
- Document assembly workflows
- Filing package structure and organization
- Form completion standards
- Schedule preparation requirements
- Quality assurance procedures
- Audit trail documentation

## Core Concepts

### 1. Filing Package Structure

Every filing package should follow a standardized structure:

```
filings/
└── {year}/
    └── {jurisdiction}-{form}-{entity}/
        ├── 00-filing-summary.md
        ├── 01-primary-form.pdf
        ├── 02-schedule-*.pdf
        ├── 03-supporting-forms.pdf
        ├── 04-information-returns.pdf
        ├── 05-prior-year-comparison.pdf
        ├── 06-supporting-statements.pdf
        ├── validation-checklist.md
        ├── audit-trail.md
        ├── compliance-report.md (after review)
        └── source-documents/
            ├── financial-statements.pdf
            ├── general-ledger.xlsx
            ├── w2-forms.pdf
            └── 1099-forms.pdf
```

**Naming Conventions**:
- Consistent numbering for filing order
- Descriptive names indicating content
- Entity and year identification in folder name
- Clear separation of final filing vs. source documents

### 2. Document Assembly Workflow

Follow systematic document gathering process:

#### Phase 1: Scope Definition (15 minutes)

```markdown
# Filing Package Initiation

**Date**: {date}
**Preparer**: {name}
**Form**: {form number and description}
**Entity**: {entity name, EIN}
**Tax Period**: {year/quarter}
**Due Date**: {date}
**Extension**: {yes/no, if yes new date}

## Objectives
- Primary form: {form number}
- Required schedules: {list}
- Estimated complexity: {simple/moderate/complex}
- Estimated preparation time: {hours}

## Skill Reference
Following filing-preparation skill patterns:
Location: plugins/tax-compliance/skills/filing-preparation/SKILL.md
```

#### Phase 2: Documentation Gathering (30-60 minutes)

Use comprehensive gathering checklist:

**Financial Documents**:
- [ ] Prior year tax return (complete package)
- [ ] Current year financial statements (audited if available)
  - [ ] Balance sheet (beginning and ending)
  - [ ] Income statement (full year)
  - [ ] Cash flow statement
  - [ ] Statement of changes in equity
- [ ] General ledger (full year, all accounts)
- [ ] Trial balance (beginning, ending, activity)
- [ ] Depreciation schedule with current year activity
- [ ] Amortization schedule (if applicable)

**Supporting Records**:
- [ ] Bank statements (all accounts, 12 months)
- [ ] Investment account statements (year-end)
- [ ] Loan documents and amortization schedules
- [ ] Property records (purchases, sales, improvements)
- [ ] Legal documents (formation, amendments, agreements)

**Information Returns**:
- [ ] W-2s (all employees)
- [ ] 1099-NEC (nonemployee compensation issued/received)
- [ ] 1099-INT (interest income)
- [ ] 1099-DIV (dividend income)
- [ ] 1099-B (brokerage transactions)
- [ ] 1099-MISC (miscellaneous income)
- [ ] K-1s (partnership/S-corp income received)
- [ ] W-9s (for issuing 1099s)

**Deduction Documentation**:
- [ ] Receipts for major deductions (>$1,000)
- [ ] Mileage logs (if claiming auto expense)
- [ ] Home office calculations (if applicable)
- [ ] Charitable contribution acknowledgments
- [ ] Medical expense records (individuals)
- [ ] Education expense records (individuals)
- [ ] Dependent information (SSNs, dates of birth)

**Entity-Specific Documents**:
- [ ] Shareholder/partner basis calculations
- [ ] Distribution records
- [ ] Capital contribution records
- [ ] Ownership percentage documentation
- [ ] Related party transaction documentation

**Jurisdiction-Specific Documents**:
- [ ] State/local apportionment data
- [ ] Sales/use tax records
- [ ] Property tax assessments
- [ ] Nexus documentation

#### Phase 3: Form Preparation (2-8 hours depending on complexity)

**Primary Form Completion**:

Follow jurisdiction-specific instructions carefully:

**Federal Form 1120 (C-Corporation)**:

```markdown
## Page 1: Income Section

### Lines 1a-1c: Gross Receipts
- Source: Income statement, GL account 4000-4999
- Verification: Tie to sales journal, 1099-K if applicable
- Returns/Allowances: GL account 4900-4990

### Line 2: Cost of Goods Sold
- Reference: Schedule A (must complete separately)
- Source: GL accounts 5000-5999
- Verification: Inventory reconciliation required

### Line 3: Gross Profit
- Calculation: Line 1c minus Line 2
- Reasonability: Compare to prior year, industry benchmarks

### Lines 4-10: Other Income
- Line 4: Dividends (Schedule C required)
- Line 5: Interest (bank statements, 1099-INT)
- Line 6: Gross rents (if property held)
- Line 7: Gross royalties (if IP licensing)
- Line 8: Capital gains (Schedule D if applicable)
- Line 9: Net gain (Form 4797 if asset sales)
- Line 10: Other (statement required if >$10,000)

### Line 11: Total Income
- Calculation: Sum of lines 3-10
- Cross-check: Tie to book income reconciliation

## Page 1: Deduction Section

### Line 12: Officer Compensation
- Source: W-2s for officers
- Requirement: Reasonable compensation test
- Documentation: Board minutes approving compensation

### Line 13: Salaries and Wages
- Source: Payroll records, exclude officers
- Verification: Tie to 941 filings
- Cross-check: W-2 total minus officers

### Lines 14-26: Operating Deductions
Each deduction requires:
- Clear source document reference
- Reasonability check vs. prior year
- Documentation adequacy verification
- Proper classification (no mixed categories)

### Line 27: Total Deductions
- Calculation: Sum of lines 12-26
- Cross-check: Tie to book expense reconciliation

### Line 28: Taxable Income Before NOL
- Calculation: Line 11 minus Line 27
- Cross-check: Tie to Schedule M-1 bottom line

### Lines 29a-29b: Net Operating Loss
- Source: Prior year returns with NOL carryforward
- Documentation: NOL calculation worksheet
- Limitation: Check for IRC Section 382 limitations

### Line 30: Taxable Income
- Calculation: Line 28 minus Line 29c

## Pages 2-3: Tax and Credits

### Schedule J: Tax Computation
- Graduated rates or flat rate (21% for corporations)
- Alternative minimum tax (if applicable)
- Credits (R&D, energy, etc.)
- Prior year minimum tax credit

### Line 31: Total Tax
- Source: Schedule J
- Verification: Tax table/rate calculation

### Line 32: Total Payments
- Estimated tax payments (Form 1120-W)
- Prior year overpayment applied
- Withholding (if any)
- Documentation: Payment confirmations, bank records

### Line 33: Refund or Amount Owed
- Calculation: Line 32 minus Line 31
- Action: If balance due, prepare Form 1120-V (payment voucher)
```

**Supporting Schedules**:

Each form has required schedules. Complete all schedules before finalizing primary form:

**Schedule A: Cost of Goods Sold**
```markdown
## Inventory Method
- [ ] FIFO (First In, First Out)
- [ ] LIFO (Last In, First Out)
- [ ] Average Cost
- [ ] Specific Identification

## Components
1. Beginning inventory (must tie to prior year ending)
2. Purchases during year
3. Cost of labor
4. Additional IRC 263A costs
5. Other costs
6. Ending inventory (physical count verification)

## Calculation
Beginning inventory
+ Purchases
+ Labor
+ Additional Section 263A costs
+ Other costs
- Ending inventory
= Cost of Goods Sold (to Form 1120, Line 2)

## Verification
- [ ] Beginning = prior year ending
- [ ] Ending supported by physical count
- [ ] Method consistent with prior year
- [ ] Section 263A properly applied
```

**Schedule M-1: Reconciliation of Income (Book-Tax)**
```markdown
## Purpose
Reconcile net income per books to taxable income per return

## Left Side (Additions to book income)
- Federal income tax expense
- Excess capital losses over capital gains
- Income subject to tax not recorded on books
- Expenses recorded on books not deducted on return:
  - Depreciation (if book differs from tax)
  - Charitable contributions (subject to limitations)
  - Travel and entertainment (50% limitation)
  - Meals (50% limitation)
  - Life insurance premiums (officer-insured)
  - Penalties and fines
  - Political contributions

## Right Side (Subtractions from book income)
- Income recorded on books not included on return:
  - Tax-exempt interest
  - Life insurance proceeds
- Deductions on return not charged against books:
  - Depreciation (if tax exceeds book)

## Bottom Line
Must equal Form 1120, Line 28 (taxable income before NOL)

## Quality Check
- [ ] All book-tax differences identified
- [ ] Material items properly classified
- [ ] Permanent vs temporary differences documented
- [ ] Reconciliation balances to return
```

**Schedule M-2: Analysis of Retained Earnings**
```markdown
## Components

### Beginning Balance
Source: Prior year Schedule M-2, ending balance

### Additions
- Net income per books (from Schedule M-1)
- Other increases (capital contributions, etc.)

### Deductions
- Distributions to shareholders
- Other decreases

### Ending Balance
Calculation: Beginning + Additions - Deductions
Cross-check: Must tie to Schedule L (balance sheet) retained earnings

## Verification
- [ ] Beginning ties to prior year
- [ ] Net income ties to Schedule M-1
- [ ] Distributions documented (board minutes, cancelled checks)
- [ ] Ending ties to Schedule L
```

**Schedule L: Balance Sheet**
```markdown
## Structure
Two columns: Beginning of year, End of year

## Assets
- Cash
- Trade receivables (net of allowance)
- Inventory
- Other current assets
- Loans to shareholders
- Mortgage and real estate loans payable
- Buildings and other depreciable assets (net)
- Depletable assets (net)
- Land
- Intangible assets (net of amortization)
- Other assets

## Liabilities
- Accounts payable
- Mortgages, notes, bonds payable (< 1 year)
- Other current liabilities
- Loans from shareholders
- Mortgages, notes, bonds payable (≥ 1 year)
- Other liabilities

## Shareholders' Equity
- Capital stock
- Additional paid-in capital
- Retained earnings (tie to Schedule M-2)
- Adjustments to shareholders' equity
- Less: Treasury stock

## Verification
- [ ] Beginning balances tie to prior year ending
- [ ] Assets = Liabilities + Equity (must balance!)
- [ ] Retained earnings tie to Schedule M-2
- [ ] Material changes from prior year explained
- [ ] Consistent with filed financial statements
```

**Schedule K: Other Information**
```markdown
## Key Questions
Complete all required questions:

1. Accounting method: Cash, Accrual, Other
2. Business activity code (6-digit NAICS)
3. Product or service
4. At the end of the tax year, did the corporation:
   a. Own directly 20% or more of voting stock?
   b. Own directly 50% or more of voting stock?
5. Ownership percentage disclosure
6. Foreign financial accounts (FBAR question)
7. Ownership of foreign entities
8. Section 465 at-risk
9. Section 1244 stock election
10. Consolidated return election
... [continues for all Schedule K questions]

## Critical Questions
Pay special attention to:
- Foreign account question (FBAR compliance)
- Related party transactions
- Ownership changes (IRC 382 implications)
- Uncertain tax positions (Schedule UTP may be required)
```

#### Phase 4: Quality Assurance (30-60 minutes)

**Pre-Review Checklist**:

```markdown
# Filing Package Quality Assurance

## Completeness Check
- [ ] All required forms included
- [ ] All required schedules included
- [ ] All supporting statements prepared
- [ ] All cross-references accurate

## Accuracy Verification
- [ ] All calculations verified
- [ ] All amounts tie to source documents
- [ ] All cross-references tie between forms
- [ ] Prior year comparison reasonable

## Compliance Review
- [ ] All required fields completed
- [ ] All required questions answered
- [ ] Proper signatures obtained (or ready)
- [ ] Filing method determined (e-file or paper)

## Documentation
- [ ] Source documents organized
- [ ] Documentation index prepared
- [ ] Audit trail completed
- [ ] Preparer notes documented

## Ready for Validation
- [ ] Package complete
- [ ] Validation checklist prepared
- [ ] Ready for @compliance-checker
```

### 3. Form-Specific Standards

#### Federal Form 1040 (Individual)

Key considerations:
- Filing status determination (single, MFJ, MFS, HOH, QW)
- Dependent qualification and documentation
- Standard vs itemized deduction analysis
- Tax credits evaluation (EITC, CTC, education, energy)
- Estimated tax payment requirements
- State residency issues

#### Federal Form 1120-S (S-Corporation)

Key considerations:
- Shareholder basis calculations (critical!)
- Built-in gains tax (if applicable)
- Excess net passive income tax (if applicable)
- Schedule K-1 preparation for each shareholder
- AAA (Accumulated Adjustments Account) tracking
- Shareholder loan basis tracking

#### Federal Form 1065 (Partnership)

Key considerations:
- Partner basis calculations (outside and inside)
- Section 743(b) adjustments (if election made)
- Section 754 election considerations
- Schedule K-1 preparation for each partner
- Capital account tracking (tax vs GAAP vs 704(b))
- Guaranteed payments to partners

### 4. Multi-Jurisdiction Preparation

**Coordinated Filing Strategy**:

When entity files in multiple jurisdictions:

```markdown
## Filing Coordination: Acme Corporation

### Federal (Primary)
1. Complete federal Form 1120 first
2. Establish base taxable income
3. Document all book-tax adjustments

### State (Secondary)
4. California Form 100:
   - Start with federal taxable income
   - Apply CA-specific adjustments
   - Calculate apportionment (sales, property, payroll)
   - Apply CA tax rate

5. New York Form CT-3:
   - Start with federal taxable income
   - Apply NY-specific adjustments
   - Calculate apportionment (different from CA)
   - Apply NY tax rate

### Local (Tertiary)
6. San Francisco Business Tax:
   - Based on gross receipts
   - Local payroll expense tax
   - Business registration fee

## Efficiency Notes
- Prepare federal first (basis for states)
- Prepare similar states together (CA before NY)
- Maintain adjustment schedule showing federal → state modifications
- Document apportionment calculations clearly
```

**Apportionment Calculations**:

For multi-state filers:

```markdown
## Apportionment Formula

Most states use three-factor formula (some now single-factor):

### Property Factor
= (CA property / Total property)
- Beginning + Ending balance / 2
- Include owned and rented (capitalized at 8x annual rent)

### Payroll Factor
= (CA payroll / Total payroll)
- W-2 wages by location
- Include only compensation for services

### Sales Factor
= (CA sales / Total sales)
- Destination-based (where customer located)
- May be double-weighted or single-factor in some states

### Combined Factor
Traditional: (Property + Payroll + Sales) / 3
CA (current): Sales only (single-factor)
NY (current): (Property + Payroll + Sales + Sales) / 4 (double-weighted sales)

### Example
Federal taxable income: $100,000
CA apportionment: 40%
CA taxable income: $40,000
```

### 5. Supporting Statement Requirements

**When to Attach Supporting Statements**:

- Any "Other" category exceeding $10,000
- Related party transactions (always)
- Unusual or non-recurring items
- Elections being made
- Method changes
- Legal structure changes

**Supporting Statement Format**:

```markdown
# Supporting Statement for Form 1120, Line 26 (Other Deductions)

**Entity**: Acme Corporation
**EIN**: 12-3456789
**Tax Year**: 2024

## Breakdown of Other Deductions

| Description | Amount | GL Account | Documentation |
|-------------|--------|------------|----------------|
| Professional fees - Legal | $15,000 | 6300 | Invoices in source docs |
| Professional fees - Accounting | $8,500 | 6310 | Invoices in source docs |
| Bank service charges | $3,200 | 6410 | Bank statements |
| Business licenses | $2,800 | 6420 | Payment receipts |
| Subscriptions and dues | $1,500 | 6500 | Invoices/receipts |
| Software licenses | $1,000 | 6510 | License agreements |

## Total Other Deductions: $32,000

All amounts are ordinary and necessary business expenses incurred in tax year 2024.
Source documentation available in filing package source-documents folder.
```

### 6. Validation Checklist Standards

Every filing package must include comprehensive validation checklist for @compliance-checker:

```markdown
# Validation Checklist: Form 1120 - {Entity} - TY {Year}

## Entity Information
- [ ] Legal name matches IRS records
- [ ] EIN correct (XX-XXXXXXX)
- [ ] Address current
- [ ] Tax year stated correctly

## Form Completeness
- [ ] All required pages included (1-5)
- [ ] All required lines completed
- [ ] No fields left blank inappropriately
- [ ] All checkboxes addressed

## Income Section
- [ ] Gross receipts tie to books
- [ ] COGS ties to Schedule A
- [ ] Gross profit calculation correct
- [ ] Other income properly classified
- [ ] Total income calculation correct

## Deduction Section
- [ ] Officer compensation ties to W-2s
- [ ] Salaries tie to payroll records
- [ ] Depreciation ties to Form 4562
- [ ] All deductions properly classified
- [ ] Supporting statements attached for "Other"
- [ ] Total deductions calculation correct

## Schedules
- [ ] Schedule A (COGS) complete and accurate
- [ ] Schedule C (Dividends) complete if applicable
- [ ] Schedule J (Tax computation) verified
- [ ] Schedule K (Other info) all questions answered
- [ ] Schedule L (Balance sheet) balances
- [ ] Schedule M-1 (Reconciliation) ties to return
- [ ] Schedule M-2 (Retained earnings) ties to Schedule L

## Supporting Forms
- [ ] Form 4562 (Depreciation) attached if needed
- [ ] Form 4797 (Asset sales) attached if needed
- [ ] Additional schedules as required

## Cross-References
- [ ] Form 1120:2 = Schedule A bottom line
- [ ] Form 1120:20 = Form 4562 total
- [ ] Form 1120:28 = Schedule M-1 bottom line
- [ ] Schedule L ending = beginning + net income - distributions
- [ ] Schedule M-2 ending = Schedule L retained earnings

## Prior Year Comparison
- [ ] Material changes explained
- [ ] Variances documented
- [ ] Consistency maintained

## Documentation
- [ ] All W-2s attached
- [ ] All 1099s attached
- [ ] Supporting statements included
- [ ] Source documents organized

## Signatures & Filing
- [ ] Officer signature line prepared
- [ ] Date to be signed
- [ ] Preparer information (if applicable)
- [ ] PTIN included (if paid preparer)
- [ ] Filing method determined
- [ ] Payment voucher prepared (if balance due)

## Compliance
- [ ] All disclosures made
- [ ] Related party transactions disclosed
- [ ] Foreign accounts question answered
- [ ] Uncertain positions assessed

## Ready for Review
- [ ] All items above checked
- [ ] Package organized per structure
- [ ] Audit trail complete
- [ ] Ready for @compliance-checker validation

**Prepared by**: {preparer name}
**Date**: {date}
**Estimated Completion**: {percentage}
```

### 7. Audit Trail Documentation

Every filing must maintain complete audit trail:

```markdown
# Audit Trail: Form 1120 - {Entity} - TY {Year}

## Preparation Sessions

### Session 1: {date} - {duration}
**Activity**: Initial setup and document gathering
**Participants**: {names}
**Documents Reviewed**:
- Prior year Form 1120
- Financial statements
- General ledger

**Decisions Made**:
- Confirmed filing requirements
- Identified needed schedules
- Assigned preparation responsibilities

**Issues Identified**:
- {list any issues}

**Resolutions**:
- {how issues were resolved}

**Next Steps**:
- Complete documentation gathering
- Begin form preparation

---

### Session 2: {date} - {duration}
**Activity**: Primary form preparation
**Participants**: {names}
**Documents Used**:
- {list source documents}

**Sections Completed**:
- Income section (Lines 1-11)
- Deduction section (Lines 12-27)
- Tax computation (Schedule J)

**Calculations Performed**:
- {describe key calculations}

**Issues Identified**:
- {list any issues}

**Resolutions**:
- {how issues were resolved}

**Verification Steps**:
- Cross-checked amounts to source documents
- Verified prior year consistency
- Confirmed reasonability

**Next Steps**:
- Complete supporting schedules
- Prepare validation checklist

---

### Session 3: {date} - {duration}
[... continue for all sessions ...]

## Source Document Cross-Reference

| Form Line | Description | Source Document | Location | Verified |
|-----------|-------------|----------------|----------|----------|
| Line 1a | Gross receipts | Income statement | source-docs/financials.pdf, p.1 | ✓ |
| Line 2 | COGS | Schedule A | Schedule A worksheet | ✓ |
| Line 12 | Officer comp | W-2 summary | source-docs/w2s.pdf | ✓ |
| Line 20 | Depreciation | Form 4562 | 09-form-4562.pdf | ✓ |
[... continue for all material lines ...]

## Skill Application

**Skill Used**: filing-preparation
**Location**: plugins/tax-compliance/skills/filing-preparation/SKILL.md

**Patterns Applied**:
- Section 2: Document Assembly Workflow
- Section 3: Form-Specific Standards (Federal 1120)
- Section 6: Validation Checklist Standards
- Section 7: This audit trail framework

**Quality Assurance**:
- All patterns followed
- All checklists completed
- All requirements met

## Issue Log

### Issue 1: Missing 1099-MISC
**Discovered**: {date}, Session 2
**Description**: 1099-MISC for contractor services not provided
**Impact**: Cannot complete Line 26 verification
**Resolution**: Requested from accounting, received {date}
**Status**: RESOLVED

### Issue 2: Depreciation calculation question
**Discovered**: {date}, Session 2
**Description**: Uncertainty about Section 179 eligibility for equipment purchase
**Impact**: Affects Line 20 and Form 4562
**Resolution**: Reviewed IRC §179, equipment qualifies
**Status**: RESOLVED

[... continue for all issues ...]

## Quality Metrics
- Total preparation time: {hours}
- Documents reviewed: {count}
- Issues identified: {count}
- Issues resolved: {count}
- Checklists completed: {count}
- Verification steps: {count}

## Sign-off

**Prepared by**: {name}
**Date**: {date}
**Status**: Ready for compliance review

**Quality Review**: {name}
**Date**: {date}
**Status**: Approved for compliance submission

**Next Step**: Submit to @compliance-checker
```

## Best Practices Summary

✓ Follow standardized filing package structure
✓ Use comprehensive document gathering checklists
✓ Complete federal returns before state returns
✓ Prepare all schedules before finalizing primary form
✓ Attach supporting statements for material "other" items
✓ Create detailed validation checklist for compliance review
✓ Maintain complete audit trail of all preparation activities
✓ Cross-reference all amounts to source documents
✓ Perform prior year comparison for reasonability
✓ Apply quality assurance procedures before submission

## Common Pitfalls to Avoid

✗ Incomplete documentation gathering
✗ Rushing to complete forms without proper review
✗ Missing required schedules
✗ Inconsistent treatment vs prior year without explanation
✗ Missing cross-reference verification
✗ Inadequate supporting statements
✗ No validation checklist prepared
✗ Poor audit trail documentation
✗ Filing without compliance review
✗ Disorganized source documents

---

**This skill ensures professional, complete, and audit-ready tax filing packages that minimize risk and maximize compliance.**
