# Implement a requirement

Implement a feature based on its requirements document.

# Instructions

When the user runs `/implement <name>`:

1. **Validate requirement exists**
   - Check if `.requirements/<name>.md` exists
   - If not found, list available requirements and ask user to choose or run `/brainstorm` first

2. **Read and analyze the requirement**
   - Load `.requirements/<name>.md`
   - Parse all sections: overview, functional requirements, technical requirements, edge cases, acceptance criteria
   - Understand the full scope before starting

3. **Update status to in-progress**
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

4. **Create implementation plan**
   Present a clear plan to the user:
   - Break down into logical steps
   - Identify files that need to be created/modified
   - Highlight any dependencies or prerequisites
   - Estimate complexity

   Ask user: "Does this plan look good? Should I proceed?"

5. **Execute implementation systematically**

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

6. **Track progress in requirements file**
   - Check off items in the Implementation Checklist
   - Mark completed acceptance criteria
   - Add notes about implementation decisions

7. **Report completion**
   - Summarize what was implemented
   - Show which acceptance criteria were met
   - Highlight any deviations from original requirements
   - Suggest running `/req-status <name>` to verify
   - Update status in `_index.json` to "done" if fully complete

8. **Handle interruptions gracefully**
   - If implementation is interrupted, save state clearly
   - Update `_index.json` with current progress
   - User can resume with `/continue <name>`

## Best Practices

- Always confirm the plan before executing
- Implement incrementally, not all at once
- Test as you go, don't wait until the end
- Keep the user informed of progress
- If requirements are unclear, ask for clarification before implementing
- Follow existing code patterns and project conventions
- Prioritize code quality and maintainability
