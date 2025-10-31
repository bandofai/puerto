# Home Inventory System Plugin

**Asset cataloging and insurance documentation specialist for household items**

Version: 1.0.0
Author: Band of AI
Issue: #111

---

## Overview

The Home Inventory System plugin provides a comprehensive solution for cataloging household assets, tracking their values over time, and generating professional insurance documentation. This plugin helps homeowners maintain detailed records of their possessions for insurance claims, estate planning, moving, and general asset management.

### Key Capabilities

- **Photo-based cataloging** with detailed metadata capture
- **Purchase tracking** including dates, prices, serial numbers, and receipts
- **Room-by-room organization** for logical inventory management
- **Current value estimation** using depreciation calculations and market research
- **Replacement cost analysis** for insurance adequacy
- **Professional PDF reports** ready for insurance companies
- **Insurance claim preparation** with comprehensive documentation

---

## Plugin Structure

```
home-inventory-system/
├── agents/
│   ├── asset-cataloger.md       # Catalogs household items (Sonnet)
│   ├── value-estimator.md       # Estimates current values (Sonnet)
│   └── insurance-reporter.md    # Generates insurance docs (Haiku)
├── skills/
│   └── asset-management/
│       └── SKILL.md             # Asset cataloging expertise
├── templates/
│   ├── asset-catalog.json       # Item catalog structure
│   ├── room-inventory.json      # Room-by-room template
│   └── insurance-report-template.md  # Insurance documentation format
├── .claude-plugin               # Plugin configuration
└── README.md                    # This file
```

---

## Agents

### 1. Asset Cataloger (Sonnet)

**Purpose:** Catalogs household items with comprehensive documentation

**Triggers:**
- "Catalog my [room] items"
- "Add items to my home inventory"
- "Document my [electronics/jewelry/furniture]"
- "Create inventory for insurance"

**Capabilities:**
- Photo-based item identification
- Purchase information tracking (date, price, serial number)
- Room-by-room organization
- Category assignment (electronics, furniture, jewelry, etc.)
- Condition assessment
- Receipt and warranty tracking

**Tools:** Read, Write, Edit, Glob, Grep

**Output:**
- Updated JSON catalog in `~/Documents/Home-Inventory/catalog.json`
- Room-specific inventory files
- Photo organization and referencing
- Summary of cataloged items

**Example Usage:**
```
User: "I need to catalog all the items in my living room for insurance purposes"

Agent:
1. Reads asset-management skill for best practices
2. Creates/loads inventory catalog
3. Guides user through item documentation
4. Captures all critical information (serial numbers, photos, values)
5. Organizes items by category and location
6. Saves structured JSON catalog
7. Provides summary and recommendations
```

---

### 2. Value Estimator (Sonnet)

**Purpose:** Estimates current market values and replacement costs for household items

**Triggers:**
- "Update values in my home inventory"
- "Estimate current value of [item]"
- "Calculate depreciation for my items"
- "What's my [category] worth now?"

**Capabilities:**
- Depreciation calculation (straight-line and declining balance methods)
- Market value research using comparable sales
- Replacement cost estimation
- Category-specific depreciation rates
- Condition-adjusted valuations
- Annual value updates

**Tools:** Read, Write, Edit, Grep, Glob

**Output:**
- Updated current values in catalog
- Replacement cost calculations
- Depreciation methodology documentation
- Market research references
- Value change summary
- Recommendations for appraisals

**Example Usage:**
```
User: "I need to update the values in my inventory - I cataloged everything 2 years ago"

Agent:
1. Reads asset-management skill for depreciation methods
2. Loads existing inventory
3. Applies appropriate depreciation for each category
4. Researches market values for high-value items
5. Calculates replacement costs
6. Updates all values in catalog
7. Flags items needing professional appraisal
8. Provides summary of value changes
```

---

### 3. Insurance Reporter (Haiku)

**Purpose:** Generates professional PDF reports for insurance documentation

**Triggers:**
- "Create insurance report"
- "Generate home inventory report for my insurer"
- "I need documentation for an insurance claim"
- "Export my inventory to PDF"

**Capabilities:**
- PDF report generation with professional formatting
- Room-by-room inventory listings
- Category summaries with totals
- High-value items section (>$1,000)
- Total value calculations
- Photo appendix with references
- Insurance coverage recommendations

**Tools:** Read, Write, Bash, Grep, Glob

**Output:**
- Professional markdown report
- PDF conversion (using pandoc/wkhtmltopdf)
- Room-by-room summaries
- Category breakdowns
- High-value items documentation
- Insurance recommendations

**Example Usage:**
```
User: "I need to provide an inventory to my insurance company"

Agent:
1. Reads asset-management skill for insurance requirements
2. Loads complete inventory catalog
3. Generates comprehensive markdown report using template
4. Organizes by rooms and categories
5. Highlights high-value items requiring riders
6. Converts to professional PDF
7. Provides recommendations for coverage
8. Saves to ~/Documents/Home-Inventory/reports/
```

---

## Asset Management Skill

The asset-management skill provides expert guidance on:

### Asset Categorization
- Electronics (TVs, computers, cameras, audio equipment)
- Appliances (kitchen, laundry, HVAC)
- Furniture (sofas, tables, beds, storage)
- Jewelry and watches (rings, necklaces, luxury timepieces)
- Art and collectibles (paintings, antiques, memorabilia)
- Tools and equipment (power tools, lawn equipment)
- Sports and recreation (bikes, golf clubs, exercise equipment)

### Depreciation Methods

**Straight-Line Depreciation:**
```
Annual Depreciation = (Purchase Price - Salvage Value) / Useful Life
Current Value = Purchase Price - (Years Owned × Annual Depreciation)
```
- Best for: Furniture, appliances, tools

**Declining Balance Depreciation:**
```
Value After Year N = Purchase Price × (1 - Rate)^N
```
- Best for: Electronics, computers, technology (30-40% annual rate)

### Photography Best Practices

**Essential Photos:**
1. Overall view - full item in good lighting
2. Serial number/label - close-up showing make/model/serial
3. Condition indicators - any wear, damage, or unique features

**Enhanced for items >$500:**
4. Multiple angles - front, back, sides
5. In context - item in location
6. Scale reference - for size determination

**Maximum for items >$2,000:**
7. Packaging/documentation
8. Authentication certificates
9. Comparison photos
10. Video walkthrough

### Insurance Claim Requirements

**Minimum Documentation:**
- Item description
- Purchase date and price
- Current replacement cost
- Photo documentation
- Proof of ownership

**Enhanced for items >$1,000:**
- Serial/model numbers
- Multiple photos
- Professional appraisal
- Condition assessment
- Maintenance records

**Special Categories (Jewelry, Art):**
- Professional appraisal (updated every 3-5 years)
- Certification (GIA for gems)
- Provenance documentation
- Insurance rider documentation

### Value Estimation Techniques

**Market Research Sources:**
- eBay sold listings (actual sale prices)
- Craigslist/Facebook Marketplace
- Specialty sites (Reverb, Chrono24, 1stDibs)
- Current retail prices for replacement cost
- Professional appraisers

**Condition Grading:**
- Excellent: 90-100% of calculated value
- Good: 70-85% of calculated value
- Fair: 50-65% of calculated value
- Poor: 25-45% of calculated value

---

## Templates

### 1. asset-catalog.json

**Purpose:** Master inventory structure for all household items

**Key Sections:**
- Property information (address, owner, insurance details)
- Summary (totals by category and room)
- Items array (detailed item records)
- Metadata (backup info, review dates)

**Item Structure:**
```json
{
  "item_id": "ITEM-001",
  "name": "Samsung 65\" Smart TV",
  "category": "electronics",
  "subcategory": "television",
  "room": "living-room",
  "acquisition": {
    "purchase_date": "2023-06-15",
    "purchase_price": 1299.99
  },
  "identification": {
    "serial_number": "SN123456789",
    "model_number": "UN65AU8000"
  },
  "valuation": {
    "current_value": 800.00,
    "replacement_cost": 1499.99,
    "depreciation_method": "declining-balance"
  },
  "condition": {
    "grade": "excellent"
  },
  "documentation": {
    "photos": ["photos/item-001-1.jpg"],
    "warranty_expiration": "2026-06-15"
  }
}
```

---

### 2. room-inventory.json

**Purpose:** Room-specific inventory with totals and organization

**Key Sections:**
- Room details (name, floor, square footage)
- Summary (item count, total value by category)
- Room photos (overview, panorama)
- Items list (references to main catalog)
- Features (flooring, built-ins, etc.)

**Use Cases:**
- Room-by-room insurance documentation
- Moving inventory by room
- High-value room identification
- Organization and retrieval

---

### 3. insurance-report-template.md

**Purpose:** Professional insurance documentation format

**Key Sections:**
- Executive summary with totals
- Room-by-room detailed listings
- Category summaries
- High-value items section (>$1,000)
- Photo appendix with references
- Insurance recommendations
- Supporting documentation references

**Output:** Converts to professional PDF for insurance submission

---

## Installation

### Plugin Installation

1. **Copy plugin to plugins directory:**
   ```bash
   cp -r home-inventory-system ~/.claude/plugins/
   ```

2. **Verify installation:**
   ```bash
   ls ~/.claude/plugins/home-inventory-system/
   ```

3. **Agents will be auto-discovered** by Claude Code

### Dependencies

**Required for PDF generation:**

```bash
# macOS
brew install pandoc wkhtmltopdf

# Ubuntu/Debian
apt-get install pandoc wkhtmltopdf

# Verify installation
pandoc --version
wkhtmltopdf --version
```

**Alternative PDF tools:**
- markdown-pdf (npm package)
- Online converters (fallback option)

---

## Usage Guide

### Getting Started

**1. Initial Inventory Creation**

```
User: "I need to create a home inventory for insurance. Let's start with my living room."

Claude: "I'll help you create a comprehensive home inventory. Let me start by using the asset-cataloger agent to document your living room items..."

[asset-cataloger agent activates]
- Reads asset-management skill
- Creates inventory structure
- Guides item documentation
- Captures photos, serial numbers, values
- Saves organized catalog
```

**2. Adding Individual Items**

```
User: "I just bought a new MacBook Pro. Add it to my inventory."

Claude: "I'll catalog your new MacBook Pro..."

[asset-cataloger agent]
- Prompts for purchase details
- Requests serial number
- Captures specifications
- Assigns category and room
- Updates catalog with new item
```

**3. Annual Value Update**

```
User: "Update all values in my inventory - it's been a year since I created it."

Claude: "I'll update your inventory values..."

[value-estimator agent]
- Loads existing catalog
- Applies depreciation by category
- Researches market values for high-value items
- Updates replacement costs
- Provides value change summary
```

**4. Insurance Report Generation**

```
User: "Generate an insurance report - I need to update my coverage."

Claude: "I'll create a comprehensive insurance report..."

[insurance-reporter agent]
- Loads complete inventory
- Generates detailed markdown report
- Organizes by rooms and categories
- Highlights high-value items
- Converts to professional PDF
- Provides coverage recommendations
```

---

### Common Workflows

#### Complete Home Inventory (First Time)

**Estimated Time:** 3-5 hours for average home

**Process:**
1. **Room-by-room cataloging**
   - Start with highest-value room
   - Document 1-2 rooms per session
   - Take photos as you go

2. **Value estimation**
   - Use purchase prices where available
   - Estimate older items
   - Research high-value items

3. **Organization and review**
   - Verify all items entered
   - Check totals by room/category
   - Identify items needing appraisal

4. **Report generation**
   - Create initial insurance report
   - Review coverage adequacy
   - Schedule appraisals if needed

**Commands:**
```
"Let's catalog my living room for insurance"
"Add my master bedroom items to inventory"
"Estimate values for all items I've cataloged"
"Generate an insurance report with everything"
```

---

#### Annual Inventory Review

**When:** Same time each year (tax time, policy renewal)

**Process:**
1. **Review existing items**
   - Verify items still present
   - Remove sold/donated items
   - Note condition changes

2. **Add new purchases**
   - Document items acquired during year
   - Include all purchase information

3. **Update values**
   - Apply depreciation
   - Update replacement costs
   - Get new appraisals if needed (every 3-5 years)

4. **Generate updated report**
   - Create current year report
   - Review insurance coverage
   - Adjust coverage as needed

**Commands:**
```
"Add this year's purchases to my inventory: [items]"
"Update all values in my home inventory"
"Remove these items I sold: [items]"
"Generate updated insurance report for 2025"
```

---

#### High-Value Item Documentation

**For items >$1,000:**

**Process:**
1. **Detailed cataloging**
   - Multiple photos (all angles)
   - Serial numbers mandatory
   - Original packaging/documentation
   - Appraisal if available

2. **Professional appraisal** (if needed)
   - Jewelry: Every 3-5 years
   - Art: Every 3-5 years
   - Collectibles: As market changes

3. **Insurance rider**
   - Schedule on policy
   - Agreed value coverage
   - Include mysterious disappearance

**Commands:**
```
"Catalog my engagement ring - it's worth $6,000"
"Document my art collection for insurance"
"I need to schedule my jewelry on my policy"
```

---

#### Insurance Claim Preparation

**After loss event:**

**Process:**
1. **File police report** (if theft)
2. **Contact insurance** (within 24-48 hours)
3. **Generate claim documentation**
   - Provide complete inventory
   - Highlight affected items
   - Include photos and receipts
4. **Submit to adjuster**

**Commands:**
```
"Generate insurance claim documentation for stolen items"
"Create report showing items damaged in [event]"
"I need documentation for items in [room] that were lost"
```

---

## File Organization

### Default Directory Structure

```
~/Documents/Home-Inventory/
├── catalog.json                 # Master inventory
├── config.json                  # Configuration
├── rooms/
│   ├── living-room.json
│   ├── kitchen.json
│   ├── master-bedroom.json
│   ├── bedroom-guest.json
│   ├── office.json
│   └── garage.json
├── photos/
│   ├── item-001-1-overall.jpg
│   ├── item-001-2-serial.jpg
│   └── ...
├── receipts/
│   ├── 2023/
│   ├── 2024/
│   └── 2025/
├── appraisals/
│   ├── jewelry-appraisal-2024.pdf
│   └── art-appraisal-2023.pdf
└── reports/
    ├── insurance-report-2025-01-15.md
    ├── insurance-report-2025-01-15.pdf
    └── archive/
```

### Backup Strategy

**3-2-1 Rule:**
- **3 copies** of data
- **2 different** media types
- **1 off-site** backup

**Implementation:**
1. Primary: Local computer (`~/Documents/Home-Inventory/`)
2. Secondary: External hard drive (weekly backup)
3. Off-site: Cloud storage (Dropbox, Google Drive, iCloud)

**Critical:** Cloud backup ensures inventory survives catastrophic loss (fire, flood) when you need it most for insurance claims.

---

## Best Practices

### Documentation

**DO:**
- Photograph every item worth >$100
- Record all serial numbers
- Save all receipts (digital and physical)
- Update after major purchases
- Review annually
- Backup to cloud

**DON'T:**
- Skip serial numbers (critical for claims)
- Use blurry or dark photos
- Estimate values without research
- Forget to backup
- Share publicly (security risk)
- Neglect high-value items

### Photography

**Quality Standards:**
- Resolution: Minimum 1920×1080
- Format: JPEG or PNG
- Lighting: Natural or well-lit
- Focus: Sharp and clear
- Framing: Item fills 60-80% of frame

**Essential Shots:**
1. Overall view
2. Serial number close-up
3. Condition indicators
4. Multiple angles (for valuable items)

### Valuation

**Accuracy is Critical:**
- Use actual purchase prices where available
- Research market values for estimates
- Apply appropriate depreciation method
- Get professional appraisals for items >$2,500
- Update values annually
- Document methodology

**Three Value Types:**
1. **Purchase Price:** What you paid
2. **Current Market Value:** What you could sell for today
3. **Replacement Cost:** Cost to buy new equivalent

### Insurance

**Coverage Adequacy:**
- Total replacement cost should match or be below coverage limit
- Schedule high-value items (>$1,000) separately
- Verify sub-limits for jewelry, electronics, etc.
- Consider replacement cost vs. actual cash value policy
- Update coverage after major purchases

**Documentation Requirements:**
- Keep inventory separate from home (cloud essential)
- Update insurance agent annually
- Provide detailed photos
- Maintain current appraisals
- Know your policy limits and exclusions

---

## Insurance Coverage Guide

### Standard Policy Limits

**Typical sub-limits:**
- Jewelry: $1,500-$2,500 total
- Watches: Included in jewelry limit
- Furs: $1,500-$2,000
- Silverware: $2,500
- Firearms: $2,000-$2,500
- Electronics: Usually covered fully (verify)
- Art: $1,500-$2,500 per item

### When to Schedule Items

**Get separate riders/floaters for:**
- Any item exceeding category limits
- Jewelry >$2,500
- Individual art pieces >$2,500
- Collections (art, wine, collectibles) >$5,000
- Professional equipment (musical instruments, cameras)
- High-value electronics (if sub-limits apply)

### Policy Types

**Actual Cash Value (ACV):**
- Pays depreciated value
- Lower premiums
- May not cover full replacement
- Example: 3-year-old TV worth $500 now (paid $1,200)

**Replacement Cost Value (RCV):**
- Pays cost to replace with new equivalent
- Higher premiums
- Better coverage
- Example: 3-year-old TV replaced with current $1,200 model

**Agreed Value:**
- Pre-agreed value (for collectibles, art)
- Requires appraisal
- No depreciation disputes
- Example: Art insured for appraised $10,000

---

## Troubleshooting

### PDF Generation Issues

**Problem:** "pandoc not found"

**Solution:**
```bash
# Install pandoc
brew install pandoc  # macOS
apt-get install pandoc  # Ubuntu

# Verify
pandoc --version
```

**Problem:** "wkhtmltopdf not found"

**Solution:**
```bash
# Install wkhtmltopdf
brew install wkhtmltopdf  # macOS
apt-get install wkhtmltopdf  # Ubuntu

# Verify
wkhtmltopdf --version
```

**Alternative:** Agent will provide markdown report if PDF tools unavailable. Convert manually using online tools or install dependencies later.

---

### Data Issues

**Problem:** "Catalog file not found"

**Solution:**
- Agent will create new catalog automatically
- Default location: `~/Documents/Home-Inventory/catalog.json`
- Specify custom location if needed

**Problem:** "Invalid JSON in catalog"

**Solution:**
- Agent will validate and attempt to fix
- Restore from backup if corrupted
- Cloud backup should have good copy

---

### Value Estimation Issues

**Problem:** "No comparable sales found"

**Solution:**
- Agent uses depreciation calculation only
- Marks as "estimated - no market data"
- Suggests professional appraisal for high-value items

**Problem:** "Depreciation rate unclear"

**Solution:**
- Agent applies category-standard rate from skill
- Documents methodology
- Adjusts for condition

---

## Security Considerations

### Sensitive Information

**This inventory contains:**
- Serial numbers (theft risk)
- Purchase prices (privacy)
- Photos of valuables (security risk)
- Home layout (security risk)

### Protection Measures

**DO:**
- Encrypt sensitive files
- Password-protect documents
- Use secure cloud storage with 2FA
- Limit access and sharing
- Don't post publicly

**DON'T:**
- Share on social media
- Store only locally (need off-site backup)
- Use weak passwords
- Leave unencrypted on public cloud

**Encryption Example:**
```bash
# Encrypt catalog
openssl enc -aes-256-cbc -salt -in catalog.json -out catalog.json.enc

# Decrypt when needed
openssl enc -d -aes-256-cbc -in catalog.json.enc -out catalog.json
```

---

## Advanced Use Cases

### Estate Planning

**Inventory aids:**
- Asset distribution planning
- Heir identification of items
- Valuation for estate taxes
- Avoiding disputes
- Charitable donation documentation

**Include:**
- Provenance/history
- Sentimental value notes
- Distribution wishes
- Share with executor

---

### Moving and Relocation

**Benefits:**
- Moving company estimates
- Insurance during move
- Unpacking verification
- Damage claims

**Process:**
1. Print complete inventory
2. Take "before move" photos
3. Note condition of all items
4. Verify insurance during move
5. Check items during unpacking
6. Document damage immediately
7. Update room locations after move

---

### Tax Deductions

**Casualty Loss:**
- Inventory proves loss amount
- Photos show condition
- Purchase prices document basis

**Charitable Donations:**
- Fair market value documentation
- Item condition assessment
- Photos for high-value items

**Business Use:**
- Home office equipment
- Depreciation tracking
- Purchase documentation

---

## Integration with Other Plugins

### Expense Manager

**Connection:** Track receipts for purchases

```
User: "I bought a new TV, add to inventory and track the expense"

1. expense-manager: Records expense, saves receipt
2. asset-cataloger: Adds to inventory, references receipt
```

### Tax Compliance

**Connection:** Charitable donations, casualty losses

```
User: "I donated these items to charity, need for taxes"

1. asset-cataloger: Documents donated items with values
2. tax-compliance: Includes in deduction calculations
```

---

## Maintenance Schedule

### Immediate (At Purchase)
- [ ] Save receipt
- [ ] Photograph receipt
- [ ] Note item details

### Within 1 Week
- [ ] Unbox and photograph item
- [ ] Record serial number
- [ ] Add to inventory catalog

### Monthly
- [ ] Review new purchases
- [ ] Add any missing items
- [ ] Backup to cloud

### Annually
- [ ] Complete inventory review
- [ ] Update all values
- [ ] Add new purchases
- [ ] Remove sold/donated items
- [ ] Retake photos if condition changed
- [ ] Update appraisals (every 3-5 years)
- [ ] Generate updated insurance report
- [ ] Review coverage adequacy

---

## FAQ

**Q: How long does initial inventory take?**
A: 3-5 hours for average home. Budget 1-2 hours per major room.

**Q: Do I need to catalog everything?**
A: Focus on items worth >$100. Small items can be grouped (e.g., "Kitchen cookware set - $500").

**Q: How often should I update values?**
A: Annually at minimum. After major purchases or before policy renewal.

**Q: What if I don't have purchase receipts?**
A: Estimate and mark as "estimated." Use current market research. Going forward, save all receipts.

**Q: Do I need professional appraisals?**
A: For jewelry, art, and collectibles >$2,500, yes. Update every 3-5 years.

**Q: How do I handle items I inherited?**
A: Mark acquisition type as "inherited," estimate acquisition date, use appraisal value if available, note provenance.

**Q: What if serial number is missing?**
A: Document reason (no serial, worn off), include detailed description, take extra photos for identification.

**Q: Should I catalog clothing?**
A: Only high-value items (furs, designer pieces). Group ordinary clothing by category.

**Q: How do I backup my inventory?**
A: Cloud storage is essential (Dropbox, Google Drive). Use 3-2-1 rule: 3 copies, 2 media types, 1 off-site.

**Q: Can I use this for business assets?**
A: Yes, but keep separate from personal inventory. Consider additional business-specific tracking.

---

## Support and Contribution

### Getting Help

**Documentation:**
- This README
- Asset-management skill (`skills/asset-management/SKILL.md`)
- Template examples in `templates/`

**Issues:**
- Report bugs or request features via GitHub issues
- Include agent logs and error messages
- Describe expected vs. actual behavior

### Contributing

**Improvements welcome:**
- Additional templates
- Enhanced depreciation methods
- New category types
- Better PDF generation
- Integration with other systems

---

## Version History

### Version 1.0.0 (January 2025)
- Initial release
- 3 agents (asset-cataloger, value-estimator, insurance-reporter)
- Asset-management skill with comprehensive guidance
- 3 templates (catalog, room inventory, insurance report)
- Complete documentation

---

## License

Part of the Puerto plugin system by Band of AI.

---

## Acknowledgments

Built following expert patterns from the subagent-creation skill, with insurance industry best practices and professional appraisal standards.

**Remember:** The best inventory system is the one you'll actually maintain. Start simple, be consistent, and update regularly. Your future self (during an insurance claim) will thank you.
