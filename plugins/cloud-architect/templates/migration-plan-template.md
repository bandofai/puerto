# Cloud Migration Plan

## Executive Summary
- **Total Applications**: {{total_apps}}
- **Migration Strategy**: {{primary_strategy}}
- **Timeline**: {{start_date}} to {{end_date}}
- **Estimated Cost**: ${{migration_cost}}
- **Expected Savings**: ${{annual_savings}}/year

## Application Inventory
| Application | Priority | Strategy | Complexity | Timeline |
|-------------|----------|----------|------------|----------|
{{#each applications}}
| {{name}} | {{priority}} | {{strategy}} | {{complexity}} | {{timeline}} |
{{/each}}

## Migration Waves
### Wave 1 ({{wave1_date}}): Low-Risk Applications
{{#each wave1_apps}}
- {{name}}: {{reason}}
{{/each}}

### Wave 2 ({{wave2_date}}): Medium-Risk Applications
{{#each wave2_apps}}
- {{name}}: {{reason}}
{{/each}}

### Wave 3 ({{wave3_date}}): High-Risk Applications
{{#each wave3_apps}}
- {{name}}: {{reason}}
{{/each}}

## Risk Assessment
| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
{{#each risks}}
| {{risk}} | {{impact}} | {{likelihood}} | {{mitigation}} |
{{/each}}

## Success Criteria
- [ ] Zero data loss during migration
- [ ] < 4 hours downtime per application
- [ ] Performance equal to or better than on-premise
- [ ] Cost within {{budget_variance}}% of projections
