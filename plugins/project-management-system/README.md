# Project Management System Plugin

Professional project management capabilities including multi-project dashboards, task coordination, timeline visualization, and project archiving.

## Overview

This plugin provides comprehensive project management tools for planning, tracking, and completing projects using industry-standard methodologies including WBS (Work Breakdown Structure), Gantt charts, dependency mapping, and resource allocation.

## Agents

### 1. project-dashboard-manager
**Model**: Haiku (fast, efficient)
**Purpose**: Multi-project dashboard creation and status tracking
**Triggers**: "dashboard", "project status", "overview"

Creates comprehensive dashboards showing:
- Project health indicators
- Key milestones and deadlines
- Resource utilization
- Risk status
- Overall portfolio view

### 2. task-coordinator
**Model**: Sonnet (requires reasoning)
**Purpose**: WBS creation, dependency mapping, resource allocation
**Triggers**: "breakdown", "tasks", "dependencies", "resources"

Handles complex task planning:
- Work Breakdown Structure creation
- Task dependency identification
- Critical path analysis
- Resource allocation and leveling
- Effort estimation

### 3. timeline-visualizer
**Model**: Haiku (fast generation)
**Purpose**: Gantt chart generation in Mermaid, milestone tracking
**Triggers**: "timeline", "gantt", "schedule", "milestones"

Generates visual timelines:
- Mermaid Gantt charts
- Milestone markers
- Dependency arrows
- Progress indicators
- Timeline adjustments

### 4. project-archiver
**Model**: Haiku (template-based)
**Purpose**: Project completion reports, lessons learned documentation
**Triggers**: "archive", "complete", "close", "lessons learned"

Documents project completion:
- Final status reports
- Lessons learned
- Metrics and KPIs
- Success criteria validation
- Knowledge base contribution

## Skills

### project-management/SKILL.md
Comprehensive project management methodology including:
- Project lifecycle management (Initiation → Planning → Execution → Closure)
- WBS creation patterns
- Dependency mapping techniques
- Resource allocation strategies
- Risk identification and mitigation
- Status reporting frameworks

### gantt-visualization/SKILL.md
Timeline and schedule visualization using:
- Mermaid Gantt syntax
- Milestone representation
- Dependency visualization
- Progress tracking
- Timeline optimization techniques

## Templates

### project-template.md
Standard project documentation template with:
- Project charter elements
- Stakeholder identification
- Scope definition
- Success criteria

### task-breakdown-template.md
WBS template with:
- Hierarchical task structure
- Effort estimation fields
- Dependency notation
- Resource assignment

### gantt-template.md
Gantt chart template with:
- Mermaid syntax structure
- Common project phases
- Milestone patterns
- Dependency examples

### dashboard-template.md
Dashboard layout template with:
- Health indicators
- Status sections
- Metric displays
- Risk summaries

### archive-template.md
Project closure template with:
- Completion checklist
- Metrics summary
- Lessons learned structure
- Knowledge transfer sections

## Installation

```bash
# Install at project level
mkdir -p .claude/agents .claude/skills .claude/templates
cp plugins/project-management-system/agents/*.md .claude/agents/
cp -r plugins/project-management-system/skills/* .claude/skills/
cp plugins/project-management-system/templates/*.md .claude/templates/

# Or install at user level
mkdir -p ~/.claude/agents ~/.claude/skills ~/.claude/templates
cp plugins/project-management-system/agents/*.md ~/.claude/agents/
cp -r plugins/project-management-system/skills/* ~/.claude/skills/
cp plugins/project-management-system/templates/*.md ~/.claude/templates/
```

## Usage Examples

### Create Project Dashboard
```bash
@project-dashboard-manager "Create dashboard for active projects"
```

### Break Down Project Tasks
```bash
@task-coordinator "Create WBS for e-commerce platform migration project"
```

### Generate Timeline
```bash
@timeline-visualizer "Generate Gantt chart for Q1 2025 product launch"
```

### Archive Completed Project
```bash
@project-archiver "Archive the mobile app redesign project with lessons learned"
```

## Workflows

### Starting a New Project
1. @task-coordinator "Create WBS for [project name]"
2. @timeline-visualizer "Generate timeline from WBS"
3. @project-dashboard-manager "Create tracking dashboard"

### Weekly Status Review
1. @project-dashboard-manager "Update dashboard with latest status"
2. @timeline-visualizer "Adjust timeline based on progress"

### Project Completion
1. @project-dashboard-manager "Generate final status report"
2. @project-archiver "Archive project with lessons learned"

## Integration

Works well with:
- **orchestrator**: Complex multi-phase project coordination
- **backend-architect**: Technical project planning
- **frontend-developer**: UI/UX project planning
- **expense-manager**: Budget tracking integration
- **tax-compliance**: Compliance milestone tracking

## Best Practices

1. **Start with WBS**: Always break down work before creating timelines
2. **Update Regularly**: Keep dashboards current (weekly minimum)
3. **Track Dependencies**: Document all task dependencies upfront
4. **Document Lessons**: Archive projects properly for organizational learning
5. **Use Templates**: Leverage provided templates for consistency

## Configuration

### Agent Settings
All agents output to `/mnt/user-data/outputs/` and provide `computer://` links.

### Skill Customization
Skills can be customized by copying to `/mnt/skills/user/` and modifying:
- WBS depth and structure preferences
- Gantt chart styling
- Dashboard layout
- Risk scoring methodology

## File Outputs

Agents create:
- `.md` files for dashboards and reports
- `.md` files with Mermaid diagrams for Gantt charts
- `.json` files for structured task data
- `.md` files for archived project documentation

## Performance

- **Dashboard generation**: ~5-10 seconds for multi-project view
- **WBS creation**: ~10-20 seconds for complex projects
- **Gantt chart**: ~5-8 seconds for 20-30 tasks
- **Archive report**: ~8-12 seconds with lessons learned

## Troubleshooting

**Dashboard not updating?**
- Verify project data files exist
- Check file paths are absolute
- Ensure dashboard-template.md is accessible

**Gantt chart not rendering?**
- Validate Mermaid syntax with online editor
- Check date formats (YYYY-MM-DD)
- Verify task dependencies are valid

**WBS too shallow/deep?**
- Adjust depth parameter in task-coordinator
- Customize WBS patterns in skill file

## License

Part of the Puerto AI Agent Plugin System.

## Version

1.0.0 - Initial release with core project management capabilities

## Related Documentation

- [Project Management Skill](/mnt/skills/public/project-management/SKILL.md)
- [Gantt Visualization Skill](/mnt/skills/public/gantt-visualization/SKILL.md)
- [Plugin Development Guide](../../docs/plugin-development.md)

## Support

For issues or feature requests, see the main Puerto repository issue tracker.
