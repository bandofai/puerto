# Expense Processing Skill

**Expert patterns for expense report processing, OCR, and data extraction**

## Core Principles

1. **Accuracy First**: OCR and data extraction must be validated
2. **Audit Trail**: Maintain complete records of all processing
3. **Policy Awareness**: Check compliance during processing, not after
4. **User Experience**: Make submission easy, minimize manual data entry

---

## Receipt OCR Best Practices

### OCR Tool Selection

**Recommended Tools**:
1. **Tesseract OCR** (Open source, good for printed receipts)
   - Installation: `brew install tesseract` or `apt-get install tesseract-ocr`
   - Best for: Standard printed receipts, invoices

2. **pytesseract** (Python wrapper for Tesseract)
   - Installation: `pip install pytesseract pillow`
   - Best for: Programmatic processing, batch operations

3. **Cloud OCR APIs** (Higher accuracy, cost per API call)
   - Google Cloud Vision API
   - AWS Textract
   - Azure Computer Vision
   - Best for: Handwritten receipts, poor quality images

### Pre-Processing for Better OCR

**Image Quality Improvements**:
```python
from PIL import Image, ImageEnhance, ImageFilter

def preprocess_receipt_image(image_path):
    """Improve image quality before OCR"""
    img = Image.open(image_path)

    # Convert to grayscale
    img = img.convert('L')

    # Increase contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)

    # Sharpen
    img = img.filter(ImageFilter.SHARPEN)

    # Resize if too small (min 1000px width)
    width, height = img.size
    if width < 1000:
        scale = 1000 / width
        img = img.resize((1000, int(height * scale)), Image.LANCZOS)

    return img
```

**Deskewing** (Fix tilted images):
```python
import cv2
import numpy as np

def deskew_image(image_path):
    """Rotate tilted receipts to be straight"""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect edges
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Detect lines
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

    # Calculate average angle
    angles = []
    if lines is not None:
        for rho, theta in lines[:, 0]:
            angle = np.degrees(theta) - 90
            angles.append(angle)

    median_angle = np.median(angles) if angles else 0

    # Rotate image
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, median_angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h),
                             flags=cv2.INTER_CUBIC,
                             borderMode=cv2.BORDER_REPLICATE)

    return rotated
```

### Data Extraction Patterns

**Amount Extraction**:
```python
import re

def extract_amount(ocr_text):
    """Extract monetary amount from receipt text"""

    # Patterns to match
    patterns = [
        r'total[:\s]*\$?(\d+\.\d{2})',      # "Total: $XX.XX"
        r'amount[:\s]*\$?(\d+\.\d{2})',     # "Amount: $XX.XX"
        r'grand\s+total[:\s]*\$?(\d+\.\d{2})',  # "Grand Total: $XX.XX"
        r'balance[:\s]*\$?(\d+\.\d{2})',    # "Balance: $XX.XX"
    ]

    # Try each pattern (case insensitive)
    for pattern in patterns:
        matches = re.findall(pattern, ocr_text, re.IGNORECASE)
        if matches:
            # Get last match (usually the final total)
            return float(matches[-1])

    # Fallback: Extract all amounts and take largest
    all_amounts = re.findall(r'\$?(\d+\.\d{2})', ocr_text)
    if all_amounts:
        amounts = [float(a) for a in all_amounts]
        return max(amounts)

    return None
```

**Date Extraction**:
```python
from dateutil import parser
import re

def extract_date(ocr_text):
    """Extract date from receipt text"""

    # Common date patterns
    date_patterns = [
        r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}',    # MM/DD/YYYY or DD/MM/YYYY
        r'\d{4}[/-]\d{1,2}[/-]\d{1,2}',      # YYYY-MM-DD
        r'[A-Z][a-z]{2}\s+\d{1,2},?\s+\d{4}', # Mon DD, YYYY
    ]

    for pattern in date_patterns:
        matches = re.findall(pattern, ocr_text)
        for match in matches:
            try:
                # Use dateutil parser for flexible parsing
                date = parser.parse(match)
                return date.strftime('%Y-%m-%d')
            except:
                continue

    return None
```

**Vendor Extraction**:
```python
def extract_vendor(ocr_text):
    """Extract vendor/merchant name from receipt"""

    lines = ocr_text.strip().split('\n')

    # Usually first non-empty line is vendor
    for line in lines:
        line = line.strip()
        if len(line) > 2:  # Skip very short lines
            # Clean up common OCR artifacts
            vendor = re.sub(r'[^a-zA-Z0-9\s&\'-]', '', line)
            return vendor.strip()

    return "Unknown Vendor"
```

**Category Inference**:
```python
def infer_category(vendor, ocr_text=None):
    """Infer expense category from vendor name"""

    vendor_lower = vendor.lower()
    text_lower = (ocr_text or "").lower()

    # Define category keywords
    categories = {
        'Meals & Entertainment': [
            'restaurant', 'cafe', 'coffee', 'starbucks', 'mcdonald',
            'burger', 'pizza', 'food', 'diner', 'grill', 'kitchen',
            'bar', 'pub', 'brewery', 'lunch', 'dinner', 'breakfast'
        ],
        'Lodging': [
            'hotel', 'inn', 'motel', 'lodge', 'resort', 'airbnb',
            'marriott', 'hilton', 'hyatt', 'holiday inn'
        ],
        'Transportation': [
            'uber', 'lyft', 'taxi', 'cab', 'parking', 'garage',
            'metro', 'transit', 'bus', 'train', 'subway'
        ],
        'Travel': [
            'airline', 'airways', 'flight', 'airport', 'delta',
            'united', 'american airlines', 'southwest', 'jetblue'
        ],
        'Office Supplies': [
            'office', 'staples', 'depot', 'supply', 'paper'
        ],
        'Professional Development': [
            'conference', 'training', 'course', 'seminar', 'workshop',
            'certification', 'education'
        ],
        'Software/Subscriptions': [
            'saas', 'software', 'subscription', 'aws', 'azure',
            'github', 'adobe', 'microsoft', 'google cloud'
        ]
    }

    # Check vendor name and text for category keywords
    combined_text = f"{vendor_lower} {text_lower}"

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in combined_text:
                return category

    return 'Other'
```

### Confidence Scoring

**Calculate confidence based on data quality**:
```python
def calculate_confidence_score(extracted_data):
    """Calculate confidence in OCR extraction quality"""

    confidence = 1.0
    penalties = []

    # Penalize missing key fields
    if not extracted_data.get('vendor'):
        confidence -= 0.3
        penalties.append('Missing vendor')

    if not extracted_data.get('date'):
        confidence -= 0.2
        penalties.append('Missing date')

    if not extracted_data.get('amount') or extracted_data['amount'] <= 0:
        confidence -= 0.4
        penalties.append('Missing or invalid amount')

    # Penalize unreasonable values
    if extracted_data.get('amount', 0) > 10000:
        confidence -= 0.1
        penalties.append('Unusually high amount')

    # Penalize if date is in future
    if extracted_data.get('date'):
        from datetime import datetime
        try:
            date = datetime.strptime(extracted_data['date'], '%Y-%m-%d')
            if date > datetime.now():
                confidence -= 0.2
                penalties.append('Future date')
        except:
            pass

    # Bonus for complete data
    required_fields = ['vendor', 'date', 'amount', 'category']
    if all(extracted_data.get(f) for f in required_fields):
        confidence += 0.1

    confidence = max(0.0, min(1.0, confidence))

    return {
        'score': confidence,
        'penalties': penalties,
        'needs_review': confidence < 0.8
    }
```

---

## Expense Report Assembly

### Report Structure Standards

**Comprehensive Report Format**:
- **Header**: Report ID, employee info, period
- **Summary**: Totals by category, count, compliance status
- **Itemized List**: All expenses with details
- **Policy Compliance**: Violations and warnings
- **Supporting Documents**: Receipt references
- **Approval Chain**: Required approvers
- **Metadata**: Created date, version, status

### Data Validation Checklist

**Before finalizing report**:
- [ ] All amounts are positive numbers
- [ ] All dates are valid and in past
- [ ] All expenses have business purpose
- [ ] All expenses have receipts (if required)
- [ ] All categories are valid
- [ ] No duplicate expenses (same vendor/date/amount)
- [ ] Employee information is complete
- [ ] Period dates are logical
- [ ] Currency codes are valid (ISO 4217)

### Duplicate Detection

```python
def detect_duplicates(expenses):
    """Find potential duplicate expenses"""

    seen = {}
    duplicates = []

    for expense in expenses:
        # Create fingerprint
        fingerprint = (
            expense['vendor'].lower().strip(),
            expense['date'],
            round(expense['amount'], 2)
        )

        if fingerprint in seen:
            duplicates.append({
                'expense_1': seen[fingerprint],
                'expense_2': expense['expense_id'],
                'vendor': expense['vendor'],
                'date': expense['date'],
                'amount': expense['amount'],
                'confidence': 'high'  # Exact match
            })
        else:
            seen[fingerprint] = expense['expense_id']

    return duplicates
```

---

## Policy Integration

### Real-Time Policy Checking

**Check during processing, not after**:

```python
def check_policy_during_processing(expense, policy_rules):
    """Check policy compliance while processing"""

    issues = []
    warnings = []

    category_rules = policy_rules.get(expense['category'], {})

    # Check amount limits
    if 'per_item_limit' in category_rules:
        if expense['amount'] > category_rules['per_item_limit']:
            issues.append({
                'type': 'amount_exceeds_limit',
                'severity': 'critical',
                'message': f"Amount ${expense['amount']} exceeds {expense['category']} limit ${category_rules['per_item_limit']}"
            })

    # Check receipt requirement
    receipt_threshold = policy_rules.get('receipts', {}).get('required_above', 25.00)
    if expense['amount'] >= receipt_threshold:
        if not expense.get('receipt_path'):
            issues.append({
                'type': 'missing_receipt',
                'severity': 'critical',
                'message': f"Receipt required for amounts ≥ ${receipt_threshold}"
            })

    # Check business purpose
    if not expense.get('business_purpose') or len(expense['business_purpose']) < 10:
        warnings.append({
            'type': 'vague_business_purpose',
            'severity': 'medium',
            'message': 'Business purpose should be detailed and specific'
        })

    return {
        'compliant': len(issues) == 0,
        'issues': issues,
        'warnings': warnings
    }
```

---

## Batch Processing

### Processing Multiple Receipts

```bash
#!/bin/bash
# batch_process_receipts.sh

RECEIPTS_DIR="$1"
OUTPUT_DIR="./expenses/receipts"

mkdir -p "$OUTPUT_DIR"

# Find all image files
find "$RECEIPTS_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.pdf" \) | while read RECEIPT_PATH; do

    FILENAME=$(basename "$RECEIPT_PATH")
    RECEIPT_ID="receipt_$(date +%Y%m%d)_$(uuidgen | cut -d'-' -f1)"

    echo "Processing: $FILENAME → $RECEIPT_ID"

    # Process with OCR
    python3 << EOF
import pytesseract
from PIL import Image
import json
import sys

try:
    img = Image.open("$RECEIPT_PATH")
    text = pytesseract.image_to_string(img)

    # Extract data (use functions defined above)
    data = {
        "receipt_id": "$RECEIPT_ID",
        "image_path": "$RECEIPT_PATH",
        "raw_text": text,
        # ... additional extraction ...
    }

    with open("$OUTPUT_DIR/${RECEIPT_ID}.json", 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✅ Processed: $RECEIPT_ID")

except Exception as e:
    print(f"❌ Error: {str(e)}", file=sys.stderr)
    sys.exit(1)
EOF

done

echo ""
echo "Batch processing complete!"
echo "Processed receipts: $OUTPUT_DIR"
```

---

## Error Handling

### Common OCR Errors

| Error Type | Cause | Solution |
|------------|-------|----------|
| No text extracted | Poor image quality | Pre-process image, increase contrast |
| Wrong vendor | Header logo misread | Use first text line, ignore images |
| Wrong amount | Multiple totals | Look for "Total" keyword, take largest |
| Future date | OCR misread (8→3, 1→7) | Validate dates, flag if >today |
| Currency symbols | Special characters | Normalize: remove $, €, £ |

### Handling Failed OCR

```python
def handle_ocr_failure(image_path, error):
    """Create manual review record when OCR fails"""

    return {
        "receipt_id": f"manual_review_{uuid.uuid4().hex[:8]}",
        "image_path": image_path,
        "status": "needs_manual_review",
        "ocr_error": str(error),
        "confidence_score": 0.0,
        "extracted_data": None,
        "manual_entry_required": True,
        "created_at": datetime.utcnow().isoformat()
    }
```

---

## Output Quality Standards

**High-Quality Expense Reports Have**:
1. ✅ All fields populated (no null/empty critical fields)
2. ✅ Consistent formatting (dates, amounts, currencies)
3. ✅ Valid business purposes (specific, not vague)
4. ✅ Receipt references (paths exist and accessible)
5. ✅ Policy compliance checked
6. ✅ Duplicate detection run
7. ✅ Metadata complete (timestamps, versions)
8. ✅ Audit trail maintained

**Verification Script**:
```bash
# Verify report quality
verify_report_quality() {
    local REPORT_PATH=$1

    echo "Verifying report quality: $REPORT_PATH"

    # Check required fields
    REQUIRED_FIELDS=("report_id" "employee" "period" "summary" "expenses")
    for FIELD in "${REQUIRED_FIELDS[@]}"; do
        if ! jq -e ".$FIELD" "$REPORT_PATH" > /dev/null 2>&1; then
            echo "❌ Missing required field: $FIELD"
            return 1
        fi
    done

    # Check each expense has required fields
    EXPENSE_COUNT=$(jq '.expenses | length' "$REPORT_PATH")
    for ((i=0; i<$EXPENSE_COUNT; i++)); do
        if ! jq -e ".expenses[$i].receipt_path" "$REPORT_PATH" > /dev/null 2>&1; then
            EXP_ID=$(jq -r ".expenses[$i].expense_id" "$REPORT_PATH")
            echo "⚠️ Expense $EXP_ID missing receipt"
        fi
    done

    echo "✅ Report quality verification complete"
}
```

---

## Best Practices Summary

1. **Pre-process images** before OCR (contrast, deskew, resize)
2. **Validate extracted data** with confidence scoring
3. **Check policy in real-time** during processing
4. **Maintain audit trail** for all operations
5. **Handle failures gracefully** with manual review fallback
6. **Batch process efficiently** for multiple receipts
7. **Verify output quality** before finalizing
8. **Provide clear feedback** on what needs manual attention

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: Receipt OCR, expense report assembly, policy checking
