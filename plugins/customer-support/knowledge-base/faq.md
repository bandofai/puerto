# Frequently Asked Questions

## Account Management

### How do I reset my password?

**KB-001**

1. Go to [your login page]
2. Click "Forgot Password" below the login button
3. Enter your email address
4. Check your email for a reset link (arrives within 2 minutes)
5. Click the link and create your new password

**Expected time**: 2-3 minutes

**Note**: The reset link expires after 24 hours. If it expires, request a new one.

---

### How do I change my email address?

**KB-005**

1. Log into your account
2. Go to Settings > Profile
3. Click "Change Email"
4. Enter your new email address
5. Click "Send Verification"
6. Check the new email for verification link
7. Click the verification link
8. Confirm the change

**Note**: You'll need access to both your old and new email addresses.

---

### How do I add team members?

**KB-010**

1. Log into your account
2. Go to Settings > Team
3. Click "Invite Member"
4. Enter their email address
5. Select their role (Admin, Member, or Viewer)
6. Click "Send Invitation"

They'll receive an email invitation to join your team.

**Roles**:
- **Admin**: Full access including billing
- **Member**: Can use all features
- **Viewer**: Read-only access

---

## Billing

### How do I update my payment method?

**KB-004**

1. Log into your account
2. Go to Settings > Billing
3. Click "Update Payment Method"
4. Enter your new card details
5. Click "Save"

Changes take effect immediately. Your next invoice will use the new payment method.

---

### How do I download an invoice?

**KB-006**

1. Go to Settings > Billing
2. Click "Invoice History"
3. Find the invoice you need
4. Click the download icon

Invoices are available in PDF format.

---

### How do I upgrade/downgrade my plan?

**KB-007**

**To Upgrade**:
1. Settings > Billing > "Change Plan"
2. Select your new plan
3. Confirm the change

Upgrade is immediate. You'll be proactively charged for the difference.

**To Downgrade**:
1. Settings > Billing > "Change Plan"
2. Select your new plan
3. Confirm the change

Downgrade takes effect at the end of your current billing period.

---

### How do I request a refund?

**KB-008**

We offer refunds within 30 days of purchase.

Contact our support team with:
- Your order number
- Reason for refund
- Email address on the account

Refunds are processed within 5-7 business days.

**Note**: This automatically escalates to the billing team.

---

## Technical

### API authentication errors (401 Unauthorized)

**KB-002**

**Symptoms**: Getting 401 Unauthorized errors on API calls

**Solution**:

1. **Verify API key is active**
   - Go to Settings > API Keys
   - Check that your key shows "Active" status

2. **Check expiration**
   - API keys expire after 1 year
   - If expired, regenerate a new key

3. **Verify header format**
   - Use: `Authorization: Bearer YOUR_API_KEY`
   - Not: `Authorization: YOUR_API_KEY`

4. **Check IP whitelisting** (if enabled)
   - Settings > API Keys > IP Restrictions
   - Add your server's IP address

**Still not working?**

Try regenerating your API key:
1. Settings > API Keys
2. Click "Regenerate" next to your key
3. Copy the new key immediately (only shown once)
4. Update your application

---

### How do I regenerate my API key?

**KB-003**

1. Log into your account
2. Go to Settings > API Keys
3. Click "Regenerate" next to your current key
4. Copy the new key immediately (it's only shown once)
5. Update your application with the new key

**Important**: The old key stops working immediately when you regenerate.

---

### Slow dashboard performance

**KB-009**

**Troubleshooting steps**:

1. **Check system status**
   - Visit our status page: [status page URL]
   - Look for any ongoing incidents

2. **Clear browser cache**
   - Chrome: Ctrl+Shift+Delete (Windows) or Cmd+Shift+Delete (Mac)
   - Select "Cached images and files"
   - Click "Clear data"

3. **Try a different browser**
   - Test with Chrome, Firefox, or Safari
   - This helps identify browser-specific issues

4. **Check your internet connection**
   - Test speed at speedtest.net
   - Minimum recommended: 5 Mbps

5. **Disable browser extensions**
   - Ad blockers can sometimes interfere
   - Try disabling temporarily

**Still slow?**

Please contact support with:
- Your browser and version
- Screenshot of the slow page
- Time when it's happening
- Your internet speed test results

This may require escalation to L2.

---

## Data & Privacy

### How do I export my data?

**KB-011**

1. Settings > Data & Privacy
2. Click "Export Data"
3. Select data type (All, Users, Projects, etc.)
4. Choose format (JSON, CSV, or Excel)
5. Click "Start Export"

You'll receive an email when your export is ready (usually within 15 minutes).

Downloads are available for 7 days.

---

### How do I delete my account?

**KB-012**

1. Settings > Data & Privacy
2. Scroll to "Delete Account"
3. Click "Request Account Deletion"
4. Confirm by entering your password
5. You'll receive a confirmation email

**Important**:
- This action is permanent and cannot be undone
- All data will be deleted after 30 days
- You have 30 days to cancel the deletion
- Active subscriptions will be cancelled

---

## Integration

### How do I set up the Slack integration?

**KB-013**

1. Settings > Integrations
2. Find "Slack" and click "Connect"
3. Click "Allow" to authorize
4. Select which Slack channel to connect
5. Configure notification preferences
6. Click "Save"

You'll start receiving notifications in Slack immediately.

---

### How do I set up webhooks?

**KB-014**

1. Settings > Integrations > Webhooks
2. Click "Add Webhook"
3. Enter your endpoint URL
4. Select events to trigger webhook
5. Copy the webhook secret (for verification)
6. Click "Save"

Test your webhook by clicking "Send Test Event".

**Events available**:
- User created
- Project updated
- Task completed
- Payment received
- And more

---

## Mobile App

### How do I reset my mobile app?

**KB-015**

**iOS**:
1. Open the app
2. Go to Settings
3. Scroll to bottom
4. Tap "Reset App"
5. Confirm

**Android**:
1. Device Settings > Apps
2. Find our app
3. Tap "Storage"
4. Tap "Clear Data"

You'll need to log in again after resetting.

---

## Search Tips

To find answers faster in our knowledge base:

- Use specific keywords: "API 401" instead of "API not working"
- Include error codes: "500 error" or "404 not found"
- Search by feature name: "webhooks", "export", "billing"
- Try alternate terms: "login" = "sign in" = "authentication"

---

**Last Updated**: 2025-01-20
**Articles**: 15
**Average Resolution Rate**: 92%
