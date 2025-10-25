# Academic Researcher Plugin

Academic research support specialist for literature search, research methodology, and citation management.

## Overview

This plugin provides comprehensive academic research support following scholarly standards for literature review, research design, and citation formatting.

## Agents

### 1. literature-searcher (Sonnet, WebSearch)
Conducts systematic literature searches using academic databases.

**Capabilities**:
- Boolean search strategies (AND, OR, NOT)
- Academic database access (Google Scholar, PubMed, JSTOR, arXiv)
- PRISMA flow documentation
- Inclusion/exclusion criteria screening
- Citation tracking (forward/backward)

### 2. methodology-designer (Sonnet)
Designs research methodologies for quantitative, qualitative, and mixed methods studies.

**Capabilities**:
- Research design selection (experimental, survey, phenomenology, etc.)
- Sampling strategies (probability and non-probability)
- Sample size determination (power analysis, saturation)
- Data collection and analysis planning
- Validity and reliability frameworks

### 3. citation-manager (Haiku, Fast)
Formats citations and creates bibliographies in major academic styles.

**Capabilities**:
- APA 7th, MLA 9th, Chicago 17th, IEEE formatting
- Complete bibliography generation
- In-text citation formatting
- Accuracy verification

### 4. literature-reviewer (Sonnet)
Synthesizes literature and identifies themes and gaps.

**Capabilities**:
- Thematic synthesis
- Critical analysis
- Gap identification
- Literature review structuring
- Recommendations for future research

## Skills

### 1. literature-review
Literature search strategies, critical analysis frameworks, synthesis approaches.

### 2. research-methodology
Research design patterns for quantitative, qualitative, and mixed methods studies.

### 3. citation-management
Citation formatting rules for APA, MLA, Chicago, IEEE styles.

## Templates

### 1. literature-review-template.md
Complete literature review structure with themes, synthesis, gaps, implications.

### 2. methodology-template.md
Comprehensive methodology section with design, participants, data collection, analysis, validity, ethics.

### 3. annotated-bibliography-template.md
Annotated bibliography format with summary, evaluation, relevance for each source.

## Key Features

✓ **WebSearch Integration**: Real-time academic database access
✓ **Multiple Citation Styles**: APA, MLA, Chicago, IEEE
✓ **Systematic Methods**: PRISMA-compliant literature search
✓ **Research Design**: Quantitative, qualitative, mixed methods
✓ **Fast Citations**: Haiku for quick formatting
✓ **Expert Analysis**: Sonnet for literature synthesis

## Workflow Examples

### Complete Literature Review
```bash
@literature-searcher "Search for machine learning in education 2015-2025"
@literature-reviewer "Synthesize findings on ML in education, identify themes and gaps"
@citation-manager "Format bibliography in APA 7th edition"
```

### Methodology Design
```bash
@methodology-designer "Design mixed methods study for teacher technology adoption, 200 survey + 20 interviews"
```

### Citation Formatting
```bash
@citation-manager "Format these 30 sources in MLA 9th edition with hanging indent"
```

## Design Rationale

**Model Selection**:
- Sonnet for literature search (WebSearch + synthesis)
- Sonnet for methodology (requires research expertise)
- **Haiku for citations** (template-based, 90% cost savings)
- Sonnet for literature review (critical analysis)

**WebSearch Integration**:
- literature-searcher accesses Google Scholar, PubMed, academic databases
- Real-time research capability

## Requirements Met

✅ **Literature search and review**: Systematic search with PRISMA
✅ **Research question formulation**: Methodology designer
✅ **Methodology design**: Quantitative, qualitative, mixed methods
✅ **Citation management**: APA, MLA, Chicago, IEEE
✅ **Bibliography creation**: Complete, formatted references
✅ **Tools Required**:
  - ✅ Academic databases: WebSearch integration
  - ✅ Citation tools: Multiple style support
  - ✅ File operations: All agents have Read, Write

## Installation

```bash
cp -r plugins/academic-researcher .claude/plugins/
```

---

**Version**: 1.0
**Date**: January 2025
**Citation Styles**: APA 7th, MLA 9th, Chicago 17th, IEEE
