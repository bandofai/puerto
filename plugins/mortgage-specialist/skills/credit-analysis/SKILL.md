# Credit Analysis Skill

Professional standards for mortgage credit report analysis, risk assessment, and credit decisioning following industry guidelines and regulatory requirements.

## Purpose

This skill provides standardized frameworks for:
- Credit report review and score evaluation
- Derogatory item analysis and treatment
- Trade line verification and debt calculation
- Credit risk assessment and underwriting recommendations
- Fair lending compliance in credit decisions

## Core Concepts

### 1. Credit Score Standards

#### Representative Credit Score Rule

**Single Borrower**:
- Obtain scores from all three bureaus (Equifax, Experian, TransUnion)
- **Use middle score** of the three
- If only two scores available: Use lower score
- If only one score: Use that score

**Multiple Borrowers**:
- Obtain middle score for each borrower
- **Use lower of the two middle scores** for qualification

**Example**:
```
Borrower 1: Equifax 720, Experian 740, TransUnion 730 → Middle: 730
Borrower 2: Equifax 680, Experian 700, TransUnion 690 → Middle: 690
Representative Score for Loan: 690 (lower of two middle scores)
```

#### Minimum Credit Score Requirements

**Conventional**:
- Minimum: 620
- Optimal pricing: 740+
- Manual underwrite: < 680 (typically)

**FHA**:
- 3.5% down: 580 minimum
- 10% down: 500 minimum
- Manual underwrite: < 580

**VA**:
- No official minimum (lender overlays typically 580-620)
- Residual income more important than score

**USDA**:
- 640 for automated approval
- < 640 requires manual underwrite

### 2. Derogatory Credit Item Treatment

#### Bankruptcies

**Chapter 7**:
- Conventional: 4 years from discharge (2 years with extenuating circumstances)
- FHA: 2 years from discharge
- VA: 2 years from discharge
- Requirements:
  - Re-established credit (2-4 tradelines)
  - Clean payment history since discharge
  - Explanation of circumstances

**Chapter 13**:
- Conventional: 2 years from discharge, or 4 years from dismissal
- FHA: 12 months of payments with court approval to incur new debt
- VA: 12 months of payments with court approval
- Requirements:
  - Payment history to trustee must be perfect
  - Court approval for new mortgage debt

#### Foreclosures

**Conventional**: 7 years from completion (3 years with extenuating circumstances)
**FHA**: 3 years from completion
**VA**: 2 years from completion

**Extenuating Circumstances** (Conventional):
- Job loss, death of wage earner, serious illness
- Results in 3-year vs 7-year waiting period
- Requires documentation of circumstances
- Cannot have other significant derogatory items

#### Short Sales / Deeds-in-Lieu

**Conventional**: 4 years (2 years with extenuating circumstances)
**FHA**: 3 years
**VA**: 2 years

**Key Factor**: Was there a deficiency?
- No deficiency: Treated more favorably
- Deficiency: Treated like foreclosure

#### Collections and Charge-Offs

**Medical Collections**:
- FHA: Can ignore all medical collections
- Conventional: Ignore if < $250 per account
- VA: Ignore if < $250

**Non-Medical Collections**:
- **Conventional**:
  - < $250/account: Can ignore
  - ≥ $250/account: Pay or payment plan if total > $5,000

- **FHA**:
  - Total non-medical > $2,000: Must pay or payment plan

- **VA**:
  - Total collections: No specific threshold, underwriter discretion
  - Delinquent federal debt: Must be paid or in payment plan

**Treatment Options**:
1. **Pay in full**: Obtain paid receipt
2. **Payment plan**: Document agreement, include in DTI
3. **Dispute**: Cannot close with active disputes unless resolved
4. **Ignore**: If within program guidelines

#### Judgments and Tax Liens

**Federal Tax Liens**:
- Must be paid off before closing OR
- Payment plan with IRS AND subordination agreement

**Other Judgments**:
- Must be paid off before closing OR
- Payment plan documented and included in DTI

**Unpaid Judgments**:
- Cannot close if judgment will become a lien on property
- Must show as satisfied on title

### 3. Payment History Analysis

#### Late Payment Evaluation

**Housing Payment History** (Most Critical):
- No 30-day late payments in past 12 months: Preferred
- 1 × 30-day late in past 12 months: Acceptable with explanation
- 2+ × 30-day lates in past 12 months: Significant concern, may decline
- Any 60-day late in past 24 months: Manual underwrite, compensating factors needed
- 90-day late: Very difficult to approve

**Installment Debt Payment History**:
- Recent lates (past 12 months): Require explanation
- Pattern of lates: Indicates financial stress
- Single isolated late: Acceptable with explanation

**Revolving Debt Payment History**:
- Recent lates on multiple cards: Red flag
- Maxed-out cards with lates: Severe risk
- Clean recent history: Positive indicator

#### Payment Pattern Assessment

**Positive Patterns**:
- Consistent on-time payments
- Paying down balances
- Long credit history
- Mix of credit types

**Negative Patterns**:
- Increasing late payments
- Rising balances
- Multiple recent accounts opened
- High utilization

### 4. Trade Line Analysis and DTI Impact

#### Revolving Credit (Credit Cards)

**Payment Calculation**:
- Use minimum payment shown on credit report
- If no payment shown: Greater of $10 or 5% of balance

**Example**:
```
Card 1: Balance $5,000, Min payment $150 → Use $150
Card 2: Balance $1,000, No payment shown → Use $50 (5% of $1,000)
Card 3: Balance $100, No payment shown → Use $10 (minimum floor)
```

**Utilization Analysis**:
- Optimal: < 30% per card, < 10% overall
- Acceptable: 30-50%
- Concerning: > 50%
- Severe: > 75% or maxed out

#### Installment Loans

**Auto Loans**:
- Include monthly payment as shown
- If < 10 months remaining: Can exclude if documented

**Personal Loans**:
- Include monthly payment
- Review purpose (red flag if recent debt consolidation)

**Student Loans**:
- **In Repayment**: Use actual payment
- **Deferred**: Use 0.5% of balance OR documented IBR payment
- **Forbearance**: Use 0.5% of balance
- **No Payment Shown**: Use 1% of balance
- **Graduated Payment**: Use future higher payment

**Example**:
```
Student Loan Balance: $50,000
Status: Deferred
No payment shown on credit
DTI Calculation: $50,000 × 1% = $500/month
```

#### Alimony / Child Support

**As Debt**:
- Must continue for at least 36 months
- Use full monthly amount from court order
- Include in DTI

**As Income**:
- Must continue for at least 36 months
- 6-month payment history may be required
- Reduces need for other income

### 5. Credit Inquiry Analysis

**Hard Inquiries** (Impact Score):
- Mortgage inquiries (45 days): Counted as 1
- Auto inquiries (14 days): Counted as 1
- Student loan inquiries (30 days): Counted as 1
- Other inquiries: Each counts separately

**Acceptable Inquiry Activity**:
- Mortgage shopping: Multiple inquiries in 45 days normal
- Auto shopping: Multiple inquiries in 14 days normal
- Mixed shopping: Reasonable pattern

**Red Flags**:
- Excessive inquiries (10+ in 6 months): Financial stress
- Multiple credit card inquiries: Seeking credit
- Inquiries for new accounts not opened: Denials?

**Required Actions**:
- Explanation letter if excessive inquiries
- Verify no new debt from recent inquiries

### 6. Credit Risk Rating Framework

#### Risk Rating Criteria

**EXCELLENT (A+) Risk**:
- Credit score ≥ 760
- Perfect payment history (24 months)
- No derogatory items (7 years)
- Utilization < 30%
- Long credit history (10+ years)
- **Approval**: Automatic, best pricing

**GOOD (A) Risk**:
- Credit score 720-759
- Clean payment history (12 months)
- No significant derogatory items (4 years)
- Utilization < 50%
- Established credit history (5+ years)
- **Approval**: Standard, good pricing

**ACCEPTABLE (B) Risk**:
- Credit score 680-719
- Minor late payments (> 12 months ago)
- Derogatory items beyond waiting periods
- Utilization < 75%
- **Approval**: Likely, moderate pricing adjustments

**MARGINAL (C) Risk**:
- Credit score 620-679
- Recent late payments or derogatory items
- Collections requiring resolution
- High utilization
- Limited credit history
- **Approval**: Manual underwrite, pricing hits, compensating factors needed

**POOR (D) Risk**:
- Credit score < 620
- Significant recent derogatory items
- Active collections/judgments
- Does not meet minimum guidelines
- **Approval**: Unlikely for conventional programs

### 7. Credit Report Verification

#### Required Checks

**Data Accuracy**:
- Verify borrower name matches application
- Verify SSN matches application
- Verify address history reasonable
- Check for variations in name/SSN (fraud indicators)

**Account Verification**:
- All accounts belong to borrower (not authorized user for qualification)
- Balances match recent statements
- Payment history consistent across bureaus

**Disputed Accounts**:
- Cannot close with active disputes
- Exception: Dispute is frivolous (account is borrower's)
- Must resolve before closing or provide documentation

**Report Age**:
- Credit report valid for 120 days
- Re-pull required if > 120 days old at closing
- Check for new derogatory items on re-pull

### 8. Fair Lending in Credit Decisions

#### Prohibited Factors

**Cannot Consider** (ECOA):
- Race or color
- Religion
- National origin
- Sex
- Marital status
- Age (unless favorable to applicant)
- Source of income (public assistance, alimony, child support)

#### Required Practices

**Consistent Standards**:
- Apply same credit criteria to all applicants
- Document reasons for adverse decisions
- Use objective standards, not subjective judgment

**Adverse Action Notices**:
- Required if: Denied, approved with less favorable terms, or counteroffer
- Must provide within 30 days
- Must state specific reasons
- Must include ECOA notice and credit score disclosure

**Documentation**:
- All credit decisions must be documented
- Rationale for manual underwrite decisions
- Compensating factors considered
- Objective criteria applied

## Credit Decision Framework

### Approve Recommendations

**Auto-Approve** (if meets all):
- Credit score meets minimum for program
- No late housing payments (12 months)
- No significant derogatory items within waiting period
- All collections within program guidelines
- DTI within acceptable range
- Adequate reserves

**Approve with Conditions**:
- Pay specific collections before closing
- Provide explanation letters for late payments
- Resolve judgment/lien before closing
- Provide payment plan documentation

### Refer to Underwriter

**Manual Underwrite Triggers**:
- Credit score below automated approval threshold
- Recent significant derogatory items
- High DTI requiring compensating factors
- Excessive inquiries or new accounts
- Payment history concerns
- Large number of collections

### Decline Recommendations

**Credit-Based Declines**:
- Credit score below program minimum
- Within waiting period for major derogatory
- Active bankruptcy (not Chapter 13 payment plan)
- Recent foreclosure within waiting period
- Unpaid federal tax lien without subordination
- Judgment that will attach to property

## Compensating Factors for Marginal Credit

**Strong Compensating Factors**:
- Large down payment (≥ 20%)
- Substantial reserves (≥ 12 months)
- Low DTI (< 30%)
- Stable employment (5+ years same employer)
- Income growth trajectory
- Minimal increase in housing payment

**Moderate Compensating Factors**:
- Down payment ≥ 10%
- Reserves ≥ 6 months
- DTI < 35%
- Stable employment (2+ years)

## Best Practices Summary

✓ **Use Middle Score**: Representative score following agency guidelines
✓ **Comprehensive Review**: Analyze all three bureaus for discrepancies
✓ **Payment History Focus**: Housing payment history most critical
✓ **Proper Debt Calculation**: Include all debts per guidelines
✓ **Document Decisions**: Clear rationale for all credit decisions
✓ **Fair Lending**: Consistent application of standards
✓ **Compensating Factors**: Consider whole picture, not just score
✓ **Dispute Resolution**: Address all disputed accounts before closing
✓ **Timing**: Re-pull credit if > 120 days old
✓ **Communication**: Explain required actions clearly to borrower

## Common Pitfalls to Avoid

✗ **Using Wrong Score**: Highest score or average instead of middle
✗ **Ignoring Derogatory Items**: Not addressing collections/judgments
✗ **Incomplete DTI**: Missing credit card payments or student loans
✗ **Active Disputes**: Attempting to close with disputed accounts
✗ **Expired Reports**: Using credit report > 120 days old
✗ **Inconsistent Treatment**: Different standards for similar situations
✗ **Unauthorized User Accounts**: Counting for credit but not obligation
✗ **Missing Explanations**: No letters for derogatory items
✗ **Overlooked Inquiries**: Not explaining excessive inquiries
✗ **Poor Documentation**: Insufficient rationale for credit decisions

---

**This skill ensures professional credit analysis that balances risk assessment with fair lending compliance, resulting in sound credit decisions and regulatory adherence.**
