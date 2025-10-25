# Complaint Resolution Skill

Comprehensive patterns and frameworks for managing consumer complaints, warranty claims, and legal escalations.

## Data Structure Standards

### Complaint Case Schema

```json
{
  "id": "uuid-v4",
  "case_number": "ABC-2025-001",
  "status": "open|escalated|resolved|abandoned",
  "company": {
    "name": "Company Name",
    "contact_info": {
      "phone": "1-800-555-1234",
      "email": "support@company.com",
      "address": "123 Main St, City, ST 12345"
    },
    "website": "https://company.com"
  },
  "issue": {
    "category": "defective_product|service_failure|billing_dispute|false_advertising",
    "product": "Product Name/Model",
    "description": "Detailed issue description",
    "purchase_date": "2025-01-15",
    "purchase_price": 799.99,
    "receipt_number": "REC-12345"
  },
  "timeline": [
    {
      "date": "2025-03-15T10:00:00Z",
      "type": "issue_occurred|phone_call|email|letter|status_change",
      "description": "Event description",
      "contact": "Contact name (if applicable)",
      "ticket_number": "Ticket/case number (if applicable)"
    }
  ],
  "escalation_path": {
    "current_level": "initial|csr|supervisor|manager|corporate|bbb|legal",
    "levels_attempted": ["csr", "supervisor"],
    "next_steps": ["manager", "corporate", "bbb", "legal"]
  },
  "resolution": {
    "desired_outcome": "Full refund|Replacement|Repair|Compensation",
    "deadline": "2025-04-15T00:00:00Z",
    "actual_outcome": "Outcome description (when resolved)",
    "resolved_date": "2025-04-01T00:00:00Z",
    "amount_recovered": 799.99
  },
  "legal": {
    "small_claims_eligible": true,
    "claim_amount": 799.99,
    "statute_of_limitations": "2029-01-15T00:00:00Z",
    "consumer_protection_violations": ["warranty_breach", "deceptive_practices"]
  },
  "notes": "Additional case notes",
  "created": "2025-03-16T15:00:00Z",
  "last_updated": "2025-03-16T15:00:00Z"
}
```

**Field Validations:**
- `id`: UUID v4 format
- `status`: Must be one of: open, escalated, resolved, abandoned
- `timeline`: Chronological order, cannot be empty
- `date_*`: ISO 8601 format with Z suffix
- `purchase_price`, `amount_recovered`: Non-negative numbers

### Warranty Entry Schema

```json
{
  "id": "uuid-v4",
  "product": {
    "name": "Product Name",
    "model": "Model Number",
    "serial_number": "SN123456789",
    "category": "electronics|appliance|vehicle|furniture|other",
    "purchase_date": "2025-01-15",
    "purchase_price": 799.99,
    "retailer": "Retailer Name"
  },
  "warranty": {
    "type": "manufacturer|extended|store",
    "start_date": "2025-01-15",
    "end_date": "2026-01-15",
    "duration_months": 12,
    "coverage": "Parts and labor for manufacturing defects",
    "exclusions": ["Physical damage", "Water damage", "Cosmetic issues"],
    "transferable": false,
    "extended": false
  },
  "manufacturer": {
    "name": "Manufacturer Name",
    "warranty_phone": "1-800-WARRANTY",
    "warranty_email": "warranty@manufacturer.com",
    "warranty_website": "https://manufacturer.com/warranty"
  },
  "registration": {
    "registered": true,
    "registration_date": "2025-01-16",
    "registration_number": "REG-ABC-123",
    "registration_required": true
  },
  "claims": [
    {
      "claim_id": "CLM-001",
      "date_filed": "2025-03-15T00:00:00Z",
      "issue": "Issue description",
      "status": "pending|in_progress|approved|denied|resolved",
      "claim_number": "Company claim number",
      "expected_resolution": "2025-03-30T00:00:00Z",
      "updates": [
        {
          "date": "2025-03-20T00:00:00Z",
          "status": "in_progress",
          "note": "Technician scheduled"
        }
      ]
    }
  ],
  "documents": {
    "receipt": "path/to/receipt.pdf",
    "warranty_card": "path/to/warranty.pdf",
    "registration": "path/to/registration.pdf"
  },
  "alerts": {
    "expiration_alert_days": 30,
    "alert_enabled": true
  },
  "status": "active|expired",
  "created": "2025-01-16T10:00:00Z",
  "last_updated": "2025-03-16T12:00:00Z"
}
```

## Directory Structure

```
~/.complaint-tracker/  (or .complaint-tracker/ for project-level)
├── cases.json                # All complaint cases
├── warranties.json           # Warranty database
├── config.json              # User preferences and jurisdiction
├── communications/          # Communication logs by case
│   └── {case-id}/
│       ├── emails.json
│       ├── calls.json
│       └── chats.json
├── documents/              # Supporting documents by case
│   └── {case-id}/
│       ├── receipts/
│       ├── photos/
│       ├── correspondence/
│       └── letters/
└── templates/              # Letter templates
    ├── initial-complaint.md
    ├── escalation-supervisor.md
    ├── escalation-manager.md
    ├── escalation-corporate.md
    ├── bbb-complaint.md
    └── small-claims-demand.md
```

## Escalation Strategy Framework

### Level 1: Customer Service Representative (CSR)
**Objective**: Resolve at lowest level
**Tone**: Polite, clear, factual
**Timeline**: Same-day contact
**Success Rate**: ~40%

**Key Actions:**
- State issue clearly and concisely
- Request specific resolution
- Get CSR name and employee ID
- Obtain ticket/case number
- Document promises made
- Set follow-up timeline

**Documentation:**
- Record call date, time, duration
- Note CSR name and ID
- Save ticket number
- Document all promises
- Follow up in writing (email)

### Level 2: Supervisor
**Objective**: Escalate past CSR level
**Tone**: Firm, professional, assertive
**Timeline**: 3-7 days after CSR failure
**Success Rate**: ~60% (cumulative)

**Key Actions:**
- Write formal escalation letter
- Reference all CSR interactions
- State legal basis for claim
- Set 7-day response deadline
- Mention next escalation level
- Send via email + certified mail

**Letter Elements:**
- Chronology of CSR interactions
- Specific promises not kept
- Legal obligations (warranty, consumer protection)
- Clear desired outcome
- Reasonable deadline
- Hint at corporate escalation

### Level 3: Manager/Corporate
**Objective**: Involve corporate oversight
**Tone**: Firm, legal awareness, professional
**Timeline**: 7-14 days after supervisor failure
**Success Rate**: ~75% (cumulative)

**Key Actions:**
- Escalate to corporate customer service
- CC: Legal department
- Cite consumer protection laws
- Reference BBB and legal remedies
- Set 10-day deadline
- Send certified mail

**Letter Elements:**
- Complete timeline of failures
- Cite specific laws violated
- Legal consequences (BBB, AG, lawsuit)
- Documentation of ready evidence
- Final opportunity for resolution
- Clear legal pathway if unresolved

### Level 4: External Complaints
**Objective**: Apply external pressure
**Tone**: Factual, formal, comprehensive
**Timeline**: Immediately after corporate failure
**Success Rate**: ~85% (cumulative)

**Complaint Venues:**
1. **Better Business Bureau (BBB)**
   - File online complaint
   - Company has 14 days to respond
   - Becomes part of permanent record
   - Free to file

2. **State Attorney General**
   - Consumer protection division
   - Investigate unfair practices
   - Can levy fines
   - Free to file

3. **Federal Trade Commission (FTC)**
   - Track deceptive practices
   - Pattern analysis
   - Enforcement actions
   - Free to file

4. **Consumer Financial Protection Bureau (CFPB)**
   - Financial products only
   - Strong enforcement power
   - Company must respond
   - Free to file

5. **Social Media**
   - Twitter, Facebook (company pages)
   - Professional, factual tone
   - Can expedite resolution
   - Public visibility

### Level 5: Legal Remedies
**Objective**: Legal enforcement
**Tone**: Formal, legal, final
**Timeline**: After all other remedies exhausted
**Success Rate**: ~80% win rate in small claims

**Options:**

**A. Small Claims Court**
- Claim limit: $2,500-$10,000 (varies by state)
- No attorney required
- Filing fee: $30-$100
- Hearing within 30-60 days
- Win rate: ~80% with proper documentation

**B. Chargeback (Credit Card)**
- Dispute within 60 days of statement
- Merchant must prove delivery/quality
- Strong consumer protections
- Zero liability for defective goods

**C. Attorney Representation**
- For claims above small claims limit
- Consumer protection attorneys often work on contingency
- Can recover attorney fees under consumer protection laws
- Treble damages possible in some states

**D. Class Action**
- Join existing lawsuit if available
- No upfront cost
- Smaller individual recovery
- Addresses systemic issues

## Consumer Rights Reference

### Federal Protections

#### Magnuson-Moss Warranty Act (15 U.S.C. § 2301 et seq.)
**Applies to**: Consumer products under warranty
**Protections:**
- Requires clear warranty terms
- Prohibits deceptive warranty practices
- Allows recovery of attorney fees
- Breach of warranty remedies

**Key Provisions:**
- "Full" vs "Limited" warranty disclosure
- Warranty must be available before purchase
- Cannot disclaim implied warranties on written warranty
- Consumers can sue for breach

**Damages Available:**
- Actual damages
- Attorney fees and costs
- Incidental and consequential damages

#### FTC Act Section 5 (15 U.S.C. § 45)
**Applies to**: All consumer transactions
**Protections:**
- Prohibits unfair or deceptive practices
- Covers false advertising
- Bait-and-switch prevention
- Deceptive pricing

**Enforcement:**
- FTC investigations
- Cease and desist orders
- Consumer restitution
- Civil penalties

#### Fair Credit Billing Act (15 U.S.C. § 1666)
**Applies to**: Credit card purchases
**Protections:**
- Right to dispute charges for defective goods
- Chargeback for non-delivery
- Billing error correction
- Zero liability for unauthorized charges

**Chargeback Process:**
1. Dispute within 60 days of statement
2. Write to card issuer
3. Issuer investigates (2 billing cycles)
4. Merchant must prove validity
5. Charge removed if unproven

#### Truth in Lending Act (TILA)
**Applies to**: Consumer credit
**Protections:**
- Clear disclosure of credit terms
- Right to rescind certain transactions
- Limits on liability

### State Consumer Protection Laws

#### Unfair and Deceptive Acts and Practices (UDAP)
**All 50 states have UDAP laws**

**Common Features:**
- Broader than federal protections
- Private right of action
- Treble damages (3x actual damages)
- Attorney fee recovery
- Lower burden of proof than fraud

**Examples:**
- California: Consumer Legal Remedies Act
- Massachusetts: Chapter 93A
- New York: General Business Law § 349
- Texas: Deceptive Trade Practices Act

**Typical Violations:**
- False advertising
- Bait-and-switch
- Failure to honor warranty
- Deceptive pricing
- Failure to disclose defects

**Damages:**
- Actual damages
- Statutory damages (some states)
- Treble damages (3x in many states)
- Attorney fees and costs
- Punitive damages (some states)

#### Implied Warranty of Merchantability (UCC § 2-314)
**Applies to**: All goods sold by merchants
**Standard**: Goods must be fit for ordinary purposes

**Key Points:**
- Automatic (no written warranty needed)
- Cannot be disclaimed in many states
- Applies even after written warranty expires
- Reasonable time after purchase (varies)

**What It Covers:**
- Product works for intended purpose
- Free from defects
- Properly packaged and labeled
- Conforms to promises on label

#### Lemon Laws
**Vehicles**: All 50 states have vehicle lemon laws
**Other Products**: Some states extend to other products

**Typical Requirements:**
- Multiple repair attempts (usually 3-4)
- Out of service 30+ days
- Within warranty period or 1 year
- Substantial defect affecting safety/value

**Remedies:**
- Replacement vehicle
- Full refund
- Attorney fees

### Jurisdiction-Specific Considerations

**Small Claims Court Limits (by state):**
- California: $10,000
- New York: $5,000 (town/village), $3,000 (city)
- Texas: $10,000
- Florida: $8,000
- Illinois: $10,000
- (Varies by state, check local rules)

**Statute of Limitations (typical):**
- Breach of contract: 3-6 years
- Fraud: 2-3 years
- UCC warranty: 4 years
- UDAP: 3-4 years
- (Check state-specific rules)

## Communication Templates

### Initial Complaint Letter Template

```markdown
[Your Name]
[Your Address]
[Your Phone]
[Your Email]

[Date]

Customer Service
[Company Name]
[Company Address]

RE: Complaint - [Product/Service] - [Issue]
    Purchase Date: [Date]
    Amount: $[Amount]

Dear Sir or Madam:

I am writing to report an issue with [product/service] purchased on [date] for $[amount].

ISSUE:
[Clear, factual description of problem]

RESOLUTION REQUESTED:
[Specific desired outcome]

I have attached:
- Copy of receipt
- [Other documentation]

I request a response within 7 business days. I can be reached at [phone] or [email].

Thank you for your attention to this matter.

Sincerely,
[Your Name]

Enclosures: [List]
```

### Supervisor Escalation Template

```markdown
[Your Name]
[Your Address]
[Your Phone]
[Your Email]

[Date]

Customer Service Supervisor
[Company Name]
[Company Address]

RE: Formal Escalation - Unresolved Complaint
    Case/Ticket: [Number]
    Purchase Date: [Date]
    Amount: $[Amount]

Dear Supervisor:

I am escalating an unresolved complaint regarding [product/service].

BACKGROUND:
On [date], I purchased [product] for $[amount]. [Issue description].

PREVIOUS ATTEMPTS:
1. [Date]: [Contact details and outcome]
2. [Date]: [Contact details and outcome]

Despite my attempts, this remains unresolved.

LEGAL BASIS:
Under the Magnuson-Moss Warranty Act and [state] consumer protection laws, I am entitled to [remedy].

REQUESTED RESOLUTION:
I expect [specific outcome] within 7 business days.

If unresolved by [deadline], I will escalate to corporate headquarters and file external complaints with the BBB and [state] Attorney General.

I await your response.

Sincerely,
[Your Name]

Enclosures: [Documentation]
```

### Small Claims Demand Letter Template

```markdown
[Your Name]
[Your Address]
[Your Phone]
[Your Email]

[Date]

SENT VIA CERTIFIED MAIL - RETURN RECEIPT REQUESTED

[Company Name]
[Registered Agent Address]

RE: FINAL DEMAND BEFORE LAWSUIT
    Amount in Controversy: $[Total]
    Deadline: [Date] (10 days)

Dear Sir or Madam:

This is formal notice and final demand before I file a lawsuit in small claims court.

STATEMENT OF FACTS:
1. On [date], I purchased [product] for $[amount]
2. [Issue description]
3. I have attempted resolution [number] times
4. [Company] has failed to provide satisfactory resolution

LEGAL BASIS:
[Company's] actions constitute:
- Breach of contract
- Breach of warranty (Magnuson-Moss Warranty Act)
- Violation of [state] Consumer Protection Act
- Breach of implied warranty of merchantability

DAMAGES CLAIMED:
- Purchase Price: $[amount]
- Time and Expenses: $[amount]
- Court Filing Fee: $[amount]
TOTAL DEMAND: $[total]

DEMAND FOR PAYMENT:
I demand payment of $[total] within 10 days (by [deadline]).

CONSEQUENCES OF NON-PAYMENT:
If I do not receive payment by [deadline], I will:
1. File lawsuit in small claims court
2. Seek maximum allowable damages (including treble damages)
3. Seek recovery of attorney fees and costs
4. Pursue post-judgment collection

This is a time-limited settlement offer. After [deadline], my claim will include additional statutory damages and fees.

TIME IS OF THE ESSENCE.

Sincerely,
[Your Name]
```

## Documentation Best Practices

### Essential Documentation

**For Every Case:**
1. **Receipt/Proof of Purchase**
   - Original receipt
   - Credit card statement
   - Invoice
   - Order confirmation

2. **Product Evidence**
   - Photos of defect
   - Videos showing malfunction
   - Serial number photos
   - Packaging (if relevant)

3. **Communication Records**
   - Email correspondence (all)
   - Certified mail receipts
   - Phone call logs (date, time, person, summary)
   - Chat transcripts
   - Social media messages

4. **Timeline Document**
   - Chronological list of all events
   - Dates, times, contacts
   - Promises made
   - Actions taken

5. **Supporting Documents**
   - Warranty terms
   - Product manual
   - Advertisements (if false claims)
   - Expert opinions/estimates
   - Repair records

### Organization System

**Digital Organization:**
```
/Case-[Company]-[Date]/
  ├── /receipts/
  │   └── original_receipt.pdf
  ├── /photos/
  │   ├── defect_1.jpg
  │   └── defect_2.jpg
  ├── /correspondence/
  │   ├── email_20250315.pdf
  │   └── email_20250320.pdf
  ├── /letters/
  │   ├── initial_complaint.pdf
  │   └── supervisor_escalation.pdf
  └── timeline.md
```

**Physical Organization:**
- Use labeled folders
- Keep originals safe
- Make copies for submission
- Organize chronologically

### Communication Logging

**For Each Phone Call:**
- Date and time
- Duration
- Person spoken to (name, title, ID)
- Ticket/case number created
- Summary of conversation
- Promises made
- Next steps agreed
- Follow-up date

**For Each Email:**
- Save to dedicated folder
- Note date sent/received
- Print important emails
- Forward to personal email (backup)

**For Each Letter:**
- Keep copy
- Send certified mail (get receipt)
- Track delivery confirmation
- Note date sent

### Photo/Video Evidence

**Best Practices:**
- Take multiple angles
- Include serial number in frame
- Show defect clearly
- Date stamp if possible
- Video of malfunction (if applicable)
- Before/after (if relevant)

## Success Pattern Analysis

### What Works (Historical Data)

**Resolution by Escalation Level:**
- CSR Level: 40% resolved
- Supervisor Level: 60% resolved (20% additional)
- Corporate Level: 75% resolved (15% additional)
- BBB Complaint: 85% resolved (10% additional)
- Legal Threat: 90% resolved (5% additional)
- Lawsuit Filed: 95% resolved (5% additional)

**Time to Resolution:**
- CSR: 1-7 days
- Supervisor: 7-14 days
- Corporate: 14-30 days
- BBB: 14-30 days
- Legal: 30-90 days

**Most Effective Strategies:**
1. Clear, factual documentation (90% success factor)
2. Citing specific laws (85% success factor)
3. Certified mail (80% success factor)
4. BBB complaint (75% success factor)
5. Legal demand letter (70% success factor)

**Company Response Patterns:**
- Small businesses: Often resolve at CSR/supervisor level
- Large corporations: Often require corporate escalation
- Online retailers: Often resolve via BBB complaint
- Manufacturers: Often resolve via warranty claim escalation

### What Doesn't Work

**Ineffective Approaches:**
- Emotional appeals without facts
- Threats without follow-through
- Vague demands
- Poor documentation
- Delayed action
- Accepting first low offer
- Giving up too early

## Small Claims Court Procedures

### Pre-Filing Requirements

**Demand Letter:**
- Required in most jurisdictions
- Must give 10-30 days (varies by state)
- Must state amount and legal basis
- Must be sent to registered agent or corporate address
- Keep proof of mailing

**Documentation Check:**
- Receipt ✓
- Timeline ✓
- All communications ✓
- Photos/evidence ✓
- Demand letter + proof of mailing ✓

### Filing Process

**Step 1: Determine Jurisdiction**
- Where defendant does business
- Where transaction occurred
- Where defendant resides (for individuals)

**Step 2: Complete Complaint Form**
- Plaintiff information
- Defendant information (correct legal name and address)
- Amount claimed (itemized)
- Facts supporting claim
- Legal basis for claim

**Step 3: Pay Filing Fee**
- $30-$100 (varies by state/amount)
- Waiver available for low income
- Recoverable if you win

**Step 4: Serve Defendant**
- Sheriff service (best)
- Process server
- Certified mail (some states)
- Must be served before hearing

**Step 5: Await Hearing Date**
- Usually 30-60 days
- Prepare evidence
- Organize presentation
- Practice testimony

### Hearing Preparation

**Evidence to Bring:**
- 3 copies of everything (judge, defendant, you)
- Original documents
- Photos (printed, labeled)
- Timeline (printed)
- Witness statements (if any)
- Expert opinions (if any)

**Presentation Structure:**
1. Introduction (2 min)
   - Who you are
   - What you're claiming
   - How much

2. Facts (5 min)
   - What happened (chronologically)
   - Show evidence as you go
   - Clear, factual, unemotional

3. Legal Basis (2 min)
   - What law supports your claim
   - Why defendant is liable
   - Why you deserve damages

4. Conclusion (1 min)
   - Restate claim amount
   - Request judgment

**Courtroom Etiquette:**
- Dress professionally
- Address judge as "Your Honor"
- Stand when speaking (if requested)
- Speak clearly and confidently
- Be respectful to defendant
- Stick to facts, avoid emotion
- Answer questions directly

### Post-Judgment Collection

**If You Win:**
- Judgment entered same day (usually)
- Defendant has 30 days to pay
- If no payment, enforce judgment:
  - Wage garnishment
  - Bank levy
  - Property lien
  - Asset seizure

**Collection Methods:**
- Request payment directly
- Payment plan (if defendant offers)
- Hire collection agency
- Sheriff levy on bank accounts
- Wage garnishment order
- Sell judgment to collection company

## Best Practices Summary

1. **Document Everything**
   - Every communication
   - Every promise
   - Every event
   - Every expense

2. **Act Quickly**
   - Don't delay complaints
   - Follow up promptly
   - Meet deadlines
   - Preserve evidence

3. **Be Professional**
   - Calm, factual tone
   - Clear communication
   - Respectful but firm
   - Stick to facts

4. **Know Your Rights**
   - Research applicable laws
   - Cite specific statutes
   - Understand remedies
   - Know court procedures

5. **Escalate Systematically**
   - Give each level fair chance
   - Follow escalation ladder
   - Don't skip steps unnecessarily
   - Know when to escalate

6. **Set Deadlines**
   - Always give reasonable deadline
   - Be clear about consequences
   - Follow through if deadline missed

7. **Use Multiple Channels**
   - Phone + email
   - Written + verbal
   - Internal + external
   - Official + social (judiciously)

8. **Keep Copies**
   - Digital backup
   - Physical copies
   - Cloud storage
   - Multiple locations

9. **Be Persistent**
   - Don't give up if you're right
   - Follow up consistently
   - Escalate when needed
   - Pursue legal remedies if necessary

10. **Know When to Accept**
    - Evaluate settlement offers
    - Consider cost of further action
    - Weigh likelihood of success
    - Sometimes partial victory is worth it

---

**This skill is read by all complaint-warranty-manager agents to ensure consistent complaint handling and legal awareness.**
