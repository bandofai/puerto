# Complaint & Warranty Manager Plugin

A comprehensive customer service interaction and warranty claim tracking system for Claude Code that helps you manage complaints, track escalations, monitor warranties, and prepare for legal remedies.

## Overview

The Complaint & Warranty Manager plugin provides intelligent agents, skills, and templates for managing consumer disputes and warranty claims. From initial complaint filing to small claims court preparation, this plugin ensures you document everything and know your rights.

## What's Included

### Agents

#### 1. complaint-case-manager
Manages complaint cases with detailed tracking and communication logging.

**Key Features:**
- Case creation and tracking (open, escalated, resolved, abandoned)
- Communication history logging (every call, email, chat)
- Status updates and timeline management
- Multi-company case management
- Documentation organization
- Case search and filtering

**Model**: Haiku (fast, efficient for case management)

**Activation**: Automatically activates for complaint tracking, or use `@complaint-case-manager`.

#### 2. escalation-specialist
Crafts strong, professional escalation communications and strategies.

**Key Features:**
- Escalation path planning (CSR → Supervisor → Manager → Legal/BBB)
- Professional letter generation
- Legal language assistance
- Consumer rights information
- Firm but respectful tone
- Small claims court preparation
- Documentation review for legal readiness

**Model**: Sonnet (nuanced understanding for legal/professional communication)

**Activation**: Use `@escalation-specialist` for escalation strategies and communications.

#### 3. warranty-claim-tracker
Tracks all warranties with expiration alerts and claim procedures.

**Key Features:**
- Warranty database management
- Expiration date tracking and alerts
- Claim procedure documentation
- Product registration tracking
- Manufacturer contact information
- Claim status monitoring
- Success/failure pattern analysis

**Model**: Haiku (efficient for database operations)

**Activation**: Use `@warranty-claim-tracker` for warranty management.

### Skills

#### complaint-resolution
Comprehensive patterns for complaint management, including:
- Escalation strategy frameworks
- Consumer rights documentation (federal/state)
- Communication templates
- Small claims court procedures
- Documentation best practices
- Success pattern analysis
- Legal remedies reference

All agents read this skill for consistent complaint handling.

### Templates

#### 1. complaint-case.json
Structured template for individual complaint cases:
- Company information
- Issue description
- Status tracking
- Communication timeline
- Escalation path
- Resolution deadlines
- Outcomes and amounts

#### 2. escalation-letter-template.md
Professional complaint letter templates:
- Initial complaint letter
- First escalation (supervisor)
- Second escalation (manager)
- Third escalation (corporate/legal)
- BBB complaint
- Small claims demand letter
- FTC/Consumer protection filing

#### 3. warranty-database.json
Warranty tracking database:
- Product information
- Purchase details
- Warranty terms and expiration
- Manufacturer contacts
- Claim procedures
- Status tracking

## Installation

```bash
/plugin install complaint-warranty-manager@puerto
```

After installation, restart Claude Code to activate all agents and skills.

## Quick Start

### Initial Setup

```bash
# Initialize complaint tracking system
@complaint-case-manager "Initialize complaint tracking system"

# Import warranties (optional)
@warranty-claim-tracker "Initialize warranty database"
```

### File a Complaint

```bash
# Create new complaint case
@complaint-case-manager "File complaint against [Company Name] for [Issue Description]"

# Example:
@complaint-case-manager "File complaint against XYZ Electronics for defective TV that stopped working after 2 months"
```

### Log Communications

```bash
# Log a call
@complaint-case-manager "Log call with XYZ Electronics: spoke with CSR John, said they would send replacement, ticket #12345"

# Log email
@complaint-case-manager "Log email sent to support@xyz.com requesting status update on ticket #12345"

# Log chat
@complaint-case-manager "Log chat with support: they claim issue not covered by warranty"
```

### Escalate a Case

```bash
# Request escalation strategy
@escalation-specialist "Review my case against XYZ Electronics and suggest escalation strategy"

# Generate escalation letter
@escalation-specialist "Write escalation letter to XYZ Electronics supervisor about defective TV"

# Prepare BBB complaint
@escalation-specialist "Draft BBB complaint against XYZ Electronics"
```

### Track Warranty

```bash
# Add warranty
@warranty-claim-tracker "Add warranty for Samsung TV purchased 2025-01-15, 1-year manufacturer warranty"

# Check expiring warranties
@warranty-claim-tracker "Show warranties expiring in next 3 months"

# File warranty claim
@warranty-claim-tracker "File warranty claim for Samsung TV, issue: screen flickering"
```

### Small Claims Preparation

```bash
# Prepare for small claims court
@escalation-specialist "Prepare small claims court case against XYZ Electronics for $800 defective TV"

# Review documentation
@escalation-specialist "Review my documentation for XYZ case - is it sufficient for small claims?"

# Generate demand letter
@escalation-specialist "Create small claims demand letter for XYZ Electronics, $800 product cost + $200 time/expenses"
```

## Data Structure

All complaint data is stored in `~/.complaint-tracker/` or `.complaint-tracker/` (project-specific).

### Directory Layout

```
.complaint-tracker/
├── cases.json                # All complaint cases
├── warranties.json           # Warranty database
├── communications/           # Communication logs by case
│   └── {case-id}/
│       ├── emails.md
│       ├── calls.md
│       └── chats.md
├── documents/               # Supporting documents by case
│   └── {case-id}/
│       ├── receipts/
│       ├── photos/
│       └── correspondence/
├── templates/               # Letter templates
│   ├── initial-complaint.md
│   ├── escalation-supervisor.md
│   ├── escalation-manager.md
│   └── small-claims-demand.md
└── config.json             # User preferences

```

### Core Data Models

#### Complaint Case Entry

```json
{
  "id": "case-uuid-12345",
  "case_number": "XYZ-2025-001",
  "status": "open",
  "company": {
    "name": "XYZ Electronics",
    "contact_info": {
      "phone": "1-800-555-1234",
      "email": "support@xyz.com",
      "address": "123 Corporate Blvd, City, ST 12345"
    },
    "website": "https://xyz.com"
  },
  "issue": {
    "category": "defective_product",
    "product": "Samsung 55\" TV Model ABC123",
    "description": "TV stopped working after 2 months, no power",
    "purchase_date": "2025-01-15",
    "purchase_price": 799.99,
    "receipt_number": "REC-12345"
  },
  "timeline": [
    {
      "date": "2025-03-15T10:00:00Z",
      "type": "issue_occurred",
      "description": "TV stopped working completely"
    },
    {
      "date": "2025-03-16T14:30:00Z",
      "type": "call",
      "contact": "CSR John",
      "summary": "Called support, given ticket #12345, promised replacement",
      "ticket_number": "12345"
    }
  ],
  "escalation_path": {
    "current_level": "csr",
    "levels_attempted": ["csr"],
    "next_steps": ["supervisor", "manager", "corporate", "bbb", "legal"]
  },
  "resolution": {
    "desired_outcome": "Full refund or replacement",
    "deadline": "2025-04-15",
    "actual_outcome": null,
    "resolved_date": null,
    "amount_recovered": null
  },
  "legal": {
    "small_claims_eligible": true,
    "claim_amount": 799.99,
    "statute_of_limitations": "2029-01-15",
    "consumer_protection_violations": []
  },
  "notes": "Customer service unhelpful, may need to escalate quickly",
  "created": "2025-03-16T15:00:00Z",
  "last_updated": "2025-03-16T15:00:00Z"
}
```

#### Warranty Entry

```json
{
  "id": "warranty-uuid-67890",
  "product": {
    "name": "Samsung 55\" TV",
    "model": "ABC123",
    "serial_number": "SN123456789",
    "category": "electronics",
    "purchase_date": "2025-01-15",
    "purchase_price": 799.99,
    "retailer": "Best Buy"
  },
  "warranty": {
    "type": "manufacturer",
    "start_date": "2025-01-15",
    "end_date": "2026-01-15",
    "duration_months": 12,
    "coverage": "Parts and labor for defects",
    "exclusions": ["Physical damage", "Water damage"],
    "transferable": false
  },
  "manufacturer": {
    "name": "Samsung",
    "warranty_phone": "1-800-SAMSUNG",
    "warranty_email": "warranty@samsung.com",
    "warranty_website": "https://samsung.com/warranty"
  },
  "registration": {
    "registered": true,
    "registration_date": "2025-01-16",
    "registration_number": "REG-ABC-123"
  },
  "claims": [
    {
      "claim_id": "CLM-001",
      "date_filed": "2025-03-16",
      "issue": "TV not powering on",
      "status": "pending",
      "expected_resolution": "2025-03-30"
    }
  ],
  "documents": {
    "receipt": "receipts/samsung-tv-receipt.pdf",
    "warranty_card": "warranties/samsung-warranty.pdf",
    "registration": "warranties/samsung-registration.pdf"
  },
  "alerts": {
    "expiration_alert_days": 30,
    "alert_enabled": true
  },
  "created": "2025-01-16T10:00:00Z",
  "last_updated": "2025-03-16T12:00:00Z"
}
```

#### Communication Log Entry

```json
{
  "id": "comm-uuid-11111",
  "case_id": "case-uuid-12345",
  "date": "2025-03-16T14:30:00Z",
  "type": "phone_call",
  "direction": "outbound",
  "contact": {
    "name": "John (CSR)",
    "title": "Customer Service Representative",
    "employee_id": null
  },
  "duration_minutes": 15,
  "summary": "Called to report defective TV. CSR John created ticket #12345 and promised replacement within 7-10 business days.",
  "details": "Explained TV stopped working after 2 months. John verified purchase, confirmed in warranty. Said replacement would be sent. Asked for tracking number, he said it would be emailed within 24 hours.",
  "ticket_number": "12345",
  "promises_made": [
    "Replacement TV will be sent",
    "Tracking number within 24 hours",
    "Resolution within 7-10 business days"
  ],
  "outcome": "pending",
  "follow_up_required": true,
  "follow_up_date": "2025-03-17",
  "recording_available": false,
  "created": "2025-03-16T14:45:00Z"
}
```

## Workflows

### Complete Complaint Lifecycle

```bash
# 1. File complaint
@complaint-case-manager "File complaint: purchased defective laptop from ABC Store for $1200, won't boot"

# 2. Log initial contact
@complaint-case-manager "Log call with ABC Store support: CSR Jane said they don't do refunds after 14 days, only store credit"

# 3. Research rights
@escalation-specialist "What are my consumer rights for defective laptop in California?"

# 4. First escalation
@escalation-specialist "Write escalation letter to ABC Store supervisor about defective laptop, demand full refund"

# 5. Log escalation
@complaint-case-manager "Log email sent: escalation letter to ABC Store supervisor via supervisor@abcstore.com"

# 6. Track response
@complaint-case-manager "Log email received: supervisor offered $1000 store credit (originally paid $1200 cash)"

# 7. Second escalation
@escalation-specialist "Write second escalation to ABC Store corporate, still demanding full $1200 refund"

# 8. BBB filing
@escalation-specialist "Draft BBB complaint against ABC Store for refusing refund on defective $1200 laptop"

# 9. Small claims prep
@escalation-specialist "Prepare small claims case: $1200 product + $150 filing/time = $1350 total"

# 10. Resolution
@complaint-case-manager "Mark case resolved: received full $1200 refund after BBB complaint"
```

### Warranty Management Workflow

```bash
# 1. Add warranty upon purchase
@warranty-claim-tracker "Add warranty: LG Refrigerator, Model XYZ, purchased 2025-01-20 from Home Depot for $2400, 1-year manufacturer + 4-year extended warranty"

# 2. Register product
@warranty-claim-tracker "Update LG refrigerator warranty: registered with LG on 2025-01-21, registration #REG-LG-789"

# 3. Set alerts
@warranty-claim-tracker "Set expiration alert for LG refrigerator: notify 60 days before warranty ends"

# 4. File claim (when needed)
@warranty-claim-tracker "File warranty claim: LG refrigerator, ice maker not working, model XYZ serial 123456"

# 5. Track claim
@warranty-claim-tracker "Update LG claim: technician scheduled for 2025-03-25"

# 6. Claim resolution
@warranty-claim-tracker "Update LG claim: ice maker replaced under warranty, claim closed"

# 7. Review expiring warranties
@warranty-claim-tracker "Show all warranties expiring in next 90 days"
```

### Escalation Strategy Workflow

```bash
# 1. Assess situation
@escalation-specialist "Review my case against XYZ Company: purchased $500 item, defective, they refuse refund, only offering 50% store credit"

# 2. Know your rights
@escalation-specialist "What consumer protection laws apply to defective products in [your state]?"

# 3. Escalation plan
@escalation-specialist "Create escalation strategy for XYZ Company case"
# Output:
# Level 1: Supervisor escalation (firm letter citing consumer protection laws)
# Level 2: Corporate complaint (CC: Legal department)
# Level 3: BBB complaint
# Level 4: State Attorney General consumer protection division
# Level 5: Small claims court ($500 + expenses)

# 4. Execute escalation
@escalation-specialist "Write supervisor escalation letter for XYZ Company, cite [applicable consumer protection laws]"

# 5. Legal demand
@escalation-specialist "Write small claims demand letter: $500 product + $100 time/expenses + $50 filing fee = $650"

# 6. Court prep
@escalation-specialist "Create small claims court documentation checklist for XYZ Company case"
```

### Pattern Analysis Workflow

```bash
# Identify what works
@complaint-case-manager "Analyze all resolved cases: what strategies worked best?"

# Company-specific patterns
@complaint-case-manager "Show all cases against XYZ Company: what's the fastest resolution path?"

# Success metrics
@complaint-case-manager "Generate success report: resolution rates by escalation level"

# Timing patterns
@complaint-case-manager "What's the average time to resolution for cases that went to BBB?"
```

## Escalation Levels Explained

### Level 1: Customer Service Representative (CSR)
- **First contact**
- Goal: Resolve at lowest level
- Document everything: name, employee ID, ticket number, promises
- Be polite but firm
- State desired outcome clearly

### Level 2: Supervisor
- **First escalation**
- Request supervisor by name
- Summarize CSR interaction
- Reiterate desired outcome
- Set deadline for response
- Send written follow-up

### Level 3: Manager/Corporate
- **Second escalation**
- Escalate to corporate customer service
- Reference previous contacts
- Cite consumer protection laws (if applicable)
- Demand resolution with deadline
- CC: Legal department (if applicable)

### Level 4: External Complaints
- **BBB (Better Business Bureau)**: File formal complaint
- **State Attorney General**: Consumer protection division
- **FTC**: Federal Trade Commission complaint
- **CFPB**: Consumer Financial Protection Bureau (financial products)
- **Social media**: Public complaint (can be effective)

### Level 5: Legal Remedies
- **Small claims court**: Up to $5,000-$10,000 (varies by state)
- **Class action**: Join existing lawsuit
- **Attorney**: Hire lawyer for larger amounts
- **Arbitration**: If required by terms of service

## Consumer Rights Reference

### Federal Protections

**Magnuson-Moss Warranty Act**
- Governs consumer product warranties
- Requires clear warranty terms
- Allows recovery of attorney fees

**FTC Act Section 5**
- Prohibits unfair or deceptive practices
- Covers false advertising
- Enforced by FTC

**Fair Credit Billing Act**
- Dispute charges for defective goods
- Credit card chargeback rights

### State Protections (Vary by State)

**Lemon Laws**
- Defective vehicles (all states)
- Defective products (some states)

**Implied Warranty of Merchantability**
- Products must work for intended purpose
- Can't be waived in many states

**Consumer Protection Acts**
- State-specific protections
- Often allow treble damages (3x)
- Attorney fee recovery

### Chargeback Rights

**Credit Card Protections:**
- Dispute defective/undelivered goods
- 60-day window from statement
- Merchant must prove delivery/quality
- Zero liability for unauthorized charges

## Small Claims Court Guide

### When to Use Small Claims

- Amount under state limit ($2,500-$10,000)
- Documented damages
- Failed to resolve through escalation
- Clear liability

### Documentation Needed

- Purchase receipt/proof of payment
- Product photos/videos showing defect
- All communication logs (emails, letters, calls)
- Warranty terms (if applicable)
- Repair estimates or expert opinions
- Timeline of events
- Demand letter sent to defendant

### Filing Process

1. **Determine jurisdiction**: Where defendant does business
2. **Complete complaint**: State facts, damages sought
3. **Pay filing fee**: $30-$100 (varies by state/amount)
4. **Serve defendant**: Sheriff, process server, or certified mail
5. **Await hearing date**: Usually 30-60 days
6. **Prepare presentation**: Organize evidence, practice testimony
7. **Attend hearing**: Present case to judge
8. **Collect judgment**: If you win

### Demand Letter Template

Before filing, send demand letter:
- State facts clearly
- Specify amount owed
- Cite legal basis
- Set 10-day deadline
- State intent to file lawsuit if not resolved

## Success Patterns

### What Works

**Documentation is king:**
- Log every communication immediately
- Save all emails and letters
- Note names, dates, times, promises
- Take photos/videos of defects
- Keep all receipts and warranties

**Escalation effectiveness:**
- 60% resolve at supervisor level
- 25% resolve at corporate level
- 10% resolve after BBB complaint
- 5% require legal action

**Best strategies:**
- Be polite but firm
- Know your rights and cite them
- Set clear deadlines
- Follow up in writing
- Use multiple channels (phone + email)
- Social media can expedite (use judiciously)

**Small claims success:**
- 80% win rate with proper documentation
- Many settle before hearing
- Median award: 85% of claimed amount

## Tips for Success

### Do's
- Document everything
- Stay calm and professional
- Know your consumer rights
- Set reasonable deadlines
- Follow up consistently
- Escalate systematically
- Keep copies of everything
- Use certified mail for important letters

### Don'ts
- Don't threaten without following through
- Don't accept first offer if unfair
- Don't lose your temper
- Don't make false claims
- Don't wait too long (statute of limitations)
- Don't give up if you're right
- Don't settle for store credit if you want cash

## Configuration

### Global Settings

Configure in `~/.complaint-tracker/config.json`:

```json
{
  "user_info": {
    "name": "Your Name",
    "address": "123 Main St, City, ST 12345",
    "phone": "555-555-5555",
    "email": "your.email@example.com"
  },
  "preferences": {
    "default_deadline_days": 14,
    "auto_escalate_after_days": 30,
    "warranty_alert_days": 30
  },
  "jurisdiction": {
    "state": "CA",
    "small_claims_limit": 10000,
    "attorney_general_url": "https://oag.ca.gov/contact/consumer-complaint-against-business-or-company"
  }
}
```

## Commands Summary

### Case Management
```bash
@complaint-case-manager "File complaint against [Company] for [Issue]"
@complaint-case-manager "Log [call/email/chat]: [summary]"
@complaint-case-manager "Update case [ID]: [new information]"
@complaint-case-manager "Show all open cases"
@complaint-case-manager "Search cases for [company/issue]"
@complaint-case-manager "Mark case [ID] resolved: [outcome]"
```

### Escalation
```bash
@escalation-specialist "Review case [ID] and suggest strategy"
@escalation-specialist "Write [supervisor/manager/corporate] escalation letter for [Company]"
@escalation-specialist "Draft BBB complaint for case [ID]"
@escalation-specialist "What are my consumer rights for [situation] in [state]?"
@escalation-specialist "Prepare small claims case for [Company]: $[amount]"
@escalation-specialist "Create demand letter for case [ID]"
```

### Warranty Tracking
```bash
@warranty-claim-tracker "Add warranty: [product], purchased [date], [warranty terms]"
@warranty-claim-tracker "Show warranties expiring in [N] days"
@warranty-claim-tracker "File claim: [product], issue: [description]"
@warranty-claim-tracker "Update claim [ID]: [status]"
@warranty-claim-tracker "Search warranties for [product/manufacturer]"
```

## Advanced Features

### Multi-Case Management
Track complaints across multiple companies simultaneously, identify patterns in company behavior.

### Legal Document Generation
Generate court-ready documents for small claims filing.

### Success Prediction
Based on historical data, estimate likelihood of resolution at each escalation level.

### Expiration Alerts
Automatic reminders before warranties expire or statutes of limitations run out.

### Template Customization
Customize letter templates for your situation and jurisdiction.

## Troubleshooting

### Case Not Resolving

**Issue**: Company not responding to escalations

**Solution**:
- Verify all communications properly documented
- Escalate to next level (BBB, AG, legal)
- Consider social media (Twitter, Facebook) for visibility
- File small claims if amount justifies

### Missing Documentation

**Issue**: Didn't save receipt or warranty

**Solution**:
- Check email for digital receipts
- Request duplicate from retailer
- Bank/credit card statements as proof of purchase
- Manufacturer may have registration records

### Past Deadline

**Issue**: Warranty expired or statute of limitations approaching

**Solution**:
- Check exact expiration dates (may have longer than thought)
- Some consumer protection laws extend beyond warranty
- Implied warranty may still apply
- Act immediately if statute of limitations near

## Privacy & Data

- **No telemetry**: Your complaint data stays local
- **Sensitive information**: Encrypt financial/personal data
- **Backups**: Recommended to backup `~/.complaint-tracker/` regularly
- **Legal privilege**: Not attorney-client privileged (consult lawyer for legal advice)

## Disclaimer

**This plugin provides information and tools, not legal advice.** For legal advice specific to your situation, consult a licensed attorney in your jurisdiction. Small claims procedures vary by state. Consumer protection laws vary by state and situation.

## Future Enhancements

Planned features:
- State-specific consumer protection law database
- Chargeback assistance for credit card disputes
- Social media complaint integration
- Attorney referral network
- Settlement negotiation guidance
- Class action lawsuit finder
- Product recall tracking
- Lemon law specific workflows

## Contributing

This plugin is part of the Puerto marketplace. See main repository for contribution guidelines.

## Links

- [FTC Consumer Information](https://consumer.ftc.gov/)
- [Better Business Bureau](https://www.bbb.org/)
- [CFPB Complaint Portal](https://www.consumerfinance.gov/complaint/)
- [State Attorneys General](https://www.naag.org/find-my-ag/)

## License

MIT License - See main repository for details

---

**Stand up for your consumer rights. Every complaint documented. Every company held accountable.**
