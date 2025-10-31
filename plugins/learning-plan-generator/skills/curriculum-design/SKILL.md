# Curriculum Design Skill

**Evidence-based learning path creation using educational psychology and learning science principles**

This skill codifies best practices from decades of research on how people learn effectively, including Bloom's taxonomy, prerequisite mapping, scaffolding, and metacognition.

---

## Core Principles

1. **Start with Clear Objectives**: Define what learners will be able to DO
2. **Map Prerequisites**: Identify knowledge dependencies
3. **Progress Systematically**: Follow Bloom's taxonomy from simple to complex
4. **Balance Theory and Practice**: 30-40% theory, 60-70% hands-on application
5. **Include Assessment**: Regular checks ensure retention and understanding
6. **Build Metacognitive Skills**: Teach learners how to learn

---

## Bloom's Taxonomy: The Foundation

### Overview

Bloom's taxonomy defines six levels of cognitive complexity, from simple recall to creating original work. **Always structure learning to progress through these levels**.

```
Level 6: CREATE ←────────────── Most Complex
    ↑
Level 5: EVALUATE
    ↑
Level 4: ANALYZE
    ↑
Level 3: APPLY
    ↑
Level 2: UNDERSTAND
    ↑
Level 1: REMEMBER ←────────────── Least Complex
```

### Level 1: Remember (Knowledge)

**Definition**: Recall facts, terms, basic concepts

**Key Verbs**: Define, list, name, identify, recall, recognize, state, describe

**Learning Activities**:
- Flashcards and spaced repetition
- Reading and note-taking
- Watching lectures/videos
- Memorization exercises

**Assessment Methods**:
- Multiple-choice questions
- Fill-in-the-blank
- Matching exercises
- True/false questions

**Example Objectives**:
- "Define what a function is in programming"
- "List the three principles of object-oriented programming"
- "Name the HTML tags for headings"

**Time Allocation**: 15-20% of learning time

---

### Level 2: Understand (Comprehension)

**Definition**: Explain ideas or concepts in your own words

**Key Verbs**: Explain, summarize, paraphrase, classify, compare, contrast, interpret

**Learning Activities**:
- Summarizing reading material
- Explaining concepts to others
- Creating concept maps
- Comparing and contrasting ideas

**Assessment Methods**:
- Short answer questions
- Explanation prompts
- Concept mapping
- Analogies

**Example Objectives**:
- "Explain the difference between let and const in JavaScript"
- "Summarize how HTTP requests work"
- "Compare SQL and NoSQL databases"

**Time Allocation**: 15-20% of learning time

---

### Level 3: Apply (Application)

**Definition**: Use information in new situations

**Key Verbs**: Apply, demonstrate, solve, use, implement, execute, operate

**Learning Activities**:
- Practice problems
- Coding exercises
- Simulations
- Case studies

**Assessment Methods**:
- Problem sets
- Coding challenges
- Practical demonstrations
- Simulations

**Example Objectives**:
- "Write a function that filters an array based on a condition"
- "Implement user authentication in a web application"
- "Use CSS Grid to create a responsive layout"

**Time Allocation**: 30-35% of learning time (MOST IMPORTANT LEVEL)

---

### Level 4: Analyze (Analysis)

**Definition**: Draw connections, find patterns, distinguish between parts

**Key Verbs**: Analyze, categorize, compare, contrast, distinguish, examine, investigate

**Learning Activities**:
- Debugging exercises
- Code review
- Architecture analysis
- Performance profiling

**Assessment Methods**:
- Debugging challenges
- Code analysis reports
- Comparative studies
- Root cause analysis

**Example Objectives**:
- "Analyze this code and identify performance bottlenecks"
- "Examine the trade-offs between different state management solutions"
- "Investigate why this application is slow and propose solutions"

**Time Allocation**: 15-20% of learning time

---

### Level 5: Evaluate (Evaluation)

**Definition**: Justify decisions, critique, make judgments based on criteria

**Key Verbs**: Assess, critique, evaluate, judge, recommend, justify, defend

**Learning Activities**:
- Code review with justification
- Technology selection decisions
- Architecture critiques
- Design pattern evaluation

**Assessment Methods**:
- Critique reports
- Justified recommendations
- Peer review with feedback
- Design evaluations

**Example Objectives**:
- "Evaluate three database options and recommend the best for this use case"
- "Critique this API design and suggest improvements"
- "Justify your choice of framework for this project"

**Time Allocation**: 10-15% of learning time

---

### Level 6: Create (Synthesis)

**Definition**: Produce new or original work

**Key Verbs**: Design, build, create, develop, formulate, author, construct

**Learning Activities**:
- Capstone projects
- Original implementations
- System design
- Portfolio work

**Assessment Methods**:
- Project-based assessment
- Portfolio review
- Design presentations
- Original implementations

**Example Objectives**:
- "Design and build a full-stack e-commerce application"
- "Create a custom state management library"
- "Develop a deployment pipeline from scratch"

**Time Allocation**: 10-15% of learning time (culminating projects)

---

## Prerequisite Mapping and Dependencies

### Why Prerequisites Matter

**Research shows**: Attempting to learn topic B before mastering prerequisite topic A leads to:
- 3x longer learning time
- 50% lower retention
- Higher frustration and dropout rates

**Solution**: Map all prerequisite relationships before designing curriculum.

### Prerequisite Analysis Process

1. **Identify all topics** in the learning domain
2. **For each topic, ask**: "What must a learner already know to understand this?"
3. **Create dependency graph** (topological ordering)
4. **Validate**: Can someone learn X without knowing Y? If no, Y is a prerequisite.
5. **Sequence topics** so prerequisites always come first

### Dependency Graph Example: Web Development

```
Basic Computer Skills
    ↓
HTML & CSS
    ↓
JavaScript Fundamentals
    ├──→ DOM Manipulation
    ├──→ Async JavaScript
    │       ↓
    │   API Integration
    ├──→ React Basics
    │       ↓
    │   React Hooks
    │       ↓
    │   State Management
    └──→ Node.js Basics
            ↓
        Express.js
            ↓
        RESTful APIs
            ↓
        Database Integration
            ↓
    Full-Stack Integration Project
```

### Prerequisite Validation Questions

For each prerequisite relationship, verify:

- **Is it necessary?** Can topic B be learned without topic A?
- **Is it sufficient?** Does topic A provide enough foundation for topic B?
- **Is it atomic?** Can it be broken into smaller prerequisites?

### Handling Multiple Prerequisites

**Rule**: ALL prerequisites must be completed before unlocking next topic.

Example:
```
Database Integration requires:
    ✓ Express.js (web framework)
    ✓ SQL Basics (database querying)
    ✓ Async JavaScript (handling database operations)

If ANY are incomplete → Database Integration remains locked
```

---

## SMART Learning Objectives

Every learning objective must be **SMART**:

### S - Specific

❌ BAD: "Learn React"
✅ GOOD: "Build three React components using hooks for state management"

**Why**: Vague objectives lead to unclear learning paths. Specific objectives provide clear targets.

### M - Measurable

❌ BAD: "Understand databases"
✅ GOOD: "Design and implement a normalized database schema with 5+ tables and foreign key relationships"

**Why**: You need to know when you've achieved the objective.

### A - Achievable

❌ BAD: "Master all of machine learning in 2 weeks"
✅ GOOD: "Train and evaluate three supervised learning models on a provided dataset in 2 weeks"

**Why**: Unrealistic objectives lead to frustration and abandonment.

### R - Relevant

❌ BAD: "Learn Assembly language" (for web development goal)
✅ GOOD: "Implement user authentication with JWT" (directly relevant to web dev)

**Why**: Every objective should clearly connect to the overall learning goal.

### T - Time-bound

❌ BAD: "Eventually build a portfolio website"
✅ GOOD: "Build and deploy a portfolio website by Week 6"

**Why**: Deadlines create urgency and help track progress.

### Template for Writing SMART Objectives

```
By [TIMEFRAME], learner will [ACTION VERB] [SPECIFIC DELIVERABLE]
that demonstrates [MEASURABLE CRITERIA] in order to [RELEVANCE TO GOAL].
```

**Example**:
"By Week 4, learner will **implement** a **user authentication system with JWT** that **includes login, logout, and protected routes** in order to **build secure full-stack applications**."

---

## Progressive Complexity: Scaffolding

### The Scaffolding Principle

**Research**: Learners master complex skills by starting with high support and gradually removing it as competence increases.

### Four Stages of Scaffolding

#### Stage 1: I Do (Modeling)
**Support Level**: MAXIMUM (100%)

**Approach**:
- Instructor demonstrates complete process
- Learner observes and takes notes
- No learner production yet
- Focus on understanding the "what" and "why"

**Example**:
"Watch me build a React component from scratch. Notice how I structure it, handle state, and add event handlers."

**Duration**: 1-2 sessions

#### Stage 2: We Do Together (Guided Practice)
**Support Level**: HIGH (75%)

**Approach**:
- Instructor and learner work together
- Instructor provides step-by-step guidance
- Learner follows along, doing the work
- Immediate feedback and correction

**Example**:
"Now let's build a similar component together. I'll guide you through each step. Try implementing the state management - I'll help if you get stuck."

**Duration**: 2-4 sessions

#### Stage 3: You Do with Support (Scaffolded Practice)
**Support Level**: MEDIUM (50%)

**Approach**:
- Learner works independently on similar problems
- Instructor available for questions
- Provide templates, checklists, hints
- Feedback after completion

**Example**:
"Build a different component on your own using this starter template. Refer to the examples we did together. I'm here if you need help."

**Duration**: 3-5 sessions

#### Stage 4: You Do Alone (Independent Practice)
**Support Level**: MINIMAL (25%)

**Approach**:
- Learner works on novel problems independently
- No templates or guides
- Instructor reviews completed work
- Learner self-assesses first

**Example**:
"Design and build a component from scratch to solve this new requirement. Show me when you're done and we'll review it together."

**Duration**: Ongoing

### Applying Scaffolding to a Learning Plan

**Week 1-2: High Support**
- Follow detailed tutorials
- Complete fill-in-the-blank exercises
- Use starter templates
- Frequent check-ins

**Week 3-5: Medium Support**
- Semi-guided projects
- Partial templates provided
- Hints available
- Weekly check-ins

**Week 6-8: Low Support**
- Open-ended projects
- Requirements only, no templates
- Self-directed problem solving
- As-needed support

**Week 9+: Independent**
- Novel, complex projects
- Self-assessment
- Peer review
- Portfolio work

---

## Chunking: Optimal Module Sizes

### The Cognitive Load Principle

**Research**: Working memory can hold 4±1 "chunks" of information at once. Exceeding this causes cognitive overload and poor learning.

### Chunking Guidelines

**Single Learning Session**:
- **Ideal**: 3-5 new concepts
- **Maximum**: 7 new concepts
- **Minimum**: 1 concept (if complex)

**Time per Concept**:
- **Simple concept**: 15-30 minutes
- **Medium concept**: 45-60 minutes
- **Complex concept**: 90-120 minutes (split across sessions)

**Module Structure**:
```
Module: JavaScript Functions (Week 2)
├── Lesson 1: Function Declaration Syntax (30 min)
├── Lesson 2: Parameters and Arguments (45 min)
├── Lesson 3: Return Values (30 min)
├── Lesson 4: Arrow Functions (45 min)
└── Practice: Build 5 functions (90 min)

Total: ~4 hours over 3-4 days
```

### Preventing Cognitive Overload

**Signs of Overload**:
- Can't recall what was just learned
- Frustration and confusion
- Declining performance
- Feeling overwhelmed

**Solutions**:
1. **Reduce chunks**: Teach fewer concepts per session
2. **Increase spacing**: Spread learning over more days
3. **Add practice**: More hands-on application between concepts
4. **Review more**: Ensure previous chunks are solid before adding new ones

---

## Zone of Proximal Development (ZPD)

### The ZPD Principle

**Definition**: The sweet spot between "too easy" (boring) and "too hard" (frustrating).

```
Too Easy ─────────── ZPD (OPTIMAL) ─────────── Too Hard
   ↓                      ↓                         ↓
Boredom              Productive                 Frustration
No growth            struggle                   Giving up
                     Maximum learning
```

### Characteristics of ZPD

**Learner can**:
- Understand the goal
- Make progress with effort
- Succeed with guidance
- Struggle productively (not hopelessly)

**Learner cannot**:
- Complete task easily without thought
- Give up immediately due to overwhelming complexity

### Designing for ZPD

**Too Easy Indicators**:
- Completes in < 50% of estimated time
- Reports feeling unchallenged
- Perfect scores without studying
- **Action**: Increase complexity, skip ahead

**ZPD Indicators** (IDEAL):
- Completes in 80-120% of estimated time
- Reports feeling challenged but capable
- Makes mistakes but learns from them
- Scores 70-90% on assessments
- **Action**: Continue current pace

**Too Hard Indicators**:
- Takes 2x+ estimated time
- Reports feeling overwhelmed
- Frequent requests for help
- Scores below 60% despite effort
- **Action**: Add support, review prerequisites, slow down

### Adjusting Difficulty

**Make Easier**:
- Provide more examples
- Add templates/starter code
- Break into smaller steps
- Increase guidance
- Review prerequisites

**Make Harder**:
- Remove scaffolding
- Add constraints/requirements
- Open-ended problems
- Novel applications
- Combine multiple concepts

---

## Interleaving vs. Blocking

### Blocking (Traditional Approach)

**Structure**: Learn topic A completely, then topic B completely, then topic C

```
Week 1: All Arrays
Week 2: All Linked Lists
Week 3: All Trees
```

**Pros**:
- Feels easier during learning
- Less mental effort to switch contexts

**Cons**:
- Poorer long-term retention
- Difficulty transferring to new situations
- Can't distinguish between similar concepts

### Interleaving (Evidence-Based Approach)

**Structure**: Mix topics A, B, and C during learning

```
Week 1: Arrays intro → Linked Lists intro → Arrays practice
Week 2: Linked Lists practice → Trees intro → Arrays application
Week 3: Trees practice → Review all three → Mixed practice
```

**Pros**:
- Better long-term retention (+30-40%)
- Improved transfer to novel problems
- Better discrimination between concepts
- More realistic (real-world problems mix concepts)

**Cons**:
- Feels harder during learning (this is GOOD)
- Requires more mental effort

### Implementing Interleaving

**Daily Schedule Example**:
```
Monday:
  9:00-10:00   New Material: React Hooks (useState)
  10:15-11:00  Review: JavaScript Arrays (from last week)
  11:15-12:00  Practice: Combining Hooks + Arrays

Tuesday:
  9:00-10:00   New Material: React Hooks (useEffect)
  10:15-11:00  Practice: useState from yesterday
  11:15-12:00  Review: Async JavaScript (from 2 weeks ago)

Wednesday:
  9:00-10:00   Practice: useEffect from yesterday
  10:15-11:00  Mixed: Combine useState + useEffect
  11:15-12:00  New Material: Custom Hooks
```

**Pattern**: Rotate between new material, recent review, and older review

### When NOT to Interleave

**Use blocking for**:
- Complete beginners (too overwhelming)
- First exposure to a concept (need focused introduction)
- Very complex topics requiring deep focus

**Switch to interleaving after**:
- Basic understanding established
- 2-3 concepts learned
- Ready for integration practice

---

## Metacognition: Teaching How to Learn

### What is Metacognition?

**Definition**: Thinking about thinking. Awareness and control of one's own learning process.

**Why it matters**: Students with strong metacognitive skills learn 40% faster and retain more.

### Metacognitive Strategies to Teach

#### 1. Self-Monitoring

**Teach learners to ask**:
- "Do I understand this?"
- "Can I explain it to someone else?"
- "What am I confused about?"
- "Am I making progress?"

**Implementation**:
```markdown
After each topic, complete this checklist:

Understanding Check:
- [ ] I can define key terms without looking them up
- [ ] I can explain the concept in my own words
- [ ] I can provide my own examples
- [ ] I can apply it to solve new problems
- [ ] I can identify when to use this concept

If you checked all 5: You understand! Move forward.
If you checked 3-4: Review unclear parts, then move forward.
If you checked 0-2: Re-study this topic before continuing.
```

#### 2. Planning Strategies

**Teach learners to**:
- Break large tasks into subtasks
- Estimate time requirements
- Identify what help/resources they'll need
- Set mini-deadlines

**Template**:
```markdown
Before starting a project:

1. What am I trying to build? [Clear goal]
2. What do I already know? [Prerequisite check]
3. What do I need to learn? [Knowledge gaps]
4. What subtasks are involved? [Break it down]
   - [ ] Subtask 1 (Est: X hours)
   - [ ] Subtask 2 (Est: Y hours)
5. What resources will I need? [List]
6. When will each part be done? [Timeline]
```

#### 3. Reflection and Adjustment

**Teach learners to review**:
- What worked well?
- What didn't work?
- What will I do differently next time?

**Weekly Reflection Template**:
```markdown
Week [N] Reflection:

What I learned well this week:
- [Concept that clicked]

What I struggled with:
- [Challenging concept]

Why I struggled:
- [ ] Didn't understand prerequisites
- [ ] Moved too fast
- [ ] Need more practice
- [ ] Need different explanation
- [ ] Other: _______

What I'll do differently next week:
- [Specific change 1]
- [Specific change 2]

Study strategies that worked:
- [What helped me learn]

Study strategies to change:
- [What didn't help]
```

#### 4. Active Learning Techniques

**Teach learners to use**:

**Retrieval Practice** (Testing Effect):
- Quiz yourself without looking at notes
- Explain concepts from memory
- Build from scratch without tutorial

**Elaboration**:
- Ask "why?" repeatedly
- Connect new concepts to what you already know
- Create analogies and metaphors

**Self-Explanation**:
- Read code line by line, explaining each step
- Explain why a solution works, not just what it does
- Verbalize your thought process while solving problems

---

## Spaced Repetition for Long-Term Retention

### The Forgetting Curve

**Research (Ebbinghaus)**: Without review, we forget:
- 50% within 1 hour
- 70% within 24 hours
- 90% within 1 week

**Solution**: Spaced repetition - review at increasing intervals

### Optimal Review Schedule

**Initial Learning**: Day 0
**Review 1**: 1 day later (Day 1)
**Review 2**: 3 days later (Day 4)
**Review 3**: 7 days later (Day 11)
**Review 4**: 14 days later (Day 25)
**Review 5**: 30 days later (Day 55)

### Curriculum Integration

**Week 1 Topics**:
- Day 1: Learn Topic A
- Day 2: Review Topic A, Learn Topic B
- Day 5: Review Topic A + B, Learn Topic C
- Day 12: Review Topic A
- Day 26: Review Topic A

**Pattern**: New material + recent reviews + older reviews every day

---

## Assessment Strategy

### Assessment Types

**Diagnostic** (Before learning):
- Identify current knowledge level
- Determine starting point
- Reveal knowledge gaps

**Formative** (During learning):
- Low-stakes knowledge checks
- Identify areas needing more study
- Adjust learning path if needed
- Provide frequent feedback

**Summative** (After learning):
- High-stakes milestone assessments
- Verify mastery
- Determine readiness to advance
- Portfolio/project evaluation

### Assessment Frequency

**Best practice**:
- Diagnostic: Once at start
- Formative: Weekly or after each module
- Summative: End of each phase (every 4-6 weeks)

---

## Time Estimation Guidelines

### Learning Time Factors

**Beginner**: 1.5x standard time
**Intermediate**: 1.0x standard time
**Advanced**: 0.7x standard time

### Content Type Multipliers

**Reading/Video** (Theory):
- Book chapter: 2-3 hours
- Video course hour: 1.5 hours actual time (pause, rewind, take notes)
- Documentation reading: 30-60 min per topic

**Practice** (Application):
- 2-3x theory time
- Coding exercises: 1-2 hours per set
- Small project: 5-10 hours
- Medium project: 20-40 hours

**Review** (Spaced Repetition):
- 20-30% of total learning time

**Buffer** (Struggling Topics):
- Add 30% for challenging new concepts
- Add 20% for life interruptions

### Example Calculation

```
Topic: React Hooks

Theory (watching course + reading docs): 6 hours
Practice (coding exercises): 12 hours (2x theory)
Review (spaced repetition): 4 hours (20% of 18)
Buffer (new concept): 7 hours (30% of 22)

Total: 29 hours

At 2 hours/day: 15 days (~2 weeks)
```

---

## Putting It All Together: Curriculum Design Checklist

When creating a learning plan, ensure:

**Learning Objectives**:
- [ ] All objectives are SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- [ ] Objectives progress through Bloom's taxonomy
- [ ] Each objective clearly states what learner will DO
- [ ] Objectives align with overall learning goal

**Prerequisite Analysis**:
- [ ] All prerequisites identified for each topic
- [ ] Dependencies mapped in a graph
- [ ] No circular dependencies
- [ ] Topics sequenced so prerequisites always come first
- [ ] Prerequisite validation questions included

**Scaffolding**:
- [ ] Learning starts with high support, gradually reduces
- [ ] Complexity increases progressively
- [ ] Clear stages: I Do → We Do → You Do (Supported) → You Do (Independent)
- [ ] Support level matches learner competence

**Chunking**:
- [ ] 3-5 concepts per module (cognitive load management)
- [ ] Module sizes appropriate for available time
- [ ] Complex topics broken into smaller chunks
- [ ] Adequate practice between chunks

**Zone of Proximal Development**:
- [ ] Difficulty level is challenging but achievable
- [ ] Provides enough support for success with effort
- [ ] Includes adjustment guidelines (too easy/too hard)

**Interleaving**:
- [ ] Topics mixed rather than blocked (after initial exposure)
- [ ] Daily schedule rotates: new + recent review + old review
- [ ] Prevents "binge and forget" pattern

**Metacognition**:
- [ ] Includes self-monitoring checklists
- [ ] Teaches planning strategies
- [ ] Requires reflection and adjustment
- [ ] Promotes active learning techniques

**Spaced Repetition**:
- [ ] Review schedule built into timeline
- [ ] Reviews at increasing intervals (1, 3, 7, 14, 30 days)
- [ ] 20-30% of time allocated for review

**Assessment**:
- [ ] Diagnostic assessment at start
- [ ] Formative assessments weekly/per module
- [ ] Summative assessments at phase ends
- [ ] Clear passing criteria defined

**Time Estimates**:
- [ ] Realistic time per topic (includes practice + review)
- [ ] Adjusted for learner level
- [ ] 30% buffer for struggling topics
- [ ] 20% buffer for life interruptions
- [ ] Total time matches available commitment

**Balance**:
- [ ] 30-40% theory, 60-70% practice
- [ ] Projects integrate multiple concepts
- [ ] Real-world applications included

---

## Common Pitfalls to Avoid

❌ **Information Dumping**: Teaching everything about a topic at once
✅ **Progressive Disclosure**: Reveal complexity gradually

❌ **Blocking**: Learning Topic A completely before Topic B
✅ **Interleaving**: Mix topics for better retention

❌ **Passive Learning**: Only reading and watching
✅ **Active Learning**: Hands-on practice and projects

❌ **No Breaks**: Cramming or marathon sessions
✅ **Distributed Practice**: Spread over time with breaks

❌ **One Learning Style**: Only video courses or only books
✅ **Multimodal**: Mix reading, video, practice, projects

❌ **No Review**: Learn once and move on
✅ **Spaced Repetition**: Review at increasing intervals

❌ **Vague Goals**: "Learn programming"
✅ **SMART Objectives**: "Build 3 web apps with React by Week 8"

---

## Research References

This skill is based on:
- Bloom's Taxonomy (1956, revised 2001)
- Ebbinghaus Forgetting Curve (1885)
- Zone of Proximal Development - Vygotsky (1978)
- Cognitive Load Theory - Sweller (1988)
- Spaced Repetition - Leitner (1970s), SuperMemo (1985)
- Interleaving Benefits - Rohrer & Taylor (2007)
- Testing Effect - Roediger & Karpicke (2006)
- Scaffolding - Wood, Bruner, & Ross (1976)
- Metacognition - Flavell (1979)

---

**Version**: 1.0.0
**Last Updated**: January 2025
**Use**: Read by learning-architect agent before creating curricula
