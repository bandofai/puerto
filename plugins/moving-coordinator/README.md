# Moving Coordinator Plugin

A comprehensive moving logistics and timeline coordination system for Claude Code that helps you manage every aspect of your relocation with confidence and organization.

## Overview

The Moving Coordinator plugin provides specialized agents, skills, and templates for managing an 8-week moving timeline, tracking room-by-room inventory, coordinating utility transfers, and ensuring no detail is overlooked during your move.

## What's Included

### Agents

#### 1. moving-timeline-coordinator (Haiku)
Manages your 8-week moving timeline with milestone tracking and task scheduling.

**Key Features:**
- 8-week structured timeline from planning to move-in
- Week-by-week task organization with priorities
- Milestone tracking (planning, packing, moving, settling)
- Progress monitoring and deadline management
- Customizable task lists for your specific move
- Weekly progress reports

**Activation**: Automatically activates for timeline operations, or use `@moving-timeline-coordinator`.

#### 2. inventory-tracker (Haiku)
Tracks room-by-room inventory and packing progress with detailed organization.

**Key Features:**
- Room-by-room item inventory
- Box creation and labeling system
- Packing progress tracking by room and overall
- Fragile, valuable, and essential item flagging
- Printable box labels generation
- Unpacking priority guide

**Activation**: Automatically activates for inventory operations, or use `@inventory-tracker`.

#### 3. address-updater (Haiku)
Manages utility transfers, address changes, and subscription updates with priority tracking.

**Key Features:**
- Utility transfer coordination (electric, gas, water, internet)
- Address change tracking for all services
- Priority-based categorization (critical, high, medium, low)
- Deadline monitoring and reminder system
- Confirmation tracking with numbers
- Comprehensive service contact management

**Activation**: Automatically activates for address updates, or use `@address-updater`.

### Skills

#### moving-coordination
Comprehensive moving best practices and patterns including:
- 8-week timeline structure and phase definitions
- Task prioritization system with dependencies
- Inventory management patterns and schemas
- Utility transfer coordination order of operations
- Address change priority matrix
- First-week essentials checklist
- Mover comparison criteria
- Moving day logistics and checklists

All agents read this skill for consistent practices and successful relocations.

### Templates

#### 1. moving-timeline.json
8-week timeline with pre-populated tasks for each week.

**Contains:**
- Week-by-week task breakdown
- 5 major milestones with completion criteria
- Task priorities (critical, high, medium, low)
- Phase definitions (Planning, Preparation, Active Packing, Final Execution)
- Customizable task notes and deadlines

#### 2. room-inventory.json
Room-by-room packing checklist with item categorization.

**Contains:**
- 6 standard rooms (living room, kitchen, bedrooms, bathroom, garage, office)
- Item categorization (fragile, valuable, essential)
- Box tracking and labeling system
- Packing supplies recommendations
- Category tracking (donate, sell, discard)
- Estimated box counts by room

#### 3. address-change-checklist.json
Comprehensive service and utility tracking template.

**Contains:**
- 5 critical utilities (electric, gas, water, internet, trash)
- Government services (USPS, DMV, voter registration, IRS)
- Financial institutions (banks, credit cards, insurance, investments)
- Personal services (employer, doctors, pharmacy, schools)
- Subscriptions (Amazon, streaming, magazines, gym)
- Priority scheduling by week

## Installation

```bash
/plugin install moving-coordinator@puerto
```

**Prerequisites:**
- Claude Code CLI
- Read and Write tools access

After installation, restart Claude Code to activate all agents and skills.

## Quick Start

### Initial Setup

```bash
# Initialize moving coordinator
@moving-timeline-coordinator "Initialize moving coordinator for my upcoming move"

# Set your moving date (generates 8-week timeline)
@moving-timeline-coordinator "Set moving date to December 15, 2025"

# Set addresses
@address-updater "Set current address to 123 Old St, Old City, CA 90001 and new address to 456 New Ave, New City, CA 90002"
```

### Timeline Management

```bash
# View current timeline
@moving-timeline-coordinator "Show my moving timeline"

# Complete a task
@moving-timeline-coordinator "Mark task 'Create moving budget' as completed"

# Get weekly report
@moving-timeline-coordinator "Generate report for current week"

# Check milestone progress
@moving-timeline-coordinator "Show milestone status"
```

### Inventory Tracking

```bash
# Initialize inventory
@inventory-tracker "Initialize inventory system"

# Add a room with items
@inventory-tracker "Add living room with sofa, TV, bookshelf, and coffee table"

# Create and pack a box
@inventory-tracker "Create box #1 for living room with TV, remote, and HDMI cables"

# Check packing progress
@inventory-tracker "Generate packing progress report"

# Generate box labels
@inventory-tracker "Generate printable box labels"
```

### Address Updates

```bash
# Add utilities
@address-updater "Add common utilities to track"

# Schedule utility transfer
@address-updater "Schedule electric disconnect for December 16 and connect for December 14"

# Add services to update
@address-updater "Add critical services for address updates"

# Update service address
@address-updater "Mark USPS mail forwarding as completed"

# Get status report
@address-updater "Generate address change status report"
```

## Data Structure

All moving data is stored in `~/.moving-coordinator/` or `.moving-coordinator/` (project-specific).

### Directory Layout

```
.moving-coordinator/
├── timeline.json              # 8-week timeline and milestones
├── inventory.json             # Room-by-room inventory and boxes
├── address-changes.json       # Utility transfers and service updates
├── timelines/                 # Timeline history and versions
├── checklists/               # Generated checklists and reports
└── documents/                # Box labels, guides, and exports
```

### Core Data Models

#### Timeline Entry

```json
{
  "week_number": 1,
  "start_date": "2025-10-20T00:00:00Z",
  "end_date": "2025-10-26T23:59:59Z",
  "phase": "Planning & Research",
  "tasks": [
    {
      "id": "budget",
      "task": "Create moving budget",
      "priority": "high",
      "completed": false,
      "notes": "Include all costs: movers, supplies, deposits"
    }
  ],
  "completed_tasks": 0,
  "total_tasks": 5
}
```

#### Inventory Item

```json
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
```

#### Utility Entry

```json
{
  "name": "Electric Service",
  "provider": "Local Electric Company",
  "priority": "critical",
  "old_address": {
    "disconnect_scheduled": true,
    "disconnect_date": "2025-12-16",
    "disconnect_confirmed": false
  },
  "new_address": {
    "connect_scheduled": true,
    "connect_date": "2025-12-14",
    "service_active": false
  }
}
```

## Workflows

### Complete Moving Workflow

#### Weeks 1-2: Planning & Research

```bash
# Week 1: Initial planning
@moving-timeline-coordinator "Show week 1 tasks"
@moving-timeline-coordinator "Complete budget creation task"
@moving-timeline-coordinator "Complete mover research task"

# Week 2: Book movers and order supplies
@moving-timeline-coordinator "Complete mover booking task"
@moving-timeline-coordinator "Complete packing supplies order"
@moving-timeline-coordinator "Check if planning milestone is achieved"
```

#### Weeks 3-4: Preparation & Early Packing

```bash
# Week 3: Declutter and organize
@inventory-tracker "Add all rooms to inventory"
@inventory-tracker "Mark items as donate/sell/discard"
@moving-timeline-coordinator "Complete decluttering task"

# Week 4: Start packing and schedule utilities
@inventory-tracker "Create boxes for garage items"
@address-updater "Research utility providers at new address"
@address-updater "Schedule utility transfers"
@moving-timeline-coordinator "Complete early packing tasks"
```

#### Weeks 5-6: Active Packing & Coordination

```bash
# Week 5: Critical address updates
@address-updater "Submit USPS mail forwarding"
@address-updater "Update banks and credit cards"
@address-updater "Update insurance providers"
@inventory-tracker "Pack non-essential rooms"
@moving-timeline-coordinator "Check utilities milestone"

# Week 6: Final room packing
@inventory-tracker "Pack kitchen and bathrooms"
@inventory-tracker "Pack electronics with cable management"
@moving-timeline-coordinator "Confirm mover details"
```

#### Weeks 7-8: Final Preparation & Moving

```bash
# Week 7: Final packing and preparation
@inventory-tracker "Pack essentials box"
@inventory-tracker "Complete final inventory"
@inventory-tracker "Generate box labels"
@moving-timeline-coordinator "Complete final tasks"

# Week 8: Moving day
@moving-timeline-coordinator "Execute moving day checklist"
@address-updater "Verify all utilities are active"
@inventory-tracker "Generate unpacking priority guide"
@moving-timeline-coordinator "Mark move complete milestone"
```

### Daily Usage Patterns

**Planning Phase (Weeks 1-2)**:
```bash
# Morning: Check today's priorities
@moving-timeline-coordinator "Show current week tasks by priority"

# Complete tasks throughout the day
@moving-timeline-coordinator "Complete task [task-id]"

# Evening: Review progress
@moving-timeline-coordinator "Generate weekly report"
```

**Packing Phase (Weeks 3-6)**:
```bash
# Start packing session
@inventory-tracker "Show rooms with items remaining"

# Pack items into boxes
@inventory-tracker "Create box #[number] for [room] with [items]"

# Track progress
@inventory-tracker "Show packing progress"
```

**Coordination Phase (Weeks 4-6)**:
```bash
# Schedule transfers
@address-updater "Schedule [utility] disconnect and connect"

# Update addresses
@address-updater "Update [service] address"

# Check completion
@address-updater "Show critical pending items"
```

## Best Practices

### Timeline Management

**Start Early**: Begin planning 8 weeks before your move date for best results.

**Daily Check-ins**: Review your timeline daily and complete at least 1-2 tasks.

**Flexibility**: Adjust tasks and deadlines based on your specific circumstances.

**Milestone Focus**: Use milestones as motivation checkpoints.

**Priority First**: Always tackle critical and high-priority tasks before medium or low.

### Inventory Organization

**Room-by-Room**: Complete one room before starting another to maintain organization.

**Box Weight**: Keep boxes under 50 pounds. Use small boxes for heavy items (books), large boxes for light items (linens).

**Clear Labeling**: Label boxes on top and at least two sides with room, contents, and any special handling instructions.

**Essentials Box**: Pack a clearly marked essentials box with everything needed for the first 24-48 hours.

**Photo Documentation**: Take photos of valuable items and electronics before packing.

**Master List**: Keep a master inventory list of all boxes and high-value items.

### Address Updates

**Timing is Critical**:
- Week 4: Schedule all utilities
- Week 5: Submit USPS forwarding and update critical services
- Week 6: Update remaining financial and government services
- Week 7-8: Update subscriptions and non-critical services

**Confirmation Numbers**: Always get and record confirmation numbers for utilities and important updates.

**Utility Order**: Schedule new address connections BEFORE disconnections at old address to ensure no service gaps.

**Critical First**: Focus on utilities, USPS, banks, insurance, and employer first.

### Moving Day Tips

**Morning Preparation**:
- Final walkthrough of every space
- Essential items (documents, medications, valuables) in car
- Chargers, snacks, and water easily accessible
- Contact numbers for movers, landlord, real estate agent

**During Move**:
- Stay available but out of the way
- Check items against inventory as loaded
- Note any pre-existing damage
- Take photos of empty rooms

**At New Home**:
- Inspect before unloading
- Verify utilities functioning
- Direct furniture placement
- Check items as unloaded
- Set up beds and bathroom first

## Mover Selection Guide

### Get Multiple Quotes

Get at least 3 written estimates from licensed, insured movers.

### Verify Credentials

**For Interstate Moves**:
- USDOT number
- Federal Motor Carrier Safety Administration registration
- Proper insurance coverage

**For Local Moves**:
- State license
- Local business license
- Liability and worker's compensation insurance

### Red Flags to Avoid

- No physical address or office location
- Requires large deposit upfront (>25%)
- Quote without in-home assessment
- No written estimate or contract
- Unmarked truck or no company logo
- Cash-only payment
- Significant undercut vs other quotes

### Comparison Criteria

**Cost Structure**:
- Hourly rate vs flat fee
- Minimum hours requirement
- Additional fees (stairs, long carry, fuel)
- Packing service costs

**Services**:
- Packing/unpacking offered
- Furniture disassembly/assembly
- Specialty item handling
- Storage availability

**Reputation**:
- BBB rating and complaint history
- Online reviews (Google, Yelp, Angie's List)
- Years in business
- Referrals from trusted sources

## First-Week Essentials Checklist

### Documents & Financial
- [ ] Passports and IDs
- [ ] Birth certificates and Social Security cards
- [ ] Insurance documents
- [ ] Lease/mortgage papers
- [ ] Moving contract and inventory list
- [ ] Checkbook and credit cards

### Personal Care
- [ ] Toiletries (toothbrush, soap, shampoo, etc.)
- [ ] Medications (1-week supply minimum)
- [ ] First aid kit
- [ ] Toilet paper (full pack)
- [ ] Hand soap
- [ ] Towels (2 per person)
- [ ] Bedding (sheets, pillows, blankets)

### Kitchen Essentials
- [ ] Paper plates, cups, and plastic utensils
- [ ] Paper towels
- [ ] Trash bags
- [ ] Dish soap
- [ ] Basic snacks and drinks
- [ ] Coffee/tea supplies
- [ ] Can opener
- [ ] One pot and one pan

### Tools & Supplies
- [ ] Screwdriver set
- [ ] Hammer
- [ ] Utility knife/box cutter
- [ ] Scissors
- [ ] Flashlight
- [ ] Phone chargers (all devices)
- [ ] Power strip
- [ ] Duct tape and packing tape

### Cleaning Supplies
- [ ] All-purpose cleaner
- [ ] Disinfecting wipes
- [ ] Broom and dustpan
- [ ] Mop or cleaning cloths
- [ ] Vacuum (if available)
- [ ] Trash bags
- [ ] Rubber gloves

### Other
- [ ] Pet food and supplies
- [ ] Baby supplies (if applicable)
- [ ] Change of clothes (2-3 days per person)
- [ ] Laptop and electronics
- [ ] Snacks and easy meals

## Utility Transfer Checklist

### 3 Weeks Before Move
- [ ] Research providers at new address
- [ ] Compare rates and service options
- [ ] Check for new vs transfer account requirements

### 2 Weeks Before Move
- [ ] Schedule connection at new address (1-2 days before move-in)
- [ ] Schedule disconnection at old address (1 day after move-out)
- [ ] Provide forwarding address for final bills

### Week of Move
- [ ] Confirm all connection appointments
- [ ] Verify disconnect dates
- [ ] Test utilities at new address if possible

### Moving Day
- [ ] Take final meter readings at old address
- [ ] Verify utilities active at new address
- [ ] Report any issues immediately

## Troubleshooting

### Timeline Not Loading
**Issue**: Timeline data not appearing or corrupted

**Solution**:
```bash
@moving-timeline-coordinator "Reinitialize timeline system"
# Set moving date again if needed
```

### Inventory Discrepancies
**Issue**: Box count or item count doesn't match

**Solution**:
- Review each room's packing status
- Regenerate packing report
- Verify box numbers are unique
- Check for duplicate entries

### Address Update Not Confirmed
**Issue**: Service shows updated but no confirmation received

**Solution**:
- Contact service provider directly
- Request confirmation via email
- Document date and method of update
- Set reminder to verify in 1 week

### Utility Not Active on Move-in
**Issue**: Arriving to no power, water, or internet

**Solution**:
- Call provider immediately from confirmation email/number
- Have account number and address ready
- Request emergency connection
- Document issue for potential moving insurance claim

## Tips for Reducing Moving Stress

### Financial
- Move mid-month or mid-week for better rates
- Source free boxes from stores
- Use clothing and linens as padding
- Declutter to reduce items moved
- Compare multiple mover quotes
- DIY pack non-fragile items

### Organizational
- Start early (8 weeks recommended)
- Use color-coded labels by room
- Keep master inventory list
- Pack room-by-room completely
- Label boxes clearly on multiple sides
- Create essentials box

### Practical
- Arrange childcare/pet care for moving day
- Eat easy meals during packing week
- Get good sleep night before move
- Stay hydrated on moving day
- Tip movers for good service (15-20%)
- Celebrate completion

## Integration with Other Plugins

**Compatible with**:
- Document organizers for important papers
- Calendar systems for deadline tracking
- Budget trackers for moving expenses
- Task managers for additional to-dos

## Privacy & Data

- **Local Storage**: All data stored locally in `~/.moving-coordinator/`
- **No Cloud Sync**: Data remains on your machine
- **Backup Recommended**: Copy `.moving-coordinator/` folder to backup
- **Sensitive Info**: Store account numbers and personal data securely

## Support & Feedback

This plugin is part of the Puerto marketplace. For issues, questions, or suggestions:
- Check documentation in `skills/moving-coordination/SKILL.md`
- Review templates for examples
- Ask agents for help with specific tasks

## License

MIT License - See main Puerto repository for details

---

**Move with confidence. Every detail tracked, every deadline managed, every item accounted for.**
