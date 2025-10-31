# Approval Workflow Skill

**Expert patterns for approval routing, status tracking, and workflow coordination**

## Core Principles

1. **Deterministic Routing**: Same inputs always produce same approval chain
2. **Transparent Status**: Everyone knows where request is at all times
3. **SLA Compliance**: Track and enforce approval deadlines
4. **Audit Trail**: Complete history of all decisions and actions
5. **Escalation Paths**: Automatic handling of delays and blockers

---

## Approval Chain Construction

### Threshold-Based Routing

**Standard Approval Matrix**:

| Amount Range | Required Approvers | Typical SLA |
|--------------|-------------------|-------------|
| $0 - $1,000 | Manager | 24-48 hours |
| $1,001 - $5,000 | Manager → Finance | 48-72 hours |
| $5,001 - $10,000 | Manager → Director → Finance | 3-5 days |
| $10,001 - $25,000 | Manager → Director → VP → Finance | 5-7 days |
| $25,001+ | Manager → Director → VP → CFO → Finance | 7-14 days |

### Dynamic Chain Algorithm

```python
class ApprovalChainBuilder:
    """Build approval chains based on rules"""

    def __init__(self, org_structure, policy_rules):
        self.org = org_structure
        self.policy = policy_rules

    def build_chain(self, expense_report):
        """Construct complete approval chain"""

        chain = []
        employee = expense_report['employee']
        total_amount = expense_report['summary']['total_amount']
        categories = expense_report['summary']['categories']
        violations = expense_report.get('policy_checks', {}).get('violations', [])

        # 1. Direct Manager (always required)
        chain.append(self._create_approver_node(
            role='Manager',
            name=employee['manager'],
            order=10,
            sla_hours=48,
            required=True,
            reason='Direct manager approval always required'
        ))

        # 2. Amount-based escalation
        if total_amount > 5000:
            director = self.org.get_director(employee['department'])
            chain.append(self._create_approver_node(
                role='Director',
                name=director,
                order=20,
                sla_hours=72,
                required=True,
                reason=f'Amount ${total_amount} exceeds $5,000 threshold'
            ))

        if total_amount > 10000:
            vp = self.org.get_vp(employee['department'])
            chain.append(self._create_approver_node(
                role='VP',
                name=vp,
                order=30,
                sla_hours=120,
                required=True,
                reason=f'Amount ${total_amount} exceeds $10,000 threshold'
            ))

        if total_amount > 25000:
            chain.append(self._create_approver_node(
                role='CFO',
                name='CFO',
                order=40,
                sla_hours=168,
                required=True,
                reason=f'Amount ${total_amount} exceeds $25,000 threshold'
            ))

        # 3. Category-specific approvers
        if 'Professional Development' in categories:
            training_coordinator = self.org.get_training_coordinator()
            chain.append(self._create_approver_node(
                role='Training Coordinator',
                name=training_coordinator,
                order=15,  # After manager, before director
                sla_hours=72,
                required=True,
                parallel_with=[10],  # Can approve in parallel with manager
                reason='Professional development expenses require training coordinator approval'
            ))

        if 'Equipment' in categories and categories['Equipment'] > 1000:
            it_approver = self.org.get_it_asset_manager()
            chain.append(self._create_approver_node(
                role='IT Asset Manager',
                name=it_approver,
                order=15,
                sla_hours=48,
                required=True,
                parallel_with=[10],
                reason='Equipment >$1,000 requires IT approval'
            ))

        # 4. Policy violation escalation
        if violations:
            high_violations = [v for v in violations if v['severity'] in ['high', 'critical']]
            if high_violations:
                # Require director approval for policy violations
                if not any(a['role'] == 'Director' for a in chain):
                    director = self.org.get_director(employee['department'])
                    chain.append(self._create_approver_node(
                        role='Director',
                        name=director,
                        order=20,
                        sla_hours=72,
                        required=True,
                        reason=f'Policy violations detected: {len(high_violations)} high/critical'
                    ))

        # 5. Finance review (always last)
        chain.append(self._create_approver_node(
            role='Finance',
            name='Finance Team',
            order=90,
            sla_hours=48,
            required=True,
            final_reviewer=True,
            reason='Finance always performs final review'
        ))

        # Sort by order
        chain.sort(key=lambda x: x['order'])

        return chain

    def _create_approver_node(self, role, name, order, sla_hours, required=True, **kwargs):
        """Create standardized approver node"""

        from datetime import datetime, timedelta

        node = {
            'role': role,
            'name': name,
            'email': self.org.get_email(name),
            'order': order,
            'status': 'pending' if order == 10 else 'waiting',
            'sla_hours': sla_hours,
            'sla_deadline': None,  # Set when notified
            'required': required,
            'notified_at': None,
            'approved_at': None,
            'comments': None,
            'decision': None,
        }

        # Add any additional kwargs
        node.update(kwargs)

        return node
```

### Parallel vs. Sequential Approval

**Sequential** (default):
```
Manager → Director → VP → Finance
  (48h)    (72h)      (120h)  (48h)
Total: ~11 days
```

**Parallel** (for independent reviewers):
```
Manager (48h) ┐
              ├→ Director → Finance
Training (72h)┘
Total: ~5 days
```

**Implementation**:
```python
def supports_parallel_approval(approver_node):
    """Check if approver can run in parallel"""

    return approver_node.get('parallel_with') is not None

def get_next_approvers(chain, current_approver):
    """Get next approvers (may be multiple if parallel)"""

    current_order = current_approver['order']

    # Find next order value
    next_orders = sorted(set(a['order'] for a in chain if a['order'] > current_order))

    if not next_orders:
        return []  # No more approvers

    next_order = next_orders[0]

    # Get all approvers at that order (parallel)
    next_approvers = [a for a in chain if a['order'] == next_order]

    return next_approvers
```

---

## Workflow State Management

### State Schema

```json
{
  "workflow_id": "WF-EXP-2025-001",
  "report_id": "EXP-2025-001",
  "version": "1.0",
  "created_at": "2025-01-20T10:00:00Z",
  "updated_at": "2025-01-20T10:00:00Z",

  "employee": {
    "name": "John Doe",
    "id": "EMP-12345",
    "email": "john.doe@company.com",
    "department": "Engineering",
    "manager": "Jane Smith"
  },

  "expense_summary": {
    "total_amount": 1547.89,
    "currency": "USD",
    "expense_count": 12,
    "period": "2025-01-01 to 2025-01-31"
  },

  "compliance": {
    "status": "compliant",
    "score": 98,
    "violations": []
  },

  "approval_chain": [
    {
      "order": 10,
      "role": "Manager",
      "name": "Jane Smith",
      "email": "jane.smith@company.com",
      "status": "approved",
      "required": true,
      "sla_hours": 48,
      "sla_deadline": "2025-01-22T10:00:00Z",
      "notified_at": "2025-01-20T10:05:00Z",
      "approved_at": "2025-01-21T14:30:00Z",
      "decision": "approved",
      "comments": "Approved. All expenses are reasonable and well-documented.",
      "duration_hours": 28.4,
      "within_sla": true
    },
    {
      "order": 90,
      "role": "Finance",
      "name": "Finance Team",
      "email": "finance@company.com",
      "status": "pending",
      "required": true,
      "sla_hours": 48,
      "sla_deadline": "2025-01-23T14:30:00Z",
      "notified_at": "2025-01-21T14:30:00Z",
      "approved_at": null,
      "decision": null,
      "comments": null,
      "final_reviewer": true
    }
  ],

  "current_step": {
    "order": 90,
    "role": "Finance",
    "status": "pending_finance"
  },

  "overall_status": "pending_finance",
  "progress_percentage": 50,

  "status_history": [
    {
      "timestamp": "2025-01-20T10:00:00Z",
      "status": "submitted",
      "actor": "John Doe (EMP-12345)",
      "actor_role": "Employee",
      "action": "submit",
      "notes": "Expense report submitted for approval"
    },
    {
      "timestamp": "2025-01-20T10:05:00Z",
      "status": "pending_manager",
      "actor": "System (approval-router)",
      "actor_role": "System",
      "action": "route",
      "notes": "Routed to Jane Smith (Manager) for approval"
    },
    {
      "timestamp": "2025-01-21T14:30:00Z",
      "status": "manager_approved",
      "actor": "Jane Smith",
      "actor_role": "Manager",
      "action": "approve",
      "notes": "Approved. All expenses are reasonable and well-documented."
    },
    {
      "timestamp": "2025-01-21T14:30:00Z",
      "status": "pending_finance",
      "actor": "System (approval-router)",
      "actor_role": "System",
      "action": "route",
      "notes": "Routed to Finance Team for final review"
    }
  ],

  "notifications": {
    "employee_updates": true,
    "approver_reminders": true,
    "escalation_alerts": true,
    "last_notification_sent": "2025-01-21T14:30:00Z",
    "reminder_schedule": [
      "2025-01-22T14:30:00Z",
      "2025-01-23T14:30:00Z"
    ]
  },

  "escalation": {
    "enabled": true,
    "policy": "auto_escalate_after_sla",
    "escalate_to_role": "Director",
    "escalate_after_hours": 72,
    "escalated": false,
    "escalation_history": []
  },

  "metrics": {
    "total_duration_hours": null,
    "average_approval_time_hours": 28.4,
    "sla_compliance_rate": 100,
    "approvals_within_sla": 1,
    "approvals_overdue": 0
  }
}
```

### State Transitions

**Valid Transitions**:
```python
VALID_TRANSITIONS = {
    'submitted': ['pending_manager', 'rejected'],
    'pending_manager': ['manager_approved', 'manager_rejected', 'needs_clarification'],
    'manager_approved': ['pending_director', 'pending_finance', 'approved'],
    'pending_director': ['director_approved', 'director_rejected', 'needs_clarification'],
    'director_approved': ['pending_vp', 'pending_finance', 'approved'],
    'pending_vp': ['vp_approved', 'vp_rejected', 'needs_clarification'],
    'vp_approved': ['pending_cfo', 'pending_finance', 'approved'],
    'pending_cfo': ['cfo_approved', 'cfo_rejected', 'needs_clarification'],
    'cfo_approved': ['pending_finance', 'approved'],
    'pending_finance': ['finance_approved', 'finance_rejected', 'needs_clarification'],
    'finance_approved': ['approved', 'queued_for_reimbursement'],
    'approved': ['queued_for_reimbursement', 'reimbursed'],
    'queued_for_reimbursement': ['reimbursed'],
    'reimbursed': [],  # Final state
    'rejected': [],    # Final state
    'needs_clarification': ['pending_manager', 'submitted'],  # Back to employee
}

def is_valid_transition(current_status, new_status):
    """Check if state transition is allowed"""
    return new_status in VALID_TRANSITIONS.get(current_status, [])

def transition_state(workflow, new_status, actor, notes=None):
    """Safely transition workflow state"""

    current_status = workflow['overall_status']

    if not is_valid_transition(current_status, new_status):
        raise ValueError(
            f"Invalid transition from '{current_status}' to '{new_status}'. "
            f"Valid transitions: {VALID_TRANSITIONS[current_status]}"
        )

    # Update status
    workflow['overall_status'] = new_status
    workflow['updated_at'] = datetime.utcnow().isoformat()

    # Add to history
    workflow['status_history'].append({
        'timestamp': datetime.utcnow().isoformat(),
        'status': new_status,
        'actor': actor,
        'action': 'transition',
        'notes': notes or f"Transitioned to {new_status}"
    })

    return workflow
```

---

## SLA Management

### SLA Calculation

```python
from datetime import datetime, timedelta

class SLAManager:
    """Calculate and enforce SLA deadlines"""

    def __init__(self, business_hours_config):
        self.config = business_hours_config

    def calculate_deadline(self, start_time, sla_hours):
        """Calculate SLA deadline accounting for business hours"""

        # Simple version (24/7)
        deadline = start_time + timedelta(hours=sla_hours)

        # Business hours version
        if self.config.get('business_hours_only'):
            deadline = self._add_business_hours(start_time, sla_hours)

        return deadline

    def _add_business_hours(self, start, hours):
        """Add business hours to start time"""

        current = start
        hours_remaining = hours

        business_start = self.config.get('day_start_hour', 9)
        business_end = self.config.get('day_end_hour', 17)
        business_hours_per_day = business_end - business_start

        while hours_remaining > 0:
            # Skip weekends
            if current.weekday() >= 5:  # Saturday=5, Sunday=6
                current += timedelta(days=1)
                current = current.replace(hour=business_start, minute=0, second=0)
                continue

            # Calculate hours available today
            if current.hour < business_start:
                current = current.replace(hour=business_start, minute=0, second=0)

            hours_left_today = business_end - current.hour

            if hours_remaining <= hours_left_today:
                # Can finish today
                current += timedelta(hours=hours_remaining)
                hours_remaining = 0
            else:
                # Move to next business day
                hours_remaining -= hours_left_today
                current += timedelta(days=1)
                current = current.replace(hour=business_start, minute=0, second=0)

        return current

    def check_sla_compliance(self, approver):
        """Check if approver is within SLA"""

        if not approver.get('sla_deadline'):
            return {'status': 'no_sla', 'overdue': False}

        deadline = datetime.fromisoformat(approver['sla_deadline'].replace('Z', '+00:00'))
        now = datetime.utcnow()

        if approver['status'] == 'approved':
            # Check if approved within SLA
            approved_at = datetime.fromisoformat(approver['approved_at'].replace('Z', '+00:00'))
            within_sla = approved_at <= deadline

            return {
                'status': 'completed',
                'overdue': not within_sla,
                'duration': (approved_at - datetime.fromisoformat(approver['notified_at'].replace('Z', '+00:00'))).total_seconds() / 3600,
                'sla_hours': approver['sla_hours']
            }

        # Pending - check if overdue
        overdue = now > deadline

        if overdue:
            hours_overdue = (now - deadline).total_seconds() / 3600
            return {
                'status': 'overdue',
                'overdue': True,
                'hours_overdue': hours_overdue
            }

        # Still within SLA
        hours_remaining = (deadline - now).total_seconds() / 3600
        return {
            'status': 'within_sla',
            'overdue': False,
            'hours_remaining': hours_remaining
        }
```

### Reminder Schedule

```python
def schedule_reminders(approver):
    """Create reminder schedule for approver"""

    notified_at = datetime.fromisoformat(approver['notified_at'].replace('Z', '+00:00'))
    deadline = datetime.fromisoformat(approver['sla_deadline'].replace('Z', '+00:00'))

    sla_hours = approver['sla_hours']

    reminders = []

    # Reminder at 50% of SLA
    reminder_50 = notified_at + timedelta(hours=sla_hours * 0.5)
    if reminder_50 < deadline:
        reminders.append({
            'scheduled_for': reminder_50.isoformat(),
            'type': 'gentle_reminder',
            'message': f"Reminder: Expense approval pending ({sla_hours//2} hours elapsed)"
        })

    # Reminder at 80% of SLA
    reminder_80 = notified_at + timedelta(hours=sla_hours * 0.8)
    if reminder_80 < deadline:
        reminders.append({
            'scheduled_for': reminder_80.isoformat(),
            'type': 'urgent_reminder',
            'message': f"Urgent: Expense approval needed soon (deadline in {sla_hours*0.2:.0f} hours)"
        })

    # Reminder at deadline
    reminders.append({
        'scheduled_for': deadline.isoformat(),
        'type': 'deadline_alert',
        'message': 'ALERT: SLA deadline reached for expense approval'
    })

    # Escalation after deadline
    escalation_time = deadline + timedelta(hours=24)
    reminders.append({
        'scheduled_for': escalation_time.isoformat(),
        'type': 'escalation',
        'message': 'Auto-escalating overdue expense approval'
    })

    return reminders
```

---

## Escalation Handling

### Auto-Escalation Logic

```python
class EscalationManager:
    """Handle overdue approvals"""

    def __init__(self, org_structure):
        self.org = org_structure

    def check_and_escalate(self, workflow):
        """Check for overdue approvals and escalate"""

        escalations = []

        for approver in workflow['approval_chain']:
            if approver['status'] != 'pending':
                continue  # Skip completed

            sla_check = check_sla_compliance(approver)

            if sla_check['overdue'] and sla_check['hours_overdue'] > 24:
                # Escalate after 24 hours overdue
                escalation = self._escalate_approval(workflow, approver)
                escalations.append(escalation)

        return escalations

    def _escalate_approval(self, workflow, overdue_approver):
        """Escalate overdue approval to next level"""

        # Determine who to escalate to
        escalate_to = self._get_escalation_target(overdue_approver, workflow)

        if not escalate_to:
            # No one to escalate to, send alert to exec team
            return self._alert_executive_team(workflow, overdue_approver)

        # Add new approver to chain
        new_approver = {
            'role': escalate_to['role'],
            'name': escalate_to['name'],
            'email': escalate_to['email'],
            'order': overdue_approver['order'] + 0.5,  # Insert after overdue
            'status': 'pending',
            'sla_hours': 24,  # Expedited SLA
            'escalated': True,
            'escalated_from': overdue_approver['name'],
            'reason': f"Escalated due to {overdue_approver['role']} approval overdue by {sla_check['hours_overdue']:.1f} hours"
        }

        # Notify new approver
        self._notify_escalation(new_approver, overdue_approver, workflow)

        # Mark original approver as escalated
        overdue_approver['status'] = 'escalated'
        overdue_approver['escalated_at'] = datetime.utcnow().isoformat()

        # Add to history
        workflow['status_history'].append({
            'timestamp': datetime.utcnow().isoformat(),
            'status': 'escalated',
            'actor': 'System (escalation-manager)',
            'action': 'escalate',
            'notes': f"Escalated from {overdue_approver['name']} ({overdue_approver['role']}) to {new_approver['name']} ({new_approver['role']})"
        })

        return new_approver

    def _get_escalation_target(self, overdue_approver, workflow):
        """Determine who to escalate to"""

        role = overdue_approver['role']
        department = workflow['employee']['department']

        escalation_map = {
            'Manager': lambda: self.org.get_director(department),
            'Director': lambda: self.org.get_vp(department),
            'VP': lambda: self.org.get_cfo(),
            'CFO': None,  # No escalation beyond CFO
        }

        escalation_func = escalation_map.get(role)

        if escalation_func:
            escalated_to = escalation_func()
            return {
                'role': self._get_role_above(role),
                'name': escalated_to,
                'email': self.org.get_email(escalated_to)
            }

        return None

    def _get_role_above(self, role):
        """Get next role in hierarchy"""

        hierarchy = ['Manager', 'Director', 'VP', 'CFO']

        try:
            current_index = hierarchy.index(role)
            if current_index < len(hierarchy) - 1:
                return hierarchy[current_index + 1]
        except ValueError:
            pass

        return None
```

---

## Notification Templates

### Email Templates

**Initial Approval Request**:
```markdown
Subject: [ACTION REQUIRED] Expense Report {report_id} - Approval Needed

Hi {approver_name},

An expense report requires your approval.

**Employee**: {employee_name} ({employee_id})
**Department**: {department}
**Report**: {report_id}
**Amount**: ${total_amount}
**Period**: {start_date} to {end_date}

**Compliance Status**: {compliance_status}
**Policy Violations**: {violation_count}

**SLA Deadline**: {deadline} ({sla_hours} hours)

[Approve] [Reject] [View Details] [Request Clarification]

---

## Quick Summary

{category_breakdown}

---

## Next Steps

- Review expense details and receipts
- Approve or reject by {deadline}
- Add comments if needed

Questions? Contact {employee_email}

---
*This is an automated notification from the Expense Management System*
```

**Reminder Template**:
```markdown
Subject: [REMINDER] Expense Report {report_id} - Approval Pending

Hi {approver_name},

This is a reminder that expense report {report_id} is awaiting your approval.

**Submitted**: {days_ago} days ago
**Deadline**: {hours_until_deadline} hours remaining
**Amount**: ${total_amount}

[Approve Now] [View Details]

If you have questions, contact {employee_email}
```

**Escalation Template**:
```markdown
Subject: [ESCALATED] Expense Report {report_id} - Urgent Approval Needed

Hi {escalated_approver_name},

This expense report has been escalated to you due to the original approver being unavailable.

**Original Approver**: {original_approver} ({original_role})
**Escalation Reason**: Overdue by {hours_overdue} hours

**Employee**: {employee_name}
**Amount**: ${total_amount}
**Report**: {report_id}

**Expedited SLA**: 24 hours

[Approve] [Reject] [View Details]

This requires urgent attention.
```

---

## Best Practices

1. **Clear SLAs**: Set realistic, enforceable deadlines
2. **Parallel When Possible**: Allow independent reviews simultaneously
3. **Auto-Escalate**: Don't let approvals get stuck
4. **Transparent Status**: Keep everyone informed
5. **Audit Everything**: Log every action and decision
6. **Flexible Routing**: Support special cases and overrides
7. **Employee Communication**: Keep submitter updated
8. **Metrics Tracking**: Monitor approval times and bottlenecks

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: Approval routing, workflow coordination, SLA management
