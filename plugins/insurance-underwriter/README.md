# Insurance Underwriter Plugin

A comprehensive insurance underwriting system providing professional risk assessment, policy pricing, claims analysis, and renewal evaluation capabilities.

## Overview

This plugin provides a complete suite of AI agents specialized in insurance underwriting tasks, from initial risk assessment through policy pricing, claims history analysis, and renewal decisions.

## Architecture

### Multi-Agent System

1. **risk-assessor** (Sonnet) - Conducts comprehensive risk evaluation with professional judgment
2. **policy-pricer** (Haiku) - Fast, accurate premium calculations and pricing worksheets
3. **claims-analyzer** (Sonnet) - Analyzes claims history patterns and risk indicators
4. **renewal-evaluator** (Sonnet) - Evaluates renewal applications with updated risk profiles
5. **underwriting-orchestrator** (Sonnet) - Coordinates complete underwriting workflows

### Design Philosophy

- **Specialized Agents**: Each agent has single clear responsibility
- **Model Selection**: Haiku for calculations, Sonnet for judgment
- **Skills-First**: All agents leverage comprehensive underwriting skills
- **Template-Driven**: Standardized outputs for consistency
- **Quality Standards**: Professional insurance industry compliance

## Agents

### Risk Assessor
**Purpose**: Comprehensive risk evaluation and classification
**Model**: Sonnet (requires professional judgment)
**Use When**: New applications, significant policy changes, high-value policies

```bash
@risk-assessor "Evaluate commercial property at 123 Main St - retail building, $2M value"
```

### Policy Pricer
**Purpose**: Premium calculations and pricing worksheets
**Model**: Haiku (fast calculations)
**Use When**: Need quick pricing, rate comparisons, premium estimates

```bash
@policy-pricer "Calculate premium for homeowners policy - $500K dwelling, $100K contents"
```

### Claims Analyzer
**Purpose**: Claims history analysis and pattern detection
**Model**: Sonnet (requires analytical judgment)
**Use When**: Reviewing applicant claims history, renewal evaluation

```bash
@claims-analyzer "Analyze claims history for applicant ID 12345 - 3 claims in 5 years"
```

### Renewal Evaluator
**Purpose**: Policy renewal evaluation and pricing adjustments
**Model**: Sonnet (complex decision making)
**Use When**: Annual renewals, mid-term changes, coverage updates

```bash
@renewal-evaluator "Evaluate renewal for Policy #ABC-123 - homeowners, 5-year history"
```

### Underwriting Orchestrator
**Purpose**: Complete end-to-end underwriting workflows
**Model**: Sonnet (coordination and decision making)
**Use When**: New applications requiring full underwriting process

```bash
@underwriting-orchestrator "Process new commercial auto application - 10 vehicles, $5M coverage"
```

## Skills

### Risk Assessment
Comprehensive risk evaluation methodologies covering:
- Property risk factors (construction, location, protection)
- Liability exposure assessment
- Loss control evaluation
- Risk classification systems
- Hazard identification

### Policy Pricing
Premium calculation frameworks including:
- Base rate determination
- Risk factor adjustments
- Credit-based pricing
- Territory rating
- Deductible credits
- Multi-policy discounts

### Claims Analysis
Claims evaluation techniques covering:
- Frequency and severity analysis
- Pattern recognition
- Red flag identification
- Loss ratio calculations
- Predictive indicators

## Templates

### Risk Assessment Template
Standardized risk evaluation reports with:
- Property/exposure details
- Risk factors and scores
- Hazard identification
- Recommendations
- Underwriting decision

### Pricing Worksheet
Complete premium calculation documentation:
- Base rates and classifications
- All rating factors applied
- Credit and discounts
- Final premium breakdown
- Competitive comparison

### Underwriting Decision
Final decision documentation:
- Decision (approve/decline/refer)
- Supporting rationale
- Conditions or exclusions
- Required endorsements
- Follow-up items

### Renewal Evaluation
Renewal analysis reports:
- Policy performance review
- Claims experience
- Current risk factors
- Rate adjustment justification
- Retention recommendations

## Quick Start

### Basic Workflow

1. **Initial Risk Assessment**
   ```bash
   @risk-assessor "Evaluate risk for [type] policy - [key details]"
   ```

2. **Price the Policy**
   ```bash
   @policy-pricer "Calculate premium based on [risk factors]"
   ```

3. **Review Claims History** (if applicable)
   ```bash
   @claims-analyzer "Analyze claims for applicant [ID] - [summary]"
   ```

4. **Make Decision**
   Review outputs and document final underwriting decision

### Complete Underwriting

For full end-to-end process:

```bash
@underwriting-orchestrator "Process [policy type] application:
- Applicant: [name/ID]
- Coverage: [limits and types]
- Key details: [relevant information]"
```

The orchestrator will:
1. Conduct risk assessment
2. Calculate pricing
3. Analyze claims (if applicable)
4. Generate underwriting decision
5. Package all documentation

## Use Cases

### Personal Lines

**Homeowners Insurance**
```bash
@risk-assessor "Homeowners - 2000 sqft single-family, brick construction, central station alarm, 2015 build, Dallas TX"
@policy-pricer "HO3 policy - $400K dwelling, $300K contents, $500K liability, $2500 deductible"
```

**Auto Insurance**
```bash
@risk-assessor "Personal auto - 2020 Honda Accord, 35yo driver, clean record, 10K miles/year"
@claims-analyzer "Review driver claims - 1 at-fault accident 3 years ago, no other claims"
@policy-pricer "Full coverage - $50K/$100K/$50K, $500 comp/coll deductible"
```

### Commercial Lines

**Commercial Property**
```bash
@risk-assessor "Commercial property - 15,000 sqft office building, fire-resistive, sprinklered, built 2010"
@policy-pricer "BOP policy - $3M building, $1M contents, $2M liability"
```

**Workers Compensation**
```bash
@risk-assessor "Workers comp - Construction company, 50 employees, $5M payroll"
@claims-analyzer "Review loss runs - 5 claims in 3 years, 1.2 experience mod"
@policy-pricer "Calculate WC premium - payroll by class code, experience mod applied"
```

### Renewals

```bash
@renewal-evaluator "Evaluate renewal for Policy #XYZ-789:
- Type: Commercial General Liability
- Current Premium: $15,000
- Claims: 2 small claims this year
- Coverage: $2M occurrence, $4M aggregate
- Years with company: 3"
```

## Best Practices

### Risk Assessment
1. Gather complete information before assessment
2. Use standardized risk scoring
3. Document all significant hazards
4. Provide clear recommendations
5. Follow company underwriting guidelines

### Pricing
1. Verify all rating factors
2. Apply credits consistently
3. Document competitive position
4. Consider market conditions
5. Review for reasonableness

### Claims Analysis
1. Review complete claims history (5+ years)
2. Look for patterns and trends
3. Verify current claims status
4. Consider severity and frequency
5. Compare to industry benchmarks

### Decision Making
1. Follow underwriting authority limits
2. Document rationale clearly
3. Consider risk appetite
4. Balance pricing and risk
5. Ensure regulatory compliance

## Output Locations

All generated files are saved to:
```
/mnt/user-data/outputs/insurance-underwriting/
```

Access via computer links:
```
computer:///mnt/user-data/outputs/insurance-underwriting/[filename]
```

## Integration

### With Other Plugins

**Risk Management**
- Risk assessment feeds into risk management planning
- Loss control recommendations

**Financial Analysis**
- Premium projections for financial modeling
- Loss ratio analysis

**Compliance**
- Regulatory filing requirements
- Rate compliance verification

### Workflow Integration

This plugin integrates with standard underwriting workflows:

1. **Submission Intake** → risk-assessor
2. **Risk Assessment** → policy-pricer
3. **Pricing** → claims-analyzer (if needed)
4. **Claims Review** → renewal-evaluator (renewals)
5. **Final Decision** → underwriting-orchestrator (coordination)

## Performance

- **Risk Assessment**: ~45-60 seconds (Sonnet - comprehensive analysis)
- **Policy Pricing**: ~10-15 seconds (Haiku - fast calculations)
- **Claims Analysis**: ~30-45 seconds (Sonnet - pattern recognition)
- **Renewal Evaluation**: ~40-55 seconds (Sonnet - complex evaluation)
- **Full Underwriting**: ~2-3 minutes (complete workflow)

## Quality Standards

All agents follow professional insurance standards:

- Accurate risk classification
- Consistent pricing methodology
- Comprehensive documentation
- Regulatory compliance
- Clear decision rationale
- Professional formatting

## Version History

### v1.0.0 (2025-10-21)
- Initial release
- 5 specialized agents
- 3 comprehensive skills
- 4 professional templates
- Complete underwriting workflow support

## Support

For issues, questions, or enhancements:
- Review agent documentation in `agents/` directory
- Check skills in `skills/` directory
- Examine templates in `templates/` directory
- Verify .claude-plugin configuration

## License

Part of the Puerto AI Plugin System
