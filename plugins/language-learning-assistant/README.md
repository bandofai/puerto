# Language Learning Assistant Plugin

Vocabulary tracking and language immersion specialist for Puerto.

## Overview

The Language Learning Assistant plugin provides comprehensive tools for language acquisition: vocabulary management with spaced repetition, practice scheduling, immersion tracking, and CEFR-based progress analysis.

## Features

- **Vocabulary Management**: Spaced repetition (SM-2 algorithm) for optimal retention
- **Practice Scheduling**: Structured daily/weekly practice routines
- **Immersion Tracking**: Log movies, podcasts, books, conversations
- **Progress Analysis**: CEFR benchmarking and growth metrics
- **Goal Tracking**: Daily/weekly/monthly learning goals
- **Multi-Skill Development**: Listening, speaking, reading, writing

## Agents

### 1. vocabulary-manager (Haiku)
Fast vocabulary CRUD with spaced repetition.

**Usage:**
```
@vocabulary-manager Add Spanish word "gato" meaning "cat"
@vocabulary-manager Show me words due for review today
@vocabulary-manager Generate a quiz with 20 vocabulary words
```

### 2. practice-scheduler (Haiku)
Practice session scheduling and routine management.

**Usage:**
```
@practice-scheduler Create a daily practice routine for Spanish (A2 level)
@practice-scheduler Schedule conversation practice with tutor on Tuesdays at 7pm
@practice-scheduler Show my practice schedule for this week
```

### 3. immersion-logger (Haiku)
Immersion activity tracking (movies, podcasts, reading, conversations).

**Usage:**
```
@immersion-logger Log: Watched "Amores Perros" (153 min) with English subtitles, 70% comprehension
@immersion-logger Show my immersion hours this week
@immersion-logger What's my average comprehension for podcasts?
```

### 4. progress-analyzer (Sonnet)
Progress analysis, CEFR benchmarking, and insights.

**Usage:**
```
@progress-analyzer Generate my monthly progress report for Spanish
@progress-analyzer What CEFR level am I at based on my vocabulary size?
@progress-analyzer Analyze my skill balance and recommend focus areas
```

## Skills

### vocabulary-learning
Vocabulary tracking, SM-2 spaced repetition algorithm, retention optimization.

### language-practice
Practice patterns, CEFR framework, four-skills development, tutor management.

### immersion-tracking
Immersion logging, comprehension tracking, content optimization, exposure analytics.

## Templates

### vocabulary-database.json
Vocabulary storage with spaced repetition metadata (next review, ease factor, repetitions).

### practice-schedule.json
Daily/weekly practice schedule with time allocations per skill.

### immersion-log.json
Activity log for movies, podcasts, books, conversations with comprehension tracking.

## Getting Started

### 1. Set Your Level
```
@progress-analyzer I'm learning Spanish. I know about 800 words. What CEFR level am I?
```

### 2. Create Practice Schedule
```
@practice-scheduler Create a B1-level Spanish practice schedule (60 min/day)
```

### 3. Add Vocabulary
```
@vocabulary-manager Import common A2-level Spanish vocabulary
```

### 4. Track Immersion
```
@immersion-logger Log: Watched La Casa de Papel S1E1, 47 min, no subtitles, 75% comprehension
```

### 5. Monitor Progress
```
@progress-analyzer Show my weekly progress summary
```

## CEFR Levels

- **A1**: Beginner (500 words, 80-100 hours)
- **A2**: Elementary (1000 words, 180-200 hours)
- **B1**: Intermediate (2000 words, 350-400 hours)
- **B2**: Upper Intermediate (4000 words, 550-650 hours)
- **C1**: Advanced (8000 words, 800-1000 hours)
- **C2**: Proficient (10000+ words, 1200+ hours)

## Best Practices

1. **Daily consistency**: 30-60 minutes daily beats weekend marathons
2. **Spaced repetition**: Review vocabulary on schedule (never skip)
3. **Balanced practice**: Don't neglect speaking/writing (output skills)
4. **Immersion goals**: 7-14 hours weekly of target language exposure
5. **Track everything**: Log all practice for accurate progress analysis

## Cost Optimization

- **Haiku agents** (vocabulary-manager, practice-scheduler, immersion-logger): Fast, frequent operations
- **Sonnet agent** (progress-analyzer): Deep analysis and insights

## License

MIT
