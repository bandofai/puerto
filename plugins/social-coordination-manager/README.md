# Social Coordination Manager Plugin

Relationship maintenance and social event coordination specialist with comprehensive birthday tracking, gift ideas, event planning, and relationship maintenance reminders.

## Overview

This plugin provides a specialized agent and comprehensive skill for managing your social connections, tracking important dates, planning memorable celebrations, and maintaining meaningful relationships.

## What's Included

### Agent: social-coordinator

A specialized agent that:
- **Tracks birthdays and anniversaries** with multi-level reminder system
- **Generates personalized gift ideas** based on interests, budgets, and preferences
- **Plans events** from intimate gatherings to large celebrations with detailed timelines
- **Maintains relationships** with scheduled check-ins and interaction logging
- **Manages contact database** with preferences, history, and notes
- **Creates budget tracking** for social spending and gift purchases
- **Provides message templates** for various occasions and situations

**Activation**: Use `@social-coordinator` or mention relationship management, birthday tracking, gift planning, or event coordination.

### Skill: social-coordination

Comprehensive guide covering:
- **Birthday & anniversary tracking** with reminder schedules
- **Gift ideation framework** across all categories and budgets
- **Event planning timelines** for events of all sizes
- **Relationship maintenance** strategies and frequency guidelines
- **Contact database management** with structured formats
- **Message templates** for all occasions
- **Budget management** and cost-saving strategies
- **Integration opportunities** with calendars and reminder systems

### Templates

Structured JSON and Markdown templates for:
- **birthday-tracker.json** - Contact database with birthdays, interests, gift history
- **gift-ideas.json** - Gift brainstorming and tracking format
- **event-plan.md** - Comprehensive event planning checklist
- **contact-log.json** - Relationship interaction history
- **reminder-schedule.json** - Automated reminder system

## Features

### Birthday & Anniversary Tracking

Never miss an important date again:
- Comprehensive contact database with relationships, interests, and preferences
- Multi-stage reminder system (60, 30, 14, 7, 3, 0 days before)
- Gift history tracking to avoid duplicates
- Milestone recognition (18th, 21st, 30th, etc.)
- Integration with calendar systems

### Personalized Gift Ideas

Stop stressing about gift shopping:
- 7-10 diverse suggestions per recipient
- Based on interests, hobbies, and past preferences
- Multiple categories: experiential, practical, personal, hobby-related, luxury
- Price ranges and purchase locations
- Personalization options for each gift
- Budget tracking and spending analysis

### Event Planning

Organize memorable celebrations with ease:
- Detailed timelines for small to large events
- Budget breakdown and tracking
- Guest list management with RSVP tracking
- Vendor coordination and contact management
- Day-of schedules and setup plans
- Menu planning with dietary accommodations
- Shopping lists organized by category

### Relationship Maintenance

Keep meaningful connections strong:
- Scheduled check-ins based on relationship tier
- Interaction logging with notes and next steps
- Outreach suggestions (messages, calls, meetups)
- Relationship quality tracking
- Action items and follow-ups
- Message templates for various situations

## Installation

```bash
/plugin install social-coordination-manager@puerto
```

After installation, restart Claude Code to activate the agent and skill.

## Usage

### Tracking a Birthday

```
@social-coordinator Track my friend Sarah's birthday on March 15th. She loves photography and hiking, prefers experiential gifts, and is vegetarian.
```

The agent will:
1. Create or update contact database entry
2. Add comprehensive profile with interests
3. Calculate reminder schedule
4. Set up automated notifications
5. Provide summary of upcoming reminders

### Getting Gift Ideas

```
@social-coordinator I need gift ideas for my brother's 30th birthday. Budget $50-100. He's into gaming and craft beer.
```

The agent will:
1. Analyze recipient profile and preferences
2. Consider milestone significance (30th birthday)
3. Generate 7-10 personalized gift suggestions
4. Include purchase locations and timing
5. Provide personalization options for each
6. Track selections and budget

### Planning an Event

```
@social-coordinator Help me plan a 40th birthday party for my wife in 3 months. About 30 guests, budget $1000.
```

The agent will:
1. Create comprehensive event planning document
2. Generate timeline with milestones (3 months → event day)
3. Provide budget breakdown by category
4. Create guest list template with RSVP tracking
5. Suggest vendors and venues
6. Set milestone reminders
7. Generate day-of schedule

### Maintaining Relationships

```
@social-coordinator Show me which friends I should reach out to this month.
```

The agent will:
1. Review contact database and interaction logs
2. Identify relationships due for check-in
3. Suggest specific outreach actions
4. Provide message templates
5. Schedule follow-up reminders

## File Structure

```
social-coordination-manager/
├── .claude-plugin/
│   └── plugin.json                    # Plugin metadata
├── agents/
│   └── social-coordinator.md          # Main agent
├── skills/
│   └── social-coordination/
│       └── SKILL.md                   # Comprehensive guide
├── templates/
│   ├── birthday-tracker.json          # Contact database template
│   ├── gift-ideas.json                # Gift planning template
│   ├── event-plan.md                  # Event checklist template
│   ├── contact-log.json               # Interaction history template
│   └── reminder-schedule.json         # Reminder system template
├── data/                              # User data storage (created when used)
└── README.md                          # This file
```

## Data Management

### Contact Database

Stores comprehensive information:
- Personal details (name, birthday, anniversary)
- Relationship type and tier (close, regular, occasional)
- Interests, hobbies, and preferences
- Gift style and celebration preferences
- Dietary restrictions and allergies
- Gift history with reactions
- Last contact date and frequency
- Personal notes and social media handles

### Event Plans

Comprehensive planning documents:
- Event details (date, location, budget, guest count)
- Timeline with milestone deadlines
- Budget breakdown by category
- Guest list with RSVP tracking
- Menu planning with dietary needs
- Vendor contacts and coordination
- Setup plans and decoration details
- Shopping lists

### Gift Tracking

Organized gift management:
- Gift ideas by recipient
- Category classification
- Price ranges and purchase locations
- Personalization options
- Selection tracking and purchase records
- Budget monitoring

## Best Practices

From the skill library, the agent follows these principles:

1. **Advance Planning**: Reminders set 30-60 days before events
2. **Personalization**: Every suggestion reflects individual preferences
3. **Budget Awareness**: Realistic financial planning and tracking
4. **Cultural Sensitivity**: Respects diverse celebration traditions
5. **Privacy Protection**: Secure handling of personal information
6. **Quality Focus**: Meaningful interactions over quantity
7. **Timeline Management**: Break tasks into manageable steps
8. **Relationship Investment**: Regular maintenance strengthens bonds

## Example Workflows

### Complete Birthday Management

1. **Add Contact** (60+ days before):
   ```
   @social-coordinator Add my friend Alex with birthday April 10. Interests: board games, cooking, dogs. Budget: $75.
   ```

2. **Get Gift Ideas** (30 days before):
   ```
   @social-coordinator Generate gift ideas for Alex's birthday.
   ```

3. **Plan Celebration** (as needed):
   ```
   @social-coordinator Plan a small birthday dinner for Alex with 8 friends.
   ```

4. **Track Interaction** (after event):
   ```
   @social-coordinator Log that I celebrated Alex's birthday yesterday. Everyone loved the dinner party.
   ```

### Event Series Management

For recurring annual events:
```
@social-coordinator Set up my annual Friendsgiving event for November 23. 12 guests, potluck style, budget $300.
```

Agent creates:
- Complete planning timeline starting 8 weeks before
- Guest list and dish assignment tracking
- Shopping and preparation schedule
- Reminder system for future years

### Relationship Maintenance System

```
@social-coordinator Create a relationship maintenance plan for my 20 closest friends and family.
```

Agent will:
- Review all contacts and last interaction dates
- Set appropriate check-in frequencies
- Generate monthly outreach schedules
- Provide message templates
- Create tracking system

## Integration Opportunities

The agent suggests integration with:

**Calendar Systems**:
- Google Calendar
- Apple Calendar
- Outlook Calendar

**Reminder Apps**:
- iOS Reminders
- Todoist
- Any.do

**Shopping Platforms**:
- Amazon Wish Lists
- Etsy Favorites
- Gift Registry Services

**Budget Tracking**:
- Mint
- YNAB
- Personal spreadsheets

## Advanced Features

### Multi-Contact Management

Track extended networks:
- Family members with different celebration styles
- Friend groups with varied interests
- Professional contacts with formal needs
- Acquaintances with minimal but thoughtful touch points

### Gift Budget Allocation

Annual planning:
- Per-person gift budgets
- Occasion-based allocations (holidays, birthdays)
- Category spending limits
- Year-over-year comparisons

### Event Templates

Reusable planning frameworks:
- Birthday party structures
- Holiday gatherings
- Anniversary celebrations
- Thank you events
- Seasonal traditions

### Reminder Customization

Flexible scheduling:
- Adjust reminder days for different occasions
- Set relationship-specific check-in frequencies
- Custom milestone alerts
- Event countdown notifications

## Benefits

### Never Forget Important Dates
- Automated reminder system
- Multiple alert stages
- Buffer time for preparation
- Milestone recognition

### Give Meaningful Gifts
- Personalized suggestions
- Budget-appropriate options
- Interest-based recommendations
- Gift history prevents duplicates

### Host Stress-Free Events
- Comprehensive planning timelines
- Nothing falls through cracks
- Budget stays on track
- Day-of confidence

### Maintain Strong Relationships
- Regular check-in prompts
- Interaction history tracking
- Quality conversation starters
- Thoughtful follow-ups

## Privacy & Security

- All personal data stored locally in your project
- No external sharing or syncing
- Sensitive information handled with care
- You control all contact details and notes

## Troubleshooting

### Agent Not Activating
- Try explicit mention: `@social-coordinator`
- Use trigger phrases: "birthday tracking", "gift ideas", "event planning"

### Data Files Not Found
- Agent creates templates automatically from examples
- Check `data/social-coordination/` directory
- Templates available in `templates/` directory

### Reminder System
- Set up calendar integration for automated alerts
- Export reminder JSON to your preferred tool
- Manual review of upcoming dates in database

## Support & Feedback

This plugin brings comprehensive social coordination to Claude Code. For issues or suggestions:

- Review the [skill library](skills/social-coordination/SKILL.md) for complete guidelines
- Check the [agent](agents/social-coordinator.md) for detailed capabilities
- Examine [templates](templates/) for data structure examples

## License

MIT License - See main repository for details

---

**Never miss another birthday. Never stress about gifts. Always stay connected with the people who matter most.**
