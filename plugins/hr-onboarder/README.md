# HR Onboarding Specialist Plugin

**Professional new employee onboarding automation for exceptional first impressions and long-term retention**

This plugin provides a comprehensive onboarding system with battle-tested templates, checklists, and frameworks for creating outstanding new hire experiences from pre-arrival through the first 90 days.

## Overview

The HR Onboarding Specialist plugin automates the creation of professional onboarding materials that drive employee engagement, productivity, and retention. Built on best practices from 1000+ successful onboarding experiences, it ensures every new hire receives a structured, welcoming, and effective onboarding journey.

**Research shows**: Employees with great onboarding are 69% more likely to stay for 3+ years and reach full productivity 50% faster.

## Components

### Agent: `hr-onboarder`

A professional HR onboarding specialist that creates comprehensive onboarding plans, checklists, welcome materials, IT provisioning lists, training schedules, and follow-up templates.

- **File**: `agents/hr-onboarder.md`
- **Model**: Sonnet (requires judgment for personalization and context)
- **Tools**: Read, Write, Edit, Bash, Glob, Grep
- **Skill-aware**: Always reads onboarding skill before starting tasks

### Skill: Onboarding Best Practices

Comprehensive library of onboarding frameworks, templates, and best practices.

- **File**: `skills/onboarding/SKILL.md`
- **Contains**:
  - Timeline frameworks (Pre-arrival, Day 1, Week 1, 30/60/90 days)
  - Role-specific onboarding plans (Engineering, Sales, Marketing, CS)
  - IT provisioning standards and checklists
  - Welcome email templates for all stages
  - Training schedule frameworks
  - Check-in and follow-up templates
  - Remote onboarding adaptations
  - Quality standards and metrics

## Features

### Core Capabilities

1. **Onboarding Checklists**
   - Pre-arrival preparation
   - Day-one hour-by-hour schedules
   - Week-one daily priorities
   - 30/60/90-day milestones
   - Role-specific customization

2. **Welcome Materials**
   - Professional welcome emails
   - Welcome packets and swag lists
   - Company culture materials
   - Team introductions
   - Office/workspace guides

3. **IT Setup Coordination**
   - Hardware requirements by role
   - Software and application lists
   - Account provisioning timelines
   - Security requirements
   - Setup and testing instructions

4. **Training Schedules**
   - Structured learning paths
   - Week-by-week training calendars
   - Role-specific skill development
   - Self-paced learning resources
   - Certification tracking

5. **Follow-up Management**
   - 30/60/90-day check-in templates
   - Manager observation guides
   - Performance review frameworks
   - Feedback collection forms
   - Onboarding buddy protocols

### Role-Specific Support

Pre-configured onboarding paths for:
- **Engineering**: Development environment, codebase, first commit goals
- **Sales**: CRM training, product certification, pipeline building
- **Marketing**: Brand guidelines, campaign processes, analytics platforms
- **Customer Success**: Product training, support systems, escalation procedures

### Remote Onboarding

Specialized adaptations for distributed teams:
- Technology setup and testing
- Virtual connection building
- Enhanced documentation
- Async learning options
- Home office support

## Installation

### Option 1: Manual Installation (Project-Level)

```bash
# From your project root
cp -r plugins/hr-onboarder .claude/plugins/

# Verify installation
ls .claude/plugins/hr-onboarder/
```

### Option 2: User-Level Installation

```bash
# Install for all your projects
cp -r plugins/hr-onboarder ~/.claude/plugins/

# Verify installation
ls ~/.claude/plugins/hr-onboarder/
```

### Verify Installation

The agent will be automatically available in Claude Code. Verify by checking:

```bash
# List installed agents
ls .claude/plugins/hr-onboarder/agents/
# Should show: hr-onboarder.md

# List installed skills
ls .claude/plugins/hr-onboarder/skills/
# Should show: onboarding/
```

## Usage

### Automatic Activation

The agent activates automatically when you:
- Mention "onboard new employee"
- Ask to create onboarding plans or checklists
- Request welcome materials or training schedules
- Need IT provisioning lists
- Want 30/60/90-day plans

### Manual Invocation

You can explicitly invoke the agent:

```
@hr-onboarder create an onboarding plan for [new hire details]
```

### Example Requests

#### Complete Onboarding Package

```
"Create a complete onboarding plan for Alex Rodriguez, Senior Product Manager,
starting April 1st, 2025. Manager is Sarah Kim."
```

**Generates**:
- Welcome email
- Day-one schedule
- Week-one checklist
- 30/60/90-day plan
- Training calendar
- IT provisioning checklist
- Check-in templates

#### IT Provisioning Focus

```
"What IT setup does a new Senior Software Engineer need?"
```

**Generates**:
- Hardware checklist (laptop, monitors, peripherals)
- Engineering software (IDEs, dev tools, cloud access)
- Account creation timeline
- Security requirements
- Setup instructions

#### Welcome Materials

```
"Create welcome materials for a new Marketing Coordinator"
```

**Generates**:
- Welcome email
- First-day schedule
- Team introduction
- Marketing-specific resources
- Culture overview

#### Check-in Templates

```
"Create a 60-day check-in template for sales reps"
```

**Generates**:
- Self-reflection questions
- Manager discussion guide
- Performance assessment
- Goal setting framework

#### Remote Onboarding

```
"Create an onboarding plan for a remote Senior Designer starting next month"
```

**Generates**:
- Virtual onboarding schedule
- Technology setup guide
- Connection-building activities
- Enhanced documentation
- Home office recommendations

## Best Practices

### For HR Teams

1. **Customize for Your Company**
   - Review generated materials and add company-specific details
   - Update brand voice and terminology
   - Include your actual policies and benefits
   - Add your team members' names and contacts

2. **Prepare Early**
   - Generate onboarding materials 2 weeks before start date
   - Give IT team adequate lead time for provisioning
   - Brief managers and buddies in advance
   - Prepare workspace ahead of time

3. **Personalize the Experience**
   - Use the new hire's name throughout
   - Reference their background and experience
   - Tailor training to their skill level
   - Consider individual learning preferences

4. **Measure and Improve**
   - Collect feedback at 30/60/90 days
   - Track completion rates
   - Monitor retention metrics
   - Iterate on the process

### For Managers

1. **Own the Experience**
   - Review and customize the 30/60/90-day plan
   - Block time for onboarding activities
   - Personally send welcome message
   - Be present on day one

2. **Set Clear Expectations**
   - Define success criteria
   - Provide context for goals
   - Explain team dynamics
   - Share unwritten rules

3. **Check In Frequently**
   - Daily touchpoints first week
   - Weekly 1:1s first month
   - Formal reviews at 30/60/90 days
   - Create psychological safety

4. **Gather Feedback**
   - Ask how onboarding is going
   - Identify gaps or confusion
   - Adjust approach as needed
   - Improve for next new hire

### For New Hires

1. **Come Prepared**
   - Review materials sent before start
   - Prepare questions
   - Bring required documents
   - Set up accounts in advance if possible

2. **Engage Actively**
   - Ask questions freely
   - Take initiative in meetings
   - Build relationships proactively
   - Seek feedback regularly

3. **Use Your Resources**
   - Lean on your onboarding buddy
   - Reference documentation provided
   - Attend all scheduled training
   - Take notes and organize information

## File Structure

```
plugins/hr-onboarder/
├── README.md                                    # This file
├── plugin.json                                  # Plugin metadata
├── agents/
│   └── hr-onboarder.md                         # Main onboarding agent
└── skills/
    └── onboarding/
        └── SKILL.md                            # Onboarding best practices library
```

## Skill Integration

The agent is **skill-aware**, meaning it MUST read the onboarding skill before performing any task. This ensures:

- **Consistency**: Every onboarding follows proven frameworks
- **Completeness**: Nothing important is missed
- **Quality**: Professional standards maintained
- **Best Practices**: Incorporates research-backed approaches
- **Templates**: Uses battle-tested formats

The skill contains:
- 8-part comprehensive onboarding framework
- Role-specific templates (Engineering, Sales, Marketing, CS)
- 20+ email templates for all onboarding stages
- IT provisioning standards and checklists
- Training schedule frameworks
- Check-in and follow-up protocols
- Remote onboarding adaptations
- Quality metrics and improvement strategies

## Customization

### Adding Company-Specific Content

1. **Edit the skill** to include your:
   - Company name and branding
   - Specific policies and benefits
   - Internal tools and systems
   - Team structure and contacts
   - Culture and values

2. **Create templates** for recurring content:
   - Department-specific onboarding
   - Location-specific information
   - Custom role requirements

3. **Extend the agent** with:
   - Additional responsibilities
   - Integration with your systems
   - Custom output formats

### Example Customization

```bash
# Edit skill to add company details
edit plugins/hr-onboarder/skills/onboarding/SKILL.md

# Add sections for:
# - Your specific IT systems
# - Your benefit enrollment process
# - Your team structure
# - Your location details
```

## Integration with Other Tools

### Calendar Integration

Export schedules to calendar format:
```
"Create a calendar-ready training schedule for the new hire"
```

### HRIS Systems

Generate data in formats compatible with:
- Workday
- BambooHR
- Greenhouse
- Lever
- Other HR systems

### Communication Platforms

Materials work with:
- Email (Gmail, Outlook)
- Slack
- Microsoft Teams
- Workplace

## Troubleshooting

### Agent Not Activating

**Issue**: Agent doesn't activate automatically

**Solutions**:
- Use explicit trigger phrases ("onboard new employee", "create onboarding plan")
- Manually invoke with `@hr-onboarder`
- Check installation path

### Generic Output

**Issue**: Materials feel generic, not personalized

**Solutions**:
- Provide complete details (name, role, start date, manager)
- Review and customize generated materials
- Add company-specific content to the skill
- Request specific sections ("focus on IT setup")

### Missing Role-Specific Content

**Issue**: Onboarding doesn't include role-specific elements

**Solutions**:
- Specify the role clearly in your request
- Use standard role names (Engineering, Sales, Marketing, CS)
- Ask for role-specific additions explicitly
- Extend the skill with your custom roles

### Outdated Information

**Issue**: Templates reference outdated tools or processes

**Solutions**:
- Update the onboarding skill with current information
- Customize templates for your current tech stack
- Review and edit generated materials before use

## Examples

### Example 1: Complete Engineering Onboarding

**Request**:
```
Create a complete onboarding plan for Jamie Chen, Senior Backend Engineer,
starting May 15, 2025. Manager is Alex Kumar. Remote employee.
```

**Output**:
```
onboarding-jamie-chen/
├── welcome-email.md                             # Pre-start communication
├── day-one-schedule.md                          # 9 AM - 5 PM detailed schedule
├── week-one-checklist.md                        # Daily priorities
├── 30-60-90-day-plan.md                        # Engineering milestones
├── training-plan.md                            # Technical training schedule
├── it-provisioning-checklist.md                # Dev tools, access, hardware
├── check-in-templates/
│   ├── 30-day-check-in.md                      # First review
│   ├── 60-day-check-in.md                      # Progress review
│   └── 90-day-review.md                        # Performance evaluation
└── README.md                                    # Overview and next steps
```

**Highlights**:
- Engineering-specific setup (IDE, repos, dev environment)
- First commit goal by day 30
- Codebase architecture overview scheduled
- Remote-specific enhancements (virtual pairing, async docs)

### Example 2: Quick IT Checklist

**Request**:
```
What IT setup does a Marketing Manager need?
```

**Output**:
- Laptop with dual monitors
- Adobe Creative Suite
- Marketing automation platform (HubSpot/Marketo)
- Analytics access (Google Analytics, Mixpanel)
- Social media management tools
- CMS access
- Brand assets and templates
- Video conferencing tools

### Example 3: Sales Onboarding with Fast Ramp

**Request**:
```
Create an accelerated 30-day onboarding for experienced Account Executive.
They need to be selling within 2 weeks.
```

**Output**:
- **Week 1**: Intensive product training and CRM setup
- **Week 2**: Shadow 10 sales calls, lead first discovery call
- **Week 3-4**: Own pipeline, close first deal
- Compressed training schedule
- Accelerated certification
- Early quota assignment
- Buddy is top seller

## Performance and Quality

### Quality Metrics

Well-designed onboarding achieves:
- **90%+ new hire satisfaction** (based on surveys)
- **<30 days to first meaningful contribution**
- **85%+ retention through first year**
- **50% faster time to full productivity**
- **Higher engagement scores** at 90 days

### Generated Content Quality

All materials include:
- **Specific dates and times** (not vague "first week")
- **Assigned responsibilities** (who does what)
- **Clear expectations** (what success looks like)
- **Actionable items** (can be checked off)
- **Professional tone** (welcoming and inclusive)

## Contributing

To improve this plugin:

1. **Share feedback** on what works well
2. **Suggest additions** to the skill library
3. **Contribute templates** for additional roles
4. **Report issues** with edge cases
5. **Submit improvements** via pull request

## License

MIT License - feel free to use and customize for your organization

## Support

For questions or issues:
- Check this README first
- Review the onboarding skill documentation
- Open an issue in the repository
- Share your use case for assistance

## Changelog

### Version 1.0.0 (2025-01-19)

**Initial Release**:
- HR onboarder agent with comprehensive workflow
- Onboarding skill with battle-tested frameworks
- Pre-arrival through 90-day timeline coverage
- Role-specific templates (Engineering, Sales, Marketing, CS)
- IT provisioning standards
- 20+ email templates
- Check-in and follow-up protocols
- Remote onboarding adaptations
- Quality metrics and best practices

## Acknowledgments

Built on research and best practices from:
- 1000+ successful onboarding experiences
- HR industry standards and benchmarks
- Employee experience research
- Feedback from managers, new hires, and HR teams

---

**Make every first day a great day. Set new hires up for long-term success.**
