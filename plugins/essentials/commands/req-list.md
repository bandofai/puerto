# List all requirements

Show all requirements with their status and metadata.

# Instructions

When the user runs `/req-list`:

1. **Check if requirements directory exists**
   - Look for `.requirements/` directory
   - If not found, show message: "No requirements found. Run `/brainstorm <name>` to create your first requirement."

2. **Read all requirement files**
   - List all `.md` files in `.requirements/` directory (excluding `_index.json`)
   - Load metadata from `.requirements/_index.json`

3. **Display requirements in a table format**

   ```
   Requirements

   Name                    Status        Created      Last Modified
   ────────────────────────────────────────────────────────────────
   user-authentication     in-progress   2025-01-15   2025-01-17
   payment-flow           done          2025-01-14   2025-01-16
   admin-dashboard        draft         2025-01-17   2025-01-17
   api-rate-limiting      in-progress   2025-01-16   2025-01-17
   ```

4. **Add summary statistics**
   ```
   Total: 4 requirements
   ✅ Done: 1
   ⏳ In Progress: 2
   📝 Draft: 1
   ```

5. **Provide helpful next actions**
   - If there are draft requirements: "Run `/implement <name>` to start implementation"
   - If there are in-progress: "Run `/continue <name>` to resume work"
   - If there are done requirements: "Run `/req-status <name>` to verify completion"

6. **Handle empty or missing metadata**
   - If `_index.json` doesn't exist, create it with default values for discovered requirements
   - If a requirement file exists but not in index, add it with default metadata

## Display Options

**Sort by:**
- Default: Last modified (most recent first)
- Can be enhanced to allow sorting by name, status, or created date

**Filter by status** (optional enhancement):
- Show only requirements with specific status
- Example: `/req-list --status in-progress`

## Best Practices

- Keep display clean and easy to scan
- Use emojis sparingly for status indicators
- Show most recently modified first by default
- Make it easy to identify what to work on next
