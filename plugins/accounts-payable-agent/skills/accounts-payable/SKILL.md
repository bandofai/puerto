# Accounts Payable Skill

**Professional accounts payable automation patterns, workflows, and best practices**

This skill provides battle-tested frameworks for invoice processing, approval routing, payment scheduling, vendor management, reconciliation, and compliance. Based on patterns from thousands of AP transactions across industries.

**Usage**: Read this entire skill before performing ANY accounts payable task to ensure professional quality, compliance, and efficiency.

---

## Table of Contents

1. [Invoice Processing & OCR](#1-invoice-processing--ocr)
2. [Approval Routing Workflows](#2-approval-routing-workflows)
3. [Payment Scheduling](#3-payment-scheduling)
4. [Vendor Database Management](#4-vendor-database-management)
5. [Reconciliation & Matching](#5-reconciliation--matching)
6. [Exception Handling](#6-exception-handling)
7. [Compliance & Controls](#7-compliance--controls)
8. [Metrics & Reporting](#8-metrics--reporting)

---

## 1. Invoice Processing & OCR

### 1.1 Invoice Data Extraction

**OCR Tools & Methods**:

**Python-based OCR** (Tesseract):
```python
import pytesseract
from PIL import Image
import pdf2image
import re

def extract_invoice_data(file_path):
    """Extract text and structured data from invoice PDF/image"""

    # Convert PDF to images if needed
    if file_path.endswith('.pdf'):
        images = pdf2image.convert_from_path(file_path)
        image = images[0]  # Process first page
    else:
        image = Image.open(file_path)

    # Extract text with OCR
    text = pytesseract.image_to_string(image)

    # Parse structured data
    invoice_data = {
        'invoice_number': extract_invoice_number(text),
        'invoice_date': extract_date(text),
        'due_date': extract_due_date(text),
        'vendor_name': extract_vendor_name(text),
        'vendor_address': extract_vendor_address(text),
        'total_amount': extract_total_amount(text),
        'line_items': extract_line_items(text),
        'tax_amount': extract_tax(text),
        'payment_terms': extract_payment_terms(text)
    }

    return invoice_data, text

def extract_invoice_number(text):
    """Extract invoice number using pattern matching"""
    patterns = [
        r'Invoice\s*#\s*[:\-]?\s*(\d+)',
        r'INV\s*[:\-]?\s*(\d+)',
        r'Invoice\s+Number\s*[:\-]?\s*(\d+)',
        r'Invoice\s+No\.\s*[:\-]?\s*(\d+)'
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)

    return None

def extract_date(text):
    """Extract invoice date"""
    patterns = [
        r'Invoice\s+Date\s*[:\-]?\s*(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4})',
        r'Date\s*[:\-]?\s*(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4})',
        r'(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4})'
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return normalize_date(match.group(1))

    return None

def extract_total_amount(text):
    """Extract total amount"""
    patterns = [
        r'Total\s*[:\-]?\s*\$?\s*([\d,]+\.\d{2})',
        r'Amount\s+Due\s*[:\-]?\s*\$?\s*([\d,]+\.\d{2})',
        r'Balance\s+Due\s*[:\-]?\s*\$?\s*([\d,]+\.\d{2})'
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            amount_str = match.group(1).replace(',', '')
            return float(amount_str)

    return None

def extract_line_items(text):
    """Extract line items from invoice"""
    # Look for table patterns
    lines = text.split('\n')
    line_items = []

    in_items_section = False
    for line in lines:
        # Detect start of line items
        if re.search(r'(Description|Item|Product)', line, re.IGNORECASE):
            in_items_section = True
            continue

        # Detect end of line items
        if re.search(r'(Subtotal|Total|Tax)', line, re.IGNORECASE):
            in_items_section = False

        # Parse line items
        if in_items_section:
            # Pattern: description quantity unit_price amount
            match = re.search(r'(.+?)\s+(\d+)\s+\$?([\d,]+\.\d{2})\s+\$?([\d,]+\.\d{2})', line)
            if match:
                line_items.append({
                    'description': match.group(1).strip(),
                    'quantity': int(match.group(2)),
                    'unit_price': float(match.group(3).replace(',', '')),
                    'amount': float(match.group(4).replace(',', ''))
                })

    return line_items
```

**Cloud OCR Services** (for higher accuracy):
```python
# Google Cloud Vision API
from google.cloud import vision

def ocr_with_google_vision(file_path):
    """Use Google Cloud Vision for OCR"""
    client = vision.ImageAnnotatorClient()

    with open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)

    return response.full_text_annotation.text

# AWS Textract (specialized for invoices)
import boto3

def ocr_with_aws_textract(file_path):
    """Use AWS Textract - optimized for invoices"""
    textract = boto3.client('textract')

    with open(file_path, 'rb') as document:
        response = textract.analyze_expense(
            Document={'Bytes': document.read()}
        )

    # Textract automatically extracts structured invoice data
    expense_documents = response['ExpenseDocuments']

    invoice_data = {}
    for doc in expense_documents:
        for field in doc['SummaryFields']:
            field_type = field['Type']['Text']
            field_value = field['ValueDetection']['Text']

            if field_type == 'INVOICE_NUMBER':
                invoice_data['invoice_number'] = field_value
            elif field_type == 'INVOICE_DATE':
                invoice_data['invoice_date'] = field_value
            elif field_type == 'TOTAL':
                invoice_data['total_amount'] = float(field_value.replace('$', '').replace(',', ''))

    return invoice_data
```

### 1.2 Invoice Validation Rules

**Mandatory Field Validation**:
```python
def validate_invoice(invoice_data):
    """Validate invoice has required fields"""

    validation_errors = []
    warnings = []

    # Required fields
    required_fields = [
        'invoice_number',
        'invoice_date',
        'vendor_name',
        'total_amount'
    ]

    for field in required_fields:
        if not invoice_data.get(field):
            validation_errors.append(f"Missing required field: {field}")

    # Business rule validations

    # 1. Invoice number must be unique
    if is_duplicate_invoice(invoice_data['invoice_number'], invoice_data['vendor_name']):
        validation_errors.append(f"Duplicate invoice: {invoice_data['invoice_number']} already processed")

    # 2. Invoice date should not be in the future
    if invoice_data.get('invoice_date'):
        if parse_date(invoice_data['invoice_date']) > datetime.now():
            validation_errors.append("Invoice date is in the future")

    # 3. Invoice date should not be too old (configurable threshold)
    if invoice_data.get('invoice_date'):
        days_old = (datetime.now() - parse_date(invoice_data['invoice_date'])).days
        if days_old > 180:  # 6 months
            warnings.append(f"Invoice is {days_old} days old (older than 6 months)")

    # 4. Amount must be positive
    if invoice_data.get('total_amount'):
        if invoice_data['total_amount'] <= 0:
            validation_errors.append("Invoice amount must be positive")

    # 5. Amount should be reasonable (not suspiciously large)
    if invoice_data.get('total_amount'):
        if invoice_data['total_amount'] > 1000000:  # $1M threshold
            warnings.append(f"Large invoice amount: ${invoice_data['total_amount']:,.2f} - requires executive approval")

    # 6. Line items should sum to total (with tax)
    if invoice_data.get('line_items') and invoice_data.get('total_amount'):
        line_items_sum = sum(item['amount'] for item in invoice_data['line_items'])
        tax = invoice_data.get('tax_amount', 0)
        expected_total = line_items_sum + tax

        if abs(expected_total - invoice_data['total_amount']) > 0.01:
            validation_errors.append(
                f"Line items + tax (${expected_total:.2f}) doesn't match total (${invoice_data['total_amount']:.2f})"
            )

    # 7. Vendor must exist in vendor database
    if invoice_data.get('vendor_name'):
        vendor = lookup_vendor(invoice_data['vendor_name'])
        if not vendor:
            warnings.append(f"Vendor '{invoice_data['vendor_name']}' not found in database - needs to be added")

    return {
        'is_valid': len(validation_errors) == 0,
        'errors': validation_errors,
        'warnings': warnings
    }
```

### 1.3 Invoice Processing Workflow

**Standard Processing Flow**:
```
1. RECEIVE Invoice (email, portal upload, mail scan)
   ↓
2. OCR & DATA EXTRACTION
   - Extract invoice number, date, vendor, amount, line items
   - Parse payment terms
   ↓
3. VALIDATION
   - Check required fields
   - Verify not duplicate
   - Validate amounts
   - Check vendor in database
   ↓
4. ENRICHMENT
   - Match to Purchase Order (if exists)
   - Lookup vendor payment terms
   - Assign GL codes to line items
   - Calculate due date
   ↓
5. APPROVAL ROUTING
   - Determine approvers based on amount + department
   - Send for approval
   - Track approval status
   ↓
6. PAYMENT SCHEDULING
   - Schedule payment based on due date and cash flow
   - Optimize for discounts (e.g., 2/10 net 30)
   ↓
7. PAYMENT EXECUTION
   - Generate payment file (ACH, check, wire)
   - Record payment in accounting system
   ↓
8. RECONCILIATION
   - Match invoice to PO and receipt
   - Match payment to bank statement
   - Close invoice
```

**Workflow Implementation**:
```python
def process_invoice_workflow(invoice_file):
    """Complete invoice processing workflow"""

    workflow_log = []

    # Step 1: OCR & Extraction
    workflow_log.append("Step 1: Extracting invoice data...")
    invoice_data, raw_text = extract_invoice_data(invoice_file)

    # Step 2: Validation
    workflow_log.append("Step 2: Validating invoice...")
    validation_result = validate_invoice(invoice_data)

    if not validation_result['is_valid']:
        workflow_log.append(f"VALIDATION FAILED: {validation_result['errors']}")
        return {
            'status': 'validation_failed',
            'errors': validation_result['errors'],
            'log': workflow_log
        }

    # Step 3: Enrichment
    workflow_log.append("Step 3: Enriching invoice data...")

    # Try to match to PO
    po = find_matching_po(invoice_data)
    if po:
        invoice_data['po_number'] = po['po_number']
        invoice_data['gl_codes'] = po['gl_codes']
        workflow_log.append(f"Matched to PO: {po['po_number']}")
    else:
        # Manual GL coding needed
        workflow_log.append("No matching PO - GL coding required")
        invoice_data['requires_gl_coding'] = True

    # Lookup vendor
    vendor = lookup_vendor(invoice_data['vendor_name'])
    if vendor:
        invoice_data['vendor_id'] = vendor['vendor_id']
        invoice_data['payment_terms'] = vendor['payment_terms']
        invoice_data['preferred_payment_method'] = vendor['payment_method']
        workflow_log.append(f"Vendor found: {vendor['vendor_name']}")

    # Calculate due date
    invoice_data['due_date'] = calculate_due_date(
        invoice_data['invoice_date'],
        invoice_data.get('payment_terms', 'Net 30')
    )

    # Step 4: Approval Routing
    workflow_log.append("Step 4: Routing for approval...")
    approvers = determine_approvers(invoice_data)

    invoice_data['approvers'] = approvers
    invoice_data['approval_status'] = 'pending'

    send_for_approval(invoice_data, approvers)
    workflow_log.append(f"Sent to approvers: {[a['name'] for a in approvers]}")

    # Step 5: Save invoice record
    invoice_id = save_invoice_record(invoice_data)
    workflow_log.append(f"Invoice saved with ID: {invoice_id}")

    return {
        'status': 'success',
        'invoice_id': invoice_id,
        'invoice_data': invoice_data,
        'warnings': validation_result['warnings'],
        'log': workflow_log
    }
```

### 1.4 OCR Quality Assurance

**Confidence Scoring**:
```python
def assess_ocr_confidence(invoice_data, raw_text):
    """Assess confidence in OCR extraction"""

    confidence_scores = {}

    # Check if key fields were extracted
    if invoice_data.get('invoice_number'):
        confidence_scores['invoice_number'] = 0.9  # High confidence if found
    else:
        confidence_scores['invoice_number'] = 0.0

    # Check amount format (should have 2 decimal places)
    if invoice_data.get('total_amount'):
        amount_str = str(invoice_data['total_amount'])
        if '.' in amount_str and len(amount_str.split('.')[1]) == 2:
            confidence_scores['total_amount'] = 0.95
        else:
            confidence_scores['total_amount'] = 0.6
    else:
        confidence_scores['total_amount'] = 0.0

    # Check date format
    if invoice_data.get('invoice_date'):
        try:
            parse_date(invoice_data['invoice_date'])
            confidence_scores['invoice_date'] = 0.9
        except:
            confidence_scores['invoice_date'] = 0.4
    else:
        confidence_scores['invoice_date'] = 0.0

    # Overall confidence
    overall_confidence = sum(confidence_scores.values()) / len(confidence_scores)

    # Recommend manual review if confidence < 80%
    needs_manual_review = overall_confidence < 0.8

    return {
        'field_confidence': confidence_scores,
        'overall_confidence': overall_confidence,
        'needs_manual_review': needs_manual_review
    }
```

---

## 2. Approval Routing Workflows

### 2.1 Approval Matrix Design

**Standard Approval Levels**:

```python
# Define approval matrix
APPROVAL_MATRIX = {
    # Amount thresholds and required approvers
    'thresholds': [
        {
            'min_amount': 0,
            'max_amount': 1000,
            'approvers': ['manager'],
            'description': 'Manager approval only'
        },
        {
            'min_amount': 1000,
            'max_amount': 5000,
            'approvers': ['manager', 'department_head'],
            'description': 'Manager + Department Head'
        },
        {
            'min_amount': 5000,
            'max_amount': 25000,
            'approvers': ['manager', 'department_head', 'finance_director'],
            'description': 'Manager + Dept Head + Finance Director'
        },
        {
            'min_amount': 25000,
            'max_amount': 100000,
            'approvers': ['manager', 'department_head', 'finance_director', 'cfo'],
            'description': 'Manager + Dept Head + Finance + CFO'
        },
        {
            'min_amount': 100000,
            'max_amount': float('inf'),
            'approvers': ['manager', 'department_head', 'finance_director', 'cfo', 'ceo'],
            'description': 'Full executive approval required'
        }
    ],

    # Department-specific overrides
    'department_rules': {
        'IT': {
            'software_threshold': 10000,  # IT manager can approve software < $10K
            'hardware_threshold': 25000    # IT director for hardware < $25K
        },
        'Marketing': {
            'campaign_threshold': 50000    # CMO approval for campaigns < $50K
        }
    },

    # Vendor-specific rules
    'vendor_rules': {
        'pre_approved_vendors': [
            # These vendors have blanket approval up to certain amounts
            {'vendor_id': 'VENDOR-001', 'auto_approve_up_to': 5000},
            {'vendor_id': 'VENDOR-002', 'auto_approve_up_to': 2500}
        ]
    }
}

def determine_approvers(invoice_data):
    """Determine who needs to approve based on amount and context"""

    amount = invoice_data['total_amount']
    department = invoice_data.get('department', 'General')
    vendor_id = invoice_data.get('vendor_id')

    # Check for auto-approval (pre-approved vendor)
    for vendor_rule in APPROVAL_MATRIX['vendor_rules']['pre_approved_vendors']:
        if vendor_id == vendor_rule['vendor_id']:
            if amount <= vendor_rule['auto_approve_up_to']:
                return [{
                    'role': 'auto_approved',
                    'name': 'System',
                    'reason': f"Pre-approved vendor up to ${vendor_rule['auto_approve_up_to']:,}"
                }]

    # Find threshold tier
    threshold_tier = None
    for tier in APPROVAL_MATRIX['thresholds']:
        if tier['min_amount'] <= amount < tier['max_amount']:
            threshold_tier = tier
            break

    if not threshold_tier:
        raise ValueError(f"No approval tier found for amount: ${amount:,}")

    # Build approver list
    approvers = []

    for role in threshold_tier['approvers']:
        approver = get_approver_for_role(role, department)
        if approver:
            approvers.append({
                'role': role,
                'name': approver['name'],
                'email': approver['email'],
                'approval_status': 'pending'
            })

    return approvers

def get_approver_for_role(role, department):
    """Lookup approver by role and department"""

    # This would query your org chart / HRIS system
    APPROVER_DIRECTORY = {
        'Engineering': {
            'manager': {'name': 'Alice Johnson', 'email': 'alice@company.com'},
            'department_head': {'name': 'Bob Smith', 'email': 'bob@company.com'},
            'finance_director': {'name': 'Carol Lee', 'email': 'carol@company.com'},
            'cfo': {'name': 'David Chen', 'email': 'david@company.com'},
            'ceo': {'name': 'Eve Williams', 'email': 'eve@company.com'}
        },
        # ... other departments
    }

    return APPROVER_DIRECTORY.get(department, {}).get(role)
```

### 2.2 Approval Workflow Engine

**Sequential vs. Parallel Approval**:

```python
class ApprovalWorkflow:
    """Manages invoice approval workflow"""

    def __init__(self, workflow_type='sequential'):
        """
        workflow_type:
        - 'sequential': Each approver in order (slower but clearer chain)
        - 'parallel': All approvers at once (faster but simultaneous)
        - 'hierarchical': Manager first, then up the chain
        """
        self.workflow_type = workflow_type

    def send_for_approval(self, invoice_data, approvers):
        """Send invoice to approvers"""

        if self.workflow_type == 'sequential':
            return self._sequential_approval(invoice_data, approvers)
        elif self.workflow_type == 'parallel':
            return self._parallel_approval(invoice_data, approvers)
        elif self.workflow_type == 'hierarchical':
            return self._hierarchical_approval(invoice_data, approvers)

    def _sequential_approval(self, invoice_data, approvers):
        """Send to first approver, then next after approval"""

        # Send to first approver only
        first_approver = approvers[0]
        send_approval_email(invoice_data, first_approver)

        # Update status
        invoice_data['current_approver'] = first_approver
        invoice_data['pending_approvers'] = approvers[1:]

        return {
            'status': 'sent_for_approval',
            'current_step': f"Waiting for {first_approver['name']} ({first_approver['role']})",
            'remaining_approvers': len(approvers)
        }

    def _parallel_approval(self, invoice_data, approvers):
        """Send to all approvers simultaneously"""

        for approver in approvers:
            send_approval_email(invoice_data, approver)

        invoice_data['approvers_pending'] = approvers

        return {
            'status': 'sent_for_approval',
            'current_step': f"Waiting for {len(approvers)} approvers",
            'approvers': [a['name'] for a in approvers]
        }

    def _hierarchical_approval(self, invoice_data, approvers):
        """Send to lowest level first, escalate up chain"""

        # Sort approvers by hierarchy (manager → dept head → director → CFO → CEO)
        hierarchy_order = ['manager', 'department_head', 'finance_director', 'cfo', 'ceo']

        sorted_approvers = sorted(
            approvers,
            key=lambda a: hierarchy_order.index(a['role']) if a['role'] in hierarchy_order else 99
        )

        # Send to first in hierarchy
        first_approver = sorted_approvers[0]
        send_approval_email(invoice_data, first_approver)

        invoice_data['approval_chain'] = sorted_approvers
        invoice_data['current_approver_index'] = 0

        return {
            'status': 'sent_for_approval',
            'current_step': f"Waiting for {first_approver['name']} ({first_approver['role']})",
            'approval_chain': [a['name'] for a in sorted_approvers]
        }

def send_approval_email(invoice_data, approver):
    """Send approval request email"""

    subject = f"Invoice Approval Required: {invoice_data['vendor_name']} - ${invoice_data['total_amount']:,.2f}"

    body = f"""
    Hello {approver['name']},

    An invoice requires your approval:

    Vendor: {invoice_data['vendor_name']}
    Invoice #: {invoice_data['invoice_number']}
    Amount: ${invoice_data['total_amount']:,.2f}
    Invoice Date: {invoice_data['invoice_date']}
    Due Date: {invoice_data['due_date']}

    {f"PO #: {invoice_data['po_number']}" if invoice_data.get('po_number') else "No PO attached"}

    [View Invoice] [Approve] [Reject] [Request More Info]

    If you have questions, please contact Accounts Payable.

    ---
    This is an automated message from the AP system.
    """

    # Send email via your email system
    send_email(
        to=approver['email'],
        subject=subject,
        body=body,
        attachments=[invoice_data['invoice_file_path']]
    )
```

### 2.3 Delegation & Escalation

**Handling Approver Absence**:

```python
def handle_approver_absence(invoice_data, approver):
    """Handle case where approver is out of office"""

    # Check if approver has delegate
    delegate = get_approver_delegate(approver['email'])

    if delegate:
        # Send to delegate
        send_approval_email(invoice_data, delegate)

        # Log delegation
        log_approval_action(invoice_data, {
            'action': 'delegated',
            'from': approver['name'],
            'to': delegate['name'],
            'reason': 'Out of office'
        })

        return delegate

    else:
        # Escalate to next level or notify
        escalate_approval(invoice_data, approver)

def escalate_approval(invoice_data, stuck_approver):
    """Escalate stuck approval"""

    # If invoice is aging (e.g., >3 days pending approval)
    days_pending = (datetime.now() - invoice_data['approval_sent_date']).days

    if days_pending > 3:
        # Escalate to approver's manager
        escalation_manager = get_manager(stuck_approver['email'])

        send_escalation_email(
            invoice_data,
            stuck_approver,
            escalation_manager,
            days_pending
        )
```

---

## 3. Payment Scheduling

### 3.1 Payment Terms Interpretation

**Common Payment Terms**:

```python
PAYMENT_TERMS_CATALOG = {
    'Net 30': {
        'days': 30,
        'discount': None,
        'description': 'Payment due 30 days from invoice date'
    },
    'Net 60': {
        'days': 60,
        'discount': None,
        'description': 'Payment due 60 days from invoice date'
    },
    '2/10 Net 30': {
        'days': 30,
        'discount': {
            'percent': 2,
            'if_paid_by_day': 10
        },
        'description': '2% discount if paid within 10 days, otherwise due in 30 days'
    },
    '1/10 Net 30': {
        'days': 30,
        'discount': {
            'percent': 1,
            'if_paid_by_day': 10
        },
        'description': '1% discount if paid within 10 days'
    },
    'Due on Receipt': {
        'days': 0,
        'discount': None,
        'description': 'Payment due immediately upon receipt'
    },
    'Net 15': {
        'days': 15,
        'discount': None,
        'description': 'Payment due 15 days from invoice date'
    },
    'EOM': {  # End of Month
        'days': 'eom',
        'discount': None,
        'description': 'Payment due at end of month following invoice month'
    },
    'COD': {  # Cash on Delivery
        'days': 0,
        'discount': None,
        'description': 'Payment due on delivery'
    }
}

def calculate_due_date(invoice_date, payment_terms):
    """Calculate payment due date based on terms"""

    invoice_dt = parse_date(invoice_date)

    terms = PAYMENT_TERMS_CATALOG.get(payment_terms)

    if not terms:
        # Default to Net 30 if terms not recognized
        terms = PAYMENT_TERMS_CATALOG['Net 30']

    if terms['days'] == 'eom':
        # End of month following invoice
        # If invoice is Jan 15, due date is Feb 28/29
        next_month = invoice_dt.replace(day=1) + timedelta(days=32)
        last_day_of_next_month = next_month.replace(day=1) - timedelta(days=1)
        return last_day_of_next_month

    elif terms['days'] == 0:
        # Due immediately
        return invoice_dt

    else:
        # Standard net days
        return invoice_dt + timedelta(days=terms['days'])

def calculate_discount_date(invoice_date, payment_terms):
    """Calculate last date to get early payment discount"""

    invoice_dt = parse_date(invoice_date)

    terms = PAYMENT_TERMS_CATALOG.get(payment_terms)

    if terms and terms.get('discount'):
        discount_days = terms['discount']['if_paid_by_day']
        return invoice_dt + timedelta(days=discount_days)

    return None
```

### 3.2 Payment Scheduling Strategy

**Optimize for Cash Flow + Discounts**:

```python
def schedule_payment(invoice_data, cash_flow_policy='balanced'):
    """
    Schedule payment date based on:
    1. Due date (must pay before this)
    2. Discount opportunity (should pay before this to save money)
    3. Cash flow optimization (can we hold cash longer?)

    Policies:
    - 'aggressive_discounts': Always take discounts if available
    - 'balanced': Take discounts if ROI > threshold, otherwise optimize cash
    - 'conservative_cash': Hold cash as long as possible, skip discounts
    """

    due_date = invoice_data['due_date']
    discount_date = calculate_discount_date(
        invoice_data['invoice_date'],
        invoice_data.get('payment_terms', 'Net 30')
    )

    # Default: pay 1 day before due to ensure on-time delivery
    default_payment_date = parse_date(due_date) - timedelta(days=1)

    # Check if discount available
    if discount_date:
        discount_percent = PAYMENT_TERMS_CATALOG[invoice_data['payment_terms']]['discount']['percent']
        discount_amount = invoice_data['total_amount'] * (discount_percent / 100)

        # Calculate annualized ROI of taking discount
        days_early = (parse_date(due_date) - parse_date(discount_date)).days

        if days_early > 0:
            # Annualized return = (discount% / days early) * 365
            annualized_roi = (discount_percent / days_early) * 365

            # Decision based on policy
            if cash_flow_policy == 'aggressive_discounts':
                # Always take discount
                scheduled_payment_date = discount_date
                reason = f"Taking {discount_percent}% discount (${discount_amount:,.2f} savings)"

            elif cash_flow_policy == 'balanced':
                # Take discount if annualized ROI > 18% (configurable threshold)
                if annualized_roi > 18:
                    scheduled_payment_date = discount_date
                    reason = f"Taking {discount_percent}% discount ({annualized_roi:.1f}% annualized ROI)"
                else:
                    scheduled_payment_date = default_payment_date
                    reason = f"Skipping discount (only {annualized_roi:.1f}% ROI)"

            else:  # conservative_cash
                # Only take discount if extremely good (>36% ROI)
                if annualized_roi > 36:
                    scheduled_payment_date = discount_date
                    reason = f"Exceptional discount ({annualized_roi:.1f}% ROI)"
                else:
                    scheduled_payment_date = default_payment_date
                    reason = "Optimizing for cash flow"
        else:
            # Discount date is same as or after due date (unusual)
            scheduled_payment_date = default_payment_date
            reason = "Discount terms don't provide early payment benefit"

    else:
        # No discount available
        scheduled_payment_date = default_payment_date
        reason = "No early payment discount available"

    return {
        'scheduled_payment_date': scheduled_payment_date,
        'due_date': due_date,
        'discount_date': discount_date,
        'reason': reason
    }
```

### 3.3 Payment Batching

**Group Payments Efficiently**:

```python
def batch_payments(invoices_to_pay, batch_strategy='by_vendor'):
    """
    Batch payments for efficiency

    Strategies:
    - 'by_vendor': One payment per vendor (consolidate multiple invoices)
    - 'by_method': Group by payment method (ACH, check, wire)
    - 'by_due_date': Group by payment date
    - 'optimal': Combine strategies for minimum transaction count
    """

    if batch_strategy == 'by_vendor':
        # Group invoices by vendor
        vendor_batches = {}

        for invoice in invoices_to_pay:
            vendor_id = invoice['vendor_id']

            if vendor_id not in vendor_batches:
                vendor_batches[vendor_id] = []

            vendor_batches[vendor_id].append(invoice)

        # Create payment batch for each vendor
        payment_batches = []

        for vendor_id, invoices in vendor_batches.items():
            total_amount = sum(inv['total_amount'] for inv in invoices)

            payment_batches.append({
                'vendor_id': vendor_id,
                'vendor_name': invoices[0]['vendor_name'],
                'payment_method': invoices[0]['preferred_payment_method'],
                'total_amount': total_amount,
                'invoice_count': len(invoices),
                'invoices': invoices,
                'payment_date': max(inv['scheduled_payment_date'] for inv in invoices)
            })

        return payment_batches

    elif batch_strategy == 'by_method':
        # Group by payment method
        method_batches = {
            'ACH': [],
            'Check': [],
            'Wire': [],
            'Credit Card': []
        }

        for invoice in invoices_to_pay:
            method = invoice.get('preferred_payment_method', 'Check')
            method_batches[method].append(invoice)

        return method_batches
```

### 3.4 Payment File Generation

**ACH File Format (NACHA)**:

```python
def generate_ach_file(payment_batch, company_info):
    """Generate NACHA ACH file for bank submission"""

    # File Header Record (Type 1)
    file_header = {
        'record_type': '1',
        'priority_code': '01',
        'immediate_destination': company_info['bank_routing_number'],
        'immediate_origin': company_info['company_tax_id'],
        'file_creation_date': datetime.now().strftime('%y%m%d'),
        'file_creation_time': datetime.now().strftime('%H%M'),
        'file_id_modifier': 'A',
        'record_size': '094',
        'blocking_factor': '10',
        'format_code': '1',
        'immediate_destination_name': company_info['bank_name'],
        'immediate_origin_name': company_info['company_name']
    }

    # Batch Header Record (Type 5)
    batch_header = {
        'record_type': '5',
        'service_class_code': '200',  # Mixed debits and credits
        'company_name': company_info['company_name'],
        'company_discretionary_data': '',
        'company_id': company_info['company_tax_id'],
        'standard_entry_class': 'CCD',  # Corporate credit or debit
        'company_entry_description': 'AP PAYMENT',
        'company_descriptive_date': datetime.now().strftime('%b %d'),
        'effective_entry_date': payment_batch['payment_date'].strftime('%y%m%d'),
        'originator_status_code': '1'
    }

    # Entry Detail Records (Type 6) - one per payment
    entry_details = []

    for payment in payment_batch['payments']:
        entry = {
            'record_type': '6',
            'transaction_code': '22',  # Credit to checking account
            'receiving_dfi_id': payment['vendor_bank_routing'][:8],
            'check_digit': payment['vendor_bank_routing'][8],
            'dfi_account_number': payment['vendor_account_number'],
            'amount': int(payment['amount'] * 100),  # In cents
            'individual_id': payment['invoice_number'],
            'individual_name': payment['vendor_name'][:22],
            'discretionary_data': '',
            'addenda_record_indicator': '0',
            'trace_number': f"{company_info['bank_routing_number']}{len(entry_details):07d}"
        }

        entry_details.append(entry)

    # Batch Control Record (Type 8)
    batch_control = {
        'record_type': '8',
        'service_class_code': '200',
        'entry_count': len(entry_details),
        'entry_hash': sum(int(e['receiving_dfi_id']) for e in entry_details) % 10000000000,
        'total_debit': 0,
        'total_credit': sum(e['amount'] for e in entry_details),
        'company_id': company_info['company_tax_id']
    }

    # File Control Record (Type 9)
    file_control = {
        'record_type': '9',
        'batch_count': 1,
        'block_count': int((2 + len(entry_details) + 2) / 10) + 1,  # Round up to 10
        'entry_count': len(entry_details),
        'entry_hash': batch_control['entry_hash'],
        'total_debit': 0,
        'total_credit': batch_control['total_credit']
    }

    # Format as fixed-width NACHA file
    ach_file_content = format_nacha_file(
        file_header,
        batch_header,
        entry_details,
        batch_control,
        file_control
    )

    return ach_file_content
```

---

## 4. Vendor Database Management

### 4.1 Vendor Master Data Schema

**Comprehensive Vendor Record**:

```python
VENDOR_SCHEMA = {
    'vendor_id': 'VENDOR-00001',  # Unique identifier
    'vendor_name': 'Acme Corporation',
    'legal_name': 'Acme Corporation Inc.',
    'tax_id': '12-3456789',  # EIN

    # Contact Information
    'contact': {
        'primary_contact_name': 'John Smith',
        'primary_contact_title': 'Accounts Receivable Manager',
        'email': 'ar@acme.com',
        'phone': '555-123-4567',
        'fax': '555-123-4568'
    },

    # Address
    'address': {
        'street': '123 Main Street',
        'city': 'New York',
        'state': 'NY',
        'zip': '10001',
        'country': 'USA'
    },

    # Payment Information
    'payment': {
        'preferred_method': 'ACH',  # ACH, Check, Wire, Credit Card
        'payment_terms': 'Net 30',
        'bank_account': {
            'bank_name': 'First National Bank',
            'routing_number': '021000021',
            'account_number': '1234567890',
            'account_type': 'Checking'
        },
        'remittance_email': 'payments@acme.com'
    },

    # Tax & Compliance
    'tax_compliance': {
        'w9_on_file': True,
        'w9_date': '2024-01-15',
        '1099_eligible': True,
        'backup_withholding': False,
        'tax_classification': 'Corporation'
    },

    # Categorization
    'categories': ['Office Supplies', 'Technology'],
    'spend_category': 'Indirect',  # Direct, Indirect, Capital

    # Performance & History
    'metrics': {
        'total_spend_ytd': 125000.00,
        'total_spend_lifetime': 450000.00,
        'invoice_count_ytd': 45,
        'average_payment_days': 28.5,  # How fast we pay them
        'on_time_payment_rate': 0.96,  # 96% paid on time
        'dispute_count': 2,
        'quality_rating': 4.5  # Out of 5
    },

    # Status & Risk
    'status': 'Active',  # Active, Inactive, On Hold, Blocked
    'risk_level': 'Low',  # Low, Medium, High
    'insurance_required': False,
    'insurance_on_file': None,

    # Approval & Limits
    'auto_approve_limit': 5000,  # Auto-approve invoices under this amount
    'requires_po': True,  # Must have PO before payment

    # Metadata
    'created_date': '2020-05-12',
    'created_by': 'jdoe@company.com',
    'last_modified_date': '2024-11-15',
    'last_modified_by': 'asmith@company.com',
    'notes': 'Primary supplier for office furniture'
}
```

### 4.2 Vendor Onboarding Process

**New Vendor Setup Workflow**:

```python
def onboard_new_vendor(vendor_data):
    """Complete vendor onboarding process"""

    onboarding_steps = []

    # Step 1: Validate vendor information
    onboarding_steps.append("Validating vendor information...")

    validation_result = validate_vendor_data(vendor_data)

    if not validation_result['is_valid']:
        return {
            'status': 'validation_failed',
            'errors': validation_result['errors']
        }

    # Step 2: Check for duplicates
    onboarding_steps.append("Checking for duplicate vendors...")

    duplicates = find_duplicate_vendors(vendor_data)

    if duplicates:
        return {
            'status': 'duplicate_found',
            'message': f"Potential duplicate: {duplicates[0]['vendor_name']}",
            'duplicate_vendor_id': duplicates[0]['vendor_id']
        }

    # Step 3: Request W-9 form
    onboarding_steps.append("Requesting W-9 tax form...")

    send_w9_request(vendor_data['contact']['email'])

    # Step 4: Setup payment information
    onboarding_steps.append("Setting up payment information...")

    # Validate bank account if ACH
    if vendor_data['payment']['preferred_method'] == 'ACH':
        validate_bank_account(
            vendor_data['payment']['bank_account']['routing_number'],
            vendor_data['payment']['bank_account']['account_number']
        )

    # Step 5: Assign vendor ID
    vendor_id = generate_vendor_id()
    vendor_data['vendor_id'] = vendor_id

    # Step 6: Set default settings
    vendor_data['status'] = 'Pending'  # Activate after W-9 received
    vendor_data['risk_level'] = 'Medium'  # Default until reviewed
    vendor_data['created_date'] = datetime.now().isoformat()

    # Step 7: Save to vendor database
    save_vendor_record(vendor_data)

    onboarding_steps.append(f"Vendor created with ID: {vendor_id}")

    # Step 8: Notify stakeholders
    notify_ap_team_new_vendor(vendor_data)

    return {
        'status': 'success',
        'vendor_id': vendor_id,
        'onboarding_steps': onboarding_steps,
        'next_steps': [
            'Await W-9 form from vendor',
            'Review and approve vendor setup',
            'Activate vendor once compliance complete'
        ]
    }

def validate_vendor_data(vendor_data):
    """Validate required vendor fields"""

    errors = []

    required_fields = [
        'vendor_name',
        'tax_id',
        'contact.email',
        'address.street',
        'payment.preferred_method',
        'payment.payment_terms'
    ]

    for field in required_fields:
        if '.' in field:
            # Nested field
            parts = field.split('.')
            value = vendor_data
            for part in parts:
                value = value.get(part, None)
                if value is None:
                    break

            if value is None:
                errors.append(f"Missing required field: {field}")
        else:
            if not vendor_data.get(field):
                errors.append(f"Missing required field: {field}")

    # Validate tax ID format (EIN: XX-XXXXXXX)
    if vendor_data.get('tax_id'):
        if not re.match(r'^\d{2}-\d{7}$', vendor_data['tax_id']):
            errors.append("Tax ID must be in format: XX-XXXXXXX")

    # Validate email
    if vendor_data.get('contact', {}).get('email'):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', vendor_data['contact']['email']):
            errors.append("Invalid email format")

    return {
        'is_valid': len(errors) == 0,
        'errors': errors
    }

def find_duplicate_vendors(vendor_data):
    """Find potential duplicate vendors"""

    # Search by:
    # 1. Exact name match
    # 2. Tax ID match
    # 3. Bank account match
    # 4. Fuzzy name matching

    duplicates = []

    # Check exact name
    existing_vendor = query_vendor_by_name(vendor_data['vendor_name'])
    if existing_vendor:
        duplicates.append(existing_vendor)

    # Check tax ID
    if vendor_data.get('tax_id'):
        existing_vendor = query_vendor_by_tax_id(vendor_data['tax_id'])
        if existing_vendor:
            duplicates.append(existing_vendor)

    # Fuzzy name matching
    similar_vendors = fuzzy_search_vendors(vendor_data['vendor_name'], threshold=0.85)
    duplicates.extend(similar_vendors)

    # Remove duplicates from duplicates list
    unique_duplicates = {v['vendor_id']: v for v in duplicates}.values()

    return list(unique_duplicates)
```

### 4.3 Vendor Performance Tracking

**Key Performance Indicators**:

```python
def calculate_vendor_metrics(vendor_id, period='ytd'):
    """Calculate vendor performance metrics"""

    # Get all invoices for this vendor in period
    invoices = get_vendor_invoices(vendor_id, period)

    if not invoices:
        return None

    # Calculate metrics
    total_spend = sum(inv['total_amount'] for inv in invoices)
    invoice_count = len(invoices)
    average_invoice_amount = total_spend / invoice_count

    # Payment performance (how fast we pay them)
    payment_days = []
    on_time_count = 0

    for invoice in invoices:
        if invoice.get('payment_date'):
            invoice_dt = parse_date(invoice['invoice_date'])
            payment_dt = parse_date(invoice['payment_date'])
            days_to_pay = (payment_dt - invoice_dt).days
            payment_days.append(days_to_pay)

            # Check if paid on time (before or on due date)
            due_dt = parse_date(invoice['due_date'])
            if payment_dt <= due_dt:
                on_time_count += 1

    average_payment_days = sum(payment_days) / len(payment_days) if payment_days else 0
    on_time_rate = on_time_count / len(invoices) if invoices else 0

    # Dispute tracking
    disputes = get_vendor_disputes(vendor_id, period)
    dispute_count = len(disputes)
    dispute_rate = dispute_count / invoice_count if invoice_count > 0 else 0

    return {
        'vendor_id': vendor_id,
        'period': period,
        'total_spend': total_spend,
        'invoice_count': invoice_count,
        'average_invoice_amount': average_invoice_amount,
        'average_payment_days': average_payment_days,
        'on_time_payment_rate': on_time_rate,
        'dispute_count': dispute_count,
        'dispute_rate': dispute_rate,
        'quality_score': calculate_vendor_quality_score(vendor_id)
    }

def calculate_vendor_quality_score(vendor_id):
    """Calculate overall vendor quality (0-5)"""

    metrics = calculate_vendor_metrics(vendor_id)

    score = 5.0  # Start at perfect

    # Deduct for disputes
    if metrics['dispute_rate'] > 0.05:  # >5% disputes
        score -= 1.0
    elif metrics['dispute_rate'] > 0.02:  # >2% disputes
        score -= 0.5

    # Deduct for late deliveries or quality issues
    # (Would need separate quality tracking system)

    # Cap at 5.0
    return min(score, 5.0)
```

---

## 5. Reconciliation & Matching

### 5.1 Three-Way Match (PO → Receipt → Invoice)

**Standard Three-Way Match**:

```
Purchase Order (PO)
    ↓ Goods/Services Delivered
Receipt/Goods Received Note (GRN)
    ↓ Vendor Sends Invoice
Invoice
    ↓ Verify all three match
APPROVE FOR PAYMENT
```

**Implementation**:

```python
def three_way_match(invoice_data):
    """Perform three-way match: PO → Receipt → Invoice"""

    match_result = {
        'status': 'pending',
        'po_match': None,
        'receipt_match': None,
        'discrepancies': [],
        'approval_recommendation': None
    }

    # Step 1: Find Purchase Order
    po = find_matching_po(invoice_data)

    if not po:
        match_result['status'] = 'no_po_found'
        match_result['discrepancies'].append('No purchase order found for this invoice')
        match_result['approval_recommendation'] = 'manual_review'
        return match_result

    match_result['po_match'] = po

    # Step 2: Find Receipt/GRN
    receipt = find_matching_receipt(po['po_number'])

    if not receipt:
        match_result['status'] = 'no_receipt_found'
        match_result['discrepancies'].append('No goods receipt found for this PO')
        match_result['approval_recommendation'] = 'manual_review'
        return match_result

    match_result['receipt_match'] = receipt

    # Step 3: Compare PO → Invoice
    po_invoice_discrepancies = compare_po_to_invoice(po, invoice_data)
    match_result['discrepancies'].extend(po_invoice_discrepancies)

    # Step 4: Compare Receipt → Invoice
    receipt_invoice_discrepancies = compare_receipt_to_invoice(receipt, invoice_data)
    match_result['discrepancies'].extend(receipt_invoice_discrepancies)

    # Step 5: Determine match status
    if len(match_result['discrepancies']) == 0:
        match_result['status'] = 'matched'
        match_result['approval_recommendation'] = 'auto_approve'

    elif all(d['severity'] == 'minor' for d in match_result['discrepancies']):
        match_result['status'] = 'minor_discrepancies'
        match_result['approval_recommendation'] = 'manager_approval'

    else:
        match_result['status'] = 'major_discrepancies'
        match_result['approval_recommendation'] = 'reject_or_manual_review'

    return match_result

def compare_po_to_invoice(po, invoice):
    """Compare PO to Invoice for discrepancies"""

    discrepancies = []

    # Check vendor
    if po['vendor_id'] != invoice.get('vendor_id'):
        discrepancies.append({
            'field': 'vendor',
            'severity': 'major',
            'message': f"Vendor mismatch: PO has {po['vendor_name']}, Invoice has {invoice['vendor_name']}"
        })

    # Check amount (allow small tolerance)
    po_amount = po['total_amount']
    invoice_amount = invoice['total_amount']

    tolerance = max(po_amount * 0.05, 10)  # 5% or $10, whichever is larger

    if abs(po_amount - invoice_amount) > tolerance:
        discrepancies.append({
            'field': 'amount',
            'severity': 'major',
            'message': f"Amount mismatch: PO ${po_amount:.2f}, Invoice ${invoice_amount:.2f} (variance: ${abs(po_amount - invoice_amount):.2f})"
        })
    elif abs(po_amount - invoice_amount) > 0.01:
        discrepancies.append({
            'field': 'amount',
            'severity': 'minor',
            'message': f"Small amount difference: PO ${po_amount:.2f}, Invoice ${invoice_amount:.2f}"
        })

    # Check line items
    if invoice.get('line_items') and po.get('line_items'):
        for inv_item in invoice['line_items']:
            # Find matching PO line item
            matching_po_item = next(
                (item for item in po['line_items']
                 if item['description'].lower() == inv_item['description'].lower()),
                None
            )

            if matching_po_item:
                # Compare quantity
                if inv_item['quantity'] > matching_po_item['quantity']:
                    discrepancies.append({
                        'field': 'quantity',
                        'severity': 'major',
                        'message': f"Quantity exceeds PO: {inv_item['description']} - PO: {matching_po_item['quantity']}, Invoice: {inv_item['quantity']}"
                    })

                # Compare unit price (allow small tolerance)
                price_variance = abs(inv_item['unit_price'] - matching_po_item['unit_price'])
                if price_variance > matching_po_item['unit_price'] * 0.02:  # 2% tolerance
                    discrepancies.append({
                        'field': 'unit_price',
                        'severity': 'minor',
                        'message': f"Unit price variance: {inv_item['description']} - PO: ${matching_po_item['unit_price']:.2f}, Invoice: ${inv_item['unit_price']:.2f}"
                    })
            else:
                discrepancies.append({
                    'field': 'line_item',
                    'severity': 'major',
                    'message': f"Invoice line item not found in PO: {inv_item['description']}"
                })

    return discrepancies

def compare_receipt_to_invoice(receipt, invoice):
    """Compare Receipt/GRN to Invoice"""

    discrepancies = []

    # Check quantity received vs. quantity invoiced
    if invoice.get('line_items') and receipt.get('line_items'):
        for inv_item in invoice['line_items']:
            # Find matching receipt line item
            matching_receipt_item = next(
                (item for item in receipt['line_items']
                 if item['description'].lower() == inv_item['description'].lower()),
                None
            )

            if matching_receipt_item:
                if inv_item['quantity'] > matching_receipt_item['quantity_received']:
                    discrepancies.append({
                        'field': 'quantity',
                        'severity': 'major',
                        'message': f"Invoiced quantity exceeds received: {inv_item['description']} - Received: {matching_receipt_item['quantity_received']}, Invoiced: {inv_item['quantity']}"
                    })
            else:
                discrepancies.append({
                    'field': 'line_item',
                    'severity': 'major',
                    'message': f"Invoice line item not found in receipt: {inv_item['description']}"
                })

    return discrepancies
```

### 5.2 Payment Reconciliation

**Match Payments to Bank Statements**:

```python
def reconcile_payments_to_bank(payment_records, bank_statement):
    """Reconcile AP payments to bank statement"""

    reconciliation_result = {
        'matched': [],
        'unmatched_payments': [],
        'unmatched_bank_transactions': [],
        'discrepancies': []
    }

    # Create copy of bank transactions to track matches
    unmatched_bank = bank_statement['transactions'].copy()

    # Try to match each payment
    for payment in payment_records:
        # Look for matching bank transaction
        matching_bank_tx = find_matching_bank_transaction(payment, unmatched_bank)

        if matching_bank_tx:
            # Verify amount matches
            if abs(payment['amount'] - matching_bank_tx['amount']) < 0.01:
                reconciliation_result['matched'].append({
                    'payment': payment,
                    'bank_transaction': matching_bank_tx,
                    'status': 'matched'
                })

                # Remove from unmatched list
                unmatched_bank.remove(matching_bank_tx)
            else:
                # Amount mismatch
                reconciliation_result['discrepancies'].append({
                    'payment': payment,
                    'bank_transaction': matching_bank_tx,
                    'issue': 'amount_mismatch',
                    'payment_amount': payment['amount'],
                    'bank_amount': matching_bank_tx['amount'],
                    'variance': abs(payment['amount'] - matching_bank_tx['amount'])
                })
        else:
            # No matching bank transaction found
            reconciliation_result['unmatched_payments'].append(payment)

    # Remaining unmatched bank transactions
    reconciliation_result['unmatched_bank_transactions'] = unmatched_bank

    return reconciliation_result

def find_matching_bank_transaction(payment, bank_transactions):
    """Find bank transaction matching a payment"""

    # Match criteria:
    # 1. Amount matches exactly (or within $0.01)
    # 2. Date is within +/- 3 business days
    # 3. Payee name matches (fuzzy)

    payment_amount = payment['amount']
    payment_date = parse_date(payment['payment_date'])
    payment_payee = payment['vendor_name'].lower()

    for bank_tx in bank_transactions:
        bank_amount = abs(bank_tx['amount'])  # Use absolute (debits are negative)
        bank_date = parse_date(bank_tx['date'])
        bank_description = bank_tx['description'].lower()

        # Check amount match (within $0.01)
        if abs(payment_amount - bank_amount) > 0.01:
            continue

        # Check date proximity (within 3 business days)
        date_diff = abs((payment_date - bank_date).days)
        if date_diff > 5:  # Allow up to 5 calendar days
            continue

        # Check payee/description match (fuzzy)
        if payment_payee in bank_description or \
           any(word in bank_description for word in payment_payee.split() if len(word) > 3):
            return bank_tx

    return None
```

---

## 6. Exception Handling

### 6.1 Common AP Exceptions

**Exception Types & Handling**:

```python
AP_EXCEPTIONS = {
    'duplicate_invoice': {
        'description': 'Invoice number already processed',
        'severity': 'high',
        'action': 'reject',
        'resolution_steps': [
            'Verify if invoice is truly duplicate',
            'Check if vendor re-sent same invoice',
            'Contact vendor to clarify'
        ]
    },

    'no_po': {
        'description': 'Invoice received without purchase order',
        'severity': 'medium',
        'action': 'manual_review',
        'resolution_steps': [
            'Check if PO required for this vendor',
            'Verify if goods/services were received',
            'Obtain retroactive PO approval if needed',
            'Update vendor requirements to prevent recurrence'
        ]
    },

    'po_mismatch': {
        'description': 'Invoice does not match PO (amount, quantity, price)',
        'severity': 'medium',
        'action': 'manual_review',
        'resolution_steps': [
            'Identify specific discrepancy',
            'Contact vendor for explanation',
            'Check if change order was issued',
            'Verify goods receipt quantity',
            'Request corrected invoice if needed'
        ]
    },

    'missing_receipt': {
        'description': 'No goods receipt for this PO',
        'severity': 'high',
        'action': 'hold',
        'resolution_steps': [
            'Verify delivery status with receiving department',
            'Contact vendor for proof of delivery',
            'Create goods receipt if items were received',
            'Investigate if items were never delivered'
        ]
    },

    'amount_over_po': {
        'description': 'Invoice amount exceeds PO amount',
        'severity': 'high',
        'action': 'manual_review',
        'resolution_steps': [
            'Calculate variance percentage',
            'Check for approved change orders',
            'Verify if additional items/services were authorized',
            'Request manager approval if variance acceptable',
            'Request corrected invoice if overcharge'
        ]
    },

    'expired_payment_terms': {
        'description': 'Invoice received after payment terms expired',
        'severity': 'low',
        'action': 'process_with_warning',
        'resolution_steps': [
            'Calculate late fee if applicable',
            'Notify vendor of late submission',
            'Process payment per terms (may be past due)'
        ]
    },

    'sales_tax_issue': {
        'description': 'Sales tax calculation incorrect or missing',
        'severity': 'medium',
        'action': 'manual_review',
        'resolution_steps': [
            'Verify tax rate for jurisdiction',
            'Calculate correct tax amount',
            'Request corrected invoice from vendor',
            'Update vendor tax settings in system'
        ]
    },

    'vendor_not_in_system': {
        'description': 'Vendor not found in vendor database',
        'severity': 'medium',
        'action': 'hold',
        'resolution_steps': [
            'Verify vendor is legitimate',
            'Initiate vendor onboarding process',
            'Request W-9 form',
            'Setup vendor record before payment'
        ]
    },

    'missing_required_docs': {
        'description': 'Required documentation not attached (contract, W-9, insurance)',
        'severity': 'high',
        'action': 'hold',
        'resolution_steps': [
            'Identify missing documents',
            'Request from vendor',
            'Verify document validity',
            'Update vendor file'
        ]
    }
}

def handle_invoice_exception(exception_type, invoice_data):
    """Handle specific invoice exception"""

    exception = AP_EXCEPTIONS.get(exception_type)

    if not exception:
        raise ValueError(f"Unknown exception type: {exception_type}")

    # Log exception
    log_exception(invoice_data, exception_type, exception)

    # Take action based on exception
    if exception['action'] == 'reject':
        reject_invoice(invoice_data, exception['description'])

    elif exception['action'] == 'hold':
        put_invoice_on_hold(invoice_data, exception['description'])

    elif exception['action'] == 'manual_review':
        route_to_manual_review(invoice_data, exception_type)

    elif exception['action'] == 'process_with_warning':
        flag_invoice_with_warning(invoice_data, exception['description'])

    # Notify stakeholders
    notify_exception_to_team(invoice_data, exception_type, exception)

    return {
        'exception_type': exception_type,
        'severity': exception['severity'],
        'action_taken': exception['action'],
        'resolution_steps': exception['resolution_steps']
    }
```

### 6.2 Fraud Detection

**Red Flags to Watch For**:

```python
def detect_potential_fraud(invoice_data, vendor_data):
    """Detect potential invoice fraud"""

    fraud_indicators = []
    risk_score = 0  # 0-100

    # Indicator 1: New vendor with large invoice
    if vendor_data.get('invoice_count_ytd', 0) < 3:
        if invoice_data['total_amount'] > 10000:
            fraud_indicators.append({
                'indicator': 'new_vendor_large_amount',
                'severity': 'medium',
                'details': f"New vendor (only {vendor_data.get('invoice_count_ytd', 0)} invoices) with large amount: ${invoice_data['total_amount']:,.2f}"
            })
            risk_score += 20

    # Indicator 2: Vendor bank account changed recently
    if vendor_data.get('bank_account_change_date'):
        days_since_change = (datetime.now() - parse_date(vendor_data['bank_account_change_date'])).days
        if days_since_change < 30:
            fraud_indicators.append({
                'indicator': 'recent_bank_change',
                'severity': 'high',
                'details': f"Bank account changed {days_since_change} days ago"
            })
            risk_score += 30

    # Indicator 3: Invoice number out of sequence
    last_invoice = get_last_invoice_for_vendor(vendor_data['vendor_id'])
    if last_invoice:
        if invoice_data.get('invoice_number'):
            # Check if sequential
            if not is_invoice_number_sequential(last_invoice['invoice_number'], invoice_data['invoice_number']):
                fraud_indicators.append({
                    'indicator': 'invoice_sequence_gap',
                    'severity': 'low',
                    'details': f"Invoice number not sequential (last: {last_invoice['invoice_number']}, current: {invoice_data['invoice_number']})"
                })
                risk_score += 10

    # Indicator 4: Duplicate vendor name (with slight variation)
    similar_vendors = fuzzy_search_vendors(vendor_data['vendor_name'], threshold=0.9)
    if len(similar_vendors) > 1:
        fraud_indicators.append({
            'indicator': 'similar_vendor_names',
            'severity': 'high',
            'details': f"Multiple similar vendor names found: {[v['vendor_name'] for v in similar_vendors]}"
        })
        risk_score += 35

    # Indicator 5: Round number amounts (common in fraud)
    if invoice_data['total_amount'] % 100 == 0 and invoice_data['total_amount'] > 1000:
        fraud_indicators.append({
            'indicator': 'round_number_amount',
            'severity': 'low',
            'details': f"Round number amount: ${invoice_data['total_amount']:,.2f}"
        })
        risk_score += 5

    # Indicator 6: Invoice just under approval threshold
    approval_threshold = get_approval_threshold(invoice_data.get('department'))
    if approval_threshold:
        if invoice_data['total_amount'] >= approval_threshold * 0.95 and \
           invoice_data['total_amount'] < approval_threshold:
            fraud_indicators.append({
                'indicator': 'just_under_threshold',
                'severity': 'medium',
                'details': f"Amount (${invoice_data['total_amount']:,.2f}) just under approval threshold (${approval_threshold:,.2f})"
            })
            risk_score += 15

    # Indicator 7: Weekend or holiday invoice date
    invoice_date = parse_date(invoice_data['invoice_date'])
    if invoice_date.weekday() >= 5:  # Saturday or Sunday
        fraud_indicators.append({
            'indicator': 'weekend_invoice',
            'severity': 'low',
            'details': f"Invoice dated on weekend: {invoice_date.strftime('%A, %B %d, %Y')}"
        })
        risk_score += 5

    # Determine fraud risk level
    if risk_score >= 60:
        fraud_risk_level = 'high'
        recommended_action = 'Hold invoice and investigate'
    elif risk_score >= 30:
        fraud_risk_level = 'medium'
        recommended_action = 'Review with senior AP staff'
    else:
        fraud_risk_level = 'low'
        recommended_action = 'Process normally with documentation'

    return {
        'fraud_risk_score': risk_score,
        'fraud_risk_level': fraud_risk_level,
        'indicators': fraud_indicators,
        'recommended_action': recommended_action
    }
```

---

## 7. Compliance & Controls

### 7.1 Segregation of Duties (SOD)

**Key Principle**: No single person should control all aspects of a financial transaction.

**SOD Matrix for AP**:

```
Role Separation:
├── Invoice Receipt & Entry → AP Clerk A
├── Invoice Approval → Manager (different person)
├── Payment Processing → AP Clerk B (different from entry)
└── Bank Reconciliation → Accountant (different from all above)
```

**Implementation**:

```python
SOD_RULES = {
    'invoice_entry_and_approval': {
        'description': 'Person who enters invoice cannot approve it',
        'severity': 'critical',
        'check': lambda inv: inv['entered_by'] != inv['approved_by']
    },

    'invoice_approval_and_payment': {
        'description': 'Person who approves invoice cannot process payment',
        'severity': 'critical',
        'check': lambda inv: inv['approved_by'] != inv['payment_processed_by']
    },

    'payment_and_reconciliation': {
        'description': 'Person who processes payment cannot reconcile bank statement',
        'severity': 'critical',
        'check': lambda inv: inv['payment_processed_by'] != inv['reconciled_by']
    },

    'vendor_setup_and_payment': {
        'description': 'Person who sets up vendor cannot process payments to that vendor',
        'severity': 'high',
        'check': lambda inv, vendor: vendor['created_by'] != inv['payment_processed_by']
    }
}

def check_sod_compliance(invoice_data, action, user):
    """Check if action violates segregation of duties"""

    violations = []

    # Example: User trying to approve invoice they entered
    if action == 'approve':
        if invoice_data.get('entered_by') == user:
            violations.append({
                'rule': 'invoice_entry_and_approval',
                'severity': 'critical',
                'message': 'You cannot approve an invoice you entered'
            })

    # Example: User trying to process payment for invoice they approved
    if action == 'process_payment':
        if invoice_data.get('approved_by') == user:
            violations.append({
                'rule': 'invoice_approval_and_payment',
                'severity': 'critical',
                'message': 'You cannot process payment for an invoice you approved'
            })

    if violations:
        return {
            'allowed': False,
            'violations': violations
        }
    else:
        return {
            'allowed': True
        }
```

### 7.2 Audit Trail Requirements

**Comprehensive Audit Logging**:

```python
def log_audit_event(event_type, entity_type, entity_id, user, details):
    """Log all AP actions for audit trail"""

    audit_log_entry = {
        'timestamp': datetime.now().isoformat(),
        'event_type': event_type,  # created, updated, approved, rejected, paid, etc.
        'entity_type': entity_type,  # invoice, payment, vendor, etc.
        'entity_id': entity_id,
        'user_id': user['user_id'],
        'user_name': user['name'],
        'user_email': user['email'],
        'ip_address': user.get('ip_address'),
        'details': details,  # What specifically changed
        'session_id': user.get('session_id')
    }

    # Save to immutable audit log
    save_to_audit_log(audit_log_entry)

    return audit_log_entry

# Example audit events:

# Invoice created
log_audit_event(
    event_type='invoice_created',
    entity_type='invoice',
    entity_id='INV-12345',
    user=current_user,
    details={
        'vendor_id': 'VENDOR-001',
        'amount': 5000.00,
        'invoice_number': 'VENDOR-INV-999'
    }
)

# Invoice approved
log_audit_event(
    event_type='invoice_approved',
    entity_type='invoice',
    entity_id='INV-12345',
    user=current_user,
    details={
        'approval_level': 'manager',
        'comments': 'Approved - matches PO'
    }
)

# Payment processed
log_audit_event(
    event_type='payment_processed',
    entity_type='payment',
    entity_id='PAY-67890',
    user=current_user,
    details={
        'invoice_id': 'INV-12345',
        'amount': 5000.00,
        'payment_method': 'ACH',
        'payment_date': '2025-01-20'
    }
)

# Vendor bank account changed
log_audit_event(
    event_type='vendor_updated',
    entity_type='vendor',
    entity_id='VENDOR-001',
    user=current_user,
    details={
        'field_changed': 'bank_account',
        'old_value': '****1234',
        'new_value': '****5678',
        'reason': 'Vendor changed banks'
    }
)
```

### 7.3 1099 Reporting Compliance

**Track 1099-Eligible Payments**:

```python
def track_1099_payments(vendor_id, year=None):
    """Track payments to 1099-eligible vendors"""

    if year is None:
        year = datetime.now().year

    # Get vendor info
    vendor = get_vendor(vendor_id)

    if not vendor['tax_compliance']['1099_eligible']:
        return {
            'vendor_id': vendor_id,
            'vendor_name': vendor['vendor_name'],
            '1099_eligible': False,
            'reason': 'Vendor is corporation or otherwise not eligible'
        }

    # Get all payments in calendar year
    payments = get_vendor_payments(vendor_id, start_date=f"{year}-01-01", end_date=f"{year}-12-31")

    total_payments = sum(p['amount'] for p in payments)

    # Check if meets reporting threshold ($600 for most 1099 types)
    reporting_threshold = 600

    return {
        'vendor_id': vendor_id,
        'vendor_name': vendor['vendor_name'],
        'tax_id': vendor['tax_id'],
        '1099_eligible': True,
        'year': year,
        'total_payments': total_payments,
        'payment_count': len(payments),
        'reporting_required': total_payments >= reporting_threshold,
        'payments': payments
    }

def generate_1099_report(year):
    """Generate 1099 report for all eligible vendors"""

    # Get all 1099-eligible vendors
    eligible_vendors = get_1099_eligible_vendors()

    report_data = []

    for vendor in eligible_vendors:
        vendor_1099_data = track_1099_payments(vendor['vendor_id'], year)

        if vendor_1099_data['reporting_required']:
            report_data.append(vendor_1099_data)

    return {
        'year': year,
        'vendor_count': len(report_data),
        'total_reportable_amount': sum(v['total_payments'] for v in report_data),
        'vendors': report_data
    }
```

---

## 8. Metrics & Reporting

### 8.1 Key Performance Indicators (KPIs)

**AP Department KPIs**:

```python
def calculate_ap_kpis(period='month'):
    """Calculate AP department performance metrics"""

    # Get all invoices for period
    invoices = get_invoices_for_period(period)
    payments = get_payments_for_period(period)

    # KPI 1: Invoice Processing Time
    # Average days from invoice receipt to approval
    processing_times = []
    for inv in invoices:
        if inv.get('approved_date'):
            receipt_dt = parse_date(inv['receipt_date'])
            approval_dt = parse_date(inv['approved_date'])
            processing_times.append((approval_dt - receipt_dt).days)

    avg_processing_time = sum(processing_times) / len(processing_times) if processing_times else 0

    # KPI 2: Invoice Processing Cost
    # Cost per invoice processed (AP dept cost / invoice volume)
    ap_dept_monthly_cost = 15000  # Example: salaries + overhead
    cost_per_invoice = ap_dept_monthly_cost / len(invoices) if invoices else 0

    # KPI 3: Straight-Through Processing (STP) Rate
    # % of invoices processed without manual intervention
    auto_processed = sum(1 for inv in invoices if inv.get('auto_processed', False))
    stp_rate = auto_processed / len(invoices) if invoices else 0

    # KPI 4: Payment Accuracy
    # % of payments made without errors
    payment_errors = get_payment_errors(period)
    payment_accuracy = 1 - (len(payment_errors) / len(payments)) if payments else 0

    # KPI 5: Early Payment Discount Capture Rate
    # % of available discounts actually taken
    discount_opportunities = [inv for inv in invoices if has_early_payment_discount(inv)]
    discounts_taken = [inv for inv in discount_opportunities if inv.get('discount_taken', False)]
    discount_capture_rate = len(discounts_taken) / len(discount_opportunities) if discount_opportunities else 0

    # KPI 6: Days Payable Outstanding (DPO)
    # Average days to pay invoices
    payment_days = []
    for inv in invoices:
        if inv.get('payment_date'):
            invoice_dt = parse_date(inv['invoice_date'])
            payment_dt = parse_date(inv['payment_date'])
            payment_days.append((payment_dt - invoice_dt).days)

    dpo = sum(payment_days) / len(payment_days) if payment_days else 0

    # KPI 7: Exception Rate
    # % of invoices requiring manual review/exception handling
    exceptions = [inv for inv in invoices if inv.get('exception_count', 0) > 0]
    exception_rate = len(exceptions) / len(invoices) if invoices else 0

    # KPI 8: Vendor Satisfaction Score
    # Survey or performance rating
    vendor_satisfaction = calculate_vendor_satisfaction_score(period)

    return {
        'period': period,
        'invoice_volume': len(invoices),
        'payment_volume': len(payments),
        'avg_processing_time_days': round(avg_processing_time, 1),
        'cost_per_invoice': round(cost_per_invoice, 2),
        'stp_rate': round(stp_rate * 100, 1),  # as percentage
        'payment_accuracy': round(payment_accuracy * 100, 1),
        'discount_capture_rate': round(discount_capture_rate * 100, 1),
        'days_payable_outstanding': round(dpo, 1),
        'exception_rate': round(exception_rate * 100, 1),
        'vendor_satisfaction_score': vendor_satisfaction
    }

# Benchmark targets (industry averages):
AP_KPI_BENCHMARKS = {
    'avg_processing_time_days': {
        'excellent': 3,
        'good': 5,
        'average': 7,
        'poor': 10
    },
    'cost_per_invoice': {
        'excellent': 3,
        'good': 5,
        'average': 8,
        'poor': 12
    },
    'stp_rate': {
        'excellent': 80,  # 80%+
        'good': 60,
        'average': 40,
        'poor': 20
    },
    'payment_accuracy': {
        'excellent': 99,  # 99%+
        'good': 97,
        'average': 95,
        'poor': 90
    },
    'discount_capture_rate': {
        'excellent': 95,
        'good': 85,
        'average': 70,
        'poor': 50
    },
    'exception_rate': {
        'excellent': 10,  # Lower is better
        'good': 20,
        'average': 30,
        'poor': 40
    }
}
```

### 8.2 Executive Dashboard

**Monthly AP Summary Report**:

```python
def generate_executive_ap_report(month, year):
    """Generate executive-level AP summary"""

    period = f"{year}-{month:02d}"

    # Get KPIs
    kpis = calculate_ap_kpis(period)

    # Get cash flow data
    cash_position = get_cash_position()

    # Get vendor data
    top_vendors = get_top_vendors_by_spend(period, limit=10)

    # Get aging report
    aging_summary = get_ap_aging_summary()

    report = f"""
    # Accounts Payable Executive Summary
    **Period**: {period}
    **Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

    ---

    ## Key Metrics

    | Metric | This Month | Target | Status |
    |--------|-----------|--------|--------|
    | Invoice Volume | {kpis['invoice_volume']:,} | - | ℹ️ |
    | Avg Processing Time | {kpis['avg_processing_time_days']} days | ≤5 days | {'✅' if kpis['avg_processing_time_days'] <= 5 else '⚠️'} |
    | Cost per Invoice | ${kpis['cost_per_invoice']:.2f} | ≤$5 | {'✅' if kpis['cost_per_invoice'] <= 5 else '⚠️'} |
    | STP Rate | {kpis['stp_rate']:.1f}% | ≥60% | {'✅' if kpis['stp_rate'] >= 60 else '⚠️'} |
    | Payment Accuracy | {kpis['payment_accuracy']:.1f}% | ≥99% | {'✅' if kpis['payment_accuracy'] >= 99 else '⚠️'} |
    | Discount Capture | {kpis['discount_capture_rate']:.1f}% | ≥85% | {'✅' if kpis['discount_capture_rate'] >= 85 else '⚠️'} |
    | Days Payable Outstanding | {kpis['days_payable_outstanding']:.1f} days | - | ℹ️ |
    | Exception Rate | {kpis['exception_rate']:.1f}% | ≤20% | {'✅' if kpis['exception_rate'] <= 20 else '⚠️'} |

    ---

    ## Financial Summary

    **Total Payables**:
    - Current: ${aging_summary['current']:,.2f}
    - 1-30 Days Past Due: ${aging_summary['1_30_days']:,.2f}
    - 31-60 Days Past Due: ${aging_summary['31_60_days']:,.2f}
    - 61-90 Days Past Due: ${aging_summary['61_90_days']:,.2f}
    - 90+ Days Past Due: ${aging_summary['90_plus_days']:,.2f}
    - **Total Outstanding**: ${aging_summary['total']:,.2f}

    **Cash Position**:
    - Available Cash: ${cash_position['available_cash']:,.2f}
    - Upcoming Payments (7 days): ${cash_position['upcoming_7_days']:,.2f}
    - Upcoming Payments (30 days): ${cash_position['upcoming_30_days']:,.2f}

    ---

    ## Top 10 Vendors by Spend

    | Vendor | Spend | Invoice Count | Avg Payment Days |
    |--------|-------|---------------|------------------|
    """

    for vendor in top_vendors:
        report += f"| {vendor['vendor_name']} | ${vendor['total_spend']:,.2f} | {vendor['invoice_count']} | {vendor['avg_payment_days']:.1f} |\n"

    report += """
    ---

    ## Action Items

    """

    # Add action items based on metrics
    if kpis['avg_processing_time_days'] > 5:
        report += "- ⚠️ **Reduce invoice processing time**: Currently {:.1f} days (target: ≤5 days)\n".format(kpis['avg_processing_time_days'])

    if kpis['discount_capture_rate'] < 85:
        report += "- ⚠️ **Improve discount capture rate**: Currently {:.1f}% (target: ≥85%)\n".format(kpis['discount_capture_rate'])

    if aging_summary['90_plus_days'] > 10000:
        report += "- 🚨 **Address aged payables**: ${:,.2f} over 90 days past due\n".format(aging_summary['90_plus_days'])

    if kpis['exception_rate'] > 20:
        report += "- ⚠️ **Reduce exception rate**: Currently {:.1f}% (target: ≤20%)\n".format(kpis['exception_rate'])

    return report
```

---

## Best Practices Summary

### Invoice Processing
✅ **DO**:
- Use OCR for automated data extraction (saves time, reduces errors)
- Validate all invoices against business rules before processing
- Implement three-way matching (PO → Receipt → Invoice) when possible
- Track OCR confidence and flag low-confidence invoices for manual review
- Maintain comprehensive audit trail of all invoice actions

❌ **DON'T**:
- Process invoices without validating vendor exists and is active
- Skip duplicate checking (can lead to double payments)
- Ignore invoice aging (old invoices can indicate problems)
- Process invoices without required approvals
- Allow same person to enter and approve invoices (SOD violation)

### Approval Routing
✅ **DO**:
- Define clear approval matrix based on amount thresholds
- Implement automatic routing based on department and amount
- Handle approver absence gracefully (delegation, escalation)
- Track approval timeline and escalate stuck approvals
- Allow for emergency/rush approval process when justified

❌ **DON'T**:
- Use vague approval criteria
- Let invoices sit pending approval indefinitely
- Skip approval levels even for trusted vendors
- Allow approvers to approve their own expense invoices
- Process payments without documented approval

### Payment Scheduling
✅ **DO**:
- Always capture early payment discounts when ROI is favorable
- Schedule payments to optimize cash flow while respecting due dates
- Batch payments by vendor to reduce transaction costs
- Use electronic payment methods (ACH) for efficiency
- Communicate payment schedules to vendors

❌ **DON'T**:
- Pay invoices early without discount benefit (wastes cash)
- Pay invoices late habitually (damages vendor relationships)
- Process individual payments when batching is possible
- Use expensive payment methods (wire, overnight check) unnecessarily
- Surprise vendors with unexpected payment delays

### Vendor Management
✅ **DO**:
- Maintain complete, up-to-date vendor records
- Collect W-9 forms before first payment
- Track vendor performance metrics
- Onboard new vendors through formal process
- Regularly review and clean vendor master data
- Validate bank account changes carefully (fraud risk)

❌ **DON'T**:
- Skip vendor onboarding steps
- Process payments without W-9 on file (1099 compliance risk)
- Ignore vendor duplicates in database
- Allow vendors to update their own bank accounts without verification
- Keep inactive vendors in active status

### Reconciliation
✅ **DO**:
- Perform three-way matching for all PO-based invoices
- Reconcile payments to bank statements monthly
- Investigate and resolve discrepancies promptly
- Document all reconciliation adjustments
- Segregate reconciliation duties from payment processing

❌ **DON'T**:
- Skip reconciliation to save time
- Let discrepancies accumulate
- Allow payment processor to also reconcile
- Ignore small variances (they add up)
- Process payments without matching to receipts

### Compliance & Controls
✅ **DO**:
- Enforce strict segregation of duties
- Maintain comprehensive audit trail
- Track 1099-eligible payments throughout the year
- Review SOD violations in access rights regularly
- Train AP staff on fraud detection red flags
- Document all policy exceptions

❌ **DON'T**:
- Allow same person to setup vendor and process payments to them
- Skip audit logging to save database space
- Wait until year-end to track 1099 payments
- Ignore SOD violations "because we're a small team"
- Process suspicious invoices without investigation
- Make policy exceptions without documentation

---

## Integration Checklist

When implementing AP automation:

**Systems to Integrate**:
- [ ] ERP/Accounting System (GL coding, invoice recording)
- [ ] Purchase Order System (PO matching)
- [ ] Receiving System (goods receipt matching)
- [ ] Banking System (payment file generation, reconciliation)
- [ ] Document Management (invoice storage, retrieval)
- [ ] Email System (approval notifications)
- [ ] HRIS (approver lookup, org chart)
- [ ] Payment Networks (ACH, wire, check printing)
- [ ] Vendor Portal (invoice submission, status inquiry)
- [ ] Expense Management (employee reimbursements)

**Data to Exchange**:
- [ ] Vendor master data (sync with ERP)
- [ ] PO data (for matching)
- [ ] Receipt data (for three-way match)
- [ ] GL account codes (for coding invoices)
- [ ] Approver information (from HRIS/org chart)
- [ ] Payment confirmations (from bank)
- [ ] Bank statements (for reconciliation)

---

## Version & Updates

**Version**: 1.0.0
**Last Updated**: 2025-01-19
**Based On**: Industry best practices, SOX compliance standards, GAAP accounting principles

**Future Enhancements**:
- AI/ML-based invoice coding (automated GL code assignment)
- Predictive analytics for cash flow forecasting
- Blockchain integration for payment verification
- Real-time fraud detection with advanced algorithms
- Integration with procurement analytics

---

**You are now equipped with comprehensive accounts payable expertise. Use this skill to automate AP workflows professionally, maintain compliance, detect fraud, and optimize working capital.**
