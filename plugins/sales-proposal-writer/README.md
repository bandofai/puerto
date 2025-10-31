# Sales Proposal Writer Plugin

> Sales proposal creation specialist - Generate and customize compelling sales proposals and RFP responses

## Overview

The Sales Proposal Writer plugin provides specialized agents for creating professional, winning sales proposals. It helps sales teams and business development professionals generate customized proposals quickly while maintaining high quality and consistency.

## Features

### Agents

- **proposal-generator** (Sonnet): Create customized proposals from templates
- **pricing-calculator** (Haiku): Calculate accurate pricing with discounts
- **case-study-selector**: Select relevant customer success stories
- **rfp-responder**: Generate comprehensive RFP responses
- **template-customizer**: Apply advanced proposal customizations

### Skills

- **proposal-generation**: Comprehensive proposal writing patterns, templates, and best practices
- **pricing-calculation**: Pricing strategies, discount structures, and ROI calculations

## Quick Start

### Installation

```bash
# Install the plugin
/plugin install sales-proposal-writer@puerto
```

### Basic Usage

**Generate a proposal:**
```bash
@proposal-generator create proposal for "Acme Corp" using consulting-services template
```

**Calculate pricing:**
```bash
@pricing-calculator calculate --service "consulting" --hours 200 --rate 250
```

**Select case studies:**
```bash
@case-study-selector find relevant cases for "B2B SaaS, $5M ARR, scaling challenges"
```

## Use Cases

### Consulting Services Proposal
```
User: "Create a proposal for Acme Corp for our 3-month consulting engagement"

@proposal-generator will:
1. Load consulting services template
2. Gather Acme Corp information
3. Select 2-3 relevant case studies
4. Calculate pricing based on scope
5. Generate customized proposal document
```

### RFP Response
```
User: "Help me respond to this RFP" [attach RFP document]

@rfp-responder will:
1. Parse RFP requirements
2. Match requirements to capabilities
3. Generate compliant responses for each section
4. Include relevant case studies and social proof
5. Format according to RFP guidelines
```

### Pricing Options
```
User: "Calculate pricing options for 150 hours of senior consulting"

@pricing-calculator will:
1. Calculate base pricing
2. Apply volume discounts
3. Generate 3 pricing options (fixed, retainer, hourly)
4. Show ROI projections
5. Format pricing table for proposal
```

## Proposal Templates

Available templates in `templates/`:

- `base-proposal.md`: Standard proposal structure
- `consulting-services.md`: Consulting engagement template
- `software-licensing.md`: Software product sales
- `managed-services.md`: Ongoing service agreements
- `rfp-response.md`: RFP response format

## Best Practices

### Winning Proposals

1. **Lead with value**: Start with client's biggest pain point
2. **Be specific**: Use concrete metrics and examples
3. **Personalize heavily**: Reference client's specific situation
4. **Include social proof**: 2-3 relevant case studies
5. **Clear pricing**: Transparent, easy-to-understand pricing
6. **Make it easy to say yes**: Simple acceptance process

### Proposal Structure

```
1. Executive Summary (one-page overview)
2. Understanding Your Needs (demonstrate research)
3. Proposed Solution (detailed approach)
4. Why Us (differentiators)
5. Case Studies (social proof)
6. Investment (transparent pricing)
7. Terms & Conditions (clear scope)
8. Next Steps (call-to-action)
```

## Configuration

### Pricing Settings

Edit `config/pricing.json` to set your rates:

```json
{
  "hourly_rates": {
    "junior": 150,
    "senior": 250,
    "principal": 400
  },
  "volume_discounts": {
    "100_hours": 0.05,
    "250_hours": 0.10,
    "500_hours": 0.15
  },
  "package_pricing": {
    "starter": 10000,
    "professional": 25000,
    "enterprise": 75000
  }
}
```

## Integration

### With CRM
```bash
# Import client data from CRM
@proposal-generator import-client --crm salesforce --client-id "001"
```

### With Document Systems
```bash
# Export proposal to various formats
@proposal-generator export --format pdf --output "proposals/acme-corp-2025.pdf"
@proposal-generator export --format docx --output "proposals/acme-corp-2025.docx"
```

## Tips for Success

### Research Before Writing
- Review client website and recent news
- Understand their industry challenges
- Research decision-makers on LinkedIn
- Find public statements about goals

### Customization Wins
- Use client's terminology and language
- Reference their specific situation
- Align with their stated objectives
- Include industry-specific insights

### Metrics Matter
- Include specific outcomes (2x growth, 50% reduction)
- Show ROI calculations
- Provide realistic timelines
- Back claims with case studies

## Examples

### Example 1: Quick Consulting Proposal

```bash
# Generate proposal with client research
@proposal-generator create \
    --client "Acme Corp" \
    --service "RevOps Consulting" \
    --duration "3 months" \
    --budget "50000" \
    --template "consulting-services"
```

**Output**: Customized 8-page proposal with:
- Executive summary tailored to Acme's goals
- 3-phase implementation plan
- 2 relevant case studies (similar companies)
- Detailed pricing breakdown
- Clear ROI projection

### Example 2: Product Sales Proposal

```bash
# Create SaaS product proposal
@proposal-generator create \
    --client "StartupXYZ" \
    --product "Analytics Platform" \
    --tier "professional" \
    --template "software-licensing"
```

**Output**: Product proposal with:
- Solution overview
- Feature comparison table
- Pricing tiers (Starter, Professional, Enterprise)
- Implementation timeline
- Customer testimonials

## Troubleshooting

**Issue**: Proposal feels generic

**Solution**: Add more client research
```bash
@proposal-generator research-client --name "Acme Corp" --deep true
# Then regenerate proposal with additional context
```

**Issue**: Pricing doesn't match company standards

**Solution**: Update pricing configuration
```bash
# Edit config/pricing.json with your rates
@pricing-calculator validate-config  # Verify settings
```

**Issue**: Missing relevant case studies

**Solution**: Add case studies to database
```bash
@case-study-selector add --client "ClientName" --industry "SaaS" --results "2x growth"
```

## Contributing

To add new proposal templates:

1. Create template in `templates/your-template.md`
2. Use `{{PLACEHOLDER}}` syntax for variables
3. Include all standard sections
4. Test with `@proposal-generator test-template`

## License

MIT

## Support

For issues and questions:
- GitHub Issues: https://github.com/bandofai/puerto/issues
- Documentation: https://github.com/bandofai/puerto/blob/main/docs

---

**Remember**: A winning proposal tells a story of transformation from current pain to desired future state. Focus on client outcomes, not your credentials.
