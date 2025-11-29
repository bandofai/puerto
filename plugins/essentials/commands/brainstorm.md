# Interactive Requirements Brainstorming with Intelligent Analysis v2.0

Start an interactive Q&A session with deep codebase analysis and dynamically generated questions.

**⚠️ CRITICAL: THIS COMMAND ONLY GATHERS REQUIREMENTS - NEVER IMPLEMENTS CODE ⚠️**

## STRICT OPERATING MODE: READ-ONLY ANALYSIS

**YOU MUST NEVER:**
- Write, edit, or modify any code files
- Create new source code files (except in `.requirements/` folder)
- Execute implementation commands
- Make code changes of any kind
- Use Edit, Write, or code modification tools
- Suggest or execute implementation during this workflow

**YOU MAY ONLY:**
- Read and analyze existing code
- Search and explore the codebase
- Research best practices
- Ask questions
- Create requirement documents in `.requirements/` folder
- Generate specifications and recommendations

**GOAL:** Gather complete, actionable requirements so implementation can happen later with `/implement` command.

---

## Full Workflow

### Phase 1: Setup & Initialization

When user runs `/brainstorm <description>`:

1. **Parse the request**
   - Extract feature description from arguments
   - Generate slug: kebab-case version (e.g., "add user logging" → "user-logging")

2. **Create timestamped requirement folder**
   - Format: `.requirements/YYYY-MM-DD-HHMM-[slug]/`
   - Example: `.requirements/2025-10-25-1430-user-logging/`

3. **Initialize files**
   - `01-initial-request.md` - Save user's original request verbatim
   - `metadata.json` - Initialize tracking structure
   - Update `.requirements/_current-requirement` with folder name

4. **Initialize metadata.json**
   ```json
   {
     "id": "user-logging",
     "slug": "user-logging",
     "started": "2025-10-25T14:30:00Z",
     "lastUpdated": "2025-10-25T14:30:00Z",
     "status": "active",
     "phase": "discovery",
     "originalRequest": "add user logging",
     "progress": {
       "discovery": { "generated": false, "answered": 0, "total": 0 },
       "analysis": { "status": "pending" },
       "expert": { "generated": false, "answered": 0, "total": 0 }
     },
     "contextFiles": [],
     "relatedFeatures": [],
     "toolsAvailable": ["serena", "context7", "WebSearch"],
     "recommendedSkill": null,
     "skillRationale": null
   }
   ```

5. **Announce**: "Starting requirements gathering for: [description]"

---

### Phase 2: Generate & Ask Discovery Questions

**IMPORTANT: Questions are NOT hardcoded - they are generated dynamically based on the user's request!**

#### Step 2.1: Generate Discovery Questions

Use **sequential thinking** to generate contextual questions:

```
Task: Generate 5-7 discovery questions to gather requirements for: "[user's request]"

Guidelines:
- Analyze what's ambiguous or unclear in the request
- Focus on WHAT the user wants, not HOW to implement
- Questions should clarify scope, behavior, and expectations
- Each question needs 2-5 numbered options with smart defaults
- Mark one option as [default - brief reason why]
- Include "Other (please specify)" for flexibility
- Mix yes/no with multiple choice appropriately

Focus areas based on request context:
- Scope and boundaries of the feature
- User interactions and workflows
- Data/content being worked with
- Performance or scale expectations
- Security/privacy considerations
- Integration with existing systems

Output format for each question:
## Q[N]: [Question Title]
```
[Question text that makes sense for THIS request]

1. [Option 1] [default - reason based on request context]
2. [Option 2]
3. [Option 3]
4. Other (please specify)
```

Available tools: serena (code analysis), context7 (library docs), WebSearch (best practices)

Save all generated questions to: 02-discovery-questions.md
```

**Example output for "add user logging":**
```markdown
## Q1: What should be logged?
```
What information should the logging system capture?

1. Error details and stack traces [default - most common use case]
2. User actions and events
3. Both errors and user actions
4. Other (please specify)
```

## Q2: Where should logs be stored?
```
What's the preferred log storage solution?

1. Local files (rotating logs) [default - simplest approach]
2. Database (queryable logs)
3. External service (e.g., Datadog, LogRocket)
4. Other (please specify)
```
```

**Example output for "build user dashboard":**
```markdown
## Q1: What data should the dashboard display?
```
What key metrics or information will users see?

1. User activity and engagement [default - common dashboard need]
2. System metrics and performance
3. Business analytics and reports
4. Other (please specify)
```

## Q2: Should the dashboard update in real-time?
```
How current should the dashboard data be?

1. Static/on-page-load [default - simplest implementation]
2. Real-time updates (WebSocket/polling)
3. Refresh on user action
4. Other (please specify)
```
```

#### Step 2.2: Ask Questions One at a Time

**UX Rules:**
- Present ONE question at a time
- Wait for user response before next question
- Accept numbered responses (e.g., "1", "2") or free text for "Other"
- Support revisions: user can say "back", "change Q2", or "restart"
- Show progress after every 2-3 questions: "So far: [brief summary]..."
- If user provides just number, auto-select that option

**After all discovery questions answered:**
- Save answers to `03-discovery-answers.md`
- Update `metadata.json` progress
- Announce: "Discovery complete. Starting intelligent codebase analysis..."

---

### Phase 3: Intelligent Codebase Analysis (Autonomous)

**NO USER INTERACTION - Fully autonomous**

**⚠️ CRITICAL REMINDER: READ-ONLY ANALYSIS ONLY - DO NOT IMPLEMENT ANYTHING ⚠️**

Use **sequential thinking** for intelligent analysis:

```
Task: Analyze codebase to support implementing: "[user's request]"

**CRITICAL CONSTRAINTS:**
- DO NOT write, edit, or modify any code files
- DO NOT create new source code files
- DO NOT use Edit, Write, or any code modification tools
- ONLY read, search, and analyze existing code
- ONLY create requirement documents in .requirements/ folder
- Your role is RESEARCH and SPECIFICATION, not implementation

Context from discovery phase:
[Include summary of all discovery answers]

Your objectives:
1. Understand current architecture and technology stack (READ-ONLY)
2. Find similar features or related implementations (READ-ONLY)
3. Identify specific files that will need modification (DOCUMENT, don't modify)
4. Research best practices for this type of feature (RESEARCH ONLY)
5. Determine integration points with existing code (ANALYZE, don't implement)
6. Generate implementation recommendations with rationale (RECOMMEND, don't execute)

Available tools (READ-ONLY usage):
- serena: For finding symbols, searching patterns, analyzing code structure
  * Use find_symbol to locate classes/functions
  * Use search_for_pattern for code patterns
  * Use find_referencing_symbols for dependencies
  * Use get_symbols_overview for file structure
  * DO NOT use replace_symbol_body, insert_after_symbol, insert_before_symbol

- context7: For library/framework documentation
  * Research best practices for libraries used in codebase

- WebSearch: For industry best practices
  * Search for implementation patterns
  * Find security considerations
  * Discover performance optimization techniques

Output required in 04-context-findings.md:

# Codebase Analysis Findings

## Architecture Overview
[High-level structure - technology stack, patterns used]

## Similar Features Found
- `[file-path]` - [what it does, why similar]
- [Include code snippets showing patterns]

## Patterns to Follow
```[language]
// Example from [file-path]:[line-number]
[relevant code snippet]
```
[Explanation of pattern and why it's relevant]

## Files to Modify/Create
- `[path]` - [what changes needed]
- `[path]` - [what to add]

## Integration Points
[How this feature connects to existing code]

## Best Practices Research
[External best practices found via context7/WebSearch]

## Recommended Approach
[Specific implementation strategy with rationale]

## Technical Constraints
[Limitations, dependencies, considerations]
```

**After Phase 3:**
- Save findings to `04-context-findings.md`
- Update `metadata.json` with `contextFiles` and `relatedFeatures`
- Announce: "✅ Read-only analysis complete. Found [N] related features and [N] files to modify (documentation only - no code was changed). Generating expert questions..."

---

### Phase 4: Generate & Ask Expert Questions

**Again, questions are dynamically generated based on findings!**

#### Step 4.1: Generate Expert Questions

Use **sequential thinking** to generate implementation questions:

```
Task: Generate 5-7 expert implementation questions

Input context:
- Original request: "[user's request]"
- Discovery answers: [summary from Phase 2]
- Codebase findings: [summary from 04-context-findings.md]

Guidelines:
- Reference ACTUAL files and patterns found in Phase 3
- Questions should finalize implementation approach
- Include numbered options with defaults based on codebase patterns
- Explain WHY each default makes sense (cite specific findings)
- Focus on HOW to implement, not WHAT to build

Question types to consider:
- Architecture decisions (extend existing vs create new)
- File/component organization
- Library/framework usage patterns
- Code pattern consistency
- Integration approach
- Testing strategy

Output format for each question:
## Q[N]: [Question Title]
```
[Question text referencing actual findings]

1. [Option 1] [default - reason citing analysis]
2. [Option 2]
3. [Option 3]

**Why this matters:**
[Explanation based on Phase 3 findings - cite files, patterns discovered]
```

Save all generated questions to: 05-expert-questions.md
```

**Example output for "add user logging" after finding existing Logger:**
```markdown
## Q6: Should we extend the existing Logger?
```
Found Logger class at `src/utils/logger.ts`. How should we implement user logging?

1. Extend existing Logger class [default - maintains consistency]
2. Create separate UserLogger class
3. Add logging as middleware

**Why this matters:**
Analysis found that `AuthService` and `PaymentService` both use the
existing Logger at src/utils/logger.ts:15. The Logger already supports
Winston with rotating file transport. Extending it maintains architectural
consistency and reuses existing log rotation configuration.
```

## Q7: Which log format should we use?
```
The existing Logger uses JSON format. Should user logging follow this pattern?

1. Yes, use JSON format [default - matches existing pattern]
2. Plain text format
3. Structured format (custom)

**Why this matters:**
Found 47 log statements across the codebase all using JSON format via
`logger.info({...})` pattern. The log aggregator at scripts/analyze-logs.ts
parses JSON format. Consistency enables easier log analysis.
```
```

#### Step 4.2: Ask Expert Questions One at a Time

Same UX rules as Phase 2:
- ONE question at a time
- Accept numbered responses
- Support revisions
- Show progress summaries

**After all expert questions answered:**
- Save answers to `06-expert-answers.md`
- Update `metadata.json`
- Announce: "Expert questions complete. Generating comprehensive requirements specification..."

---

### Phase 5: Generate Comprehensive Requirements Spec

**First: Detect which skill should be used for implementation**

Use this logic to recommend a skill:

```
Analyze:
- Original request keywords
- Files involved from Phase 3 analysis
- Discovery answers (what user wants)
- Expert decisions (implementation approach)

Skill Detection Rules:
1. **developer** skill if:
   - Keywords: "add", "implement", "build", "create", "fix", "refactor", "update [code]"
   - Files: .ts, .tsx, .js, .jsx, .py, .go, .rs (code files)
   - Context: Code implementation, testing, debugging

2. **docs-master** skill if:
   - Keywords: "document", "write docs", "update README", "create guide"
   - Files: .md, CLAUDE.md, AGENTS.md, docs/ folder
   - Context: Documentation, guides, specifications

3. **gpt5-mini-prompting** skill if:
   - Keywords: "tune", "optimize extraction", "confidence", "entity type", "prompt", "cost"
   - Files: prompts-stage1.ts, prompts-stage2.ts, extractor.ts, identifier-config.ts
   - Context: Prompt engineering, entity extraction

4. **skill-creator** skill if:
   - Keywords: "create skill", "extract pattern", "new skill"
   - Files: .claude/skills/
   - Context: Meta-level skill creation

Default: `developer` if ambiguous

If multiple skills apply, recommend primary skill + note secondary tasks.
```

**Then: Create `07-requirements-spec.md` synthesizing all information:**

```markdown
# [Feature Name from Request]

**Created:** [ISO-8601 timestamp]
**Status:** draft
**Last Updated:** [ISO-8601 timestamp]

---

## Overview

[2-3 paragraph summary combining:
- Original request
- Discovery answers (what user wants)
- Analysis findings (current state)
- Implementation approach (expert decisions)]

---

## Implementation Strategy

### Recommended Skill
**Skill:** `[skill-name]`

**Rationale:**
This requirement involves [reason based on analysis]:
- Files to modify: [list from Phase 3]
- Task type: [feature/bugfix/refactor/documentation/optimization]
- Context: [brief explanation of why this skill fits]

The `[skill-name]` skill provides:
[List key capabilities of the skill that apply to this task]

**To implement:** Run `/implement [slug]` which will automatically invoke the `[skill-name]` skill.

**Override:** If you prefer a different approach, edit this section before running `/implement`.

**Secondary tasks:** [If other skills needed, note them here]

---

## Requirements

### Functional Requirements
[From discovery answers - what the feature must do]

1. [Requirement based on discovery Q&A]
2. [Requirement based on discovery Q&A]
3. [Additional requirements inferred]

### User Interactions
[Detailed workflow based on discovery answers]

---

## Technical Implementation

### Architecture Decision
[Based on expert Q&A - chosen approach with rationale]

### Files to Modify
[From Phase 3 analysis and Phase 4 decisions]

- **`[file-path]`**
  - What to change: [description]
  - Pattern to follow: [reference to similar code]

- **`[file-path]`**
  - What to create: [description]

### Technology Stack
[Libraries/frameworks from analysis and decisions]

### Integration Points
[From Phase 3 analysis - how it connects]

---

## Implementation Guide

### Patterns to Follow

```[language]
// From [similar-feature-file]:[line-number]
[code snippet showing pattern to follow]
```
**Apply this pattern for:** [explanation]

### Similar Features for Reference
- **`[file-path]`** - [what it does similarly, line numbers]
- **`[file-path]`** - [pattern to emulate]

### Step-by-Step Approach
1. [Concrete step from expert decisions]
2. [Concrete step referencing files]
3. [Concrete step with pattern reference]

---

## Testing Strategy

[Based on how similar features are tested]

- Unit tests: [approach based on codebase patterns]
- Integration tests: [if needed]
- Test files: [where to add tests, following existing structure]

---

## Edge Cases & Constraints

### Edge Cases to Handle
[From discovery phase and analysis]

### Technical Constraints
[From Phase 3 analysis]

### Performance Considerations
[From discovery answers if applicable]

### Security Considerations
[From discovery answers and analysis]

---

## Acceptance Criteria

- [ ] [Functional criterion from requirements]
- [ ] [Implementation criterion from expert decisions]
- [ ] [Integration criterion from analysis]
- [ ] [Testing criterion]
- [ ] [Documentation criterion]

---

## Implementation Checklist

- [ ] Review similar implementation at `[file-path]:[line]`
- [ ] [Specific action from expert Q&A]
- [ ] Modify `[file-path]` following pattern from `[reference-file]`
- [ ] Add tests in `[test-file-path]` (follow existing test structure)
- [ ] Update documentation at `[doc-path]`
- [ ] [Any security/performance tasks]

---

## References

- **Codebase Analysis:** `04-context-findings.md`
- **Similar Features:**
  - `[file-path]` - [what to learn from it]
- **Best Practices:** [links from WebSearch/context7]
- **Dependencies:** [libraries mentioned in analysis]

---

## Notes

[Any assumptions made, open questions, or alternative approaches considered]
```

**After Phase 5:**
- Update `metadata.json` with recommended skill:
  ```json
  {
    "recommendedSkill": "developer",
    "skillRationale": "Code implementation with testing required"
  }
  ```
- Update `.requirements/_index.json`:
  ```json
  {
    "user-logging": {
      "created": "2025-10-25T14:30:00Z",
      "status": "draft",
      "lastModified": "2025-10-25T15:15:00Z",
      "lastWorked": null,
      "folder": ".requirements/2025-10-25-1430-user-logging/",
      "relatedFeatures": ["auth-service", "payment-logging"],
      "filesInvolved": 5,
      "recommendedSkill": "developer"
    }
  }
  ```
- Show completion summary with **explicit reminder**:

```
✅ Requirements gathering complete!

📁 All documentation saved to: .requirements/[folder]/

⚠️ IMPORTANT: NO CODE WAS MODIFIED
- This was a READ-ONLY analysis phase
- All findings are documented in requirement files
- No source code files were changed

📋 Next Steps:
1. Review requirements: .requirements/[folder]/07-requirements-spec.md
2. When ready to implement: /implement [slug]

This brainstorm session ONLY gathered requirements.
Implementation is a separate step that you control.
```

---

## Best Practices

### Question Flow
- **One at a time** - Never ask multiple questions simultaneously
- **Accept shorthand** - User can respond with just number (e.g., "1")
- **Auto-select defaults** - If user presses enter, use [default]
- **Follow-up intelligently** - Ask clarifying questions based on answers
- **Show progress** - Every 2-3 questions, show summary: "So far we have..."
- **Allow revisions** - User can say "back", "change Q3", or "restart from Q5"

### Analysis Phase
- **CRITICAL: READ-ONLY MODE** - Never use Edit, Write, or code modification tools
- Use sequential thinking for intelligent tool coordination
- Document file paths and line numbers in findings
- Capture code snippets from similar features (for documentation, not implementation)
- Research external best practices
- Generate hypotheses and verify them (through reading, not implementing)
- Track confidence in recommendations
- **STOP if you find yourself about to modify code** - This is requirements gathering only!

### Expert Questions
- Always reference actual files found in analysis
- Explain rationale for defaults using findings
- Give user flexibility to choose different approach
- Use numbered format for consistency
- Include "Why this matters" explanations

### Tool Usage

**ALLOWED TOOLS (Read-Only):**
- ✅ Read - Read existing files
- ✅ Glob - Find files by pattern
- ✅ Grep - Search code content
- ✅ serena (read-only): find_symbol, search_for_pattern, get_symbols_overview, find_referencing_symbols
- ✅ context7 - Research library documentation
- ✅ WebSearch - Research best practices
- ✅ Bash (read-only commands): ls, cat, find, grep, git log, etc.

**FORBIDDEN TOOLS (Implementation):**
- ❌ Edit - NEVER use
- ❌ Write - NEVER use (EXCEPT for creating files in `.requirements/` folder ONLY)
- ❌ NotebookEdit - NEVER use
- ❌ serena (write operations): replace_symbol_body, insert_after_symbol, insert_before_symbol, rename_symbol - NEVER use
- ❌ Bash (write commands): touch, cp, mv (except in `.requirements/`), git commit, npm install - NEVER use
- ❌ Task - NEVER use for implementation agents
- ❌ Any code generation or modification tool

**EXCEPTION:** Write tool is allowed ONLY for creating requirement documents in `.requirements/[timestamp-slug]/` folder. Never write to source code files.

**Guidelines:**
- Check which tools are available before use
- Prefer serena for symbol-level code analysis (READ-ONLY)
- Use context7 for library documentation
- Use WebSearch for industry best practices
- Always document which tools were used in metadata
- **IF YOU CATCH YOURSELF ABOUT TO USE A FORBIDDEN TOOL, STOP IMMEDIATELY**

### User Experience
- Announce phase transitions clearly
- Provide rich context for decisions
- Save progress after each phase
- Support interruption and resumption
- Allow user to review/revise any phase
- Generate actionable, specific outputs

---

## Why This Version Is Optimal

1. ✅ **Adaptive** - Questions change based on what user actually asked for
2. ✅ **Intelligent** - Sequential thinking powers all analysis and generation
3. ✅ **Context-aware** - Expert questions reference actual code found
4. ✅ **Simple tools** - Only serena, context7, WebSearch (no redundant tools)
5. ✅ **User-friendly** - Numbered choices, revisions, progress tracking
6. ✅ **Actionable** - Output includes specific files, patterns, and steps
7. ✅ **Flexible** - Works for any type of request (logging, UI, API, refactoring, etc.)
8. ✅ **Safe** - READ-ONLY mode prevents accidental implementation during requirements gathering

---

## Examples of Adaptive Behavior

### Request: "add logging to error handlers"
- Phase 2 generates questions about: log levels, storage, PII handling, error context
- Phase 3 finds: existing error handlers, current logging setup
- Phase 4 asks: extend current logger? which error handler files to modify?

### Request: "build user dashboard"
- Phase 2 generates questions about: data to show, real-time updates, user personalization
- Phase 3 finds: existing dashboard components, data fetching patterns
- Phase 4 asks: reuse Dashboard layout? follow existing chart library pattern?

### Request: "refactor authentication"
- Phase 2 generates questions about: what to improve, breaking changes okay?, migration path
- Phase 3 finds: current auth implementation, all usage locations
- Phase 4 asks: backward compatibility approach? update all 47 references at once?

**The questions adapt to the request - no more generic "what type of feature is this?"**

---

## Phase Transitions

After each phase, clearly announce:
- ✅ "Phase 1 complete. Generating discovery questions for: [request]..."
- ✅ "Phase 2 complete. Starting READ-ONLY codebase analysis (no code will be modified)..."
- ✅ "Phase 3 complete (READ-ONLY analysis - no code changed). Generating expert questions based on findings..."
- ✅ "Phase 4 complete. Generating comprehensive requirements specification..."
- ✅ "Requirements gathering complete! Review at `.requirements/[folder]/`. NO CODE WAS MODIFIED - implementation is a separate step."

---

## Error Handling

- **If you catch yourself using Edit/Write/modification tools**: STOP IMMEDIATELY, apologize, explain this is read-only mode, continue with read-only analysis
- **If you start implementing code**: STOP IMMEDIATELY, delete any modifications, remind yourself this is requirements gathering only
- If tools unavailable: Skip Phase 3, ask generic expert questions
- If sequential thinking fails: Fall back to manual analysis
- If user abandons mid-session: Save progress in metadata, allow resume
- If folder exists: Ask "Requirement exists. Overwrite, new version, or cancel?"
- **If user asks "can you implement this?"**: Respond "This is requirements gathering phase. Once complete, use `/implement [slug]` to start implementation."
