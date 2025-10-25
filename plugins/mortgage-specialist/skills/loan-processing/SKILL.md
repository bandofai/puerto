# Loan Processing Skill

Professional standards and methodologies for mortgage loan application processing, document collection, qualification analysis, and file management through the complete loan lifecycle.

## Purpose

This skill provides standardized frameworks for:
- Application intake and initial setup
- Comprehensive document collection
- Income and asset verification
- Initial qualification calculations (DTI, LTV)
- TRID disclosure compliance
- File organization and status tracking

## Core Concepts

### 1. Loan Application File Structure

Every loan application should follow standardized organization:

```
loan-applications/{year}/{app-id}-{borrower-last-name}/
├── 00-application-summary.md
├── 01-initial-application/
│   ├── 1003-uniform-residential-loan-application.pdf
│   ├── borrower-authorization-forms.pdf
│   ├── intent-to-proceed.pdf
│   └── application-checklist.md
├── 02-disclosures/
│   ├── loan-estimate-initial.pdf
│   ├── loan-estimate-revised-{date}.pdf
│   ├── closing-disclosure.pdf
│   ├── servicing-disclosure.pdf
│   ├── affiliated-business-disclosure.pdf
│   └── disclosure-log.md
├── 03-income-documentation/
│   ├── w2-forms/
│   ├── pay-stubs/
│   ├── tax-returns/
│   ├── business-tax-returns/
│   ├── voe-forms/
│   └── income-calculation-worksheet.md
├── 04-asset-documentation/
│   ├── bank-statements/
│   ├── investment-statements/
│   ├── retirement-statements/
│   ├── gift-letters/
│   └── asset-calculation-worksheet.md
├── 05-credit-documentation/
│   ├── credit-report.pdf
│   ├── credit-explanation-letters/
│   └── credit-analysis-summary.md
├── 06-property-documentation/
│   ├── purchase-agreement.pdf
│   ├── appraisal-report.pdf
│   ├── title-report.pdf
│   ├── hoa-documents/
│   ├── insurance-declaration.pdf
│   └── property-inspection-reports/
├── 07-underwriting/
│   ├── underwriting-submission-package.pdf
│   ├── findings-and-conditions.md
│   ├── condition-responses/
│   └── final-approval-letter.pdf
├── 08-compliance/
│   ├── compliance-checklist.md
│   ├── QM-determination.md
│   ├── ATR-documentation.md
│   └── compliance-validation-report.md
├── 09-closing-documents/
├── processing-timeline.md
├── qualification-analysis.md
└── processor-notes.md
```

### 2. Document Collection Standards

#### Standard Documentation Requirements

**Income Documentation (W-2 Employees)**:
- Most recent 2 years W-2 forms (all employers)
- Most recent 30 days consecutive pay stubs showing YTD earnings
- Most recent 2 years personal tax returns (1040 with all schedules)
- Verification of Employment (VOE) - ordered by processor
- If overtime/bonus/commission: 2-year history and continuance verification

**Income Documentation (Self-Employed)**:
- Most recent 2 years personal tax returns (1040 with all schedules)
- Most recent 2 years business tax returns (1120/1120-S/1065/Schedule C)
- YTD Profit & Loss statement (signed by CPA or borrower)
- YTD Balance Sheet (if corporate entity)
- Business license or evidence of business existence
- Note: Self-employed defined as ≥25% ownership in business

**Asset Documentation**:
- Most recent 2 months bank statements (all pages, all accounts)
  - Checking accounts
  - Savings accounts
  - Money market accounts
- Most recent 2 months investment statements
  - Brokerage accounts
  - Stocks, bonds, mutual funds
- Most recent quarterly retirement account statements
  - 401(k), 403(b), 457 plans
  - Traditional and Roth IRAs
- Gift funds (if applicable):
  - Gift letter from donor (relationship, amount, no repayment expected)
  - Donor's bank statement showing withdrawal
  - Evidence of transfer to borrower account
- Large deposit explanations (>50% of monthly income):
  - Written explanation from borrower
  - Supporting documentation (tax refund, sale of asset, transfer between own accounts)

**Credit Documentation**:
- Tri-merge credit report (all three bureaus: Equifax, Experian, TransUnion)
- Signed credit authorization form
- Explanation letters for derogatory credit items:
  - Late payments (30, 60, 90 days)
  - Collections accounts
  - Charge-offs
  - Bankruptcies
  - Foreclosures
  - Short sales
- Payment arrangements for unpaid collections/judgments

**Property Documentation (Purchase)**:
- Fully executed purchase agreement
- All addenda and amendments
- Property inspection reports
- Appraisal report (ordered after application)
- Preliminary title report/title commitment
- HOA documents (if applicable):
  - CC&Rs (Covenants, Conditions & Restrictions)
  - Bylaws
  - Budget
  - Master insurance policy
  - Questionnaire
- Hazard insurance binder/declaration page
- Property tax bills

**Property Documentation (Refinance)**:
- Current mortgage statement (all loans on property)
- Property tax bills
- Homeowners insurance declaration page
- HOA documents (if applicable)
- Appraisal report (ordered after application)
- Preliminary title report

**Identity & Legal Documentation**:
- Government-issued photo ID (driver's license, passport, state ID)
- Social Security card or SSN verification
- Proof of legal residency (if not U.S. citizen):
  - Permanent resident card (green card)
  - Work visa with EAD
- Divorce decree (if applicable)
- Child support/alimony court order (if applicable)
- Bankruptcy discharge papers (if applicable, with all schedules)
- Deed-in-lieu or short sale documents (if applicable)

### 3. Debt-to-Income (DTI) Calculation Standards

#### Front-End Ratio (Housing Ratio)

Formula: **PITIA / Gross Monthly Income**

**PITIA Components**:
- **P**: Principal (monthly principal payment)
- **I**: Interest (monthly interest payment)
- **T**: Property Taxes (annual / 12)
- **I**: Insurance (annual homeowner's insurance / 12)
- **A**: Association Dues (monthly HOA dues, if applicable)

**Additional Housing Costs**:
- Mortgage Insurance (PMI for conventional, MIP for FHA, funding fee for VA)
- Special assessments (if applicable)
- Ground rent (if applicable)

**Front-End Ratio Guidelines**:
- Conventional: Typically ≤ 28%
- FHA: ≤ 31% (can exceed with compensating factors)
- VA: No front-end ratio requirement
- USDA: ≤ 29%

#### Back-End Ratio (Total DTI)

Formula: **(PITIA + Monthly Debt Obligations) / Gross Monthly Income**

**Monthly Debt Obligations Include**:

1. **Revolving Debt (Credit Cards)**:
   - Use actual minimum payment shown on credit report
   - If no payment shown: Use greater of $10 or 5% of outstanding balance
   - Count even if paying off at closing (unless documented payoff)

2. **Installment Loans**:
   - Auto loans: Monthly payment as shown
   - Personal loans: Monthly payment as shown
   - Furniture/appliance financing: Monthly payment
   - If ≤ 10 months remaining: Can exclude if documented to end

3. **Student Loans**:
   - If in repayment: Use actual payment
   - If deferred/forbearance: Use 0.5% of outstanding balance OR actual IBR payment if documented
   - If graduated/step payment: Use future payment, not current
   - If no payment shown: Use 1% of outstanding balance

4. **Alimony/Child Support**:
   - Use full monthly payment per court order
   - Must continue for at least 36 months (3 years)

5. **Other Obligations**:
   - Auto leases: Monthly payment (exclude if < 10 months and documented)
   - Timeshare maintenance fees: Monthly amount
   - Tax liens: Payment plan amount
   - Other debts: Any recurring monthly obligation

**Items NOT Included in DTI**:
- Utilities (electric, gas, water, internet, phone)
- Groceries and food
- Medical expenses (unless monthly payment plan)
- Insurance (auto, life, unless financed)
- Entertainment and discretionary spending
- Child care
- Cell phone bills
- Gym memberships

**Back-End DTI Guidelines**:
- Conventional: ≤ 43% (Qualified Mortgage), ≤ 50% with DU/LP approval
- FHA: ≤ 43% standard, ≤ 50% with compensating factors
- VA: ≤ 41% guideline (residual income more important)
- USDA: ≤ 41%

#### DTI Calculation Example

```
Borrower Monthly Income: $6,000
Co-Borrower Monthly Income: $4,000
Total Gross Monthly Income: $10,000

Proposed Housing Payment (PITIA):
- Principal & Interest: $1,200
- Property Taxes: $300
- Homeowners Insurance: $100
- HOA Dues: $150
- Mortgage Insurance: $150
Total PITIA: $1,900

Monthly Debts:
- Auto loan: $400
- Student loan: $250
- Credit card minimums: $150
Total Monthly Debts: $800

Front-End Ratio = $1,900 / $10,000 = 19% ✓
Back-End Ratio = ($1,900 + $800) / $10,000 = 27% ✓

Status: Qualified (both ratios within conventional guidelines)
```

### 4. Loan-to-Value (LTV) Calculation Standards

#### LTV Formula

**LTV = Loan Amount / Property Value × 100**

**Property Value** = Lesser of:
- Purchase price (for purchases)
- Appraised value

#### LTV Examples

**Purchase Example**:
- Purchase price: $400,000
- Appraised value: $420,000
- Property value (lesser): $400,000
- Down payment: $40,000
- Loan amount: $360,000
- LTV = $360,000 / $400,000 = 90%

**Refinance Example**:
- Current loan balance: $250,000
- Appraised value: $400,000
- New loan amount: $320,000 (cash-out)
- LTV = $320,000 / $400,000 = 80%

#### Combined LTV (CLTV)

When multiple mortgages:

**CLTV = (First Mortgage + Second Mortgage + Other Liens) / Property Value × 100**

**Example**:
- Property value: $400,000
- First mortgage: $300,000
- HELOC/Second mortgage: $40,000
- CLTV = ($300,000 + $40,000) / $400,000 = 85%

#### LTV Guidelines by Loan Type

**Conventional Loans**:
- Maximum LTV: 97% (with PMI)
- PMI required if LTV > 80%
- PMI cancellation when LTV ≤ 78% (paid down)
- Higher LTV requires higher credit scores

**FHA Loans**:
- Maximum LTV: 96.5%
- Upfront MIP: 1.75% of base loan amount
- Annual MIP required (life of loan if LTV > 90% at origination)

**VA Loans**:
- Maximum LTV: 100% (no down payment)
- VA funding fee: 2.3% (first use), 3.6% (subsequent use), waived for disabled veterans
- No PMI required

**USDA Loans**:
- Maximum LTV: 100% (no down payment)
- Upfront guarantee fee: 1% of loan amount
- Annual fee: 0.35% of outstanding balance
- Property must be in USDA-eligible rural area

**Jumbo Loans**:
- Maximum LTV: 80-90% (varies by lender)
- Loan amount exceeds conforming limit ($766,550 in most areas for 2024)
- Stricter qualifying standards
- Higher reserves required

### 5. TRID Disclosure Timeline Standards

#### Application Definition

An **application** consists of six pieces of information:
1. Borrower's name
2. Borrower's income
3. Borrower's Social Security number
4. Property address
5. Estimate of property value
6. Loan amount sought

**Application Date** = Date when all six pieces received

#### Loan Estimate (LE) Timeline

**3-Business Day Rule**:
- Lender must deliver or mail LE within 3 business days of application
- **Business days**: All calendar days except Sundays and federal holidays
- If mailed: Add 3 days to delivery date (presumed receipt rule)

**LE Expiration**:
- LE valid for 10 business days from issuance
- After 10 days, lender may issue revised LE

**Intent to Proceed**:
- Borrower must indicate intent to proceed before lender can charge fees
- Can be verbal or written
- Allows lender to order appraisal, charge credit report fee

**Changed Circumstances**:

Valid reasons to revise LE:
1. **Changed Circumstance**: Information relied upon changes or was inaccurate
2. **Changed Circumstance Affecting Eligibility**: Borrower no longer qualifies
3. **Revisions Requested by Borrower**: Borrower requests changes
4. **Interest Rate Lock**: Rate locked (if rate-dependent fees change)
5. **Expiration**: LE expires, settlement delayed beyond expiration
6. **Construction Delays**: Construction loan only

**Revised LE Timeline**:
- Must be provided within 3 business days of receiving information about changed circumstance
- Resets any applicable waiting periods

#### Closing Disclosure (CD) Timeline

**3-Business Day Rule**:
- CD must be provided at least 3 business days before consummation
- **Business days**: All calendar days except Sundays and federal holidays
- Consummation = When borrower becomes contractually obligated (signing)

**Delivery Methods**:
- Hand delivery: Received same day
- Mail: Received 3 business days after mailing
- Email: Received same day (if borrower consents to electronic delivery)

**Changes Requiring New 3-Day Wait**:
1. APR increases by more than 1/8% (0.125%) for regular transactions
2. APR increases by more than 1/4% (0.25%) for irregular transactions
3. Loan product changes
4. Prepayment penalty is added when not previously disclosed

**Changes NOT Requiring New 3-Day Wait**:
- APR decreases
- Other fees change (within tolerance)
- Closing cost increases within tolerance
- Minor clerical changes

### 6. Income Calculation Standards

#### W-2 Wage Earners

**Base Salary**:
- Use current pay stub (monthly salary or hourly × average hours)
- Verify with W-2 (current year and prior year)
- Verify with VOE
- Must show 2-year history

**Overtime/Bonus/Commission**:
- Requires 2-year history
- Calculate average of 2 years
- Divide by 24 months for monthly average
- Must verify likelihood of continuance
- If declining, may need to use lower year or exclude

**Example**:
```
Year 1 Overtime: $12,000
Year 2 Overtime: $15,000
Average: ($12,000 + $15,000) / 2 = $13,500/year
Monthly: $13,500 / 12 = $1,125/month
```

**Multiple Jobs**:
- Each job requires 2-year history for stability
- If less than 2 years, may need to exclude

#### Self-Employed Income

**Income Calculation**:
- Use tax returns (personal and business)
- Calculate average of 2 years
- Add back non-recurring expenses:
  - Depreciation (non-cash expense)
  - Depletion (non-cash expense)
  - Business use of home (if applicable)
  - Meals and entertainment (if added back per policy)

**Example - Schedule C**:
```
Year 1 Net Profit (Schedule C): $60,000
Year 1 Depreciation: $5,000
Year 1 Adjusted Income: $65,000

Year 2 Net Profit: $70,000
Year 2 Depreciation: $6,000
Year 2 Adjusted Income: $76,000

Average: ($65,000 + $76,000) / 2 = $70,500/year
Monthly: $70,500 / 12 = $5,875/month
```

**Partnership/S-Corp (K-1 Income)**:
- Use K-1 line 1 (ordinary business income)
- Add back depreciation from K-1
- Average 2 years
- Verify cash flow with business tax returns

**Declining Income**:
- If declining year-over-year, may use lower year
- May require CPA letter explaining circumstances
- May not be acceptable if significant decline

#### Rental Income

**Documentation Required**:
- Current lease agreement
- Schedule E from tax returns (2 years)
- Rental history if new landlord

**Income Calculation**:
- Use Schedule E income (or loss)
- If new rental: Use 75% of gross rent (PITI already in DTI)
- If established rental: Use actual from tax returns

**Example**:
```
Gross Rents: $24,000
Expenses: $18,000
Net Rental Income (Schedule E): $6,000
Monthly: $6,000 / 12 = $500/month
```

**Rental Loss**:
- If Schedule E shows loss, add to DTI as debt

#### Other Income Sources

**Social Security/Pension/Disability**:
- Award letter required
- Must continue for at least 3 years
- Use gross monthly amount

**Alimony/Child Support Received**:
- Divorce decree or court order required
- Must continue for at least 3 years
- Payment history (6 months) may be required
- Use monthly amount

**Investment/Interest/Dividend Income**:
- 2 years tax returns showing income
- Account statements
- Average 2 years for monthly amount

### 7. Asset Verification Standards

#### Acceptable Sources

**Liquid Assets** (Available for Down Payment/Closing Costs):
- Checking accounts
- Savings accounts
- Money market accounts
- Stocks, bonds, mutual funds (use current value minus any penalties/taxes)
- Retirement accounts (401k, IRA) - 60% of vested balance (40% penalty/tax)

**Non-Liquid Assets** (For Reserves Only):
- Retirement accounts (use 100% of vested balance for reserve calculation)
- Cash value life insurance

#### Verification Requirements

**Bank Statements**:
- Most recent 2 consecutive months
- All pages (even blank pages) required
- Must show: Account number, borrower name, period dates, beginning/ending balance

**Large Deposit Verification**:
- Any deposit > 50% of gross monthly income requires explanation
- Acceptable sources:
  - Payroll deposit (verify with pay stub)
  - Tax refund (provide tax return or IRS letter)
  - Transfer between own accounts (provide both statements)
  - Sale of asset (provide closing statement or receipt)
  - Gift (provide gift letter and donor statement)

**Unacceptable Sources**:
- Loans from individuals
- Unsecured personal loans
- Credit card cash advances
- Unexplained large deposits

#### Reserves Requirement

**Reserves** = Monthly PITIA × Number of Months

**Reserve Requirements by Loan Type**:
- Primary Residence (1 unit): 2 months
- Second Home: 2 months
- Investment Property (1 unit): 6 months
- 2-4 Units (owner-occupied): 6 months
- High LTV (>90%): May require additional reserves

**Calculating Reserves**:
```
Monthly PITIA: $2,000
Required Reserves (Primary, 2 months): $4,000

Available Assets:
- Checking: $5,000
- Savings: $10,000
- 401k (vested): $50,000 → Count as $50,000 for reserves
Total Available for Reserves: $65,000 ✓
```

### 8. Application Status Workflow

#### Status Progression

```
Application Received
    ↓
Disclosures Sent (LE within 3 days)
    ↓
Intent to Proceed Received
    ↓
Documentation Requested
    ↓
Documentation In Progress (% complete tracking)
    ↓
Income Verified
    ↓
Assets Verified
    ↓
Credit Reviewed
    ↓
Appraisal Ordered
    ↓
Appraisal Completed
    ↓
File Complete - Ready for Underwriting
    ↓
Submitted to Underwriting
    ↓
Initial Review (Underwriter)
    ↓
Suspended (Awaiting Conditions) [if applicable]
    ↓
Conditionally Approved
    ↓
Conditions Cleared
    ↓
Clear to Close
    ↓
CD Sent (3-day wait)
    ↓
Closing Scheduled
    ↓
Funded
    ↓
Closed
```

#### Status Definitions

- **Application Received**: Initial 1003 submitted
- **Disclosures Sent**: LE provided to borrower (within 3 business days)
- **Intent Received**: Borrower indicated intent to proceed
- **Docs Requested**: Document checklist sent to borrower
- **Docs In Progress**: Partial documents received (track % complete)
- **Income Verified**: All income documentation complete and verified
- **Assets Verified**: All asset documentation complete and verified
- **Credit Reviewed**: Credit report reviewed, explanations obtained
- **Appraisal Ordered**: Appraisal ordered from AMC
- **Appraisal Complete**: Appraisal received and acceptable
- **Submitted to UW**: Complete file package submitted to underwriter
- **Initial Review**: Underwriter conducting first review
- **Suspended**: Underwriter needs additional documentation/conditions
- **Conditionally Approved**: Approved subject to conditions
- **Conditions Cleared**: All underwriting conditions satisfied
- **Clear to Close**: Final approval, no outstanding conditions
- **CD Sent**: Closing Disclosure sent (3-day waiting period starts)
- **Closing Scheduled**: Closing date/time confirmed
- **Funded**: Loan funded
- **Closed**: Loan successfully closed

## Best Practices Summary

✓ **Complete Documentation Upfront**: Request all documents at application to avoid delays
✓ **Accurate DTI Calculations**: Include all debts, use proper income averaging
✓ **TRID Compliance**: Track all disclosure deadlines meticulously
✓ **Consistent File Organization**: Use standardized folder structure
✓ **Clear Communication**: Set expectations with borrowers on requirements and timeline
✓ **Proactive Follow-up**: Don't wait for borrowers, follow up regularly
✓ **Quality Control**: Review all documents for completeness before submission
✓ **Status Transparency**: Keep all stakeholders informed of progress
✓ **Condition Management**: Track and clear conditions systematically
✓ **Timeline Management**: Monitor processing time and identify delays early

## Common Pitfalls to Avoid

✗ **Incomplete Applications**: Missing key information delays disclosure
✗ **Late Disclosure Delivery**: TRID violations can void the loan
✗ **Incorrect DTI Calculation**: Including wrong items or excluding required debts
✗ **Insufficient Documentation**: Partial bank statements, missing schedules on tax returns
✗ **Large Deposit Oversight**: Failing to document deposits > 50% monthly income
✗ **Self-Employment Miscalculation**: Not adding back depreciation
✗ **Student Loan Omission**: Failing to include deferred student loans in DTI
✗ **Reserve Shortfall**: Not calculating reserves correctly
✗ **Expired Documents**: Allowing documents to exceed 120-day age limit
✗ **Poor File Organization**: Disorganized files delay underwriting

---

**This skill ensures professional, complete loan processing that accelerates approvals, maintains compliance, and delivers excellent borrower service.**
