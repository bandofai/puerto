# Mental Health Journal Plugin

Privacy-first mental health tracking and journaling for Claude Code. All data stays local, encrypted, and under your control.

## Overview

A compassionate mental health companion providing:
- **Daily mood tracking** with evidence-based scales
- **Therapy journaling** with guided prompts
- **Pattern analysis** to understand your emotional landscape
- **Coping strategies** library with proven techniques
- **Crisis support** with immediate resources

**Core Promise**: Your data never leaves your device. Absolute privacy.

## What's Included

### 5 Specialized Agents

1. **mood-tracker** (Sonnet) - Daily check-ins with validated mood scales
2. **journal-assistant** (Sonnet) - Therapeutic writing support with CBT/DBT prompts
3. **pattern-analyzer** (Sonnet) - Discover triggers, trends, and what helps
4. **coping-guide** (Sonnet) - Evidence-based coping strategies matched to your needs
5. **crisis-helper** (Sonnet) - Immediate crisis resources and supportive presence

### 4 Comprehensive Skills

1. **SKILL.md** - Complete mental health best practices and therapeutic techniques
2. **mood-scales.md** - PHQ-9, GAD-7 inspired assessment tools
3. **emotion-taxonomy.md** - Accurate emotion categorization
4. **crisis-resources.md** - Global crisis hotlines and support services

### Key Features

- **Privacy-First**: Local-only storage, no cloud, no tracking
- **Evidence-Based**: CBT, DBT, ACT approaches
- **Compassionate**: Non-judgmental, supportive interactions
- **Professional**: Encourages mental health care, doesn't replace it
- **Actionable**: Pattern insights connect to coping strategies

## Quick Start

### Daily Mood Check-In

```
@mood-tracker
```

The agent will guide you through:
- Overall mood (1-10)
- Energy, anxiety, sleep
- Emotions and triggers
- Brief reflection

Takes 2-3 minutes. All data saved privately.

### Therapy Journaling

```
@journal-assistant I want to journal about...
```

Choose from:
- Free-form reflection
- Therapy session prep
- Trigger analysis
- CBT thought record
- Gratitude practice

### Find Patterns

```
@pattern-analyzer Show me my mood trends
```

Discover:
- What affects your mood
- Common triggers
- What helps
- Emotional patterns

### Get Coping Support

```
@coping-guide I'm feeling anxious
```

Receive:
- Matched coping techniques
- Step-by-step guidance
- Evidence-based approaches
- Build personal coping library

### Crisis Support

If you're in crisis:

```
@crisis-helper
```

**Or call immediately**:
- US: 988
- UK: 116 123
- Australia: 13 11 14
- International: See crisis-resources skill

## Data Structure

Your data is stored at:
```
~/.claude/mental-health/
├── entries/          # Daily mood check-ins
├── journal/          # Journal entries
├── patterns/         # Analysis results
├── exports/          # Your exports
└── backups/          # Automatic backups
```

**Permissions**: 700 (user-only access)

## Privacy & Security

### What We Do

✅ Store everything locally
✅ Use strict file permissions
✅ Provide easy export/deletion
✅ No network calls
✅ No analytics
✅ No tracking

### What We Don't Do

❌ Cloud sync
❌ External APIs
❌ Share your data
❌ Track usage
❌ Require internet

### Your Rights

- **Ownership**: You own all your data
- **Privacy**: No one can access without your device
- **Portability**: Export anytime (JSON, CSV, Markdown)
- **Deletion**: Delete all data easily
- **Control**: You decide what to track

## Important Disclaimers

### This is NOT Therapy

This plugin is a journaling and tracking tool. It:
- Supports your mental health journey
- Helps you notice patterns
- Provides coping techniques
- Connects you to resources

It is NOT:
- A replacement for therapy
- A diagnostic tool
- A treatment
- A substitute for professional care

### When to Seek Professional Help

Please see a mental health professional if:
- You have suicidal thoughts
- You're in crisis
- Mood problems persist (2+ weeks)
- Functioning is significantly impaired
- You need diagnosis or medication

Resources:
- Psychology Today: Find a therapist
- OpenCounseling: Low-cost options
- NAMI: Support and resources
- Crisis lines: See crisis-resources skill

### Crisis Situations

If you're in crisis:
1. **Call crisis line immediately**: 988 (US) or your country's line
2. **Go to emergency room** if in danger
3. **Tell someone you trust**
4. **Use @crisis-helper** for resources and support

**You are not alone. Help is available.**

## Use Cases

### For Therapy Clients

- Prepare for sessions
- Track progress between appointments
- Notice patterns to discuss
- Process insights from therapy

### For Those Exploring Mental Health

- Build self-awareness
- Learn coping skills
- Track mood over time
- Understand triggers

### For Crisis Prevention

- Notice warning signs early
- Build coping library
- Track what helps
- Stay connected to resources

### For Personal Growth

- Process emotions
- Practice gratitude
- Develop self-compassion
- Build emotional vocabulary

## Best Practices

1. **Daily check-ins** - Consistency reveals patterns
2. **Honesty** - It's private, be real
3. **Explore patterns** - Monthly analysis
4. **Build coping library** - Note what works
5. **Share with therapist** - If helpful
6. **Backup regularly** - Protect your insights
7. **Professional support** - This supplements, not replaces

## Agents Overview

### mood-tracker
Daily mood check-ins with evidence-based scales (PHQ-9, GAD-7 inspired). Tracks overall mood, energy, anxiety, sleep quality, emotions, and triggers. Provides gentle insights and crisis detection.

### journal-assistant
Therapeutic writing support with guided prompts. CBT/DBT-inspired journaling for emotional processing, therapy prep/debrief, trigger analysis, and gratitude practice.

### pattern-analyzer
Privacy-preserving analytics to discover mood trends, common triggers, emotion patterns, and what helps. Connects insights to actionable coping strategies.

### coping-guide
Evidence-based coping techniques matched to your current state. Includes grounding, breathing, CBT reframing, DBT skills, and self-compassion practices.

### crisis-helper
Immediate crisis resources and supportive presence. Provides global hotlines, safety planning, grounding techniques, and professional referral.

## Skills Overview

### mental-health/SKILL.md
Comprehensive best practices including CBT techniques, DBT skills, grounding methods, self-compassion practices, therapeutic prompts, and pattern analysis guidelines.

### mental-health/mood-scales.md
Evidence-based assessment scales including PHQ-9 inspired depression screening, GAD-7 inspired anxiety screening, and validated mood/sleep/energy scales.

### mental-health/emotion-taxonomy.md
Comprehensive emotion categorization covering primary emotions (joy, sadness, anger, fear, disgust, surprise) and complex emotional states.

### mental-health/crisis-resources.md
Global crisis hotlines and support services covering 40+ countries, specialized support (LGBTQ+, veterans, substance abuse), and emergency resources.

## Ethics & Values

This plugin is built on:
- **Compassion**: Every interaction is supportive
- **Evidence**: Only proven techniques
- **Privacy**: Absolute data protection
- **Empowerment**: You have agency
- **Professional respect**: Encourages mental health care
- **Hope**: Recovery and growth are possible

## License

MIT License

**Disclaimer**: This plugin is not medical advice. Consult mental health professionals for diagnosis and treatment.

## Resources

- **NAMI** (National Alliance on Mental Illness): nami.org
- **Mental Health America**: mhanational.org
- **Crisis Text Line**: crisistextline.org
- **Therapy directories**: psychologytoday.com, openpathcollective.org
- **International Association for Suicide Prevention**: iasp.info

---

**You deserve support. Your mental health matters. Help is available.**
