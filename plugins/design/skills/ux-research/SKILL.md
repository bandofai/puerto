# UX Research

**User research methodologies and insights synthesis**

# Research Methods Skill

**Comprehensive guide to UX research methodologies and when to use each method**

This skill codifies best practices from hundreds of successful UX research projects across discovery, validation, and optimization phases.

---

## Core Principles

1. **Match Method to Question**: Choose research methods based on what you need to learn, not what's trendy
2. **Triangulate**: Use multiple methods to validate findings and reduce bias
3. **Include Users Early and Often**: Research throughout the product lifecycle, not just at the beginning
4. **Balance Qual and Quant**: Qualitative explores "why," quantitative measures "how much"
5. **Ethical Research Always**: Respect participant time, privacy, and dignity

---

## Research Method Selection Framework

### The 2x2 Framework: Attitudinal vs. Behavioral, Qualitative vs. Quantitative

```
                    QUALITATIVE                 QUANTITATIVE
                    (Why/How)                   (How many/much)
              ┌─────────────────────┬──────────────────────────┐
              │                     │                          │
ATTITUDINAL   │  • Interviews       │  • Surveys               │
(What people  │  • Focus Groups     │  • Card Sorting (quant)  │
say)          │  • Diary Studies    │  • A/B Tests (attitudes) │
              │                     │  • Analytics (stated)    │
              ├─────────────────────┼──────────────────────────┤
              │                     │                          │
BEHAVIORAL    │  • Usability Tests  │  • Analytics             │
(What people  │  • Field Studies    │  • A/B Tests             │
do)           │  • Contextual Inq.  │  • Heatmaps/Click tracks │
              │  • Task Analysis    │  • Performance Metrics   │
              │                     │                          │
              └─────────────────────┴──────────────────────────┘
```

### When to Use Each Quadrant

**Attitudinal + Qualitative**: Understanding motivations, perceptions, mental models
- "Why do users prefer X over Y?"
- "What do users think about this concept?"

**Attitudinal + Quantitative**: Measuring opinions at scale
- "How satisfied are users with feature X?"
- "How many users would pay for premium tier?"

**Behavioral + Qualitative**: Understanding how users interact and why
- "How do users currently accomplish task X?"
- "What workarounds do users create?"

**Behavioral + Quantitative**: Measuring what users do at scale
- "What percentage of users complete onboarding?"
- "Which features are used most frequently?"

---

## Research Methods by Purpose

### 1. GENERATIVE RESEARCH (Discovery & Exploration)

**Goal**: Understand user needs, contexts, and problems before defining solutions

#### User Interviews
**Best for**: Deep understanding of motivations, attitudes, experiences

**When to use**:
- Beginning of project to understand problem space
- Exploring new market or user segment
- Understanding "why" behind behaviors

**Pros**:
- Rich, deep insights
- Flexibility to explore unexpected topics
- Can uncover unarticulated needs

**Cons**:
- Time-consuming (typically 45-90 min per interview)
- Small sample size (5-12 participants)
- Susceptible to social desirability bias

**Sample size**: 5-12 participants per user segment

**Typical questions**:
- "Tell me about the last time you..."
- "Walk me through how you..."
- "What's most important to you when..."

---

#### Contextual Inquiry / Field Studies
**Best for**: Observing users in their natural environment

**When to use**:
- Understanding workflow in complex environments
- Observing actual behavior (not self-reported)
- Discovering workarounds and adaptations

**Pros**:
- Observe real behavior in context
- See environmental factors affecting use
- Discover unarticulated needs

**Cons**:
- Very time-intensive
- Logistically complex (travel, access)
- Can be intrusive to participants

**Sample size**: 4-8 site visits

**Process**:
1. Shadow user in their environment
2. Observe tasks and workflows
3. Ask questions about what you observe
4. Document context (photos, notes)

---

#### Diary Studies
**Best for**: Understanding behaviors and experiences over time

**When to use**:
- Behaviors that occur sporadically
- Understanding context of use over time
- Capturing in-the-moment experiences

**Pros**:
- Captures real-time experiences (less recall bias)
- Shows patterns over time
- Less researcher time than shadowing

**Cons**:
- Participant burden (compliance issues)
- Self-reported data
- Can take weeks to complete

**Sample size**: 10-20 participants over 1-4 weeks

**Tools**: Mobile apps (dscout, Indeemo), photo journals, SMS surveys

---

#### Surveys (Exploratory)
**Best for**: Identifying patterns and priorities across large populations

**When to use**:
- Need to understand frequency of behaviors
- Want to segment users
- Validate interview findings at scale

**Pros**:
- Large sample sizes
- Statistically significant results
- Cost-effective per response

**Cons**:
- Can't explore "why" deeply
- Response bias
- No opportunity to clarify answers

**Sample size**: Minimum 100 for basic analysis, 300+ for segmentation

**Question types**:
- Multiple choice for quantification
- Likert scales for attitudes
- Open-ended for unexpected insights (limited)

---

### 2. EVALUATIVE RESEARCH (Testing & Validation)

**Goal**: Test designs, concepts, or products to identify issues and validate solutions

#### Usability Testing (Moderated)
**Best for**: Identifying usability issues and understanding user behavior with product

**When to use**:
- Testing prototypes or live products
- Evaluating specific flows or features
- Before major product launches

**Pros**:
- Identifies specific usability issues
- Can probe to understand "why"
- Flexible to explore unexpected findings

**Cons**:
- Artificial environment (not real context)
- Moderator bias possible
- Time-consuming

**Sample size**: 5 users per user segment (finds ~85% of issues per Nielsen)

**Process**:
1. Give user realistic task scenarios
2. Ask them to think aloud
3. Observe struggles and successes
4. Measure time, errors, completion

**Metrics**:
- Task completion rate
- Time on task
- Error rate
- Satisfaction ratings (post-task)

---

#### Usability Testing (Unmoderated Remote)
**Best for**: Quick feedback on specific tasks at scale

**When to use**:
- Need results quickly
- Testing simple, linear flows
- Want larger sample size

**Pros**:
- Fast turnaround (hours, not weeks)
- Larger sample sizes
- Lower cost per participant

**Cons**:
- Can't ask follow-up questions
- Limited to simple tasks
- No way to clarify misunderstandings

**Sample size**: 15-30 participants

**Tools**: UserTesting, Maze, UserZoom

---

#### A/B Testing
**Best for**: Comparing two design alternatives with real users

**When to use**:
- Have two viable design options
- Need to measure impact on key metrics
- Have sufficient traffic for significance

**Pros**:
- Measures real behavior (not stated preferences)
- Statistically significant results
- Removes opinion-based decisions

**Cons**:
- Requires traffic volume
- Can only test one variable at a time
- Doesn't explain "why" variant won

**Sample size**: Depends on baseline conversion and desired lift (use calculator)

**Metrics**: Conversion rate, click-through rate, time on page, revenue

---

#### Concept Testing
**Best for**: Validating ideas before building them

**When to use**:
- Early stage, before detailed design
- Choosing between multiple concepts
- Validating value proposition

**Pros**:
- Fail fast and cheap
- Can test multiple concepts
- Provides direction for design

**Cons**:
- Reactions to concept ≠ actual usage
- Risk of overvaluing stated intent
- Hard to imagine new paradigms

**Sample size**: 8-15 for qualitative, 100+ for quantitative

**Methods**: Show concept (sketches, storyboards, mockups), gather reactions

---

#### Card Sorting
**Best for**: Testing or creating information architecture

**When to use**:
- Designing navigation structure
- Organizing content or features
- Understanding mental models of categorization

**Types**:
- **Open**: Users create and name categories
- **Closed**: Users sort into predefined categories
- **Hybrid**: Mix of both

**Pros**:
- User-centered IA
- Quantifiable results
- Easy to conduct remotely

**Cons**:
- Decontextualized from real use
- Only tests grouping, not findability
- Assumes users know all items

**Sample size**: 15-30 for open, 30+ for closed

**Tools**: Optimal Workshop, Maze, UserZoom

---

#### Tree Testing
**Best for**: Validating navigation structure

**When to use**:
- After creating IA (validates card sorting)
- Testing if users can find content
- Before visual design

**Pros**:
- Tests findability directly
- Quantifiable results
- Fast and cost-effective

**Cons**:
- No visual design context
- Text-only (misses visual cues)
- Limited to tree structures

**Sample size**: 50-100 participants

**Metrics**: Success rate, directness, time

---

### 3. ANALYTICS & BEHAVIORAL DATA

#### Web/Product Analytics
**Best for**: Understanding actual user behavior at scale

**When to use**:
- Identifying where users drop off
- Measuring feature adoption
- Tracking key metrics over time
- Generating hypotheses for research

**Pros**:
- Real behavior, not self-reported
- Large sample sizes
- Continuous monitoring

**Cons**:
- Doesn't explain "why"
- Privacy concerns
- Can be misinterpreted without context

**Key Metrics**:
- Acquisition: Where users come from
- Activation: Do they complete onboarding?
- Engagement: How often do they return?
- Retention: Do they stick around?
- Revenue: Do they pay?

**Tools**: Google Analytics, Mixpanel, Amplitude, Heap

---

#### Heatmaps & Session Recordings
**Best for**: Visualizing where users click, scroll, and focus attention

**When to use**:
- Optimizing page layouts
- Understanding confusion points
- Identifying ignored content

**Pros**:
- Visual and intuitive
- Shows aggregate patterns
- Can identify rage clicks (frustration)

**Cons**:
- Descriptive, not explanatory
- Can be over-interpreted
- Privacy concerns

**Tools**: Hotjar, Crazy Egg, FullStory

---

### 4. SPECIALIZED METHODS

#### Accessibility Testing
**Best for**: Ensuring product works for users with disabilities

**When to use**:
- Required for compliance (WCAG, ADA)
- Serving diverse user base
- Ethical product development

**Methods**:
- Automated testing (axe, WAVE, Lighthouse)
- Manual testing with assistive tech
- User testing with people with disabilities

**Sample size**: 3-5 users per disability type

---

#### Competitive Analysis
**Best for**: Understanding market landscape and best practices

**When to use**:
- Entering new market
- Benchmarking against competitors
- Identifying feature gaps

**Process**:
1. Identify competitors
2. Analyze key features, flows, pricing
3. Conduct comparative usability testing
4. Document strengths and weaknesses

---

#### Heuristic Evaluation
**Best for**: Expert review against usability principles

**When to use**:
- Quick assessment without users
- Budget/time constraints
- Before user testing to fix obvious issues

**Heuristics** (Nielsen's 10):
1. Visibility of system status
2. Match between system and real world
3. User control and freedom
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use
8. Aesthetic and minimalist design
9. Help users recognize, diagnose, and recover from errors
10. Help and documentation

**Evaluators**: 3-5 UX experts

---

## Research Method Selection Guide

### By Project Stage

**Discovery / Problem Definition**:
- User interviews
- Field studies / Contextual inquiry
- Diary studies
- Surveys (exploratory)
- Competitive analysis

**Ideation / Concept Validation**:
- Concept testing
- Participatory design workshops
- Card sorting (for IA)
- Surveys (concept preference)

**Design / Prototype Testing**:
- Usability testing (moderated)
- Tree testing
- First-click testing
- Heuristic evaluation

**Pre-Launch Validation**:
- Usability testing (unmoderated)
- Accessibility testing
- Beta testing
- A/B testing (if redesign)

**Post-Launch Optimization**:
- Analytics
- A/B testing
- Surveys (satisfaction)
- Session recordings
- Ongoing usability testing

---

### By Research Question Type

**"What do users need?"**
→ Interviews, field studies, diary studies

**"Will users understand this concept?"**
→ Concept testing, first-click tests

**"Can users complete this task?"**
→ Usability testing, task analysis

**"How many users experience this?"**
→ Surveys, analytics

**"Which design performs better?"**
→ A/B testing, preference testing

**"How satisfied are users?"**
→ Surveys (NPS, CSAT, SUS), interviews

**"How do we organize content?"**
→ Card sorting, tree testing

**"Is this accessible?"**
→ Accessibility testing, assistive tech testing

---

## Sample Size Guidelines

### Qualitative Research

**Interviews / Usability Tests**: 5-8 per user segment
- Diminishing returns after 5 (per Nielsen)
- If multiple distinct segments, 5 per segment
- For very simple products: 3-5 total
- For complex products: 8-12 total

**Field Studies**: 4-8 site visits
- Very time-intensive
- Smaller sample acceptable

**Diary Studies**: 10-20 participants
- Higher dropout rate
- Need larger initial sample

---

### Quantitative Research

**Surveys**:
- Exploratory: 100+ for basic insights
- Segmentation analysis: 300+
- Statistical modeling: 1000+

**A/B Tests**:
- Depends on baseline conversion rate and desired lift
- Typically need thousands of users per variant
- Use online calculator for specific estimates

**Card Sorting**:
- Open: 15-30
- Closed: 30-50

**Tree Testing**: 50-100

---

## Mixed Methods Approach

**Best practice**: Combine qualitative and quantitative for robust insights

### Example: Redesigning Checkout Flow

1. **Discover** (Qual): Interview 8 users about current checkout experience
   - Identify pain points and needs

2. **Validate** (Quant): Survey 300 users on identified pain points
   - Quantify how many experience each issue

3. **Test** (Qual): Usability test new design with 6 users
   - Identify usability issues

4. **Measure** (Quant): A/B test new design with live traffic
   - Measure impact on conversion

5. **Understand** (Qual): Interview users who abandoned new checkout
   - Understand why some still fail

This creates a complete picture: qualitative explains, quantitative measures.

---

## Common Research Mistakes to Avoid

### 1. Confirmation Bias
❌ **Mistake**: Only asking questions that support your hypothesis
✅ **Fix**: Include questions that could disprove your assumptions

### 2. Leading Questions
❌ **Mistake**: "Don't you think this design is confusing?"
✅ **Fix**: "What are your thoughts on this design?"

### 3. Hypothetical Questions
❌ **Mistake**: "Would you use this feature?"
✅ **Fix**: "Tell me about the last time you needed to [accomplish task]"

### 4. Treating Insights as Data
❌ **Mistake**: "5 users said X, so everyone must think X"
✅ **Fix**: "5/5 users experienced X (small sample, directional insight)"

### 5. Testing Too Late
❌ **Mistake**: Only testing after full build
✅ **Fix**: Test early with low-fidelity prototypes

### 6. Ignoring Negative Findings
❌ **Mistake**: Cherry-picking data that supports your design
✅ **Fix**: Report all findings, especially contradictory ones

### 7. Over-Researching
❌ **Mistake**: Endless research without action
✅ **Fix**: Define decision criteria upfront, research only to inform decision

### 8. Research Without Clear Objectives
❌ **Mistake**: "Let's do some user interviews and see what we find"
✅ **Fix**: "We need to understand [specific question] to decide [specific decision]"

---

## Ethical Research Guidelines

### Informed Consent
- [ ] Explain purpose of research clearly
- [ ] Explain how data will be used
- [ ] Explain recording and privacy practices
- [ ] Allow participant to opt out at any time
- [ ] Obtain explicit consent before proceeding

### Privacy and Confidentiality
- [ ] Anonymize participant data
- [ ] Secure storage of recordings and notes
- [ ] Delete personal information after analysis
- [ ] Don't share recordings outside research team
- [ ] Follow GDPR/privacy regulations

### Respectful Treatment
- [ ] Compensate participants fairly for time
- [ ] Don't make participants feel judged
- [ ] Accommodate accessibility needs
- [ ] Allow breaks and adjust pace
- [ ] Thank participants sincerely

### Vulnerable Populations
- [ ] Extra care with children, elderly, disabled
- [ ] May require guardian consent
- [ ] Trauma-informed approach for sensitive topics
- [ ] Have resources ready if distress occurs

---

## Research Planning Checklist

**Before Research**:
- [ ] Clear research questions defined
- [ ] Method(s) selected and justified
- [ ] Participant criteria specified
- [ ] Recruitment plan in place
- [ ] Materials prepared (guides, prototypes)
- [ ] Consent forms ready
- [ ] Recording setup tested
- [ ] Pilot test conducted

**During Research**:
- [ ] Follow protocol consistently
- [ ] Take detailed notes
- [ ] Record sessions (with consent)
- [ ] Note unexpected findings
- [ ] Debrief after each session
- [ ] Adjust if critical issues found

**After Research**:
- [ ] Analyze data systematically
- [ ] Identify patterns and themes
- [ ] Create actionable insights
- [ ] Prioritize recommendations
- [ ] Share findings with stakeholders
- [ ] Track implementation of recommendations

---

## Quick Reference: Method Selection Matrix

| If you need to... | Use this method |
|-------------------|----------------|
| Understand user needs before designing | Interviews, Field Studies |
| Test if users can complete a task | Usability Testing |
| Choose between two designs | A/B Testing, Preference Testing |
| Organize content/features | Card Sorting |
| Validate navigation structure | Tree Testing |
| Measure satisfaction | Surveys (SUS, NPS, CSAT) |
| Understand "why" behind analytics | Interviews, Session Recordings |
| Validate a new concept | Concept Testing |
| Track behavior over time | Diary Studies, Analytics |
| Quick feedback on prototype | Unmoderated Usability Testing |
| Understand expert perspective | Heuristic Evaluation |
| Ensure accessibility | Accessibility Testing |

---

**Version**: 1.0
**Last Updated**: January 2025
**Success Rate**: Based on industry best practices and research literature
