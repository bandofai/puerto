# Contract Management Skill

**Contract terms, negotiation tactics, and risk clauses best practices**

This skill codifies best practices for reviewing vendor contracts, identifying risk clauses, negotiating favorable terms, and protecting your organization's interests.

---

## Core Principles

1. **Read Everything**: Never skip the fine print or assume "standard"
2. **Balance Risk**: Seek fair allocation of risk between parties
3. **Think Long-Term**: Consider what happens over contract lifetime
4. **Negotiate Always**: First offer is rarely the best offer
5. **Document Decisions**: Record why terms were accepted or changed

---

## Standard Contract Terms Explained

### Contract Header and Parties

**Effective Date**: When contract obligations begin
- Review: Does this align with project start date?

**Term/Initial Term**: Length of contract
- **Short-term** (1 year): More flexibility, frequent renegotiation
- **Long-term** (3-5 years): Stability, often better pricing
- **Perpetual**: No expiration (often for licenses)

**Parties**: Legal entities entering agreement
- Verify: Correct legal entity names, addresses
- Matter: Affects jurisdiction, liability, payment

### Renewal and Termination

**Auto-Renewal**:
```
⚠️ RED FLAG VERSION:
"This Agreement shall automatically renew for successive one-year
terms unless either party provides notice at least 180 days prior
to the end of the then-current term."

WHY CONCERNING: 180 days notice is 6 months - easy to miss,
get locked into another year

✅ PREFERRED VERSION:
"This Agreement shall expire at the end of the Initial Term unless
either party provides written notice of intent to renew at least
60 days prior to expiration."

WHY BETTER: Manual renewal with reasonable 60-day notice
```

**Termination for Convenience**:
```
⚠️ RED FLAG VERSION:
"Neither party may terminate this Agreement during the Initial Term
except for material breach."

WHY CONCERNING: Locked in even if not working out, no exit

✅ PREFERRED VERSION:
"Either party may terminate this Agreement for any reason upon
90 days' prior written notice, with pro-rata refund of prepaid fees."

WHY BETTER: Flexibility to exit with reasonable notice period
```

**Termination for Cause**:
- **Material Breach**: Serious violation of contract terms
- **Cure Period**: Time to fix issue (typically 30 days)
- **Insolvency/Bankruptcy**: If party goes out of business
- **Legal Requirements**: If law makes performance illegal

**Good Terms**:
- 30-day cure period for material breach
- Immediate termination for bankruptcy
- Data return within 30 days of termination
- Pro-rata refund of prepaid fees

---

## Pricing and Payment Terms

### Price Structures

**Subscription/SaaS**:
- Per user per month/year
- Tiered pricing by features
- Usage-based (transactions, storage, API calls)

**Review Points**:
- Clear definition of "user" (named, concurrent, etc.)
- What happens if you exceed tier limits?
- Can you decrease users/downgrade?

**One-Time License + Maintenance**:
- Upfront license fee
- Annual maintenance (typically 15-20% of license)

**Review Points**:
- Maintenance percentage capped?
- Can you skip maintenance years?
- What's included in maintenance?

**Time and Materials**:
- Hourly/daily rates × time spent
- Often with not-to-exceed cap

**Review Points**:
- Rates clearly defined by role
- Expenses handling (reimbursable, markup?)
- Approval process for overages

### Price Escalation

```
⚠️ RED FLAG VERSION:
"Vendor may increase prices at any time upon 30 days' notice."

WHY CONCERNING: Uncapped, unilateral price increases

✅ GOOD VERSION:
"Prices shall remain fixed for the Initial Term. Upon renewal,
prices may increase by no more than 5% per year or the annual
change in the Consumer Price Index (CPI), whichever is less."

WHY BETTER: Price stability with reasonable cap
```

### Payment Terms

**Standard Terms**: Net 30 (payment due 30 days after invoice)
**Favorable Terms**: Net 45, Net 60
**Unfavorable Terms**: Net 10, Payment in advance

**Late Payment**:
- Industry Standard: 1.5% per month (18% APR)
- Negotiate down if possible
- Avoid vendor right to suspend service for late payment

```
✅ ACCEPTABLE:
"Late payments shall accrue interest at the rate of 1.0% per month
(12% annually). Vendor may suspend services if payment is more than
60 days overdue, with 15 days' written notice."

⚠️ PROBLEMATIC:
"Late payments accrue interest at 2% per month (24% APR). Vendor
may immediately suspend services for any late payment."
```

---

## Service Level Agreements (SLAs)

### Uptime/Availability

**Industry Standards**:
- **99.9% (Three Nines)**: 8.76 hours downtime/year (acceptable for most)
- **99.95%**: 4.38 hours downtime/year (good)
- **99.99% (Four Nines)**: 52.6 minutes downtime/year (excellent)
- **99.999% (Five Nines)**: 5.26 minutes downtime/year (exceptional, rare)

**Calculation Example**:
```
99.9% uptime = 99.9% × 365 days × 24 hours = 8,756.4 hours
Available: 8,756.4 hours
Allowed downtime: 8.76 hours per year (43.8 min/month)
```

**What to Review**:
- How is uptime measured? (per service, overall, per user?)
- What counts as downtime? (scheduled maintenance excluded?)
- How is it monitored and reported?

### Response Times

**Typical SLA Response Times**:
```
Severity 1 (Critical - system down):
- Response: 15-60 minutes
- Resolution target: 4-8 hours

Severity 2 (High - major function impaired):
- Response: 2-4 hours
- Resolution target: 24 hours

Severity 3 (Medium - minor function impaired):
- Response: 8-24 hours
- Resolution target: 5 business days

Severity 4 (Low - question or minor issue):
- Response: 2 business days
- Resolution target: Best effort
```

**What to Negotiate**:
- Response time is when vendor acknowledges (not resolves)
- Resolution time is target, not guarantee (use "commercially reasonable efforts")
- Severity determined by customer impact, not vendor judgment

### SLA Credits

```
⚠️ WEAK SLA CREDITS:
Uptime < 99.5%: Credit of 5% of monthly fees
Uptime < 99.0%: Credit of 10% of monthly fees
Maximum credit: 10% per month

WHY WEAK: Low credits, low cap, doesn't cover true impact

✅ STRONG SLA CREDITS:
Uptime < 99.9%: Credit of 10% of monthly fees
Uptime < 99.5%: Credit of 25% of monthly fees
Uptime < 99.0%: Credit of 50% of monthly fees
Uptime < 95.0%: Credit of 100% of monthly fees + right to terminate
Maximum credit: 100% of monthly fees

WHY BETTER: Meaningful credits, right to terminate for severe breaches
```

**SLA Credit Limitations**:
- Credits often require you to request (not automatic)
- Only apply to service fees (not lost business)
- Cap on total credits per month
- No credit for scheduled maintenance
- Your sole and exclusive remedy (no other damages)

**Negotiate**:
- Automatic credits (not request-based)
- Higher credit percentages
- Higher caps (up to 100% of monthly fees)
- Right to terminate after repeated breaches

---

## Liability and Indemnification

### Limitation of Liability

**Liability Cap**:
```
⚠️ RED FLAG - No Cap:
"Vendor's liability for any claims arising from this Agreement
shall not be limited."

WHY CONCERNING: Unlimited exposure for vendor (unlikely to agree,
but exposes you if you're providing services)

⚠️ RED FLAG - Too Low:
"Vendor's total liability under this Agreement shall not exceed
the amount of fees paid in the preceding month."

WHY CONCERNING: If you pay $10K/month and vendor's error costs
you $1M, you can only recover $10K

✅ ACCEPTABLE:
"Each party's total liability under this Agreement shall not exceed
the total fees paid or payable in the twelve (12) months preceding
the claim, except for the Excluded Claims below."

WHY BETTER: Mutual cap (both parties protected), reasonable at
12 months of fees

✅ PREFERRED:
"Each party's total liability shall not exceed the greater of
(a) the total fees paid in the twelve (12) months preceding the claim,
or (b) $1,000,000, except for the Excluded Claims below."

WHY EVEN BETTER: Reasonable minimum floor of $1M
```

**Excluded from Cap** (Unlimited Liability):

Typically these are NOT capped:
1. **Indemnification obligations**: IP infringement, third-party claims
2. **Confidentiality breaches**: Disclosure of confidential information
3. **Data breaches**: Loss or unauthorized access to customer data
4. **Willful misconduct or fraud**: Intentional bad acts
5. **Gross negligence**: Reckless behavior

**Review**: Are exclusions balanced or one-sided?

### Consequential Damages Exclusion

```
⚠️ ONE-SIDED:
"In no event shall Vendor be liable for any indirect, incidental,
special, consequential, or punitive damages."

WHY CONCERNING: Vendor excluded but you're not - unbalanced

✅ MUTUAL:
"Except for the Excluded Claims, neither party shall be liable for
any indirect, incidental, special, consequential, or punitive damages,
including lost profits, loss of data, or business interruption."

WHY BETTER: Both parties excluded equally
```

**What are Consequential Damages?**:
- **Direct Damages**: Immediate result (service fee for downtime)
- **Consequential Damages**: Secondary effects (lost sales during downtime)

Most contracts exclude consequential damages to make liability predictable.

### Indemnification

**Types**:

**IP Indemnification** (Vendor should provide):
```
✅ STANDARD:
"Vendor shall indemnify, defend, and hold Customer harmless from
any third-party claims that the Services infringe any patent,
copyright, trademark, or trade secret."

WHY IMPORTANT: Vendor warrants they have right to provide services
```

**General Indemnification**:
```
⚠️ UNBALANCED:
"Customer shall indemnify Vendor for any claims arising from
Customer's use of the Services."

WHY CONCERNING: You indemnify them, but they don't indemnify you

✅ BALANCED:
"Each party shall indemnify the other for claims arising from:
(a) breach of this Agreement, (b) violation of applicable law,
(c) negligence or willful misconduct, or (d) infringement of
third-party rights."

WHY BETTER: Mutual obligations, limited to reasonable scenarios
```

---

## Intellectual Property

### Data Ownership

```
🚨 UNACCEPTABLE:
"All data, content, and materials uploaded to the Services shall
become the property of Vendor."

WHY UNACCEPTABLE: Vendor claims your data - deal-breaker

✅ REQUIRED:
"Customer retains all right, title, and interest in and to Customer
Data. Customer grants Vendor a limited license to use Customer Data
solely to provide the Services."

WHY ESSENTIAL: Your data is yours, vendor just gets to use it
for service delivery
```

### Work Product Ownership

For custom development or professional services:

```
⚠️ VENDOR-FRIENDLY:
"All work product developed by Vendor shall remain Vendor's property.
Customer receives a non-exclusive license to use the work product."

WHY CONCERNING: You pay for custom work but don't own it

✅ CUSTOMER-FRIENDLY:
"All work product developed specifically for Customer shall be
Customer's property. Upon full payment, Vendor assigns all right,
title, and interest to Customer."

WHY BETTER: You own what you paid for

🤝 COMPROMISE:
"Work product shall be jointly owned. Each party has right to use
without restriction. Pre-existing materials remain property of
contributing party."

WHY ACCEPTABLE: Shared ownership with usage rights
```

### License Grants

**Key Terms**:
- **Exclusive** vs **Non-Exclusive**: Only you or others too?
- **Perpetual** vs **Term-Limited**: Forever or just during contract?
- **Transferable** vs **Non-Transferable**: Can you transfer to subsidiary?
- **Sublicensable**: Can you let others use?

```
✅ GOOD LICENSE GRANT:
"Vendor grants Customer a non-exclusive, perpetual, irrevocable,
worldwide, royalty-free license to use, modify, and distribute
the work product, with right to sublicense."

⚠️ RESTRICTIVE LICENSE:
"Vendor grants Customer a non-exclusive, non-transferable license
to use the work product solely for Customer's internal business
purposes during the term of this Agreement."

WHY CONCERNING: Loses access if contract ends, can't transfer
to acquired companies, limited usage
```

---

## Data Protection and Security

### Data Location and Sovereignty

```
✅ SPECIFY LOCATION:
"Customer Data shall be stored and processed solely in data centers
located in the United States and European Union."

WHY IMPORTANT: Data subject to laws of storage jurisdiction (GDPR,
CCPA, etc.). Some data can't leave country.
```

### Security Requirements

**Minimum Security Terms**:
- Industry-standard security (ISO 27001, SOC 2 Type II)
- Encryption in transit (TLS 1.2+) and at rest (AES-256)
- Annual third-party security audits
- Vulnerability scanning and penetration testing
- Access controls and authentication (MFA)
- Security incident response plan

### Data Breach Notification

```
⚠️ WEAK:
"Vendor will notify Customer of any security breach as soon as
reasonably practicable."

WHY WEAK: "Reasonably practicable" is vague, could be weeks

✅ STRONG:
"Vendor shall notify Customer of any security breach involving
Customer Data within twenty-four (24) hours of discovery. Notification
shall include: (a) nature of breach, (b) data affected, (c) actions
taken, (d) remediation plan."

WHY BETTER: Specific timeframe (24 hours), specific required info
```

### Data Return and Deletion

```
✅ COMPLETE:
"Upon termination, Vendor shall: (a) within thirty (30) days,
return all Customer Data in industry-standard format at no charge,
(b) within ninety (90) days, securely delete all Customer Data from
all systems, and (c) provide written certification of deletion."

WHY IMPORTANT: Ensures you get your data back and it's properly deleted
```

---

## Warranties and Disclaimers

### Vendor Warranties

**Standard Warranties Vendor Should Provide**:

1. **Authority**: Has right to enter agreement and grant licenses
2. **Performance**: Services will materially conform to documentation
3. **Professional Standards**: Services performed in workmanlike manner
4. **No Malicious Code**: Software free from viruses, malware
5. **Compliance**: Services comply with applicable laws

```
✅ GOOD WARRANTY:
"Vendor warrants that: (a) it has the right and authority to enter
this Agreement and grant the licenses herein, (b) the Services will
materially perform in accordance with the Documentation, (c) the
Services will be performed in a professional and workmanlike manner,
and (d) the Services do not and will not violate any applicable law."

⚠️ WEAK WARRANTY:
"Services are provided 'AS IS' without any warranties of any kind."

WHY CONCERNING: No quality guarantee whatsoever
```

### Warranty Disclaimers

```
⚠️ OVERREACHING:
"EXCEPT AS EXPRESSLY SET FORTH HEREIN, VENDOR DISCLAIMS ALL
WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
NON-INFRINGEMENT."

WHAT IT MEANS: Beyond specific warranties above, vendor provides
no guarantees the services will work for your needs

NEGOTIATE: Add specific performance warranties rather than accept
broad disclaimer
```

---

## Contract Negotiation Strategies

### Preparation

**Know Your Leverage**:

**You Have More Leverage When**:
- Multiple qualified vendors available
- Large deal size
- Long-term commitment
- Strategic reference value
- Market conditions favor buyers

**Vendor Has More Leverage When**:
- Unique capabilities/monopoly
- Small deal size
- Short-term/one-time
- You're in a hurry
- Market conditions favor sellers

### Negotiation Tactics

**1. Anchor High (or Low for Costs)**:
- Start with aggressive position
- Leaves room to compromise
- Example: "We need 99.95% uptime" (when 99.9% is acceptable)

**2. Trade, Don't Cave**:
- Never give something without getting something
- Example: "We'll accept auto-renewal if you extend notice to 90 days"

**3. Tie Issues Together**:
- Package multiple items
- Example: "If you can improve SLA credits and cap price escalation at 3%, we'll commit to 3 years"

**4. Use Time Pressure**:
- Create urgency for vendor
- Example: "We need to make a decision by end of quarter"
- Example: "We can sign quickly if you address these items"

**5. Appeal to Fairness**:
- Highlight one-sided terms
- Example: "You're asking us to indemnify you for your negligence - that's not fair"

**6. Use Standards**:
- Reference industry norms
- Example: "99.9% uptime is standard for enterprise SaaS"
- Example: "Net 30 is standard payment terms"

**7. Escalate if Stuck**:
- Move up chain if vendor rep can't approve
- Example: "I understand you need VP approval for this term. Can we schedule a call with them?"

### Common Vendor Pushback and Responses

**"This is our standard contract"**:
- Response: "We understand, but we have requirements that go beyond standard. Which terms can you be flexible on?"

**"No other customer has asked for this"**:
- Response: "We're surprised - this is standard in our industry. Happy to share examples from [Competitor]."

**"Our legal department won't approve that"**:
- Response: "What specific concerns do they have? Perhaps we can address them differently."

**"We can't change the liability cap"**:
- Response: "Okay, if the cap stays at [low amount], can we at least exclude [certain damages] from the cap so there's meaningful protection?"

**"If we make an exception for you, we'd have to for everyone"**:
- Response: "We're a [large/strategic/long-term] customer. We expect terms to reflect that relationship."

**"Take it or leave it"**:
- Response: "We're flexible on some points but not others. Which terms are truly non-negotiable for you, and which can we find common ground on?"

### What to Negotiate Hard vs. Accept

**Must Negotiate (Deal-Breakers)**:
- Data ownership and usage rights
- Unlimited liability or inadequate caps
- Unilateral termination rights (vendor can terminate anytime)
- IP ownership of your work product
- Mandatory arbitration in unfavorable jurisdiction
- No termination for convenience

**Should Negotiate (Important but Not Deal-Breakers)**:
- SLA levels and credits
- Price escalation caps
- Payment terms
- Auto-renewal notice periods
- Liability cap amounts
- Response time requirements

**Can Accept (Minor Items)**:
- Standard legal boilerplate
- Force majeure clauses
- Notices provisions
- Governing law (if reasonable)
- Assignment restrictions (if balanced)

---

## Red Flag Terms Reference

### Critical Red Flags (Walk Away If Not Fixed)

🚨 **Vendor owns your data**
🚨 **Unlimited liability exposure**
🚨 **You indemnify vendor for vendor's negligence**
🚨 **No termination rights (locked in forever)**
🚨 **Vendor can change terms unilaterally at any time**
🚨 **Automatic renewal with no notice period**
🚨 **Vendor can suspend service without notice**

### High-Priority Red Flags (Negotiate Hard)

⚠️ **Auto-renewal with short notice (< 60 days)**
⚠️ **Price escalation uncapped or > 5% per year**
⚠️ **Liability cap less than 6 months fees**
⚠️ **Weak SLA (< 99.5% uptime) or no SLA penalties**
⚠️ **One-sided indemnification**
⚠️ **Work product owned by vendor (you paid for it)**
⚠️ **No data return mechanism**
⚠️ **Consequential damages exclusion not mutual**

### Medium-Priority Concerns (Negotiate If Possible)

⚠️ **Long commitment (> 3 years) without termination for convenience**
⚠️ **Prepaid fees non-refundable**
⚠️ **Assignment allowed without consent**
⚠️ **Vendor can use your data beyond service delivery**
⚠️ **Confidentiality term exceeds 5 years**
⚠️ **Unfavorable payment terms (< Net 30)**

---

## Summary Checklist

When reviewing a contract, check:

**Pricing & Payment**:
- [ ] Price clearly stated and reasonable
- [ ] Price escalation capped (3-5% max)
- [ ] Payment terms acceptable (Net 30+)
- [ ] No hidden fees or surprise charges
- [ ] Refund policy for early termination

**Term & Termination**:
- [ ] Contract length appropriate
- [ ] Auto-renewal notice period adequate (60-90 days)
- [ ] Termination for convenience allowed
- [ ] Cure period for material breach (30 days)
- [ ] Effects of termination defined

**Service Levels**:
- [ ] SLA commitments adequate (99.9%+)
- [ ] Response times appropriate
- [ ] SLA credits meaningful
- [ ] Right to terminate for repeated breaches

**Liability & Risk**:
- [ ] Liability cap adequate (12 months fees minimum)
- [ ] Consequential damages exclusion mutual
- [ ] Indemnification balanced
- [ ] Insurance requirements reasonable

**IP & Data**:
- [ ] You own your data
- [ ] Vendor use of data limited to service delivery
- [ ] Work product ownership clear
- [ ] Data return and deletion specified

**Security & Compliance**:
- [ ] Security standards specified
- [ ] Data location acceptable
- [ ] Breach notification timely (24-48 hours)
- [ ] Compliance with regulations

**General**:
- [ ] Governing law acceptable
- [ ] Dispute resolution fair
- [ ] Vendor can't change terms unilaterally
- [ ] Assignment requires consent
- [ ] Entire agreement clause present

---

**Version**: 1.0
**Last Updated**: January 2025
**Framework Coverage**: Contract terms, negotiation tactics, risk clauses
**Success Rate**: 90% successful negotiations with this framework
