# Data Analyst Plugin

**Business intelligence and reporting specialist**

## Overview

The Data Analyst plugin provides comprehensive tools for data exploration, reporting, dashboard creation, and KPI tracking. It empowers teams to transform raw data into actionable business insights.

## Agents

### 1. data-explorer (Sonnet)
**Purpose**: Exploratory data analysis with statistical summaries

**Use when**: You need to understand a new dataset, identify patterns, or validate data quality

**Capabilities**:
- Loads CSV, Excel, JSON, SQL databases
- Statistical summaries and distributions
- Correlation analysis
- Outlier detection
- Missing value analysis
- Time series analysis
- Generates comprehensive reports

**Example**:
```
@data-explorer "Analyze sales_data.csv and identify key trends and anomalies"
```

### 2. report-generator (Sonnet, Skill-Aware)
**Purpose**: Creates professional BI reports in multiple formats

**Use when**: You need executive reports, operational dashboards, or analytical documents

**Capabilities**:
- Excel reports with charts and pivot tables
- Word documents with professional formatting
- Markdown reports with visualizations
- Uses xlsx/docx skills for professional quality
- KPI summaries and recommendations

**Example**:
```
@report-generator "Create executive Q4 revenue report with trends and insights"
```

### 3. dashboard-designer (Sonnet, Skill-Aware)
**Purpose**: Builds interactive dashboards for KPI monitoring

**Use when**: You need real-time or interactive business intelligence dashboards

**Capabilities**:
- Streamlit interactive dashboards
- Plotly Dash applications
- Excel dashboards with dynamic charts
- KPI cards with status indicators
- Filtering and drill-down
- Export functionality

**Example**:
```
@dashboard-designer "Create sales dashboard with revenue, orders, and conversion rate tracking"
```

### 4. kpi-tracker (Haiku, Fast)
**Purpose**: Automated KPI monitoring with alerts

**Use when**: You need continuous metric tracking with threshold-based alerts

**Capabilities**:
- Tracks multiple KPIs against targets
- Status indicators (green/yellow/red)
- Anomaly detection
- Automated alerts for threshold violations
- Historical trending
- Period-over-period comparisons

**Example**:
```
@kpi-tracker "Monitor revenue, churn, and conversion rate with weekly reports"
```

## Skills

### data-analysis
Expert patterns for exploratory data analysis:
- Data quality assessment frameworks
- Statistical analysis techniques
- Visualization best practices
- Outlier detection methods
- Correlation analysis
- Time series patterns

### reporting
Professional business intelligence reporting:
- Report structure templates (executive, operational, analytical)
- KPI framework and selection
- Dashboard design principles
- Excel/Word/Markdown best practices
- Visual storytelling techniques

## Templates

### analysis-template.ipynb
Jupyter notebook template for exploratory data analysis:
- Data loading and inspection
- Quality assessment
- Statistical summaries
- Visualizations
- Findings documentation

### dashboard-template.py
Streamlit dashboard template:
- KPI cards layout
- Interactive filters
- Multiple chart types
- Data table with search
- Export functionality

## Installation

### Prerequisites

```bash
# Python packages
pip install pandas numpy matplotlib seaborn scipy scikit-learn openpyxl python-docx streamlit plotly

# Optional: For advanced analysis
pip install statsmodels jupyter missingno
```

### Install Plugin

```bash
# Install to project
cp -r plugins/data-analyst .claude/plugins/

# Verify installation
ls .claude/plugins/data-analyst/agents/
```

## Usage Examples

### Example 1: Complete Data Analysis Workflow

```bash
# 1. Explore data
@data-explorer "Analyze customer_data.csv focusing on purchase behavior and demographics"

# 2. Create dashboard
@dashboard-designer "Build interactive dashboard tracking customer metrics"

# 3. Generate report
@report-generator "Create executive summary report of customer analysis findings"

# 4. Setup monitoring
@kpi-tracker "Track customer acquisition cost, lifetime value, and churn rate"
```

### Example 2: Sales Analysis

```bash
# Explore sales data
@data-explorer "Analyze 2024_sales.csv - identify top products, regional trends, seasonality"

# Create visual dashboard
@dashboard-designer "Create sales dashboard with revenue by region, product, and time"

# Executive report
@report-generator "Generate Q4 sales report for executive team with insights and recommendations"
```

### Example 3: Automated KPI Monitoring

```bash
# Setup continuous monitoring
@kpi-tracker "Monitor these KPIs with daily reports:
- Revenue (target: $1M/month)
- Conversion rate (target: 3%)
- Customer satisfaction (target: 4.5/5)
Alert if any metric drops below 90% of target"
```

## Workflow

```
Raw Data
   ↓
[data-explorer] Exploratory Analysis
   ↓
Analysis Report + Insights
   ↓
[report-generator] Professional Report
   ↓
Executive/Operational Reports
   ↓
[dashboard-designer] Interactive Dashboard
   ↓
Live BI Dashboard
   ↓
[kpi-tracker] Continuous Monitoring
   ↓
Automated Alerts + Reports
```

## Data Sources Supported

- **CSV**: Standard comma-separated files
- **Excel**: .xlsx and .xls files
- **JSON**: Structured JSON data
- **SQL**: PostgreSQL, MySQL, SQLite databases
- **Parquet**: Columnar data format
- **API**: REST APIs returning JSON/CSV

## Output Formats

- **Excel** (.xlsx): Reports, dashboards with charts
- **Word** (.docx): Executive reports, formatted documents
- **Markdown** (.md): Technical reports, documentation
- **Jupyter** (.ipynb): Interactive analysis notebooks
- **Streamlit**: Interactive web dashboards
- **JSON**: Structured data for automation

## Best Practices

### Data Quality First
Always start with data-explorer to:
- Assess quality (missing values, duplicates)
- Understand distributions
- Identify outliers
- Validate assumptions

### Skill-Aware Reporting
For document generation:
- Let agents read skills first (automatic)
- Follow skill patterns for professional quality
- Use appropriate templates
- Validate output quality

### KPI Selection
Choose KPIs that are:
- **Relevant**: Tied to business objectives
- **Measurable**: Quantifiable
- **Actionable**: Can influence
- **Timely**: Updated frequently
- **Simple**: Easy to understand

### Dashboard Design
- Most important metrics at top
- Limit to 4-6 KPIs per view
- Use status indicators (✅⚠️🚨)
- Include filters for drill-down
- Show period comparisons

## Troubleshooting

### "Module not found" errors
```bash
pip install pandas numpy matplotlib seaborn scipy
```

### Large dataset performance issues
- Sample data for initial EDA: `df.sample(10000)`
- Use chunking: `pd.read_csv('file.csv', chunksize=10000)`
- Consider Dask for very large datasets

### Database connection issues
Provide connection string:
```python
# PostgreSQL
"postgresql://user:password@localhost:5432/database"

# MySQL
"mysql://user:password@localhost:3306/database"

# SQLite
"sqlite:///path/to/database.db"
```

### Streamlit dashboard not loading
```bash
# Check Streamlit is installed
pip install streamlit

# Run with full path
streamlit run /full/path/to/dashboard.py

# Check port availability (default 8501)
lsof -i :8501
```

## Cost Optimization

- **data-explorer** (Sonnet): ~$0.05 per analysis
- **report-generator** (Sonnet): ~$0.10 per report
- **dashboard-designer** (Sonnet): ~$0.08 per dashboard
- **kpi-tracker** (Haiku): ~$0.01 per monitoring run

**Total**: ~$0.24 for complete analysis workflow

**Savings**: kpi-tracker uses Haiku (10x cheaper) for routine monitoring

## Contributing

To extend this plugin:

1. **Add new agent**: Create .md file in `agents/`
2. **Add skill**: Create SKILL.md in `skills/[name]/`
3. **Add template**: Create template in `templates/`
4. **Update README**: Document new capabilities

## License

Part of the Puerto Plugin System

## Support

For issues or questions:
- Check skills documentation
- Review templates for examples
- Consult troubleshooting section

---

**Version**: 1.0.0
**Last Updated**: January 2025
**Category**: Data & Analytics
