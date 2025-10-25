# Innovation Consultant Plugin

Innovation strategy and ideation specialist for generating new product ideas, analyzing trends, validating concepts, and designing pilot programs.

## Overview

The Innovation Consultant plugin provides agents for systematic innovation using proven frameworks, trend analysis, rigorous concept validation, and pilot program design to turn ideas into tested solutions.

## Agents

### 1. idea-generator (Sonnet, Skill-Aware, WebSearch)
Facilitates idea generation using creative frameworks like SCAMPER, Design Thinking, Jobs-to-be-Done, and Blue Ocean Strategy.

**Use for**: Brainstorming sessions, new product ideas, feature innovation, business model innovation

**Example**:
```
Use idea-generator to create 10 product ideas for improving remote team collaboration.
Target users: Distributed software teams (10-50 people)
Context: Current tools lack async collaboration and timezone awareness
Frameworks: Use SCAMPER and Jobs-to-be-Done
Include: WebSearch for latest remote work trends
```

### 2. trend-analyzer (Sonnet, WebSearch)
Analyzes industry trends, emerging technologies, and market shifts to identify innovation opportunities.

**Use for**: Technology trends, market analysis, competitive landscape, future forecasting

**Example**:
```
Use trend-analyzer to analyze AI trends for healthcare in 2024-2025.
Focus areas: Diagnostic AI, patient monitoring, drug discovery
Include: Gartner Hype Cycle positioning, adoption timelines, key players
Sources: Industry reports, research papers, vendor announcements
```

### 3. concept-validator (Sonnet, Skill-Aware)
Validates concepts using frameworks like Lean Canvas, Value Proposition Canvas, feasibility analysis, and market sizing.

**Use for**: Idea evaluation, business case development, go/no-go decisions, prioritization

**Example**:
```
Use concept-validator to validate: AI-powered meeting note-taker
Frameworks: Lean Canvas, Value Proposition Canvas
Analysis: Market size, competitive landscape, technical feasibility
Criteria: Desirability, Viability, Feasibility
Output: Go/no-go recommendation with scorecard
```

### 4. pilot-designer (Sonnet, Skill-Aware)
Designs pilot programs to test concepts with minimal risk: hypothesis, metrics, timeline, budget, success criteria.

**Use for**: MVP planning, proof of concept, beta programs, market tests

**Example**:
```
Use pilot-designer to design 90-day pilot for new SaaS feature.
Feature: AI writing assistant for emails
Target: 50 beta users from enterprise customers
Budget: $25K
Success metrics: Usage rate, time saved, NPS, conversion intent
Include: Testing plan, feedback loops, iteration cycles
```

## Skills

### innovation-strategy
Frameworks for systematic innovation: Design Thinking, Lean Startup, Blue Ocean Strategy, Jobs-to-be-Done, SCAMPER, Disruptive Innovation Theory.

### ideation-frameworks
Creative ideation techniques: Brainstorming, SCAMPER, Six Thinking Hats, Reverse Thinking, Analogical Thinking, Provocation, Constraint-Based Thinking.

## Templates

### innovation-workshop-template.md
Complete workshop structure for facilitated idea generation with activities, timing, and facilitation guides.

### pilot-program-template.md
Pilot program framework with hypothesis, success criteria, metrics, timeline, budget, and risk mitigation.

### concept-validation-scorecard.md
Scoring framework for evaluating ideas on Desirability, Viability, and Feasibility dimensions.

## Workflows

### Complete Innovation Process
```
1. Generate ideas
Use idea-generator with SCAMPER and Jobs-to-be-Done for [problem space]

2. Analyze trends
Use trend-analyzer to research [industry] trends and emerging opportunities

3. Validate concepts
Use concept-validator to score top 5 ideas on Desirability/Viability/Feasibility

4. Design pilot
Use pilot-designer to create 90-day pilot for highest-scoring concept
```

## Requirements Met

✅ Role: Innovation strategy and ideation specialist
✅ Idea generation facilitation: idea-generator with creative frameworks
✅ Innovation framework design: innovation-strategy skill with Design Thinking, Lean Startup, etc.
✅ Trend analysis: trend-analyzer with WebSearch for current insights
✅ Concept validation: concept-validator with rigorous scoring frameworks
✅ Pilot program design: pilot-designer with hypothesis-driven testing
✅ Tools: Research tools (WebSearch), frameworks (skills), file operations

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 2 comprehensive skills with innovation frameworks
- ✅ 3 professional templates for workshops, pilots, and validation
- ✅ Complete README with workflows

Closes #65
