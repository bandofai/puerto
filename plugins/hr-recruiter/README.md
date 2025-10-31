# HR Recruiter Plugin

**Professional recruitment assistant for candidate screening, job postings, interview coordination, and hiring pipeline management.**

## Overview

The HR Recruiter plugin provides a specialized subagent for handling end-to-end recruitment workflows. It combines battle-tested HR best practices with automated workflows to streamline hiring processes while maintaining professional standards and inclusive practices.

### Key Features

- **CV Screening**: Intelligent resume analysis with evidence-based scoring
- **Job Description Creation**: Professional, inclusive job postings using proven templates
- **Interview Coordination**: Automated scheduling and communication
- **Candidate Communication**: Professional email templates for all hiring stages
- **Pipeline Tracking**: JSON-based candidate management system
- **Diversity & Inclusion**: Built-in guidelines for fair, inclusive hiring

## Installation

### User-Level (Available to All Projects)

```bash
# Copy agent
cp plugins/hr-recruiter/agents/hr-recruiter.md ~/.claude/agents/

# Copy skill
mkdir -p ~/.claude/skills/recruitment/
cp plugins/hr-recruiter/skills/recruitment/SKILL.md ~/.claude/skills/recruitment/
```

### Project-Level (Project-Specific)

```bash
# Copy agent
mkdir -p .claude/agents/
cp plugins/hr-recruiter/agents/hr-recruiter.md .claude/agents/

# Copy skill
mkdir -p .claude/skills/recruitment/
cp plugins/hr-recruiter/skills/recruitment/SKILL.md .claude/skills/recruitment/
```

## Quick Start

### 1. Screen a Resume

Simply ask Claude Code:
```
"Please screen this resume for the Senior Engineer position"
```

The agent will:
- Read the recruitment skill
- Parse the resume
- Score against requirements
- Generate a detailed screening report
- Provide hiring recommendation

**Output**: `.claude/recruitment/screenings/[candidate-name]-[date].md`

### 2. Create a Job Description

```
"Create a job description for a Senior Software Engineer position"
```

The agent will:
- Ask clarifying questions about the role
- Use appropriate template from skill
- Ensure inclusive language
- Generate professional posting

**Output**: `.claude/recruitment/job-descriptions/[role]-[date].md`

### 3. Schedule an Interview

```
"Schedule an interview with Jane Doe for the engineering role"
```

The agent will:
- Generate scheduling email with time options
- Provide confirmation template
- Create interview prep materials

**Output**: `.claude/recruitment/communications/[candidate-name]-interview-invite.md`

### 4. Track Candidate Pipeline

```
"Update Jane Doe's status to 'interviewing' in the pipeline"
```

The agent will:
- Load pipeline JSON
- Update candidate status
- Set next steps
- Save updated pipeline

**Output**: `.claude/recruitment/pipeline.json`

## Components

### Agent: `hr-recruiter`

**Location**: `agents/hr-recruiter.md`

**Description**: PROACTIVELY use for recruitment tasks. Screens CVs, creates job postings, schedules interviews, manages candidate communication, and tracks hiring pipeline.

**Tools**: Read, Write, Edit, Bash, Glob, Grep

**Model**: Sonnet (requires judgment for candidate evaluation)

**Key Capabilities**:
- Resume parsing and evaluation
- Job description generation
- Interview coordination
- Professional email composition
- Pipeline management

### Skill: Recruitment Best Practices

**Location**: `skills/recruitment/SKILL.md`

**Contains**:
- Resume screening rubrics (0-10 scoring system)
- Job description templates (Engineering, Marketing, Sales)
- Interview question banks (behavioral, technical)
- Email templates (20+ scenarios)
- Pipeline data structures
- Diversity & inclusion guidelines
- Legal compliance guidelines

## Usage Examples

### Example 1: Full Candidate Screening

**Input**:
```
"Screen this resume for our Senior Software Engineer position:
[paste resume or provide file path]

Job requirements:
- 5+ years Python experience
- Strong API design skills
- Experience with distributed systems
- Leadership experience preferred"
```

**Output**:
```markdown
✅ Candidate screening completed

**Candidate**: John Doe
**Assessment**: Strong Fit (8.5/10)
**Recommendation**: Schedule technical interview

Screening report: .claude/recruitment/screenings/john-doe-2025-01-19.md

Key highlights:
- 7 years Python development experience
- Led API redesign serving 10M+ requests/day
- Built distributed caching system
- Mentored team of 4 junior engineers

Next steps: Schedule technical interview focusing on system design and architecture
```

### Example 2: Job Posting Creation

**Input**:
```
"Create a job description for a Marketing Manager position.

Details:
- B2B SaaS company
- Will own content marketing and demand generation
- Report to VP Marketing
- Remote position
- 5-8 years experience
- Budget: $120k-$150k"
```

**Output**:
```markdown
✅ Job description created

**Position**: Marketing Manager
**Key highlights**: Remote role leading content marketing and demand gen for B2B SaaS company

Job description: .claude/recruitment/job-descriptions/marketing-manager-2025-01-19.md

Ready to post to: LinkedIn, Indeed, company careers page

The posting includes:
- Compelling company overview
- Clear responsibilities
- Realistic requirements
- Transparent compensation range
- Inclusive language (scored 98/100 on bias checker)
```

### Example 3: Multi-Step Interview Coordination

**Input**:
```
"We want to interview Sarah Chen for the Product Manager role. She's available Tuesday or Thursday afternoons. Set up a panel interview with the engineering lead and design lead."
```

**Output**:
```markdown
✅ Interview coordination completed

**Candidate**: Sarah Chen
**Position**: Product Manager
**Format**: Panel interview (90 minutes)
**Interviewers**:
- Alex Rodriguez, Engineering Lead
- Morgan Kim, Design Lead

Communications generated:
1. Interview invitation: .claude/recruitment/communications/sarah-chen-interview-invite.md
2. Confirmation template: .claude/recruitment/communications/sarah-chen-confirmation.md
3. Reminder template: .claude/recruitment/communications/sarah-chen-reminder.md

Suggested schedule:
- Option 1: Tuesday, Jan 23 at 2:00 PM EST
- Option 2: Thursday, Jan 25 at 1:00 PM EST
- Option 3: Thursday, Jan 25 at 3:00 PM EST

Next steps: Send invitation email and await confirmation
```

## Pipeline Management

### Pipeline Structure

The agent maintains a JSON-based pipeline:

```json
{
  "pipeline_version": "1.0",
  "last_updated": "2025-01-19T10:30:00Z",
  "positions": [...],
  "candidates": [
    {
      "id": "CAND-001",
      "name": "Jane Doe",
      "email": "jane.doe@example.com",
      "position_id": "JOB-001",
      "status": "interviewing",
      "screening_score": 8.5,
      "next_steps": "Schedule panel interview",
      ...
    }
  ]
}
```

### Status Values

**Candidate Statuses**:
- `applied` → `screening` → `screening_passed` → `interviewing` → `interview_completed` → `offer_extended` → `hired`

Alternative paths:
- `screening_declined`: Did not meet requirements
- `offer_declined`: Candidate declined offer
- `withdrawn`: Candidate withdrew

### Pipeline Operations

**View Pipeline**:
```
"Show me the current recruitment pipeline"
```

**Update Status**:
```
"Move John Doe to 'offer_extended' status"
```

**Generate Report**:
```
"Generate a weekly recruitment pipeline report"
```

## Best Practices

### Screening

✅ **DO**:
- Use the scoring rubric consistently
- Cite specific evidence from resume
- Focus on qualifications, not demographics
- Give credit for transferable skills
- Consider non-traditional backgrounds

❌ **DON'T**:
- Make snap judgments
- Let personal preferences influence scores
- Assume based on school names or company logos
- Penalize employment gaps without context
- Screen out based on protected characteristics

### Job Descriptions

✅ **DO**:
- Keep required qualifications realistic
- Use inclusive, gender-neutral language
- Include compensation range (if company policy allows)
- Highlight growth opportunities
- Be transparent about work arrangement

❌ **DON'T**:
- Create wish lists of nice-to-haves
- Use jargon or exclusionary terms ("rockstar", "ninja")
- Hide critical information
- Copy outdated templates
- Skip the diversity statement

### Communication

✅ **DO**:
- Respond within 2 business days
- Personalize every message
- Set clear next steps and timelines
- Be respectful and professional
- Proofread before sending

❌ **DON'T**:
- Ghost candidates
- Use generic copy-paste responses
- Leave candidates hanging
- Over-promise and under-deliver
- Forget to follow up

## Integration

### With Other Claude Code Plugins

**Orchestrator Plugin**: Coordinate multi-agent recruitment workflows
```
Orchestrator → HR Recruiter (screen) → Technical Interviewer → HR Recruiter (offer)
```

**Document Generator**: Create formatted offer letters
```
HR Recruiter (approve offer) → Doc Generator (create PDF) → HR Recruiter (send)
```

### With External Tools

**Email Systems**: Send communications (Gmail, Outlook, etc.)
**Calendar**: Schedule interviews (Google Calendar, Outlook)
**ATS Systems**: Import/export pipeline data (Greenhouse, Lever)
**Job Boards**: Post job descriptions (LinkedIn, Indeed)

## Configuration

### Customizing Templates

Edit the skill file to add company-specific templates:

```bash
# Edit skill
vi ~/.claude/skills/recruitment/SKILL.md

# Or project-level
vi .claude/skills/recruitment/SKILL.md
```

**What to customize**:
- Company name in templates
- Benefits and perks
- Interview process details
- Diversity statements
- Email signatures

### Adjusting Scoring Rubrics

Modify the screening rubric in the skill file to match your company's priorities:

```markdown
**Experience Match (0-3 points)**:
- 3: [Your criteria for top score]
- 2: [Your criteria for good score]
- 1: [Your criteria for acceptable]
- 0: [Your criteria for insufficient]
```

## Privacy and Compliance

### Data Protection

The agent is designed to handle candidate data responsibly:

- **Storage**: All data stored locally in `.claude/recruitment/`
- **Access**: File permissions should restrict access appropriately
- **Retention**: Delete candidate data per company policy
- **Consent**: Inform candidates about data collection and usage

### Legal Compliance

The skill includes guidelines for:
- **GDPR** (EU): Right to access, delete, and data portability
- **CCPA** (California): Data collection disclosure
- **EEOC** (US): Non-discriminatory hiring practices
- **ADA** (US): Reasonable accommodations

**Important**: This agent provides guidance but does not replace legal counsel. Consult with your legal team about compliance requirements.

## Troubleshooting

### Agent doesn't activate

**Problem**: You ask about recruitment but the agent doesn't engage

**Solution**: Use trigger phrases:
- "Please screen this resume..."
- "Create a job description for..."
- "Schedule an interview with..."
- Or explicitly invoke the agent

### Skill not found

**Problem**: Agent can't find recruitment skill

**Solution**: Verify skill is installed:
```bash
# Check user-level
ls ~/.claude/skills/recruitment/SKILL.md

# Check project-level
ls .claude/skills/recruitment/SKILL.md
```

If missing, reinstall following [Installation](#installation) steps.

### Pipeline JSON errors

**Problem**: Pipeline file is corrupted or invalid

**Solution**: Validate and fix JSON:
```bash
# Validate
jq . .claude/recruitment/pipeline.json

# If corrupted, restore from backup or reinitialize
echo '{"candidates":[]}' > .claude/recruitment/pipeline.json
```

### Templates seem outdated

**Problem**: Email templates or job descriptions don't match current practices

**Solution**: The skill file is customizable. Update templates to match your company's current standards:
```bash
vi ~/.claude/skills/recruitment/SKILL.md
```

## Contributing

Found ways to improve this plugin? Contributions welcome!

### Ideas for Enhancement

- Integration with specific ATS systems
- Additional job description templates (Executive, Operations, etc.)
- Interview question banks for specialized roles
- Automated reference checking workflows
- Offer negotiation guidance
- Onboarding handoff workflows

### Submitting Improvements

1. Test your changes thoroughly
2. Update documentation
3. Submit pull request with clear description
4. Include examples of improvements

## Support

### Resources

- **Plugin Documentation**: This README
- **Skill Guide**: `skills/recruitment/SKILL.md`
- **Agent Definition**: `agents/hr-recruiter.md`
- **Examples**: See [Usage Examples](#usage-examples)

### Getting Help

- Check troubleshooting section above
- Review skill guide for template details
- Consult Claude Code documentation
- Open issue in Puerto repository

## License

This plugin is part of the Puerto project. See main repository for license details.

## Changelog

### Version 1.0.0 (2025-01-19)

**Initial Release**:
- HR Recruiter agent with comprehensive recruitment capabilities
- Recruitment skill with templates and best practices
- Resume screening with evidence-based rubric
- Job description templates (Engineering, Marketing, Sales)
- Interview coordination workflows
- Candidate communication templates (20+ scenarios)
- Pipeline management with JSON structure
- Diversity & inclusion guidelines
- Legal compliance guidance

## Acknowledgments

Built with best practices from:
- HR professionals with 50+ years combined experience
- 1000+ successful hires across tech, marketing, and sales roles
- Diversity & inclusion research and frameworks
- EEOC, GDPR, and employment law guidelines

---

**Version**: 1.0.0
**Author**: Claude Code Community
**Maintained by**: Puerto Plugin Marketplace
**Last Updated**: January 2025
