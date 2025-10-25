# Data Engineer Plugin

A comprehensive data engineering plugin providing specialized agents for ETL pipeline development, data quality validation, pipeline orchestration, and data warehouse design.

## Overview

The Data Engineer plugin equips Claude with expert capabilities in:
- ETL pipeline development (extract, transform, load)
- Data quality validation and profiling
- Pipeline orchestration with Airflow/Prefect
- Data warehouse dimensional modeling
- Production-ready data infrastructure

## Agents

### 1. ETL Builder (`etl-builder`)
**Model:** Sonnet | **Type:** Read-Write

Creates robust ETL pipelines for extracting, transforming, and loading data.

**Capabilities:**
- Design data extraction strategies (full, incremental, CDC)
- Implement data transformations and cleansing
- Create efficient loading mechanisms (bulk, upsert)
- Handle errors and implement retry logic
- Track data lineage and watermarks

**Usage:**
```
Ask etl-builder: Create an ETL pipeline to load customer data from PostgreSQL to Snowflake with incremental extraction based on updated_at timestamp
```

**Best For:**
- Building new data pipelines
- Migrating data between systems
- Implementing incremental load strategies
- Creating data integration workflows

### 2. Data Quality Checker (`data-quality-checker`)
**Model:** Sonnet | **Type:** Read-Only

Validates data quality, performs profiling, and detects anomalies.

**Capabilities:**
- Validate data completeness and accuracy
- Profile datasets with statistical analysis
- Detect anomalies and outliers
- Check referential integrity
- Generate quality scorecards and reports

**Usage:**
```
Ask data-quality-checker: Validate the quality of the customer table and generate a comprehensive quality report with recommendations
```

**Best For:**
- Data quality assessment
- Pre/post-load validation
- Anomaly detection
- Quality monitoring and reporting

**Note:** This is a READ-ONLY agent for security. It reports issues but does not modify data.

### 3. Pipeline Orchestrator (`pipeline-orchestrator`)
**Model:** Sonnet | **Type:** Read-Write

Creates and manages workflow orchestration using Airflow, Prefect, and other tools.

**Capabilities:**
- Design DAGs with proper dependencies
- Configure scheduling and triggers
- Implement monitoring and alerting
- Handle errors with retry strategies
- Create event-driven workflows

**Usage:**
```
Ask pipeline-orchestrator: Create an Airflow DAG to orchestrate the customer ETL pipeline with quality checks and error handling
```

**Best For:**
- Scheduling data pipelines
- Creating complex workflows
- Implementing monitoring and alerts
- Managing pipeline dependencies

### 4. Warehouse Architect (`warehouse-architect`)
**Model:** Sonnet | **Type:** Read-Write

Designs data warehouses with dimensional models and star/snowflake schemas.

**Capabilities:**
- Design star and snowflake schemas
- Implement slowly changing dimensions (SCD Types 0-6)
- Create fact tables (transaction, snapshot, accumulating)
- Optimize for cloud warehouses (Snowflake, BigQuery, Redshift)
- Plan incremental loading strategies

**Usage:**
```
Ask warehouse-architect: Design a data warehouse schema for e-commerce analytics with sales facts and customer, product, and date dimensions using SCD Type 2
```

**Best For:**
- Designing new data warehouses
- Dimensional modeling
- Schema optimization
- Data mart creation

## Skills

All agents have access to specialized skills that provide in-depth knowledge:

### etl-patterns
Comprehensive ETL design patterns including:
- Extraction strategies (full, incremental, CDC, partition-based, API)
- Transformation patterns (cleansing, enrichment, aggregation, SCD)
- Loading patterns (bulk insert, upsert, staging)
- Error handling and retry mechanisms
- Performance optimization

### data-quality
Data validation and quality monitoring techniques:
- Completeness checks (nulls, required fields)
- Accuracy checks (formats, ranges, types)
- Consistency checks (referential integrity, cross-field)
- Uniqueness checks (duplicates, primary keys)
- Timeliness checks (data freshness)
- Anomaly detection methods

### orchestration
Workflow orchestration best practices:
- DAG design patterns (sequential, parallel, branching)
- Scheduling strategies (time-based, event-driven)
- Error handling and retry logic
- Monitoring and alerting
- Resource management
- Airflow and Prefect patterns

### warehouse-design
Dimensional modeling expertise:
- Star vs. snowflake schemas
- Fact table types (transaction, snapshot, accumulating)
- Dimension table patterns (SCD Types 0-6)
- Junk dimensions and role-playing dimensions
- Cloud warehouse optimizations
- Schema evolution strategies

## Templates

Production-ready templates to accelerate development:

### etl-pipeline-template.py
Complete ETL pipeline with:
- Database connections (source and target)
- Watermark-based incremental extraction
- Data transformation pipeline
- Staging and loading with validation
- Comprehensive error handling and logging
- Execution metrics tracking

**Features:**
- Retry with exponential backoff
- Configurable batch processing
- Connection pooling
- Watermark management
- Quality validation checkpoints

### airflow-dag-template.py
Production Airflow DAG with:
- Connection validation
- Source data checks
- Extract, transform, load tasks
- Data quality validation
- Cleanup operations
- Comprehensive error handling and callbacks

**Features:**
- Task dependencies and orchestration
- XCom for data passing
- SLA monitoring
- Email alerts on failures
- Retry strategies
- Detailed documentation

### data-quality-checks-template.py
Comprehensive validation suite with:
- Completeness checks (nulls, record counts)
- Accuracy checks (types, formats, ranges)
- Consistency checks (referential integrity, cross-field)
- Uniqueness checks (duplicates, primary keys)
- Timeliness checks (data freshness)
- Anomaly detection (outliers, distribution changes)
- Quality scoring and reporting

**Features:**
- Modular validation functions
- Quality scorecard generation
- Detailed reporting
- Anomaly detection algorithms
- Dataset profiling

### warehouse-schema-template.sql
Complete star schema with:
- Dimension tables (date, customer, product, store, promotion)
- Fact tables (sales, inventory snapshot, customer activity)
- SCD Type 2 implementation
- Indexes and constraints
- Helper tables (watermarks, quality metrics)
- Sample queries and views

**Features:**
- Multiple dimension types (Type 0, 1, 2)
- Multiple fact types (transaction, snapshot, accumulating)
- Junk dimensions
- Role-playing dimensions
- Referential integrity
- Query optimization

## Usage Examples

### Example 1: Build Complete ETL Pipeline

```
1. Ask warehouse-architect: Design a customer data warehouse schema with Type 2 SCD

2. Ask etl-builder: Create an ETL pipeline to extract customers from MySQL, transform the data (cleanse emails, standardize addresses), and load to the warehouse schema with SCD Type 2 logic

3. Ask data-quality-checker: Validate the loaded customer data for completeness, accuracy, and data quality issues

4. Ask pipeline-orchestrator: Create an Airflow DAG to run this ETL daily at 2 AM with quality checks and alerts on failures
```

### Example 2: Data Quality Assessment

```
Ask data-quality-checker: Analyze the sales_transactions table and provide:
- Completeness score (null values in required fields)
- Accuracy validation (email formats, date ranges)
- Duplicate detection on transaction_id
- Outlier detection on order_amount
- Data freshness check on transaction_date
- Overall quality score and recommendations
```

### Example 3: Complex Orchestration

```
Ask pipeline-orchestrator: Create an Airflow DAG that:
1. Extracts data from 3 sources in parallel (MySQL, PostgreSQL, API)
2. Runs quality checks on each extraction
3. Merges the data if all checks pass
4. Transforms and loads to warehouse
5. Sends Slack alert on completion
6. Runs daily at 2 AM with 3 retries on failure
```

### Example 4: Warehouse Modernization

```
Ask warehouse-architect: Design a modern data warehouse schema for a retail business including:
- Sales fact table (transaction grain)
- Inventory snapshot fact (daily grain)
- Customer dimension (SCD Type 2 for address changes)
- Product dimension (SCD Type 2 for price changes)
- Date dimension (pre-populated calendar)
- Store dimension (Type 1)
- Optimize for Snowflake with clustering and partitioning
```

## Architecture Patterns

### Pattern 1: Medallion Architecture (Bronze-Silver-Gold)

**Bronze Layer** (Raw Data)
- Use etl-builder to ingest raw data as-is
- Minimal transformation, preserve source structure
- Append-only for auditability

**Silver Layer** (Cleaned Data)
- Use etl-builder for cleansing and standardization
- Use data-quality-checker for validation
- Deduplicate and enforce schema

**Gold Layer** (Business-Ready)
- Use warehouse-architect to design dimensional models
- Aggregate and denormalize for analytics
- Optimize for query performance

### Pattern 2: Lambda Architecture (Batch + Stream)

**Batch Layer**
- Use etl-builder for daily batch processing
- Use pipeline-orchestrator for scheduling
- Historical data processing

**Speed Layer**
- Use etl-builder with streaming connectors
- Real-time/near-real-time processing
- Handle late-arriving data

**Serving Layer**
- Use warehouse-architect for analytics schemas
- Merge batch and streaming results

### Pattern 3: Data Vault + Dimensional

**Raw Vault** (Auditability)
- Hubs, Links, Satellites for source tracking
- Use warehouse-architect for vault design

**Dimensional Marts** (Analytics)
- Star schemas for business users
- Use warehouse-architect for Kimball design
- Derived from vault

## Best Practices

### ETL Development
1. Always use incremental extraction when possible
2. Implement idempotent operations (safe to retry)
3. Use staging tables for validation before production load
4. Track watermarks for incremental processing
5. Log data lineage and transformation steps
6. Validate data at each stage (extract, transform, load)

### Data Quality
1. Define quality thresholds upfront
2. Automate quality checks in pipelines
3. Track quality metrics over time
4. Alert on quality degradation
5. Document validation rules clearly
6. Test with production-like data

### Orchestration
1. Keep DAGs simple and focused
2. Design for idempotency
3. Implement proper error handling and retries
4. Monitor execution metrics and SLAs
5. Use meaningful task and DAG IDs
6. Document dependencies and purpose

### Warehouse Design
1. Define grain before designing fact tables
2. Use surrogate keys for all dimensions
3. Implement SCD Type 2 for tracking important changes
4. Denormalize dimensions for query performance
5. Partition large fact tables by date
6. Create indexes on foreign keys

## Configuration

### Environment Variables

For ETL pipelines:
```bash
# Source database
SOURCE_DB_HOST=localhost
SOURCE_DB_PORT=5432
SOURCE_DB_NAME=source_db
SOURCE_DB_USER=user
SOURCE_DB_PASSWORD=password

# Target database
TARGET_DB_HOST=warehouse.example.com
TARGET_DB_NAME=warehouse
TARGET_DB_USER=etl_user
TARGET_DB_PASSWORD=password

# Pipeline settings
BATCH_SIZE=10000
MAX_RETRIES=3
```

### Airflow Connections

```bash
# Add connections via Airflow UI or CLI
airflow connections add postgres_source \
    --conn-type postgres \
    --conn-host localhost \
    --conn-schema source_db \
    --conn-login user \
    --conn-password password

airflow connections add snowflake_target \
    --conn-type snowflake \
    --conn-host account.snowflakecomputing.com \
    --conn-schema public \
    --conn-login user \
    --conn-password password
```

## Testing

### Testing ETL Pipelines
```python
# Use small sample datasets
# Test with edge cases (nulls, duplicates, invalid formats)
# Validate row counts and data quality
# Test error handling and recovery
```

### Testing Data Quality
```python
# Run checks on known good/bad datasets
# Validate thresholds are appropriate
# Test anomaly detection sensitivity
# Verify report generation
```

### Testing DAGs
```python
# Test DAG structure (no cycles)
# Test task logic independently
# Test with mock data
# Validate error handling and retries
```

## Troubleshooting

### Common Issues

**Pipeline fails with connection timeout**
- Check network connectivity
- Verify credentials
- Increase connection timeout settings
- Check firewall rules

**Data quality checks failing**
- Review validation thresholds
- Check for schema changes in source
- Verify data distributions are as expected
- Check for new data patterns

**DAG tasks hanging**
- Check for long-running queries
- Verify task timeouts are set
- Check resource availability (CPU, memory)
- Review logs for blocking operations

**SCD Type 2 creating duplicate current records**
- Verify effective_date/expiration_date logic
- Check is_current flag updates
- Ensure proper transaction handling
- Review merge/upsert logic

## Integration with Other Plugins

- **Database Architect**: Get schema designs for target warehouses
- **Backend Architect**: Coordinate data flow in microservices
- **API Developer**: Create APIs for data access
- **DevOps Engineer**: Deploy and monitor data pipelines

## License

This plugin is part of the Puerto project.

## Support

For issues or questions, please refer to the Puerto documentation or create an issue in the repository.
