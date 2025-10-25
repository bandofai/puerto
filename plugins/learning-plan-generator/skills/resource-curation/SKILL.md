# Resource Curation Skill

**Finding and evaluating high-quality learning materials for optimal learning outcomes**

This skill codifies best practices for selecting educational resources based on authority, accuracy, currency, relevance, and pedagogical effectiveness.

---

## Core Principles

1. **Quality Over Quantity**: 3 excellent resources beat 20 mediocre ones
2. **Multi-Modal Learning**: Mix formats (video, text, interactive, projects)
3. **Currency Matters**: Technology evolves; recent resources for current best practices
4. **Authority is Key**: Learn from recognized experts and reputable sources
5. **Match to Learning Style**: Different learners, different optimal formats
6. **Always Provide Alternatives**: Free and paid, video and text, beginner and advanced

---

## CRAAP Test for Resource Quality

### Currency

**When was it published or updated?**

**Technology resources**:
- ✅ Excellent: Published/updated within last 12 months
- ✅ Good: Published/updated within last 2 years
- ⚠️ Acceptable: 2-3 years (verify best practices still current)
- ❌ Outdated: 3+ years (unless timeless concepts like algorithms)

**Non-technology resources** (math, writing, theory):
- More forgiving timeline
- Core concepts don't change as fast
- Still prefer recent examples and applications

**How to check**:
```
- Publication date on book/course
- "Last updated" date on website
- Course reviews mentioning if outdated
- Check GitHub repo commit dates
- Look for "2024", "2025" in titles/descriptions
```

**Red flags**:
- "JavaScript ES5" (current is ES2023+)
- "React Class Components" (Hooks are current best practice)
- "Python 2" (Python 3 has been standard since 2008)
- Framework version 2+ major versions behind current

---

### Relevance

**Does it match the learning objective?**

**Questions to ask**:
- Does this teach what learner needs to know?
- Is the level appropriate (beginner/intermediate/advanced)?
- Does it cover the specific topics in learning plan?
- Is the scope right (not too narrow or too broad)?

**Example**:
```
Learning Objective: Build REST APIs with Node.js and Express

✅ Relevant:
- "Building RESTful APIs with Node.js and Express" (exact match)
- "Backend Development with Node.js" (includes REST APIs)

❌ Not Relevant:
- "JavaScript for Beginners" (too broad, no Express)
- "GraphQL API Development" (different paradigm)
- "Complete MEAN Stack" (too broad, includes unneeded topics)
```

**Scope matching**:
- **Too narrow**: "Handling CORS in Express" (too specific for main resource)
- **Just right**: "Express.js Fundamentals"
- **Too broad**: "Full Stack Web Development" (includes too much)

---

### Authority

**Who created it? Are they credible?**

**Author/Instructor credentials to look for**:
- Industry experience (worked at major companies)
- Teaching experience (university, bootcamp, online courses)
- Books published by reputable publishers
- Conference speakers
- Open source contributions
- GitHub stars/followers
- Community recognition

**Publisher/Platform reputation**:

**Top-tier (highest authority)**:
- Official documentation (React.dev, Python.org, MDN)
- University courses (MIT OCW, Stanford, Harvard)
- Established publishers (O'Reilly, Manning, Packt)
- Major platforms (Coursera, edX, Pluralsight)

**Mid-tier (good authority)**:
- Established Udemy instructors (high ratings, many students)
- Known bloggers/YouTubers (consistent quality content)
- Tech company blogs (Google, Netflix, Airbnb engineering)

**Be cautious**:
- Unknown authors with no credentials
- Self-published with no reviews
- Platforms with no quality control
- Content farms (mass-produced, low-quality articles)

**How to verify authority**:
```
1. Google the author name + topic
2. Check LinkedIn for professional background
3. Look at other resources they've created
4. Read reviews from learners
5. Check if recommended by experts
```

---

### Accuracy

**Is the information correct?**

**How to evaluate**:
- **Cross-reference**: Check against official docs
- **Reviews**: Look for comments about errors
- **Code samples**: Do they run? Are they best practice?
- **Community validation**: Recommended by multiple sources?
- **Errata**: Does book have published corrections?

**Red flags for inaccuracy**:
- Deprecated methods presented as current
- Security vulnerabilities in example code
- Obvious bugs that weren't caught
- Contradicts official documentation
- Many reviews mentioning errors
- Code samples don't run

**Green flags for accuracy**:
- Technical reviewers listed (for books)
- Active errata/corrections published
- Code samples on GitHub (community can verify)
- Author responds to error reports
- Aligns with official documentation
- Recommended by multiple experts

---

### Purpose

**Why does this resource exist?**

**Educational (best for learning)**:
- Primary goal: Teach concepts clearly
- Examples: Textbooks, courses, tutorials
- Pros: Structured, comprehensive, pedagogically designed

**Reference (good for lookup)**:
- Primary goal: Provide comprehensive info
- Examples: Documentation, API references
- Pros: Authoritative, complete, searchable
- Cons: Not always beginner-friendly

**Commercial (be cautious)**:
- Primary goal: Sell product/service
- Examples: Tool tutorials, framework marketing
- Pros: Often high production value
- Cons: May push specific tool unnecessarily

**Community (varies)**:
- Primary goal: Share knowledge
- Examples: Blogs, Stack Overflow, forums
- Pros: Real-world problems and solutions
- Cons: Quality varies widely

---

## Resource Types and When to Use

### Official Documentation

**Best for**:
- Authoritative reference
- Up-to-date syntax and APIs
- Seeing all available features
- Troubleshooting specific issues

**Not ideal for**:
- Complete beginners (can be dense)
- High-level overview (too detailed)
- Learning best practices (shows what, not why)

**How to use**:
- Start with "Getting Started" / "Quickstart"
- Reference during projects
- Read "Best Practices" sections
- Keep open while coding

**Quality indicators**:
- Search functionality
- Code examples that run
- Regularly updated
- Community-maintained improvements

---

### Books

**Best for**:
- Deep, comprehensive understanding
- Structured learning path
- Reference material
- Theory and fundamentals

**Not ideal for**:
- Quick answers (too much to read)
- Rapidly changing technologies (gets outdated)
- Purely hands-on learners (less interactive)

**How to evaluate books**:

**Publisher reputation** (quality indicator):
- O'Reilly (strong technical review process)
- Manning (code-focused, practical)
- Packt (practical, sometimes uneven quality)
- Pragmatic Programmers (practical, experienced authors)
- No Starch Press (beginner-friendly)
- Apress (hit-or-miss quality)

**Author credentials**:
- Industry experience?
- Previous books?
- Community recognition?

**Edition and date**:
- Latest edition?
- Publication date?
- Planned updates?

**Reviews**:
- Amazon rating (4+ stars, 50+ reviews)
- Goodreads ratings
- Technical community recommendations (Reddit, HackerNews)

**Table of contents**:
- Covers topics you need?
- Logical progression?
- Appropriate depth?

**Sample chapter**:
- Clear writing style?
- Good examples?
- Right level of detail?

---

### Video Courses

**Best for**:
- Visual learners
- Step-by-step guidance
- Seeing process (watching code being written)
- Engagement and motivation

**Not ideal for**:
- Quick reference (hard to search)
- Readers who prefer text
- Going at your own pace (video is fixed speed)

**Platform evaluation**:

**Coursera / edX**:
- Pros: University-backed, structured, certificates
- Cons: Fixed schedule (some courses), variable quality
- Best for: Academic approach, credentialing

**Udemy**:
- Pros: Huge selection, affordable sales, lifetime access
- Cons: Quality varies widely, no vetting
- Best for: Practical skills, when instructor is vetted

**Pluralsight / LinkedIn Learning**:
- Pros: High quality bar, skill assessments, professional
- Cons: Subscription required, less community
- Best for: Corporate training, structured paths

**Frontend Masters / egghead.io**:
- Pros: Very high quality, expert instructors, niche topics
- Cons: More expensive, smaller catalog
- Best for: Web development, advanced topics

**YouTube**:
- Pros: Free, huge variety, can preview quality
- Cons: No structure, variable quality, ads
- Best for: Supplemental learning, specific topics

**Course quality indicators**:
```
✅ Good signs:
- Instructor credentials clear
- Recent publication (< 2 years)
- 4+ stars with 1000+ ratings
- Regular updates mentioned
- Includes exercises/projects
- Q&A active
- Downloadable resources

❌ Red flags:
- < 3.5 stars
- Few reviews (< 100)
- Outdated content (3+ years old, no updates)
- Instructor has many low-rated courses
- No projects/exercises
- Inactive Q&A
```

---

### Interactive Tutorials

**Best for**:
- Hands-on learners
- Immediate feedback
- Building muscle memory
- Staying engaged

**Not ideal for**:
- Theoretical understanding
- Complex projects
- Those who need to see big picture first

**Top platforms by category**:

**General Programming**:
- Codecademy: Interactive coding, instant feedback
- freeCodeCamp: Project-based, free, certification
- Exercism: Mentor-reviewed practice
- Codewars: Algorithm challenges

**Web Development**:
- Scrimba: Interactive screencasts
- Frontend Mentor: Real-world projects
- The Odin Project: Full curriculum, free

**Data Science**:
- DataCamp: Interactive data science
- Kaggle Learn: Quick courses + competitions

**DevOps**:
- Katacoda: Interactive DevOps scenarios
- KodeKloud: Hands-on cloud/DevOps

**Quality evaluation**:
- Is feedback immediate and clear?
- Are exercises well-structured?
- Does difficulty progress appropriately?
- Are real-world projects included?

---

### Practice Platforms

**Best for**:
- Skill reinforcement
- Interview preparation
- Mastery through repetition
- Competitive motivation

**Platform types**:

**Algorithm/DSA**:
- LeetCode: Interview prep, company-specific questions
- HackerRank: Broad practice, certifications
- CodeSignal: Interview practice, arcade mode
- Project Euler: Math-focused problems

**Project-based**:
- Frontend Mentor: Real-world UI challenges
- Codepen Challenges: Creative coding
- DevProjects: Guided real projects

**Domain-specific**:
- SQL: SQLZoo, Mode Analytics, LeetCode SQL
- CSS: CSS Battle, 100 Days CSS
- JavaScript: JavaScript30, CodinGame
- Regex: Regex101, Regexr

**How to use**:
- Start with easy problems (build confidence)
- Progress to medium (where learning happens)
- Do hard problems for mastery
- Time yourself for interview prep
- Read other solutions (learn patterns)

---

### Community Resources

**Best for**:
- Specific problems
- Real-world experiences
- Current trends and best practices
- Learning what to avoid

**Stack Overflow**:
- Pros: High-quality answers, voting system, searchable
- Cons: Can be intimidating to ask questions
- How to use: Search before asking, read highly-voted answers

**Reddit**:
- Pros: Active communities, diverse perspectives
- Cons: Variable quality, can be overwhelming
- Best subreddits: r/learnprogramming, r/webdev, language-specific subs
- How to use: Read wikis/FAQs first, search before posting

**Dev.to**:
- Pros: Beginner-friendly, tutorials and experiences
- Cons: Quality varies
- How to use: Follow good authors, read comments

**Medium/Personal Blogs**:
- Pros: In-depth articles, real experiences
- Cons: Often behind paywall, quality varies
- How to use: Check author credentials, cross-reference info

**GitHub**:
- Awesome lists: Curated resources for technologies
- Example projects: Learn from real code
- Issues: See common problems and solutions

---

## Matching Resources to Learning Styles

### Visual Learners

**Prefer**:
- Video courses
- Diagrams and infographics
- Screencasts
- Visual documentation

**Recommended**:
- Frontend Masters (high-quality video)
- Scrimba (visual + interactive)
- freeCodeCamp YouTube
- Mermaid diagrams in docs

---

### Reading/Writing Learners

**Prefer**:
- Books
- Written tutorials
- Documentation
- Note-taking

**Recommended**:
- O'Reilly books
- MDN documentation
- Written tutorials (dev.to, blogs)
- Official guides

---

### Kinesthetic (Hands-On) Learners

**Prefer**:
- Interactive tutorials
- Coding challenges
- Building projects
- Trial and error

**Recommended**:
- freeCodeCamp (hands-on projects)
- Exercism (practice with feedback)
- Frontend Mentor (build real projects)
- LeetCode (algorithm practice)

---

### Auditory Learners

**Prefer**:
- Video lectures
- Podcasts
- Explaining to others
- Group discussions

**Recommended**:
- Coursera lecture videos
- Syntax podcast (web dev)
- ShopTalk Show podcast
- YouTube tutorials

**Most effective**: Combine multiple styles

---

## Budget-Conscious Resource Selection

### Free Tier (Excellent Free Resources)

**Documentation**:
- Official docs (React, Python, etc.) - Always free
- MDN Web Docs - Comprehensive, free

**Courses**:
- freeCodeCamp - Full curriculum, projects, certificates
- The Odin Project - Full stack, completely free
- MIT OpenCourseWare - University courses
- CS50 (Harvard) - Introduction to CS

**Books**:
- Eloquent JavaScript - Free online
- You Don't Know JS - Free on GitHub
- Automate the Boring Stuff - Free online

**Interactive**:
- Codecademy free tier - Basic courses
- Exercism - All free with mentoring
- Khan Academy - Free programming courses

**Practice**:
- LeetCode free problems
- HackerRank free tier
- Frontend Mentor free challenges

**Budget**: $0
**Time**: Unlimited access

---

### Budget Tier ($20-50/month)

**Best value subscriptions**:
- Udemy courses on sale ($10-15 each, lifetime access)
- O'Reilly Learning ($50/month, huge library)
- Frontend Masters ($39/month, expert content)

**Selective purchases**:
- 1-2 Udemy courses per month
- 1 quality book ($30-40)

**Strategy**:
- Use free resources as foundation
- Pay for specialized/advanced topics
- Wait for Udemy sales (90% off, frequent)
- Check local library for O'Reilly access (some offer free)

**Budget**: $20-50/month
**Result**: Substantial paid content plus all free resources

---

### Premium Tier ($100+/month)

**Comprehensive subscriptions**:
- Pluralsight ($29-45/month)
- LinkedIn Learning ($30-40/month)
- O'Reilly Learning ($50/month)
- Frontend Masters ($39/month)

**Additional**:
- Multiple books per month
- Premium courses
- Bootcamp prep materials

**Budget**: $100+/month
**Result**: Access to nearly all quality resources

---

### Smart Budget Strategies

**Maximize free resources**:
- Exhaust free options before paying
- Official docs are often best resource anyway
- freeCodeCamp rivals paid bootcamps

**Strategic purchasing**:
- Buy books that are timeless (algorithms, fundamentals)
- Rent/library for rapidly changing tech
- Udemy sales only (never pay full price)

**Subscription timing**:
- Subscribe for 1-2 months intensively
- Cancel and use purchased/free resources
- Re-subscribe when needed

**Community resources**:
- Local library (free O'Reilly, Lynda/LinkedIn Learning)
- University access (if student)
- Employer benefits (many companies provide learning subscriptions)

---

## Evaluating Resource Quality: Checklist

When considering a resource, check:

**Currency**:
- [ ] Published/updated within appropriate timeframe
- [ ] Uses current best practices
- [ ] Version numbers are current
- [ ] Community confirms it's not outdated

**Relevance**:
- [ ] Matches learning objectives
- [ ] Appropriate level (beginner/intermediate/advanced)
- [ ] Covers needed topics
- [ ] Right scope (not too narrow or broad)

**Authority**:
- [ ] Author has credible credentials
- [ ] Publisher/platform is reputable
- [ ] Community recommends it
- [ ] Author is recognized expert

**Accuracy**:
- [ ] Aligns with official documentation
- [ ] Code samples work
- [ ] Few/no error reports in reviews
- [ ] Technical reviewers listed (for books)

**Quality**:
- [ ] 4+ stars with substantial reviews (100+)
- [ ] Clear writing/presentation
- [ ] Good examples
- [ ] Includes exercises/projects

**Value**:
- [ ] Price is reasonable for content quality
- [ ] Free alternatives considered
- [ ] Worth the time investment

**Learning effectiveness**:
- [ ] Matches learner's learning style
- [ ] Appropriate pedagogical approach
- [ ] Includes practice opportunities
- [ ] Provides feedback/solutions

---

## Common Resource Selection Mistakes

### ❌ Hoarding Resources

**Problem**: Collecting dozens of courses/books but not completing any

**Solution**:
- Pick 1-2 primary resources per topic
- Finish before adding more
- Others as supplements/reference only

### ❌ Outdated Content

**Problem**: Learning from 5-year-old courses with deprecated practices

**Solution**:
- Always check publication date
- Verify current best practices haven't changed
- Prefer recently updated resources

### ❌ Wrong Level

**Problem**: Beginner taking advanced course or vice versa

**Solution**:
- Read prerequisites carefully
- Check first few lessons/chapters
- Look for "beginner", "intermediate", "advanced" labels

### ❌ Ignoring Reviews

**Problem**: Choosing resource without checking quality

**Solution**:
- Read reviews, especially critical ones
- Look for patterns (many people mention same issue)
- Check recent reviews (resource may have degraded)

### ❌ Analysis Paralysis

**Problem**: Spending weeks researching "the perfect resource" instead of learning

**Solution**:
- Good enough is good enough
- Can always switch if not working
- Time learning > time researching

### ❌ No Practice Resources

**Problem**: Only consuming content (reading/watching) without doing

**Solution**:
- For every hour of theory, do 2 hours of practice
- Always include practice platforms in resource list
- Projects are essential, not optional

---

## Resource Combination Strategies

### The Ideal Resource Mix

For any topic, combine:

**1. Reference** (official docs):
- Purpose: Authoritative source of truth
- Usage: Keep open while working

**2. Primary learning** (1 book OR 1 course):
- Purpose: Structured learning path
- Usage: Work through sequentially

**3. Practice** (interactive platform):
- Purpose: Hands-on skill building
- Usage: Daily exercises

**4. Community** (forums, blogs):
- Purpose: Real-world context, problem-solving
- Usage: As needed for specific questions

### Example: Learning React

```
Reference:
- React.dev (official docs)

Primary Learning (choose one):
- Epic React (course) OR
- Fullstack React (book)

Practice:
- Frontend Mentor (projects)
- Scrimba React course (interactive)

Community:
- r/reactjs (Reddit)
- React Discord
- Dev.to React articles

Projects:
- Build 3 apps (increasing complexity)
```

---

## Research References

This skill is based on:
- CRAAP Test for Information Quality (CSU Chico, 2010)
- Learning Styles Research (Kolb, Honey & Mumford)
- Open Educational Resources Quality
- Information Literacy Standards (ACRL)

---

**Version**: 1.0.0
**Last Updated**: January 2025
**Use**: Read by resource-curator agent before finding learning resources
