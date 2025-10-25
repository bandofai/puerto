# Sales Lead Qualifier Plugin

> Professional sales lead qualification system with BANT/MEDDIC frameworks, intelligent scoring, data enrichment, and automated routing

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](plugin.json)
[![Model](https://img.shields.io/badge/model-sonnet-green.svg)](agents/sales-lead-qualifier.md)
[![Skill-Aware](https://img.shields.io/badge/skill--aware-yes-orange.svg)](skills/lead-qualification/SKILL.md)

## Overview

The **Sales Lead Qualifier** plugin provides a comprehensive, professional-grade lead qualification system for Claude Code. It enables sales teams to quickly qualify leads using proven frameworks (BANT, MEDDIC), enrich with company data, score and prioritize automatically, and route to the right reps—dramatically improving sales efficiency and pipeline quality.

### Key Features

✅ **BANT & MEDDIC Frameworks** - Industry-standard qualification methodologies
✅ **Intelligent Lead Scoring** - 0-140 point composite scoring system
✅ **Automated Data Enrichment** - Company and contact research via web search
✅ **Smart Prioritization** - P1-P5 priority levels with SLA recommendations
✅ **Automated Routing** - Route leads to the right rep based on criteria
✅ **CRM Integration** - Generate JSON/CSV data ready for import
✅ **Disqualification Handling** - Polite decline emails and proper documentation
✅ **Skill-Aware** - Reads qualification best practices before every task

---

## Components

### 🤖 Agent: `sales-lead-qualifier`

**File**: [`agents/sales-lead-qualifier.md`](agents/sales-lead-qualifier.md)

**Description**: Sales lead qualification specialist that scores leads using BANT or MEDDIC, enriches data via web search, prioritizes, and routes to appropriate sales reps.

**Configuration**:
- **Model**: Sonnet (requires sales judgment and web research)
- **Tools**: Read, Write, Edit, Bash, Grep, Glob, WebSearch
- **Skill-Aware**: Yes - MUST read lead qualification skill before tasks

**Responsibilities**:
- Lead scoring using BANT/MEDDIC frameworks
- Company and contact data enrichment
- Lead prioritization (P1-P5)
- Routing to appropriate sales reps
- CRM data entry automation
- Disqualification with polite feedback

---

### 📚 Skill: Lead Qualification Best Practices

**File**: [`skills/lead-qualification/SKILL.md`](skills/lead-qualification/SKILL.md)

**Contents**:
- **BANT Framework** - Budget, Authority, Need, Timeline (transactional sales)
- **MEDDIC Framework** - Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion (enterprise sales)
- **Lead Scoring System** - Qualification (100) + Fit (20) + Engagement (20) = 140 points
- **Enrichment Templates** - Company and contact research guides
- **Prioritization Rules** - P1-P5 levels with SLA and actions
- **Routing Logic** - Territory, size, industry, score-based routing
- **CRM Data Formats** - JSON, CSV, Markdown outputs
- **Disqualification Criteria** - When and how to disqualify
- **Question Banks** - 100+ discovery questions for BANT and MEDDIC

**Why Skill-Aware Matters**: The skill contains battle-tested frameworks from thousands of B2B sales scenarios. By reading the skill first, the agent ensures consistent, professional qualification that matches industry best practices.

---

## Installation

### User-Level Installation
Installs the plugin for all your projects:

```bash
# Create plugin directory
mkdir -p ~/.claude/plugins/sales-lead-qualifier

# Copy plugin files
cp -r plugins/sales-lead-qualifier/* ~/.claude/plugins/sales-lead-qualifier/

# Verify installation
ls ~/.claude/plugins/sales-lead-qualifier/
```

### Project-Level Installation
Installs the plugin for a specific project only:

```bash
# Create plugin directory in your project
mkdir -p .claude/plugins/sales-lead-qualifier

# Copy plugin files
cp -r plugins/sales-lead-qualifier/* .claude/plugins/sales-lead-qualifier/

# Add to version control (optional)
git add .claude/plugins/sales-lead-qualifier/
git commit -m "Add Sales Lead Qualifier plugin"
```

### Verify Installation

```bash
# Check that agent is available
ls ~/.claude/plugins/sales-lead-qualifier/agents/

# Check that skill is accessible
ls ~/.claude/plugins/sales-lead-qualifier/skills/lead-qualification/
```

---

## Usage

### Quick Start

The agent activates automatically when you request lead qualification tasks:

```
"Qualify this lead using BANT: Jane Smith, VP Engineering at TechCorp"
"Score these 50 webinar leads and prioritize them"
"Enrich this company: Acme Inc, acme.com"
"Route this lead to the right rep"
```

The agent will:
1. ✅ Read the lead qualification skill (mandatory)
2. ✅ Enrich company/contact data via web search
3. ✅ Apply BANT or MEDDIC framework
4. ✅ Calculate composite score (qualification + fit + engagement)
5. ✅ Assign priority level (P1-P5) with SLA
6. ✅ Route to appropriate sales rep
7. ✅ Generate CRM-ready outputs

---

## Features & Examples

### 1. BANT Qualification (Transactional Sales)

Use BANT for shorter sales cycles, SMB/mid-market, and transactional deals < $50K.

**Example Request**:
```
"Qualify this inbound demo request using BANT:
- Name: Sarah Chen
- Title: Director of Marketing
- Company: GrowthCo (200 employees, SaaS)
- Source: Demo form
- Message: 'We need better analytics for our marketing campaigns'"
```

**What You Get**:
- **Budget** (0-25): Scored based on signals and research
- **Authority** (0-25): Director level = likely influencer (15-20 points)
- **Need** (0-25): Pain around analytics = moderate to high need
- **Timeline** (0-25): Demo request = some urgency (15-20 points)
- **BANT Total**: 55-85/100
- **Fit Score**: Company size and industry match
- **Engagement Score**: Demo request = 5 points
- **Priority**: P2 or P3 depending on total score
- **Routing**: Assigned to Mid-Market AE in appropriate territory

**Output Location**: `./leads/growthco-bant-qualification.md`

---

### 2. MEDDIC Qualification (Enterprise Sales)

Use MEDDIC for complex sales cycles, enterprise deals > $100K, multiple stakeholders.

**Example Request**:
```
"Qualify this enterprise lead using MEDDIC:
- Contact: Michael Torres, VP of Engineering
- Company: Enterprise Tech Inc (5000 employees)
- Context: Exploring solutions for infrastructure modernization
- Budget: $500K mentioned in initial call"
```

**What You Get**:
- **Metrics** (0-20): ROI and measurable impact
- **Economic Buyer** (0-20): VP Eng likely has budget authority = 15-20
- **Decision Criteria** (0-15): Evaluation factors they'll use
- **Decision Process** (0-15): Steps to purchase, stakeholders
- **Identify Pain** (0-20): Infrastructure pain severity
- **Champion** (0-10): Internal advocate strength
- **MEDDIC Total**: Comprehensive score /100
- **Enrichment**: Company research, tech stack, recent news
- **Priority**: Likely P1 or P2 (enterprise + budget)
- **Routing**: Senior Enterprise AE

**Output Location**: `./leads/enterprisetech-meddic-qualification.md` + CRM data JSON

---

### 3. Company & Contact Enrichment

Research and enrich leads with firmographic, technographic, and strategic data.

**Example Request**:
```
"Enrich this company: Startup XYZ, website: startupxyz.com"
```

**Agent Process**:
1. **Web Search** for company website, About page, blog
2. **LinkedIn** company page research
3. **News search** for recent funding, growth, press releases
4. **Job boards** search for hiring signals (buying indicators)
5. **Tech stack** research (if relevant tools)

**What You Get**:
- **Firmographics**: Size, revenue, location, industry, founded date
- **Funding**: Stage, total raised, recent rounds, investors
- **Tech Stack**: Tools they use (CRM, marketing automation, etc.)
- **Recent News**: Funding, product launches, expansion
- **Job Postings**: Roles they're hiring (strong buying signals)
- **Strategic Initiatives**: Inferred from blog, job posts, news
- **ICP Fit Score**: How well they match your ideal customer profile

**Output Location**: `./leads/startupxyz-enrichment.md`

---

### 4. Lead Scoring & Prioritization

Score and prioritize leads using composite scoring system.

**Example Request**:
```
"I have 100 inbound leads from last month. Score and prioritize them."
```

**Scoring Formula**:
```
Total Score (0-140) = Qualification (0-100) + Fit (0-20) + Engagement (0-20)
```

**Priority Levels**:
| Score | Priority | Label | Action | SLA |
|-------|----------|-------|--------|-----|
| 100+ | P1 | Hot Lead | Immediate outreach, exec engagement | Same day |
| 75-99 | P2 | Warm Lead | Priority outreach, personalized | 24 hours |
| 50-74 | P3 | Qualified | Standard process | 48 hours |
| 25-49 | P4 | Long-term Nurture | Automated campaigns | Weekly |
| 0-24 | P5 | Disqualified | Polite decline or far-future | As needed |

**What You Get**:
- Prioritized lead list (sorted by score)
- P1 leads with detailed qualification reports
- Routing assignments by rep
- Summary stats (e.g., "15 P1, 30 P2, 40 P3, 15 P4/P5")

**Output Location**: `./leads/batch-scoring-2025-01.csv` + individual P1 reports

---

### 5. Lead Routing

Automatically route leads to the right sales rep based on multiple criteria.

**Example Request**:
```
"Route this lead: John Smith, CTO at BigCorp (10,000 employees), HQ in NYC"
```

**Routing Criteria**:
- **Company Size**: BigCorp = Enterprise (>1000 employees)
- **Geography**: NYC = East Coast territory
- **Title**: CTO = Technical buyer, enterprise deal
- **Score**: If high score → Senior rep

**Routing Logic**:
```
IF Score >= 100 AND Size = Enterprise
  → Senior Enterprise AE

ELSE IF Size >= 1000 employees
  → Enterprise AE for territory

ELSE IF Size = 100-1000
  → Mid-Market AE

ELSE IF Size < 100
  → SMB Rep
```

**What You Get**:
- **Assigned Rep**: "Sarah Johnson - Enterprise AE (East Coast)"
- **Rationale**: "Enterprise size, East Coast territory, technical buyer"
- **Next Steps**: Personalized outreach guidance
- **SLA**: Based on priority level

---

### 6. CRM Data Automation

Generate CRM-ready data in JSON or CSV format for bulk imports.

**Example Request**:
```
"Generate CRM data for this qualified lead in JSON format"
```

**JSON Output**:
```json
{
  "lead_id": "LEAD-12345",
  "contact": {
    "first_name": "Jane",
    "last_name": "Smith",
    "title": "VP of Engineering",
    "email": "jane.smith@company.com"
  },
  "company": {
    "name": "TechCorp Inc.",
    "size": 500,
    "industry": "SaaS"
  },
  "qualification": {
    "framework": "BANT",
    "score": 85,
    "priority": "P2"
  },
  "routing": {
    "assigned_to": "John Doe (Mid-Market AE)",
    "reason": "Territory, company size"
  }
}
```

**Use Cases**:
- Import into Salesforce, HubSpot, Pipedrive, etc.
- Automate lead assignment via API
- Sync with marketing automation platforms
- Generate reports and dashboards

---

### 7. Disqualification Handling

Politely disqualify leads that don't fit, with helpful alternatives.

**Example Request**:
```
"This lead is too small for us (5 employees, no budget). Disqualify with a polite email."
```

**What You Get**:
- **Disqualification Email**: Professional, helpful decline
- **Alternative Suggestions**: Recommend solutions better suited for their size
- **CRM Update**: Status = Disqualified, reason documented
- **Optional Nurture**: Add to long-term nurture list (check back in 12 months)

**Email Template** (from skill):
```
Subject: Re: [Solution] for [Company]

Hi [Name],

Thank you for your interest in [Solution]. After reviewing your needs,
I want to be upfront that we may not be the best fit at this time.

[Specific reason: e.g., "We specialize in mid-market companies (100-1000
employees), and you might find better value with solutions tailored for
smaller teams."]

I'd recommend checking out [Alternative 1] or [Alternative 2].

If your situation changes (e.g., you scale to 100+ employees), feel free
to reach out anytime.

Best of luck!
[Your Name]
```

---

## Document Structure

All outputs are organized in a clean structure:

```
./leads/
├── qualified/
│   ├── techcorp-bant-qualification.md
│   ├── enterprisetech-meddic-qualification.md
│   └── startupxyz-bant-qualification.md
├── enrichment/
│   ├── techcorp-enrichment.md
│   └── startupxyz-enrichment.md
├── batch-scoring/
│   ├── webinar-leads-2025-01.csv
│   └── p1-leads-detailed/
├── crm-data/
│   ├── lead-12345.json
│   ├── lead-12346.json
│   └── bulk-import-2025-01.csv
└── disqualified/
    ├── too-small-leads.md
    └── wrong-industry-leads.md
```

---

## Best Practices

### For Sales Reps

**Lead Qualification**:
- ✅ Qualify early (don't wait until late in sales cycle)
- ✅ Use BANT for transactional, MEDDIC for enterprise
- ✅ Document evidence for every score
- ✅ Disqualify quickly if poor fit (save time)
- ✅ Update qualification as you learn more
- ✅ Focus on P1/P2 leads first

**Enrichment**:
- ✅ Always enrich before first outreach
- ✅ Look for recent news and buying signals
- ✅ Check job postings (strong intent signal)
- ✅ Find personalization angles
- ✅ Validate contact title and authority

**Prioritization**:
- ✅ Work P1 leads same day
- ✅ Don't spend equal time on all leads
- ✅ Nurture P4 leads via automation
- ✅ Revisit P3 leads if they engage

---

### For Sales Operations

**Lead Routing**:
- ✅ Define clear routing criteria
- ✅ Balance rep workloads
- ✅ Route hot leads to senior reps
- ✅ Track routing effectiveness
- ✅ Adjust rules based on data

**CRM Hygiene**:
- ✅ Import qualified leads with complete data
- ✅ Standardize field formats
- ✅ Document qualification in notes
- ✅ Track disqualification reasons
- ✅ Regular data cleanup

**Performance Metrics**:
- ✅ Track qualification accuracy
- ✅ Monitor conversion by priority level
- ✅ Measure time to first response
- ✅ Analyze win rates by score
- ✅ Optimize routing logic

---

### For Sales Leaders

**Pipeline Quality**:
- ✅ Focus on quality over quantity
- ✅ Set standards for qualification
- ✅ Review P1 leads in pipeline reviews
- ✅ Coach reps on qualification
- ✅ Celebrate wins from well-qualified leads

**Resource Allocation**:
- ✅ Assign senior reps to P1 leads
- ✅ Use BDRs for P3 lead development
- ✅ Automate P4 nurture
- ✅ Disqualify P5 quickly

---

## Framework Comparison

### When to Use BANT vs. MEDDIC

**Use BANT When**:
- Transactional sales (< $50K)
- Shorter sales cycles (< 3 months)
- SMB and mid-market segments
- Clear product-market fit
- Simple buying process
- Single decision maker

**Use MEDDIC When**:
- Enterprise sales (> $100K)
- Complex sales cycles (> 3 months)
- Multiple stakeholders
- Technical evaluations and POCs
- Committee-based decisions
- Strategic, transformational deals

**Hybrid Approach**:
- Start with BANT for quick qualification
- Transition to MEDDIC for deals that grow in scope
- Use BANT for initial lead scoring, MEDDIC for deep qualification

---

## Integration with Sales Tools

### Salesforce Integration

```bash
# Export CRM data in Salesforce format
"Generate Salesforce CSV for these qualified leads"

# Fields mapped:
# - First Name, Last Name, Title, Email, Phone
# - Company, Website, Industry, Employees, Revenue
# - Lead Source, Lead Score, Priority
# - Owner (routing assignment)
# - Description (qualification summary)
```

### HubSpot Integration

```bash
# Export in HubSpot format
"Generate HubSpot CSV with lifecycle stage and lead score"

# Mapping:
# - Contact properties
# - Company properties
# - Custom properties for BANT/MEDDIC scores
# - Lifecycle stage based on priority
```

### API Integration

```json
// JSON format for API imports
{
  "leads": [
    {
      "contact": {...},
      "company": {...},
      "qualification": {...},
      "priority": "P1",
      "assigned_to": "rep@company.com"
    }
  ]
}
```

---

## Troubleshooting

### Agent doesn't activate automatically
**Solution**: Use explicit invocation:
```
"Use the sales-lead-qualifier agent to qualify this lead"
```

### Enrichment data is limited
**Cause**: Company has minimal online presence or private information.
**Solution**: Agent will document what's unavailable and flag for manual research.

### Scores seem too low/high
**Cause**: Incomplete information or different scoring expectations.
**Solution**: Review skill rubrics, provide more context, calibrate with team.

### Routing doesn't match expectations
**Cause**: Routing logic doesn't match your specific rules.
**Solution**: Customize routing rules in skill file (`.claude/skills/lead-qualification/SKILL.md`).

### Need to customize for industry
**Solution**: Copy skill to project level and add industry-specific criteria:
```bash
cp ~/.claude/plugins/sales-lead-qualifier/skills/lead-qualification/SKILL.md \
   .claude/skills/lead-qualification/SKILL.md

# Edit to add:
# - Industry-specific qualification questions
# - Custom scoring rubrics
# - Vertical-specific routing rules
```

---

## Customization

### Adapting to Your Sales Process

All templates in the skill can be customized:

```bash
# Copy skill to customize
cp ~/.claude/plugins/sales-lead-qualifier/skills/lead-qualification/SKILL.md \
   .claude/skills/lead-qualification/SKILL.md

# Customize for your company:
# - Adjust scoring rubrics
# - Add custom qualification criteria
# - Define your routing rules
# - Add industry-specific questions
# - Set your priority thresholds
```

**Priority**: Project-level skills override user-level, allowing per-company customization.

### Custom Routing Rules

Edit the skill to define your routing:

```markdown
## Custom Routing Rules

IF Company Size >= 1000 AND Score >= 90
  → Route to: Alice (Enterprise AE, West)

ELSE IF Industry = "Healthcare" AND Score >= 70
  → Route to: Bob (Healthcare Specialist)

ELSE IF Geography = "EU"
  → Route to: Carol (EMEA Team)

ELSE
  → Route to: Round-robin (US Team)
```

---

## Examples by Sales Segment

### For SDRs/BDRs

**Batch Qualification**:
```
"I have 200 inbound leads from a webinar. Score them using BANT and give me the top 20 to call."
```

**Quick Enrichment**:
```
"Enrich these 10 companies before my cold calls: [company list]"
```

**Disqualification**:
```
"This lead is a student. Write a polite disqualification email."
```

---

### For Account Executives

**Deep Qualification**:
```
"Qualify this enterprise opportunity using MEDDIC: [details]"
```

**Multi-Threaded Approach**:
```
"I have 3 contacts at BigCorp (CTO, VP Ops, Director IT). Assess authority and help me map the buying committee."
```

**Deal Review**:
```
"Re-score this opportunity. We've learned budget is confirmed ($200K) and timeline is end of quarter."
```

---

### For Sales Managers

**Pipeline Review**:
```
"Score all open opportunities in discovery stage and identify which should be fast-tracked."
```

**Resource Allocation**:
```
"Analyze our P1 leads and recommend which reps should get them based on territory and expertise."
```

**Win/Loss Analysis**:
```
"Review our lost deals last quarter. Were they properly qualified? What were common gaps?"
```

---

## Lead Qualification Resources

### Recommended Reading

**Books**:
- "The Sales Development Playbook" by Trish Bertuzzi
- "Predictable Revenue" by Aaron Ross
- "SPIN Selling" by Neil Rackham
- "The Challenger Sale" by Matthew Dixon

**Frameworks**:
- BANT (Budget, Authority, Need, Timeline)
- MEDDIC (Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion)
- CHAMP (Challenges, Authority, Money, Prioritization)
- GPCT (Goals, Plans, Challenges, Timeline)

### Industry Benchmarks

**Lead Response Times** (Harvard Business Review):
- Respond within 5 minutes → 21x more likely to qualify
- Respond within 1 hour → 7x more likely
- Respond within 24 hours → baseline

**Qualification Standards**:
- Top performers qualify out 50%+ of leads quickly
- Average qualification score for closed-won deals: 75-85/100
- P1 leads convert 5-10x better than P3

---

## FAQ

**Q: Can I use both BANT and MEDDIC on the same lead?**
A: Yes! Start with BANT for quick qualification, then deepen with MEDDIC for high-value opportunities.

**Q: How accurate is the web enrichment?**
A: The agent gathers publicly available information from company websites, LinkedIn, news, and job boards. Always validate critical information.

**Q: Can I import this data into my CRM?**
A: Yes! The agent generates JSON and CSV formats compatible with most CRMs (Salesforce, HubSpot, Pipedrive, etc.).

**Q: What if I disagree with the score?**
A: Review the evidence and rubrics in the skill. You can adjust scores based on additional context, or customize the rubrics in the skill file.

**Q: How do I handle leads from different industries?**
A: Customize the fit score criteria in the skill to weight your target industries higher.

**Q: Can I qualify leads in bulk?**
A: Yes! Provide a CSV or list of leads, and the agent will qualify, score, and prioritize all of them.

**Q: What about GDPR and data privacy?**
A: All enrichment uses publicly available information. Follow your company's data handling policies. Don't store sensitive data unnecessarily.

**Q: How often should I re-qualify?**
A: Re-qualify when you learn significant new information (budget confirmed, timeline changed, new stakeholder involved).

---

## Version History

**v1.0.0** (2025-01-19)
- Initial release
- BANT qualification framework
- MEDDIC qualification framework
- Lead scoring system (0-140 points)
- Company and contact enrichment via WebSearch
- Priority levels (P1-P5) with SLAs
- Lead routing logic
- CRM data generation (JSON, CSV)
- Disqualification handling
- Comprehensive skill library with question banks

---

## License

MIT License - See repository for full license text

---

## Support

**Issues & Bug Reports**: [GitHub Issues](https://github.com/bandofai/puerto/issues)

**Discussions**: [GitHub Discussions](https://github.com/bandofai/puerto/discussions)

**Documentation**: [Puerto Marketplace Docs](https://github.com/bandofai/puerto)

---

## Acknowledgments

Frameworks and best practices adapted from:
- The Bridge Group (Sales Development research)
- MEDDIC Academy (Enterprise sales methodology)
- SiriusDecisions (B2B demand generation research)
- Sales Hacker and Sales Gravy communities
- 1000+ B2B sales qualification scenarios

---

**Ready to qualify better leads faster?**

```bash
# Install the plugin
cp -r plugins/sales-lead-qualifier ~/.claude/plugins/

# Start using it
"Qualify this lead using BANT: Jane Smith, VP Engineering at TechCorp"
```

**Professional, consistent, effective lead qualification - every time.**
