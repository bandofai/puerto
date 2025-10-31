# Compliance Validation Skill

Professional standards for mortgage regulatory compliance validation, covering TRID, RESPA, TILA, QM/ATR, and fair lending requirements.

## Purpose

This skill provides standardized frameworks for:
- TRID disclosure timing and content validation
- RESPA compliance verification
- TILA accuracy testing
- Qualified Mortgage (QM) and Ability-to-Repay (ATR) determination
- Fair lending compliance review
- Risk-based compliance assessment

## Core Concepts

### 1. TRID Compliance Framework

#### Timeline Validation

**Loan Estimate (LE) - 3 Business Day Rule**:

Business Days = All days except Sundays and federal holidays

**Key Deadlines**:
1. **Application Date**: When all 6 pieces received (name, income, SSN, property address, value, loan amount)
2. **LE Due**: Within 3 business days of application
3. **LE Delivery**:
   - Hand delivery: Received same day
   - Mail: Add 3 business days for presumed receipt
   - Email: Received same day (if borrower consents to electronic)

**Example Calculation**:
```
Application: Monday, January 3
Business Day 1: Tuesday, January 4
Business Day 2: Wednesday, January 5
Business Day 3: Thursday, January 6
LE Must be Delivered/Mailed by: Thursday, January 6

If mailed Thursday, presumed received: Sunday + 3 days = Wednesday, January 12
```

**Closing Disclosure (CD) - 3 Business Day Rule**:

Business Days = All days except Sundays and federal holidays

**Key Deadlines**:
1. **CD Delivery**: At least 3 business days before consummation
2. **Consummation**: When borrower becomes contractually obligated (typically signing date)
3. **Delivery Methods**: Same as LE

**Example Calculation**:
```
Consummation (Signing): Friday, January 20
Count back 3 business days:
Business Day 3: Thursday, January 19
Business Day 2: Wednesday, January 18
Business Day 1: Tuesday, January 17
CD Must be Delivered/Mailed by: Tuesday, January 17

If mailed Tuesday, presumed received: Friday, January 20 (too late!)
Must mail by: Saturday, January 14 (presumed received Tuesday, January 17)
```

#### Changed Circumstances

**Valid Changed Circumstances**:

1. **Information Changes**: Facts relied upon change or were inaccurate
   - Income different than stated
   - Property value differs from estimate
   - Title issues discovered

2. **Eligibility Changes**: Borrower no longer qualifies for product
   - Credit score dropped
   - Debt increased
   - Property type changed

3. **Borrower-Requested Changes**: Borrower asks for different loan
   - Rate lock request
   - Loan amount change
   - Product change

4. **Rate Lock**: Rate lock may trigger revised LE if rate-dependent fees change

5. **Expiration**: LE valid 10 business days, can revise if expires

6. **Construction Delays**: Construction loans only

**Revised LE Timeline**:
- Must provide within 3 business days of receiving information about changed circumstance
- Borrower must receive before or at consummation
- Can issue multiple revised LEs

**Resetting 3-Day Waiting Period**:

CD must be re-disclosed (new 3-day wait) if:
1. **APR increases > 1/8% (0.125%)** for regular transactions
2. **APR increases > 1/4% (0.25%)** for irregular transactions (variable rate, graduated payment, balloon)
3. **Loan product changes** (e.g., fixed to ARM)
4. **Prepayment penalty added** when not previously disclosed

Changes that DON'T reset waiting period:
- APR decreases
- Fees increase (within tolerance)
- Minor changes to closing costs
- Clerical corrections

### 2. Fee Tolerance Testing

#### Zero Tolerance Items (No Increase Allowed)

**Cannot Increase from LE to CD**:
1. Lender's origination charges
2. Credit or charge for specific interest rate (discount points)
3. Transfer taxes

**If these increase**: Lender must cure by reducing other charges or refunding at/before closing

#### 10% Cumulative Tolerance

**Can increase up to 10% cumulatively**:
1. Recording fees
2. Services borrower can shop for (if borrower selects from lender's list)
3. Third-party services borrower cannot shop for

**Calculation**:
```
LE Total (Category): $1,500
CD Total (Category): $1,700
Variance: $200
Tolerance: $1,500 × 10% = $150
Overage: $200 - $150 = $50

Cure Required: $50 (lender must refund or reduce other fees)
```

#### Unlimited Tolerance

**Can increase without limit if valid changed circumstance**:
- Must document changed circumstance
- Must issue revised LE
- Borrower must receive revised LE

**Changed Circumstances Examples**:
- Title company finds additional lien (title fee increases)
- Property inspection reveals need for additional survey
- Natural disaster affects property (increased insurance)

### 3. APR Accuracy Standards

#### APR Components

**Included in APR Calculation**:
- Interest on the loan
- Loan origination fees
- Discount points
- Mortgage insurance (BPMI, MIP, funding fee)
- Prepaid interest
- Loan-level price adjustments

**Excluded from APR**:
- Appraisal fee (if borrower can choose provider)
- Credit report fee
- Title charges (if borrower can choose)
- Recording fees
- Property taxes
- Homeowners insurance
- HOA dues
- Pest inspection

#### APR Accuracy Tolerance

**Regular Transaction**:
- APR must be within ± 0.125% (1/8%) of actual APR
- Example: If actual APR is 4.500%, disclosed must be 4.375% - 4.625%

**Irregular Transaction** (variable rate, graduated payment, balloon, step rate):
- APR must be within ± 0.25% (1/4%) of actual APR

**Non-Compliance**:
- APR outside tolerance = regulatory violation
- May require re-disclosure and resetting waiting period
- Potential penalties to lender

### 4. Qualified Mortgage (QM) Determination

#### Product Features Test

**QM Requirements** (must meet ALL):
1. **Loan term ≤ 30 years**: No loans > 360 months
2. **No negative amortization**: Payment must cover at least interest
3. **No interest-only period**: Payment must include principal
4. **No balloon payment**: Except small creditor exception
5. **Points and fees ≤ 3%**: Subject to loan amount thresholds

#### Points and Fees Test

**Items Included**:
- Origination charges (points, fees)
- Real estate-related fees retained by lender or affiliate
- Premiums for credit life or debt cancellation insurance

**Items Excluded**:
- Bona fide discount points (if rate reduction ≥ 1% per point and typical for market)
- Fees for actual services (appraisal, credit report) if reasonable
- Up to 2 bona fide discount points (if certain conditions met)

**Thresholds** (2024):
- Loan ≥ $132,304: 3%
- Loan ≥ $79,382 to < $132,304: $3,969
- Loan ≥ $26,461 to < $79,382: 5%
- Loan ≥ $15,877 to < $26,461: $1,323
- Loan < $15,877: 8%

**Example**:
```
Loan Amount: $300,000
Origination Fee: $5,000
Discount Points: $3,000
Affiliate Title Fee: $500
Total Points & Fees: $8,500

Threshold: $300,000 × 3% = $9,000
$8,500 < $9,000 ✓ PASSES

Percentage: $8,500 / $300,000 = 2.83% ✓ PASSES
```

#### QM Categories

**1. Safe Harbor QM**:
- Meets product features test
- Points & fees within limit
- **APR < APOR + 1.5%** (first lien) or APOR + 3.5% (subordinate lien)
- Conclusive presumption of ATR compliance

**2. Rebuttable Presumption QM**:
- Meets product features test
- Points & fees within limit
- **APR < APOR + 3.5%** (first lien) or APOR + 6.5% (subordinate lien)
- Presumption of ATR, but rebuttable

**3. Agency QM**:
- Eligible for purchase by Fannie Mae or Freddie Mac
- Automatically receives QM status
- Must meet GSE underwriting standards

**4. Small Creditor QM**:
- Special rules for small lenders
- Can have balloon payments
- DTI ≤ 43% or meet other requirements

#### APOR (Average Prime Offer Rate)

**Published**: By FFIEC weekly
**Used**: To determine QM Safe Harbor vs Rebuttable Presumption
**Varies by**: Loan term, lien position, lock period

**Example**:
```
Loan APR: 5.250%
APOR (for that week, term, lien): 4.500%
Spread: 5.250% - 4.500% = 0.750%

Safe Harbor threshold: APOR + 1.5% = 6.000%
5.250% < 6.000% ✓ SAFE HARBOR QM
```

### 5. Ability-to-Repay (ATR) Requirements

#### 8 Underwriting Factors

**Must Consider and Document**:

1. **Current or Reasonably Expected Income/Assets**:
   - Income verification (W-2, pay stubs, tax returns)
   - Asset verification (bank statements)
   - Employment verification

2. **Current Employment Status**:
   - VOE or pay stubs
   - Self-employed: Business documents

3. **Monthly Payment on Loan**:
   - Principal and interest
   - Full PITIA calculation

4. **Monthly Payment on Simultaneous Loans**:
   - HELOC, second mortgage
   - Include in DTI

5. **Monthly Payments for Mortgage-Related Obligations**:
   - Property taxes
   - Insurance
   - HOA dues
   - PMI/MIP

6. **Current Debt Obligations**:
   - All debts from credit report
   - Alimony/child support
   - Include in DTI calculation

7. **DTI Ratio or Residual Income**:
   - Calculate and document DTI
   - VA loans: Residual income

8. **Credit History**:
   - Credit report obtained
   - Credit analysis performed
   - Risk assessment documented

**Documentation Standard**:
- Each factor must be verified
- Documentation must be in loan file
- Cannot rely on borrower statement alone

### 6. RESPA Compliance

#### Section 8: Kickbacks and Unearned Fees

**Prohibited**:
- Kickbacks for referrals
- Fee splitting for services not performed
- Unearned fees

**Red Flags**:
- Unusually high fees
- Services not actually provided
- Marketing payments to referral sources
- Yield spread premiums (outdated, but monitor)

**Permitted**:
- Payments for actual services rendered
- Bona fide employee compensation
- Payments for goods/facilities provided

#### Affiliated Business Arrangements (AfBA)

**Required Disclosure**:
- At or before time of referral
- Description of relationship
- Estimate of charges
- Statement that borrower not required to use
- Borrower signature

**AfBA Example**:
```
Lender refers to title company
Lender owns 25% of title company
Must provide AfBA disclosure
Borrower must have choice to use different title company
```

#### Section 9: Seller-Required Title Insurance

**Prohibited**: Seller cannot require buyer to use specific title company

**Exception**: Seller can pay for title insurance from company of seller's choice

**Disclosure**: Must be disclosed on LE/CD if seller requires

#### Section 10: Escrow Account Limitations

**Cushion Limit**: Maximum 2 months (1/6 annual charges)

**Example**:
```
Annual Property Taxes: $3,600
Annual Insurance: $1,200
Total Annual: $4,800

Monthly Escrow: $4,800 / 12 = $400
Maximum Cushion: $4,800 / 6 = $800

Cannot collect more than $800 cushion at closing
```

### 7. Fair Lending Compliance

#### ECOA (Equal Credit Opportunity Act)

**Prohibited Basis**:
- Race, color, religion, national origin
- Sex (including gender identity, sexual orientation)
- Marital status
- Age (unless favorable)
- Source of income (public assistance)

**Required**:
- Consistent underwriting standards
- Objective criteria for decisions
- Adverse action notices (30 days)
- Specific reasons for denial

#### Disparate Treatment

**Prohibited**: Treating applicants differently based on prohibited basis

**Examples**:
- Different underwriting standards by race
- Steering protected class to certain products
- Different pricing not based on risk factors

**Compliance**: Apply same standards to all applicants

#### Disparate Impact

**Definition**: Neutral policy that has disproportionate adverse impact on protected class

**Test**:
1. Does policy have disparate impact?
2. Is there business necessity?
3. Is there less discriminatory alternative?

**Example**:
```
Policy: Minimum credit score 680
Impact: Disproportionately affects certain groups
Business Necessity: Required for risk management
Alternative: Consider compensating factors, not just score
```

### 8. Compliance Risk Assessment Framework

#### Risk Rating System

**Critical Issues** (STOP - Cannot Close):
- TRID timing violations
- APR accuracy errors outside tolerance
- Fee tolerance violations (uncured)
- Missing required disclosures
- Non-QM without proper ATR documentation
- Fair lending violations

**High-Priority Issues** (Must Cure Before Closing):
- Documentation gaps in ATR factors
- AfBA disclosure missing
- Escrow calculation errors
- Program requirement violations (FHA, VA, USDA)
- Missing borrower signatures

**Medium-Priority Issues** (Should Cure):
- Minor disclosure inconsistencies
- Formatting errors
- Missing optional documentation
- Late arrival of documents

**Low-Priority Issues** (Note for File):
- Clerical errors that don't affect compliance
- Minor date discrepancies
- Extra documentation provided

#### Compliance Validation Checklist

**TRID Review**:
- [ ] Application date documented
- [ ] LE sent within 3 business days
- [ ] LE received (documented)
- [ ] Intent to proceed received
- [ ] Changed circumstances documented
- [ ] Revised LE sent timely (if applicable)
- [ ] CD sent 3 business days before consummation
- [ ] CD received (documented)
- [ ] No changes requiring new waiting period
- [ ] All tolerance tests passed

**Fee Tolerance Review**:
- [ ] Zero tolerance items unchanged
- [ ] 10% tolerance items within limit
- [ ] Cures processed (if needed)
- [ ] Unlimited tolerance items documented

**APR Review**:
- [ ] APR calculated correctly
- [ ] APR within tolerance
- [ ] Finance charge accurate
- [ ] Amount financed correct

**QM/ATR Review**:
- [ ] Product features compliant
- [ ] Points & fees within limit
- [ ] All 8 ATR factors documented
- [ ] QM status determined
- [ ] Proper disclosures provided

**RESPA Review**:
- [ ] AfBA disclosure (if applicable)
- [ ] No kickback arrangements
- [ ] Escrow within limits
- [ ] Servicing disclosure provided

**Fair Lending Review**:
- [ ] Consistent standards applied
- [ ] No prohibited basis in decision
- [ ] Adverse action notice (if applicable)
- [ ] Documentation supports decision

## Best Practices Summary

✓ **Business Day Tracking**: Use calendar to count TRID business days accurately
✓ **Document Everything**: TRID compliance requires complete documentation trail
✓ **Test All Tolerances**: Zero, 10%, and unlimited categories
✓ **APR Precision**: Must be within tolerance, no exceptions
✓ **Complete ATR**: All 8 factors must be documented
✓ **QM Determination**: Know which category and document
✓ **Fair Lending**: Consistent treatment and objective criteria
✓ **Independent Review**: Compliance should be separate from production
✓ **Cure Promptly**: Address violations before closing
✓ **Stay Current**: Regulations change, update procedures regularly

## Common Pitfalls to Avoid

✗ **Counting Sundays**: Sundays are not business days for TRID
✗ **Mail Timing**: Forgetting to add 3 days for presumed receipt
✗ **Changed Circumstances**: Not documenting or issuing revised LE
✗ **Fee Tolerance**: Not testing all categories or missing cures
✗ **APR Errors**: Miscalculating or being outside tolerance
✗ **Missing ATR Factors**: Incomplete documentation of 8 factors
✗ **QM Assumption**: Assuming QM without testing points & fees
✗ **AfBA Omission**: Not disclosing affiliated relationships
✗ **Inconsistent Standards**: Different treatment of similar borrowers
✗ **Late Compliance Review**: Waiting until day before closing

---

**This skill ensures comprehensive regulatory compliance, protecting both lender and borrower while avoiding costly violations and penalties.**
