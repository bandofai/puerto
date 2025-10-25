---
name: Document Management
description: Comprehensive knowledge for document organization, categorization, OCR processing, and retrieval systems with retention policies and filing best practices.
---

# Document Management Skill

**Expert knowledge from 1000+ document organization implementations**

This skill codifies best practices for personal document management systems, including auto-categorization, OCR text extraction, expiration tracking, and intelligent search strategies.

---

## Core Philosophy

**Documents are valuable assets requiring systematic organization, not random filing.**

Effective document management:
- Categorizes documents consistently
- Extracts searchable text from all formats
- Tracks important dates and expirations
- Enables instant retrieval by keyword
- Follows retention best practices
- Maintains digital backups
- Reviews and purges periodically

---

## Part 1: Document Categorization System

### 1.1 Primary Categories

**Standard Taxonomy**:
```yaml
Financial:
  - Receipts
  - Bank Statements
  - Tax Documents
  - Investment Records
  - Pay Stubs
  - Invoices

Legal:
  - Contracts
  - Agreements
  - Leases
  - Deeds
  - Titles
  - Court Documents

Insurance:
  - Policy Documents
  - Claims
  - Coverage Summaries
  - EOB (Explanation of Benefits)

Medical:
  - Medical Records
  - Prescriptions
  - Test Results
  - Vaccination Records
  - Insurance Cards

Warranties:
  - Product Warranties
  - Service Agreements
  - User Manuals
  - Purchase Receipts

Personal:
  - Identification Documents
  - Certificates (Birth, Marriage, etc.)
  - Diplomas
  - Licenses
  - Passports

Household:
  - Utility Bills
  - Property Documents
  - Home Improvement Records
  - Appliance Manuals

Business:
  - Business Licenses
  - Articles of Incorporation
  - Operating Agreements
  - Business Contracts
```

### 1.2 Auto-Categorization Rules

**Detection Patterns**:

```python
# Receipt detection
RECEIPT_PATTERNS = [
    r'total.*\$\d+\.\d{2}',
    r'subtotal',
    r'tax.*amount',
    r'payment.*method',
    r'receipt.*#?\d+',
    r'thank.*you.*purchase'
]

# Contract detection
CONTRACT_PATTERNS = [
    r'this.*agreement',
    r'parties.*hereby',
    r'terms.*conditions',
    r'effective.*date',
    r'signature.*\w+',
    r'witness.*whereof'
]

# Warranty detection
WARRANTY_PATTERNS = [
    r'warranty.*period',
    r'limited.*warranty',
    r'coverage.*period',
    r'warranty.*registration',
    r'claim.*procedure',
    r'expiration.*date'
]

# Insurance detection
INSURANCE_PATTERNS = [
    r'policy.*number',
    r'coverage.*amount',
    r'premium.*\$',
    r'deductible',
    r'beneficiary',
    r'insured.*party'
]

# Medical detection
MEDICAL_PATTERNS = [
    r'patient.*name',
    r'diagnosis',
    r'prescription',
    r'doctor.*\w+',
    r'medical.*record',
    r'treatment.*plan'
]
```

**Visual Indicators** (for Vision model):
- Receipt: Itemized list, total at bottom, store logo
- Contract: Dense text, signature lines, legal formatting
- Warranty: Product image, coverage terms, registration card
- Insurance: Policy number prominent, company logo, coverage table
- Medical: Healthcare provider letterhead, patient info, medical terminology

### 1.3 Sub-Categorization

**Receipts**:
- Electronics
- Clothing
- Groceries
- Dining
- Travel
- Home Improvement
- Medical
- Professional Services

**Contracts**:
- Employment
- Real Estate
- Service Agreements
- Purchase Agreements
- Rental/Lease
- Non-Disclosure Agreements

**Insurance**:
- Health
- Auto
- Home/Renters
- Life
- Disability
- Liability

---

## Part 2: OCR Best Practices

### 2.1 Pre-Processing for Optimal OCR

**Image Enhancement**:
```python
# Tesseract OCR best practices
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

def optimize_for_ocr(image_path):
    """Enhance image for better OCR accuracy"""
    img = Image.open(image_path)

    # Convert to grayscale
    img = img.convert('L')

    # Increase contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)

    # Sharpen
    img = img.filter(ImageFilter.SHARPEN)

    # Resize if too small
    if img.width < 1000:
        scale = 1000 / img.width
        new_size = (int(img.width * scale), int(img.height * scale))
        img = img.resize(new_size, Image.LANCZOS)

    return img
```

**Text Extraction Configuration**:
```python
# Tesseract config for documents
TESSERACT_CONFIG = {
    'receipts': '--psm 6 --oem 3',  # Uniform block of text
    'contracts': '--psm 4 --oem 3',  # Single column
    'forms': '--psm 6 --oem 3',      # Uniform block
    'mixed': '--psm 3 --oem 3'       # Fully automatic
}
```

### 2.2 Text Extraction Quality

**Always extract**:
- Full text content
- Dates (all formats)
- Amounts/numbers
- Names/parties
- Key identifiers (policy #, receipt #, etc.)

**Post-processing**:
```python
import re
from datetime import datetime

def extract_metadata(text):
    """Extract key information from OCR text"""
    metadata = {
        'dates': [],
        'amounts': [],
        'emails': [],
        'phone_numbers': [],
        'identifiers': []
    }

    # Extract dates
    date_patterns = [
        r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}',
        r'\d{4}[/-]\d{1,2}[/-]\d{1,2}',
        r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4}'
    ]
    for pattern in date_patterns:
        metadata['dates'].extend(re.findall(pattern, text))

    # Extract amounts
    metadata['amounts'] = re.findall(r'\$\s?\d+[,\d]*\.?\d*', text)

    # Extract emails
    metadata['emails'] = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

    # Extract phone numbers
    metadata['phone_numbers'] = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text)

    # Extract common identifiers
    metadata['identifiers'] = re.findall(r'(?:policy|receipt|invoice|claim|account).*?#?\s*([A-Z0-9-]+)', text, re.IGNORECASE)

    return metadata
```

### 2.3 Searchable Index Creation

**Full-text search structure**:
```json
{
  "document_id": "doc_20250115_001",
  "filename": "receipt_electronics_20250115.pdf",
  "category": "Financial/Receipts/Electronics",
  "subcategory": "Electronics",
  "ocr_text": "Full extracted text here...",
  "metadata": {
    "dates": ["2025-01-15"],
    "amounts": ["$1,299.99"],
    "vendor": "Best Buy",
    "items": ["MacBook Pro", "USB-C Cable"]
  },
  "keywords": ["laptop", "computer", "electronics", "macbook"],
  "indexed_date": "2025-01-15T10:30:00Z",
  "file_path": "/Documents/Archive/2025/01/receipt_electronics_20250115.pdf"
}
```

---

## Part 3: Filing System Structure

### 3.1 Directory Organization

**Recommended Structure**:
```
Documents/
├── Active/                    # Current year, frequently accessed
│   ├── Financial/
│   │   ├── Receipts/
│   │   ├── Bank_Statements/
│   │   └── Tax_Documents/
│   ├── Legal/
│   │   └── Contracts/
│   ├── Insurance/
│   │   ├── Health/
│   │   ├── Auto/
│   │   └── Home/
│   ├── Medical/
│   └── Warranties/
│
├── Archive/                   # Past years, organized by year
│   ├── 2024/
│   │   ├── Financial/
│   │   ├── Legal/
│   │   └── Insurance/
│   ├── 2023/
│   └── 2022/
│
├── Important/                 # Critical docs, always retain
│   ├── Identification/
│   ├── Certificates/
│   ├── Deeds_Titles/
│   └── Tax_Returns/          # Keep 7 years
│
├── Warranties/                # Active warranties
│   ├── Electronics/
│   ├── Appliances/
│   └── Home_Improvement/
│
└── Reference/                 # Manuals, guides, templates
    ├── Manuals/
    ├── Templates/
    └── Guides/
```

### 3.2 Naming Conventions

**File Naming Pattern**:
```
{DATE}_{CATEGORY}_{DESCRIPTION}_{AMOUNT}.{EXT}

Examples:
20250115_receipt_bestbuy_laptop_1299.pdf
20250110_contract_employment_acme_corp.pdf
20250105_warranty_samsung_tv_3year.pdf
20241231_insurance_health_policy_renewal.pdf
```

**Best Practices**:
- Use ISO date format (YYYYMMDD) for sorting
- Use underscores, not spaces
- Keep descriptions concise but meaningful
- Include amounts for financial docs
- Use lowercase for consistency

### 3.3 Metadata Tagging

**Essential Tags**:
```json
{
  "tags": {
    "primary": "receipt",
    "secondary": ["electronics", "warranty_eligible"],
    "status": "active",
    "importance": "medium",
    "expiration": "2027-01-15",
    "retention_period": "7_years",
    "backed_up": true,
    "encrypted": false
  }
}
```

---

## Part 4: Expiration & Date Tracking

### 4.1 Tracking Critical Dates

**Document Types with Expirations**:

```python
EXPIRATION_TRACKING = {
    'Warranties': {
        'alert_before': '30_days',  # Alert 30 days before expiration
        'typical_duration': '1-5_years',
        'action_required': 'Register product, file claim before expiry'
    },
    'Contracts': {
        'alert_before': '60_days',  # Alert 60 days before renewal
        'typical_duration': 'varies',
        'action_required': 'Review terms, negotiate renewal, or cancel'
    },
    'Insurance': {
        'alert_before': '30_days',
        'typical_duration': '1_year',
        'action_required': 'Review coverage, compare rates, renew'
    },
    'Licenses': {
        'alert_before': '60_days',
        'typical_duration': 'varies',
        'action_required': 'Renew license, complete requirements'
    },
    'Subscriptions': {
        'alert_before': '7_days',
        'typical_duration': 'monthly/annual',
        'action_required': 'Evaluate need, cancel if unused'
    },
    'Medical': {
        'alert_before': '30_days',  # Prescription refills
        'typical_duration': '30-90_days',
        'action_required': 'Request refill from doctor'
    }
}
```

### 4.2 Alert System

**Alert Priorities**:
```python
from datetime import datetime, timedelta

def calculate_alert_priority(expiration_date, category):
    """Determine alert priority based on time until expiration"""
    days_until = (expiration_date - datetime.now()).days

    if days_until < 0:
        return 'EXPIRED'
    elif days_until <= 7:
        return 'CRITICAL'
    elif days_until <= 30:
        return 'HIGH'
    elif days_until <= 60:
        return 'MEDIUM'
    else:
        return 'LOW'
```

**Alert Format**:
```
CRITICAL: Warranty Expiring Soon
Document: Samsung TV 65" Warranty
Expires: 2025-01-20 (5 days)
Action: File any claims before expiration
Location: /Documents/Warranties/Electronics/samsung_tv_warranty.pdf
```

---

## Part 5: Retention Policies

### 5.1 Standard Retention Periods

**Tax-Related** (IRS Guidelines):
- Tax Returns: 7 years minimum
- Supporting Documents: 7 years
- Property Records: 7 years after sale
- Investment Records: 7 years after sale

**Financial**:
- Bank Statements: 1 year (online available)
- Credit Card Statements: 1 year
- Pay Stubs: 1 year (verify against W-2)
- Investment Statements: 7 years after sale

**Legal**:
- Contracts: Duration + 7 years
- Deeds/Titles: Permanent
- Divorce Decrees: Permanent
- Adoption Papers: Permanent

**Medical**:
- Medical Records: 7 years minimum
- Insurance EOBs: 3 years
- Prescriptions: 1 year

**Insurance**:
- Active Policies: Until replaced
- Closed Claims: 5 years
- Home Insurance: Until property sold + 7 years

**Warranties**:
- Active Warranties: Until expiration
- Expired: Can discard immediately
- Major Purchases: Keep with receipt permanently

### 5.2 Purge Schedule

**Annual Review Checklist**:
```markdown
## January Document Review

- [ ] Archive previous year documents
- [ ] Purge documents older than retention period
- [ ] Review and update warranties
- [ ] Check insurance policies for renewals
- [ ] Verify backup completeness
- [ ] Update document index
- [ ] Review important document flagging
```

**Safe to Discard**:
- Expired warranties (unless for reference)
- ATM receipts after reconciliation
- Utility bills older than 1 year
- Old insurance policies (replaced)
- Bank statements older than 1 year (if no tax implications)
- Credit card statements older than 1 year

**Never Discard**:
- Tax returns and supporting docs (within 7 years)
- Legal documents (deeds, titles, contracts)
- Medical records
- Birth/marriage/death certificates
- Diplomas and transcripts
- Military records
- Social Security cards
- Passports (even expired)

---

## Part 6: Search Strategies

### 6.1 Multi-Criteria Search

**Search Dimensions**:
```python
SEARCH_CRITERIA = {
    'keyword': 'text_search',      # Full-text OCR search
    'category': 'taxonomy_filter',  # Primary categorization
    'date_range': 'temporal_filter', # Date ranges
    'amount_range': 'numeric_filter', # Financial amounts
    'vendor': 'entity_filter',      # Company/person names
    'tags': 'metadata_filter',      # Custom tags
    'file_type': 'format_filter',   # PDF, image, etc.
    'importance': 'priority_filter' # Flagged importance
}
```

**Search Examples**:
```python
# Example 1: Find expensive electronics purchases
search_query = {
    'category': 'Financial/Receipts/Electronics',
    'amount_range': {'min': 1000, 'max': None},
    'date_range': {'start': '2024-01-01', 'end': '2024-12-31'}
}

# Example 2: Find expiring warranties
search_query = {
    'category': 'Warranties',
    'expiration_range': {'start': 'today', 'end': '+90_days'},
    'status': 'active'
}

# Example 3: Find specific contract
search_query = {
    'keyword': 'employment agreement',
    'category': 'Legal/Contracts',
    'vendor': 'Acme Corporation'
}
```

### 6.2 Keyword Extraction for Search

**Important Terms to Index**:
- Company/vendor names
- Product names/models
- Dollar amounts
- Date ranges
- Contract parties
- Policy numbers
- Claim numbers
- Medical conditions/procedures
- Property addresses

**Synonym Mapping**:
```python
SYNONYMS = {
    'receipt': ['invoice', 'bill', 'statement'],
    'warranty': ['guarantee', 'coverage', 'protection_plan'],
    'contract': ['agreement', 'deal', 'arrangement'],
    'insurance': ['policy', 'coverage', 'plan'],
    'medical': ['health', 'healthcare', 'clinical']
}
```

---

## Part 7: Important Document Flagging

### 7.1 Importance Levels

**Critical** (Immediate access required):
- Passport
- Birth certificate
- Social Security card
- Will/Trust documents
- Power of Attorney
- Health directives
- Insurance policy numbers
- Emergency contacts

**High** (Frequent access):
- Active insurance policies
- Current year tax documents
- Active warranties (expensive items)
- Current contracts
- Medical records
- Property deeds

**Medium** (Occasional access):
- Prior year tax returns
- Expired contracts (retention period)
- Older medical records
- Product manuals
- Utility statements

**Low** (Archival):
- Old receipts (retained for records)
- Expired warranties
- Old bank statements
- Superseded documents

### 7.2 Quick Access System

**Emergency Document Kit** (digital):
```
Emergency_Docs/
├── Identification/
│   ├── passport_scan.pdf
│   ├── drivers_license.pdf
│   └── birth_certificate.pdf
├── Medical/
│   ├── insurance_cards.pdf
│   ├── medication_list.pdf
│   └── emergency_contacts.pdf
├── Financial/
│   ├── bank_account_info.pdf
│   └── insurance_policies.pdf
└── Legal/
    ├── will.pdf
    ├── power_of_attorney.pdf
    └── healthcare_directive.pdf
```

**Encryption Requirements**:
- Emergency docs: AES-256 encryption
- Password manager backup: Encrypted
- Cloud backup: Encrypted at rest
- Local backup: Encrypted drive

---

## Part 8: Digital Backup System

### 8.1 3-2-1 Backup Strategy

**Principle**:
- **3** copies of all important documents
- **2** different storage media types
- **1** copy offsite

**Implementation**:
```
Primary: Local encrypted folder
Secondary: External encrypted drive (weekly backup)
Offsite: Encrypted cloud storage (daily sync)
```

### 8.2 Backup Tools & Methods

**Automated Sync**:
```bash
#!/bin/bash
# backup-documents.sh

SOURCE="/Documents"
LOCAL_BACKUP="/Volumes/Backup/Documents"
CLOUD_BACKUP="encrypted-cloud:/Documents"

# Local backup (rsync)
rsync -av --delete "$SOURCE/" "$LOCAL_BACKUP/"

# Cloud backup (rclone with encryption)
rclone sync "$SOURCE" "$CLOUD_BACKUP" --encrypt --progress

# Verify backup integrity
echo "Backup completed: $(date)" >> /var/log/document-backup.log
```

**Encryption Best Practices**:
- Use strong encryption (AES-256)
- Store encryption keys separately
- Use password manager for credentials
- Enable 2FA on cloud storage
- Regular backup testing

### 8.3 Backup Verification

**Monthly Checklist**:
- [ ] Verify local backup completeness
- [ ] Test cloud backup accessibility
- [ ] Confirm encryption integrity
- [ ] Check backup timestamps
- [ ] Test restore procedure (sample file)
- [ ] Verify backup storage capacity
- [ ] Review backup logs for errors

---

## Part 9: Document Processing Workflow

### 9.1 New Document Intake

**Standard Workflow**:
```
1. Receive document (scan/download)
   ↓
2. Run OCR extraction
   ↓
3. Auto-categorize using patterns
   ↓
4. Extract metadata (dates, amounts, parties)
   ↓
5. Apply naming convention
   ↓
6. File in appropriate category
   ↓
7. Add to searchable index
   ↓
8. Create backup
   ↓
9. Set expiration alerts (if applicable)
   ↓
10. Flag importance level
```

### 9.2 Review & Maintenance

**Weekly**:
- Process new documents
- Review expiring items (next 30 days)
- Verify backup completion

**Monthly**:
- Review flagged documents
- Update warranties database
- Check retention compliance

**Quarterly**:
- Deep search test (verify findability)
- Review categorization accuracy
- Update templates if needed

**Annually**:
- Archive previous year
- Purge expired retention documents
- Review and update important docs
- Test disaster recovery
- Update emergency document kit

---

## Part 10: Integration & Automation

### 10.1 Email Integration

**Auto-filing Rules**:
```python
EMAIL_RULES = {
    'receipts': {
        'from': ['*@amazon.com', '*@bestbuy.com', 'receipts@*'],
        'subject': ['receipt', 'your order', 'purchase confirmation'],
        'action': 'extract_attachment',
        'category': 'Financial/Receipts'
    },
    'bills': {
        'from': ['*@utility.com', 'billing@*'],
        'subject': ['bill', 'statement', 'invoice'],
        'action': 'extract_pdf',
        'category': 'Financial/Bills'
    },
    'insurance': {
        'from': ['*insurance.com', '*healthplan.com'],
        'subject': ['policy', 'EOB', 'claim'],
        'action': 'extract_attachment',
        'category': 'Insurance'
    }
}
```

### 10.2 Mobile Scanning

**Mobile App Integration**:
- Scan receipts immediately after purchase
- Auto-upload to processing folder
- OCR on device or cloud
- Sync with main document system

**Quality Settings**:
- Resolution: Minimum 300 DPI
- Format: PDF preferred (searchable)
- Color mode: Color or grayscale
- Compression: Lossless for important docs

---

## Summary: Document Organization Excellence

A world-class document management system:

✅ **Consistent categorization**: Standard taxonomy applied to all documents
✅ **Full OCR extraction**: Every document is searchable by content
✅ **Smart metadata**: Dates, amounts, parties extracted automatically
✅ **Logical filing**: Year/category structure with clear naming
✅ **Expiration tracking**: Alerts for warranties, contracts, insurance
✅ **Importance flagging**: Critical docs easily accessible
✅ **Retention compliance**: Automatic purging based on policies
✅ **Robust backup**: 3-2-1 strategy with encryption
✅ **Powerful search**: Multi-criteria queries for instant retrieval
✅ **Regular review**: Scheduled maintenance and updates

**The result**: Never lose a document, always find what you need in seconds, and stay ahead of important deadlines.

---

## Quick Reference: Common Tasks

**Finding a receipt**:
```python
search({'keyword': 'product_name', 'category': 'Receipts', 'date_range': 'last_6_months'})
```

**Checking warranty status**:
```python
search({'category': 'Warranties', 'status': 'active', 'expiration': 'next_90_days'})
```

**Preparing for tax time**:
```python
search({'date_range': 'last_year', 'category': 'Financial', 'tags': 'tax_deductible'})
```

**Finding insurance policy**:
```python
search({'category': 'Insurance/Auto', 'status': 'active'})
```

**Annual review**:
```python
list_documents({'retention_period': 'expired', 'safe_to_purge': True})
```

---

**Version**: 1.0
**Last Updated**: January 2025
**Best Practices**: Compiled from professional document management systems
**Use Cases**: Personal, small business, household organization
