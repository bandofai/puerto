# Compliance Reporting Skill

Expert knowledge for AML compliance, SAR generation, and regulatory reporting per FinCEN, BSA, and USA PATRIOT Act requirements.

## SAR Filing Requirements

### When to File SAR

**Dollar Thresholds** (31 CFR § 1020.320):
- Insider abuse: ANY amount
- Other crimes: ≥$5,000
- Structuring: ≥$5,000
- Money laundering: ≥$5,000
- Unknown perpetrator: ≥$25,000

**Federal Crimes Requiring SAR**:
- Wire fraud
- Identity theft
- Account takeover
- Credit/debit card fraud
- ACH fraud
- Check fraud
- Money laundering
- Structuring (31 U.S.C. § 5324)
- Terrorist financing
- Elder financial exploitation

### SAR Timeline

**30 Calendar Days**: From detection to filing
**Detection Date**: When institution first becomes aware of suspicious activity

```python
# Filing deadline calculation
filing_deadline = detection_date + timedelta(days=30)
# Must file by 11:59 PM ET on 30th day
```

**Best Practice**: File within 15-20 days

---

## FinCEN Form 111 Structure

### Part I: Subject Information

**Individual**:
- Full name (Last, First, Middle)
- SSN or ITIN
- Date of birth (MM/DD/YYYY)
- Address (street, city, state, ZIP)
- Phone number
- Email address
- Occupation
- Identification type (Driver's License, Passport, State ID)
- Identification number
- Issuing state or country

**Entity**:
- Legal name
- DBA name (if different)
- EIN
- State of formation
- Business type
- Address
- Phone
- Website

**Note**: Customer may be VICTIM, not perpetrator. Clearly identify which.

---

### Part II: Suspicious Activity Information

**Activity Types** (Check all that apply):
- ☐ Structuring
- ☐ Terrorist financing
- ☐ Identity theft
- ☐ Check fraud
- ☐ Credit card fraud
- ☐ Debit card fraud
- ☐ Wire transfer fraud
- ☐ ACH fraud
- ☐ Money laundering
- ☐ Mortgage loan fraud
- ☐ Consumer loan fraud
- ☐ Other (specify)

**Financial Details**:
- Total dollar amount involved
- Loss amount (if fraud)
- Recovery amount
- Currency type

**Account Information**:
- Account number (last 4 digits for customer protection)
- Account type
- Account open date
- Current balance

**Transaction Summary**:
- Number of transactions
- Date range
- Total transaction amount
- Transaction types

---

### Part III: Institution Information

**Required**:
- Institution legal name
- Institution type (bank, credit union, MSB)
- EIN
- RSSD ID (if applicable)
- Address
- Primary federal regulator (OCC, FDIC, FRB, NCUA, FinCEN)

---

### Part IV: Contact Information

**Primary Contact** (required):
- Name
- Title
- Phone
- Email

**Alternate Contact** (recommended):
- Name
- Title
- Phone
- Email

---

### Part V: Narrative

**Most Critical Section** - Tell the complete story

**Required Elements**:

1. **Background** (1-2 paragraphs):
   - How account/relationship established
   - Normal account activity baseline
   - Customer profile

2. **Detection** (1 paragraph):
   - How suspicious activity identified
   - Detection method (automated system, analyst review, customer report)
   - Date/time of detection

3. **Detailed Description** (3-5 paragraphs):
   - Chronological account of ALL suspicious transactions
   - Specific dates, times, amounts, locations
   - Merchant names and categories
   - Transaction types
   - Device/IP information (if relevant)

4. **Why Suspicious** (2-3 paragraphs):
   - Specific red flag indicators
   - Deviations from customer's normal behavior
   - Pattern matching to known fraud typologies
   - Statistical anomalies
   - Comparison to peer group

5. **Actions Taken** (1-2 paragraphs):
   - Card/account blocked
   - Customer contacted
   - Investigation conducted
   - Disputes filed
   - Recovery efforts
   - Law enforcement contacted (if applicable)

6. **Supporting Documentation** (list):
   - Transaction records
   - Customer communications
   - Investigation reports
   - Related SAR references

---

## Narrative Writing Standards

### Do's

✅ **Be Factual**: Stick to verifiable facts only
✅ **Be Specific**: Include dates, amounts, locations, names
✅ **Be Chronological**: Present events in timeline order
✅ **Be Comprehensive**: Include all relevant details
✅ **Be Clear**: Write for law enforcement to understand
✅ **Be Professional**: Business tone, proper grammar
✅ **Explain Red Flags**: Don't just list, explain why suspicious

### Don'ts

❌ **No Speculation**: Don't guess or assume
❌ **No Opinions**: Don't judge or editorialize
❌ **No Vague Statements**: "Unusual activity" is not enough
❌ **No Tipping Off**: Don't reference that SAR was filed
❌ **No Legal Conclusions**: Don't say "guilty" or "innocent"
❌ **No Incomplete Info**: Don't leave gaps in timeline
❌ **No Technical Jargon**: Make it understandable

### Narrative Examples

**GOOD Narrative**:
```
On January 20, 2025, our automated fraud monitoring system detected
15 debit card transactions totaling $45,000 within an 8-minute period
(8:30 AM - 8:38 AM) on customer account XXXXX-6789. This represented
a 2,172% increase from the customer's 90-day average daily spending
of $201.25.

The transactions occurred at 15 different merchants in Los Angeles,
California: 5 electronics stores, 6 jewelry stores, and 4 luxury
goods retailers. Transaction amounts progressively increased: $100,
$500, $1,000, $2,000, $5,000 (×3), $3,000 (×2), $4,000 (×2).

This activity is suspicious because:
1. The customer's last prior transaction occurred 2 hours earlier in
   New York City, 2,451 miles away, making physical travel impossible.
2. The 15-transaction velocity exceeds the customer's baseline by 652%.
3. All 15 merchants were new to the customer (no prior transaction history).
4. The merchant categories (electronics, jewelry, luxury goods) deviated
   completely from the customer's typical spending pattern (groceries
   40%, gas 25%, dining 20%).
5. The transaction device was a new Android device, whereas the customer
   exclusively used an iPhone 12 for the prior 6 months.

We contacted the customer at 10:20 AM via SMS and email. The customer
returned our call at 11:15 AM and confirmed they did not authorize any
of the 15 transactions. The customer stated they were at work in New
York during the Los Angeles transactions and their debit card was in
their physical possession. We immediately blocked the card and filed
disputes with all 15 merchants.

We believe the customer's debit card credentials were compromised,
likely through a phishing attack. The perpetrator then used a cloned
card or stolen card details to conduct card-present transactions in
Los Angeles.
```

**BAD Narrative**:
```
Customer had unusual activity. Many transactions in short time.
Looks like fraud. We blocked the card.
```
(❌ Vague, lacks specifics, no timeline, no details, no red flags explained)

---

## Regulatory Framework

### Bank Secrecy Act (BSA)

**31 U.S.C. § 5311 et seq.**

**Key Requirements**:
- SAR filing for suspicious activity ≥$5,000
- Recordkeeping: 5 years from filing date
- Confidentiality: Mandatory, violations punishable
- Customer Identification Program (CIP)
- Customer Due Diligence (CDD)

**Penalties for Non-Compliance**:
- Civil: Up to $100,000 per violation
- Criminal: Up to $250,000 and/or 5 years imprisonment

---

### USA PATRIOT Act

**Sections Relevant to SARs**:

**Section 314(a)**: FinCEN Information Requests
- Respond within 14 days to FinCEN requests
- Search records for individuals/entities
- Report matches

**Section 314(b)**: Information Sharing
- Share SARs with other institutions (with safeguards)
- Liability protection for good-faith sharing

**Section 356**: Enhanced SAR Requirements
- Expanded reporting obligations
- Increased penalties for violations

---

### FinCEN Regulations

**31 CFR § 1020.320**: SAR Filing Requirements

**Key Points**:
- Must file within 30 calendar days
- Use FinCEN Form 111 (Suspicious Activity Report)
- File electronically via BSA E-Filing System
- Maintain copy for 5 years
- Do NOT notify subject

**BSA E-Filing System**:
- Create FinCEN account
- Submit SAR electronically
- Receive acknowledgment with BSA ID
- BSA ID for tracking and correspondence

---

### Confidentiality Requirements

**31 U.S.C. § 5318(g)(2)**: SAR Confidentiality

**PROHIBITED Disclosures**:
- ❌ Subject of SAR (customer or suspect)
- ❌ Subject's attorney
- ❌ Media/press
- ❌ General public
- ❌ Anyone without "need to know"

**PERMITTED Disclosures**:
- ✅ FinCEN
- ✅ Federal law enforcement (upon request)
- ✅ Federal functional regulator (OCC, FDIC, FRB, etc.)
- ✅ Self-regulatory organization (FINRA, etc.)
- ✅ Within institution (need-to-know basis only)
- ✅ Other financial institutions (under 314(b) with protections)

**"Tipping Off" Prohibition**:
- Cannot notify subject that SAR was filed
- Cannot say "we had to file a SAR about this"
- Violation is serious federal offense

**Penalties for Violation**:
- Civil: Up to $100,000 per violation
- Criminal: Up to $250,000 fine and/or 5 years imprisonment
- Institution reputation damage
- Regulatory enforcement action

---

## SAR Quality Validation Checklist

### Completeness Check

**Part I - Subject Information**:
- ✅ Full legal name
- ✅ SSN/EIN (if known)
- ✅ Date of birth (individual) or formation date (entity)
- ✅ Complete address
- ✅ Phone number (if available)
- ✅ Identification details

**Part II - Activity Information**:
- ✅ Activity type(s) checked
- ✅ Dollar amounts accurate and verified
- ✅ Account information complete
- ✅ Transaction details specific

**Part III - Institution Information**:
- ✅ All fields complete
- ✅ Regulatory identifiers correct
- ✅ Contact information current

**Part IV - Contact Information**:
- ✅ Primary contact complete
- ✅ Alternate contact provided (recommended)

**Part V - Narrative**:
- ✅ Background section present
- ✅ Detection method described
- ✅ Detailed chronological description
- ✅ Red flags explicitly explained
- ✅ Actions taken documented
- ✅ Supporting documentation listed

### Quality Check

**Narrative Standards**:
- ✅ Factual (no speculation or assumptions)
- ✅ Specific (dates, amounts, locations, names)
- ✅ Chronological (events in order)
- ✅ Comprehensive (all relevant details)
- ✅ Clear (law enforcement can understand)
- ✅ Professional (proper grammar, business tone)
- ✅ Explanatory (red flags explained, not just listed)

**Accuracy Verification**:
- ✅ All dollar amounts verified against records
- ✅ All dates/times accurate
- ✅ All names spelled correctly
- ✅ All locations verified
- ✅ Transaction counts accurate
- ✅ Account numbers correct (last 4 digits for security)

**Regulatory Compliance**:
- ✅ Filed within 30-day deadline
- ✅ $5,000 threshold met (or other applicable threshold)
- ✅ Suspicious activity type clearly identified
- ✅ No "tipping off" language
- ✅ Supporting documentation attached or referenced

**Internal Review**:
- ✅ Reviewed by senior compliance officer
- ✅ Legal review (if high-risk case)
- ✅ Approved for filing by authorized signatory
- ✅ Audit trail documented

---

## Post-Filing Requirements

### Retention

**5-Year Retention** (31 CFR § 1020.320(d)):
- Original SAR
- Supporting documentation
- All evidence referenced in SAR
- Internal review notes
- Filing confirmation (BSA ID)

**Storage Requirements**:
- Secure location
- Limited access (need-to-know only)
- Searchable for future reference
- Protected from unauthorized disclosure

### Ongoing Monitoring

**FinCEN May**:
- Request additional information (respond within timeframe specified)
- Ask clarifying questions
- Request supplemental documentation

**Law Enforcement May**:
- Request complete case file
- Interview institution personnel
- Subpoena records
- Initiate investigation

**Institution Must**:
- Cooperate fully with FinCEN and law enforcement
- Respond promptly to information requests
- Maintain confidentiality
- Document all regulatory interactions

### Supplemental SARs

**File Supplemental SAR if**:
- New information discovered about same activity
- Additional transactions identified
- Perpetrator identified (if previously unknown)
- Activity continues after initial SAR

**Reference Original SAR**:
- Include original BSA ID
- Explain relationship to original SAR
- Provide new information only (don't repeat original)

---

## Common SAR Scenarios

### Identity Theft

**SAR Triggers**:
- Account opened with stolen identity
- Unauthorized transactions on existing account
- Synthetic identity fraud
- Tax refund fraud

**Key Information to Include**:
- How identity theft discovered
- Victim information (if different from account holder)
- Perpetrator information (if known)
- Fraudulent transactions timeline
- Customer verification of non-authorization

---

### Structuring

**SAR Triggers**:
- Multiple transactions $9,000-$9,999
- Pattern of just-below-threshold amounts
- Multiple locations/branches
- Deliberate avoidance of CTR ($10,000 reporting)

**Key Information to Include**:
- Specific amounts and dates of each transaction
- Locations/branches used
- Pattern description (why it appears deliberate)
- Customer statements (if asked about large cash needs)
- Total amount structured

---

### Money Laundering

**SAR Triggers**:
- Rapid in/out movement of funds
- No apparent business purpose
- Layering transactions
- Trade-based money laundering
- Use of shell companies
- High-risk jurisdictions

**Key Information to Include**:
- Complete transaction flow (in → through → out)
- Lack of economic purpose
- Source and destination of funds
- Layering techniques observed
- Red flags for money laundering

---

### Account Takeover

**SAR Triggers**:
- Unauthorized access to legitimate account
- Device/location changes + unusual transactions
- Password resets + immediate fraud
- Customer denies transactions

**Key Information to Include**:
- How account was compromised (if known)
- Timeline of takeover indicators
- Unauthorized transactions
- Customer verification obtained
- Fraud recovery actions

---

## Summary

**This skill provides**:
- Complete SAR filing requirements and thresholds
- FinCEN Form 111 structure (Parts I-V)
- Narrative writing standards (do's and don'ts)
- Regulatory framework (BSA, PATRIOT Act, FinCEN)
- Confidentiality requirements and penalties
- Quality validation checklist
- Post-filing requirements (retention, monitoring)
- Common SAR scenarios and examples

**Use this skill to**:
- Determine when SAR filing required
- Generate complete, compliant SARs
- Write high-quality narratives
- Ensure regulatory compliance
- Maintain SAR confidentiality
- Meet retention requirements
- Support law enforcement investigations

**Remember**: SARs are critical tools for law enforcement. Quality SARs with detailed narratives enable investigations that prevent and prosecute financial crimes. Maintain strict confidentiality to protect investigation integrity and comply with federal law.
