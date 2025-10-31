# Document Organizer Plugin

**Personal document archiving and organization specialist with auto-categorization, OCR, warranty tracking, and intelligent search**

Version 1.0.0 | Puerto Plugin System

---

## Overview

The Document Organizer plugin transforms chaotic document management into a streamlined, searchable, and automated system. Never lose a receipt, forget a warranty expiration, or spend hours searching for important documents again.

### What It Does

- **Auto-categorizes** receipts, contracts, warranties, insurance docs, and medical records
- **OCR text extraction** makes every document searchable by content
- **Tracks expiration dates** for warranties, contracts, and insurance policies
- **Flags important documents** for instant access during emergencies
- **Digital backup system** with encryption and 3-2-1 strategy
- **Quick retrieval** by keyword, category, date, amount, or vendor
- **Annual review reminders** for retention compliance and purging

### Why You Need It

**Before Document Organizer:**
- Receipts stuffed in drawers, shoeboxes, or scattered across folders
- "Where did I put that warranty?" panic when something breaks
- Missing tax deductions because you can't find receipts
- Insurance claim delays from lost policy documents
- Hours wasted searching through file cabinets
- Expired warranties you forgot to use

**After Document Organizer:**
- Every document categorized automatically and OCR-indexed
- Warranty expirations tracked with advance alerts
- Find any document in seconds with multi-criteria search
- Tax time is easy with instant receipt retrieval
- Important docs always accessible, backed up, and encrypted
- Retention policies enforced automatically

---

## Features

### 1. Automatic Document Classification

Uses vision and OCR to identify document types:

- **Receipts**: Detects store logos, itemized lists, totals
- **Contracts**: Identifies legal formatting, signature lines, terms
- **Warranties**: Recognizes product info, coverage terms, expiration dates
- **Insurance**: Finds policy numbers, coverage tables, premiums
- **Medical**: Detects healthcare provider letterhead, patient info

Extracts metadata automatically:
- Dates (all formats)
- Dollar amounts
- Vendor/company names
- Product descriptions
- Policy/receipt numbers
- Expiration dates

### 2. OCR Text Extraction

Every document becomes fully searchable:
- Scanned receipts
- PDF contracts
- Image-based warranties
- Insurance policies
- Medical records

Search by any text content, even years later.

### 3. Warranty Tracking

Never miss a warranty expiration again:
- Tracks coverage periods
- Sends alerts (30 days, 7 days, 1 day before expiration)
- Monitors registration requirements
- Manages warranty claims
- Stores claim history

### 4. Intelligent Search

Multi-criteria search finds documents instantly:
- **Keyword**: Full-text search through OCR content
- **Category**: Financial, Legal, Insurance, Medical, Warranties
- **Date range**: Last month, last year, tax year, custom
- **Amount range**: Find expensive purchases or small receipts
- **Vendor**: All documents from specific companies
- **Tags**: Tax-deductible, important, active policies
- **Importance**: Critical, high, medium, low

### 5. Document Review Scheduling

Automated maintenance reminders:
- **Weekly**: Process new receipts, check warranty alerts
- **Monthly**: File documents, review upcoming expirations
- **Quarterly**: Check warranties, verify backups, review insurance
- **Annual**: Archive year, purge expired docs, compliance check

### 6. Retention Compliance

Follows IRS and best practice guidelines:
- Tax documents: 7 years
- Financial statements: 1-7 years
- Legal contracts: Duration + 7 years
- Medical records: 7 years minimum
- Never purge: Birth certificates, deeds, diplomas

Automatic purge recommendations based on retention periods.

### 7. Backup & Security

3-2-1 backup strategy:
- 3 copies (original + 2 backups)
- 2 different media types (local + cloud)
- 1 offsite (encrypted cloud storage)

Emergency document kit for critical docs.

---

## Architecture

### Agents

**1. document-classifier** (Sonnet 4 + Vision)
- Auto-categorizes documents using OCR and vision
- Extracts metadata (dates, amounts, vendors)
- Applies naming conventions
- Creates searchable index entries
- Flags importance levels
- Sets expiration tracking

**2. warranty-tracker** (Haiku)
- Manages warranty database
- Tracks coverage periods and expirations
- Sends timely alerts (30/7/1 day warnings)
- Monitors registration requirements
- Manages warranty claims
- Generates status reports

**3. document-searcher** (Sonnet)
- Multi-criteria search across indexed documents
- Full-text OCR search
- Metadata filtering (category, date, amount, vendor)
- Relevance ranking
- Related document discovery
- Quick search templates

**4. review-scheduler** (Haiku)
- Schedules periodic reviews (weekly, monthly, quarterly, annual)
- Generates detailed checklists
- Tracks completion status
- Sends reminders before due dates
- Manages custom reviews (tax prep, insurance renewal)
- Ensures retention compliance

### Skill

**document-management**
- Document categorization taxonomies
- OCR best practices and text extraction
- Filing system structures and naming conventions
- Retention policies (IRS guidelines)
- Expiration tracking rules
- Search strategies and keyword extraction
- Backup methodologies (3-2-1 strategy)
- Review schedules and maintenance tasks

### Templates

**document-index-template.json**
- Searchable index structure
- Metadata schema
- OCR text storage
- Keyword arrays
- Example documents (receipt, contract, warranty, insurance)

**warranty-database-template.json**
- Warranty tracking structure
- Product information
- Coverage details and exclusions
- Alert scheduling
- Claim management
- Example warranties with different statuses

**review-schedule-template.json**
- Annual, quarterly, monthly, weekly review schedules
- Task checklists with time estimates
- Reminder settings
- Custom review examples (tax prep, insurance renewal)
- Completion tracking

---

## Installation

### Prerequisites

- Puerto plugin system installed
- Claude Code CLI
- Python 3.8+ (for OCR processing)
- Optional: Tesseract OCR for advanced text extraction

### Install Plugin

```bash
# Clone or copy plugin to Puerto plugins directory
cp -r document-organizer ~/.puerto/plugins/

# Or use Puerto plugin manager
puerto plugin install document-organizer
```

### Initialize Data Structures

```bash
# Create data directory
mkdir -p ~/Documents/data

# Copy templates to data directory
cp templates/document-index-template.json ~/Documents/data/document-index.json
cp templates/warranty-database-template.json ~/Documents/data/warranty-database.json
cp templates/review-schedule-template.json ~/Documents/data/review-schedule.json
```

### Create Directory Structure

```bash
# Create recommended filing structure
mkdir -p ~/Documents/{Active,Archive,Important,Warranties,Reference}
mkdir -p ~/Documents/Active/{Financial,Legal,Insurance,Medical,Warranties}
mkdir -p ~/Documents/Active/Financial/Receipts
mkdir -p ~/Documents/Important/{Identification,Certificates,Deeds_Titles}
mkdir -p ~/Documents/Reference/Manuals
```

---

## Usage

### Quick Start

**1. Classify a New Document**

```
User: I just scanned a receipt from Best Buy for a laptop purchase.
      Can you categorize it?

Claude: [Activates document-classifier agent]

Agent:
- Analyzes image using vision
- Extracts text via OCR
- Identifies as receipt
- Extracts: date, vendor, items, amount
- Categorizes: Financial/Receipts/Electronics
- Applies naming: 20250115_receipt_bestbuy_laptop_1299.pdf
- Adds to searchable index
- Checks if warranty-eligible

Result: Document classified, filed, and indexed in seconds.
```

**2. Track a Warranty**

```
User: I bought a Samsung TV with a 3-year warranty.
      Can you track it?

Claude: [Activates warranty-tracker agent]

Agent:
- Creates warranty entry
- Calculates expiration date (3 years from purchase)
- Sets alerts (30 days, 7 days, 1 day before)
- Notes registration requirement
- Adds to warranty database

Result: Warranty tracked, alerts scheduled, registration reminder set.
```

**3. Search for Documents**

```
User: Find all receipts from 2024 over $1,000

Claude: [Activates document-searcher agent]

Agent:
- Loads document index
- Filters: category="Receipts", date_range="2024", amount>$1,000
- Ranks by relevance
- Shows results with metadata

Result: 5 documents found
- MacBook Pro - Best Buy - $1,299.99
- Dell Monitor - Amazon - $1,499.00
- Samsung TV - Best Buy - $899.99 (doesn't match, filtered out)
...
```

**4. Check Review Schedule**

```
User: What document reviews are coming up?

Claude: [Activates review-scheduler agent]

Agent:
- Loads review schedule
- Calculates days until each review
- Shows overdue, due soon, upcoming

Result:
DUE SOON:
- Weekly Review - Due in 2 days (~15 min)
- Monthly Review - Due in 12 days (~30 min)

UPCOMING:
- Quarterly Review - Due in 60 days (~45 min)
- Tax Preparation - Due in 80 days (custom)
```

### Advanced Usage

#### Multi-Criteria Search

```
Find tax-deductible receipts from last year over $500:

Criteria:
- tags: "tax_deductible"
- date_range: "2024-01-01" to "2024-12-31"
- amount_range: min=$500
- category: "Financial/Receipts"
```

#### Warranty Expiration Alerts

```
Check warranties expiring in next 90 days:

Agent shows:
HIGH PRIORITY (30 days):
- Laptop Warranty - Dell XPS 15 - Expires 2025-02-10
  Action: Test all hardware, file claims if issues

MEDIUM PRIORITY (60 days):
- Dishwasher - Bosch - Expires 2025-04-15
  Action: Run all cycles, check for issues
```

#### Annual Document Review

```
Generate annual review checklist:

Agent provides:
1. Archive previous year (30 min)
2. Purge expired documents (30 min)
3. Review warranties (20 min)
4. Verify backups (20 min)
5. Update important flags (15 min)
6. Retention compliance (15 min)
7. Update document index (10 min)

Total: 2 hours 20 minutes
```

---

## Workflows

### New Document Intake

```
1. Receive document (scan/download)
   ↓
2. Use document-classifier agent
   ↓
3. Agent processes:
   - OCR extraction
   - Auto-categorization
   - Metadata extraction
   - Naming convention
   - Index creation
   ↓
4. File in appropriate location
   ↓
5. Backup automatically
   ↓
6. Set alerts if applicable
```

### Tax Preparation

```
1. Create custom review "Tax Prep 2024"
   ↓
2. Search for tax-deductible receipts:
   - tags: "tax_deductible"
   - date_range: "2024-01-01" to "2024-12-31"
   ↓
3. Organize by category:
   - Home office
   - Business expenses
   - Medical
   - Charitable donations
   ↓
4. Calculate totals per category
   ↓
5. Generate summary report
   ↓
6. Provide to accountant
```

### Warranty Claim Process

```
1. Product issue occurs
   ↓
2. Search for warranty:
   - keyword: "product name"
   - category: "Warranties"
   ↓
3. Verify coverage:
   - Check warranty status (active/expired)
   - Review coverage details
   - Check exclusions
   ↓
4. File claim using warranty info:
   - Contact: 1-800-XXX-XXXX
   - Claim process: online/phone
   - Required: serial number, proof of purchase
   ↓
5. Track claim in warranty database
   ↓
6. Update with resolution
```

### Insurance Renewal

```
1. Receive renewal reminder (30 days before)
   ↓
2. Review current policy:
   - Coverage amounts
   - Deductibles
   - Premium cost
   ↓
3. Compare quotes from 3 providers
   ↓
4. Make decision (renew or switch)
   ↓
5. Update insurance documents
   ↓
6. Archive old policy
```

---

## Configuration

### Customizing Categories

Edit skill file to add custom categories:

```yaml
Custom_Category:
  - Subcategory_1
  - Subcategory_2
```

### Adjusting Retention Periods

Modify retention rules in skill:

```yaml
Custom_Documents: 5_years
Special_Receipts: 3_years
```

### Alert Timing

Adjust alert schedules in warranty-tracker:

```python
alerts = [
    {"days_before": 60, "priority": "LOW"},
    {"days_before": 30, "priority": "MEDIUM"},
    {"days_before": 7, "priority": "HIGH"}
]
```

### Review Frequency

Modify review schedule:

```json
{
  "monthly": {
    "frequency": "monthly",
    "day": 15
  }
}
```

---

## File Organization

### Recommended Structure

```
~/Documents/
├── Active/                          # Current year documents
│   ├── Financial/
│   │   ├── Receipts/
│   │   │   ├── Electronics/
│   │   │   ├── Groceries/
│   │   │   ├── Dining/
│   │   │   └── Travel/
│   │   ├── Bank_Statements/
│   │   └── Tax_Documents/
│   ├── Legal/
│   │   └── Contracts/
│   │       ├── Employment/
│   │       ├── Real_Estate/
│   │       └── Service_Agreements/
│   ├── Insurance/
│   │   ├── Health/
│   │   ├── Auto/
│   │   └── Home/
│   ├── Medical/
│   └── Warranties/
│
├── Archive/                         # Past years
│   ├── 2024/
│   │   ├── Financial/
│   │   ├── Legal/
│   │   └── Insurance/
│   ├── 2023/
│   └── 2022/
│
├── Important/                       # Critical documents
│   ├── Identification/
│   │   ├── passport.pdf
│   │   ├── birth_certificate.pdf
│   │   └── social_security.pdf
│   ├── Certificates/
│   │   ├── marriage_certificate.pdf
│   │   └── diplomas/
│   ├── Deeds_Titles/
│   │   ├── home_deed.pdf
│   │   └── car_title.pdf
│   └── Tax_Returns/                 # 7 years retention
│
├── Warranties/                      # Active warranties
│   ├── Electronics/
│   ├── Appliances/
│   └── Home_Improvement/
│
├── Reference/                       # Manuals, templates
│   ├── Manuals/
│   ├── Templates/
│   └── Guides/
│
└── data/                           # Plugin databases
    ├── document-index.json
    ├── warranty-database.json
    └── review-schedule.json
```

### Naming Convention

```
Format: {YYYYMMDD}_{category}_{description}_{amount}.{ext}

Examples:
20250115_receipt_bestbuy_laptop_1299.pdf
20250110_contract_employment_acme_corp.pdf
20250105_warranty_samsung_tv_3year.pdf
20241215_insurance_auto_policy_renewal.pdf
20250101_medical_prescription_refill.pdf
```

---

## Backup Strategy

### 3-2-1 Rule

**3 copies:**
1. Original documents in ~/Documents/
2. Local backup on external drive
3. Cloud backup (encrypted)

**2 media types:**
1. Local SSD/Hard drive
2. Cloud storage (Dropbox, Google Drive, iCloud)

**1 offsite:**
- Encrypted cloud backup
- Accessible from anywhere
- Protected from local disasters

### Backup Schedule

**Continuous:**
- Cloud sync (automatic)

**Daily:**
- Cloud backup verification

**Weekly:**
- Local backup to external drive

**Monthly:**
- Backup integrity test (restore sample file)

**Quarterly:**
- Full backup verification
- Test restore procedures

### Encryption

**Critical documents:**
- AES-256 encryption
- Separate encryption for emergency docs
- Password manager for keys
- 2FA on cloud storage

**Emergency Document Kit:**
```
Emergency_Docs/ (encrypted)
├── passport_scan.pdf
├── birth_certificate.pdf
├── insurance_policies.pdf
├── medical_info.pdf
└── financial_accounts.pdf
```

---

## Best Practices

### Document Processing

1. **Process immediately**: Don't let documents pile up
2. **Scan receipts**: Use mobile scanner app right after purchase
3. **Register warranties**: Within 30 days of purchase
4. **Tag important docs**: Flag critical documents immediately
5. **Verify OCR**: Spot-check text extraction accuracy

### Categorization

1. **Be consistent**: Use standard taxonomy from skill
2. **Single category**: Don't duplicate documents across categories
3. **Use tags**: Add tags for cross-category attributes
4. **Update index**: Keep searchable index current

### Retention

1. **Follow policies**: Adhere to IRS 7-year rule for taxes
2. **Review annually**: Purge expired documents each January
3. **Never delete**: Birth certificates, deeds, diplomas
4. **Safety period**: Move to "Purged" folder for 30 days before deleting

### Security

1. **Encrypt critical docs**: Passports, SSN, financial accounts
2. **Secure passwords**: Use password manager for encryption keys
3. **2FA everything**: Cloud storage, email, important accounts
4. **Test restores**: Monthly backup verification

### Maintenance

1. **Weekly**: Process new receipts (15 min)
2. **Monthly**: File documents, check expirations (30 min)
3. **Quarterly**: Review warranties, test backups (45 min)
4. **Annual**: Archive year, purge expired, compliance check (2 hours)

---

## Troubleshooting

### OCR Not Working

**Symptom**: Text not extracted from images

**Solutions**:
1. Ensure image quality is good (300+ DPI)
2. Check file format (PDF, JPG, PNG supported)
3. Install Tesseract OCR if not present
4. Try re-scanning document with better lighting
5. Manually enter key metadata if OCR fails

### Search Returns No Results

**Symptom**: Can't find documents you know exist

**Solutions**:
1. Verify document is in index (check document-index.json)
2. Try broader search terms
3. Check category filters
4. Search by date or amount instead of keywords
5. Rebuild index if corrupted

### Warranty Alerts Not Showing

**Symptom**: Missing warranty expiration alerts

**Solutions**:
1. Check warranty database for alert dates
2. Verify warranty status is "active"
3. Ensure alert_date is in the future
4. Check alert priority settings
5. Re-calculate alert dates if needed

### Backup Failures

**Symptom**: Backup not completing or fails verification

**Solutions**:
1. Check storage space on backup destination
2. Verify network connection for cloud backups
3. Test backup credentials/permissions
4. Check backup logs for specific errors
5. Try manual backup to isolate issue

### Index Out of Sync

**Symptom**: Index shows documents that don't exist or missing new docs

**Solutions**:
1. Run document-classifier on all uncategorized docs
2. Rebuild index from scratch
3. Remove deleted documents from index manually
4. Verify file paths are correct
5. Update index after moving documents

---

## FAQ

**Q: Can I use this for business documents?**
A: Yes! The system works for personal and small business document management. Create custom categories for business needs.

**Q: What happens if I lose my laptop?**
A: Your documents are safe in cloud backup. Restore from encrypted backup to new device. Emergency docs are accessible via password-protected cloud storage.

**Q: How accurate is auto-categorization?**
A: 95%+ accuracy for standard documents (receipts, contracts, warranties). Complex or unusual documents may need manual verification.

**Q: Can I change categories after filing?**
A: Yes. Update the document entry in the index and move the file to the new category folder.

**Q: How much storage do I need?**
A: Depends on volume. Most personal systems use <10GB. Businesses may need 50-100GB. Cloud storage recommendations: Dropbox Plus (2TB), Google Drive (100GB+).

**Q: Does this work with physical documents?**
A: Yes, after scanning. Use a scanner app (Adobe Scan, CamScanner) to create PDFs, then process with document-classifier.

**Q: What if warranty expires and I forgot to check?**
A: Alerts are sent 30, 7, and 1 day before expiration. If missed, the warranty will be marked "expired" in database but kept for reference.

**Q: Can I access documents from my phone?**
A: Yes, if using cloud sync (Dropbox, Google Drive, iCloud). Documents are accessible from any device with cloud access.

**Q: How do I handle multi-year contracts?**
A: Tag with "active_contract", set expiration date to contract end, and add to review schedule for renewal consideration.

**Q: Is this HIPAA compliant for medical records?**
A: Personal use with proper encryption meets HIPAA technical safeguards. For professional medical practices, consult HIPAA compliance specialist.

---

## Examples

### Example 1: Tax Preparation

**Scenario**: Preparing 2024 taxes, need all deductible receipts

```
User: Find all tax-deductible receipts from 2024

document-searcher:
- Searches: tags="tax_deductible", date_range="2024-01-01 to 2024-12-31"
- Finds: 47 documents
- Groups by category:
  - Home office: $3,245
  - Business travel: $1,890
  - Professional services: $2,100
  - Charitable donations: $1,500
- Total deductions: $8,735

User: Create a summary report

Result: Summary with all receipts organized by category, totals calculated,
document paths provided for accountant.
```

### Example 2: Warranty Claim

**Scenario**: Laptop trackpad broken, need to file warranty claim

```
User: My Dell XPS 15 trackpad is broken. Is it under warranty?

warranty-tracker:
- Searches warranty database for "Dell XPS 15"
- Finds: warranty_id war_20240620_001
- Status: Active
- Expires: 2027-06-20 (2.5 years remaining)
- Coverage: Premium Support Plus with accidental damage
- Contact: 1-800-DELL-HELP
- Service tag: DEL123ABC456

User: File a claim

warranty-tracker:
- Creates claim entry
- Claim ID: claim_002
- Issue: Trackpad unresponsive
- Method: Online chat
- Status: Pending
- Updates warranty database

Result: Claim filed, tracking number saved, will update with resolution.
```

### Example 3: Insurance Renewal

**Scenario**: Auto insurance renewal coming up, want to compare rates

```
User: My auto insurance renews in 30 days. Help me review.

document-searcher:
- Finds: Active auto insurance policy
- Policy: Progressive POL-987654321
- Expires: 2026-01-01
- Premium: $1,200/year
- Coverage: Full coverage, $500 deductible

review-scheduler:
- Creates custom review: "Auto Insurance Renewal 2026"
- Due date: 2025-12-01 (30 days before expiration)
- Tasks:
  1. Review current coverage amounts
  2. Get quotes from 3 providers (Geico, State Farm, Allstate)
  3. Compare coverage vs. cost
  4. Make renewal decision by 2025-12-15

Result: Custom review scheduled with reminders 30 days before renewal.
```

### Example 4: Annual Review

**Scenario**: It's January, time for annual document review

```
User: Run my annual document review

review-scheduler:
- Generates complete checklist:

[1] ARCHIVE 2024 DOCUMENTS (30 min)
    - Move Active/2024 to Archive/2024
    - Verify all documents moved
    - Update index file paths

[2] PURGE EXPIRED DOCUMENTS (30 min)
    - Tax docs before 2018 (>7 years)
    - Bank statements before 2024 (>1 year)
    - Receipts before 2024 (>1 year, non-tax)
    - Total to purge: 234 documents

[3] REVIEW WARRANTIES (20 min)
    - Active: 5 warranties
    - Expiring in 2025: 1 (dishwasher)
    - Expired: 2 (can remove)

[4] VERIFY BACKUPS (20 min)
    - Local backup: ✓ Current as of 2025-01-14
    - Cloud backup: ✓ Synced
    - Test restore: sample.pdf restored successfully

[5] UPDATE IMPORTANT FLAGS (15 min)
    - Passport: Expires 2028 ✓
    - Insurance policies: All current ✓
    - Emergency contacts: Updated

[6] RETENTION COMPLIANCE (15 min)
    - Tax documents: Compliant (keeping 7 years)
    - Medical records: Compliant (keeping 7 years)
    - Contracts: Compliant (duration + 7 years)

[7] UPDATE DOCUMENT INDEX (10 min)
    - Total documents: 1,247
    - New in 2024: 198
    - Purged: 234
    - Current total: 1,211

Estimated time: 2 hours 20 minutes
Schedule uninterrupted block for completion.
```

---

## Support

### Getting Help

1. **Documentation**: Read this README and skill documentation
2. **Templates**: Reference template files for structure examples
3. **Community**: Puerto plugin community forums
4. **Issues**: Report bugs on GitHub

### Contributing

Contributions welcome! Areas for improvement:
- Additional document categories
- More OCR providers
- Mobile app integration
- Cloud storage integrations
- AI-powered categorization improvements

### Roadmap

**Version 1.1** (Q2 2025):
- Mobile scanning app integration
- Email auto-filing rules
- Receipt photo → instant categorization
- Multiple language support

**Version 1.2** (Q3 2025):
- Advanced analytics (spending by category)
- Duplicate detection
- OCR confidence scoring
- Bulk operations (re-categorize, rename)

**Version 2.0** (Q4 2025):
- AI recommendations for retention
- Smart folder organization
- Predictive search
- Integration with accounting software

---

## License

MIT License - See LICENSE file for details

---

## Credits

**Created by**: Puerto Team
**Version**: 1.0.0
**Last Updated**: January 2025

Built with Puerto plugin framework for Claude Code.

**Special Thanks**:
- Document management professionals for best practices
- IRS for retention guidelines
- OCR community for text extraction patterns
- Claude Code team for the agent framework

---

## Appendix: Agent Reference

### document-classifier

**Model**: Sonnet 4 (with Vision)
**Tools**: Read, Write, Bash, Glob
**Triggers**: "organize documents", "categorize receipt", "classify this document"

**Capabilities**:
- Vision-based document type detection
- OCR text extraction
- Metadata parsing (dates, amounts, vendors)
- Auto-categorization using taxonomy
- Searchable index creation
- Importance flagging

**Best for**:
- New document intake
- Bulk categorization
- Index building

### warranty-tracker

**Model**: Haiku
**Tools**: Read, Write, Bash
**Triggers**: "track warranty", "check warranty status", "warranty expiring"

**Capabilities**:
- Warranty database management
- Expiration date calculation
- Alert scheduling (30/7/1 day)
- Registration tracking
- Claim management
- Status reports

**Best for**:
- Adding new warranties
- Checking expiring warranties
- Filing warranty claims
- Generating warranty reports

### document-searcher

**Model**: Sonnet
**Tools**: Read, Grep, Glob
**Triggers**: "find document", "search for receipt", "locate warranty"

**Capabilities**:
- Multi-criteria search
- Full-text OCR search
- Metadata filtering
- Relevance ranking
- Related document discovery
- Quick search templates

**Best for**:
- Finding specific documents
- Tax preparation searches
- Warranty lookups
- Insurance policy retrieval

### review-scheduler

**Model**: Haiku
**Tools**: Read, Write, Bash
**Triggers**: "document review", "schedule review", "what reviews are due"

**Capabilities**:
- Review schedule management
- Checklist generation
- Completion tracking
- Reminder scheduling
- Custom review creation
- Retention compliance

**Best for**:
- Annual document reviews
- Periodic maintenance
- Tax preparation planning
- Insurance renewal reminders

---

**Ready to organize your documents? Start with document-classifier to process your first batch!**
