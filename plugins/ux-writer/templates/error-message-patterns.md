# Error Message Patterns Template

Comprehensive error message patterns following the What-Why-How framework for clear, helpful error communication.

## Error Message Framework

Every error should answer:
1. **What happened?** - Clear statement of the problem
2. **Why did it happen?** - Context and reason (when helpful)
3. **How to fix?** - Specific, actionable next steps

## Validation Errors

### Email Address
```
Trigger: Invalid email format
Severity: Minor

❌ "Invalid email"
✅ "Please enter a valid email address (e.g., name@company.com)"

Location: Below email field (inline validation)
Icon: ⚠️
Dismissible: No (clears when corrected)
ARIA: aria-invalid="true" aria-describedby="email-error"
```

### Password Requirements
```
Trigger: Password doesn't meet requirements
Severity: Minor

❌ "Password invalid"
✅ "Your password must be at least 8 characters with 1 number and 1 special character"

Alternative (progressive):
✅ "Password needs:"
   • At least 8 characters ❌
   • 1 number ❌
   • 1 special character (!@#$%^&*) ✓

Location: Below password field
Icon: ⚠️
Dismissible: No
```

### Required Field
```
Trigger: User tries to submit without filling required field
Severity: Minor

❌ "Field required"
❌ "This field cannot be empty"
✅ "We need your phone number to send order updates"
✅ "Please enter your company name"

Location: Below empty field
Icon: ⚠️
Color: Red text + border
```

### Phone Number Format
```
Trigger: Invalid phone format
Severity: Minor

❌ "Invalid phone number"
✅ "Please enter a valid phone number, including area code (e.g., 555-123-4567)"
✅ "Phone number should be 10 digits like 5551234567"

Location: Inline below field
```

### Date Format
```
Trigger: Invalid date entry
Severity: Minor

❌ "Date error"
✅ "Please enter a valid date in MM/DD/YYYY format (e.g., 01/15/2024)"

Alternative (date picker):
✅ "Please select a date from the calendar"
```

### URL Format
```
Trigger: Invalid URL
Severity: Minor

❌ "URL must start with http"
✅ "Please enter a valid URL starting with http:// or https:// (e.g., https://example.com)"
```

### Character Limits
```
Trigger: Input too short
Severity: Minor

❌ "Too short"
✅ "Your username must be at least 3 characters long"

Trigger: Input too long
❌ "Too long"
✅ "Your bio can be up to 500 characters (you've entered 547)"
```

### Duplicate Entry
```
Trigger: Email/username already exists
Severity: Minor

❌ "Duplicate"
❌ "Already exists"
✅ "An account with this email already exists. Try signing in or use a different email."

CTA: [Sign in instead]
```

### File Upload Issues
```
Trigger: File too large
Severity: Minor

❌ "File too big"
✅ "This file is too large (25 MB). Please upload a file under 10 MB."

Trigger: Wrong file type
❌ "Invalid file"
✅ "This file type isn't supported. Please upload a .jpg, .png, or .pdf file."
```

## System Errors

### 500 Internal Server Error
```
Trigger: Server error
Severity: Critical

❌ "Error 500: Internal server error"
❌ "Something went wrong"
✅ "Something went wrong on our end. We've been notified and are working on it. Please try again in a few minutes."

Alternative (if user action critical):
✅ "We couldn't process your request due to a technical issue. We've been notified. Your data is safe. Please try again in 5 minutes or contact support if urgent."

CTA: [Try again] [Contact support]
Status page link: [Check system status]
```

### Network/Connection Error
```
Trigger: No internet or connection timeout
Severity: Moderate

❌ "Request failed"
❌ "Connection error"
✅ "We couldn't connect to our servers. Check your internet connection and try again."

Alternative (offline mode available):
✅ "You're offline. Your changes are saved locally and will sync when you reconnect."

Icon: 📡 or ⚠️
CTA: [Retry]
```

### Request Timeout
```
Trigger: Request takes too long
Severity: Moderate

❌ "Timeout"
✅ "This is taking longer than expected. Your work is saved—you can continue later or try refreshing the page."

Alternative (background processing):
✅ "This is taking a while. We'll continue processing in the background and email you when it's done."

CTA: [Refresh] [Continue later]
```

### Service Unavailable
```
Trigger: Service is down or maintenance
Severity: Critical

❌ "503 Service Unavailable"
✅ "We're currently performing maintenance and will be back soon. Check our status page for updates."

With estimate:
✅ "We're experiencing technical difficulties. We expect to be back online by [time]. Your data is safe."

CTA: [Check status page] [Get notified when we're back]
```

### Rate Limit Exceeded
```
Trigger: Too many requests
Severity: Moderate

❌ "Too many requests"
✅ "You've made too many requests. Please wait a minute and try again."

Alternative (with counter):
✅ "You've reached the rate limit (100 requests per minute). Try again in 45 seconds."
```

## Permission Errors

### Access Denied
```
Trigger: User doesn't have permission
Severity: Moderate

❌ "403 Forbidden"
❌ "Access denied"
✅ "You don't have permission to view this page. Contact your team admin to request access."

Specific:
✅ "Only workspace owners can change billing settings. Ask [Owner Name] to make this change or request owner access."

CTA: [Contact admin] [Request access]
```

### Session Expired
```
Trigger: User session timed out
Severity: Moderate

❌ "Unauthorized"
❌ "401 Error"
✅ "Your session has expired. Please sign in again to continue."

Alternative (with data preservation):
✅ "Your session has expired. Your work has been saved. Sign in to continue where you left off."

CTA: [Sign in]
```

### Read-Only Access
```
Trigger: User tries to edit with read-only permissions
Severity: Minor

❌ "Cannot edit"
✅ "This project is read-only. You can view it but not make changes. Contact the project owner to request edit access."

CTA: [Request edit access]
```

### Plan/Subscription Limitation
```
Trigger: Feature not available in user's plan
Severity: Minor

❌ "Premium feature"
❌ "Access denied"
✅ "This feature is available on Pro and Enterprise plans. Upgrade to unlock it."

Alternative (with value):
✅ "Advanced analytics are available on Pro plans ($29/month). Upgrade to track detailed metrics and generate custom reports."

CTA: [See plans] [Upgrade now]
```

## Not Found Errors

### 404 Page Not Found
```
Trigger: URL doesn't exist
Severity: Moderate

❌ "404 Not Found"
❌ "Page not found"
✅ "We can't find that page. It may have been moved or deleted."

Helpful version:
✅ "This page doesn't exist. It may have been moved or deleted. Return to your dashboard or search for what you need."

CTA: [Go to dashboard] [Search] [Get help]
```

### Resource Deleted
```
Trigger: Accessing a deleted item
Severity: Moderate

❌ "Not found"
✅ "This project has been deleted. Check your archived projects or create a new one."

Alternative (with recovery):
✅ "This file was deleted on [date]. It will be permanently removed in 25 days. Restore it or let it expire."

CTA: [View archived projects] [Create new] [Restore]
```

### Search No Results
```
Trigger: Search returns nothing
Severity: Minor

❌ "No results"
❌ "Nothing found"
✅ "No results for '[search term]'. Try different keywords or check your spelling."

Alternative (with suggestions):
✅ "No results for '[query]'. Did you mean '[suggestion]'?"

CTA: [Clear search] [Browse all] [View suggestions]
```

## Constraint Errors

### Storage Limit Exceeded
```
Trigger: User exceeds storage quota
Severity: Moderate

❌ "Storage full"
✅ "Your storage is full (5 GB used). Delete some files or upgrade to get more space."

Alternative (approaching limit):
✅ "You're using 4.8 GB of 5 GB (96%). You'll need to free up space or upgrade soon."

CTA: [Manage storage] [Upgrade plan]
```

### User Limit Reached
```
Trigger: Max users for plan
Severity: Moderate

❌ "Limit exceeded"
✅ "You've reached your limit of 5 team members on the Starter plan. Upgrade to add unlimited users."

Alternative:
✅ "Your team is full (5/5 members). Remove a member or upgrade to add more."

CTA: [Upgrade plan] [Manage team]
```

### Quota Exceeded
```
Trigger: API calls, exports, etc. quota hit
Severity: Moderate

❌ "Quota exceeded"
✅ "You've used your 1,000 API calls this month (resets on March 1). Upgrade for higher limits."

Alternative (with countdown):
✅ "Monthly export limit reached (10/10 used). Your quota resets in 12 days."

CTA: [Upgrade now] [View usage]
```

## User Conflict Errors

### Edit Conflict
```
Trigger: Multiple users editing simultaneously
Severity: Moderate

❌ "Conflict detected"
✅ "Someone else edited this document while you were working. Review their changes before saving yours."

Alternative (with details):
✅ "[Colleague Name] made changes to this file 30 seconds ago. Refresh to see the latest version or save as a new file."

CTA: [Review changes] [Reload] [Save as copy]
```

### Concurrent Modification
```
Trigger: Resource modified by another user
Severity: Moderate

❌ "Resource changed"
✅ "This item was updated by [User] while you were editing. Reload to see the latest version."

CTA: [Reload] [Save as new]
```

## Payment Errors

### Card Declined
```
Trigger: Payment processor declines card
Severity: Moderate

❌ "Payment failed"
✅ "Your card was declined. Please check your card details or try a different payment method."

Alternative (with reason if known):
✅ "Your card was declined due to insufficient funds. Please use a different card or contact your bank."

CTA: [Update payment method] [Try again]
```

### Payment Processing Error
```
Trigger: Error during payment
Severity: Critical

❌ "Error processing payment"
✅ "We encountered an issue processing your payment. Your card has not been charged. Please try again or contact support if the problem continues."

CTA: [Try again] [Contact support]
```

## Error Message Templates by Severity

### Minor Errors (User mistakes, validation)
```
Template:
"[Clear explanation of the issue]. [How to fix it with example]."

Tone: Friendly and helpful
Example: "Please enter a valid email address (e.g., name@company.com)"

Actions: Inline correction, no modal needed
Icon: ⚠️ Warning
```

### Moderate Errors (Not found, permissions, some system issues)
```
Template:
"[What happened]. [Why - if helpful]. [What to do next]."

Tone: Professional and clear
Example: "You don't have permission to edit this file. Contact the file owner to request access."

Actions: Alternative paths, request access, go back
Icon: 🔒 (permissions) or ℹ️ (info)
CTA: Primary action button
```

### Critical Errors (System failures, payment issues, data at risk)
```
Template:
"[Calm statement of problem]. [Reassurance about data/money]. [What we're doing]. [What you should do]."

Tone: Calm, reassuring, transparent
Example: "We encountered a technical issue and couldn't complete your payment. Your card has not been charged. We've been notified and are working on a fix. Please try again in 30 minutes or contact support if urgent."

Actions: Retry, contact support, check status
Icon: ❌ Error or 🛠️ Technical
CTA: Multiple options (Retry, Support, Status)
```

## Best Practices

1. **Never blame the user**: "Invalid input" → "Please enter..."
2. **Be specific**: "Error occurred" → "We couldn't save your document"
3. **Provide solutions**: "Failed" → "Check your connection and try again"
4. **Explain consequences**: "Offline" → "Your changes will sync when you reconnect"
5. **Show progress**: "Processing..." → "Processing your payment (Step 2 of 3)..."
6. **Use plain language**: No error codes alone, avoid jargon
7. **Match severity to tone**: Critical = calm/reassuring, Minor = friendly/helpful
8. **Always test**: With real users, especially non-technical ones

## Accessibility Requirements

- [ ] Error associated with field (`aria-invalid`, `aria-describedby`)
- [ ] Error announced to screen readers (`role="alert"`)
- [ ] Visual indicator beyond color (icon + text)
- [ ] Error persists until resolved (doesn't auto-dismiss)
- [ ] Error text is keyboard accessible
- [ ] Clear color contrast (WCAG AA minimum)

This template provides battle-tested error message patterns. Adapt the wording to match your product's voice while maintaining clarity and helpfulness.
