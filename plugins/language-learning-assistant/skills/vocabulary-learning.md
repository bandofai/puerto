# Vocabulary Learning Skill

Comprehensive patterns for vocabulary tracking, spaced repetition, and retention optimization.

## Vocabulary Data Structure

```json
{
  "id": "vocab-001",
  "word": "gato",
  "language": "Spanish",
  "targetLanguage": "English",
  "translation": "cat",
  "partOfSpeech": "noun",
  "gender": "masculine",
  "plural": "gatos",
  "pronunciation": "ˈɡa.to",
  "audioUrl": "",
  "difficulty": 1,
  "frequency": "high",
  "cef rLevel": "A1",
  "exampleSentences": [
    {
      "original": "El gato está durmiendo",
      "translation": "The cat is sleeping",
      "audioUrl": ""
    }
  ],
  "synonyms": ["minino", "felino"],
  "antonyms": [],
  "relatedWords": ["perro", "animal", "mascota"],
  "tags": ["animals", "pets", "basic"],
  "notes": "Common household pet",
  "imageUrl": "",
  "dateAdded": "2025-01-15",
  "dateLastReviewed": "2025-02-15",
  "dateNextReview": "2025-02-20",
  "repetitions": 3,
  "easeFactor": 2.5,
  "interval": 5,
  "reviewHistory": []
}
```

## Spaced Repetition Algorithm (SM-2)

### Core Formula
```python
def calculate_next_review(quality, repetitions, interval, ease_factor):
    """
    SM-2 Algorithm Implementation

    quality: 0-5 (user response quality)
    0: Complete blackout
    1: Incorrect, correct answer seemed familiar
    2: Incorrect, correct answer seemed easy to recall
    3: Correct with difficulty
    4: Correct after hesitation
    5: Perfect response
    """

    if quality < 3:
        # Reset if response is poor
        repetitions = 0
        interval = 1
    else:
        if repetitions == 0:
            interval = 1
        elif repetitions == 1:
            interval = 6
        else:
            interval = round(interval * ease_factor)

        repetitions += 1

    # Adjust ease factor
    ease_factor = ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))

    if ease_factor < 1.3:
        ease_factor = 1.3

    next_review = current_date + timedelta(days=interval)

    return {
        "repetitions": repetitions,
        "interval": interval,
        "easeFactor": ease_factor,
        "nextReview": next_review
    }
```

### Interval Schedule Examples
```
Repetition 0: 1 day
Repetition 1: 6 days
Repetition 2: 6 * EF = ~15 days (EF=2.5)
Repetition 3: 15 * EF = ~37 days
Repetition 4: 37 * EF = ~92 days
Repetition 5: 92 * EF = ~230 days
```

## Vocabulary Organization

### By CEFR Level
- **A1**: 500 most common words
- **A2**: Next 500 words (500-1000)
- **B1**: Next 1000 words (1000-2000)
- **B2**: Next 2000 words (2000-4000)
- **C1**: Next 4000 words (4000-8000)
- **C2**: Advanced vocabulary (8000+)

### By Topic/Theme
```
Topics:
├── Daily Life
│   ├── Food & Drink (100 words)
│   ├── Clothing (80 words)
│   ├── Home & Family (120 words)
│   └── Daily Routines (90 words)
├── Work & Education
│   ├── Office (150 words)
│   ├── School (130 words)
│   └── Technology (200 words)
├── Travel & Transportation
│   ├── Directions (70 words)
│   ├── Hotels (90 words)
│   └── Transportation (110 words)
└── Culture & Entertainment
    ├── Sports (80 words)
    ├── Music (60 words)
    └── Literature (120 words)
```

### By Frequency
- **High frequency**: Top 1000 most common words
- **Medium frequency**: Words 1000-5000
- **Low frequency**: Less common but useful
- **Specialized**: Technical, academic, domain-specific

## Review Scheduling

### Daily Review Queue
```python
def get_due_reviews(vocabulary_db, current_date):
    """Get all words due for review today"""
    due_words = []
    for word in vocabulary_db:
        if word['dateNextReview'] <= current_date:
            due_words.append(word)

    # Prioritize by:
    # 1. Overdue words (oldest first)
    # 2. New words (never reviewed)
    # 3. Regular reviews

    return sorted(due_words, key=lambda x: (
        x['repetitions'] == 0,  # New words first
        x['dateNextReview'],     # Then by due date
        -x['difficulty']         # Then by difficulty
    ))
```

### Review Session Structure
1. **Warm-up**: 5 easy reviews
2. **Main session**: Mix of difficulties
3. **Cool-down**: New word introduction
4. **Duration**: 15-20 minutes optimal

## Learning Strategies

### New Word Introduction
- **Batch size**: 5-10 new words per day
- **Context first**: Present in sentence
- **Multiple exposures**: Show 3-5 examples
- **Mnemonic aids**: Memory techniques
- **Visual association**: Images when possible

### Review Techniques
1. **Recognition**: Show word → recall translation
2. **Recall**: Show translation → produce word
3. **Contextual**: Fill in blanks
4. **Listening**: Audio → meaning
5. **Production**: Use in sentence

## Progress Tracking

### Vocabulary Metrics
```python
# Vocabulary size by status
total_words = len(vocabulary_db)
learning_words = len([w for w in vocabulary_db if 0 < w['repetitions'] < 5])
mastered_words = len([w for w in vocabulary_db if w['repetitions'] >= 5])
new_words = len([w for w in vocabulary_db if w['repetitions'] == 0])

# Learning velocity
words_per_day = new_mastered_words / days_learning
projected_fluency = days_to_reach_goal(current_words, goal_words, words_per_day)

# Retention rate
reviewed_words = len(review_history)
successful_reviews = len([r for r in review_history if r['quality'] >= 3])
retention_rate = (successful_reviews / reviewed_words) * 100
```

### Milestone Tracking
```json
{
  "milestones": [
    {"level": "A1", "words": 500, "achieved": true, "date": "2025-01-30"},
    {"level": "A2", "words": 1000, "achieved": false, "progress": 65},
    {"level": "B1", "words": 2000, "achieved": false, "progress": 0}
  ]
}
```

## Best Practices

### Word Selection
- Start with high-frequency words
- Focus on personal relevance
- Include cognates (easier to learn)
- Balance nouns, verbs, adjectives
- Add words from immersion activities

### Study Habits
- **Consistency over intensity**: Daily 15-minute sessions better than weekly marathons
- **Active recall**: Test yourself, don't just re-read
- **Varied practice**: Mix recognition and production
- **Contextual learning**: Always use words in sentences
- **Regular reviews**: Never skip scheduled reviews

### Retention Optimization
- Sleep after study sessions (consolidation)
- Space reviews optimally (SM-2 algorithm)
- Use multisensory learning (visual, audio, kinesthetic)
- Create personal connections to words
- Practice in real conversations

## Common Challenges

### Forgetting Curve
- Most forgetting occurs in first 24 hours
- First review at 1 day is critical
- Spaced repetition counteracts forgetting
- Multiple exposures strengthen memory

### Interference
- Similar words cause confusion
- Separate learning of similar forms
- Use contrastive examples
- Create distinctive mnemonics

### Motivation
- Set achievable daily goals
- Track and visualize progress
- Celebrate milestones
- Vary study activities
- Connect to personal interests

## Advanced Techniques

### Word Families
Group related forms together:
```
Base: "escribir" (to write)
├── Noun: "escritura" (writing)
├── Noun: "escritor" (writer)
├── Adjective: "escrito" (written)
└── Adverb: "por escrito" (in writing)
```

### Collocations
Learn words in common combinations:
```
"hacer" (to do/make):
├── hacer la cama (make the bed)
├── hacer ejercicio (exercise)
├── hacer una pregunta (ask a question)
└── hacer cola (wait in line)
```

### False Friends
Track words that look similar but mean different:
```
Spanish "embarazada" ≠ English "embarrassed"
(means "pregnant")
```

## Integration with Other Skills

### Grammar Connection
- Learn verbs with conjugation patterns
- Include prepositions with verbs
- Note irregular forms

### Immersion Connection
- Add words from movies/podcasts
- Track word exposure frequency
- Note context where word was encountered

### Practice Connection
- Use new words in speaking practice
- Write sentences with new vocabulary
- Test in conversation scenarios
