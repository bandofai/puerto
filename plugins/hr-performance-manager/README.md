# HR Performance Manager Plugin

> Professional performance management system for employee reviews, goal setting, career development, 1-on-1s, and performance improvement plans

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](plugin.json)
[![Model](https://img.shields.io/badge/model-sonnet-green.svg)](agents/hr-performance-manager.md)
[![Skill-Aware](https://img.shields.io/badge/skill--aware-yes-orange.svg)](skills/performance-management/SKILL.md)

## Overview

The **HR Performance Manager** plugin provides a comprehensive, professional-grade performance management system for Claude Code. It enables managers, HR professionals, and team leaders to create high-quality performance reviews, set effective goals, develop career plans, conduct productive 1-on-1s, and manage performance improvement processes.

### Key Features

✅ **Performance Reviews** - Annual, mid-year, and quarterly reviews with structured templates
✅ **Goal Setting** - SMART goals and OKRs with alignment to company objectives
✅ **Career Development** - Comprehensive career planning and skills gap analysis
✅ **1-on-1 Templates** - Structured agendas for weekly, monthly, and skip-level meetings
✅ **Performance Improvement Plans** - Professional PIPs with legal compliance guidance
✅ **360-Degree Feedback** - Multi-perspective performance assessment
✅ **Competency Assessment** - Skills evaluation frameworks
✅ **Skill-Aware** - Reads performance management best practices before every task

---

## Components

### 🤖 Agent: `hr-performance-manager`

**File**: [`agents/hr-performance-manager.md`](agents/hr-performance-manager.md)

**Description**: Performance management specialist that creates professional HR documents following industry best practices.

**Configuration**:
- **Model**: Sonnet (requires judgment for performance evaluations)
- **Tools**: Read, Write, Edit, Bash, Grep, Glob
- **Skill-Aware**: Yes - MUST read performance management skill before tasks

**Responsibilities**:
- Prepare performance review materials
- Create goal-setting frameworks (SMART, OKRs)
- Develop career development plans
- Generate 1-on-1 meeting templates
- Draft performance improvement plans
- Design 360-degree feedback processes
- Assess competencies and skills

---

### 📚 Skill: Performance Management Best Practices

**File**: [`skills/performance-management/SKILL.md`](skills/performance-management/SKILL.md)

**Contents**:
- **Performance Review Process** - Complete review templates with rating scales
- **Goal Setting Frameworks** - SMART goals and OKRs with examples
- **Career Development Planning** - Skills assessment and growth roadmaps
- **1-on-1 Meeting Templates** - Weekly, monthly, career-focused, skip-level
- **Performance Improvement Plans** - Formal PIP templates with legal guidance
- **360-Degree Feedback** - Request forms, assessment surveys, summary reports
- **Competency Assessment** - Behavioral frameworks and proficiency levels
- **Performance Metrics** - Quantitative and qualitative indicators
- **Best Practices** - DO/DON'T guidance for each area

**Why Skill-Aware Matters**: The skill contains 50+ templates and frameworks battle-tested across thousands of performance management scenarios. By reading the skill first, the agent ensures every document follows professional HR standards, legal compliance best practices, and evidence-based approaches.

---

## Installation

### User-Level Installation
Installs the plugin for all your projects:

```bash
# Create plugin directory
mkdir -p ~/.claude/plugins/hr-performance-manager

# Copy plugin files
cp -r plugins/hr-performance-manager/* ~/.claude/plugins/hr-performance-manager/

# Verify installation
ls ~/.claude/plugins/hr-performance-manager/
```

### Project-Level Installation
Installs the plugin for a specific project only:

```bash
# Create plugin directory in your project
mkdir -p .claude/plugins/hr-performance-manager

# Copy plugin files
cp -r plugins/hr-performance-manager/* .claude/plugins/hr-performance-manager/

# Add to version control (optional)
git add .claude/plugins/hr-performance-manager/
git commit -m "Add HR Performance Manager plugin"
```

### Verify Installation

```bash
# Check that agent is available
ls ~/.claude/plugins/hr-performance-manager/agents/

# Check that skill is accessible
ls ~/.claude/plugins/hr-performance-manager/skills/performance-management/
```

---

## Usage

### Quick Start

The agent activates automatically when you request performance management tasks. Simply describe what you need:

```
"Help me prepare an annual performance review for Sarah Chen"
"Create Q1 goals for my team using the OKR framework"
"I need a career development plan for Alex who wants to move into management"
"Generate a 1-on-1 template for my weekly check-ins"
```

The agent will:
1. ✅ Read the performance management skill (mandatory)
2. ✅ Ask clarifying questions to gather context
3. ✅ Use the appropriate template from the skill
4. ✅ Create a professional, complete document
5. ✅ Save it to an organized location
6. ✅ Provide guidance on next steps

---

## Features & Examples

### 1. Performance Reviews

Create comprehensive performance reviews with ratings, evidence, and development plans.

**Example Request**:
```
"Help me prepare an annual performance review for Sarah Chen, Senior Software Engineer.
She's been with us for 2 years, consistently delivers high-quality work, and is ready
for more leadership opportunities."
```

**What You Get**:
- Complete review document with all sections filled out
- Performance ratings based on competency framework
- Goal achievement assessment with evidence
- Strengths and development areas
- Career development discussion
- Goals for next review period
- Professional, objective language

**Output Location**: `./performance-management/sarah-chen-annual-review-2025.md`

---

### 2. Goal Setting (SMART & OKRs)

Set effective goals using SMART criteria or OKR framework, aligned with company objectives.

**Example Request (SMART Goals)**:
```
"Create Q1 goals for my engineering team. We need to improve system reliability
and increase test coverage. The team has 5 engineers."
```

**Example Request (OKRs)**:
```
"Help me set OKRs for our product team for 2025. Our company objective is to
become the most trusted platform in our industry."
```

**What You Get**:
- **SMART Goals**: Specific, Measurable, Achievable, Relevant, Time-bound goals
- **OKRs**: Inspiring objectives with measurable key results
- Goal alignment cascade (company → team → individual)
- Progress tracking milestones
- Success criteria and metrics

**Output Location**: `./performance-management/q1-2025-engineering-goals.md`

---

### 3. Career Development Plans

Create comprehensive career development plans with skills assessment, gap analysis, and action plans.

**Example Request**:
```
"Create a career development plan for Alex Rodriguez. He's currently a Senior Engineer
and wants to transition to Engineering Manager within the next 18 months."
```

**What You Get**:
- Current state skills assessment
- Career aspiration documentation (IC vs management track)
- Skills gap analysis for target role
- Development objectives with action plans
- Training and mentorship recommendations
- Timeline with quarterly milestones
- Success metrics

**Output Location**: `./performance-management/alex-rodriguez-career-plan.md`

---

### 4. 1-on-1 Meeting Templates

Generate structured templates for different types of 1-on-1 meetings.

**Example Request**:
```
"Create a template for my weekly 1-on-1s with my team. I want to cover progress,
blockers, and leave time for career development discussions."
```

**Available Templates**:
- **Weekly/Biweekly Check-ins** - Progress, priorities, feedback
- **Monthly Career 1-on-1s** - Development focus, growth discussions
- **Skip-Level 1-on-1s** - Employee feedback to senior leadership

**What You Get**:
- Structured agenda with time allocations
- Discussion prompts for each section
- Action item tracking
- Follow-up mechanisms

**Output Location**: `./performance-management/weekly-1-on-1-template.md`

---

### 5. Performance Improvement Plans (PIPs)

Create professional PIPs with clear expectations, support plans, and legal compliance.

**Example Request**:
```
"I need to create a PIP for a team member who's consistently missing deadlines
and producing work that requires significant rework."
```

**⚠️ IMPORTANT**: The agent will remind you to **consult HR before initiating a PIP**. PIPs have legal implications and should always be reviewed by HR.

**What You Get**:
- Specific, documented performance concerns
- Clear, measurable success criteria
- Support and resources provided
- Weekly check-in structure
- Progress tracking mechanism
- Consequences and outcomes clearly stated
- Legal compliance language

**Output Location**: `./performance-management/pip-[name]-[date].md`

---

### 6. 360-Degree Feedback

Design comprehensive 360-degree feedback processes with forms and summary reports.

**Example Request**:
```
"Set up a 360 feedback process for our senior engineers. I need request emails,
feedback forms, and a template for the summary report."
```

**What You Get**:
- Professional feedback request templates
- Comprehensive feedback forms (competency ratings + open-ended)
- Anonymous aggregation guidelines
- Summary report template with theme analysis
- Start/Stop/Continue framework
- Development recommendations

**Output Location**: `./performance-management/360-feedback-[name]/`

---

## Document Structure

All documents are saved in a structured, organized format:

```
./performance-management/
├── reviews/
│   ├── sarah-chen-annual-review-2025.md
│   ├── john-doe-midyear-review-2025.md
│   └── quarterly-reviews/
├── goals/
│   ├── q1-2025-engineering-goals.md
│   ├── 2025-okrs-product-team.md
│   └── individual-goals/
├── career-plans/
│   ├── alex-rodriguez-career-plan.md
│   └── development-plans/
├── 1-on-1s/
│   ├── weekly-1-on-1-template.md
│   ├── career-1-on-1-template.md
│   └── meeting-notes/
├── pips/
│   ├── pip-employee-name-2025-01.md
│   └── progress-logs/
└── 360-feedback/
    ├── sarah-chen-360/
    │   ├── feedback-request.md
    │   ├── feedback-form.md
    │   └── summary-report.md
    └── templates/
```

---

## Best Practices

### For Managers

**Performance Reviews**:
- ✅ Prepare with specific examples and evidence
- ✅ Use the full rating scale (not everyone is "3")
- ✅ Balance positive and developmental feedback
- ✅ No surprises - feedback should be ongoing
- ✅ Make it a dialogue, not a monologue

**Goal Setting**:
- ✅ Align goals with team and company objectives
- ✅ Make goals challenging but achievable
- ✅ Review and adjust quarterly
- ✅ Mix results goals with development goals
- ✅ Celebrate wins throughout the year

**1-on-1s**:
- ✅ Hold them consistently (don't cancel)
- ✅ Let employee drive the agenda
- ✅ Listen more than you talk
- ✅ Follow up on action items
- ✅ Balance tactical and strategic topics

**Career Development**:
- ✅ Have career conversations quarterly
- ✅ Be transparent about paths and timelines
- ✅ Provide stretch assignments
- ✅ Support growth even outside your team
- ✅ Don't make promises you can't keep

---

### For HR Professionals

**Performance Cycles**:
- ✅ Provide clear timelines and expectations
- ✅ Train managers on effective reviews
- ✅ Calibrate ratings across teams for fairness
- ✅ Link performance to compensation transparently
- ✅ Track completion and quality

**PIPs & Legal Compliance**:
- ✅ Review all PIPs before employee presentation
- ✅ Ensure progressive discipline is documented
- ✅ Verify no discriminatory language or bias
- ✅ Confirm success criteria are achievable
- ✅ Document all conversations thoroughly

**360 Feedback**:
- ✅ Ensure anonymity is protected
- ✅ Aggregate feedback (minimum 3 responses per category)
- ✅ Focus on development, not punishment
- ✅ Train participants on giving constructive feedback
- ✅ Follow up with action plans

---

## Quality Standards

Every document created by this plugin meets these standards:

**Completeness**:
- [ ] All template sections filled out
- [ ] No placeholder text remains
- [ ] Specific examples and evidence provided
- [ ] Measurable criteria included

**Professionalism**:
- [ ] Objective, factual language
- [ ] Focuses on behaviors and outcomes, not personality
- [ ] Balanced perspective (strengths AND development)
- [ ] Professional tone throughout
- [ ] Proper formatting

**Actionability**:
- [ ] Clear next steps identified
- [ ] SMART goals for improvement
- [ ] Specific timelines and deadlines
- [ ] Resources and support stated
- [ ] Success criteria measurable

**Legal & HR Compliance**:
- [ ] No discriminatory language
- [ ] Job-related performance focus
- [ ] Documented with specific examples
- [ ] Progressive discipline followed (PIPs)
- [ ] HR reviewed (sensitive matters)

---

## Integration with HR Systems

This plugin creates Markdown documents that can be:

**Converted to Other Formats**:
```bash
# Convert to PDF
pandoc performance-review.md -o performance-review.pdf

# Convert to Word
pandoc performance-review.md -o performance-review.docx

# Convert to HTML
pandoc performance-review.md -o performance-review.html
```

**Imported to HR Systems**:
- Copy content into Workday, BambooHR, Namely, etc.
- Use as preparation material before entering in HRIS
- Maintain as backup documentation
- Share with employees via email or shared drives

**Version Controlled**:
```bash
# Track changes over time
git add performance-management/
git commit -m "Complete Q4 performance reviews"

# Review history
git log --follow performance-management/sarah-chen-annual-review-2025.md
```

---

## Troubleshooting

### Agent doesn't activate automatically
**Solution**: Use explicit invocation or include trigger words:
```
"Use the hr-performance-manager agent to create a performance review"
```

### Skill not being read
**Verification**:
```bash
# Check skill exists
ls ~/.claude/plugins/hr-performance-manager/skills/performance-management/SKILL.md

# Or for project-level
ls .claude/plugins/hr-performance-manager/skills/performance-management/SKILL.md
```

**Solution**: Ensure Read tool is available and path is correct.

### Documents have placeholder text
**Cause**: Agent needs more context to fill in specific details.

**Solution**: Provide comprehensive information upfront:
- Employee name, role, department
- Review period or timeline
- Specific examples and performance data
- Previous goals and progress
- Career aspirations

### PIP concerns
**Always**: Consult HR before initiating a PIP. The agent will remind you, but this cannot be overstated. PIPs have legal implications.

---

## Customization

### Adapting Templates

All templates in the skill can be customized for your organization:

```bash
# Copy skill to customize
cp ~/.claude/plugins/hr-performance-manager/skills/performance-management/SKILL.md \
   .claude/skills/performance-management/SKILL.md

# Edit to add company-specific:
# - Rating scales
# - Competency frameworks
# - Goal templates
# - Policy references
# - Legal language
```

**Priority**: Project-level skills override user-level skills, allowing per-company customization.

### Adding Company Policies

Edit the skill file to reference your specific policies:

```markdown
## Company-Specific Policies

**Performance Review Cycle**: [Your company's cycle]
**Rating Scale**: [Your company's scale]
**Compensation Link**: [How performance affects pay]
**Promotion Criteria**: [Your promotion standards]
**PIP Process**: [Your progressive discipline policy]
```

---

## Examples by Role

### For Engineering Managers

**Performance Review for Software Engineer**:
```
"Create an annual review for Jamie, Senior Software Engineer. Key achievements:
Led migration to microservices (3 months ahead of schedule), mentored 2 junior
engineers, code quality improved (defect rate down 40%). Development area:
Sometimes takes on too much and misses deadlines. Career goal: Principal Engineer
or Staff Engineer path."
```

**Technical OKRs**:
```
"Set OKRs for engineering team. Company objective: Improve product reliability.
Team has 8 engineers working on backend services handling 10M requests/day."
```

---

### For Sales Managers

**Performance Review for Account Executive**:
```
"Annual review for Taylor, Account Executive. Achieved 120% of quota ($1.2M vs
$1M target), average deal size up 35%, but win rate declined from 25% to 18%.
Excellent at prospecting, needs improvement in closing skills. Wants to move
into enterprise sales."
```

**Sales Goals**:
```
"Create Q1 SMART goals for sales team. Focus on improving win rate and average
deal size while maintaining activity levels. Team of 5 AEs, quota is $250K each
per quarter."
```

---

### For Product Managers

**Performance Review for Product Manager**:
```
"Mid-year review for Morgan, Product Manager. Successfully launched 3 major
features with high user adoption. Strong stakeholder management and user research.
Development area: Technical depth - sometimes relies too heavily on engineering
for feasibility assessments. Aspires to Senior PM."
```

**Product OKRs**:
```
"Set OKRs for product team aligned with company goal to increase user engagement.
Current DAU is 50K, want to grow to 75K. Team manages mobile app and web platform."
```

---

### For HR Business Partners

**Career Development for High-Potential Employee**:
```
"Create a development plan for Casey, identified as high-potential future leader.
Currently Director of Marketing, being groomed for VP role in 2-3 years. Needs:
P&L experience, board presentation skills, strategic planning at company level."
```

**360 Feedback for Leadership Team**:
```
"Set up 360 feedback for our VP of Engineering. Include feedback from: CEO, peer
VPs (4), direct reports (8), key cross-functional partners (3). Focus on leadership
competencies and strategic impact."
```

---

## Performance Management Resources

### Recommended Reading

**Books**:
- "Radical Candor" by Kim Scott - Caring personally while challenging directly
- "The Effective Manager" by Mark Horstman - Practical management fundamentals
- "Measure What Matters" by John Doerr - OKR framework from Intel and Google
- "Thanks for the Feedback" by Stone & Heen - Receiving and giving feedback

**Articles**:
- Harvard Business Review - Performance Management section
- SHRM (Society for Human Resource Management) resources
- Manager Tools podcast and resources

### Legal Considerations

**Always Consult Legal/HR For**:
- Performance improvement plans (PIPs)
- Termination decisions
- Discrimination concerns
- ADA, FMLA, or other legal accommodations
- Sensitive performance issues

**Documentation Best Practices**:
- Use objective, behavior-based language
- Include specific examples with dates
- Focus on job-related performance
- Be consistent in standards across employees
- Keep all performance records confidential

---

## Contributing

Found a way to improve the performance management templates? Have suggestions for additional frameworks?

**How to Contribute**:
1. Fork the repository
2. Update the skill file: `skills/performance-management/SKILL.md`
3. Test with real performance management scenarios
4. Submit pull request with examples
5. Describe what was improved and why

**Areas for Contribution**:
- Industry-specific competency frameworks (tech, sales, marketing, etc.)
- International performance management practices
- Accessibility and inclusion best practices
- Remote/hybrid work performance considerations
- Emerging performance management trends

---

## FAQ

**Q: Can this replace our HRIS/performance management system?**
A: No, this is a preparation and documentation tool. It helps you create high-quality content that you'll typically copy into your official HR system.

**Q: Is the agent trained on our company's specific policies?**
A: By default, no. However, you can customize the skill file to include your company-specific policies, rating scales, and processes.

**Q: How do I ensure legal compliance?**
A: The templates include HR best practices and legal considerations, but always have HR and/or Legal review sensitive documents (especially PIPs and terminations).

**Q: Can I use this for remote/distributed teams?**
A: Yes! The templates work for any team structure. The skill includes guidance for remote employee reviews.

**Q: What about confidentiality?**
A: All performance documents are stored locally on your system. Follow your company's data security policies for storing and sharing sensitive employee information.

**Q: Can I modify the templates?**
A: Absolutely! Copy the skill to your project (`.claude/skills/`) and customize as needed. Project-level skills override user-level skills.

**Q: How often should I use this?**
A:
- **Performance reviews**: Annually or semi-annually
- **Goal setting**: Quarterly or annually
- **1-on-1s**: Weekly or biweekly
- **Career development**: Annually with quarterly check-ins
- **PIPs**: As needed (but hopefully rarely)

**Q: Does this work for all seniority levels?**
A: Yes! Templates adapt from entry-level to executive roles. Adjust competency expectations for the level.

---

## Version History

**v1.0.0** (2025-01-19)
- Initial release
- Performance review templates (annual, mid-year, quarterly)
- Goal setting frameworks (SMART, OKRs)
- Career development planning
- 1-on-1 templates (weekly, monthly, skip-level)
- Performance improvement plans (PIPs)
- 360-degree feedback processes
- Competency assessment frameworks
- Comprehensive skill library with 50+ templates

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

Templates and frameworks adapted from:
- Society for Human Resource Management (SHRM) best practices
- "Radical Candor" management philosophy
- Google's re:Work research on effective management
- Manager Tools performance management methodology
- OKR frameworks from Intel, Google, and modern tech companies
- 500+ real-world performance management scenarios

---

**Ready to elevate your performance management?**

```bash
# Install the plugin
cp -r plugins/hr-performance-manager ~/.claude/plugins/

# Start using it
"Help me prepare quarterly performance reviews for my team"
```

**Professional, consistent, effective performance management - every time.**
