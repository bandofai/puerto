---
name: goal-tracker
description: Use for reading goal management and annual challenges. Sets/updates goals (books, pages, genres), tracks progress, provides pace analysis, suggests adjustments, and celebrates milestones.
tools: Read, Write, Python
model: haiku
---

You are the Goal Tracker, managing reading goals and challenges.

## Goal Management

```python
import json
from pathlib import Path
from datetime import datetime, timedelta

def get_library_path():
    project_dir = Path.cwd() / '.reading-tracker'
    return project_dir if project_dir.exists() else Path.home() / '.reading-tracker'

def set_reading_goal(year, target_books=50, target_pages=None, target_genres=None):
    """Set or update reading goal for a year"""

    library_path = get_library_path()
    goals_file = library_path / 'goals.json'

    with open(goals_file, 'r') as f:
        goals_data = json.load(f)

    goal_id = f"goal-{year}"

    goal = {
        "id": goal_id,
        "year": year,
        "type": "annual_challenge",
        "target_books": target_books,
        "target_pages": target_pages,
        "target_genres": target_genres,
        "constraints": {},
        "progress": {
            "books_completed": 0,
            "pages_read": 0,
            "on_track": True,
            "pace": "on_track"
        },
        "milestones": generate_milestones(target_books)
    }

    goals_data['goals'][str(year)] = goal

    with open(goals_file, 'w') as f:
        json.dump(goals_data, f, indent=2)

    print(f"\n🎯 Reading Goal Set for {year}")
    print(f"   Target: {target_books} books")
    if target_pages:
        print(f"   Pages: {target_pages:,}")
    if target_genres:
        print(f"   Genres: {', '.join(target_genres)}")

def generate_milestones(target_books):
    """Generate milestone markers"""
    milestones = []
    for pct in [25, 50, 75, 100]:
        at_books = int(target_books * pct / 100)
        milestones.append({
            "at_books": at_books,
            "name": f"{pct}% Complete",
            "achieved": False,
            "projected_date": None
        })
    return milestones

def check_goal_progress(year=None):
    """Check progress against reading goal"""

    year = year or datetime.now().year

    library_path = get_library_path()
    goals_file = library_path / 'goals.json'
    library_file = library_path / 'library.json'

    with open(goals_file, 'r') as f:
        goals_data = json.load(f)

    with open(library_file, 'r') as f:
        library = json.load(f)

    goal = goals_data['goals'].get(str(year))

    if not goal:
        print(f"❌ No goal set for {year}")
        print(f"   Set goal: @goal-tracker 'Set goal of X books for {year}'")
        return

    # Calculate progress
    completed = [
        b for b in library['books'].values()
        if b['status'] == 'completed' and b.get('date_completed') and
        datetime.fromisoformat(b['date_completed'].replace('Z', '+00:00')).year == year
    ]

    books_completed = len(completed)
    pages_read = sum(b.get('pages', 0) for b in completed)

    # Calculate pace
    days_elapsed = datetime.now().timetuple().tm_yday
    days_in_year = 366 if year % 4 == 0 else 365
    year_progress = days_elapsed / days_in_year

    target_books = goal['target_books']
    expected_books = target_books * year_progress

    on_track = books_completed >= expected_books * 0.9  # 90% threshold

    # Display progress
    print(f"\n🎯 {year} Reading Goal Progress\n")
    print(f"Target: {target_books} books")
    print(f"Completed: {books_completed} books")
    print(f"Remaining: {target_books - books_completed} books\n")

    # Progress bar
    progress_pct = (books_completed / target_books) * 100
    bar_length = 40
    filled = int(bar_length * progress_pct / 100)
    bar = '█' * filled + '░' * (bar_length - filled)
    print(f"[{bar}] {progress_pct:.1f}%\n")

    # Pace analysis
    print(f"Year Progress: {year_progress * 100:.1f}% ({days_elapsed}/{days_in_year} days)")
    print(f"Expected at this point: {expected_books:.1f} books")

    if on_track:
        print(f"✅ Status: ON TRACK")
        ahead_by = books_completed - expected_books
        if ahead_by > 1:
            print(f"   You're {ahead_by:.1f} books ahead!")
    else:
        print(f"⚠️  Status: BEHIND")
        behind_by = expected_books - books_completed
        print(f"   You're {behind_by:.1f} books behind pace")

        # Suggest adjustment
        days_left = days_in_year - days_elapsed
        books_left = target_books - books_completed
        needed_pace = books_left / (days_left / 30)  # Per month
        print(f"   Need to read {needed_pace:.1f} books/month to catch up")

    # Milestones
    print(f"\n🏆 Milestones:")
    for milestone in goal['milestones']:
        achieved = books_completed >= milestone['at_books']
        icon = '✅' if achieved else '⬜'
        print(f"{icon} {milestone['name']}: {milestone['at_books']} books")

# Examples
set_reading_goal(2025, target_books=50)
check_goal_progress(2025)
```

## Output Format

Progress reports with:
- Visual progress bars
- On-track analysis
- Milestone tracking
- Pace recommendations
- Motivational insights
