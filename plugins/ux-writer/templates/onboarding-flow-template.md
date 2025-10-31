# Onboarding Flow Template

A comprehensive template for designing effective user onboarding experiences that get users to value quickly.

## Onboarding Strategy

**Product**: [Your product name]
**Target users**: [Primary user persona]
**Core value**: [Main benefit users get]
**Time to value goal**: [X] minutes
**Onboarding type**: [Linear/Branching/Gradual/Hybrid]

## Success Metrics

**First meaningful action**: [What action shows user "gets it"]
**Aha moment**: [When user experiences core value]
**Activation criteria**: [What defines an activated user]

Target metrics:
- Onboarding completion: [%]
- Time to first value: [minutes]
- 7-day retention: [%]
- Drop-off at step: [Identify critical point]

## Onboarding Flow

### Step 0: Welcome Screen

**Purpose**: Set expectations and build confidence

```
┌─────────────────────────────────────────┐
│  [Product Logo]                         │
│                                         │
│  Welcome to [Product]!                  │
│  Let's get your workspace set up.       │
│                                         │
│  We'll help you [benefit 1], [benefit   │
│  2], and [benefit 3]—all in about       │
│  [X] minutes.                           │
│                                         │
│  [Continue]      [Skip setup]           │
└─────────────────────────────────────────┘
```

**Copy**:
- **Headline**: "Welcome to [Product]! Let's get your workspace set up."
- **Subheadline**: "We'll help you [action 1], [action 2], and [action 3]—all in about [X] minutes."
- **Primary CTA**: "Continue" or "Get started"
- **Secondary CTA**: "Skip setup - I'll explore on my own"

**Design notes**:
- Include friendly illustration or product screenshot
- Show time estimate to set expectations
- Make skip option available but not prominent
- Don't show progress indicator yet (overwhelming)

---

### Step 1: [Essential Setup Action]

**Purpose**: [Why this step matters]
**Time estimate**: ~30 seconds

```
Progress: Step 1 of [total]
┌─────────────────────────────────────────┐
│  Step 1 of 4                            │
│  ■■■■□□□□ 25%                           │
│                                         │
│  [Connect your account / Import data /   │
│   Set up your profile]                  │
│                                         │
│  [Context sentence explaining why this  │
│   matters to the user]                  │
│                                         │
│  [Form fields or action buttons]        │
│                                         │
│  [Continue]         [Back] [Skip]       │
└─────────────────────────────────────────┘
```

**Copy**:
- **Progress**: "Step 1 of 4" + visual progress bar
- **Headline**: "[Action-oriented title]"
  - Examples: "Connect your email", "Import your contacts", "Set up your profile"
- **Context** (1 sentence): "[Why this matters to user]"
  - Examples: "This lets us automatically turn your emails into tasks."
- **Primary CTA**: "Continue" or specific action like "Connect Gmail"
- **Secondary CTA**: "Back" and "Skip for now" (if optional)

**Fields/Actions**:
[List specific fields or buttons needed]

**Validation**:
- Required fields: [List]
- Optional fields: [List]
- Error messages: [See error-message-patterns.md]

**Success indicator**:
When completed: ✓ "[Action] connected" or "[Action] complete"

---

### Step 2: [Second Essential Action]

**Purpose**: [Why this step matters]
**Time estimate**: ~45 seconds

```
Progress: Step 2 of [total]
┌─────────────────────────────────────────┐
│  Step 2 of 4                            │
│  ■■■■■■□□ 50%                           │
│                                         │
│  [Action title]                         │
│                                         │
│  [Context sentence]                     │
│                                         │
│  [Form fields or action interface]      │
│                                         │
│  [Continue]         [Back] [Skip]       │
└─────────────────────────────────────────┘
```

**Copy**:
- **Progress**: "Step 2 of 4"
- **Headline**: "[Second action]"
- **Context**: "[Why this matters]"
- **Primary CTA**: "Continue" or "[Specific action]"
- **Secondary CTA**: "Back" and "Skip for now" (if optional)

**Fields/Actions**:
[List specific fields or buttons]

---

### Step 3: [Third Action]

**Purpose**: [Why this step matters]
**Time estimate**: ~1 minute

```
Progress: Step 3 of [total]
┌─────────────────────────────────────────┐
│  Step 3 of 4                            │
│  ■■■■■■■■■□ 75%                         │
│                                         │
│  [Action title]                         │
│                                         │
│  [Context sentence]                     │
│                                         │
│  [Interface]                            │
│                                         │
│  [Continue]         [Back] [Skip]       │
└─────────────────────────────────────────┘
```

---

### Step 4: Completion

**Purpose**: Celebrate success and show what's unlocked

```
┌─────────────────────────────────────────┐
│  [Success icon or celebration graphic]  │
│                                         │
│  You're all set!                        │
│                                         │
│  Your workspace is ready to use. Here's │
│  what you can do now:                   │
│                                         │
│  ✓ [Core capability 1]                  │
│  ✓ [Core capability 2]                  │
│  ✓ [Core capability 3]                  │
│                                         │
│  Need help? [View quick guide →]        │
│                                         │
│  [Start using [Product]]                │
└─────────────────────────────────────────┘
```

**Copy**:
- **Headline**: "You're all set!" or "Excellent! Your workspace is ready."
- **Subheadline**: "Here's what you can do now:"
- **Feature list**: Bullet points with checkmarks showing unlocked capabilities
- **Help link**: "Need help? View our quick start guide →"
- **Primary CTA**: "Start using [Product]" or "Go to dashboard"

**Design notes**:
- Use celebratory visual (confetti, checkmark, illustration)
- List 3-5 key capabilities they've unlocked
- Provide easy access to help resources
- No secondary CTA (don't distract from main action)

---

## Post-Onboarding: Gradual Feature Introduction

After core onboarding, introduce advanced features contextually:

### Feature Tooltip (Coachmark)

**Trigger**: First time user encounters feature
**Frequency**: Once per feature (respect dismissal)
**Timing**: On interaction, not page load

```
┌─────────────────────────────────┐
│ [Feature name]                   │
│                                 │
│ [1-2 sentence explanation of    │
│  what this does and why it's    │
│  useful. Include keyboard       │
│  shortcut if relevant.]         │
│                                 │
│ [Got it]                  [×]   │
└─────────────────────────────────┘
```

**Example**:
```
Quick Add

Use Quick Add (⌘K) to create tasks, projects, or events from anywhere without leaving your current page.

[Got it]  [×]
```

**Guidelines**:
- Maximum 3-5 tooltips per session
- Spread over time (not all at once)
- Always dismissible
- Point directly to UI element
- Show keyboard shortcuts when relevant

### Empty States (First Use)

**When**: User first accesses a section
**Purpose**: Explain what goes here and encourage first action

```
┌─────────────────────────────────────────┐
│  [Friendly illustration]                │
│                                         │
│  [State name]                           │
│                                         │
│  [1-2 sentences explaining what this    │
│   section is for and why it's useful]   │
│                                         │
│  [Primary action CTA]                   │
│  [Secondary option or help link]        │
└─────────────────────────────────────────┘
```

**Example**:
```
┌─────────────────────────────────────────┐
│  [Dashboard illustration]               │
│                                         │
│  Your dashboard awaits                  │
│                                         │
│  Dashboards give you an at-a-glance     │
│  view of your most important metrics.   │
│  Create your first one to get started.  │
│                                         │
│  [Create dashboard]                     │
│  [See example dashboard]                │
└─────────────────────────────────────────┘
```

---

## Onboarding Best Practices

### Do's ✅

1. **Focus on value, not features**: Show what users can accomplish, not what buttons do
2. **Minimize steps**: Only include essential setup (3-5 steps ideal)
3. **Show progress**: Clear indicators so users know how far they've come
4. **Allow skipping**: Respect user's time and knowledge
5. **Celebrate completion**: Acknowledge their effort and show what's unlocked
6. **Defer advanced features**: Introduce contextually after core setup
7. **Use real data**: Let users work with their own data ASAP
8. **Time estimate**: Tell users how long it will take
9. **Save progress**: Auto-save so users can resume if interrupted
10. **Test frequently**: Watch real users go through onboarding

### Don'ts ❌

1. **Don't show everything**: Overwhelming users leads to abandonment
2. **Don't use fake data**: Demo mode delays real value
3. **Don't force linear paths**: Allow exploration when safe
4. **Don't auto-play videos**: Especially with sound
5. **Don't require social sharing**: Never force users to invite or share
6. **Don't ask for reviews**: Too early—they haven't experienced value yet
7. **Don't use technical jargon**: Plain language only
8. **Don't hide skip option**: Users resent being trapped
9. **Don't repeat info**: If you explained it once, don't ask them to read it again
10. **Don't neglect mobile**: Onboarding must work on all devices

---

## Personalization Options

### Branching Onboarding

Ask users about their role or goal to customize their experience:

```
┌─────────────────────────────────────────┐
│  What brings you to [Product]?          │
│                                         │
│  Choose the option that best describes  │
│  your goal:                             │
│                                         │
│  ◯ I want to [Goal A]                   │
│  ◯ I want to [Goal B]                   │
│  ◯ I want to [Goal C]                   │
│  ◯ I'm just exploring                   │
│                                         │
│  [Continue]                             │
└─────────────────────────────────────────┘
```

Then show relevant onboarding path for each persona.

---

## Accessibility Checklist

- [ ] Keyboard navigation works through all steps
- [ ] Progress announced to screen readers
- [ ] Form labels are properly associated
- [ ] Error messages are linked to fields
- [ ] Skip links available for each step
- [ ] Color contrast meets WCAG AA standards
- [ ] No time limits (or generous with warnings)
- [ ] Focus management between steps
- [ ] All interactive elements have clear focus states
- [ ] Images have appropriate alt text

---

## Measurement Plan

**Track these metrics**:

1. **Completion rate by step**:
   - Step 1: [%]
   - Step 2: [%]
   - Step 3: [%]
   - Final completion: [%]

2. **Time spent per step**:
   - Step 1: [avg time]
   - Step 2: [avg time]
   - etc.

3. **Skip rates**: Which steps are skipped most?

4. **Drop-off analysis**: Where do users abandon?

5. **Activation rate**: Users who complete onboarding AND take first core action

6. **7-day retention**: Users still active after 7 days

7. **Time to value**: How long until first meaningful action

**Iterate based on data**:
- High drop-off at a step? Simplify or remove it
- Low completion? Reduce total steps
- Users skip a step? Maybe it's not essential
- Slow time to value? Front-load the "aha moment"

---

## Usage Instructions

1. **Copy this template** for your product
2. **Fill in each section** with your specific content
3. **Design mockups** based on the wireframes
4. **Write all copy** following UX writing best practices
5. **Test with users** before shipping
6. **Measure and iterate** based on completion and retention data

The goal of onboarding is not to showcase all features—it's to get users to their first success as quickly and clearly as possible. Every word, every step, and every design choice should accelerate that journey.
