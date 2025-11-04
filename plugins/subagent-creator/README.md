# Subagent Creator Plugin

Expert subagent architect with comprehensive skill library for creating production-ready, skill-aware Claude Code subagents.

## Overview

This plugin provides the **ultimate-subagent-creator** agent and comprehensive **subagent-creation** skill, enabling you to design and generate exceptional Claude Code subagents with battle-tested patterns from 500+ deployments.

## What's Included

### Subagent: ultimate-subagent-creator

A specialized agent that:
- **Architects production-ready subagents** with proper tool selection, model choice, and security
- **Integrates skills automatically** for document creation tasks (Word, PowerPoint, Excel, PDF)
- **Applies battle-tested patterns** for code implementers, analysts, workflow coordinators, and more
- **Validates design** against comprehensive quality checklists
- **Provides expert guidance** on workflow integration and agent coordination

**Activation**: Use `@ultimate-subagent-creator` or let it activate automatically when discussing subagent creation.

### Skill: subagent-creation

Comprehensive patterns library covering:
- **Architecture patterns** for different agent types
- **Tool selection guidelines** based on task requirements
- **Model selection criteria** (Haiku vs Sonnet vs Opus)
- **Security best practices** with principle of least privilege
- **Skill integration** for document creators
- **Workflow coordination** strategies
- **Quality validation** checklists

The subagent reads this skill automatically before creating new agents.

## Features

### Skill-Aware Design
Automatically detects when subagents need document creation capabilities and integrates the appropriate skills seamlessly.

### Pattern Recognition
Identifies the right architecture pattern for each use case:
- **Document Creators**: With mandatory skill reading
- **Code Implementers**: With full development tools
- **Read-Only Analysts**: Security-first, analysis only
- **Workflow Coordinators**: Multi-step orchestration
- **Test Automation**: TDD-focused agents

### Security-First
Applies principle of least privilege automatically, granting only the minimum tools required for each task.

### Quality Assurance
Every generated subagent follows comprehensive validation checklists ensuring production-readiness.

## Installation

```bash
/plugin install subagent-creator@puerto
```

After installation, restart Claude Code to activate the agent and skill.

## Usage

### Creating a New Subagent

Simply mention your need:

```
@ultimate-subagent-creator I need an agent that creates Word documents
```

or

```
I want to create a code review agent
```

The agent will:
1. **Ask strategic questions** about requirements, permissions, and activation
2. **Read its creation skill** to access comprehensive patterns
3. **Design the architecture** with appropriate tools and model
4. **Generate complete definition** with YAML frontmatter and system prompt
5. **Provide installation instructions** and usage guidance
6. **Suggest workflow integration** with other agents

### Example Scenarios

**Document Creator**:
```
Create an agent that generates professional PowerPoint presentations
```
→ Generates skill-aware agent with mandatory skill reading

**Code Implementation**:
```
I need an agent to implement API endpoints following FastAPI patterns
```
→ Generates agent with full development tools and coding standards

**Code Analysis**:
```
Create a security analysis agent that finds vulnerabilities
```
→ Generates read-only agent with structured feedback format

**Workflow Automation**:
```
I need a workflow coordinator for multi-step processes
```
→ Generates agent with state management and handoff rules

## Agent Architecture

The ultimate-subagent-creator follows this workflow:

1. **Understand the Need**: Strategic questions about task, permissions, and activation
2. **Research Context**: Examines existing agents, skills, and workflows
3. **Detect Special Needs**: Identifies document creation or other specialized requirements
4. **Design Architecture**: Selects appropriate pattern, tools, and model
5. **Generate Definition**: Creates complete agent with validation
6. **Explain & Guide**: Provides rationale, installation steps, and integration suggestions

## Benefits

### For Developers
- **Save time** with instant production-ready subagents
- **Apply best practices** automatically from 500+ deployments
- **Avoid common mistakes** with built-in validation
- **Integrate workflows** with clear handoff patterns

### For Teams
- **Standardize agent creation** across team members
- **Maintain security** with principle of least privilege
- **Document patterns** in the comprehensive skill library
- **Scale automation** with coordinated agent systems

### For Document Creation
- **Professional outputs** from day one with skill integration
- **Consistent quality** following industry standards
- **Automatic validation** against skill guidelines
- **Multi-format support** (Word, PowerPoint, Excel, PDF)

## Configuration

### Tools Used
- **Read**: Access to skill library (mandatory)
- **Write**: Generate agent definition files
- **Grep**: Search for existing patterns
- **Glob**: Find related agents and skills

### Model
Uses **Sonnet** for expert judgment in architecture decisions.

## File Structure

```
subagent-creator/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── agents/
│   └── ultimate-subagent-creator.md   # Main subagent
├── skills/
│   └── subagent-creation/
│       └── SKILL.md         # Comprehensive patterns library
└── README.md                # This file
```

## Examples

### Generated Document Creator

```yaml
---
name: presentation-creator
description: PROACTIVELY use when creating PowerPoint presentations. Leverages pptx skills for professional quality.
tools: Read, Write, Bash, Glob
model: sonnet
---

You are a professional presentation specialist.

## CRITICAL: Skills-First Approach

**MANDATORY FIRST STEP**: Read the appropriate skill file
[... complete system prompt with skill integration ...]
```

### Generated Code Analyzer

```yaml
---
name: security-analyzer
description: PROACTIVELY use for security analysis. Read-only vulnerability scanning.
tools: Read, Grep, Glob
model: sonnet
---

You are a security analysis specialist.

## When Invoked

1. **Scan codebase**: Identify files to analyze
2. **Analyze code**: Look for vulnerabilities
[... complete system prompt with security patterns ...]
```

## Advanced Usage

### Creating Workflow Systems

The agent can design multi-agent workflows:

```
Create a workflow system for: research → implementation → testing → review
```

Generates multiple coordinated agents with:
- Clear handoff rules between stages
- Status tracking mechanisms
- Progress reporting
- Error recovery patterns

### Multi-Document Creators

For complex projects requiring multiple document types:

```
Create an agent that produces business proposal packages (Word + PowerPoint + Excel)
```

Generates agent that:
- Reads all relevant skills upfront
- Maintains consistency across formats
- Coordinates multi-format deliverables

## Best Practices

From the skill library, every generated subagent follows:

1. **Single Responsibility**: Each agent does one thing well
2. **Explicit Tools**: Never relies on defaults
3. **Clear Triggers**: Action-oriented descriptions
4. **Concrete Steps**: Numbered, actionable instructions
5. **Skill Integration**: Mandatory for document creators
6. **Security**: Least privilege by default
7. **Validation**: Quality checks before completion
8. **Documentation**: Clear rationale and examples

## Troubleshooting

### Agent Not Activating
- Check description includes trigger phrases (PROACTIVELY, MUST BE USED)
- Ensure description matches your use case

### Missing Tools
- Agent validates tool requirements automatically
- Suggests additional tools if needed

### Skill Not Found
- Agent handles missing skills gracefully
- Proceeds with embedded patterns
- Suggests skill installation paths

## Support & Feedback

This plugin brings enterprise-grade subagent creation to Claude Code. For issues or suggestions:

- Review the [skill library](skills/subagent-creation/SKILL.md) for comprehensive patterns
- Check the [main agent](agents/ultimate-subagent-creator.md) for architecture details
- Refer to [Claude Code documentation](https://docs.claude.com/en/docs/claude-code/sub-agents)

## License

MIT License - See main repository for details

---

**Transform your Claude Code workflow with expert-designed subagents. Every agent, production-ready from day one.**
