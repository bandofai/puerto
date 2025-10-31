# ETL Patterns Skill

This skill provides comprehensive patterns and best practices for Extract, Transform, Load (ETL) pipeline development.

## Extraction Patterns

### 1. Full Extraction
Extract complete dataset from source (initial load or small tables).

```python
def full_extraction(connection, table_name):
    """Extract all records from source table."""
    query = f"SELECT * FROM {table_name}"
    return pd.read_sql(query, connection)
```

**Use when:**
- Initial data load
- Small reference tables
- No reliable change tracking in source

### 2. Incremental Extraction (Timestamp-Based)
Extract only new/modified records since last run.

```python
def incremental_extraction(connection, table_name, last_run_timestamp):
    """Extract records modified since last run."""
    query = f"""
        SELECT * FROM {table_name}
        WHERE updated_at > %s
        ORDER BY updated_at
    """
    return pd.read_sql(query, connection, params=[last_run_timestamp])
```

**Use when:**
- Source has reliable timestamp columns (created_at, updated_at)
- Large tables with frequent updates
- Need to minimize data transfer

### 3. Change Data Capture (CDC)
Extract changes using database transaction logs or CDC tools.

```python
def cdc_extraction(connection, table_name, last_lsn):
    """Extract changes using CDC."""
    query = f"""
        SELECT * FROM cdc.{table_name}_CT
        WHERE __$start_lsn > %s
    """
    return pd.read_sql(query, connection, params=[last_lsn])
```

**Use when:**
- Need to capture deletes
- High-frequency changes
- Database supports CDC (SQL Server, PostgreSQL, Oracle)

### 4. Partition-Based Extraction
Extract data in partitions for parallel processing.

```python
def partition_extraction(connection, table_name, partition_key, partition_value):
    """Extract data for specific partition."""
    query = f"""
        SELECT * FROM {table_name}
        WHERE {partition_key} = %s
    """
    return pd.read_sql(query, connection, params=[partition_value])
```

**Use when:**
- Very large tables
- Data is naturally partitioned (by date, region, etc.)
- Need parallel processing

### 5. API Extraction
Extract data from REST APIs with pagination and rate limiting.

```python
import time
import requests

def api_extraction(base_url, endpoint, params=None, rate_limit=100):
    """Extract data from API with pagination and rate limiting."""
    all_data = []
    page = 1

    while True:
        # Rate limiting
        time.sleep(1 / rate_limit)

        # API request
        response = requests.get(
            f"{base_url}/{endpoint}",
            params={**(params or {}), 'page': page}
        )
        response.raise_for_status()

        data = response.json()
        if not data:
            break

        all_data.extend(data)
        page += 1

    return all_data
```

## Transformation Patterns

### 1. Data Cleansing
Remove inconsistencies, duplicates, and fix data quality issues.

```python
def cleanse_data(df):
    """Apply data cleansing transformations."""
    # Remove duplicates
    df = df.drop_duplicates(subset=['customer_id'], keep='last')

    # Handle nulls
    df['email'] = df['email'].fillna('unknown@example.com')
    df['phone'] = df['phone'].fillna('')

    # Trim whitespace
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()

    # Standardize casing
    df['email'] = df['email'].str.lower()
    df['country'] = df['country'].str.upper()

    return df
```

### 2. Data Type Conversion
Ensure correct data types for target schema.

```python
def convert_data_types(df):
    """Convert data types to match target schema."""
    type_mappings = {
        'customer_id': 'int64',
        'created_at': 'datetime64[ns]',
        'total_amount': 'float64',
        'is_active': 'bool',
        'zip_code': 'str'
    }

    for col, dtype in type_mappings.items():
        if col in df.columns:
            df[col] = df[col].astype(dtype)

    return df
```

### 3. Data Enrichment
Add calculated fields and derived attributes.

```python
def enrich_data(df):
    """Add calculated and derived fields."""
    # Calculate age from birthdate
    df['age'] = (pd.Timestamp.now() - df['birthdate']).dt.days // 365

    # Derive customer segment
    df['segment'] = pd.cut(
        df['total_purchases'],
        bins=[0, 1000, 5000, float('inf')],
        labels=['bronze', 'silver', 'gold']
    )

    # Generate full name
    df['full_name'] = df['first_name'] + ' ' + df['last_name']

    # Hash sensitive data
    df['email_hash'] = df['email'].apply(lambda x: hashlib.sha256(x.encode()).hexdigest())

    return df
```

### 4. Data Aggregation
Summarize data for analytical purposes.

```python
def aggregate_data(df, group_by_cols, agg_config):
    """Aggregate data based on configuration."""
    return df.groupby(group_by_cols).agg(agg_config).reset_index()

# Example usage
sales_summary = aggregate_data(
    df,
    group_by_cols=['customer_id', 'product_id'],
    agg_config={
        'order_id': 'count',
        'total_amount': ['sum', 'mean'],
        'quantity': 'sum'
    }
)
```

### 5. Slowly Changing Dimension (SCD) Type 2
Track historical changes in dimension tables.

```python
def apply_scd_type2(new_df, existing_df, natural_key, compare_cols):
    """Apply SCD Type 2 logic to track historical changes."""
    # Merge new and existing data
    merged = new_df.merge(
        existing_df[existing_df['is_current'] == True],
        on=natural_key,
        how='left',
        suffixes=('_new', '_old')
    )

    # Identify changes
    changed_mask = False
    for col in compare_cols:
        changed_mask |= (merged[f'{col}_new'] != merged[f'{col}_old'])

    # Expire old records
    expired_records = existing_df[
        (existing_df[natural_key].isin(merged[changed_mask][natural_key])) &
        (existing_df['is_current'] == True)
    ].copy()
    expired_records['is_current'] = False
    expired_records['end_date'] = pd.Timestamp.now()

    # Create new records for changes
    new_records = new_df[new_df[natural_key].isin(merged[changed_mask][natural_key])].copy()
    new_records['is_current'] = True
    new_records['start_date'] = pd.Timestamp.now()
    new_records['end_date'] = pd.Timestamp('2999-12-31')

    # Combine results
    return pd.concat([expired_records, new_records], ignore_index=True)
```

## Loading Patterns

### 1. Bulk Insert
Fast loading for new data.

```python
def bulk_insert(df, connection, table_name, batch_size=10000):
    """Bulk insert data into target table."""
    from sqlalchemy import create_engine

    engine = create_engine(connection)
    df.to_sql(
        table_name,
        engine,
        if_exists='append',
        index=False,
        method='multi',
        chunksize=batch_size
    )
```

### 2. Upsert (Merge)
Insert new records and update existing ones.

```python
def upsert_data(df, connection, table_name, key_columns):
    """Upsert data using staging table and MERGE."""
    staging_table = f"{table_name}_staging"

    # Load to staging
    df.to_sql(staging_table, connection, if_exists='replace', index=False)

    # Build MERGE statement
    key_join = " AND ".join([f"target.{k} = staging.{k}" for k in key_columns])
    update_set = ", ".join([
        f"{col} = staging.{col}"
        for col in df.columns if col not in key_columns
    ])
    insert_cols = ", ".join(df.columns)
    insert_vals = ", ".join([f"staging.{col}" for col in df.columns])

    merge_sql = f"""
        MERGE INTO {table_name} AS target
        USING {staging_table} AS staging
        ON {key_join}
        WHEN MATCHED THEN
            UPDATE SET {update_set}
        WHEN NOT MATCHED THEN
            INSERT ({insert_cols})
            VALUES ({insert_vals})
    """

    connection.execute(merge_sql)
```

### 3. Staging to Production
Load data through staging tables for validation.

```python
def stage_and_load(df, connection, table_name):
    """Load via staging with validation."""
    staging_table = f"{table_name}_staging"

    # Load to staging
    df.to_sql(staging_table, connection, if_exists='replace', index=False)

    # Validate staging data
    validation_sql = f"""
        SELECT COUNT(*) as errors
        FROM {staging_table}
        WHERE email IS NULL OR email NOT LIKE '%@%'
    """
    errors = pd.read_sql(validation_sql, connection).iloc[0]['errors']

    if errors > 0:
        raise ValueError(f"Validation failed: {errors} records with invalid emails")

    # Swap tables (atomic operation)
    connection.execute(f"DROP TABLE IF EXISTS {table_name}_old")
    connection.execute(f"ALTER TABLE {table_name} RENAME TO {table_name}_old")
    connection.execute(f"ALTER TABLE {staging_table} RENAME TO {table_name}")
```

### 4. Incremental Load with Watermark
Track high watermark for incremental processing.

```python
def incremental_load(df, connection, table_name, watermark_col):
    """Load data incrementally with watermark tracking."""
    # Load new data
    df.to_sql(table_name, connection, if_exists='append', index=False)

    # Update watermark
    max_watermark = df[watermark_col].max()
    watermark_sql = f"""
        INSERT INTO etl_watermarks (table_name, watermark_value, updated_at)
        VALUES ('{table_name}', '{max_watermark}', CURRENT_TIMESTAMP)
        ON CONFLICT (table_name)
        DO UPDATE SET
            watermark_value = EXCLUDED.watermark_value,
            updated_at = EXCLUDED.updated_at
    """
    connection.execute(watermark_sql)
```

## Error Handling Patterns

### 1. Retry with Exponential Backoff

```python
import time
from functools import wraps

def retry_with_backoff(max_retries=3, base_delay=1, max_delay=60):
    """Decorator for retry with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise

                    delay = min(base_delay * (2 ** attempt), max_delay)
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator
```

### 2. Dead Letter Queue for Failed Records

```python
def process_with_dlq(df, process_func, connection, dlq_table):
    """Process records with dead letter queue for failures."""
    success_records = []
    failed_records = []

    for idx, row in df.iterrows():
        try:
            processed = process_func(row)
            success_records.append(processed)
        except Exception as e:
            failed_record = row.to_dict()
            failed_record['error_message'] = str(e)
            failed_record['failed_at'] = pd.Timestamp.now()
            failed_records.append(failed_record)

    # Save failed records for manual review
    if failed_records:
        pd.DataFrame(failed_records).to_sql(
            dlq_table, connection, if_exists='append', index=False
        )

    return pd.DataFrame(success_records)
```

## Performance Optimization

### 1. Parallel Processing

```python
from multiprocessing import Pool

def parallel_extract(partitions, extract_func):
    """Extract data in parallel using multiprocessing."""
    with Pool() as pool:
        results = pool.map(extract_func, partitions)
    return pd.concat(results, ignore_index=True)
```

### 2. Batch Processing

```python
def batch_process(df, process_func, batch_size=1000):
    """Process data in batches to manage memory."""
    results = []
    for start_idx in range(0, len(df), batch_size):
        batch = df.iloc[start_idx:start_idx + batch_size]
        processed = process_func(batch)
        results.append(processed)
    return pd.concat(results, ignore_index=True)
```

## Best Practices

1. **Idempotency**: Design pipelines to produce same results when run multiple times
2. **Data Lineage**: Track source, transformations, and destination
3. **Logging**: Log start, end, row counts, and errors at each stage
4. **Validation**: Validate data at extraction, transformation, and loading stages
5. **Configuration**: Externalize connection strings, parameters, and business rules
6. **Monitoring**: Track execution time, data volumes, and error rates
7. **Checkpointing**: Save progress for long-running pipelines
8. **Testing**: Unit test transformations, integration test full pipeline

## Common Anti-Patterns to Avoid

1. **No error handling**: Always expect failures and handle gracefully
2. **Loading directly to production**: Use staging tables
3. **No logging**: Essential for debugging production issues
4. **Hardcoded values**: Use configuration files
5. **No data validation**: Validate at each stage
6. **Processing entire dataset**: Use incremental extraction when possible
7. **No monitoring**: Track pipeline health and performance
8. **Ignoring data types**: Explicit type conversion prevents errors
