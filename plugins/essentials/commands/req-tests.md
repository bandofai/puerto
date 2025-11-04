# Generate test plan from requirements

Create comprehensive test scenarios based on a requirement document.

# Instructions

When the user runs `/req-tests <name>`:

1. **Validate requirement exists**
   - Check if `.requirements/<name>.md` exists
   - If not found, list available requirements

2. **Read and analyze the requirement**
   - Load `.requirements/<name>.md`
   - Extract:
     - Functional requirements
     - Edge cases and constraints
     - Acceptance criteria
     - User stories

3. **Generate comprehensive test scenarios**

   Create tests covering:

   **a. Unit Tests**
   - Test each functional requirement individually
   - Test edge cases mentioned in requirements
   - Test error conditions
   - Test validation logic

   **b. Integration Tests**
   - Test interactions between components
   - Test external integrations (APIs, databases, etc.)
   - Test data flow through the system

   **c. End-to-End Tests**
   - Test complete user flows from user stories
   - Test acceptance criteria scenarios
   - Test real-world usage patterns

   **d. Edge Case Tests**
   - Test all edge cases mentioned in requirements
   - Test boundary conditions
   - Test error handling
   - Test performance under constraints

4. **Structure test scenarios**

   Format:
   ```markdown
   ## Test Scenarios

   ### Unit Tests

   #### Test: [Function/Component Name]
   - **Given:** [Initial state/conditions]
   - **When:** [Action taken]
   - **Then:** [Expected outcome]
   - **Test Type:** Unit
   - **Priority:** High/Medium/Low

   ### Integration Tests

   #### Test: [Integration Point]
   - **Given:** [Setup]
   - **When:** [Integration action]
   - **Then:** [Expected result]
   - **Test Type:** Integration
   - **Priority:** High/Medium/Low

   ### End-to-End Tests

   #### Test: [User Flow]
   - **Scenario:** [User story or flow]
   - **Steps:**
     1. [Step 1]
     2. [Step 2]
     3. [Step 3]
   - **Expected:** [Final outcome]
   - **Test Type:** E2E
   - **Priority:** High/Medium/Low

   ### Edge Case Tests

   #### Test: [Edge Case Description]
   - **Given:** [Edge case setup]
   - **When:** [Edge case trigger]
   - **Then:** [Expected handling]
   - **Test Type:** Edge Case
   - **Priority:** High/Medium/Low
   ```

5. **Ask for preference on storage**
   ```
   Where should I save these test scenarios?

   1. Append to requirements file (.requirements/<name>.md)
   2. Create separate test file (.requirements/<name>-tests.md)
   3. Show only (don't save)
   ```

6. **Save test scenarios**
   Based on user choice:
   - If appending: Add "## Test Scenarios" section to requirement file
   - If separate: Create new test file
   - If show only: Display but don't persist

7. **Generate test code templates** (optional)
   Ask: "Would you like me to generate test code templates?"

   If yes, create example test code in the project's test framework:
   ```javascript
   // Example for Jest
   describe('User Authentication', () => {
     test('should allow login with valid credentials', () => {
       // Given: Valid user credentials
       const credentials = { email: 'user@example.com', password: 'password123' };

       // When: User attempts to login
       const result = login(credentials);

       // Then: Login succeeds
       expect(result.success).toBe(true);
       expect(result.token).toBeDefined();
     });
   });
   ```

8. **Update requirement metadata**
   - Add note that test scenarios were generated
   - Update `lastModified` in `_index.json`

9. **Provide summary**
   ```
   Generated test scenarios:
   - 5 Unit Tests
   - 3 Integration Tests
   - 2 End-to-End Tests
   - 4 Edge Case Tests

   Total: 14 test scenarios covering all requirements
   ```

## Best Practices

- Cover all functional requirements with tests
- Don't forget negative test cases (what should fail)
- Prioritize tests based on critical functionality
- Make tests specific and actionable
- Include setup/teardown considerations
- Consider performance testing for performance requirements
- Include security testing for security requirements
- Map tests back to acceptance criteria
