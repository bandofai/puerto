# Synthesis Skill

**Transform research data into actionable insights through systematic analysis**

This skill codifies proven techniques for analyzing qualitative and quantitative research data and generating insights that drive product decisions.

---

## Core Principles

1. **Let Data Speak**: Avoid confirmation bias; find patterns objectively
2. **Triangulate**: Validate findings across multiple data sources
3. **From Data to Insight**: Data describes what happened; insights explain why it matters
4. **Actionable Over Academic**: Focus on insights that inform decisions
5. **Show Your Work**: Make analysis transparent and traceable

---

## Synthesis Process Overview

### The 5-Stage Synthesis Framework

```
1. IMMERSION     → Familiarize yourself with all data
2. ORGANIZATION  → Structure and code data
3. ANALYSIS      → Identify patterns and themes
4. INSIGHT       → Connect findings to implications
5. COMMUNICATION → Present findings compellingly
```

---

## Stage 1: Immersion

### Goal: Deeply understand the raw data

**Activities**:
- Read all transcripts, notes, responses
- Watch session recordings
- Review quantitative data
- Note initial observations (but don't draw conclusions yet)

**Deliverables**:
- Data inventory (what you have)
- Initial observations list
- Questions raised by data

---

### Data Inventory Template

```markdown
## Data Inventory

### Research Overview
- **Study**: [Name]
- **Methods**: [Interviews, usability tests, surveys, etc.]
- **Timeline**: [Start - End dates]
- **Participants**: [N total, breakdown by segment]

### Data Sources

**Qualitative**:
- [ ] Interview transcripts: [N files]
- [ ] Usability test recordings: [N sessions]
- [ ] Session notes: [N documents]
- [ ] Observation notes: [N field visits]
- [ ] Open-ended survey responses: [N responses]

**Quantitative**:
- [ ] Survey responses: [N responses]
- [ ] Usability test metrics: [N participants × N tasks]
- [ ] Analytics data: [Date range, metrics]
- [ ] A/B test results: [Variants, sample sizes]

**Artifacts**:
- [ ] Screenshots of user behaviors
- [ ] Photos from field studies
- [ ] User-created artifacts (workarounds, etc.)

### Initial Read-Through Notes
[High-level observations, recurring themes, surprising findings]
```

---

### Immersion Best Practices

**DO**:
- ✅ Set aside dedicated time (no multitasking)
- ✅ Read/watch everything at least once
- ✅ Take notes on initial impressions
- ✅ Note questions or contradictions
- ✅ Look for patterns naturally emerging

**DON'T**:
- ❌ Jump to conclusions too quickly
- ❌ Cherry-pick data that supports assumptions
- ❌ Skip contradictory or negative findings
- ❌ Rush through this phase

**Time allocation**: Plan 30-60 minutes per hour of interview/session data

---

## Stage 2: Organization

### Goal: Structure data for analysis

**Activities**:
- Create coding framework
- Tag data with codes
- Group codes into categories
- Organize in affinity diagram

---

### Qualitative Coding

#### Open Coding (Bottom-Up)

**Purpose**: Identify concepts in the data without predetermined categories

**Process**:
1. Read through data line by line
2. Assign descriptive labels (codes) to meaningful segments
3. Use participants' own words when possible (in-vivo coding)
4. Create new codes as needed—don't force data into existing codes

**Example codes**:
- `time_pressure`
- `workaround_behavior`
- `terminology_confusion`
- `positive_feature_x`
- `frustration_navigation`
- `mobile_context`
- `collaboration_need`

**Tools**:
- Spreadsheet with columns: Quote | Code | Participant | Context
- Qualitative analysis software (Dovetail, Reframer, NVivo, Atlas.ti)
- Physical sticky notes (analog affinity mapping)

---

#### Axial Coding (Grouping Related Codes)

**Purpose**: Find relationships between codes and group into categories

**Process**:
1. Review all codes
2. Group related codes together
3. Name each group (category)
4. Define what makes each category distinct

**Example**:
```
Category: NAVIGATION ISSUES
├─ cant_find_settings
├─ unclear_menu_labels
├─ deep_hierarchy
└─ search_not_working

Category: ONBOARDING CHALLENGES
├─ unclear_value_prop
├─ skipped_tutorial
├─ first_task_unclear
└─ terminology_confusion

Category: POWER_USER_NEEDS
├─ keyboard_shortcuts_wanted
├─ bulk_actions_needed
├─ customization_desired
└─ advanced_features_hidden
```

---

#### Selective Coding (Identifying Themes)

**Purpose**: Identify overarching themes that tell a story

**Process**:
1. Review categories
2. Identify higher-level themes
3. Connect themes to research questions
4. Define each theme clearly

**Example**:
```
THEME 1: Information Architecture Fails First-Time Users
└─ Categories: Navigation Issues, Onboarding Challenges
└─ Evidence: 4/5 participants couldn't find settings, 60% task completion
└─ Implication: Redesign IA and navigation

THEME 2: Power Users Underutilize Advanced Features
└─ Categories: Power User Needs, Feature Discovery
└─ Evidence: 45% unaware of shortcuts, workarounds for existing features
└─ Implication: Improve feature discoverability and education
```

---

### Affinity Mapping

**Purpose**: Visualize patterns and relationships in qualitative data

**Process**:

1. **Write observations on sticky notes**
   - One observation per note
   - Include participant ID
   - Use direct quotes when powerful
   - Include behaviors, pain points, needs, positive reactions

2. **Group related notes**
   - Look for natural clusters
   - Move notes around as patterns emerge
   - No predetermined categories—let patterns emerge

3. **Label groups**
   - Give each cluster a descriptive name
   - Summarize what unites them

4. **Group clusters into themes**
   - Look for higher-level patterns
   - Create hierarchy (themes → categories → observations)

5. **Document relationships**
   - Draw connections between related groups
   - Note contradictions or tensions

**Visual structure**:
```
┌─────────────────────────────────────────────────┐
│ THEME: Users can't accomplish core tasks       │
├─────────────────────────────────────────────────┤
│                                                 │
│ ┌──────────────────┐  ┌──────────────────┐    │
│ │ CATEGORY:        │  │ CATEGORY:        │    │
│ │ Navigation       │  │ Terminology      │    │
│ │ confusion        │  │ unclear          │    │
│ ├──────────────────┤  ├──────────────────┤    │
│ │ • "Couldn't find │  │ • "What's sync?" │    │
│ │   settings" [P1] │  │   [P2]           │    │
│ │ • Clicked wrong  │  │ • Confused       │    │
│ │   menu 3× [P4]   │  │   workspace/     │    │
│ │ • Expected top   │  │   folder [P3]    │    │
│ │   right [P2,P5]  │  │                  │    │
│ └──────────────────┘  └──────────────────┘    │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Tools**:
- Physical: Sticky notes on wall
- Digital: Miro, Mural, FigJam, Dovetail

---

### Quantitative Data Organization

**Metrics to calculate**:

**Usability Testing**:
- Task completion rate (% who completed successfully)
- Time on task (average, median, range)
- Error rate (average errors per task)
- Satisfaction ratings (SUS, task-level ratings)
- Assistance required (% who needed help)

**Surveys**:
- Response rates
- Descriptive statistics (mean, median, mode)
- Distribution (histograms, frequency tables)
- Segmentation (compare groups)
- Correlation (relationships between variables)

**Analytics**:
- Conversion rates
- Drop-off points (funnel analysis)
- Time on page/in app
- Feature adoption rates
- Retention/churn rates

**Organize in tables and charts**:
```markdown
### Task Completion Rates

| Task | Success | Partial | Failed | Mean Time |
|------|---------|---------|--------|-----------|
| Create account | 100% (5/5) | 0% | 0% | 45s |
| Find settings | 60% (3/5) | 20% (1/5) | 20% (1/5) | 120s |
| Share document | 80% (4/5) | 0% | 20% (1/5) | 78s |
```

---

## Stage 3: Analysis

### Goal: Identify patterns, trends, and relationships

---

### Pattern Identification

**Look for**:

**Frequency**: How many participants mentioned this?
- "4 out of 5 participants couldn't find settings"
- Signal: If >50% of participants share experience, it's a pattern

**Intensity**: How strongly did they feel?
- Strong language: "This is incredibly frustrating"
- Non-verbal cues: Visible frustration, confusion
- Attempted workarounds: They care enough to find another way

**Consistency**: Does it appear across data sources?
- Mentioned in interviews AND failed in usability tests AND low ratings in survey
- Triangulation strengthens confidence

**Segments**: Does pattern vary by user type?
- "New users struggled, but experienced users had no issues"
- Signals different needs or missing onboarding

**Context**: When/where does this occur?
- "Only happens on mobile, not desktop"
- "Only when multitasking or in a hurry"

---

### Quantitative Analysis Techniques

#### Descriptive Statistics

**Central tendency**:
- Mean (average)—use when data is normally distributed
- Median (middle value)—use when there are outliers
- Mode (most common)—use for categorical data

**Variability**:
- Range (min to max)
- Standard deviation (how spread out)

**Example**:
```
Task 2 completion time:
- Mean: 120 seconds
- Median: 90 seconds
- Range: 45-300 seconds
- SD: 75 seconds

→ Insight: High variability suggests inconsistent experience
→ Some users breeze through, others really struggle
```

---

#### Comparative Analysis

**Compare groups**:
- New users vs. experienced users
- Mobile vs. desktop
- Segment A vs. Segment B
- Before vs. after (longitudinal)

**Example**:
```
SUS Score by User Type:
- New users: 62 (below average)
- Experienced users: 78 (above average)

→ Insight: Onboarding gap—new users struggle until they learn the system
```

---

#### Correlation Analysis

**Purpose**: Identify relationships between variables

**Example**:
```
Correlation between feature usage and satisfaction:
- Users who adopted feature X: NPS +45
- Users who didn't: NPS +10

→ Insight: Feature X is a key driver of satisfaction
→ Recommendation: Make feature X more discoverable
```

**Caution**: Correlation ≠ causation. Explore with qualitative follow-up.

---

### Mixed Methods Analysis (Triangulation)

**Purpose**: Validate findings across qualitative and quantitative data

**Process**:
1. Identify patterns in qualitative data
2. Check if quantitative data supports
3. Resolve discrepancies
4. Strengthen confidence in findings

**Example**:

**Qualitative**: 4/5 interview participants said navigation is confusing

**Quantitative**:
- 60% task completion (below 80% threshold)
- Mean time 120s (target was 45s)
- Survey: 42% rated navigation as "difficult"

**Triangulation**: Multiple data sources confirm navigation issue
→ **High confidence** in this finding

---

### Outlier Analysis

**Don't ignore outliers**—they can reveal important edge cases or unexpected user segments.

**Example**:
- 4 participants took 90-120s on Task 2
- 1 participant took 300s

**Investigate**:
- What was different about that participant?
- What path did they take?
- Does it reveal a usability issue or different use case?

---

## Stage 4: From Findings to Insights

### Understanding the Difference

**Finding** (what you observed):
- "4 out of 5 participants couldn't find the settings page"
- "Average task completion time was 120 seconds"
- "60% of users said they would recommend the product"

**Insight** (what it means + why it matters):
- "Users can't access critical functionality because settings are in an unconventional location, leading to frustration and support tickets"
- "The onboarding gap causes 38% of new users to churn in the first week because they don't understand the core value proposition"

---

### Insight Framework: So What? So What? So What?

**Purpose**: Transform observations into actionable insights

**Process**: For each finding, ask "So what?" three times

**Example**:
1. **Finding**: 60% of participants failed to complete Task 2
   - **So what?** → They can't access a key feature

2. **So what?** → They can't accomplish their goal
   - **So what?** → They might abandon the product

3. **So what?** → We lose users and revenue
   - **INSIGHT**: Poor discoverability of Feature X is a churn risk for new users, potentially costing $XXk in lost revenue annually

---

### Insight Quality Checklist

A good insight is:

- [ ] **Specific**: Not vague or general
  - ❌ "Users find the app confusing"
  - ✅ "Users can't find settings because it's not in the expected top-right location"

- [ ] **Evidence-based**: Supported by data
  - Include: participant quotes, metrics, frequency

- [ ] **Explains "why"**: Not just "what"
  - Goes beyond description to interpretation

- [ ] **Actionable**: Clear implications
  - Leads naturally to recommendations

- [ ] **Connected to goals**: Tied to business/product objectives
  - "This impacts retention" or "This affects conversion"

- [ ] **Surprising or non-obvious**: Not just confirming what everyone knows
  - If it's already known, document as "validation" not "insight"

---

### Insight Template

```markdown
## Insight: [Descriptive title]

**Finding**: [What you observed in data]

**Evidence**:
- [Quantitative data point]
- [Quote from participant] - [Participant ID]
- [Behavioral observation]
- [Frequency: N/N participants]

**Why it matters**:
[Connection to user goals and business goals]

**Impact**: [High/Medium/Low]
- [Specific impact on users]
- [Specific impact on business/product]

**Affected users**: [Segment, frequency]

**Recommendation**: [What should be done]
```

---

### Example Insight

```markdown
## Insight: Users Can't Discover Core Features Due to Unclear Navigation

**Finding**:
Majority of participants failed to locate settings and other key features within expected timeframe.

**Evidence**:
- 60% task completion rate (4% below 80% target)
- Average time to find settings: 120s (target: <45s)
- "I expected settings to be in the top right like every other app" - P2, P4, P5
- 3/5 participants clicked wrong menu before finding settings
- Survey: 42% rated navigation as "difficult" or "very difficult"

**Why it matters**:
Users can't access critical functionality needed to customize their experience and accomplish their goals. This creates frustration, increases support burden, and may lead to abandonment before users experience core value.

**Impact**: HIGH
- Users: Frustration, inefficiency, incomplete task completion
- Business: Increased support tickets (23% navigation-related), potential churn
- Estimated impact: If 40% of users struggle, ~10k users affected monthly

**Affected users**:
Primarily new and occasional users (daily users have learned locations)

**Recommendation**:
1. Move settings to conventional top-right position (industry standard)
2. Add visual icon to increase scannability
3. Include "Settings" in search autocomplete suggestions
4. Add first-time user tooltip highlighting settings location
```

---

## Stage 5: Synthesis Frameworks

### Jobs to Be Done (JTBD) Framework

**Purpose**: Understand the "job" users are hiring your product to do

**Template**:
```
When [situation], I want to [motivation], so I can [outcome]
```

**Example from research**:
```
When I'm managing multiple projects with tight deadlines,
I want to quickly see all tasks due this week across projects,
so I can prioritize and avoid missing deadlines.

→ Insight: Users need consolidated cross-project views, not just single-project task lists
```

---

### Journey Mapping

**Purpose**: Visualize user experience across touchpoints, highlighting pain points and opportunities

**Structure**:
| Phase | Actions | Thoughts | Emotions | Pain Points | Opportunities |
|-------|---------|----------|----------|-------------|---------------|

**Example from research**:
```markdown
## Journey: New User Activation

| Phase | Actions | Thoughts | Emotions | Pain Points | Opportunities |
|-------|---------|----------|----------|-------------|---------------|
| Discovery | Search for solution, read reviews | "Does this solve my problem?" | 🤔 Curious | Value prop unclear on website | Clarify unique benefits |
| Signup | Create account | "This is quick and easy" | 😊 Pleased | None identified | - |
| First use | Open app, see empty state | "What do I do now?" | 😕 Confused | No guidance or examples | Add contextual onboarding |
| Learning | Click around, try features | "I don't get it" | 😰 Frustrated | Tutorial was skippable and unclear | Interactive, progressive onboarding |
| Abandonment | Close app | "This is too complex" | 😞 Disappointed | Didn't experience core value | Better empty states with examples |
```

**Insights from journey**:
- Critical drop-off at "First use" phase
- Empty state is a missed opportunity to demonstrate value
- Need better progressive onboarding

---

### Persona Development (from research data)

**Purpose**: Represent key user segments with goals, behaviors, and pain points

**Data-driven persona template**:
```markdown
## Persona: [Name representing segment]

**Demographics**: [From research data]
- Age range: [From participant data]
- Occupation: [Most common in segment]
- Tech savviness: [Observed in research]

**Behavioral patterns**: [From interviews/observations]
- Frequency of use: [Daily/Weekly/Monthly]
- Context of use: [When/where they use product]
- Tools used: [Current solutions]

**Goals**: [From research data]
1. [Primary goal - from "Jobs to be Done"]
2. [Secondary goal]

**Frustrations**: [From pain points identified]
1. [Top frustration - quote from participant]
2. [Second frustration]

**Needs**: [From synthesis]
1. [Unmet need]
2. [Desired capability]

**Quote**: "[Characteristic quote from research that captures mindset]"

**Prevalence**: [% of user base this represents, if known]
```

---

## Prioritization of Insights

### Impact vs. Effort Matrix

**Purpose**: Prioritize recommendations

```
         HIGH IMPACT
         │
    P0   │   P1
  ───────┼───────
    P2   │   P3
         │
         LOW IMPACT

    LOW EFFORT → HIGH EFFORT
```

**Priority levels**:
- **P0**: High impact, low effort (QUICK WINS - do first)
- **P1**: High impact, high effort (BIG BETS - plan carefully)
- **P2**: Low impact, low effort (NICE TO HAVE - do if time)
- **P3**: Low impact, high effort (AVOID - not worth it)

---

### Severity Rating (for usability issues)

**Critical** (P0):
- Prevents task completion
- Affects majority of users (>50%)
- No workaround available
- Data loss or security risk

**High** (P1):
- Causes significant difficulty
- Affects many users (25-50%)
- Workaround exists but difficult
- Major impact on satisfaction

**Medium** (P2):
- Causes minor difficulty
- Affects some users (10-25%)
- Easy workaround exists
- Moderate impact on satisfaction

**Low** (P3):
- Cosmetic or rare issue
- Affects few users (<10%)
- Minimal impact on satisfaction

---

## Communication and Reporting

### Executive Summary Structure

**Keep to 1-2 pages**:

1. **Research overview** (2-3 sentences)
   - What was studied, how, and with whom

2. **Key findings** (3-5 bullet points)
   - Most critical insights only
   - Lead with impact, not methodology

3. **Top recommendations** (3-5 prioritized)
   - Specific, actionable, prioritized
   - Include expected impact

4. **Success metrics**
   - How to measure improvement

---

### Full Report Structure

See research report template for detailed structure. Key sections:

1. **Executive Summary**: High-level overview
2. **Research Overview**: Context, objectives, questions
3. **Methodology**: How research was conducted
4. **Participant Profile**: Who participated
5. **Key Findings**: Organized by theme
6. **Detailed Insights**: Evidence and implications
7. **Recommendations**: Prioritized actions
8. **Appendix**: Supporting materials

---

### Presentation Best Practices

**DO**:
- ✅ Lead with insights, not process
- ✅ Use participant quotes for impact
- ✅ Show visual evidence (screenshots, journey maps)
- ✅ Connect findings to business goals
- ✅ Prioritize recommendations clearly
- ✅ Be concise (assume limited attention span)
- ✅ End with clear next steps

**DON'T**:
- ❌ Lead with methodology details (save for appendix)
- ❌ Present every finding (prioritize top insights)
- ❌ Use jargon or research terminology
- ❌ Present problems without solutions
- ❌ Make recommendations without evidence

---

### Storytelling Framework

**Narrative structure** for presenting findings:

1. **Setup**: Current state and problem
   - "Users currently struggle to..."

2. **Evidence**: What you learned
   - "In our research, we found that 4 out of 5 users..."

3. **Impact**: Why it matters
   - "This is causing frustration and churn because..."

4. **Solution**: What should be done
   - "We recommend..."

5. **Expected outcome**: Future state
   - "This will improve [metric] by reducing [problem]"

---

## Quality Assurance for Synthesis

### Bias Check

**Confirmation bias**: Only finding what you expected?
- [ ] Have you actively looked for disconfirming evidence?
- [ ] Have you included contradictory findings?
- [ ] Did you adjust your hypothesis based on data?

**Availability bias**: Over-weighting recent or memorable examples?
- [ ] Have you systematically reviewed all data?
- [ ] Are you balancing memorable quotes with frequency data?

**Researcher bias**: Letting your opinions influence findings?
- [ ] Have you involved others in analysis?
- [ ] Can you trace insights back to evidence?
- [ ] Would another researcher reach similar conclusions?

---

### Validation Checklist

- [ ] Every insight is backed by specific evidence
- [ ] Evidence includes quotes, metrics, and frequency
- [ ] Findings answer original research questions
- [ ] Unexpected findings are highlighted
- [ ] Contradictions or nuances are acknowledged
- [ ] Recommendations are specific and actionable
- [ ] Impact is estimated or measurable
- [ ] Findings are validated across data sources (triangulation)
- [ ] Analysis is transparent and traceable

---

## Synthesis Tools and Templates

### Recommended Tools

**Qualitative analysis**:
- Dovetail (collaborative, user-friendly)
- Reframer (affinity mapping focused)
- Miro/Mural (flexible, visual)
- Airtable/Notion (structured, customizable)
- NVivo/Atlas.ti (academic-grade, complex)

**Quantitative analysis**:
- Excel/Google Sheets (basic stats)
- Tableau/Power BI (visualization)
- R/Python (advanced statistics)
- SPSS (academic research)

**Presentation**:
- Google Slides/PowerPoint
- Pitch/Keynote
- Notion (interactive docs)

---

### Time Allocation Guidelines

**For typical 5-participant study**:

- Immersion: 3-4 hours (read/watch everything)
- Coding: 4-6 hours (tag and categorize)
- Affinity mapping: 2-3 hours (group and theme)
- Analysis: 3-4 hours (identify patterns)
- Insight generation: 2-3 hours (connect to implications)
- Report writing: 4-6 hours (full report)
- Presentation creation: 2-3 hours (deck)

**Total**: ~20-30 hours for thorough synthesis

**Plan accordingly**: Synthesis takes as long or longer than data collection

---

## Common Synthesis Mistakes

### 1. Cherry-Picking Data
❌ **Mistake**: Only including findings that support your hypothesis
✅ **Fix**: Systematically review ALL data; include contradictions

### 2. Confusing Data with Insights
❌ **Mistake**: "60% of users failed Task 2" (that's data, not insight)
✅ **Fix**: "Users can't access critical features due to poor navigation, risking churn"

### 3. Presenting Findings Without Context
❌ **Mistake**: Listing observations without explaining why they matter
✅ **Fix**: Connect every finding to user impact and business goals

### 4. Vague Recommendations
❌ **Mistake**: "Improve navigation"
✅ **Fix**: "Move settings to top-right corner and add icon for scannability"

### 5. Analysis Paralysis
❌ **Mistake**: Over-analyzing data for weeks, delaying insights
✅ **Fix**: Set deadlines; perfect is the enemy of good enough

### 6. Ignoring Quantitative Context
❌ **Mistake**: "3 users mentioned X" (without saying how many total)
✅ **Fix**: "3 out of 5 users (60%) mentioned X"

### 7. Losing Participant Voice
❌ **Mistake**: Over-abstracting into themes without quotes
✅ **Fix**: Include powerful verbatim quotes to bring insights to life

---

## Advanced Synthesis Techniques

### Grounded Theory

**Purpose**: Build theory from data (not test existing theory)

**Process**:
1. Open coding (line-by-line)
2. Axial coding (relate codes)
3. Selective coding (core categories)
4. Theoretical sampling (collect more data to refine)
5. Theory development

**When to use**: Academic research, very exploratory studies

---

### Thematic Analysis (Braun & Clarke)

**6-phase process**:
1. Familiarization: Read data thoroughly
2. Coding: Systematic labeling
3. Theme development: Group codes into themes
4. Theme review: Check themes against data
5. Theme definition: Clearly define each theme
6. Report writing: Present themes with evidence

---

### Content Analysis

**Purpose**: Quantify qualitative data

**Example**:
- Count frequency of specific words/concepts
- Calculate percentage of participants mentioning each theme
- Compare frequency across segments

**When to use**: Large qualitative datasets, mixed methods

---

## Synthesis Checklist

**Before starting**:
- [ ] All data collected and organized
- [ ] Research questions clearly defined
- [ ] Time allocated for thorough analysis

**During synthesis**:
- [ ] Read/watch all data systematically
- [ ] Code data consistently
- [ ] Look for patterns across participants
- [ ] Triangulate across data sources
- [ ] Actively seek disconfirming evidence
- [ ] Involve others to reduce bias

**Insight quality**:
- [ ] Specific and evidence-based
- [ ] Explains "why," not just "what"
- [ ] Connected to business/product goals
- [ ] Actionable recommendations
- [ ] Prioritized by impact

**Communication**:
- [ ] Lead with insights, not methodology
- [ ] Use participant quotes effectively
- [ ] Visualize patterns (journey maps, affinity diagrams)
- [ ] Prioritize recommendations clearly
- [ ] Define success metrics

---

**Version**: 1.0
**Last Updated**: January 2025
**Based on**: Established qualitative and quantitative analysis methodologies
