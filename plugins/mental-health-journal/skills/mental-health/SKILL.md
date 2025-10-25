# Mental Health Journaling & Tracking Skill

Evidence-based approaches for mental health support through journaling and mood tracking.

## Core Principles

### 1. Privacy First

ALL data must:
- Stay local (never cloud sync without explicit user encryption)
- Be stored with strict permissions (chmod 600)
- Be easily exportable (user owns their data)
- Be deletable (user's right to forget)

### 2. Evidence-Based

Approaches based on:
- **CBT** (Cognitive Behavioral Therapy): Thought-emotion-behavior connections
- **DBT** (Dialectical Behavior Therapy): Emotion regulation, distress tolerance
- **ACT** (Acceptance & Commitment Therapy): Mindfulness, values
- **Positive Psychology**: Gratitude, strengths, meaning

### 3. Therapeutic Boundaries

This is **NOT therapy**. It is:
- Journaling support
- Mood tracking
- Coping skill library
- Pattern recognition

Always encourage professional mental health care for:
- Ongoing struggles
- Crisis situations
- Diagnosis needs
- Medication management

### 4. Crisis Response

Immediate response for:
- Suicidal ideation
- Self-harm urges
- Severe distress
- Safety concerns

Always provide crisis hotlines FIRST, support SECOND.

## Data Structure

### Daily Mood Entry

```json
{
  "date": "YYYY-MM-DD",
  "timestamp": "ISO-8601",
  "mood": {
    "overall": 1-10,
    "energy": 1-10,
    "anxiety": 1-10,
    "depression": 1-10,
    "sleep_quality": 1-10
  },
  "emotions": ["primary", "secondary", "tertiary"],
  "triggers": ["identified triggers"],
  "coping_used": ["strategies employed"],
  "gratitude": ["items"],
  "notes": "free-form reflection",
  "therapy_session": "boolean",
  "medication_taken": "boolean (if tracked)",
  "exercise": "boolean/description",
  "social_connection": "boolean/description"
}
```

### Journal Entry

```json
{
  "id": "YYYYMMDD-HHMMSS",
  "date": "YYYY-MM-DD",
  "timestamp": "ISO-8601",
  "type": "free-form|therapy-prep|therapy-debrief|trigger-analysis|gratitude|worry-dump|cbt-structured",
  "title": "optional",
  "content": "main journaling",
  "prompts_used": ["therapeutic prompts"],
  "emotions": ["tagged"],
  "triggers": ["identified"],
  "insights": "realizations",
  "situation": "context",
  "thoughts": "CBT thought record",
  "feelings": "emotional response",
  "behaviors": "actions taken",
  "alternative_thoughts": "reframing",
  "therapy_related": "session connection"
}
```

### Coping Strategy Log

```json
{
  "technique": "name",
  "category": "anxiety|depression|anger|general",
  "used_date": "ISO-8601",
  "situation": "when used",
  "effectiveness": "1-10",
  "duration": "time taken",
  "notes": "observations",
  "source": "CBT|DBT|therapist|self-discovered"
}
```

## Therapeutic Techniques

### CBT Techniques

**Thought Records**:
1. Situation: What happened?
2. Automatic thought: What went through your mind?
3. Evidence for: What supports this thought?
4. Evidence against: What contradicts it?
5. Alternative thought: More balanced perspective
6. New feeling: How do you feel now?

**Cognitive Distortions to Identify**:
- All-or-nothing thinking
- Overgeneralization
- Mental filter
- Discounting positives
- Jumping to conclusions
- Catastrophizing
- Emotional reasoning
- Should statements
- Labeling
- Personalization

### DBT Skills

**Distress Tolerance (TIPP)**:
- Temperature: Cold water on face
- Intense exercise: Brief, vigorous movement
- Paced breathing: Slow, controlled
- Progressive relaxation: Tense and release muscles

**STOP Technique**:
- Stop: Pause whatever you're doing
- Take a step back: Physically or mentally
- Observe: Notice what's happening
- Proceed mindfully: Choose your next action

**Emotion Regulation**:
- Identify and label emotions
- Opposite action
- Check the facts
- Problem-solving
- Accumulate positive experiences

### Grounding Techniques

**5-4-3-2-1**:
- 5 things you see
- 4 things you touch
- 3 things you hear
- 2 things you smell
- 1 thing you taste

**Physical Grounding**:
- Feel feet on floor
- Hold ice cube
- Splash cold water
- Deep pressure (hug yourself)

**Mental Grounding**:
- Count backwards from 100 by 7s
- Name categories (colors, countries)
- Recite poem or song lyrics

### Self-Compassion

**Three Components** (Kristin Neff):
1. Self-kindness vs self-judgment
2. Common humanity vs isolation
3. Mindfulness vs over-identification

**Self-Compassion Break**:
1. "This is a moment of suffering"
2. "Suffering is part of life"
3. "May I be kind to myself"

## Pattern Analysis Guidelines

### What to Look For

**Helpful patterns**:
- Activities that correlate with better mood
- Coping strategies that work
- Protective factors
- Positive trends

**Concerning patterns**:
- Consistent low mood (5+ days < 4)
- Increasing anxiety
- Sleep deterioration
- Social isolation
- Specific triggers

### How to Present Patterns

**Always**:
- Non-judgmental language
- Empowering (user has agency)
- Actionable insights
- Connect to coping

**Never**:
- Diagnostic language
- Deterministic predictions
- Overwhelming data dumps
- Pattern as destiny

## Journaling Prompts Library

### Morning Prompts
- How am I feeling waking up today?
- What's one thing I'm looking forward to?
- What do I need today?
- Intention for today:

### Evening Prompts
- How did today go?
- What am I grateful for?
- What challenged me?
- What did I learn about myself?
- How can I be kind to myself tonight?

### Therapy Prep
- What do I want to discuss in therapy?
- Progress since last session:
- Challenges I'm facing:
- Questions for my therapist:
- Goals for this session:

### Trigger Exploration
- What happened? (situation)
- What did I feel? (emotions)
- What did I think? (thoughts)
- How did I respond? (behaviors)
- What needed attention? (unmet need)
- What would help next time?

### Gratitude
- Three good things today:
- Someone who helped me:
- Something I did well:
- A moment I appreciated:
- What brought joy:

### Worry Dump
- What's worrying me:
- Worst case scenario:
- Best case scenario:
- Most likely scenario:
- What's in my control:
- What I can let go:

### Self-Compassion
- How am I suffering right now?
- What would I say to a friend feeling this?
- What do I need to hear?
- How can I be kind to myself?

## Agent Coordination

### Workflow

```
User → mood-tracker → Daily check-in saved
                    ↓
                    Pattern emerges
                    ↓
              pattern-analyzer → Insights
                    ↓
                Trigger identified
                    ↓
              coping-guide → Strategies
                    ↓
              journal-assistant → Process experience
```

### Crisis Flow

```
Any agent detects crisis
        ↓
crisis-helper activated immediately
        ↓
Resources provided FIRST
        ↓
Supportive presence
        ↓
Professional referral
        ↓
Follow-up check-in
```

## Data Storage Structure

```
~/.claude/mental-health/
├── entries/                    # Daily mood entries
│   ├── 2025-01-15.json
│   ├── 2025-01-16.json
│   └── ...
├── journal/                    # Journal entries
│   ├── 20250115-083022.json
│   ├── 20250115-201544.json
│   └── ...
├── coping-library.json         # Personal coping strategies
├── crisis-log.json             # Crisis events (if user consents)
├── patterns/                   # Analysis results
│   ├── mood-trends.json
│   ├── triggers.json
│   └── correlations.json
├── exports/                    # User-requested exports
│   └── ...
└── .gitignore                  # Prevent accidental commits
```

### Permissions

```bash
# Set strict permissions
chmod 700 ~/.claude/mental-health/
chmod 600 ~/.claude/mental-health/**/*.json
```

## Export Formats

### CSV Export

```csv
date,overall_mood,energy,anxiety,depression,sleep,primary_emotion,triggers,notes
2025-01-15,7,6,4,3,8,content,"work stress","Good day overall"
```

### JSON Export

```json
{
  "export_date": "2025-01-15",
  "date_range": {
    "start": "2025-01-01",
    "end": "2025-01-15"
  },
  "entries": [...],
  "journals": [...],
  "analytics": {
    "mood_average": 6.8,
    "common_triggers": [...],
    "helpful_coping": [...]
  }
}
```

### Markdown Export (therapy sharing)

```markdown
# Mental Health Journal Summary
## Date Range: Jan 1 - Jan 15, 2025

### Mood Overview
- Average: 6.8/10
- Trend: Improving
- Best days: Jan 10, 14
- Challenging days: Jan 3, 7

### Common Triggers
1. Work deadlines
2. Social anxiety
3. Poor sleep

### What Helps
- Morning walks
- Journaling
- Talking to friend

### Insights for Therapy
- [User-selected entries]
- [Patterns noticed]
- [Questions for therapist]
```

## Best Practices

### For Agents

1. **Always read this skill first**
2. **Privacy is paramount** - local-only, strict permissions
3. **Non-judgmental** - all emotions are valid
4. **Evidence-based** - stick to proven techniques
5. **Encourage professional help** - especially for ongoing issues
6. **Crisis first** - immediate response to crisis indicators
7. **Empowering** - user has agency
8. **Compassionate** - warm, supportive tone

### For Users

1. **Consistency** - daily check-ins build valuable data
2. **Honesty** - this is private, be real
3. **Professional support** - this supplements, not replaces therapy
4. **Export regularly** - backup your data
5. **Share with therapist** - if helpful
6. **Customize** - make it work for you

## Limitations

This system:
- Is NOT therapy
- Cannot diagnose
- Cannot prescribe
- Cannot replace professional help
- Is best used alongside mental health care

For:
- Diagnosis
- Medication
- Complex trauma
- Crisis intervention
- Long-term treatment

→ See a licensed mental health professional

## Quality Standards

Every interaction should:
- ✅ Validate user's experience
- ✅ Provide actionable support
- ✅ Maintain strict privacy
- ✅ Use evidence-based approaches
- ✅ Encourage professional help when needed
- ✅ Offer hope
- ✅ Respect user autonomy

Mental health is a journey. This tool supports that journey with
compassion, evidence, and absolute respect for privacy.
