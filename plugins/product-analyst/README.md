# Product Analyst Plugin

Product analytics specialist for metrics tracking, funnel analysis, and experimentation.

## Agents

### metrics-tracker (Sonnet)
Defines and tracks product metrics, KPIs, and North Star metrics.

### funnel-analyzer (Sonnet)
Analyzes conversion funnels, identifies drop-offs, suggests optimizations.

### experiment-analyzer (Haiku)
Analyzes A/B tests with statistical significance and confidence intervals.

## Usage

```bash
# Track metrics
@metrics-tracker "Define metrics framework for SaaS onboarding"

# Analyze funnel
@funnel-analyzer "Analyze signup to activation funnel"

# Analyze experiment
@experiment-analyzer "Analyze A/B test results: variant A 5.2% vs variant B 6.1%, 10K users each"
```

## Skills

- **product-metrics**: Metric frameworks (AARRR, HEART), KPI selection
- **experimentation**: A/B testing, statistical significance

Closes #33
