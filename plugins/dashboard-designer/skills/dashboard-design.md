# Dashboard Design Skill

Comprehensive patterns for creating effective dashboards, selecting KPIs, designing visualizations, and automating reports using proven data visualization principles.

## Core Principles

### Edward Tufte's Principles
- **Data-ink ratio**: Maximize the ink used to display actual data, minimize chart decoration
- **Chartjunk elimination**: Remove unnecessary grid lines, 3D effects, and decorative elements
- **Information density**: Show the maximum amount of data in the smallest space without clutter
- **Small multiples**: Use repeated charts with same scale for comparison
- **Sparklines**: Intense, simple, word-sized graphics for inline trend display

### Stephen Few's Dashboard Design
- **Dashboard types**: Operational (real-time monitoring), tactical (trends/patterns), strategic (KPIs/goals)
- **Optimal layout**: Most important information top-left (F-pattern reading)
- **Visual perception**: Pre-attentive attributes (color, size, position)
- **Gestalt principles**: Proximity, similarity, enclosure, connection
- **Information scent**: Clear navigation and labeling

### Alberto Cairo's Data Visualization
- **Truthfulness**: Accurate representation without distortion
- **Functionality**: Serves the intended purpose effectively
- **Beauty**: Aesthetically pleasing and professional
- **Insightfulness**: Reveals patterns and relationships
- **Enlightenment**: Changes perception and understanding

## Chart Selection Framework

### Time Series Data (trends over time)
**Line Chart**
- Best for: Continuous data, multiple series comparison
- When to use: Stock prices, temperature over time, user growth
- Avoid: Too many lines (max 5-7), categorical data
- Example: Monthly revenue trend, daily active users

**Area Chart**
- Best for: Cumulative totals, part-to-whole over time
- When to use: Stacked categories showing total and breakdown
- Avoid: Too many layers (hard to read middle layers)
- Example: Revenue by product category over time

**Spark Line**
- Best for: Inline micro-charts, quick trend indication
- When to use: Dashboard tables, compact displays
- Avoid: When detail matters, need exact values
- Example: 7-day trend next to current metric

### Comparison Data (comparing categories)
**Bar Chart (Horizontal)**
- Best for: Comparing categories with long labels
- When to use: Ranking items, showing magnitude
- Avoid: Time series data, too many bars (max 15)
- Example: Revenue by sales region, product rankings

**Column Chart (Vertical)**
- Best for: Comparing categories with short labels
- When to use: Comparing discrete groups
- Avoid: Long category names (use horizontal bars)
- Example: Monthly sales by quarter, daily signups

**Grouped Bar Chart**
- Best for: Comparing subcategories within categories
- When to use: Multiple metrics per category
- Avoid: More than 3 subcategories (cluttered)
- Example: Revenue vs. cost by region

**Stacked Bar Chart**
- Best for: Part-to-whole comparison across categories
- When to use: Show total and breakdown simultaneously
- Avoid: Comparing middle segments (hard to compare)
- Example: Budget allocation by department

### Part-to-Whole Data (composition)
**Pie Chart**
- Best for: Simple proportions (max 5 slices)
- When to use: Market share, budget allocation
- Avoid: More than 5 categories, comparing similar sizes
- Example: Traffic sources (organic, paid, direct, social)

**Donut Chart**
- Best for: Same as pie, with center for total/label
- When to use: Need to display total value
- Avoid: Same as pie chart
- Example: Revenue breakdown with total in center

**Treemap**
- Best for: Hierarchical part-to-whole, many categories
- When to use: Complex hierarchies, space-efficient display
- Avoid: When exact proportions matter
- Example: Disk space usage by folder

**Waterfall Chart**
- Best for: Sequential additions/subtractions showing cumulative effect
- When to use: Profit/loss breakdown, budget variance
- Avoid: Non-sequential data
- Example: Revenue minus expenses equals profit

### Distribution Data (spread of values)
**Histogram**
- Best for: Frequency distribution of continuous data
- When to use: Understanding data distribution shape
- Avoid: Categorical data (use bar chart)
- Example: Customer age distribution, response times

**Box Plot**
- Best for: Statistical distribution (quartiles, outliers)
- When to use: Comparing distributions across groups
- Avoid: Non-technical audiences
- Example: Salary ranges by department

**Violin Plot**
- Best for: Distribution density + box plot combined
- When to use: Showing full distribution shape
- Avoid: Simple comparisons (use box plot)
- Example: Response time distribution by server

### Relationship Data (correlation)
**Scatter Plot**
- Best for: Correlation between two continuous variables
- When to use: Finding relationships, outliers
- Avoid: Too many points (thousands), categorical data
- Example: Ad spend vs. revenue, age vs. purchase amount

**Bubble Chart**
- Best for: Three variables (x, y, size)
- When to use: Adding dimension to scatter plot
- Avoid: Too many bubbles (overlap), size encoding issues
- Example: Countries by GDP (x), life expectancy (y), population (size)

**Heatmap**
- Best for: Matrix of values with color intensity
- When to use: Correlations, dense data grids
- Avoid: When exact values crucial
- Example: Correlation matrix, daily activity by hour

### Geospatial Data (location-based)
**Choropleth Map**
- Best for: Values by geographic region
- When to use: Regional comparisons (sales by state)
- Avoid: Non-geographic groupings
- Example: Election results, COVID cases by county

**Symbol Map**
- Best for: Point locations with variable size/color
- When to use: Store locations, event mapping
- Avoid: Overlapping markers
- Example: Store revenue by location

**Flow Map**
- Best for: Movement between locations
- When to use: Migration, shipping routes, traffic
- Avoid: Too many flows (cluttered)
- Example: User traffic between pages

### KPI/Metric Display
**Big Number (Scorecard)**
- Best for: Single most important metric
- When to use: Primary KPI, dashboard header
- Avoid: Too many numbers (diminishes importance)
- Example: Current MRR, active users, NPS score

**Gauge Chart**
- Best for: Progress toward goal with defined range
- When to use: Capacity utilization, goal achievement
- Avoid: Overuse (takes up space), multiple gauges
- Example: Quarterly revenue vs. target

**Bullet Chart**
- Best for: Gauge alternative, more compact
- When to use: Performance vs. target with context
- Avoid: When simple number sufficient
- Example: Sales vs. quota with good/fair/poor zones

## KPI Selection Frameworks

### SMART Criteria for KPIs
- **Specific**: Clearly defined, no ambiguity
- **Measurable**: Quantifiable with data
- **Achievable**: Realistic given resources
- **Relevant**: Aligned with business objectives
- **Time-bound**: Specific timeframe for achievement

### North Star Metric
**Definition**: Single metric that best captures core value delivered to customers

**Examples by Business Type**:
- E-commerce: Orders per active customer
- SaaS: Weekly active users completing core action
- Marketplace: Gross merchandise value (GMV)
- Media: Time spent consuming content
- B2B: Active users in paying accounts

**Supporting Metrics**: Metrics that drive the North Star
- Acquisition metrics (new users, traffic sources)
- Activation metrics (onboarding completion, time to value)
- Engagement metrics (feature usage, session duration)
- Retention metrics (churn rate, cohort retention)
- Revenue metrics (ARPU, LTV)

### AARRR (Pirate Metrics)
**Acquisition**: How users find you
- Traffic sources, new visitors, sign-up rate
- Cost per acquisition (CPA), conversion rate

**Activation**: First user experience
- Onboarding completion rate, time to first value
- Feature discovery, setup completion

**Retention**: Users coming back
- Daily/weekly/monthly active users (DAU/WAU/MAU)
- Churn rate, retention cohorts, stickiness (DAU/MAU)

**Revenue**: Monetization
- MRR/ARR, ARPU, customer lifetime value (LTV)
- LTV:CAC ratio, expansion revenue

**Referral**: Viral growth
- Referral rate, viral coefficient, NPS
- Shares, invites sent, referral conversion

### Balanced Scorecard
**Financial Perspective**
- Revenue, profit margin, ROI, cost reduction
- Cash flow, shareholder value

**Customer Perspective**
- Customer satisfaction (CSAT, NPS), retention rate
- Market share, brand perception

**Internal Process Perspective**
- Process efficiency, quality metrics, cycle time
- Innovation rate, error rate

**Learning & Growth Perspective**
- Employee satisfaction, skill development
- Technology capability, innovation pipeline

### OKRs (Objectives and Key Results)
**Structure**:
- Objective: Qualitative, inspiring goal
- Key Results: 3-5 measurable outcomes (quantitative)

**Example**:
- Objective: Become the market leader in customer satisfaction
- KR1: Increase NPS from 45 to 65
- KR2: Reduce support response time to under 2 hours
- KR3: Achieve 95% customer retention rate

### Leading vs. Lagging Indicators
**Lagging Indicators** (outcomes, historical)
- Revenue, profit, market share
- Customer satisfaction, churn rate
- Hard to influence directly, measure past performance

**Leading Indicators** (predictive, actionable)
- Website traffic, trial signups, pipeline value
- Feature adoption, engagement metrics
- Can influence directly, predict future outcomes

**Best Practice**: Combine both types
- Lagging: Revenue (what happened)
- Leading: Sales pipeline, demo requests (what will happen)

## Color Theory for Dashboards

### Color Schemes

**Sequential (single hue gradient)**
```
Light Blue → Blue → Dark Blue
Use for: Ordered data, heatmaps, choropleth maps
Example: Revenue intensity by region
```

**Diverging (two hues from center)**
```
Red ← White → Green
Red ← Gray → Blue
Use for: Data with meaningful midpoint, positive/negative
Example: Variance from target (red=under, green=over)
```

**Categorical (distinct hues)**
```
Blue, Orange, Green, Red, Purple, Brown, Pink
Use for: Different categories with no order
Example: Product lines, customer segments
Limit: Maximum 7-10 colors for distinguishability
```

### Semantic Color Conventions
- **Red**: Danger, negative, below target, stop, decrease
- **Green**: Success, positive, above target, go, increase
- **Yellow/Orange**: Warning, attention needed, caution
- **Blue**: Neutral, information, trust, primary action
- **Gray**: Inactive, disabled, secondary information
- **Purple**: Premium, advanced features

### Accessibility Guidelines

**Color Blindness Considerations**:
- Red-Green color blindness: 8% of males, 0.5% of females
- Solution: Use color + pattern/texture/icon
- Test tools: Coblis, Color Oracle

**WCAG Contrast Requirements**:
- Normal text: 4.5:1 minimum (AA), 7:1 enhanced (AAA)
- Large text: 3:1 minimum (AA), 4.5:1 enhanced (AAA)
- UI components: 3:1 minimum

**Best Practices**:
- Don't rely on color alone (add labels, patterns)
- Provide text alternatives
- Use high contrast between text and background
- Test with color blindness simulators

## Dashboard Layout Patterns

### F-Pattern Layout (Executive Dashboards)
**Reading pattern**: Left to right, top to bottom, emphasis on left
```
[KPI 1]     [KPI 2]     [KPI 3]     [KPI 4]
[Primary Chart - Full Width              ]
[Secondary Chart] [Secondary Chart]
[Detail Table                            ]
```

**Use for**: Quick scanning, busy executives, mobile-friendly
**Characteristics**: Most important top-left, decreasing importance

### Z-Pattern Layout (Storytelling)
**Reading pattern**: Top-left → top-right → diagonal → bottom-left → bottom-right
```
[Title/Context --------------------------->]
[Primary Visualization ---------------------]
[Supporting Data] [Supporting Data]
[Insight/Recommendation ------------------->]
```

**Use for**: Presentations, reports, guided analysis
**Characteristics**: Narrative flow, clear start and end

### Grid Layout (Operational Dashboards)
**Reading pattern**: Uniform grid, all equal importance
```
[Metric] [Metric] [Metric] [Metric]
[Chart]  [Chart]  [Chart]  [Chart]
[Table]  [Table]  [Table]  [Table]
```

**Use for**: Real-time monitoring, control rooms, NOC dashboards
**Characteristics**: Dense information, all visible at once

### Card Layout (Responsive Design)
**Reading pattern**: Top to bottom, stacked cards
```
[Card: KPI Summary    ]
[Card: Trend Chart    ]
[Card: Breakdown      ]
[Card: Recent Activity]
```

**Use for**: Mobile dashboards, responsive layouts
**Characteristics**: Vertical scroll, self-contained cards

### Dashboard Hierarchy
**Primary Level** (Always visible):
- North Star Metric or most critical KPI
- High-level summary (big numbers)
- Placement: Top-left, largest size

**Secondary Level** (Supporting context):
- Trends, comparisons, breakdowns
- Placement: Middle sections

**Tertiary Level** (Details on demand):
- Detailed tables, drill-down data
- Placement: Bottom, collapsible sections

## Interactivity Patterns

### Filters
- **Global filters**: Apply to entire dashboard (date range, region)
- **Local filters**: Apply to single chart
- **Filter persistence**: Remember selections across sessions
- **Filter indicators**: Show active filters clearly

### Drill-Down
- **Click-through**: Click metric → see detailed breakdown
- **Breadcrumbs**: Show navigation path
- **Context preservation**: Maintain filters during drill-down
- **Level limits**: 3-4 levels maximum (avoid deep nesting)

### Tooltips
- **On hover**: Show exact values, additional context
- **Content**: Value, label, percentage, comparison
- **Timing**: 200ms delay before show, instant hide
- **Positioning**: Near pointer, avoid covering data

### Cross-Filtering
- **Click interaction**: Select data point → filter other charts
- **Visual feedback**: Highlight selected, dim unselected
- **Clear selection**: Easy reset/clear button
- **Performance**: Optimize for large datasets

### Export/Share
- **PDF export**: Maintain layout, embed charts as images
- **Excel export**: Raw data for analysis
- **Image export**: PNG/SVG for presentations
- **Share link**: Snapshot with filters applied

## Dashboard Types

### Operational Dashboard
**Purpose**: Real-time monitoring, immediate action
**Update frequency**: Real-time to hourly
**Audience**: Operations team, support staff
**Key features**: Current status, alerts, live data
**Examples**: Server monitoring, call center metrics, inventory levels

**Typical Metrics**:
- System uptime, error rate, response time
- Active sessions, queue length
- Threshold alerts (red/yellow/green)

### Tactical Dashboard
**Purpose**: Analyze trends, identify patterns
**Update frequency**: Daily to weekly
**Audience**: Managers, analysts
**Key features**: Trends, comparisons, drill-down
**Examples**: Sales performance, marketing campaigns, customer support

**Typical Metrics**:
- Week-over-week trends
- Segment comparisons
- Goal vs. actual
- Conversion funnels

### Strategic Dashboard
**Purpose**: Long-term planning, goal tracking
**Update frequency**: Weekly to monthly
**Audience**: Executives, board members
**Key features**: High-level KPIs, simplified views, mobile-friendly
**Examples**: Company scorecard, OKR tracking, balanced scorecard

**Typical Metrics**:
- Revenue, growth rate
- Market share
- Customer acquisition cost
- Employee satisfaction

## Tools & Technologies

### BI Platforms

**Tableau**
- Strengths: Powerful visualization, large datasets, interactive
- Best for: Complex analysis, data exploration
- Learning curve: Medium to high
- Cost: $70/user/month (Creator)

**Power BI**
- Strengths: Microsoft integration, affordable, good community
- Best for: Microsoft ecosystem, budget-conscious
- Learning curve: Medium
- Cost: $10/user/month (Pro)

**Looker**
- Strengths: Code-based (LookML), version control, embedded analytics
- Best for: Developer-heavy teams, embedded dashboards
- Learning curve: High
- Cost: Custom pricing (expensive)

**Metabase**
- Strengths: Open-source, easy setup, SQL-friendly
- Best for: Startups, simple dashboards, self-hosted
- Learning curve: Low
- Cost: Free (open-source) or $85/month (Cloud Pro)

**Google Data Studio (Looker Studio)**
- Strengths: Free, Google integration, sharing
- Best for: Small teams, Google Workspace users
- Learning curve: Low
- Cost: Free

### Custom Development

**Plotly Dash (Python)**
- Component-based, reactive, Python backend
- Best for: Python data scientists, ML integration

**Streamlit (Python)**
- Simple syntax, rapid prototyping
- Best for: Quick dashboards, demos

**D3.js (JavaScript)**
- Maximum flexibility, custom visualizations
- Best for: Unique requirements, developers

**Chart.js / Highcharts (JavaScript)**
- Pre-built charts, easy integration
- Best for: Web apps, standard charts

## Real-Time vs. Batch Reporting

### Real-Time Dashboards
**Characteristics**:
- Sub-second to minute updates
- Live data streams, WebSockets
- Limited historical data (last 24h)

**Use cases**:
- System monitoring (servers, networks)
- Live event tracking (elections, sports)
- Trading dashboards
- Operations centers

**Technical requirements**:
- Streaming data pipeline (Kafka, Kinesis)
- Real-time database (Redis, InfluxDB)
- WebSocket connections
- Efficient rendering (canvas vs. SVG)

**Challenges**:
- Performance optimization
- Connection reliability
- Data volume management

### Batch Reporting
**Characteristics**:
- Scheduled updates (hourly, daily, weekly)
- Historical analysis
- Complex calculations

**Use cases**:
- Business intelligence
- Financial reporting
- Marketing analytics
- HR dashboards

**Technical requirements**:
- ETL pipeline
- Data warehouse
- Scheduled jobs (cron, Airflow)
- Caching layer

**Advantages**:
- Reliable, consistent
- Complex aggregations
- Lower infrastructure cost

## Mobile Dashboard Design

### Constraints
- **Screen size**: 375px - 428px width (iOS)
- **Touch targets**: Minimum 44x44 points
- **Network**: Slower connections, data limits
- **Context**: Glanceable, quick interactions

### Design Principles

**Simplification**:
- Show fewer metrics (3-5 key KPIs)
- Single column layout
- Vertical scroll (not horizontal)
- Collapsible sections

**Prioritization**:
- Most important metric at top
- Progressive disclosure (details on demand)
- Essential actions only

**Touch-Friendly**:
- Large buttons (48x48 dp minimum)
- Swipe gestures (pull to refresh)
- Avoid hover interactions
- Thumb-friendly navigation (bottom)

**Performance**:
- Lazy loading
- Image optimization
- Minimal chart complexity
- Offline capability

**Responsive Breakpoints**:
```
Mobile:  < 768px  (1 column, stacked)
Tablet:  768-1024px (2 columns)
Desktop: > 1024px (3-4 columns, full grid)
```

## Data Refresh Strategies

### Update Frequencies
- **Real-time**: < 1 second (live events, monitoring)
- **Near real-time**: 1-60 seconds (operational dashboards)
- **Frequent**: 5-15 minutes (sales dashboards)
- **Regular**: Hourly (standard business dashboards)
- **Daily**: Nightly batch (strategic dashboards)
- **Weekly/Monthly**: Scheduled (executive reports)

### Caching Strategies
- **Time-based**: Expire after N minutes
- **Event-based**: Invalidate on data change
- **Hybrid**: Time + event triggers
- **User-specific**: Cache per user/tenant

### Performance Optimization
- **Pre-aggregation**: Calculate metrics in advance
- **Materialized views**: Store computed results
- **Incremental updates**: Update only changed data
- **Query optimization**: Indexes, efficient SQL
- **Data sampling**: For exploratory dashboards

## Best Practices Summary

### Do's
- Start with user needs and goals
- Choose the right chart for data type
- Use color purposefully and accessibly
- Maintain high data-ink ratio
- Provide context (comparisons, targets)
- Enable interactivity (filters, drill-down)
- Test with real users
- Optimize for performance
- Design for mobile
- Document metrics clearly

### Don'ts
- Use pie charts for many categories (>5)
- Create 3D charts (distorts perception)
- Use too many colors (>7)
- Clutter with chartjunk
- Start bar charts at non-zero (misleading)
- Rely on color alone
- Over-complicate interactions
- Show everything at once
- Ignore loading performance
- Forget to test on mobile

### Common Mistakes to Avoid
1. **Wrong chart type**: Pie chart for time series
2. **Too much data**: 50 metrics on one screen
3. **Poor color choices**: Red/green without patterns
4. **No context**: Metric without comparison or target
5. **Misleading scales**: Truncated y-axis
6. **Overcomplicated**: Too many filters, drill-downs
7. **Slow loading**: Large unoptimized images
8. **Not mobile-friendly**: Requires horizontal scroll

## Metrics Documentation Template

```markdown
### [Metric Name]

**Definition**: Clear explanation of what this measures
**Formula**: Exact calculation (e.g., (Revenue - Costs) / Revenue)
**Data Source**: Where the data comes from
**Update Frequency**: How often it refreshes
**Target/Goal**: What success looks like
**Owner**: Who is responsible
**Dashboard Placement**: Where it appears
**Related Metrics**: Connected KPIs
**Notes**: Edge cases, exclusions, context
```

## Implementation Checklist

### Planning Phase
- [ ] Define dashboard purpose and audience
- [ ] Select KPIs aligned with goals
- [ ] Choose appropriate dashboard type
- [ ] Determine update frequency
- [ ] Plan for mobile access

### Design Phase
- [ ] Select chart types for each metric
- [ ] Create layout wireframe
- [ ] Define color scheme (accessible)
- [ ] Plan interactivity features
- [ ] Design for responsiveness

### Development Phase
- [ ] Set up data pipeline
- [ ] Implement visualizations
- [ ] Add filters and interactions
- [ ] Optimize performance
- [ ] Test on multiple devices

### Deployment Phase
- [ ] User acceptance testing
- [ ] Document metrics and usage
- [ ] Train users
- [ ] Monitor performance
- [ ] Gather feedback for iteration

## Resources

### Books
- "The Visual Display of Quantitative Information" - Edward Tufte
- "Information Dashboard Design" - Stephen Few
- "The Truthful Art" - Alberto Cairo
- "Storytelling with Data" - Cole Nussbaumer Knaflic

### Tools
- ColorBrewer: Color schemes for maps and charts
- Coblis: Color blindness simulator
- WebAIM Contrast Checker: WCAG compliance
- Figma/Sketch: Design mockups

### Communities
- Data Visualization Society
- r/dataisbeautiful
- Tableau Community
- Power BI Community
