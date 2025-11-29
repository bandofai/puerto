# Continue implementation

Resume implementation of a requirement that was interrupted.

# Instructions

When the user runs `/continue [name]`:

1. **Determine which requirement to continue**

   a. **If name is provided**: `/continue user-authentication`
      - Use that specific requirement

   b. **If no name provided**: `/continue`
      - Read `.requirements/_index.json`
      - Find the requirement with the most recent `lastWorked` timestamp
      - If none found or multiple with same timestamp, ask user to specify

2. **Load the requirement and current state**
   - Read `.requirements/<name>.md`
   - Extract recommended skill from "Implementation Strategy" section (if present)
   - Check which items in Implementation Checklist are checked
   - Check which Acceptance Criteria are marked done
   - Review any notes about implementation progress
   - Check if a skill was being used previously

3. **Analyze codebase for current state**
   - Use available tools to examine relevant files
   - Identify what has been implemented
   - Find where implementation stopped
   - Look for TODO comments or incomplete code

4. **Determine remaining work**
   - Compare requirements with actual implementation
   - List what's complete
   - List what remains to be done
   - Identify any gaps or issues

5. **Present status to user**
   Show clearly:
   ```
   Continuing: <name>

   ✅ Completed:
   - [Item 1]
   - [Item 2]

   ⏳ In Progress:
   - [Item 3] (partially done)

   ❌ Not Started:
   - [Item 4]
   - [Item 5]

   Next step: [What I'll do next]
   ```

6. **Ask for confirmation**
   "Should I continue with [next step], or would you like to adjust the plan?"

7. **Resume implementation**
   - If a skill was recommended:
     - Announce: "Resuming with `[skill-name]` skill (as recommended in requirements)"
     - Use Skill tool with the recommended skill name
     - The skill will continue from where it left off
   - If no skill or manual implementation:
     - Pick up where it left off manually
     - Follow the same systematic approach as `/implement`
   - Update checklist items as completed
   - Update `_index.json` with `lastWorked` timestamp

8. **Handle completion**
   - If all work is done, mark requirement as "done" in `_index.json`
   - Summarize what was completed in this session
   - Suggest running `/req-status <name>` to verify

## Best Practices

- **Use the same skill that was recommended**: Maintain consistency with original implementation approach
- Always verify current state before continuing
- Don't assume previous implementation was complete
- Check for code quality issues in existing implementation
- Maintain consistency with existing code
- Update the requirements document with any new insights
- If previous implementation has issues, fix them before continuing
- If switching from manual to skill-based (or vice versa), inform the user
