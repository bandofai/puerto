# Skill: Ticket Resolution

ITIL-based incident and request management workflows, SLA management, and resolution best practices.

## Ticket Lifecycle Management

### Ticket States

```
New → Triaged → Assigned → In Progress → Pending → Resolved → Closed
                                ↓
                            Reopened ← (back to In Progress)
```

#### State Definitions

**New**: Ticket just created, not yet reviewed
- Action: Awaits triage
- Owner: Unassigned
- Duration: < 15 minutes for P1, < 1 hour for P2-P4

**Triaged**: Classified and ready for assignment
- Action: Route to appropriate queue or agent
- Owner: Assigned to queue
- Duration: Minutes to hours depending on priority

**Assigned**: Specific person responsible
- Action: Agent reviews and begins work
- Owner: Specific agent or team member
- Duration: Should move to In Progress quickly

**In Progress**: Active work happening
- Action: Diagnosis, testing, implementing fix
- Owner: Assigned agent
- Duration: Varies by complexity, monitor SLA

**Pending**: Waiting for external input
- Action: Awaiting user response, vendor, approval, parts
- Owner: Assigned agent (still responsible)
- Duration: Set reminder to follow up, pause SLA clock (sometimes)

**Resolved**: Solution implemented, awaiting verification
- Action: User verification or automatic closure timer
- Owner: Assigned agent
- Duration: 24-72 hours before auto-close

**Closed**: Issue verified fixed, ticket complete
- Action: None, ticket archived
- Owner: N/A
- Duration: Permanent (unless reopened within 30 days)

**Reopened**: Issue recurred or not actually fixed
- Action: Return to In Progress, investigate why fix failed
- Owner: Original agent or escalate
- Duration: Treat as new ticket with higher priority

## Ticket Classification

### Categories

#### Hardware
- Desktop/laptop issues
- Printer problems
- Monitor, keyboard, mouse
- Server hardware
- Mobile devices
- Network equipment

#### Software
- Application errors
- Installation issues
- License problems
- Performance issues
- Software updates
- Compatibility issues

#### Access
- New user accounts
- Password resets
- Permission changes
- Account lockouts
- Group membership
- Offboarding

#### Network
- Connectivity issues
- VPN problems
- WiFi problems
- DNS issues
- Slow network
- Website access issues

#### Email
- Cannot send/receive
- Mailbox full
- Outlook configuration
- Mobile email setup
- Distribution lists
- Email forwarding

#### Other
- Questions/how-to
- Feature requests
- Change requests
- Documentation
- Training requests

### Priority Matrix

| Priority | Response SLA | Resolution SLA | Definition | Examples |
|----------|--------------|----------------|------------|-----------|
| **P1 - Critical** | 15 minutes | 4 hours | Complete service outage, security breach, data loss | Production server down, all users affected, security incident |
| **P2 - High** | 1 hour | 8 hours | Major functionality impaired, multiple users affected | Key application unusable, department-wide issue, VIP user blocked |
| **P3 - Medium** | 4 hours | 24 hours | Minor functionality impaired, single user affected | One user's printer not working, slow computer, minor bug |
| **P4 - Low** | 8 hours | 72 hours | Minimal impact, questions, feature requests | How-to questions, cosmetic issues, enhancements |

### Impact vs Urgency Matrix

|                    | **Low Urgency** | **Medium Urgency** | **High Urgency** | **Critical Urgency** |
|--------------------|----------------|-------------------|-----------------|---------------------|
| **High Impact**    | P3 | P2 | P1 | P1 |
| **Medium Impact**  | P4 | P3 | P2 | P2 |
| **Low Impact**     | P4 | P4 | P3 | P3 |

**Impact**: How many users/systems affected
**Urgency**: How quickly resolution is needed

## SLA Management

### SLA Clock

#### Clock Starts
- When ticket is created
- When ticket is reopened

#### Clock Stops (Pauses)
- Ticket in Pending state (if configured)
- Waiting for user response
- Waiting for parts/procurement
- Outside business hours (if 24/7 SLA not applicable)

#### Clock Resumes
- User responds
- Parts arrive
- Return to business hours

#### Clock Ends
- Ticket resolved or closed
- SLA breach occurred

### SLA Breach Prevention

#### Proactive Monitoring
- **75% threshold**: Warning alert to agent
- **90% threshold**: Escalation to manager
- **At breach**: Automatic escalation, incident report

#### Auto-Escalation Rules
- P1 tickets: No update in 1 hour → escalate
- P2 tickets: No update in 4 hours → escalate
- P3 tickets: No update in 12 hours → escalate
- P4 tickets: No update in 24 hours → escalate

#### Stale Ticket Detection
- Assigned but no activity in 24 hours → alert agent
- In Progress but no update in 48 hours → escalate to manager
- Pending for > 7 days → close with note "no response from user"

## Escalation Procedures

### Escalation Types

#### Functional Escalation (Technical)
- Issue beyond current team's expertise
- Requires specialized knowledge or tools
- **Tier 1 → Tier 2**: Complex troubleshooting, requires advanced tools
- **Tier 2 → Tier 3/Vendor**: Software bug, hardware RMA, deep expertise needed

#### Hierarchical Escalation (Management)
- SLA at risk or breached
- Resource allocation needed
- Policy exception required
- **Agent → Team Lead → Manager → Director → VP**: As severity increases

### When to Escalate

**Immediate Escalation (P1)**:
- Complete service outage
- Security breach or data loss
- Multiple failed resolution attempts
- Requires emergency change

**Proactive Escalation (P2-P3)**:
- SLA approaching breach (90% consumed)
- Ticket bounced between agents 3+ times
- Requires approval or resources not available
- Pattern detection (5+ similar tickets)

**Escalation to Vendor**:
- Hardware under warranty needing replacement
- Software bug requiring vendor patch
- Product-specific issue not documented
- Requires vendor support account or tools

### Escalation Handoff

**Information to Provide**:
1. Ticket number and priority
2. Problem summary (what, when, who, impact)
3. Steps already taken (avoid duplicate work)
4. Current state and recent findings
5. Why escalating (skill gap, SLA risk, resource need)
6. Expected assistance (diagnosis help, approval, parts, etc.)

**Handoff Methods**:
- Update ticket with escalation note
- Email or message escalation team
- Phone call for P1 (immediate contact)
- Include in daily escalation report

## Communication Standards

### User Communication

#### Initial Response
- Acknowledge receipt of ticket
- Confirm understanding of issue
- Provide ticket number for reference
- Set expectations for next steps and timing
- **Timeline**: Within response SLA

**Example**:
```
Hi [User],

Thank you for contacting IT Support. Your ticket #INC-12345 has been received and assigned to me.

I understand you're unable to print to the 3rd floor printer. I'll investigate and get back to you within 4 hours with an update or resolution.

If you have any additional information, please reply to this email or call our help desk at ext. 5555.

Best regards,
[Your Name]
IT Support Team
```

#### Progress Updates
- Provide updates at least every 24 hours for P1-P2
- Update when changing state (to Pending, to Escalated)
- Explain delays honestly
- Reset expectations if timeline changes

**Example**:
```
Hi [User],

Quick update on your ticket #INC-12345. I've diagnosed the issue as a driver problem and am currently downloading the updated printer driver. This should resolve your issue within the next hour.

I'll let you know once it's ready to test.

Best regards,
[Your Name]
```

#### Resolution Communication
- Explain what was wrong
- Explain what was fixed
- Confirm user can verify
- Ask user to reply if issue recurs
- Request ticket closure confirmation

**Example**:
```
Hi [User],

Great news! I've resolved your ticket #INC-12345. The issue was an outdated printer driver that wasn't compatible with the latest Windows update. I've installed the updated driver (version 3.2.1) and successfully printed a test page.

Please try printing your document now and let me know if it works. If you have any issues, please reply to this email and I'll reopen the ticket.

If everything is working correctly, this ticket will automatically close in 24 hours.

Best regards,
[Your Name]
```

### Internal Communication (Ticket Notes)

#### Documentation Requirements
- **Date/Time**: When action taken
- **What was done**: Specific steps, commands, changes
- **Results**: What happened (success, error, partial)
- **Next steps**: What needs to happen next
- **Time spent**: For tracking and billing

**Good Ticket Note**:
```
2025-10-20 14:30 - Ran system diagnostics on WIN-PC-042
- CPU usage: 45% (normal)
- Memory: 8GB total, 6.5GB used (81%)
- Disk C: 98% full (465GB used of 475GB)
- Root cause: Disk space exhaustion causing paging and slowness

Actions taken:
- Cleared temp files (C:\Windows\Temp) - recovered 2GB
- Emptied Recycle Bin - recovered 5GB
- Deleted old Windows Update files - recovered 3GB
- Total recovered: 10GB, disk now at 91%

Result: Computer performance improved significantly. User confirmed applications now open quickly.

Recommendation: User should archive or delete old files to maintain < 85% disk usage.

Time spent: 25 minutes
Status: Resolved
```

**Bad Ticket Note**:
```
Fixed computer, slow disk issue
```

## Resolution Documentation

### Resolution Types

#### Permanent Fix
- Root cause eliminated
- Issue will not recur
- Preferred resolution type

**Example**: Updated software to version with bug fix

#### Workaround
- Issue mitigated but root cause remains
- Temporary solution
- Permanent fix planned separately

**Example**: Restarting service daily while awaiting vendor patch

#### Cannot Reproduce
- Unable to recreate issue
- Closed with monitoring
- May reopen if recurs

**Example**: Intermittent error, not occurring during investigation

#### Duplicate Ticket
- Same issue as another ticket
- Close and link to original

**Example**: Multiple users reported same outage

#### User Error
- User misunderstanding or training issue
- Provide education or documentation

**Example**: User didn't know how to use feature

#### By Design / Feature Request
- Not a bug, working as intended
- Route to feature request process if applicable

**Example**: Application doesn't have requested feature

### Root Cause Documentation

#### 5 Whys Technique
Keep asking "Why?" to find root cause:
```
Problem: Website is down
Why? → Web server is not responding
Why? → Web service crashed
Why? → Out of memory error
Why? → Memory leak in version 2.1
Why? → Bug in session management code
Root Cause: Software bug in version 2.1
```

#### Contributing Factors
List all factors that contributed:
- Primary cause: Software bug
- Contributing factors:
  - High user load (250 concurrent users)
  - No memory monitoring alerts
  - No automatic restart on OOM condition

## Knowledge Base Integration

### When to Create KB Article

**Criteria**:
- Issue occurred 3+ times (pattern)
- Common issue with clear solution
- Time-consuming diagnosis or resolution
- Frequently asked question
- Complex procedure worth documenting

**Process**:
1. Resolve ticket with clear documentation
2. Create KB article with structure:
   - Title (searchable problem statement)
   - Symptoms
   - Cause
   - Resolution steps
   - Prevention
   - Related articles
3. Link KB article to ticket
4. Tag article for discovery

### KB Article from Ticket

**Good Source Tickets**:
- Well-documented resolution
- Clear root cause identified
- Step-by-step fix provided
- Reproducible issue and solution

**Poor Source Tickets**:
- Vague problem description
- Unclear resolution
- One-off unique issue
- No verification of fix

## Ticket Quality Metrics

### Quality Checklist

**Before Closing**:
- [ ] Problem clearly described
- [ ] Root cause identified and documented
- [ ] Resolution steps documented
- [ ] User confirmed issue resolved
- [ ] Time spent recorded accurately
- [ ] All actions logged in ticket notes
- [ ] KB article created if applicable
- [ ] Related tickets linked
- [ ] Proper category and priority set

### Quality Metrics

- **First Contact Resolution (FCR)**: Resolved without reassignment = **Target: > 70%**
- **Reopened Tickets**: Ticket reopened within 30 days = **Target: < 5%**
- **SLA Compliance**: Met SLA deadline = **Target: > 95%**
- **Documentation Quality**: Audit score = **Target: > 90%**
- **User Satisfaction**: CSAT survey score = **Target: > 4.0/5.0**

## Ticket Templates

### Standard Ticket Structure

```json
{
  "ticket_id": "INC-2025-XXXXX",
  "type": "Incident | Service Request | Change Request",
  "category": "Hardware | Software | Access | Network | Email | Other",
  "subcategory": "Specific type",
  "priority": "P1 | P2 | P3 | P4",
  "status": "New | Triaged | Assigned | In Progress | Pending | Resolved | Closed",
  "created_at": "ISO-8601 timestamp",
  "updated_at": "ISO-8601 timestamp",
  "sla_deadline": "ISO-8601 timestamp",
  "reported_by": {
    "name": "User name",
    "email": "user@company.com",
    "department": "Department",
    "location": "Office location",
    "phone": "Phone number"
  },
  "assigned_to": "Agent name or Unassigned",
  "assigned_team": "Tier 1 | Tier 2 | Specialist Team",
  "subject": "Brief description (< 100 chars)",
  "description": "Detailed problem description from user",
  "affected_systems": ["system1", "system2"],
  "error_messages": ["error text if applicable"],
  "business_impact": "Impact on business operations",
  "resolution": "What fixed the issue",
  "root_cause": "Why the issue occurred",
  "workaround": "Temporary fix if permanent not available",
  "actions_taken": ["action1", "action2"],
  "related_tickets": ["INC-XXX", "CHG-YYY"],
  "kb_articles": ["KB-123", "KB-456"],
  "attachments": ["screenshots", "log files"],
  "time_spent_minutes": 0,
  "tags": ["tag1", "tag2"]
}
```

## Common Resolution Scenarios

### Password Reset
1. Verify user identity (employee ID, manager, security questions)
2. Reset password in AD/directory
3. Provide temp password securely (phone, not email)
4. Set must-change-on-next-login
5. Document in ticket
6. Close when user confirms access restored
**Time: 5 minutes, Priority: P3**

### Software Installation Request
1. Verify software is approved/licensed
2. Check compatibility with user's OS
3. Obtain manager approval if required
4. Install software remotely or schedule visit
5. Verify installation successful
6. Provide basic usage guide if available
7. Document software version installed
**Time: 15-30 minutes, Priority: P3-P4**

### Printer Not Working
1. Check printer power and connections
2. Test printer from another computer (is it printer or computer?)
3. Check print queue for stuck jobs
4. Verify correct printer driver installed
5. Update driver if needed
6. Print test page to verify
7. Document root cause and fix
**Time: 15-20 minutes, Priority: P3**

### Email Issues
1. Check mailbox quota (often the cause)
2. Check send/receive settings
3. Test with webmail (rule out Outlook)
4. Check junk/spam folders
5. Verify email account not disabled
6. Recreate Outlook profile if needed
7. Verify issue resolved
**Time: 15-30 minutes, Priority: P2-P3**

### VPN Connection Issues
1. Verify internet connectivity
2. Check VPN client version (update if old)
3. Verify credentials correct
4. Test from different network (rule out firewall)
5. Check VPN server status
6. Reinstall VPN client if needed
7. Document resolution
**Time: 20-30 minutes, Priority: P2**

## Customer Satisfaction

### CSAT Survey
- Sent after ticket closure
- 5-point scale: Very Dissatisfied → Very Satisfied
- Optional comments field
- Track trends, not individual scores

### Improving Satisfaction

**Do**:
- Respond quickly (acknowledge receipt)
- Set realistic expectations
- Provide regular updates
- Explain issues in user-friendly terms
- Verify resolution with user
- Be courteous and professional

**Don't**:
- Leave user without updates for days
- Use technical jargon without explanation
- Blame user for issue
- Close ticket without verifying fix
- Promise what you can't deliver

### Handling Difficult Users

**De-escalation Techniques**:
1. Listen actively without interrupting
2. Empathize ("I understand this is frustrating")
3. Apologize for inconvenience (not for blame)
4. Focus on solution, not problem
5. Set clear expectations
6. Follow up proactively
7. Escalate if user requests manager

**Example**:
```
User: "This is ridiculous! My email has been down for 2 hours and I can't do my job!"

Response: "I completely understand how frustrating this must be, especially when email is critical to your work. I'm going to make this my top priority right now. Let me take a look at your account and I'll have an update for you within 15 minutes. Can I reach you at [phone number] when I have information?"
```
