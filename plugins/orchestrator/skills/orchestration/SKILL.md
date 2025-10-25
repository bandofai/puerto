# Orchestration Skill

**Expert patterns for coordinating multiple Claude Code subagents in complex workflows**

This skill codifies strategies for breaking down complex requests into coordinated subagent executions, managing dependencies, parallelizing work, and aggregating results.

---

## Core Philosophy

**The orchestrator doesn't DO the work - it coordinates those who do.**

Key principles:
- Subagents cannot invoke other subagents (architectural constraint)
- Main Claude instance executes the coordination plan
- Orchestration is about intelligent task decomposition and sequencing
- Parallel execution maximizes throughput
- Clear handoffs prevent confusion
- Aggregation adds value beyond sum of parts

---

## Part 1: Understanding Orchestration Constraints

### 1.1 The Subagent Execution Model

**How it ACTUALLY works**:
```
Main Claude
    ↓ (invokes)
Subagent A
    ↓ (returns result)
Main Claude
    ↓ (invokes with context)
Subagent B
    ↓ (returns result)
Main Claude (aggregates)
```

**What subagents CANNOT do**:
- ❌ Invoke other subagents directly
- ❌ Access results from other subagents
- ❌ Coordinate parallel execution
- ❌ Make orchestration decisions

**What subagents CAN do**:
- ✅ Return structured output
- ✅ Suggest next steps
- ✅ Provide status information
- ✅ Write state to files (for coordination)

### 1.2 Main Claude's Role

The main Claude instance is the **execution engine**:
- Reads orchestration plans
- Invokes subagents in correct order
- Manages parallel execution groups
- Passes context between subagents
- Aggregates final results
- Handles errors and retries

---

## Part 2: Task Decomposition Patterns

### 2.1 Dependency Analysis

**Questions to ask**:
1. What are the atomic tasks?
2. Which tasks depend on others?
3. Which tasks can run in parallel?
4. What data flows between tasks?
5. What are the failure modes?

**Dependency Types**:

| Type | Description | Example |
|------|-------------|---------|
| **Sequential** | B needs A's output | Spec → Implementation |
| **Parallel** | Independent tasks | Multiple file analysis |
| **Fan-out** | One input, many processors | Code review by multiple specialists |
| **Fan-in** | Many inputs, one aggregator | Collect all test results |
| **Conditional** | Depends on A's result | If tests pass → deploy |

### 2.2 Decomposition Strategies

**Strategy 1: Pipeline (Sequential)**
```
Task: "Build and deploy new feature"

Decomposition:
1. requirements-analyzer → spec
2. architect-reviewer → ADR (uses spec)
3. feature-builder → code (uses ADR)
4. test-runner → results (uses code)
5. deployment-manager → deployed (if tests pass)
```

**Strategy 2: Parallel Divide-and-Conquer**
```
Task: "Analyze codebase for issues"

Decomposition:
Parallel Group 1:
- security-scanner → security report
- code-reviewer → quality report
- performance-analyzer → perf report
- dependency-checker → dependency report

Sequential:
- report-aggregator → comprehensive analysis (uses all reports)
```

**Strategy 3: Iterative Refinement**
```
Task: "Create comprehensive documentation"

Decomposition:
1. docs-outliner → structure
2. Parallel:
   - api-documenter → API docs (uses structure)
   - tutorial-writer → tutorials (uses structure)
   - example-creator → code examples (uses structure)
3. docs-reviewer → feedback (uses all docs)
4. docs-refiner → final docs (uses feedback)
```

**Strategy 4: Specialist Consultation**
```
Task: "Design system architecture"

Decomposition:
1. architect-planner → initial design
2. Parallel consultation:
   - security-specialist → security review
   - performance-specialist → performance review
   - scalability-specialist → scalability review
   - cost-specialist → cost analysis
3. architect-synthesizer → final architecture (incorporates all feedback)
```

### 2.3 Execution Plan Format

**Standard JSON structure**:
```json
{
  "plan_id": "task-2025-01-15-001",
  "objective": "Build user authentication feature",
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
          "input": "User request for authentication",
          "output_var": "spec",
          "dependencies": []
        }
      ]
    },
    {
      "stage_id": 2,
      "name": "Design",
      "execution": "sequential",
      "tasks": [
        {
          "task_id": "2.1",
          "agent": "architect-reviewer",
          "input": "${spec}",
          "output_var": "architecture",
          "dependencies": ["1.1"]
        }
      ]
    },
    {
      "stage_id": 3,
      "name": "Implementation",
      "execution": "parallel",
      "tasks": [
        {
          "task_id": "3.1",
          "agent": "backend-builder",
          "input": "${architecture}",
          "output_var": "backend_code",
          "dependencies": ["2.1"]
        },
        {
          "task_id": "3.2",
          "agent": "frontend-builder",
          "input": "${architecture}",
          "output_var": "frontend_code",
          "dependencies": ["2.1"]
        },
        {
          "task_id": "3.3",
          "agent": "test-generator",
          "input": "${architecture}",
          "output_var": "tests",
          "dependencies": ["2.1"]
        }
      ]
    },
    {
      "stage_id": 4,
      "name": "Validation",
      "execution": "sequential",
      "tasks": [
        {
          "task_id": "4.1",
          "agent": "test-runner",
          "input": "${backend_code}, ${frontend_code}, ${tests}",
          "output_var": "test_results",
          "dependencies": ["3.1", "3.2", "3.3"]
        }
      ]
    }
  ],
  "success_criteria": "All tests pass",
  "failure_handling": "If tests fail, invoke debug-specialist with test_results"
}
```

---

## Part 3: Subagent Discovery and Selection

### 3.1 Registry Pattern

**Discover available subagents**:
```bash
# User-level agents
echo "=== User Agents ==="
for agent in ~/.claude/agents/*.md; do
    if [ -f "$agent" ]; then
        NAME=$(grep "^name:" "$agent" | head -1 | cut -d: -f2- | xargs)
        DESC=$(grep "^description:" "$agent" | head -1 | cut -d: -f2- | xargs)
        echo "- $NAME: $DESC"
    fi
done

# Project-level agents
echo -e "\n=== Project Agents ==="
for agent in .claude/agents/*.md; do
    if [ -f "$agent" ]; then
        NAME=$(grep "^name:" "$agent" | head -1 | cut -d: -f2- | xargs)
        DESC=$(grep "^description:" "$agent" | head -1 | cut -d: -f2- | xargs)
        echo "- $NAME: $DESC"
    fi
done
```

### 3.2 Intelligent Agent Selection

**Matching strategies**:

**Keyword Matching**:
```
Task: "Review code for security"
Keywords: ["review", "security"]
→ Matches: "security-scanner", "code-reviewer"
→ Select: security-scanner (more specific)
```

**Capability Matching**:
```
Task: "Create PowerPoint presentation"
Required capability: Document creation (pptx)
→ Filter agents with: tools includes "Write", description includes "presentation"/"pptx"
→ Select: presentation-creator
```

**Tool Matching**:
```
Task: "Deploy to production"
Required tools: Bash (for deployment commands)
→ Filter agents with: tools includes "Bash", description includes "deploy"
→ Select: deployment-manager
```

**Exclusion Patterns**:
```
# Read-only analysis task
→ Exclude agents with: "Write", "Edit" tools
→ Prefer agents with: "Read", "Grep", "Glob" only
```

### 3.3 Fallback Strategies

**When no exact match exists**:

1. **Composition**: Use multiple general agents
   ```
   No "api-tester" agent
   → Use: test-generator + test-runner
   ```

2. **Generalist fallback**: Use main Claude
   ```
   No specialized agent available
   → Execute task directly without delegation
   ```

3. **Recommendation**: Suggest agent creation
   ```
   Task requires specialized capabilities repeatedly
   → "This task would benefit from a dedicated agent"
   → Use ultimate-subagent-creator to build one
   ```

---

## Part 4: Parallel Execution Patterns

### 4.1 Independent Parallel Tasks

**When to parallelize**:
- ✅ Tasks have no dependencies
- ✅ Each task has separate inputs
- ✅ Order doesn't matter
- ✅ Results can be aggregated independently

**How to execute (Main Claude)**:
```markdown
I'll run these tasks in parallel:

<invoke security-scanner>
<invoke code-reviewer>
<invoke performance-analyzer>

(All three tool calls in single message)
```

**Result aggregation**:
```markdown
After receiving all results:

## Security Analysis
[From security-scanner]

## Code Quality
[From code-reviewer]

## Performance Issues
[From performance-analyzer]

## Summary
Consolidated findings across all dimensions...
```

### 4.2 Dependent Parallel Groups

**Pattern**: Multiple parallel stages with sequential dependencies

```
Stage 1 (Sequential):
  spec-writer → specification

Stage 2 (Parallel, depends on Stage 1):
  architecture-reviewer → arch-review
  security-reviewer → security-review
  ux-reviewer → ux-review

Stage 3 (Sequential, depends on Stage 2):
  spec-refiner → final-spec (incorporates all reviews)
```

**Execution**:
```markdown
Step 1: Invoke spec-writer
[Wait for result]

Step 2: Invoke all reviewers in parallel with spec as input
<invoke architecture-reviewer with spec>
<invoke security-reviewer with spec>
<invoke ux-reviewer with spec>
[Wait for all results]

Step 3: Invoke spec-refiner with all reviews
<invoke spec-refiner with all review results>
```

### 4.3 Fan-Out/Fan-In Pattern

**Use case**: Process multiple items with same agent

```
Task: "Review all Python files for security"

Discovery:
  find . -name "*.py" → 15 files

Fan-out (Parallel):
  security-scanner(file1)
  security-scanner(file2)
  ...
  security-scanner(file15)

Fan-in (Aggregate):
  Consolidate all findings
  Deduplicate issues
  Prioritize by severity
  Generate summary report
```

**Batching strategy**:
```
If >10 files:
  Batch into groups of 5
  Process each batch in parallel
  Prevents overwhelming context
```

---

## Part 5: Context Passing and State Management

### 5.1 Passing Output Between Agents

**Direct context passing**:
```markdown
Step 1: Get specification
<invoke requirements-analyzer>
Result: [spec content stored in variable]

Step 2: Pass to architect
<invoke architect-reviewer>
Prompt: "Review this specification: [insert spec content]"
```

**File-based handoffs**:
```markdown
Step 1: Agent A writes output
Agent A creates: .claude/work/task-001/spec.md

Step 2: Agent B reads input
<invoke architect-reviewer>
Prompt: "Review specification at .claude/work/task-001/spec.md"
```

### 5.2 State Files for Coordination

**Queue-based workflow**:
```json
// .claude/queue.json
{
  "tasks": [
    {
      "id": "task-001",
      "status": "READY_FOR_ARCH_REVIEW",
      "artifacts": {
        "spec": ".claude/work/task-001/spec.md"
      },
      "next_agent": "architect-reviewer"
    }
  ]
}
```

**Workflow status tracking**:
```json
// .claude/work/task-001/status.json
{
  "task_id": "task-001",
  "current_stage": "implementation",
  "completed_stages": ["analysis", "architecture"],
  "pending_stages": ["testing", "review", "deployment"],
  "artifacts": {
    "spec": "spec.md",
    "architecture": "architecture.md",
    "code": "src/"
  }
}
```

### 5.3 Error State Handling

**Recording failures**:
```json
{
  "task_id": "task-001",
  "status": "FAILED",
  "failed_stage": "testing",
  "error": "3 tests failed",
  "failed_agent": "test-runner",
  "retry_count": 1,
  "max_retries": 3,
  "next_action": "debug-specialist"
}
```

---

## Part 6: Result Aggregation Strategies

### 6.1 Simple Concatenation

**When**: Results are independent sections

```markdown
# Comprehensive Analysis Report

## Security Assessment
[Full output from security-scanner]

## Code Quality Review
[Full output from code-reviewer]

## Performance Analysis
[Full output from performance-analyzer]

## Recommendations
Based on all analyses above, here are prioritized actions...
```

### 6.2 Synthesis and Deduplication

**When**: Multiple agents find overlapping issues

```markdown
Received from 3 agents:
- security-scanner: "SQL injection risk in login.py:45"
- code-reviewer: "Unsafe SQL in login.py:45"
- best-practices: "Use parameterized queries in login.py:45"

Synthesized:
**CRITICAL: SQL Injection Vulnerability**
Location: login.py:45
Found by: security-scanner, code-reviewer, best-practices
Issue: Unsafe SQL construction
Fix: Use parameterized queries
```

### 6.3 Cross-Agent Validation

**When**: Agents should agree on facts

```markdown
backend-analyzer says: "API has 15 endpoints"
frontend-analyzer says: "Frontend calls 12 endpoints"

Validation finding:
⚠️ Mismatch detected: 3 backend endpoints unused by frontend
→ Document or deprecate: /api/legacy/*, /api/admin/old
```

### 6.4 Hierarchical Summarization

**When**: Large volumes of detailed results

```
Level 1 (Agent outputs): Detailed findings (1000s of lines)
    ↓
Level 2 (Category summaries): Group by type/severity (100s of lines)
    ↓
Level 3 (Executive summary): Key metrics and top issues (10-20 lines)
    ↓
Level 4 (Action items): Prioritized next steps (3-5 items)
```

---

## Part 7: Error Handling and Recovery

### 7.1 Failure Modes

**Agent not found**:
```markdown
Planned: <invoke specialized-tester>
Error: "Agent specialized-tester does not exist"

Recovery:
1. Check if similar agent exists (test-runner)
2. Use fallback (main Claude performs testing)
3. Suggest creating the agent if needed frequently
```

**Agent fails to complete**:
```markdown
<invoke code-builder>
Result: "Error: Missing dependency requirements.txt"

Recovery:
1. Analyze error message
2. Fix prerequisite (create requirements.txt)
3. Retry agent invocation
```

**Partial success**:
```markdown
<invoke test-runner>
Result: "15/20 tests passed, 5 failed"

Recovery:
1. Extract failed test details
2. Invoke debug-specialist with failures
3. Fix issues
4. Re-run test-runner
```

### 7.2 Retry Strategies

**Immediate retry** (transient failures):
```markdown
Attempt 1: Failed (timeout)
Wait: 5 seconds
Attempt 2: Success
```

**Retry with modification** (input issues):
```markdown
Attempt 1: Failed (invalid format)
Modify: Fix input format
Attempt 2: Success
```

**Escalation** (persistent failures):
```markdown
Attempt 1: Failed
Attempt 2: Failed
Attempt 3: Failed
Escalate: Inform user, request guidance
```

### 7.3 Graceful Degradation

**Progressive fallback**:
```
Ideal: Use 3 specialized agents in parallel
↓ (if one unavailable)
Fallback 1: Use 2 specialized agents + generalist
↓ (if multiple unavailable)
Fallback 2: Use main Claude for all tasks
↓ (if main Claude uncertain)
Fallback 3: Ask user for guidance
```

---

## Part 8: Workflow Patterns

### 8.1 Linear Pipeline

```
A → B → C → D → E
```

**Characteristics**:
- Each stage depends on previous
- Sequential execution only
- Clear error propagation
- Simple to reason about

**Use cases**:
- Traditional SDLC (spec → design → build → test → deploy)
- Document creation (outline → draft → review → finalize)
- Data pipelines (extract → transform → validate → load)

### 8.2 Diamond Pattern

```
    A
   / \
  B   C
   \ /
    D
```

**Characteristics**:
- Parallel middle stages
- Single aggregation point
- Faster than linear
- Requires result merging

**Use cases**:
- Multi-aspect review (security + quality reviews → aggregate)
- Parallel implementation (frontend + backend → integration)
- Distributed analysis (multiple analyzers → synthesis)

### 8.3 Iterative Refinement

```
A → B → C
    ↑   ↓
    ← D ←
```

**Characteristics**:
- Feedback loops
- Progressive improvement
- Multiple iterations
- Convergence criteria needed

**Use cases**:
- Code optimization (implement → test → profile → refine → test...)
- Document writing (draft → review → revise → review...)
- Design iteration (prototype → feedback → improve → feedback...)

### 8.4 Conditional Branching

```
A → B → [condition]
        ├─ true → C → E
        └─ false → D → E
```

**Characteristics**:
- Decision points
- Different paths
- Conditional execution
- Eventual convergence

**Use cases**:
- CI/CD (test → [pass?] → deploy : fix)
- Validation (check → [valid?] → proceed : reject)
- Triage (analyze → [severity?] → urgent-path : normal-path)

---

## Part 9: Advanced Patterns

### 9.1 Hierarchical Orchestration

**Multi-level coordination**:
```
Main Orchestrator
  ├─ Feature A Orchestrator
  │   ├─ Backend Team
  │   │   ├─ API Builder
  │   │   └─ Database Designer
  │   └─ Frontend Team
  │       ├─ UI Builder
  │       └─ State Manager
  └─ Feature B Orchestrator
      └─ ...
```

**When to use**:
- Very large projects
- Multi-team coordination
- Modular decomposition
- Parallel feature development

### 9.2 Event-Driven Orchestration

**Trigger-based coordination**:
```
Event: "Code pushed to branch"
  → Trigger: test-runner
  → If tests pass → Trigger: code-reviewer
  → If review approved → Trigger: deployment-manager
```

**Implementation**:
```bash
# Git hook: post-commit
#!/bin/bash
echo '{"event": "commit", "branch": "'$(git branch --show-current)'"}' >> .claude/events.log

# Hook: UserPromptSubmit.sh checks events
if grep -q '"event": "commit"' .claude/events.log; then
    echo "Detected new commit. Run test-runner to validate changes."
fi
```

### 9.3 Resource-Aware Orchestration

**Optimize based on constraints**:
```json
{
  "constraints": {
    "max_parallel": 3,
    "token_budget": 50000,
    "time_limit_minutes": 10
  },
  "optimizations": {
    "prefer": "parallel",
    "model_selection": "minimize_cost",
    "batch_size": "adaptive"
  }
}
```

**Adaptive batching**:
```
If token_budget > 100k:
  Batch size: 10 parallel tasks
Else if token_budget > 50k:
  Batch size: 5 parallel tasks
Else:
  Sequential execution
```

---

## Part 10: Orchestration Anti-Patterns

### 10.1 Over-Orchestration

**❌ BAD**: Breaking simple tasks into unnecessary steps
```
Task: "Add a comment to function"
Plan:
  1. comment-analyzer → analyze existing comments
  2. comment-style-checker → determine style
  3. comment-writer → write comment
  4. comment-reviewer → review comment
```

**✅ GOOD**: Just do it directly
```
Task: "Add a comment to function"
Direct execution: Add the comment (no orchestration needed)
```

**Rule**: Only orchestrate if >3 distinct, complex subtasks

### 10.2 Sequential When Parallel Possible

**❌ BAD**: Sequential independent tasks
```
Stage 1: security-scan
Stage 2: code-review (waits for stage 1)
Stage 3: performance-check (waits for stage 2)
```

**✅ GOOD**: Parallel independent tasks
```
Parallel:
  - security-scan
  - code-review
  - performance-check
```

### 10.3 Ignoring Agent Capabilities

**❌ BAD**: Using wrong agent
```
Task: "Create PowerPoint presentation"
Selected: code-reviewer (has Write tool)
```

**✅ GOOD**: Match capabilities
```
Task: "Create PowerPoint presentation"
Selected: presentation-creator (skill-aware, pptx specialist)
```

### 10.4 No Error Handling

**❌ BAD**: Assume success
```
Plan:
  1. build-code
  2. deploy (assumes build succeeded)
```

**✅ GOOD**: Explicit error handling
```
Plan:
  1. build-code
  2. IF build succeeds:
       deploy
     ELSE:
       debug-specialist → fix → retry build
```

### 10.5 Context Loss

**❌ BAD**: Not passing context
```
Agent A produces detailed analysis → saved somewhere
Agent B invoked without context → starts from scratch
```

**✅ GOOD**: Explicit context passing
```
Agent A produces analysis → stored in variable
Agent B invoked WITH analysis → builds on it
```

---

## Part 11: Orchestration in Practice

### 11.1 Example: Feature Implementation

**Request**: "Build user authentication system"

**Orchestration plan**:
```json
{
  "strategy": "pipeline",
  "stages": [
    {
      "stage": 1,
      "tasks": [
        {
          "agent": "requirements-analyzer",
          "purpose": "Extract authentication requirements",
          "output": "auth_spec.md"
        }
      ]
    },
    {
      "stage": 2,
      "execution": "parallel",
      "tasks": [
        {
          "agent": "security-architect",
          "input": "auth_spec.md",
          "purpose": "Design security model",
          "output": "security_design.md"
        },
        {
          "agent": "database-architect",
          "input": "auth_spec.md",
          "purpose": "Design user schema",
          "output": "schema.sql"
        }
      ]
    },
    {
      "stage": 3,
      "execution": "parallel",
      "tasks": [
        {
          "agent": "backend-builder",
          "input": ["security_design.md", "schema.sql"],
          "purpose": "Implement auth API",
          "output": "backend_code"
        },
        {
          "agent": "frontend-builder",
          "input": "security_design.md",
          "purpose": "Implement login UI",
          "output": "frontend_code"
        },
        {
          "agent": "test-generator",
          "input": ["security_design.md", "auth_spec.md"],
          "purpose": "Create auth tests",
          "output": "tests"
        }
      ]
    },
    {
      "stage": 4,
      "tasks": [
        {
          "agent": "test-runner",
          "input": ["backend_code", "frontend_code", "tests"],
          "purpose": "Validate implementation",
          "output": "test_results"
        }
      ]
    },
    {
      "stage": 5,
      "condition": "test_results.passed == true",
      "tasks": [
        {
          "agent": "security-scanner",
          "input": ["backend_code", "frontend_code"],
          "purpose": "Final security audit",
          "output": "security_report"
        }
      ],
      "else": {
        "agent": "debug-specialist",
        "input": "test_results",
        "action": "Fix failures, return to stage 3"
      }
    }
  ]
}
```

**Execution by Main Claude**:
```markdown
Building user authentication system with coordinated subagents:

## Stage 1: Requirements Analysis
<invoke requirements-analyzer>
✅ Specification complete → auth_spec.md

## Stage 2: Architecture Design (Parallel)
<invoke security-architect with auth_spec.md>
<invoke database-architect with auth_spec.md>
✅ Security model designed → security_design.md
✅ Database schema designed → schema.sql

## Stage 3: Implementation (Parallel)
<invoke backend-builder with security_design.md, schema.sql>
<invoke frontend-builder with security_design.md>
<invoke test-generator with security_design.md, auth_spec.md>
✅ Backend implemented
✅ Frontend implemented
✅ Tests created

## Stage 4: Validation
<invoke test-runner with all code and tests>
Result: 28/28 tests passed ✅

## Stage 5: Security Audit
<invoke security-scanner with all code>
✅ No vulnerabilities found

## Deliverables
- Working authentication system
- Comprehensive test coverage
- Security validated
- All artifacts in .claude/work/auth/
```

### 11.2 Example: Codebase Analysis

**Request**: "Comprehensive codebase health check"

**Orchestration plan**:
```markdown
Strategy: Fan-out parallel analysis → fan-in aggregation

## Phase 1: Parallel Analysis
Launch all analyzers simultaneously:
- security-scanner → security_report
- code-reviewer → quality_report
- dependency-checker → dependency_report
- performance-analyzer → performance_report
- test-coverage-analyzer → coverage_report
- documentation-checker → docs_report

## Phase 2: Synthesis
Main Claude aggregates results:
- Combine all findings
- Identify themes across reports
- Prioritize issues by severity and frequency
- Generate executive summary
- Create action plan
```

### 11.3 Example: Document Generation

**Request**: "Create quarterly business review package"

**Orchestration plan**:
```markdown
Strategy: Parallel document creation with shared data

## Phase 1: Data Gathering
data-aggregator → financial_data, metrics_data, achievements

## Phase 2: Parallel Document Creation
All use same data sources:
- excel-report-creator → financial_analysis.xlsx
- ppt-creator → executive_presentation.pptx
- word-report-creator → detailed_report.docx

## Phase 3: Validation
document-validator → check consistency across all documents

## Phase 4: Packaging
package-creator → final_qbr_package.zip
```

---

## Summary: Orchestration Mastery

Effective orchestration requires:

✅ **Understanding constraints**: Subagents can't invoke subagents
✅ **Smart decomposition**: Break tasks by dependencies
✅ **Parallel thinking**: Maximize concurrent execution
✅ **Context management**: Pass data explicitly between agents
✅ **Error handling**: Plan for failures at every stage
✅ **Agent selection**: Match capabilities to requirements
✅ **Result synthesis**: Add value in aggregation
✅ **Adaptive planning**: Adjust based on intermediate results
✅ **Resource awareness**: Optimize for time/cost/quality
✅ **Simplicity bias**: Don't orchestrate if not needed

**The secret**: Orchestration is an art. The best orchestrators know when NOT to orchestrate.

---

**Version**: 1.0
**Last Updated**: January 2025
**Pattern Source**: Analysis of Claude Code subagent architecture

**Remember**: You are the conductor, not the musician. Let the specialists play their instruments.
