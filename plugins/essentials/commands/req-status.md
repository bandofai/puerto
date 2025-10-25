# Show requirement implementation status

Compare requirements with actual implementation to show progress and gaps.

# Instructions

When the user runs `/req-status [name]`:

1. **Determine which requirement(s) to check**

   a. **If name provided**: `/req-status user-authentication`
      - Check that specific requirement

   b. **If no name provided**: `/req-status`
      - Show status for all requirements
      - Focus on in-progress and recent ones

2. **Load requirement and analyze**
   - Read `.requirements/<name>.md`
   - Extract all requirements, acceptance criteria, and checklist items

3. **Analyze codebase implementation**
   - Use available tools to examine relevant files
   - Search for related code
   - Check tests
   - Verify functionality exists

4. **Compare requirements vs reality**

   For each requirement, determine:
   - ✅ **Fully Implemented** - Code exists, tests pass, acceptance criteria met
   - ⚠️ **Partially Implemented** - Started but incomplete
   - ❌ **Not Started** - No code found
   - ❓ **Cannot Verify** - Need manual verification

5. **Generate detailed status report**

   **For single requirement:**
   ```
   Status: user-authentication

   Overall Progress: 75% (6/8 items complete)

   Functional Requirements:
   ✅ User can register with email/password
   ✅ User can login with credentials
   ⚠️ Password reset flow (partially done - email not implemented)
   ❌ OAuth integration not started

   Acceptance Criteria:
   ✅ Passwords are hashed
   ✅ JWT tokens are generated
   ⚠️ Password strength validation (basic only, missing special chars)
   ❌ Rate limiting not implemented

   Tests:
   ✅ Unit tests: 12/12 passing
   ⚠️ Integration tests: 3/5 passing
   ❌ E2E tests: Not written

   Issues Found:
   - Password reset emails not configured
   - Rate limiting mentioned in requirements but missing
   - Integration tests failing for OAuth flows
   ```

   **For all requirements:**
   ```
   Requirements Status Overview

   Name                    Progress  Status
   ────────────────────────────────────────────
   user-authentication     75%       in-progress
   payment-flow           100%       done ✅
   admin-dashboard        30%       in-progress
   api-rate-limiting      0%        draft

   Summary:
   - 1 complete
   - 2 in progress (average 52.5% done)
   - 1 not started
   ```

6. **Identify gaps and issues**
   - Requirements with no implementation
   - Partial implementations
   - Missing tests
   - Acceptance criteria not met
   - Code that exists but wasn't in requirements (scope creep)

7. **Provide actionable recommendations**
   ```
   Recommendations:

   High Priority:
   - Complete password reset email integration
   - Implement rate limiting (security requirement)
   - Fix failing integration tests

   Medium Priority:
   - Enhance password validation
   - Add E2E tests

   Low Priority:
   - Start OAuth integration planning
   ```

8. **Update metadata if status changed**
   - If implementation is now complete, update status to "done"
   - Update `lastModified` timestamp

9. **Suggest next actions**
   - If incomplete: "Run `/continue <name>` to finish implementation"
   - If gaps found: "Run `/req-update <name>` to adjust requirements"
   - If complete: "Requirement fully implemented!"

## Best Practices

- Be thorough but don't overwhelm with too much detail
- Highlight critical gaps (security, core functionality)
- Show progress visually (percentages, checkmarks)
- Make it easy to see what needs attention
- Don't just check if files exist - verify functionality
- Consider test coverage as part of "done"
- Flag discrepancies between requirements and implementation
- Provide clear next steps
