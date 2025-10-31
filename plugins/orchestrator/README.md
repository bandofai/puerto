# Orchestrator Plugin

Master coordinator for complex multi-agent workflows. Intelligently decomposes tasks, creates execution plans, and coordinates subagents for optimal parallel execution.

## Overview

The Orchestrator Plugin transforms how you handle complex tasks in Claude Code by providing intelligent task decomposition, parallel execution planning, and multi-agent coordination. Instead of manually managing multiple subagents, the orchestrator analyzes your request, discovers available agents, maps dependencies, and creates optimized execution plans.

## What's Included

### Agent: orchestrator-planner

A strategic planning agent that:
- **Analyzes complex requests** and breaks them into atomic tasks
- **Maps dependencies** to identify parallel execution opportunities
- **Discovers available subagents** and matches them to task requirements
- **Creates structured execution plans** with detailed sequencing
- **Selects optimal strategies** (pipeline, diamond, fan-out, iterative, etc.)
- **Plans error handling** with retry and fallback strategies
- **Optimizes for efficiency** through intelligent parallelization

**Activation**: Automatically activates for complex multi-step requests, or use `@orchestrator-planner`.

### Skill: orchestration

Comprehensive patterns library for coordination including:
- **Task decomposition strategies** for breaking down complexity
- **Orchestration patterns** (pipeline, diamond, fan-out, iterative, conditional, hierarchical)
- **Parallel execution techniques** for maximizing throughput
- **Agent selection algorithms** for optimal capability matching
- **Context passing methods** for data flow between agents
- **Error handling patterns** for robust execution
- **Result aggregation strategies** for synthesizing outputs
- **Anti-patterns** to avoid common mistakes

The main Claude instance reads this skill to execute orchestration plans effectively.

## The Orchestration Model

### How It Works

```
User: Complex multi-step request
    ↓
orchestrator-planner analyzes
    ↓
Creates structured execution plan
    ↓
Returns plan to main Claude
    ↓
Main Claude reads orchestration skill
    ↓
Executes plan (invokes agents as specified)
    ↓
Aggregates results
    ↓
Delivers final output to user
```

**Key Insight**: Subagents can't invoke other subagents (architectural constraint). The orchestrator-planner creates the strategy, and main Claude executes it.

### Why This Architecture?

**Problem**: Claude Code subagents cannot directly invoke other subagents.

**Solution**: Two-component system:
1. **orchestrator-planner**: Strategic planning (this agent)
2. **orchestration skill**: Execution guidance (read by main Claude)

This hybrid approach leverages the strengths of both:
- Planner provides deep analysis and structured plans
- Main Claude executes with coordination skill guidance

## Features

### Intelligent Task Decomposition

Automatically breaks complex requests into optimal task structures:

```
Request: "Build user authentication system"

Plan:
├─ Stage 1: Requirements analysis
├─ Stage 2: Architecture (parallel: security + database)
├─ Stage 3: Implementation (parallel: backend + frontend + tests)
├─ Stage 4: Validation (sequential: test runner)
└─ Stage 5: Security audit (conditional: if tests pass)
```

### Parallel Execution Optimization

Identifies independent tasks and groups them for concurrent execution:

```
Sequential (slow):
A → B → C → D → E    (5 time units)

Parallelized (fast):
A → [B, C, D] → E    (3 time units)
    └─parallel─┘
```

### Smart Agent Discovery

Scans and categorizes available subagents:
- User-level agents (~/.claude/agents/)
- Project-level agents (.claude/agents/)
- Capability matching by description, tools, and specialization
- Fallback strategies when exact matches unavailable

### Multiple Orchestration Patterns

**Pipeline**: Sequential chain
```
spec → architecture → implementation → testing → deployment
```

**Diamond**: Parallel middle stages
```
        analysis
       /    |    \
  security  quality  performance
       \    |    /
       aggregate
```

**Fan-out**: Parallel processing
```
        codebase
    /    |    |    \
  file1 file2 file3 file4  (parallel analysis)
    \    |    |    /
      consolidate
```

**Iterative**: Refinement loop
```
draft → review → refine → review (repeat until approved)
```

**Conditional**: Branching logic
```
tests → [pass?] → deploy
           |
         [fail?] → debug → tests
```

**Hierarchical**: Multi-level coordination
```
Main Orchestrator
├─ Feature A Orchestrator → [sub-agents]
├─ Feature B Orchestrator → [sub-agents]
└─ Integration Orchestrator → [sub-agents]
```

### Comprehensive Error Handling

Every plan includes:
- Retry strategies (immediate, with-modification, escalation)
- Fallback plans for missing agents
- Recovery procedures for failures
- Escalation criteria for user intervention

### Resource Optimization

Considers constraints:
- Token budget optimization (Haiku vs Sonnet vs Opus selection)
- Time limits (parallel vs sequential trade-offs)
- Concurrency limits (max parallel agents)
- Cost efficiency (batch processing, caching)

## Installation

```bash
/plugin install orchestrator@puerto
```

After installation, restart Claude Code to activate the agent and skill.

## Usage

### Automatic Activation

The orchestrator-planner automatically activates for complex multi-step requests:

```
User: "Build a user authentication system with security audit and tests"

orchestrator-planner activates automatically, creates plan, returns to main Claude for execution.
```

### Manual Activation

For explicit orchestration:

```
@orchestrator-planner Analyze how to implement a comprehensive codebase health check
```

### Example Scenarios

#### Scenario 1: Feature Implementation

**Request**:
```
Build user authentication with JWT, bcrypt password hashing, email verification,
and comprehensive tests
```

**Orchestrator creates**:
```
Plan: Pipeline strategy
├─ requirements-analyzer → auth_spec
├─ security-architect → security_design (parallel with ↓)
├─ database-architect → schema_design
├─ backend-builder → auth_api (parallel with ↓)
├─ frontend-builder → login_ui (parallel with ↓)
├─ test-generator → test_suite
├─ test-runner → validation
└─ security-scanner → audit
```

#### Scenario 2: Codebase Analysis

**Request**:
```
Comprehensive analysis of codebase health including security, quality,
performance, dependencies, and test coverage
```

**Orchestrator creates**:
```
Plan: Fan-out strategy
├─ Parallel analysis:
│  ├─ security-scanner → security_report
│  ├─ code-reviewer → quality_report
│  ├─ performance-analyzer → perf_report
│  ├─ dependency-checker → dependency_report
│  └─ coverage-analyzer → coverage_report
└─ Main Claude aggregates → comprehensive_health_report
```

#### Scenario 3: Document Package

**Request**:
```
Create quarterly business review package with Excel financials,
PowerPoint presentation, and Word detailed report
```

**Orchestrator creates**:
```
Plan: Parallel document creation
├─ data-aggregator → financial_data, metrics
├─ Parallel creation (all use same data):
│  ├─ excel-creator → financial_analysis.xlsx
│  ├─ ppt-creator → executive_presentation.pptx
│  └─ word-creator → detailed_report.docx
├─ validator → consistency_check
└─ packager → final_qbr_package.zip
```

#### Scenario 4: When Orchestration Isn't Needed

**Request**:
```
Add a comment to the calculateTotal function
```

**Orchestrator response**:
```
## Orchestration Assessment: Not Needed

This task is straightforward and can be executed directly.

Recommendation: Main Claude can handle this in a single step without
orchestration overhead.
```

The orchestrator knows when NOT to orchestrate.

## Plan Structure

The orchestrator generates detailed JSON execution plans:

```json
{
  "plan_id": "task-2025-01-15-001",
  "objective": "Build user authentication system",
  "complexity": "complex",
  "strategy": "pipeline",
  "stages": [
    {
      "stage_id": 1,
      "name": "Analysis",
      "execution": "sequential",
      "tasks": [
        {
          "task_id": "1.1",
          "agent": "requirements-analyzer",
          "purpose": "Extract authentication requirements",
          "input": "User request",
          "output_var": "auth_spec",
          "dependencies": []
        }
      ]
    }
  ],
  "parallelization": {
    "max_concurrent": 3,
    "parallel_groups": [...]
  },
  "error_handling": {
    "retry_strategy": "immediate",
    "max_retries": 3,
    "fallback_plan": "..."
  },
  "success_criteria": "All tests pass and security audit clean",
  "deliverables": ["auth_api", "login_ui", "tests", "security_report"]
}
```

Plans are saved to `.claude/plans/` for reference and tracking.

## Benefits

### For Complex Projects

- **Faster execution**: Parallel processing reduces total time
- **Better organization**: Clear stages and dependencies
- **Robust handling**: Planned error recovery and retries
- **Optimal resource use**: Right agents for right tasks
- **Visibility**: Structured plans show full scope

### For Multi-Agent Workflows

- **Smart coordination**: Automatic dependency resolution
- **Efficient sequencing**: Maximize parallelization opportunities
- **Context management**: Explicit data flow between agents
- **Capability matching**: Best agent for each subtask
- **Fallback planning**: Handle missing agents gracefully

### For Development Teams

- **Standardized workflows**: Consistent approach to complex tasks
- **Knowledge capture**: Plans document decision-making
- **Reusable patterns**: Learn from previous orchestrations
- **Scalable automation**: Handle increasingly complex projects
- **Quality assurance**: Built-in validation and testing stages

## Configuration

### Agent Settings

**orchestrator-planner**:
- **Tools**: Read, Write, Grep, Glob
- **Model**: Sonnet (requires strategic thinking)
- **Permissions**: Read-only for discovery, writes plans to .claude/plans/

### Skill Location

The orchestration skill can be at:
- `~/.claude/skills/orchestration/SKILL.md` (user-level)
- `.claude/skills/orchestration/SKILL.md` (project-level)

Main Claude reads this automatically when executing plans.

## File Structure

```
orchestrator/
├── agents/
│   └── orchestrator-planner.md    # Planning agent
├── skills/
│   └── orchestration/
│       └── SKILL.md               # Coordination patterns library
└── README.md                       # This file
```

## Advanced Usage

### Hierarchical Orchestration

For very large projects:

```
@orchestrator-planner Create a plan for building a complete e-commerce platform
with user auth, product catalog, shopping cart, payment processing, and admin dashboard
```

The orchestrator may create a hierarchical plan with sub-orchestrators for each major feature.

### Resource-Constrained Planning

```
@orchestrator-planner Optimize for minimal token usage: comprehensive codebase analysis
```

The orchestrator will:
- Prefer Haiku for deterministic tasks (90% cost reduction)
- Batch similar operations
- Skip optional analyses
- Provide cost/quality trade-off analysis

### Adaptive Planning

For uncertain situations:

```
@orchestrator-planner Create a plan with branches for: if codebase has tests use
test-augmentation approach, else use test-generation approach
```

The orchestrator creates conditional plans with decision points.

### Integration with Workflows

The orchestrator works with existing workflow patterns:
- Queue-based coordination (.claude/queue.json)
- Hook-driven automation (.claude/hooks/)
- State-file tracking (.claude/work/*/status.json)

## Best Practices

### When to Use Orchestration

✅ **Use orchestration for**:
- Complex multi-step projects (6+ distinct tasks)
- Tasks requiring multiple specialized agents
- Workflows with parallel execution opportunities
- Coordinated document/code generation
- Large-scale analysis or transformation

❌ **Don't use orchestration for**:
- Simple 1-2 step tasks
- Tasks handled by single agent
- Ad-hoc exploratory work
- Quick fixes or minor edits

### Optimizing Plans

**Maximize parallelization**:
- Identify independent tasks
- Group by stage with explicit dependencies
- Use fan-out for similar operations

**Right-size agents**:
- Haiku for deterministic, template-based work
- Sonnet for domain expertise and judgment
- Opus for deep reasoning and novel problems

**Plan for failures**:
- Define retry strategies upfront
- Specify fallbacks for missing agents
- Set clear escalation criteria

### Working with Plans

**Review before execution**:
```
1. Check agent availability
2. Verify parallel groups make sense
3. Confirm dependencies are correct
4. Validate success criteria
5. Approve or request modifications
```

**Track execution**:
```
Plans saved to .claude/plans/plan-TIMESTAMP.json
Reference during execution
Update if modifications needed
Review after completion for learnings
```

## Troubleshooting

### Orchestrator Doesn't Activate

**Issue**: Simple tasks triggering orchestrator unnecessarily

**Solution**: Orchestrator has built-in complexity assessment. For simple tasks, it recommends direct execution.

### Missing Agents

**Issue**: Plan references agents that don't exist

**Solution**: Orchestrator provides:
- Fallback strategies (use similar agent or main Claude)
- Recommendations for agent creation
- Alternative approaches

### Unexpected Sequential Execution

**Issue**: Tasks that could be parallel are sequential

**Solution**: Review plan's dependency analysis. If incorrect:
```
@orchestrator-planner Please revise: tasks B and C are actually independent
and can run in parallel
```

### Plan Too Complex

**Issue**: Orchestration creates overcomplicated plans

**Solution**:
```
@orchestrator-planner Simplify this plan, prioritize essential tasks only
```

Or execute directly without orchestration for simpler approaches.

## Examples from Production

### Example 1: Multi-Format Documentation

**Request**: "Create API documentation in Markdown, HTML, and PDF formats with examples"

**Plan Generated**:
```
Stage 1: api-analyzer → extracts API endpoints
Stage 2 (parallel):
  - markdown-docs-creator → api.md
  - html-docs-creator → api.html
  - pdf-docs-creator → api.pdf
  - example-generator → code_examples/
Stage 3: docs-validator → consistency check
```

**Execution Time**: 3 stages vs 6 sequential = 50% time savings

### Example 2: Codebase Migration

**Request**: "Migrate Python 2 codebase to Python 3 with testing"

**Plan Generated**:
```
Stage 1: codebase-analyzer → migration_plan
Stage 2: dependency-checker → updated_requirements
Stage 3 (parallel, process files in batches):
  - migrator(batch1) → converted files
  - migrator(batch2) → converted files
  - migrator(batch3) → converted files
Stage 4: test-generator → py3_tests
Stage 5: test-runner → validation
Stage 6 (conditional on tests): deployment
```

**Result**: Parallel file processing + automated testing = reliable migration

### Example 3: Security Audit

**Request**: "Complete security audit with penetration testing report"

**Plan Generated**:
```
Stage 1 (parallel):
  - security-scanner → vulnerability_scan
  - dependency-checker → dependency_audit
  - config-reviewer → configuration_review
  - secrets-scanner → secrets_audit
Stage 2: penetration-tester → pentest_report (uses all stage 1 outputs)
Stage 3: report-generator → executive_summary + technical_details
```

**Value**: Comprehensive coverage through specialist coordination

## Future Enhancements

Planned features:
- **Plan templates**: Reusable orchestration patterns for common tasks
- **Execution tracking**: Real-time progress monitoring
- **Performance analytics**: Compare planned vs actual execution
- **Auto-optimization**: Learn from execution history
- **Agent suggestions**: Recommend new agents based on workflow gaps

## Contributing

This plugin is part of the Puerto marketplace. See main repository for contribution guidelines.

## Support

For issues or questions:
- Review the [orchestration skill](skills/orchestration/SKILL.md) for comprehensive patterns
- Check the [orchestrator-planner agent](agents/orchestrator-planner.md) for planning details
- Refer to [Claude Code subagent documentation](https://docs.claude.com/en/docs/claude-code/sub-agents)

## License

MIT License - See main repository for details

---

**Transform complexity into coordinated excellence. Every complex task, optimally orchestrated.**
