# Moving Coordination Skill

Comprehensive patterns and best practices for moving logistics, timeline management, and successful relocation coordination.

## Moving Timeline Standards

### 8-Week Timeline Structure

The standard moving timeline spans 8 weeks from planning to move-in completion:

**Weeks 1-2: Planning & Research**
- Budget creation and mover selection
- Preliminary inventory and decluttering strategy
- School/daycare research (if applicable)
- Lease/closing date confirmation

**Weeks 3-4: Preparation & Early Packing**
- Declutter and organize belongings
- Pack non-essentials and storage items
- Order packing supplies
- Research utility providers

**Weeks 5-6: Active Packing & Coordination**
- Pack majority of rooms (except essentials)
- Schedule all utility transfers
- Submit USPS address change
- Update financial institutions

**Weeks 7-8: Final Preparation & Moving**
- Pack remaining items and essentials
- Confirm mover details
- Final walkthrough and cleaning
- Moving day execution and immediate settling

### Phase Definitions

```json
{
  "planning_research": {
    "weeks": [1, 2],
    "focus": "Decision-making and vendor selection",
    "key_tasks": ["budget", "mover_selection", "inventory", "timeline"]
  },
  "preparation": {
    "weeks": [3, 4],
    "focus": "Organization and early packing",
    "key_tasks": ["declutter", "supplies", "utility_research", "early_packing"]
  },
  "active_packing": {
    "weeks": [5, 6],
    "focus": "Bulk packing and coordination",
    "key_tasks": ["room_packing", "utility_scheduling", "address_changes"]
  },
  "final_execution": {
    "weeks": [7, 8],
    "focus": "Final preparation and moving",
    "key_tasks": ["final_packing", "confirmation", "moving", "settling"]
  }
}
```

## Task Prioritization System

### Priority Levels

**Critical**: Must be completed on time or move cannot proceed
- Moving date confirmation
- Mover booking
- Utility connection at new address
- USPS mail forwarding
- Key financial institution updates

**High**: Important for smooth transition, minimal flexibility
- Utility disconnection scheduling
- Major address updates (DMV, employer, insurance)
- Essential item packing
- Box labeling system setup

**Medium**: Should be completed but have some flexibility
- Non-essential decluttering
- Subscription updates
- Address updates for minor accounts
- Cleaning supplies organization

**Low**: Nice to have, can be completed after move
- Magazine subscription updates
- Loyalty program address changes
- Non-essential service cancellations

### Task Dependencies

```python
dependencies = {
    "pack_room": ["acquire_supplies", "declutter_complete"],
    "schedule_utilities": ["new_address_confirmed", "move_date_confirmed"],
    "label_boxes": ["numbering_system_created"],
    "final_walkthrough": ["all_packing_complete", "cleaning_complete"],
    "utility_connect": ["lease_signed", "move_in_date_confirmed"]
}
```

## Inventory Management Patterns

### Room-by-Room Inventory Schema

```json
{
  "room_id": "living_room",
  "name": "Living Room",
  "items": [
    {
      "name": "Television 55 inch",
      "quantity": 1,
      "category": "electronics",
      "fragile": true,
      "valuable": true,
      "essential": false,
      "packed": false,
      "box_number": null,
      "estimated_value": 800,
      "notes": "Original box available in garage"
    }
  ],
  "packing_priority": "medium",
  "estimated_boxes": 8,
  "actual_boxes": 0,
  "packing_complete": false
}
```

### Item Categories

**Electronics**: TVs, computers, gaming consoles, audio equipment
- Require original boxes if possible
- Need anti-static wrapping
- Cable management critical
- Photo documentation recommended

**Fragile**: Glassware, artwork, ceramics, mirrors
- Double boxing for valuable items
- Bubble wrap and packing paper
- Clear "FRAGILE" labeling on all sides
- Professional packing for high-value items

**Essential**: Items needed for first 24-48 hours
- Toiletries and medications
- Change of clothes
- Important documents
- Basic kitchen items
- Phone chargers and electronics
- Pet supplies

**Valuable**: Jewelry, collectibles, important documents
- Consider personal transport
- Insurance documentation
- Photograph items before packing
- Itemized list with estimated values

**Bulk/Heavy**: Furniture, appliances, exercise equipment
- Professional mover handling
- Disassembly instructions
- Hardware bags labeled
- Furniture pads required

### Box Labeling System

**Standard Format**:
```
BOX #[number]
ROOM: [destination room]
CONTENTS: [brief description]
PRIORITY: [high/medium/low]
FLAGS: [FRAGILE/ESSENTIAL/THIS SIDE UP]
```

**Color Coding Option**:
- Red: Fragile items
- Yellow: Open first / Essential
- Green: Can wait / Low priority
- Blue: Garage/Storage destination

### Packing Progress Calculation

```python
def calculate_packing_progress(rooms):
    """Calculate overall packing completion percentage"""

    total_items = sum(room['total_items'] for room in rooms.values())
    packed_items = sum(room['items_packed'] for room in rooms.values())

    if total_items == 0:
        return 0

    return (packed_items / total_items) * 100

def estimate_boxes_needed(room):
    """Estimate boxes needed based on room type and items"""

    # Average items per box by category
    items_per_box = {
        "books": 10,
        "clothes": 15,
        "kitchen": 12,
        "electronics": 2,
        "decor": 8,
        "general": 10
    }

    estimated_boxes = 0
    for item in room['items']:
        category = item.get('category', 'general')
        items_per_box_category = items_per_box.get(category, 10)
        estimated_boxes += item['quantity'] / items_per_box_category

    return max(1, round(estimated_boxes))
```

## Utility Transfer Coordination

### Utility Transfer Order of Operations

**3 Weeks Before Move**:
1. Research providers at new address
2. Compare rates and service options
3. Check for transfer vs new account requirements

**2 Weeks Before Move**:
1. Schedule connection at new address (schedule for day before or day of move)
2. Notify current providers of disconnect date (day after move)
3. Request final billing address

**Week of Move**:
1. Confirm all connection appointments
2. Verify disconnect dates
3. Ensure utilities active at new address before moving day

### Utility Priority Tiers

**Tier 1 - Must be active before move-in**:
- Electricity
- Water
- Heat (in cold climates)
- Gas (if needed for heat/cooking)

**Tier 2 - Should be active within 24 hours**:
- Internet/Cable
- Trash/Recycling service

**Tier 3 - Can be activated within first week**:
- Home phone (if separate)
- Lawn care
- Security system

### Utility Transfer Schema

```json
{
  "utility_id": "electric",
  "name": "Electric Service",
  "provider": "Local Electric Company",
  "account_number": "1234567890",
  "priority": "critical",
  "old_address": {
    "disconnect_date": "2025-12-16",
    "disconnect_scheduled": true,
    "final_reading": null,
    "final_bill_address": "new_address"
  },
  "new_address": {
    "connect_date": "2025-12-14",
    "connect_scheduled": true,
    "installation_appointment": "9am-12pm",
    "account_number": "9876543210",
    "deposit_required": false
  },
  "contact": {
    "phone": "1-800-555-0100",
    "website": "www.electriccompany.com",
    "customer_service_hours": "24/7"
  }
}
```

## Address Change Management

### Address Change Priority Matrix

**Priority 1 (Critical - Week 5)**: Must update before or immediately at move
- USPS Mail Forwarding (submit 2 weeks before)
- Employer/Payroll
- Bank (primary checking/savings)
- Credit cards (all)
- Health insurance
- Auto insurance
- Driver's license (within state timeframe)
- Vehicle registration

**Priority 2 (High - Week 6)**: Update within first week
- Doctors/Dentists/Medical providers
- Pharmacy
- Children's schools
- Investment accounts
- Loan servicers
- IRS/Tax authorities
- Voter registration

**Priority 3 (Medium - Week 7-8)**: Update within first month
- Subscriptions (Amazon, streaming, etc.)
- Loyalty programs
- Professional associations
- Alumni associations
- Magazine subscriptions
- Online retailers

**Priority 4 (Low - After move)**: Update as needed
- Social media profiles
- Non-critical newsletters
- Infrequent vendors

### Address Update Tracking Schema

```json
{
  "service_id": "bank_checking",
  "name": "Bank - Checking Account",
  "category": "financial",
  "priority": "critical",
  "update_deadline": "2025-12-10",
  "update_method": "online",
  "updated": true,
  "update_date": "2025-12-01T10:30:00Z",
  "confirmation_number": "BANK123456",
  "contact": {
    "phone": "1-800-555-BANK",
    "website": "www.bank.com/profile",
    "requires_verification": true
  },
  "notes": "Updated online, received email confirmation"
}
```

### USPS Mail Forwarding Best Practices

**Temporary Forwarding** (Recommended for moves):
- Duration: 6 months or 12 months
- Gives time to update all addresses
- Catches any missed notifications
- Covers unexpected mail

**Permanent Forwarding** (Optional):
- Use only if certain all critical addresses updated
- Can cause issues with some services
- May not forward all mail types

**Key Points**:
- Submit 2 weeks before move date
- Costs approximately $1 for identity verification
- Confirmation sent to both addresses
- Does not forward packages from all carriers
- Magazine subscriptions may take longer

## First-Week Essentials

### Essentials Box Contents

**Documents & Financial**:
- Passports and IDs
- Social Security cards
- Birth certificates
- Insurance documents
- Lease/mortgage papers
- Moving company contract
- Utility account numbers
- Bank information

**Personal Care**:
- Toiletries (toothbrush, soap, shampoo)
- Medications (1-week supply minimum)
- First aid kit
- Toilet paper (full pack)
- Hand soap
- Towels (2 per person)
- Bedding (sheets, pillows, blankets)

**Kitchen Essentials**:
- Paper plates and cups
- Plastic utensils
- Paper towels
- Trash bags
- Dish soap
- Basic snacks
- Coffee/tea supplies
- Can opener
- One pot, one pan

**Tools & Supplies**:
- Screwdriver set
- Hammer
- Utility knife/box cutter
- Scissors
- Flashlight
- Phone chargers (all devices)
- Power strip
- Duct tape
- Packing tape

**Cleaning Supplies**:
- All-purpose cleaner
- Disinfecting wipes
- Broom and dustpan
- Mop or cleaning cloths
- Vacuum (if available)
- Trash bags
- Rubber gloves

**Other Essentials**:
- Pet food and supplies (if applicable)
- Baby supplies (if applicable)
- Medications and prescriptions
- Snacks and easy meals for 2-3 days
- Laptop and important electronics
- Change of clothes (2-3 days per person)

## Mover Comparison Criteria

### Key Evaluation Factors

**Licensing & Insurance**:
- USDOT number (for interstate moves)
- State license (for local moves)
- Liability coverage details
- Worker's compensation insurance
- Cargo insurance options

**Services Offered**:
- Packing services (full/partial)
- Furniture disassembly/assembly
- Specialty item handling (piano, art, etc.)
- Storage options
- Vehicle transport

**Cost Factors**:
- Hourly rate vs flat fee
- Minimum hours
- Travel time charges
- Fuel surcharges
- Stairs/elevator fees
- Long carry charges
- Packing material costs

**Reputation**:
- BBB rating
- Online reviews (Google, Yelp)
- Complaint history
- Years in business
- Referrals from trusted sources

### Red Flags to Avoid

- No physical address or office
- Requires large deposit upfront
- Provides quote without in-home assessment
- No written estimate
- Unmarked truck or no company logo
- Cash-only payment
- Unable to provide license/insurance proof
- Significant price undercut vs competitors

### Mover Comparison Schema

```json
{
  "company_name": "Quality Movers Inc",
  "contact": {
    "phone": "555-0123",
    "email": "info@qualitymovers.com",
    "website": "www.qualitymovers.com"
  },
  "licensing": {
    "usdot_number": "123456",
    "state_license": "CA-T-123456",
    "insured": true,
    "insurance_amount": "$1,000,000"
  },
  "quote": {
    "type": "hourly",
    "rate": 150,
    "minimum_hours": 3,
    "estimated_total": 675,
    "includes": ["2 movers", "truck", "basic insurance"],
    "additional_fees": ["$50 stair fee per floor", "$25 long carry over 75ft"]
  },
  "services": {
    "packing": true,
    "unpacking": true,
    "furniture_assembly": true,
    "storage": false,
    "specialty_items": ["pianos", "artwork"]
  },
  "availability": {
    "preferred_date_available": true,
    "flexible_scheduling": true,
    "weekend_premium": 25
  },
  "reputation": {
    "bbb_rating": "A+",
    "google_rating": 4.7,
    "years_in_business": 15,
    "complaints": 0
  },
  "notes": "Highly recommended by neighbor, very responsive"
}
```

## Moving Day Logistics

### Pre-Move Day Checklist (Night Before)

- [ ] Confirm mover arrival time
- [ ] Pack final essentials box
- [ ] Empty and defrost refrigerator/freezer
- [ ] Disconnect washer and dryer
- [ ] Remove wall-mounted items
- [ ] Set aside items not going to movers
- [ ] Charge all devices
- [ ] Set aside keys, garage openers, manuals
- [ ] Reserve parking/loading zone if needed
- [ ] Prepare payment for movers
- [ ] Review mover inventory list
- [ ] Get good night's sleep

### Moving Day Morning

- [ ] Final walkthrough of every room, closet, cabinet
- [ ] Meet movers and review plan
- [ ] Provide movers with new address and directions
- [ ] Provide movers with contact phone number
- [ ] Stay available but out of the way
- [ ] Check items as loaded (verify inventory)
- [ ] Note any damage to items before loading
- [ ] Take photos of empty rooms
- [ ] Get copies of all paperwork
- [ ] Do not sign until satisfied

### New Home Arrival

- [ ] Inspect property before unloading
- [ ] Check for damage or issues
- [ ] Verify utilities are functioning
- [ ] Direct movers for furniture placement
- [ ] Check items as unloaded (verify inventory)
- [ ] Note any damage that occurred during move
- [ ] Tip movers if service was good (15-20% or $4-5 per person per hour)
- [ ] Locate essentials box immediately
- [ ] Make beds first
- [ ] Set up bathroom basics

### End of Day Priorities

- [ ] Set up beds
- [ ] Unpack toiletries
- [ ] Set up basic kitchen functionality
- [ ] Take out trash
- [ ] Locate and organize important documents
- [ ] Check door locks and security
- [ ] Program garage door opener
- [ ] Feed pets and set up pet area
- [ ] Order or prepare dinner
- [ ] Get keys from landlord/real estate agent
- [ ] Rest and celebrate completion

## Best Practices & Tips

### Packing Efficiency

**Room-by-Room Approach**:
- Complete one room before starting another
- Reduces confusion and maintains organization
- Makes unpacking easier
- Helps track progress

**Heavy Items First**:
- Pack books and heavy items in small boxes
- Prevents boxes from becoming too heavy
- Reduces risk of box bottom failure
- Easier for movers to handle

**Box Weight Rule**:
- Maximum 50 pounds per box
- If you can't lift it easily, it's too heavy
- Use larger boxes for lighter items (linens, pillows)
- Use smaller boxes for heavier items (books, dishes)

### Labeling Best Practices

- Label on top and at least two sides
- Include box number and total count
- Note destination room
- List fragile items specifically
- Create master inventory list
- Use color coding for priority
- Take photos of valuable box contents

### Common Mistakes to Avoid

**Procrastination**: Starting too late leads to stress and errors
**Over-packing boxes**: Makes them too heavy and prone to breaking
**Poor labeling**: Creates chaos during unpacking
**Forgetting essentials**: Leads to frustrating first days
**Not researching movers**: Can result in scams or poor service
**Skipping insurance**: Leaves you vulnerable to loss
**Ignoring utilities**: Arriving to no power or water
**Missing address updates**: Lost mail and service disruptions

### Money-Saving Tips

- Move mid-month or mid-week (cheaper rates)
- Source free boxes from stores and liquor stores
- Use clothing and linens as padding
- Declutter before packing (less to move)
- Compare multiple mover quotes
- DIY pack non-fragile items
- Use tax deductions if work-related move
- Negotiate utility installation fees
- Time utility connections carefully to avoid overlap charges

## Data Structure Standards

### Timeline Entry Schema

```json
{
  "week_number": 1,
  "start_date": "2025-11-01T00:00:00Z",
  "end_date": "2025-11-07T23:59:59Z",
  "phase": "Planning & Research",
  "tasks": [
    {
      "id": "create_budget",
      "name": "Create moving budget",
      "priority": "high",
      "completed": false,
      "completed_date": null,
      "notes": ""
    }
  ],
  "total_tasks": 5,
  "completed_tasks": 0,
  "completion_percentage": 0
}
```

### Milestone Schema

```json
{
  "id": "planning_complete",
  "name": "Planning & Research Complete",
  "week": 2,
  "description": "Mover selected, budget finalized, major decisions made",
  "completed": false,
  "completed_date": null,
  "criteria": [
    "Moving company booked",
    "Budget approved",
    "Timeline confirmed",
    "Inventory started"
  ]
}
```

## Validation Rules

### Timeline Validation

- Moving date must be in future
- Timeline must span exactly 8 weeks
- Each week must have at least one task
- Critical tasks must have completion tracking
- Milestones must align with appropriate weeks

### Inventory Validation

- Each item must have a name
- Quantities must be positive integers
- Box numbers must be unique
- Fragile items must be flagged
- High-value items should have estimated value

### Address Update Validation

- Current and new addresses must be complete
- Move dates must be logical (move-in after move-out)
- Utility disconnect date should be after move
- Utility connect date should be before or on move day
- Critical services must be updated before move

## Error Handling Patterns

### Common Error Scenarios

**Timeline conflicts**:
```python
if disconnect_date <= move_date:
    raise ValidationError("Utilities should disconnect AFTER move-out date")
```

**Incomplete address**:
```python
required_fields = ['street', 'city', 'state', 'zip']
if not all(address.get(field) for field in required_fields):
    raise ValidationError("Complete address required")
```

**Overweight boxes**:
```python
if estimated_weight > 50:
    print("⚠️  Warning: Box may be too heavy")
    print("   Consider splitting into multiple boxes")
```

## Success Metrics

Track these metrics for successful move:

- Timeline adherence (% of tasks completed on time)
- Packing efficiency (actual boxes vs estimated)
- Address update completion (% updated before move)
- Utility activation success (all working on move-in day)
- Damage rate (% of items damaged during move)
- Budget variance (actual vs planned costs)
- Stress level (subjective, but important)

---

**This skill is read by all moving-coordinator agents to ensure consistent practices and successful relocations.**
