# Career Development Planner Plugin

Professional career growth and development specialist providing comprehensive skill gap analysis, networking management, job search organization, and career advancement planning.

## Overview

The Career Development Planner plugin transforms how you manage your professional growth by providing three specialized AI agents and comprehensive career development resources. Whether you're targeting a promotion, pivoting careers, or optimizing your job search, this plugin provides the frameworks, tracking, and guidance to achieve your career goals systematically.

## What's Included

### 3 Specialized Agents

#### 1. skill-gap-analyzer (Sonnet)

Expert career analyst that:
- **Analyzes current skills** versus target role requirements
- **Identifies critical gaps** with prioritization (must-have, competitive advantage, emerging)
- **Creates phased development plans** with concrete learning paths and resources
- **Estimates learning timelines** based on skill complexity and time availability
- **Generates comprehensive reports** with actionable next steps

**Activation**: Use `@skill-gap-analyzer` or automatically activates when discussing career goals and skill development.

**Use Cases**:
- Planning promotion to senior/lead role
- Career pivot preparation (e.g., marketing → data analytics)
- Evaluating readiness for target role
- Creating 6-12 month professional development roadmap

#### 2. networking-manager (Haiku)

Professional relationship coordinator that:
- **Tracks contacts** with comprehensive professional network database
- **Logs interactions** with dates, summaries, and action items
- **Manages follow-ups** with automatic reminder calculation
- **Categorizes relationships** by strength (new → weak → moderate → strong → champion)
- **Provides actionable insights** on who to contact and when

**Activation**: Use `@networking-manager` for all professional networking activities.

**Use Cases**:
- Building network in target industry/company
- Managing job search connections
- Tracking informational interviews
- Nurturing mentor relationships
- Following up with hiring managers

#### 3. job-application-tracker (Haiku)

Job search organizer that:
- **Tracks applications** through entire funnel (applied → interview → offer)
- **Schedules interviews** with preparation checklists
- **Records salary data** for negotiation intelligence
- **Compares offers** across total compensation and fit factors
- **Analyzes conversion rates** to optimize job search strategy

**Activation**: Use `@job-application-tracker` for all job search activities.

**Use Cases**:
- Organizing active job search
- Preparing for interview rounds
- Tracking salary negotiation data
- Comparing multiple offers
- Monitoring job search health metrics

### Comprehensive Skill Library

**Career Development Skill** (`skills/career-development/SKILL.md`)

Expert knowledge covering:
- **Skill Gap Analysis**: Assessment frameworks, proficiency levels, gap identification
- **Career Goal Setting**: SMART goals, vision exercises, reverse engineering
- **Professional Development**: Learning pathways, portfolio building, resource guides
- **Networking Strategies**: Relationship building, informational interviews, event networking
- **Job Search Best Practices**: Application optimization, channel strategies, funnel metrics
- **Interview Preparation**: Technical, behavioral, system design prep with frameworks
- **Salary Negotiation**: Research, strategy, scripts, offer evaluation
- **Career Transitions**: Promotion paths, career pivots, leadership development
- **Industry Resources**: Job boards, communities, certifications, learning platforms

All agents read this skill to provide expert-level guidance.

### Professional Templates

**1. Career Development Plan Template** (`templates/career-development-plan-template.md`)

Comprehensive plan structure with:
- Current state and target state assessment
- Detailed skill gap analysis by priority
- 3-phase development plan (Foundation → Growth → Mastery)
- Weekly schedules and action items
- Portfolio project planning
- Networking strategy
- Success metrics and KPIs
- Risk mitigation and contingency plans

**2. Networking Database Template** (`templates/networking-database-template.json`)

Professional contact tracking with:
- Contact information and relationship details
- Interaction logging with timestamps
- Follow-up scheduling and reminders
- Career relevance tracking (value exchange)
- Relationship strength progression
- Personal notes and conversation topics
- Tags for easy filtering

**3. Job Application Tracker Template** (`templates/job-application-tracker-template.json`)

Complete job search management with:
- Application status tracking (applied → offer)
- Interview scheduling and preparation
- Compensation data and negotiation tracking
- Offer comparison framework
- Job search statistics and conversion rates
- Action item management
- Salary research and market data

## Installation

```bash
/plugin install career-development-planner@puerto
```

After installation, restart Claude Code to activate all agents and skills.

## Quick Start

### Scenario 1: Planning Career Growth

```
@skill-gap-analyzer I'm a mid-level software engineer targeting a senior role
in 6-12 months. I have 4 years Python experience, built microservices, but
limited system design and leadership experience.
```

**Agent will**:
1. Ask clarifying questions about target role details
2. Research market requirements for senior engineers
3. Identify critical gaps (system design, technical leadership)
4. Create phased learning plan with courses, projects, timelines
5. Generate comprehensive development plan

**You receive**:
- `skill_gap_analysis.md` - Detailed gap analysis
- `development_plan.json` - Structured plan for tracking
- `learning_tracker.csv` - Progress tracking spreadsheet

### Scenario 2: Building Professional Network

```
@networking-manager Add new contact: Jane Smith, Senior Engineering Manager
at Tech Corp. Met at TechConf 2025. She's hiring for my target role and
offered to have coffee chat.
```

**Agent will**:
1. Create contact record in database
2. Log initial interaction
3. Calculate next follow-up date
4. Suggest specific follow-up action

```
@networking-manager Show me who I need to follow up with this week
```

**Agent will**:
1. Check all contacts for overdue/upcoming follow-ups
2. Prioritize by relationship strength and career relevance
3. Suggest specific actions for each person
4. Generate networking report

**You receive**:
- `networking_database.json` - Comprehensive contact database
- `networking_report.md` - Follow-up dashboard and insights
- `contacts_export.csv` - Spreadsheet-compatible export

### Scenario 3: Managing Job Search

```
@job-application-tracker Add application: Tech Corp, Senior Software Engineer,
applied via employee referral from Jane Smith. Salary range $150-180k, targeting
$185k. High priority, very interested.
```

**Agent will**:
1. Create application record with all details
2. Calculate follow-up schedule
3. Set next action reminders
4. Track in overall job search funnel

```
@job-application-tracker Schedule interview: Tech Corp, technical round,
Jan 30 at 10am, 90 minutes, video call, system design focus
```

**Agent will**:
1. Add interview to application
2. Update status to "technical"
3. Generate preparation checklist
4. Suggest study resources

```
@job-application-tracker Show my job search dashboard
```

**Agent will**:
1. Calculate conversion rates
2. List upcoming interviews
3. Identify follow-ups needed
4. Show application velocity vs. goal
5. Generate comprehensive report

**You receive**:
- `job_applications.json` - Complete application database
- `job_search_report.md` - Dashboard with metrics and action items
- `applications_export.csv` - Spreadsheet export

## Complete Workflow Example

**Goal**: Get promoted to Senior Engineer in 6 months

### Month 1: Assessment & Planning

```
# Step 1: Skill gap analysis
@skill-gap-analyzer Analyze gaps for Senior Software Engineer promotion at
my current company. Focus: system design, technical leadership, cross-team
collaboration.

# Step 2: Build development plan from analysis
# Review skill_gap_analysis.md and development_plan.json

# Step 3: Start networking
@networking-manager Add contact: Bob Johnson, current Senior Engineer on
Platform team. Can provide mentorship on system design.

# Begin learning (from plan)
# Enroll in "Grokking System Design Interview" course
# Start "Designing Data-Intensive Applications" book
```

### Month 2-3: Skill Building

```
# Log learning progress and network growth
@skill-gap-analyzer Update: Completed system design fundamentals course,
built URL shortener system design, practicing weekly.

@networking-manager Log interaction: Coffee chat with Bob Johnson.
Discussed system design patterns. He offered to review my designs.
Action item: Share my URL shortener design for feedback.

# Continue building portfolio
# Complete 2 system design projects
# Present technical talk at team meeting
```

### Month 4-5: Demonstrate Readiness

```
# Lead project to demonstrate senior-level work
# Mentor junior engineer
# Drive technical decision on team

@networking-manager Add contact: Sarah Williams, Engineering Manager.
She's involved in promotion decisions. Met at company all-hands.

@networking-manager Log interaction: 1-on-1 with Sarah. Discussed
career goals and promotion timeline. Action: Prepare promotion packet
for next review cycle.
```

### Month 6: Promotion Discussion

```
# Prepare promotion materials
# Review skill_gap_analysis.md to document progress
# Update resume with senior-level accomplishments

# Have promotion conversation with manager
# If successful: Update LinkedIn, celebrate
# If not: Re-run analysis, adjust plan, continue growth
```

**Alternative: External Job Search**

If pursuing external opportunities:

```
# After skill building (Months 1-3)

@job-application-tracker Set job search metadata:
Target: Senior Software Engineer
Goal: 5 applications per week
Timeline: Start offers by Month 6

@job-application-tracker Add application: [Company details]

# Track through interview process
@job-application-tracker Schedule interview: [Details]

# Compare offers
@job-application-tracker Compare all offers

# Use networking database for company research
@networking-manager Search contacts: Company = "Target Corp"
```

## Features

### Intelligent Analysis

**skill-gap-analyzer**:
- Multi-dimensional skill assessment (technical, soft, domain)
- Industry-standard frameworks (SFIA, O*NET)
- Realistic time estimates based on skill complexity
- Phased learning approach (critical → important → emerging)
- Comprehensive resource curation (courses, books, projects)
- Portfolio-building integrated throughout
- Validation methods for each skill

### Relationship Management

**networking-manager**:
- Automatic follow-up scheduling based on relationship strength
- Interaction history with searchable notes
- Value exchange tracking (mutual help)
- Personal detail storage for meaningful conversations
- Tag-based filtering (hiring manager, mentor, peer, etc.)
- Export to CRM tools (CSV format)
- Relationship progression tracking (new → champion)

### Job Search Optimization

**job-application-tracker**:
- Full funnel tracking (applied → offer)
- Conversion rate analytics (response rate, interview rate)
- Interview preparation checklists
- Salary data aggregation for negotiation
- Offer comparison framework (total comp + fit factors)
- Application velocity monitoring (vs. weekly goal)
- Follow-up reminder system

## Agent Coordination

The three agents work together seamlessly:

```
skill-gap-analyzer
    ↓ Identifies needed skills
    ↓ Recommends networking with experts
    ↓
networking-manager
    ↓ Tracks mentors and industry contacts
    ↓ Builds relationships at target companies
    ↓
job-application-tracker
    ↓ Organizes applications to target companies
    ↓ References networking contacts
    ↓
    → Tracks interviews and offers
    → Uses skill development for interview prep
    → Validates readiness from skill gap analysis
```

**Example**:
1. `@skill-gap-analyzer` identifies "system design" as critical gap
2. Suggests networking with senior engineers for mentorship
3. `@networking-manager` tracks mentorship relationships
4. You build skills through mentored projects
5. `@job-application-tracker` tracks applications requiring system design
6. Interview prep references your portfolio from skill development
7. Salary negotiation uses market data from application tracking

## Configuration

### Agent Settings

**skill-gap-analyzer**:
- **Tools**: Read, Write, Python
- **Model**: Sonnet (requires analytical reasoning)
- **Outputs**: `/Users/tomas.kavka/www/bandofai/puerto-issue-133/outputs/`

**networking-manager**:
- **Tools**: Read, Write, Python
- **Model**: Haiku (fast CRUD operations)
- **Database**: `/Users/tomas.kavka/www/bandofai/puerto-issue-133/outputs/networking_database.json`

**job-application-tracker**:
- **Tools**: Read, Write, Python
- **Model**: Haiku (efficient tracking and reporting)
- **Database**: `/Users/tomas.kavka/www/bandofai/puerto-issue-133/outputs/job_applications.json`

### Customization

**Adjust output location** by modifying agent paths:
```python
# In each agent's code
DATABASE_PATH = "/your/preferred/location/database.json"
```

**Import/export data**:
- All databases use standard JSON format
- CSV exports available for spreadsheet tools
- Compatible with CRM systems (networking data)
- Can import into Notion, Trello, etc.

## File Structure

```
career-development-planner/
├── .claude-plugin/
│   └── plugin.json                      # Plugin metadata
├── agents/
│   ├── skill-gap-analyzer.md            # Career analysis agent (Sonnet)
│   ├── networking-manager.md            # Relationship tracking (Haiku)
│   └── job-application-tracker.md       # Job search organizer (Haiku)
├── skills/
│   └── career-development/
│       └── SKILL.md                     # Comprehensive career expertise
├── templates/
│   ├── career-development-plan-template.md   # Development plan structure
│   ├── networking-database-template.json     # Contact tracking format
│   └── job-application-tracker-template.json # Job search format
└── README.md                            # This file
```

## Best Practices

### Career Development Planning

**Run skill gap analysis**:
- When targeting promotion (3-6 months before review cycle)
- Before career pivot (to understand learning required)
- Annually for continuous growth planning
- When job descriptions consistently show unfamiliar requirements

**Update development plan**:
- Weekly: Track hours invested, courses completed
- Monthly: Assess progress vs. plan, adjust if needed
- Quarterly: Re-run skill gap analysis to measure growth

### Professional Networking

**Add contacts immediately**:
- After conferences, meetups, events
- When receiving LinkedIn connection acceptance
- After informational interviews
- When meeting colleagues at target companies

**Log interactions consistently**:
- Same day as interaction (details fresh)
- Include action items and follow-up needs
- Note personal details for future conversations

**Follow up religiously**:
- Check weekly for overdue/upcoming follow-ups
- New contacts: within 3 days
- Weak relationships: monthly
- Strong relationships: quarterly
- Champions: monthly (very important)

### Job Search Management

**Track all applications**:
- Even "long shot" applications (you might be surprised)
- Record salary ranges (builds market intelligence)
- Save job descriptions (they get removed from postings)

**Update immediately**:
- When status changes (phone screen scheduled, rejection, etc.)
- After every interview (notes, feedback, impressions)
- When receiving offer (full details for comparison)

**Monitor metrics weekly**:
- Are you hitting application goal? (typically 5-10/week)
- Response rate acceptable? (target: 15-30%)
- Interview conversion healthy? (phone→technical: 50%+)
- Follow-ups current? (no overdue items)

## Success Metrics

Track these indicators monthly:

### Skill Development
- Courses completed vs. plan
- Certifications achieved
- Portfolio projects shipped
- Blog posts or talks delivered
- Hours invested in learning

### Networking
- Total contacts (target: grow 20-30/quarter)
- Relationship progression (weak → moderate → strong)
- Follow-ups completed on time (target: 100%)
- Value provided to network (introductions, help given)
- Informational interviews conducted

### Job Search (if active)
- Applications submitted vs. goal
- Response rate (target: 15-30%)
- Interview conversion rates
- Offers received
- Days to offer (from search start)

### Career Impact
- Promotions or scope increases
- Compensation growth (YoY)
- Industry recognition (speaking, writing)
- Leadership responsibilities

## Integration with Other Tools

### Export to Spreadsheets

All databases provide CSV exports:
```
@networking-manager Export to CSV
→ contacts_export.csv (import to Excel, Google Sheets)

@job-application-tracker Export to CSV
→ applications_export.csv (import to spreadsheet)
```

### Import to Project Management

JSON databases can be imported:
- **Notion**: Import JSON as database
- **Trello**: Convert to cards via API
- **Asana**: Import as tasks
- **CRM tools**: Use CSV export

### Link with Calendar

Use action items and dates to create calendar events:
- Interview dates
- Follow-up reminders
- Application deadlines
- Networking events

### Combine with Resume Tools

Reference databases when updating:
- Resume: Pull accomplishments from development plan
- LinkedIn: Add new skills as acquired
- Portfolio: Link to projects from skill development

## Troubleshooting

### Skill Gap Analysis Issues

**Issue**: Analysis seems generic, not specific to my situation

**Solution**: Provide more context:
- Current role and seniority level
- Specific target companies/industries
- Years of experience in key skills
- Unique constraints (timeline, budget, time availability)

**Issue**: Learning timeline seems unrealistic

**Solution**: Adjust based on your availability:
- Provide actual hours/week available for learning
- Consider extending overall timeline
- Prioritize critical skills only if time-constrained

### Networking Management Issues

**Issue**: Too many overdue follow-ups

**Solution**:
- Prioritize by relationship strength and career relevance
- Focus on "champion" and "strong" relationships first
- Extend follow-up intervals if needed
- Archive inactive contacts

**Issue**: Don't know what to say in follow-ups

**Solution**: Use suggested actions:
- Share relevant article (value-first approach)
- Ask specific question related to your career goals
- Provide update on your progress
- Offer help with their projects

### Job Search Tracking Issues

**Issue**: Low response rate (< 10%)

**Solution**:
- Review resume (too generic? missing keywords?)
- Improve application targeting (apply to better-fit roles)
- Get resume reviewed by professional
- Focus on referrals vs. online applications

**Issue**: Interviews not converting to offers

**Solution**:
- Practice more (mock interviews on Pramp, Interviewing.io)
- Review interview feedback if available
- Strengthen weak areas (coding, system design, behavioral)
- Consider interview coaching

**Issue**: Job search taking too long

**Solution**:
- Increase application velocity (5-10/week minimum)
- Expand target companies/roles
- Leverage network more (referrals have 40% interview rate)
- Consider bridge role while building skills

## Advanced Usage

### Career Pivot Planning

For major career transitions:

```
# Step 1: Analyze gaps for new field
@skill-gap-analyzer I'm a marketing professional with 5 years experience
targeting Data Analyst role. No technical background. Timeline: 12 months.

# Step 2: Identify transferable skills
# Focus development plan on critical gaps only

# Step 3: Build network in new field
@networking-manager Tag contacts: career_pivot, data_analytics
# Connect with 20-30 data professionals
# Schedule 10+ informational interviews

# Step 4: Build portfolio proving capability
# Complete 3-5 data projects
# Contribute to open source
# Write blog posts demonstrating knowledge

# Step 5: Target bridge roles
@job-application-tracker Target: Junior Data Analyst or Analytics Associate
# Accept lower initial salary for field entry
# Grow from within new field
```

### Promotion Preparation

Internal advancement strategy:

```
# 6 months before promotion cycle

# Step 1: Gap analysis for next level
@skill-gap-analyzer Targeting promotion from Software Engineer II to
Senior Engineer. Internal promotion at current company.

# Step 2: Document current impact
# Build portfolio of senior-level work
# Demonstrate leadership without title

# Step 3: Build internal support
@networking-manager Add contacts: Manager, skip-level manager, peer
senior engineers, other team leads

# Step 4: Create promotion packet
# Reference skill_gap_analysis.md for evidence
# Quantify impact (metrics, scope, complexity)
# Get peer endorsements

# Step 5: Promotion discussion
# Present packet to manager
# Reference specific accomplishments
# Demonstrate operating at next level for 6+ months
```

### Optimizing Multiple Offers

Decision framework:

```
# You have 3 offers

@job-application-tracker Compare all offers

# Evaluate beyond just total comp:

Factors to consider:
1. Total comp (base + bonus + equity realistic value)
2. Learning opportunity (skills you'll gain)
3. Career trajectory (what's next role after this?)
4. Work-life balance (hours, flexibility, PTO)
5. Company stability (runway, profitability, market)
6. Culture fit (values, team, management style)
7. Location (commute, relocation, remote)

# Use weighted scoring:
Company A: $450k, excellent learning, good culture → Score: 8.5
Company B: $480k, moderate learning, okay culture → Score: 7.8
Company C: $420k, exceptional learning, great culture → Score: 9.0

# Company C wins despite lowest comp
# Sometimes highest comp isn't best long-term career move
```

## Examples from Production

### Example 1: Junior to Senior Promotion (6 months)

**Starting Point**:
- Junior Engineer, 2 years experience
- Strong coding, weak system design
- No leadership experience

**Skill Gap Analysis**:
- Critical: System design, technical leadership
- Important: Cross-team collaboration, mentorship
- Emerging: Architecture patterns

**Plan Execution**:
- Months 1-2: Complete system design course, design 2 systems
- Months 3-4: Lead medium project, mentor 1 junior
- Months 5-6: Drive technical decision, present at company tech talk

**Result**: Promoted at 6-month mark

**Key Success Factors**:
- Demonstrated senior work before title
- Built internal support (manager, senior peers)
- Quantified impact in promotion packet

### Example 2: Career Pivot (Marketing → Data Science, 12 months)

**Starting Point**:
- Marketing Manager, 6 years experience
- No programming or statistics background
- Strong communication and business acumen

**Skill Gap Analysis**:
- Critical: Python, SQL, statistics, ML fundamentals
- Important: Data visualization, experimentation
- Transferable: Domain knowledge, stakeholder management

**Plan Execution**:
- Months 1-4: Python + SQL courses, statistics fundamentals
- Months 5-8: ML courses, 3 portfolio projects
- Months 9-10: Applied to Junior Data Scientist / Analytics roles
- Months 11-12: Interviewed, accepted offer (40% pay cut for field entry)

**Result**: Successful pivot, now Data Scientist at tech company

**Key Success Factors**:
- Realistic timeline (12 months for fundamentals)
- Strong portfolio (compensated for lack of formal background)
- Leveraged transferable skills (business context, communication)
- Accepted bridge role (junior level to enter field)

### Example 3: Job Search Optimization (3 months to offer)

**Starting Point**:
- Mid-level engineer, laid off, need job quickly
- Good skills, poor job search strategy
- Applying online only, low response rate (5%)

**Optimization**:
- Week 1-2: Resume review, optimize for ATS, add metrics
- Week 3-4: Activate network, request 10 referrals
- Week 5-8: Apply 8/week (50% referral, 50% online)
- Week 9-12: Interview prep (LeetCode, system design), 15 interviews

**Results**:
- 60 applications total
- Response rate: 25% (15/60)
- 15 phone screens → 8 technical → 4 onsite → 2 offers
- Accepted offer after negotiation (+15% from initial)

**Key Success Factors**:
- Referrals dramatically improved response rate
- Consistent application velocity (8/week)
- Strong interview prep (technical + behavioral)
- Negotiated both offers (leveraged competition)

## Future Enhancements

Planned features:
- **AI-powered skill recommendations** based on job market trends
- **Automated LinkedIn profile optimization** from skill development
- **Resume auto-generation** from portfolio and accomplishments
- **Interview question generator** based on target role
- **Salary benchmarking API integration** (real-time market data)
- **Network health scoring** (relationship quality metrics)
- **Job search automation** (auto-apply with customized materials)
- **Career trajectory modeling** (predict path to goal)

## Support & Resources

### Documentation
- [Comprehensive skill library](skills/career-development/SKILL.md)
- [Template examples](templates/)
- [Agent definitions](agents/)

### Community Resources
- r/cscareerquestions (Reddit)
- Blind (anonymous tech professionals)
- LinkedIn career development groups
- Industry-specific Slack/Discord communities

### Professional Services
- Career coaching (consider if pivoting or stuck)
- Resume review services
- Interview coaching (especially for FAANG)
- Executive recruiters (for senior roles)

## Contributing

This plugin is part of the Puerto marketplace. To contribute:
1. Fork the repository
2. Make improvements (better resources, additional frameworks)
3. Submit pull request with clear description
4. Follow existing patterns and structure

## License

MIT License - See main repository for details

---

**Take control of your career. Strategic planning + consistent execution = professional success.**

**Your career is your responsibility. Own it.**
