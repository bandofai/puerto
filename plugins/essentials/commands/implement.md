# Implement a requirement

Implement a feature based on its requirements document.

# Instructions

When the user runs `/implement <name>`:

1. **Validate requirement exists**
   - Check if `.requirements/<name>.md` exists
   - If not found, list available requirements and ask user to choose or run `/brainstorm` first

2. **Read and analyze the requirement**
   - Load `.requirements/<name>.md`
   - Parse all sections: overview, **Implementation Strategy**, functional requirements, technical requirements, edge cases, acceptance criteria
   - Extract recommended skill from "Implementation Strategy" section (if present)
   - Understand the full scope before starting

3. **Check for recommended skill**
   - If "Implementation Strategy" section exists:
     - Extract skill name (e.g., "developer", "docs-master", "gpt5-mini-prompting")
     - Read rationale to understand why this skill was chosen
     - Verify skill exists in `.claude/skills/`
   - If no recommendation or skill doesn't exist:
     - Default to `developer` for code-related tasks
     - Ask user for confirmation before proceeding

4. **Update status to in-progress**
   - Update `.requirements/_index.json`:
     ```json
     {
       "<name>": {
         "status": "in-progress",
         "lastWorked": "2025-01-17T11:00:00Z",
         "lastModified": "2025-01-17T11:00:00Z"
       }
     }
     ```

5. **Invoke recommended skill (if available)**
   - If skill was detected in step 3:
     - Announce: "Using `[skill-name]` skill for implementation (as recommended in requirements)"
     - Use Skill tool with the recommended skill name
     - Pass requirement context to the skill
     - The skill will follow its own workflow and best practices
     - Skip to step 8 (skill handles implementation)

   - If no skill or skill doesn't exist:
     - Proceed with manual implementation (steps 6-7)
     - Note: "Manual implementation (no skill recommended or skill unavailable)"

6. **Create implementation plan** (manual implementation fallback)
   Present a clear plan to the user:
   - Break down into logical steps
   - Identify files that need to be created/modified
   - Highlight any dependencies or prerequisites
   - Estimate complexity

   Ask user: "Does this plan look good? Should I proceed?"

7. **Execute implementation systematically** (manual implementation fallback)

   a. **Setup phase**
      - Create necessary directories
      - Set up any configuration files
      - Install dependencies if needed

   b. **Core implementation**
      - Follow the plan step by step
      - Implement according to technical requirements
      - Handle edge cases mentioned in requirements
      - Add proper error handling
      - Include logging where appropriate

   c. **Testing**
      - Write unit tests for core functionality
      - Write integration tests if applicable
      - Test edge cases from requirements
      - Verify acceptance criteria

   d. **Documentation**
      - Add code comments for complex logic
      - Update README if needed
      - Document API endpoints or interfaces

8. **Track progress in requirements file**
   - Check off items in the Implementation Checklist
   - Mark completed acceptance criteria
   - Add notes about implementation decisions
   - Note which skill was used (if applicable)

9. **Report completion**
   - Summarize what was implemented
   - Show which acceptance criteria were met
   - Highlight any deviations from original requirements
   - Suggest running `/req-status <name>` to verify
   - Update status in `_index.json` to "done" if fully complete

10. **Handle interruptions gracefully**
   - If implementation is interrupted, save state clearly
   - Update `_index.json` with current progress
   - Note which skill was being used (if applicable)
   - User can resume with `/continue <name>`

## Best Practices

- **Prioritize skill-based implementation**: If a skill is recommended, use it instead of manual implementation
- Always confirm the plan before executing (unless skill is handling it)
- Implement incrementally, not all at once
- Test as you go, don't wait until the end
- Keep the user informed of progress
- If requirements are unclear, ask for clarification before implementing
- Follow existing code patterns and project conventions
- Prioritize code quality and maintainability
- Trust the skill's workflow - skills encode project-specific best practices
