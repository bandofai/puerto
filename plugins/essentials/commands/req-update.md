# Update a requirement

Modify an existing requirement document.

# Instructions

When the user runs `/req-update <name>`:

1. **Validate requirement exists**
   - Check if `.requirements/<name>.md` exists
   - If not found, list available requirements or suggest creating one with `/brainstorm`

2. **Load current requirement**
   - Read `.requirements/<name>.md`
   - Show summary of current content

3. **Ask what to update**
   Present options:
   ```
   What would you like to update?

   1. Overview / Goals
   2. User Stories
   3. Functional Requirements
   4. Technical Requirements
   5. Edge Cases & Constraints
   6. Acceptance Criteria
   7. Free-form edit (tell me what to change)
   ```

4. **Handle the update based on choice**

   **For specific sections (1-6):**
   - Show current content of that section
   - Ask: "What changes would you like to make?"
   - Accept additions, modifications, or deletions
   - Update that section while preserving the rest

   **For free-form edit (7):**
   - Ask: "Describe the changes you want to make"
   - Parse user's intent
   - Apply changes to appropriate sections
   - Show what changed

5. **Preview changes**
   Show diff or summary:
   ```
   Changes to be made:

   + Added to Functional Requirements:
     - Support OAuth 2.0 authentication

   ~ Modified in Technical Requirements:
     - JWT tokens → OAuth 2.0 tokens

   - Removed from Edge Cases:
     - Password reset via email (no longer needed)
   ```

6. **Confirm before saving**
   Ask: "Should I save these changes?"

7. **Save updates**
   - Write updated content to `.requirements/<name>.md`
   - Update metadata in `.requirements/_index.json`:
     ```json
     {
       "<name>": {
         "lastModified": "2025-01-17T12:00:00Z",
         "version": 2
       }
     }
     ```
   - Add changelog entry at bottom of requirement file:
     ```markdown
     ## Changelog
     - **2025-01-17**: Updated authentication approach to OAuth 2.0
     - **2025-01-15**: Initial version
     ```

8. **Suggest next steps**
   - If status is "done": "Requirements changed. Consider running `/req-status <name>` to check if implementation still matches."
   - If status is "in-progress": "Updated requirements. You may want to adjust your implementation."
   - If status is "draft": "Requirements updated. Ready to run `/implement <name>`?"

## Best Practices

- Always show what will change before saving
- Preserve existing content unless explicitly asked to remove it
- Maintain document structure and formatting
- Keep changelog for traceability
- If changes affect completed work, warn the user
- Be careful not to lose information during updates
