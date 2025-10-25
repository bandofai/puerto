# Tax Preparation Assistant Plugin

Tax preparation and document organization specialist for stress-free tax season.

## Overview

Simplify tax season with automated document checklists, deduction scanning, organized receipts, and year-end summaries. Never miss a deduction or deadline again.

## Agent

### tax-preparer (Sonnet)
**Description**: PROACTIVELY assists with tax preparation and document organization

**Capabilities**:
- Document checklist (W-2, 1099s, deduction receipts)
- Deduction scanner (medical, charitable, business)
- Organize receipts by tax category
- Year-end summary report
- Prior year comparison
- Missing document alerts
- Tax estimation

**Use When**:
- Beginning tax preparation
- Organizing receipts throughout the year
- Checking for missing documents
- Comparing to prior year
- Scanning for deductions

**Tools**: Read, Write, Bash

## Features

✅ **Document Checklist**: Complete list of required tax forms
✅ **Deduction Scanner**: Identify all deductible expenses
✅ **Receipt Organization**: Categorize by tax purpose
✅ **Year-End Summary**: Complete tax picture
✅ **Prior Year Comparison**: Track year-over-year changes
✅ **Missing Document Alerts**: Never miss a form
✅ **Standard vs Itemized**: Optimal deduction strategy

## Usage Examples

### Generate Document Checklist

```
Use tax-preparer to create my 2025 tax document checklist
Filing status: Single
Income sources: W-2, investment income, freelance
```

**Result**:
```
📋 Tax Document Checklist (2025)

INCOME DOCUMENTS
⏳ W-2 from Acme Corp (Expected: Jan 31)
⏳ 1099-INT from Chase Bank (Expected: Jan 31)
⏳ 1099-DIV from Vanguard (Expected: Feb 15)
⏳ 1099-NEC from Freelance Clients (Expected: Jan 31)

DEDUCTION DOCUMENTS
⏳ Mortgage interest 1098 (Expected: Jan 31)
⏳ Property tax statement (Expected: Mar 31)
✅ Charitable donations organized

Status: 1 received, 6 pending
Deadline: April 15, 2026
```

### Scan for Deductions

```
Use tax-preparer to scan my 2025 receipts for tax deductions
```

**Result**:
```
💰 Tax Deductions Found

MEDICAL EXPENSES (>7.5% AGI)
- Prescriptions: $1,240
- Doctor visits: $890
- Dental: $450
Total: $2,580 (Check if exceeds threshold)

CHARITABLE DONATIONS
- Goodwill (non-cash): $450
- Red Cross (cash): $500
- Local food bank: $200
Total: $1,150 ✅

BUSINESS EXPENSES (Self-employed)
- Office supplies: $340
- Software (Adobe): $660
- Professional development: $1,200
- Business meals: $890 (50% deductible = $445)
Total: $2,645 ✅

HOME OFFICE
- Proportion: 10% of home
- Utilities: $240
- Internet: $720
Total: $960 ✅

Total deductions found: $7,335
```

### Create Year-End Summary

```
Use tax-preparer to generate my 2025 year-end tax summary
```

**Result**:
```
📊 2025 Tax Year Summary

INCOME
Wages (W-2)             $85,000
Interest                    $640
Dividends                 $1,890
Freelance (1099-NEC)    $12,000
Total Income            $99,530

ADJUSTMENTS
Self-employment tax      -$848
IRA contribution       -$6,500
Adjusted Gross Income   $92,182

DEDUCTIONS
Standard: $14,600
Itemized: $18,450
Using: Itemized (saves $3,850)

Taxable Income          $73,732

ESTIMATED TAX
Federal (22% bracket)    $11,642
Self-employment tax       $1,696
State (5%)               $3,687
Total liability         $17,025

Already paid: $18,200
ESTIMATED REFUND: $1,175 ✅
```

### Compare to Prior Year

```
Use tax-preparer to compare 2025 vs 2024 taxes
```

**Result**:
```
📈 Tax Year Comparison: 2025 vs 2024

INCOME
W-2 Wages: $85,000 (+$5,000, +6.3%)
Freelance: $12,000 (+$4,000, +50.0%) ⬆️
Investment: $2,530 (+$340, +15.5%)

DEDUCTIONS
Itemized: $18,450 (+$2,200, +13.5%)
- Charitable: $1,150 (+$400, +53.3%) ⬆️
- Business: $2,645 (+$980, +58.8%) ⬆️

TAX LIABILITY
2024: $15,890
2025: $17,025 (+$1,135, +7.1%)

Higher income (+$9,340) led to higher taxes
but increased deductions partially offset
```

## Document Checklist

### Income Documents

| Form | Purpose | Deadline | Source |
|------|---------|----------|--------|
| **W-2** | Wage and salary income | Jan 31 | Employer |
| **1099-INT** | Interest income | Jan 31 | Banks |
| **1099-DIV** | Dividend income | Feb 15 | Brokerage |
| **1099-B** | Stock sales | Feb 15 | Brokerage |
| **1099-MISC** | Miscellaneous income | Jan 31 | Various |
| **1099-NEC** | Non-employee compensation | Jan 31 | Clients |
| **1099-K** | Payment card transactions | Jan 31 | PayPal, Venmo |
| **K-1** | Partnership/S-corp income | Mar 15 | Business |

### Deduction Documents

| Category | Documents Needed | Notes |
|----------|------------------|-------|
| **Medical** | Insurance premiums, prescriptions, doctor bills | >7.5% AGI threshold |
| **Charitable** | Donation receipts | >$250 needs acknowledgment |
| **Mortgage** | 1098 interest statement | From lender |
| **Property Tax** | Tax bill and payment proof | From county |
| **Business** | Receipts for all expenses | Self-employed |
| **Education** | 1098-T, 1098-E | Tuition, student loans |

## Deduction Categories

### Above-the-Line Deductions
Available even if taking standard deduction:

| Deduction | Limit | Who Qualifies |
|-----------|-------|---------------|
| IRA contribution | $7,000 ($8,000 if 50+) | Income limits apply |
| Student loan interest | $2,500 | Income limits apply |
| HSA contribution | $4,150 single ($8,300 family) | HDHP required |
| Self-employed health insurance | No limit | Self-employed only |
| Self-employment tax | 50% of SE tax | Self-employed only |

### Itemized Deductions

**Standard Deduction (2025)**:
- Single: $14,600
- Married filing jointly: $29,200
- Head of household: $21,900

**When to Itemize**: Only if total itemized exceeds standard

**Categories**:
1. **Medical**: Expenses >7.5% of AGI
2. **State/Local Taxes**: Max $10,000 (SALT cap)
3. **Mortgage Interest**: Primary residence
4. **Charitable**: Cash and non-cash donations
5. **Casualty Losses**: Federally declared disasters only

## Tax Brackets (2025)

### Single Filers

| Taxable Income | Rate |
|----------------|------|
| $0 - $11,600 | 10% |
| $11,601 - $47,150 | 12% |
| $47,151 - $100,525 | 22% |
| $100,526 - $191,950 | 24% |
| $191,951 - $243,725 | 32% |
| $243,726 - $609,350 | 35% |
| $609,351+ | 37% |

## Important Tax Deadlines

| Date | Deadline |
|------|----------|
| **Jan 31** | W-2, 1099-MISC/NEC due |
| **Feb 15** | Most 1099 forms (INT, DIV, B) |
| **Apr 15** | Tax return filing deadline |
| **Apr 15** | IRA contribution deadline (prior year) |
| **Oct 15** | Extended deadline (if extension filed) |

## Installation

```bash
# Plugin is ready to use
# Integrates with receipt-processor for deduction scanning
# Use throughout the year to stay organized
```

## Design Decisions

**Model Choice**: Sonnet
- Tax knowledge requires expertise
- Deduction rules need accurate interpretation
- Document requirements vary by situation
- Prior year comparison needs context
- Cost: ~$0.015/1K tokens (justified for accuracy)

**Tools**: Read, Write, Bash
- Read: Access receipts and financial data
- Write: Save checklists and summaries
- Bash: Run tax calculation scripts

**Integration**: Works with other plugins
- receipt-processor: Deduction data
- portfolio-tracker: Investment income
- goal-tracker: Charitable contributions
- bill-reminder: Deductible payments

## Requirements Met

✅ Document checklist (W-2, 1099, receipts)
✅ Deduction scanner (medical, charitable, business)
✅ Organize receipts by tax category
✅ Year-end summary report
✅ Prior year comparison
✅ Missing document alerts

## Integration with Other Plugins

**receipt-processor** (#105):
- Provides expense and deduction data
- Categorizes receipts by tax purpose
- Flags tax-deductible items

**portfolio-tracker** (#106):
- Investment income (dividends, interest, capital gains)
- Tax-loss harvesting data
- Cost basis for stock sales

**goal-tracker** (#107):
- IRA contributions
- Charitable giving goals
- Business expense tracking

**bill-reminder** (#104):
- Mortgage interest payments
- Property tax payments
- Deductible utilities (home office)

## Tax Planning Tips

1. **Maximize Deductions**:
   - Bunch charitable donations in one year
   - Time medical procedures
   - Harvest tax losses before year-end

2. **Above-the-Line First**:
   - Max out IRA ($7,000)
   - Max out HSA ($4,150)
   - Deduct student loan interest

3. **Track Throughout Year**:
   - Don't wait until April
   - Save all receipts
   - Document mileage

4. **Consider Itemizing If**:
   - High medical expenses
   - Significant charitable giving
   - Large mortgage interest
   - Live in high-tax state

## Disclaimer

⚠️ **Not Professional Tax Advice**

This plugin:
- ✅ Organizes documents
- ✅ Identifies potential deductions
- ✅ Generates summaries
- ❌ Does NOT provide tax advice
- ❌ Does NOT prepare tax returns
- ❌ Does NOT guarantee deduction eligibility

**Always consult a tax professional** for:
- Complex tax situations
- Business tax planning
- Audit representation
- State-specific rules
- Tax law interpretation

## Troubleshooting

**Missing 1099 forms**:
- Contact payer/financial institution
- Check online account portals
- Request by Feb 15 deadline

**Deductions not found**:
- Ensure receipts processed by receipt-processor
- Check category assignments
- Verify tax-deductible flag set

**Incorrect tax estimate**:
- Verify income amounts
- Check filing status
- Review deduction calculations
- Tax brackets may have changed

---

**Version**: 1.0.0
**Model**: Sonnet (tax expertise)
**Status**: Production-ready
**Tax Year**: 2025
