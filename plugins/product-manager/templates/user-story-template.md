# User Story: [Story Title]

**Story ID**: [US-XXX]
**Epic**: [Link to epic or feature name]
**Created**: [YYYY-MM-DD]
**Last Updated**: [YYYY-MM-DD]

---

## Story

**As a** [persona/user type],
**I want to** [perform some action],
**So that** [achieve some goal/value/benefit].

### User Value

[Explain in 2-3 sentences why this matters to the user and/or business. What problem does it solve? What value does it create?]

---

## Acceptance Criteria

### Scenario 1: [Happy Path / Primary Use Case]

- [ ] **Given** [initial context or precondition]
      **When** [action or event occurs]
      **Then** [expected outcome or result]
      **And** [additional outcome if applicable]

### Scenario 2: [Alternative Path / Edge Case]

- [ ] **Given** [different context or precondition]
      **When** [action or event occurs]
      **Then** [expected outcome or result]
      **And** [additional outcome if applicable]

### Scenario 3: [Error Handling / Validation]

- [ ] **Given** [error condition or invalid input]
      **When** [action occurs]
      **Then** [appropriate error handling]
      **And** [user guidance provided]

### Additional Criteria (Checklist Style)

- [ ] [Specific requirement or behavior]
- [ ] [Specific requirement or behavior]
- [ ] [Specific requirement or behavior]
- [ ] [Performance requirement if applicable]
- [ ] [Security requirement if applicable]
- [ ] [Accessibility requirement if applicable]

---

## Additional Details

### Priority
**[High / Medium / Low]**

**Rationale**: [Why this priority level]

### Story Points / Size
**[1 / 2 / 3 / 5 / 8 / 13]** or **[XS / S / M / L / XL]**

**Estimation Notes**: [Any notes on complexity or sizing]

### Sprint / Release
**Sprint**: [Sprint number / TBD]
**Target Release**: [Version number / Date]

### Dependencies

**Blocked By**:
- [Story ID / Task] - [Description]
- [Story ID / Task] - [Description]

**Blocks**:
- [Story ID / Task] - [Description]

**Related Stories**:
- [Story ID] - [Description]
- [Story ID] - [Description]

---

## Design

### Mockups / Wireframes
- [Link to Figma / Sketch / Design tool]
- [Link to interactive prototype]

### User Flow
[Link to user flow diagram or describe the flow]

### Design Notes
- [Important design consideration]
- [Edge case to handle visually]
- [Accessibility requirement]

---

## Technical Details

### Implementation Notes

**Approach**:
[High-level technical approach - what components/services/APIs are involved]

**Key Technical Considerations**:
- [Technical consideration 1]
- [Technical consideration 2]
- [Technical consideration 3]

### API Changes

**Endpoints Required**:
- `[HTTP METHOD] /api/v1/[endpoint]` - [Description]
- `[HTTP METHOD] /api/v1/[endpoint]` - [Description]

**Request/Response Examples**:
```json
// Request
{
  "field": "value"
}

// Response
{
  "status": "success",
  "data": {}
}
```

### Database Changes

**New Tables**:
- [Table name] - [Description]

**Schema Changes**:
- [Table.field] - [Type] - [Description]
- [Table.field] - [Type] - [Description]

**Migrations**:
- [Description of data migration if needed]

### Third-Party Integrations
- [Service name] - [What it's used for]
- [Service name] - [What it's used for]

### Performance Requirements
- [Requirement 1 - e.g., "Response time < 500ms for p95"]
- [Requirement 2 - e.g., "Support 1000 concurrent users"]

### Security Considerations
- [Security requirement 1]
- [Security requirement 2]
- [Authentication/authorization required]

---

## Testing Requirements

### Unit Tests
- [ ] Test [specific functionality]
- [ ] Test [error handling]
- [ ] Test [edge case]
- [ ] Code coverage ≥ 80%

### Integration Tests
- [ ] Test [end-to-end workflow]
- [ ] Test [API integration]
- [ ] Test [database operations]

### Manual Testing Scenarios

**Test Case 1**: [Title]
1. [Step 1]
2. [Step 2]
3. [Step 3]
**Expected**: [What should happen]

**Test Case 2**: [Title]
1. [Step 1]
2. [Step 2]
**Expected**: [What should happen]

### Accessibility Testing
- [ ] Keyboard navigation works
- [ ] Screen reader compatible
- [ ] Color contrast meets WCAG AA
- [ ] Focus indicators visible
- [ ] ARIA labels present where needed

### Browser/Platform Testing
- [ ] Chrome (latest)
- [ ] Safari (latest)
- [ ] Firefox (latest)
- [ ] Edge (latest)
- [ ] Mobile (iOS Safari, Android Chrome)

---

## Definition of Done

### Code
- [ ] Code implemented according to acceptance criteria
- [ ] Code follows team style guide and conventions
- [ ] Code reviewed and approved by peer(s)
- [ ] No compiler warnings or linter errors
- [ ] Technical debt minimized

### Testing
- [ ] Unit tests written and passing
- [ ] Integration tests written and passing
- [ ] Manual testing completed
- [ ] Edge cases tested
- [ ] Error handling tested
- [ ] Performance requirements met
- [ ] Security review completed (if applicable)
- [ ] Accessibility requirements met

### Documentation
- [ ] Code comments added where needed
- [ ] API documentation updated
- [ ] User documentation updated
- [ ] README updated (if applicable)
- [ ] Changelog updated

### Quality
- [ ] All acceptance criteria verified
- [ ] No known critical or high-priority bugs
- [ ] Product owner demo completed
- [ ] Product owner accepted story
- [ ] Design review completed

### Deployment
- [ ] Deployed to development environment
- [ ] Deployed to staging environment
- [ ] Smoke tests passing on staging
- [ ] Feature flag configured (if applicable)
- [ ] Rollback plan documented
- [ ] Ready for production deployment

### Communication
- [ ] Stakeholders notified of completion
- [ ] Release notes written (if customer-facing)
- [ ] Support team informed (if customer-facing)
- [ ] Sales team informed (if customer-facing)

---

## Out of Scope

**Explicitly NOT included in this story:**
- [Feature or functionality not in scope]
- [Feature or functionality not in scope]
- [Feature or functionality not in scope]

**Future Enhancements** (Separate stories to create):
- [Future enhancement 1]
- [Future enhancement 2]

---

## Questions & Clarifications

**Open Questions**:
1. [Question 1]
   - **Answer**: [Answer when available]
2. [Question 2]
   - **Answer**: [Answer when available]

**Clarifications**:
- [Date] - [Person]: [Clarification provided]
- [Date] - [Person]: [Clarification provided]

---

## Notes & Discussion

### Development Notes
- [Date] - [Developer]: [Note about implementation]
- [Date] - [Developer]: [Note about blocker or issue]

### Product Notes
- [Date] - [PM]: [Note about requirements or priority]
- [Date] - [PM]: [Note about user feedback]

### Design Notes
- [Date] - [Designer]: [Note about design decision]
- [Date] - [Designer]: [Note about usability consideration]

---

## Metrics & Success Criteria

### Success Metrics (Post-Launch)

**User Adoption**:
- [Metric]: [Target] - [How to measure]
- [Metric]: [Target] - [How to measure]

**User Satisfaction**:
- [Metric]: [Target] - [How to measure]
- [Metric]: [Target] - [How to measure]

**Business Impact**:
- [Metric]: [Target] - [How to measure]
- [Metric]: [Target] - [How to measure]

### Measurement Plan
- **Tracking**: [What events/metrics to track]
- **Dashboard**: [Link to analytics dashboard]
- **Review Date**: [When to review metrics]

---

## Changelog

| Date | Change | Changed By |
|------|--------|------------|
| [YYYY-MM-DD] | Story created | [Name] |
| [YYYY-MM-DD] | [What changed] | [Name] |
| [YYYY-MM-DD] | [What changed] | [Name] |

---

## Attachments

- [Link to research document]
- [Link to user feedback]
- [Link to competitive analysis]
- [Link to technical spike]
- [Screenshots or examples]

---

**Story Owner**: [Product Manager Name]
**Technical Lead**: [Engineer Name]
**Designer**: [Designer Name]

**Questions?** Contact [Owner Name] at [email]
