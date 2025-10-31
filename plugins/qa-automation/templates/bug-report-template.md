# [Severity] Brief description of the bug

## Summary
One-sentence description of the issue.

## Environment
- OS: [e.g., macOS 14.0, Ubuntu 22.04, Windows 11]
- Runtime: [e.g., Python 3.11.5, Node.js 18.17.0]
- Framework: [e.g., pytest 7.4.0, jest 29.0.0]
- Dependencies: [relevant package versions]

## Reproduction Steps
1. Step one
2. Step two
3. Step three
4. Observe the error

## Expected Behavior
Clear description of what should happen.

## Actual Behavior
Clear description of what actually happens.

## Error Output
```
Paste error messages, stack traces, or relevant output here
```

## Root Cause (if known)
Brief explanation of what causes the issue.

## Suggested Fix
Specific code or configuration changes to resolve the issue.

```python
# Example fix
def fixed_function():
    try:
        # Add proper error handling
        result = risky_operation()
        return result
    except SpecificError as e:
        logger.error(f"Operation failed: {e}")
        raise HTTPException(status_code=400, detail=str(e))
```

## Additional Context
- Related issues: #123, #456
- Introduced in: commit abc123 or version 1.2.0
- Affects: [specific features, user groups, or environments]
- Workaround: [temporary solution if available]

## Severity Justification
**[Critical/High/Medium/Low]**: [Explain why this severity level is appropriate]

## Attachments
- Screenshots: [if applicable]
- Log files: [attach or link]
- Test results: [relevant output]

---
**Reporter**: [Your name]
**Date**: [YYYY-MM-DD]
**Assigned to**: [Team or person]
**Labels**: bug, [priority], [component]
