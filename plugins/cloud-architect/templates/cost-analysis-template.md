# Cloud Cost Analysis Report
**Period**: {{start_date}} to {{end_date}}
**Total Spend**: ${{total_cost}}

## Cost Breakdown
| Service | Cost | % of Total | Trend |
|---------|------|------------|-------|
{{#each services}}
| {{name}} | ${{cost}} | {{percentage}}% | {{trend}} |
{{/each}}

## Top 10 Cost Drivers
{{#each top_resources}}
{{rank}}. {{resource_name}} ({{service}}): ${{cost}}
{{/each}}

## Optimization Recommendations
### High Priority (Est. Savings: ${{high_priority_savings}}/month)
{{#each high_priority_recommendations}}
- {{recommendation}} (Savings: ${{savings}}/month)
{{/each}}

### Medium Priority (Est. Savings: ${{medium_priority_savings}}/month)
{{#each medium_recommendations}}
- {{recommendation}} (Savings: ${{savings}}/month)
{{/each}}

## Reserved Instance Recommendations
- Current RI Coverage: {{ri_coverage}}%
- Recommended Purchases: {{ri_recommendations}}
- Est. Annual Savings: ${{ri_savings}}

## Action Plan
1. {{action_1}}
2. {{action_2}}
3. {{action_3}}
