# Language Learning Assistant Plugin

Your personal AI-powered language learning companion with vocabulary management, spaced repetition, grammar reference, immersion tracking, and milestone progression for comprehensive language mastery.

## Overview

The Language Learning Assistant plugin transforms language learning with Claude Code by providing intelligent vocabulary management with spaced repetition algorithms, structured grammar reference, practice session scheduling, immersion activity logging, fluency milestone tracking with CEFR level alignment, and conversation partner coordination. It combines the science of spaced repetition with AI-powered personalization for optimal learning outcomes.

## What's Included

### Agents

#### 1. vocabulary-manager
Manages your vocabulary database with intelligent spaced repetition algorithms (SM-2, Leitner).

**Capabilities**:
- Add new words/phrases with context and examples
- Review due items based on SRS algorithm
- Track learning progress and retention rates
- Export/import vocabulary lists
- Generate practice sessions
- Analyze weak areas and suggest focus

**Activation**: Use `@vocabulary-manager` or automatically activates for vocabulary-related requests.

#### 2. grammar-tutor
Comprehensive grammar reference and explanation system for your target language.

**Capabilities**:
- Explain grammar rules with clear examples
- Provide practice exercises for specific rules
- Compare grammar between native and target language
- Track grammar topics mastered
- Generate targeted practice based on mistakes
- Create grammar cheat sheets

**Activation**: Use `@grammar-tutor` or automatically activates for grammar questions.

#### 3. practice-scheduler
Creates and manages practice sessions based on your schedule, goals, and learning patterns.

**Capabilities**:
- Design optimal practice schedules
- Balance vocabulary, grammar, listening, speaking
- Adapt to your availability and energy levels
- Track practice streaks and consistency
- Suggest optimal practice times
- Generate session plans with varied activities

**Activation**: Use `@practice-scheduler` for schedule planning.

#### 4. immersion-tracker
Logs and analyzes your language immersion activities (movies, podcasts, reading, conversations).

**Capabilities**:
- Log immersion activities with details
- Track total immersion hours
- Analyze content difficulty levels
- Suggest content based on level
- Visualize immersion patterns
- Identify immersion gaps (too much reading, not enough listening, etc.)

**Activation**: Use `@immersion-tracker` for logging activities.

#### 5. milestone-tracker
Tracks your progress toward fluency milestones aligned with CEFR levels (A1-C2).

**Capabilities**:
- Assess current CEFR level
- Define milestones and benchmarks
- Track skills by category (reading, writing, listening, speaking)
- Generate progress reports
- Suggest next learning objectives
- Celebrate achievements

**Activation**: Use `@milestone-tracker` for progress assessment.

#### 6. conversation-coordinator
Manages scheduling and tracking of sessions with tutors/conversation partners.

**Capabilities**:
- Schedule tutor/partner sessions
- Log session notes and topics covered
- Track conversation time and partners
- Suggest conversation topics
- Prepare session agendas
- Follow up on homework/practice items

**Activation**: Use `@conversation-coordinator` for session management.

### Skills

#### language-learning
Comprehensive patterns for effective language acquisition including:
- Spaced repetition algorithms (SM-2, Leitner system)
- Vocabulary acquisition strategies
- Grammar learning frameworks
- Immersion techniques and tracking
- CEFR level progression paths
- Practice session design patterns
- Motivation and habit formation
- Multi-skill integration (reading, writing, listening, speaking)

Main Claude reads this skill for coordinated language learning workflows.

### Python Utilities

#### spaced_repetition.py
Core spaced repetition algorithms:
- **SM-2 Algorithm**: SuperMemo 2 implementation with intervals and ease factors
- **Leitner System**: Box-based progressive learning
- **Review Scheduler**: Calculates next review dates
- **Performance Analytics**: Retention rates and weak areas

#### vocab_database.py
SQLite-based vocabulary management:
- Word/phrase storage with metadata
- Learning state tracking
- Review history
- Search and filtering
- Import/export functionality

#### progress_tracker.py
Progress analytics and visualization:
- CEFR level assessment algorithms
- Milestone tracking
- Learning curve analysis
- Study time analytics
- Visualization generators

## The Language Learning Model

### How It Works

```
User: "Add vocabulary: 'libro' means 'book' in Spanish"
    ↓
@vocabulary-manager activates
    ↓
Stores word with SRS scheduling
    ↓
Returns confirmation + first review time
```

```
User: "What should I practice today?"
    ↓
@practice-scheduler analyzes
    ↓
Checks due vocabulary reviews
Identifies weak grammar areas
Reviews recent immersion balance
    ↓
Creates personalized session plan
```

```
User: "I watched a Spanish movie for 2 hours"
    ↓
@immersion-tracker logs activity
    ↓
Updates total immersion time
Analyzes content balance
    ↓
Suggests complementary activities
```

### Data Flow Architecture

```
┌─────────────────────────────────────────────┐
│         Language Learning Data              │
├─────────────────────────────────────────────┤
│                                             │
│  ~/.language-learning/                      │
│  ├── vocabulary.db       (SQLite)           │
│  ├── grammar/            (Markdown refs)    │
│  ├── immersion.json      (Activity log)     │
│  ├── milestones.json     (Progress data)    │
│  ├── schedule.json       (Practice plans)   │
│  └── conversations.json  (Tutor sessions)   │
│                                             │
└─────────────────────────────────────────────┘
         ↓                    ↑
    Agents read/write      Data flows
         ↓                    ↑
┌─────────────────────────────────────────────┐
│           Coordination Layer                │
│   (Main Claude + language-learning skill)   │
└─────────────────────────────────────────────┘
```

## Features

### Intelligent Spaced Repetition

Uses proven algorithms for optimal retention:

**SM-2 Algorithm**:
```
Initial interval: 1 day
After correct recall: Interval × Ease Factor
After wrong recall: Reset to 1 day
Ease factor adjusts based on performance
```

**Leitner System**:
```
Box 1 (new): Review daily
Box 2: Review every 3 days
Box 3: Review weekly
Box 4: Review bi-weekly
Box 5: Review monthly

Correct answer: Move to next box
Incorrect answer: Move back to Box 1
```

### Comprehensive Vocabulary Database

Stores rich vocabulary data:

```json
{
  "word": "hablar",
  "translation": "to speak",
  "language": "es",
  "pos": "verb",
  "conjugation": "regular -ar",
  "example": "Yo hablo español todos los días.",
  "context": "Daily conversation practice",
  "added_date": "2025-01-15",
  "last_reviewed": "2025-01-20",
  "next_review": "2025-01-25",
  "interval": 5,
  "ease_factor": 2.5,
  "review_count": 3,
  "correct_count": 2,
  "box": 2,
  "tags": ["daily-life", "communication", "basic"]
}
```

### Grammar Reference System

Organized grammar knowledge base:

```
~/.language-learning/grammar/
├── spanish/
│   ├── present-tense.md
│   ├── preterite-vs-imperfect.md
│   ├── subjunctive.md
│   ├── por-vs-para.md
│   └── ser-vs-estar.md
├── french/
│   ├── passe-compose.md
│   ├── subjunctive-mood.md
│   └── articles.md
└── templates/
    └── grammar-rule-template.md
```

Each rule includes:
- Clear explanation
- Formation rules
- Usage cases
- Examples (correct + incorrect)
- Practice exercises
- Common mistakes
- Related concepts

### CEFR-Aligned Milestones

Track progress through standardized levels:

**A1 (Beginner)**:
- 500-1000 vocabulary words
- Basic present tense
- Simple conversations
- Understanding simple texts

**A2 (Elementary)**:
- 1000-2000 words
- Past tense introduction
- Common situations
- Short texts and dialogs

**B1 (Intermediate)**:
- 2000-3500 words
- Most grammar structures
- Independent conversations
- Understanding main points

**B2 (Upper Intermediate)**:
- 3500-5000 words
- Complex grammar mastery
- Fluent conversations
- Detailed texts

**C1 (Advanced)**:
- 5000-8000 words
- Nuanced expression
- Professional contexts
- Complex literature

**C2 (Proficiency)**:
- 8000+ words
- Native-like fluency
- All contexts
- Academic/literary texts

### Immersion Tracking

Log diverse learning activities:

```json
{
  "activity_id": "imm-20250115-001",
  "date": "2025-01-15",
  "type": "movie",
  "title": "Coco",
  "language": "es",
  "duration_minutes": 105,
  "difficulty": "B1",
  "subtitles": "es",
  "comprehension": 75,
  "new_words_learned": 12,
  "notes": "Family-themed, clear audio, learned food vocabulary",
  "enjoyment": 5
}
```

Types tracked:
- Movies/TV (with/without subtitles)
- Podcasts/Audio
- Books/Articles
- Conversations
- YouTube videos
- Language exchange
- Immersive gaming

### Practice Session Design

Structured, varied sessions:

```markdown
## Practice Session - 2025-01-20 (30 minutes)

### Vocabulary Review (10 min)
- 15 words due for review (SRS-scheduled)
- Focus: Food & Cooking vocabulary

### Grammar Practice (10 min)
- Topic: Preterite vs Imperfect
- 5 fill-in-the-blank exercises
- 3 sentence translations

### Listening (5 min)
- Short podcast clip (A2 level)
- Comprehension questions

### Speaking Practice (5 min)
- Record yourself: "Describe your daily routine"
- Self-assess pronunciation and fluency

### Bonus
- 2 new words to add to vocabulary
- Plan tomorrow's immersion activity
```

## Installation

```bash
/plugin install language-learning@puerto
```

After installation, restart Claude Code to activate all agents and skills.

## Initial Setup

After installing, initialize your learning profile:

```
@milestone-tracker Initialize my language learning profile

Language: Spanish
Native language: English
Current level estimate: A2
Daily study time available: 30 minutes
Primary goal: Conversational fluency for travel
Target milestone: B1 in 6 months
```

This creates your data directory and sets up initial tracking.

## Usage Examples

### Scenario 1: Daily Vocabulary Review

**Request**:
```
@vocabulary-manager Show me today's vocabulary review
```

**Agent response**:
```
=== Vocabulary Review Session - 2025-01-20 ===

15 words due for review today:

1/15: hablar
Translation: ?
[Think about it... press Enter for answer]

→ "to speak"
✓ Correct!
Difficulty (1-5): 2

Next interval: 7 days
Next review: 2025-01-27

---

Session complete: 15/15 correct (100%)
Average difficulty: 2.3/5
Next review: 12 words on 2025-01-22
```

### Scenario 2: Adding New Vocabulary

**Request**:
```
@vocabulary-manager Add word: "la biblioteca" (the library)
Context: I need to find the library to study.
Example: "Voy a la biblioteca para estudiar."
```

**Agent response**:
```
✓ Added: "la biblioteca" → "the library"

Details:
- Language: Spanish
- Part of speech: noun (feminine)
- Context saved
- Example sentence saved
- Tags: [places, daily-life]

First review scheduled: 2025-01-21 (1 day)

Related words you might want to add:
- el libro (the book)
- estudiar (to study)
- leer (to read)
```

### Scenario 3: Grammar Help

**Request**:
```
@grammar-tutor Explain when to use "por" vs "para" in Spanish
```

**Agent response**:
```markdown
## Por vs Para in Spanish

### PARA (Purpose/Destination/Deadline)

**Uses**:
1. Purpose ("in order to", "for the purpose of")
   - Estudio para aprender → I study (in order) to learn

2. Destination
   - Voy para Madrid → I'm going to Madrid

3. Deadline
   - Es para mañana → It's due tomorrow

4. Recipient
   - Este regalo es para ti → This gift is for you

### POR (Reason/Duration/Exchange)

**Uses**:
1. Reason/Cause ("because of")
   - Estudio por mi futuro → I study because of my future

2. Duration
   - Estudié por dos horas → I studied for two hours

3. Exchange ("for" in trade)
   - Pagué 5 euros por el libro → I paid 5 euros for the book

4. Movement through
   - Camino por el parque → I walk through the park

### Memory Trick
PARA = Purpose, Aim, Recipient, Arrival
POR = Reason, Over (duration), Route

Practice saved to: ~/.language-learning/grammar/spanish/por-vs-para.md

Would you like practice exercises for this topic?
```

### Scenario 4: Creating Practice Schedule

**Request**:
```
@practice-scheduler Create my weekly practice plan
Available: Weekdays 7-8 AM, Weekends 2-4 PM
```

**Agent response**:
```markdown
## Weekly Practice Schedule

### Monday - Friday (7:00-8:00 AM)
**Focus**: Vocabulary + Grammar

Mon: Vocab review (30m) + Grammar: Present tense (30m)
Tue: Vocab review (30m) + Listening practice (30m)
Wed: Vocab review (30m) + Grammar: Past tense (30m)
Thu: Vocab review (30m) + Reading comprehension (30m)
Fri: Vocab review (30m) + Speaking practice (30m)

### Saturday (2:00-4:00 PM)
**Focus**: Immersion + Conversation prep

2:00-3:00 PM: Watch Spanish movie/show (with subtitles)
3:00-4:00 PM: Conversation practice or tutor session

### Sunday (2:00-4:00 PM)
**Focus**: Reading + Review

2:00-3:00 PM: Read Spanish article/book chapter
3:00-4:00 PM: Weekly review + Plan next week

### Daily Micro-Practice (5-10 min)
- Morning commute: Spanish podcast
- Lunch break: Duolingo or flashcards
- Evening: One song in Spanish

Total weekly hours: 9 hours structured + 2-3 hours immersion

Saved to: ~/.language-learning/schedule.json
```

### Scenario 5: Logging Immersion

**Request**:
```
@immersion-tracker I watched "La Casa de Papel" episode (45 min)
Difficulty: Hard (lots of slang)
Spanish audio, Spanish subtitles
Comprehension: ~60%
```

**Agent response**:
```
✓ Immersion activity logged

Activity: TV Episode - "La Casa de Papel"
Date: 2025-01-20
Duration: 45 minutes
Difficulty: B2/C1 (challenging)
Comprehension: 60%

=== Your Immersion Stats ===

This week: 3h 15m total
- Watching: 2h 30m (77%)
- Listening: 45m (23%)
- Reading: 0m (0%)
⚠️  Low reading balance

This month: 14h 30m total
Average daily: 45 minutes

=== Recommendations ===

1. Great job with authentic content!
   B2+ difficulty shows you're challenging yourself.

2. Balance suggestion:
   Try adding 30m of reading this week.
   Recommended: Spanish news articles or short stories at B1/B2 level.

3. Comprehension trend:
   60% is good for challenging content.
   Consider mixing in some B1 content for confidence boost.

Next milestone: 20 hours → A2 → B1 listening transition
Progress: 72% (14.5/20 hours)
```

### Scenario 6: Checking Progress

**Request**:
```
@milestone-tracker Show my progress toward B1 level
```

**Agent response**:
```markdown
## CEFR Progress Report - Spanish

Current Level: **A2+ (Upper Elementary)**
Target: **B1 (Intermediate)**

### Progress by Skill

**Vocabulary** ⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜ 75% to B1
- Current: 1,847 words
- B1 target: 2,500 words
- Remaining: 653 words
- Rate: ~15 words/week
- Estimated: 44 weeks to target

**Grammar** ⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜ 60% to B1
Mastered:
- ✅ Present tense (all verbs)
- ✅ Preterite (regular)
- ✅ Basic past (imperfect intro)

In progress:
- 🔄 Preterite irregular verbs
- 🔄 Future tense
- 🔄 Subjunctive (introduction)

**Listening** ⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜ 68% to B1
- Immersion hours: 14.5 total
- B1 target: ~30 hours
- Can understand: Clear speech on familiar topics
- Struggling with: Fast native speech, regional accents

**Reading** ⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜ 52% to B1
- Can read: Simple texts, children's books
- Need more: News articles, longer narratives

**Speaking** ⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜ 45% to B1
- Conversation hours: 6 total (with tutor)
- Can discuss: Present situations, basic past
- Need work: Fluency, complex past narratives

**Writing** ⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜ 55% to B1
- Can write: Simple messages, short paragraphs
- Need work: Longer compositions, variety

### Overall Assessment

**Estimated B1 Achievement**: 6-8 months
(at current pace: 30 min/day study + 45 min/day immersion)

### Next 30-Day Goals

1. Vocabulary: Add 200 new words (food, travel, work themes)
2. Grammar: Master preterite irregular + introduce subjunctive
3. Listening: 10 more hours (podcasts + shows)
4. Speaking: 4 tutor sessions (weekly)
5. Reading: Start B1-level short stories

### Accelerators

To reach B1 faster:
- Increase immersion to 90 min/day → Reach B1 in 4 months
- Add language exchange 2x/week → Boost speaking to 65%
- Daily reading habit (20 min) → Reading to 70%

Keep up the great work! You're making steady progress. 🎉
```

### Scenario 7: Coordinating Tutor Sessions

**Request**:
```
@conversation-coordinator Schedule tutor session for next Tuesday 7 PM
Topics: Preterite practice, travel vocabulary
```

**Agent response**:
```
✓ Tutor session scheduled

Date: Tuesday, January 23, 2025
Time: 7:00 PM (1 hour)
Platform: Zoom (link saved)

=== Session Agenda ===

1. Warm-up (5 min)
   - How was your week? (En español!)

2. Preterite Practice (25 min)
   - Review irregular verbs you learned
   - Storytelling exercise (past vacation)
   - Correction and feedback

3. Travel Vocabulary (20 min)
   - Airport/hotel scenarios
   - Role-play: Checking into a hotel
   - Common travel phrases

4. Free Conversation (10 min)
   - Discuss your upcoming trip plans
   - Q&A and general practice

=== Preparation Tasks ===

Before Tuesday:
- [ ] Review preterite irregular verbs (hacer, ir, ser, tener)
- [ ] Learn 10 travel words from vocabulary list
- [ ] Prepare: "Tell a story about a past trip" (5 sentences)

=== Previous Sessions ===

Last session: January 16, 2025
Topics covered: Present tense review, restaurant vocabulary
Homework: ✓ Completed
Tutor notes: "Good progress on pronunciation. Work on verb conjugations."

Total conversation time: 7 hours (this will be session #8)

Session saved to: ~/.language-learning/conversations.json
```

## Orchestrated Workflows

The plugin works seamlessly with the orchestrator for complex tasks:

### Example: Complete Learning Day Plan

**Request**: "Plan my complete Spanish learning day: review, new content, and practice"

**Orchestrator creates**:
```
Plan: Sequential + Parallel workflow

Stage 1: Morning Review (parallel)
├─ @vocabulary-manager → Due vocabulary review
└─ @grammar-tutor → Quick grammar refresher

Stage 2: Learning Session
├─ @vocabulary-manager → Add 10 new words (theme: work)
└─ @grammar-tutor → Subjunctive lesson

Stage 3: Immersion (user choice)
└─ @immersion-tracker → Suggests content at right level

Stage 4: Practice
└─ @practice-scheduler → Generates session with exercises

Stage 5: Progress Update (parallel)
├─ @milestone-tracker → Update progress metrics
└─ @conversation-coordinator → Confirm next tutor session
```

## File Structure

```
language-learning/
├── agents/
│   ├── vocabulary-manager.md
│   ├── grammar-tutor.md
│   ├── practice-scheduler.md
│   ├── immersion-tracker.md
│   ├── milestone-tracker.md
│   └── conversation-coordinator.md
├── skills/
│   └── language-learning/
│       └── SKILL.md
├── utils/
│   ├── spaced_repetition.py
│   ├── vocab_database.py
│   └── progress_tracker.py
└── README.md (this file)
```

## Data Storage

User learning data is stored in:

```
~/.language-learning/
├── vocabulary.db          # SQLite database
├── config.json           # User preferences & settings
├── immersion.json        # Activity logs
├── milestones.json       # Progress tracking
├── schedule.json         # Practice plans
├── conversations.json    # Tutor session logs
└── grammar/             # Grammar reference library
    └── [language]/
        └── *.md
```

All data is local and private. Export/backup features included.

## Advanced Features

### Multi-Language Support

Track multiple languages simultaneously:

```
@milestone-tracker
Languages tracked:
- Spanish: A2+ (primary)
- French: A1 (casual)
- German: A1 (starting)
```

Each language has separate vocabulary database and progress tracking.

### Custom Learning Algorithms

Choose your preferred SRS algorithm:

- **SM-2**: Best for long-term retention (default)
- **Leitner**: Simpler, box-based system
- **Custom**: Define your own intervals

### Analytics Dashboard

Request comprehensive analytics:

```
@milestone-tracker Generate learning analytics report
```

Includes:
- Retention curve (vocabulary)
- Study time heatmap
- Immersion balance chart
- Milestone progression timeline
- Weak areas identification
- Recommended focus areas

### Vocabulary Import/Export

Import from popular sources:

```
@vocabulary-manager Import from Anki deck "Spanish-Core-2000.apkg"
@vocabulary-manager Export to CSV for backup
```

### Gamification Elements

- Study streaks tracking
- Milestone achievements
- Personal bests
- Weekly challenges

## Best Practices

### Effective Vocabulary Learning

1. **Context is key**: Always add example sentences
2. **Use it or lose it**: Review consistently, don't skip
3. **Quality over quantity**: 10 words deeply learned > 50 barely known
4. **Theme batches**: Learn related words together (e.g., "kitchen vocabulary")
5. **Regular review**: Follow SRS schedule religiously

### Grammar Mastery

1. **One concept at a time**: Don't rush through multiple complex topics
2. **Practice immediately**: Apply new grammar in sentences
3. **Compare with native language**: Understand similarities/differences
4. **Common mistakes**: Learn from errors, track problem areas
5. **Contextual learning**: Grammar through reading/listening, not just rules

### Balanced Immersion

1. **Variety**: Mix movies, podcasts, reading, conversations
2. **Appropriate level**: 70% comprehension sweet spot (i+1)
3. **Active vs passive**: Balance passive watching with active study
4. **Enjoyment matters**: Choose content you're interested in
5. **Quantity counts**: Aim for 30+ hours at each CEFR level

### Practice Consistency

1. **Daily habit**: Even 15 minutes is better than 0
2. **Same time**: Schedule practice at consistent times
3. **Realistic goals**: Better to sustain 30 min/day than burn out at 2 hours
4. **Varied activities**: Prevent boredom with diverse practice
5. **Track everything**: Logging creates accountability

## Troubleshooting

### Vocabulary Reviews Pile Up

**Issue**: Too many due reviews, overwhelming

**Solution**:
```
@vocabulary-manager Adjust review load
Options:
- Increase intervals (slower forgetting curve)
- Reduce new words added per day
- Focus on most important words (filter by tags)
- Declare "review bankruptcy" and reset some items
```

### Stuck at a Level

**Issue**: Not progressing toward next CEFR level

**Solution**:
```
@milestone-tracker Analyze progress bottleneck

Identifies:
- Which skill is lagging (vocabulary? grammar? listening?)
- Suggested focus area
- Recommended resources
- Adjusted timeline with intensive plan
```

### Finding Time for Practice

**Issue**: Inconsistent schedule, missing sessions

**Solution**:
```
@practice-scheduler Create micro-practice plan
- 10-minute sessions
- Commute-friendly activities
- Habit stacking suggestions
- Weekend intensive options
```

## Integration with Other Plugins

### With Orchestrator

Complex learning workflows:
```
@orchestrator-planner Create 90-day Spanish immersion plan
→ Coordinates all learning agents for comprehensive program
```

### With Subagent Creator

Create custom agents:
```
@ultimate-subagent-creator
Create an agent for Spanish music lyrics analysis and vocabulary extraction
```

## Future Enhancements

Planned features:
- **Speech recognition**: Practice pronunciation with feedback
- **AI conversation partner**: ChatGPT-style conversation practice
- **Community sharing**: Share/import vocabulary decks
- **Mobile sync**: Sync with mobile flashcard apps
- **Video learning**: YouTube subtitle extraction and vocabulary mining
- **Writing correction**: AI-powered essay correction
- **Placement test**: Automated CEFR level assessment

## Contributing

This plugin is part of the Puerto marketplace. Contributions welcome:
- New language templates
- Grammar reference content
- SRS algorithm improvements
- Analytics visualizations

## Support

For issues or questions:
- Review the [language-learning skill](skills/language-learning/SKILL.md)
- Check individual agent documentation in `agents/`
- See Python utilities documentation in `utils/`

## License

MIT License - See main repository for details

---

**Master any language through consistent, intelligent, personalized practice. Your AI language learning companion is ready.** 🌍📚🎯
