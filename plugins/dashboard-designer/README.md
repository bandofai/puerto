# Dashboard Designer Plugin

Dashboard and reporting design specialist for creating data visualizations, selecting KPIs, implementing best practices, automating reports, and customizing for stakeholders.

## Overview

The Dashboard Designer plugin provides agents for effective data visualization using proven frameworks: information density, data-ink ratio, color theory, chart selection, and stakeholder-specific design.

## Agents

### 1. kpi-selector (Sonnet, Skill-Aware)
Selects relevant KPIs aligned with business objectives using frameworks like OKRs, North Star Metric, and balanced scorecard.

**Use for**: KPI identification, metric framework, leading vs lagging indicators

**Example**:
```
Use kpi-selector for SaaS company dashboard.
Business goals:
- Increase ARR by 50%
- Improve retention to 95%
- Reduce CAC by 20%

KPI Framework:
North Star Metric: Weekly Active Users completing core action

Supporting KPIs:
Acquisition: MRR, new customers, CAC, LTV:CAC
Activation: Onboarding completion %, time to value
Retention: Churn rate, NPS, feature adoption
Revenue: ARPU, expansion revenue, upgrade rate
Referral: Referral rate, viral coefficient

Include: Targets, data sources, update frequency
```

### 2. visualization-designer (Sonnet, Skill-Aware)
Designs effective visualizations following best practices: chart selection, color theory, information density.

**Use for**: Chart type selection, color schemes, layout design, accessibility

**Example**:
```
Use visualization-designer for sales dashboard.
Data to visualize:
1. Monthly revenue trend (time series)
   → Line chart (shows trend clearly)

2. Revenue by region (comparison)
   → Bar chart (easy comparison) or map (geographic context)

3. Sales funnel (sequential stages with drop-off)
   → Funnel chart or waterfall chart

4. Product mix (part-to-whole)
   → Pie chart (max 5 categories) or stacked bar

Design principles:
- Color: Use color purposefully (red=bad, green=good, gray=neutral)
- Labels: Direct labeling (not legends when possible)
- Axes: Start at zero for bar charts, not required for line charts
- Data-ink ratio: Maximize data, minimize chart junk
```

### 3. dashboard-builder (Sonnet, Skill-Aware)
Builds complete dashboards with layout, hierarchy, interactivity, and responsiveness.

**Use for**: Dashboard layout, information architecture, user experience, tool selection

**Example**:
```
Use dashboard-builder for executive dashboard.
Audience: C-suite executives (quick overview, mobile-friendly)
Layout (F-pattern for reading):
1. Top row: Key metrics (revenue, customers, churn) - big numbers
2. Second row: Trends (revenue trend, customer growth) - line charts
3. Third row: Breakdowns (revenue by product, customers by segment) - bar charts

Tools: Tableau, Power BI, Looker, Metabase, Grafana
Features:
- Drill-down capability (click metric → see details)
- Filters (date range, product, region)
- Export to PDF/Excel
- Auto-refresh every hour
- Mobile responsive
```

### 4. report-automator (Sonnet, Skill-Aware)
Automates report generation and distribution with scheduling, recipients, and delivery formats.

**Use for**: Report automation, scheduling, distribution, format customization

**Example**:
```
Use report-automator for weekly sales report.
Recipients:
- Sales team: Detailed report (all metrics, drill-downs)
- Leadership: Executive summary (key highlights only)
- Board: Monthly summary (trends, insights)

Schedule:
- Daily: Automated email at 8am (yesterday's metrics)
- Weekly: Monday 9am (previous week summary)
- Monthly: 1st of month (previous month deep dive)

Format:
- Email: Embedded charts + PDF attachment
- Slack: Key metrics posted to #sales channel
- Dashboard: Always-on live dashboard

Automation: Python script + SQL queries + email service
```

## Skills

### dashboard-design
Data visualization and dashboard design best practices:
- **Chart Selection**: Line (trends), bar (comparison), pie (part-to-whole), scatter (correlation)
- **Color Theory**: Sequential (gradients), diverging (red-green), categorical (distinct colors)
- **Gestalt Principles**: Proximity, similarity, continuity, closure
- **Information Density**: Balance detail vs clutter (Tufte's data-ink ratio)
- **Hierarchy**: Primary metrics prominent, supporting metrics secondary
- **Interactivity**: Filters, drill-downs, tooltips, cross-filtering
- **Accessibility**: Color blindness (use patterns + color), screen readers
- **Performance**: Query optimization, caching, pre-aggregation
- **KPI Frameworks**: OKRs, North Star Metric, AARRR, balanced scorecard

## Templates

### dashboard-wireframe-template.md
Dashboard layout wireframe: Grid structure (rows and columns), metric placement (F-pattern), chart types, filters and controls, color scheme, responsive behavior.

### kpi-framework-template.md
KPI framework document: Business objectives, KPI definitions (formula, data source), targets and thresholds (red/yellow/green), update frequency, ownership, dashboard placement.

### visualization-guide-template.md
Visualization best practices guide: Chart selection matrix (data type → chart type), color palette (brand colors + semantic colors), accessibility guidelines, common mistakes to avoid.

### reporting-requirements-template.md
Reporting requirements: Stakeholder personas, information needs, frequency, format, distribution method, data sources, refresh schedule.

## Workflows

### Complete Dashboard Development
```
1. Select KPIs
Use kpi-selector to identify metrics aligned with business goals

2. Design visualizations
Use visualization-designer to choose appropriate chart types

3. Build dashboard
Use dashboard-builder to create layout and implement interactivity

4. Automate reports
Use report-automator to schedule and distribute reports
```

### Executive Dashboard
```
1. KPI selection
Use kpi-selector for North Star Metric + 5-7 supporting metrics

2. Layout design
Use dashboard-builder for clean, scannable layout (F-pattern)

3. Visualizations
Use visualization-designer for trend lines, comparison bars, big numbers

4. Delivery
Use report-automator for weekly email + always-on dashboard
```

## Requirements Met

✅ Role: Dashboard and reporting design specialist
✅ Dashboard design: dashboard-builder with layout and UX best practices
✅ KPI selection and tracking: kpi-selector with strategic frameworks
✅ Visualization best practices: visualization-designer with chart selection
✅ Report automation: report-automator with scheduling and distribution
✅ Stakeholder customization: Persona-based design in all agents
✅ Tools: Visualization tools (guidance), data analysis, design principles

## Key Features

✓ **KPI Frameworks**: North Star Metric, OKRs, AARRR, balanced scorecard
✓ **Chart Selection**: Data type → optimal chart type
✓ **Color Theory**: Sequential, diverging, categorical palettes
✓ **Information Density**: Tufte's data-ink ratio
✓ **Accessibility**: Color blindness, screen readers
✓ **Interactivity**: Filters, drill-downs, cross-filtering
✓ **Automation**: Scheduled reports, email/Slack distribution
✓ **Responsive Design**: Desktop, tablet, mobile

## Chart Selection Guide

### Time Series (trends over time)
- **Line chart**: Continuous data, multiple series
- **Area chart**: Emphasize cumulative totals
- **Spark line**: Inline mini-chart for trends

### Comparison (compare categories)
- **Bar chart**: Horizontal comparison (easier to read long labels)
- **Column chart**: Vertical comparison (timeline feel)
- **Grouped/stacked bar**: Compare subcategories

### Part-to-Whole (composition)
- **Pie chart**: Max 5 categories, shows proportions
- **Donut chart**: Same as pie, center for total
- **Treemap**: Many categories, hierarchical
- **Stacked bar**: Part-to-whole + comparison

### Distribution (spread of values)
- **Histogram**: Frequency distribution
- **Box plot**: Quartiles, outliers, distribution
- **Violin plot**: Distribution shape + density

### Relationship (correlation)
- **Scatter plot**: Two variables, find correlation
- **Bubble chart**: Three variables (x, y, size)
- **Heatmap**: Matrix of values with color intensity

### Geospatial
- **Choropleth map**: Values by region (shaded)
- **Symbol map**: Points on map (bubbles, markers)

## Color Best Practices

### Sequential (ordered data)
- Single hue gradient: Light → dark blue
- Use for: Heat maps, choropleth maps, ordered categories

### Diverging (data with meaningful midpoint)
- Two hues: Red ← gray → green
- Use for: Positive/negative values, variance from mean

### Categorical (distinct categories)
- Distinct hues: Blue, orange, green, red, purple
- Use for: Different products, regions, segments
- Max 7-10 colors (beyond that, hard to distinguish)

### Semantic (meaning-based)
- Red: Negative, danger, down, stop
- Green: Positive, success, up, go
- Yellow/orange: Warning, caution
- Blue: Neutral, information, trust
- Gray: Inactive, secondary

### Accessibility
- Don't rely on color alone (use patterns, labels)
- Check color blindness (red-green most common)
- Ensure sufficient contrast (WCAG AA: 4.5:1)

## Dashboard Layout Patterns

### F-Pattern (executives, quick scanning)
```
[Key Metric 1] [Key Metric 2] [Key Metric 3]
[Trend Chart --------------------------------]
[Comparison Chart] [Breakdown Chart]
```

### Z-Pattern (storytelling)
```
[Title/Context ----------------------------->]
[Primary Visualization ---------------------]
[Supporting Chart] [Supporting Chart]
[Insight/Action ----------------------------->]
```

### Grid Layout (operational dashboards)
```
[Metric] [Metric] [Metric] [Metric]
[Chart ] [Chart ] [Chart ] [Chart ]
[Table ] [Table ] [Table ] [Table ]
```

## KPI Metrics by Function

### Sales
- Revenue (MRR, ARR)
- Win rate
- Sales cycle length
- Pipeline value
- CAC

### Marketing
- MQLs, SQLs
- Conversion rate
- CAC
- Marketing ROI
- Attribution

### Product
- DAU/MAU ratio (stickiness)
- Feature adoption
- NPS
- Activation rate
- Retention cohorts

### Support
- CSAT
- Response time
- Resolution time
- Ticket volume
- First contact resolution

### Finance
- Revenue
- Gross margin
- Burn rate
- Runway
- LTV:CAC

## Testing

- ✅ 4 specialized agents with appropriate tools and models
- ✅ 1 comprehensive dashboard-design skill
- ✅ 4 professional templates for wireframes, KPIs, visualization, requirements
- ✅ Complete README with chart selection and color theory

Closes #82
