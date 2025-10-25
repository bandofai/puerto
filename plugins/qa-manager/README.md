# QA Manager Plugin

Quality management system specialist for designing QA processes, defining quality standards, coordinating audits, tracking corrective actions, and facilitating continuous improvement using ISO 9001 and Six Sigma methodologies.

## Overview

The QA Manager plugin provides agents for systematic quality management following ISO 9001, PDCA (Plan-Do-Check-Act), Six Sigma DMAIC, and continuous improvement frameworks.

## Agents

### 1. process-designer (Sonnet, Skill-Aware)
Designs comprehensive QA processes with quality gates, acceptance criteria, and testing workflows.

**Use for**: QA process definition, quality gates, testing standards, process documentation

**Example**:
```
Use process-designer for software QA process.
Product: SaaS application, monthly releases
Quality gates:
- Code review: 100% of code reviewed, 2 approvals required
- Unit tests: 80%+ coverage, all tests passing
- Integration tests: Critical paths covered
- Performance tests: P95 latency <200ms, load >1000 RPS
- Security scan: No high/critical vulnerabilities
- UAT: Product owner sign-off
Include: Testing levels (unit, integration, E2E), defect workflow, metrics
```

### 2. standards-auditor (Sonnet, Skill-Aware)
Conducts quality audits against defined standards (ISO 9001, industry-specific) and identifies gaps.

**Use for**: ISO 9001 audits, compliance checking, gap analysis, certification preparation

**Example**:
```
Use standards-auditor for ISO 9001 internal audit.
Scope: Development and support processes (Clauses 4-10)
Focus areas:
- Clause 5: Leadership and commitment
- Clause 6: Planning (quality objectives, risk management)
- Clause 8: Operation (design, production, delivery)
- Clause 9: Performance evaluation (monitoring, audits)
- Clause 10: Improvement (nonconformity, corrective action)
Output: Audit report with findings (major/minor nonconformities), evidence, recommendations
```

### 3. corrective-action-tracker (Sonnet, Skill-Aware)
Manages corrective and preventive actions (CAPA) with root cause analysis and effectiveness verification.

**Use for**: Defect tracking, root cause analysis, CAPA management, effectiveness checks

**Example**:
```
Use corrective-action-tracker for production defect.
Defect: Payment processing failure (50 customers affected)
Root cause analysis (5 Whys):
1. Why did payments fail? → Database timeout
2. Why timeout? → Query taking 30+ seconds
3. Why slow query? → Missing index on transactions table
4. Why missing index? → Not identified in code review
5. Why not caught? → No performance testing in QA process
Corrective action: Add missing index (immediate)
Preventive action: Add performance tests to QA process (systematic)
Verification: Monitor query time, ensure <100ms
```

### 4. improvement-facilitator (Sonnet, Skill-Aware)
Facilitates continuous improvement using PDCA, Kaizen, and Six Sigma methodologies.

**Use for**: Continuous improvement, process optimization, waste reduction, efficiency gains

**Example**:
```
Use improvement-facilitator for release process optimization.
Current state: 4-hour manual release process, 20% rollback rate
Improvement approach: PDCA (Plan-Do-Check-Act)
Plan:
- Identify waste in current process (waiting, manual steps)
- Propose automation: CI/CD pipeline with automated tests
- Set target: <30 min release time, <5% rollback rate
Do:
- Implement automated deployment pipeline (canary strategy)
- Add smoke tests and rollback automation
Check:
- Measure results over 10 releases
- Release time reduced to 25 min (88% improvement)
- Rollback rate reduced to 3% (85% improvement)
Act:
- Standardize automated deployment
- Document new process
- Train team
```

## Skills

### quality-management
Comprehensive quality management frameworks:
- **ISO 9001**: Quality management system standard (clauses 4-10)
- **PDCA Cycle**: Plan-Do-Check-Act continuous improvement
- **Six Sigma DMAIC**: Define-Measure-Analyze-Improve-Control
- **Quality Gates**: Go/no-go decision points based on quality criteria
- **Root Cause Analysis**: 5 Whys, Fishbone diagram, Fault Tree Analysis
- **CAPA**: Corrective and Preventive Actions
- **Quality Metrics**: Defect density, escape rate, test coverage, customer satisfaction
- **Test Levels**: Unit, integration, system, acceptance testing
- **Defect Lifecycle**: New → Assigned → Fixed → Verified → Closed

## Templates

### qa-process-template.md
QA process documentation: Process overview, quality gates, testing levels, acceptance criteria, defect workflow, roles & responsibilities, metrics and KPIs.

### audit-checklist-template.md
Quality audit checklist: ISO 9001 clauses, audit questions, evidence requirements, conformity assessment (C/NC/OFI), findings documentation.

### corrective-action-template.md
CAPA template: Problem description, impact assessment, root cause analysis (5 Whys/Fishbone), corrective actions (immediate), preventive actions (systematic), verification plan, effectiveness review.

### continuous-improvement-plan-template.md
Improvement plan: Current state analysis, waste identification, improvement hypothesis, PDCA cycle, metrics and targets, implementation timeline, results tracking.

## Workflows

### Complete QA System Implementation
```
1. Design QA process
Use process-designer to define testing standards and quality gates

2. Conduct audits
Use standards-auditor for compliance and gap identification

3. Track corrective actions
Use corrective-action-tracker for defect resolution and root cause analysis

4. Continuous improvement
Use improvement-facilitator for process optimization
```

### ISO 9001 Certification
```
1. Gap analysis
Use standards-auditor to assess current state vs ISO 9001 requirements

2. Process improvement
Use improvement-facilitator to close gaps

3. Internal audits
Use standards-auditor for regular internal audits

4. Corrective actions
Use corrective-action-tracker to resolve nonconformities

5. Certification audit
Prepare for external auditor with documented processes and evidence
```

## Requirements Met

✅ Role: Quality management system specialist
✅ QA process design: process-designer with quality gates and testing standards
✅ Quality standards definition: ISO 9001, Six Sigma, industry standards
✅ Audit coordination: standards-auditor with ISO 9001 compliance
✅ Corrective action tracking: corrective-action-tracker with CAPA management
✅ Continuous improvement: improvement-facilitator with PDCA/DMAIC
✅ Tools: QA frameworks (ISO 9001, Six Sigma), tracking tools, file operations

## Key Features

✓ **ISO 9001 Compliance**: Complete QMS framework
✓ **Quality Gates**: Go/no-go decision points
✓ **Root Cause Analysis**: 5 Whys, Fishbone, FTA
✓ **CAPA Management**: Corrective and preventive actions
✓ **PDCA Cycle**: Continuous improvement methodology
✓ **Six Sigma DMAIC**: Data-driven process improvement
✓ **Audit Framework**: Internal audits, compliance checking
✓ **Metrics-Driven**: Defect density, escape rate, test coverage

## Quality Metrics

### Process Metrics
- **Test Coverage**: % of code covered by tests (target: 80%+)
- **Defect Density**: Defects per 1000 lines of code (target: <1)
- **Defect Escape Rate**: % defects found in production vs total (target: <5%)
- **Test Execution Time**: Time to run full test suite
- **Automation Rate**: % of tests automated (target: 80%+)

### Product Metrics
- **Defect Age**: Days from defect creation to closure
- **Reopen Rate**: % of defects reopened after fix (target: <5%)
- **Fix Time**: Average time to fix defects by severity
- **Customer-Reported Defects**: Defects found by customers vs QA

### Quality Gates
- All P0/critical defects resolved
- <5 P1/high defects
- 80%+ test coverage
- All security scans passing
- Performance tests meeting SLOs
- Product owner approval

## ISO 9001 Structure

### Clause 4: Context of the Organization
- Understanding organization and context
- Understanding needs of interested parties
- Quality management system scope

### Clause 5: Leadership
- Leadership and commitment
- Quality policy
- Organizational roles and responsibilities

### Clause 6: Planning
- Actions to address risks and opportunities
- Quality objectives and planning
- Planning of changes

### Clause 7: Support
- Resources, competence, awareness
- Communication
- Documented information

### Clause 8: Operation
- Operational planning and control
- Requirements for products/services
- Design and development
- Control of externally provided processes
- Production and service provision
- Release of products/services
- Control of nonconforming outputs

### Clause 9: Performance Evaluation
- Monitoring, measurement, analysis, evaluation
- Internal audit
- Management review

### Clause 10: Improvement
- General (continuous improvement)
- Nonconformity and corrective action
- Continual improvement

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 1 comprehensive quality-management skill (ISO 9001, Six Sigma)
- ✅ 4 professional templates for processes, audits, CAPA, improvement
- ✅ Complete README with frameworks and methodologies

Closes #84
