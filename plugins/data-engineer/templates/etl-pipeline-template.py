"""
ETL Pipeline Template
Complete production-ready ETL pipeline with error handling, logging, and monitoring.
"""

import os
import sys
import logging
import time
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
import pandas as pd
from sqlalchemy import create_engine
from functools import wraps

# ============================================
# CONFIGURATION
# ============================================

CONFIG = {
    'source': {
        'type': 'postgresql',
        'host': os.getenv('SOURCE_DB_HOST', 'localhost'),
        'port': int(os.getenv('SOURCE_DB_PORT', 5432)),
        'database': os.getenv('SOURCE_DB_NAME', 'source_db'),
        'username': os.getenv('SOURCE_DB_USER', 'user'),
        'password': os.getenv('SOURCE_DB_PASSWORD', 'password'),
    },
    'target': {
        'type': 'snowflake',
        'account': os.getenv('SNOWFLAKE_ACCOUNT', 'account'),
        'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE', 'COMPUTE_WH'),
        'database': os.getenv('SNOWFLAKE_DATABASE', 'target_db'),
        'schema': os.getenv('SNOWFLAKE_SCHEMA', 'public'),
        'username': os.getenv('SNOWFLAKE_USER', 'user'),
        'password': os.getenv('SNOWFLAKE_PASSWORD', 'password'),
    },
    'pipeline': {
        'name': 'customer_etl',
        'source_table': 'customers',
        'target_table': 'customers',
        'batch_size': 10000,
        'watermark_column': 'updated_at',
    }
}

# ============================================
# LOGGING SETUP
# ============================================

def setup_logging() -> logging.Logger:
    """Configure logging for the pipeline."""
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler(f"logs/{CONFIG['pipeline']['name']}_{datetime.now().strftime('%Y%m%d')}.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(CONFIG['pipeline']['name'])

logger = setup_logging()

# ============================================
# DECORATORS
# ============================================

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
                        logger.error(f"Max retries ({max_retries}) reached for {func.__name__}")
                        raise

                    delay = min(base_delay * (2 ** attempt), max_delay)
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

def log_execution_time(func):
    """Decorator to log function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"Starting {func.__name__}...")

        try:
            result = func(*args, **kwargs)
            duration = time.time() - start_time
            logger.info(f"Completed {func.__name__} in {duration:.2f}s")
            return result
        except Exception as e:
            duration = time.time() - start_time
            logger.error(f"Failed {func.__name__} after {duration:.2f}s: {e}")
            raise
    return wrapper

# ============================================
# DATABASE CONNECTIONS
# ============================================

@retry_with_backoff(max_retries=3)
def get_source_connection():
    """Create connection to source database."""
    config = CONFIG['source']
    connection_string = (
        f"postgresql://{config['username']}:{config['password']}"
        f"@{config['host']}:{config['port']}/{config['database']}"
    )
    engine = create_engine(connection_string)
    logger.info("Source database connection established")
    return engine

@retry_with_backoff(max_retries=3)
def get_target_connection():
    """Create connection to target database."""
    config = CONFIG['target']
    connection_string = (
        f"snowflake://{config['username']}:{config['password']}"
        f"@{config['account']}/{config['database']}/{config['schema']}"
        f"?warehouse={config['warehouse']}"
    )
    engine = create_engine(connection_string)
    logger.info("Target database connection established")
    return engine

# ============================================
# WATERMARK MANAGEMENT
# ============================================

def get_last_watermark(connection) -> Optional[datetime]:
    """Retrieve the last successful extraction timestamp."""
    try:
        query = """
            SELECT MAX(watermark_value) as last_watermark
            FROM etl_watermarks
            WHERE pipeline_name = %(pipeline_name)s
        """
        result = pd.read_sql(query, connection, params={'pipeline_name': CONFIG['pipeline']['name']})
        watermark = result.iloc[0]['last_watermark']

        if pd.notna(watermark):
            logger.info(f"Last watermark: {watermark}")
            return watermark
        else:
            logger.info("No previous watermark found, performing full extraction")
            return None
    except Exception as e:
        logger.warning(f"Could not retrieve watermark: {e}. Performing full extraction.")
        return None

def update_watermark(connection, watermark_value: datetime):
    """Update the watermark after successful load."""
    query = """
        INSERT INTO etl_watermarks (pipeline_name, watermark_value, updated_at)
        VALUES (%(pipeline_name)s, %(watermark_value)s, %(updated_at)s)
        ON CONFLICT (pipeline_name)
        DO UPDATE SET
            watermark_value = EXCLUDED.watermark_value,
            updated_at = EXCLUDED.updated_at
    """
    pd.io.sql.execute(
        query,
        connection,
        params={
            'pipeline_name': CONFIG['pipeline']['name'],
            'watermark_value': watermark_value,
            'updated_at': datetime.now()
        }
    )
    logger.info(f"Watermark updated to: {watermark_value}")

# ============================================
# EXTRACTION
# ============================================

@log_execution_time
@retry_with_backoff(max_retries=3)
def extract_data(source_connection, last_watermark: Optional[datetime]) -> pd.DataFrame:
    """Extract data from source database."""
    table_name = CONFIG['pipeline']['source_table']
    watermark_column = CONFIG['pipeline']['watermark_column']

    if last_watermark:
        # Incremental extraction
        query = f"""
            SELECT *
            FROM {table_name}
            WHERE {watermark_column} > %(last_watermark)s
            ORDER BY {watermark_column}
        """
        params = {'last_watermark': last_watermark}
        logger.info(f"Performing incremental extraction since {last_watermark}")
    else:
        # Full extraction
        query = f"SELECT * FROM {table_name}"
        params = None
        logger.info("Performing full extraction")

    df = pd.read_sql(query, source_connection, params=params)
    logger.info(f"Extracted {len(df)} records from {table_name}")

    return df

# ============================================
# TRANSFORMATION
# ============================================

@log_execution_time
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply transformations to extracted data."""
    if df.empty:
        logger.info("No data to transform")
        return df

    logger.info(f"Starting transformation on {len(df)} records")
    original_count = len(df)

    # 1. Remove duplicates
    df = df.drop_duplicates(subset=['customer_id'], keep='last')
    logger.info(f"Removed {original_count - len(df)} duplicate records")

    # 2. Handle nulls
    df['email'] = df['email'].fillna('unknown@example.com')
    df['phone'] = df['phone'].fillna('')

    # 3. Data cleansing
    # Trim whitespace
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()

    # Standardize casing
    df['email'] = df['email'].str.lower()
    df['country'] = df['country'].str.upper()

    # 4. Data type conversions
    df['customer_id'] = df['customer_id'].astype('int64')
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['updated_at'] = pd.to_datetime(df['updated_at'])

    # 5. Data enrichment
    # Calculate customer age if birthdate exists
    if 'birthdate' in df.columns:
        df['age'] = (pd.Timestamp.now() - pd.to_datetime(df['birthdate'])).dt.days // 365

    # Derive full name
    if 'first_name' in df.columns and 'last_name' in df.columns:
        df['full_name'] = df['first_name'] + ' ' + df['last_name']

    # 6. Validation
    # Validate email format
    invalid_emails = ~df['email'].str.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', na=False)
    if invalid_emails.any():
        logger.warning(f"Found {invalid_emails.sum()} records with invalid email format")
        # Option: filter out or fix
        # df = df[~invalid_emails]

    logger.info(f"Transformation completed. {len(df)} records ready for loading")
    return df

# ============================================
# LOADING
# ============================================

@log_execution_time
@retry_with_backoff(max_retries=3)
def load_data(df: pd.DataFrame, target_connection) -> Dict[str, Any]:
    """Load transformed data to target database."""
    if df.empty:
        logger.info("No data to load")
        return {'rows_loaded': 0}

    table_name = CONFIG['pipeline']['target_table']
    staging_table = f"{table_name}_staging"
    batch_size = CONFIG['pipeline']['batch_size']

    logger.info(f"Loading {len(df)} records to {table_name}")

    try:
        # 1. Load to staging table
        df.to_sql(
            staging_table,
            target_connection,
            if_exists='replace',
            index=False,
            method='multi',
            chunksize=batch_size
        )
        logger.info(f"Loaded data to staging table: {staging_table}")

        # 2. Validate staging data
        validation_query = f"""
            SELECT
                COUNT(*) as total_rows,
                COUNT(CASE WHEN email IS NULL OR email = '' THEN 1 END) as null_emails
            FROM {staging_table}
        """
        validation_result = pd.read_sql(validation_query, target_connection)
        logger.info(f"Staging validation: {validation_result.to_dict('records')[0]}")

        # 3. Merge staging to production (upsert)
        merge_query = f"""
            MERGE INTO {table_name} AS target
            USING {staging_table} AS staging
            ON target.customer_id = staging.customer_id
            WHEN MATCHED THEN
                UPDATE SET
                    email = staging.email,
                    phone = staging.phone,
                    full_name = staging.full_name,
                    updated_at = staging.updated_at
            WHEN NOT MATCHED THEN
                INSERT (customer_id, email, phone, full_name, created_at, updated_at)
                VALUES (staging.customer_id, staging.email, staging.phone,
                        staging.full_name, staging.created_at, staging.updated_at)
        """
        target_connection.execute(merge_query)
        logger.info(f"Merged {len(df)} records into {table_name}")

        return {
            'rows_loaded': len(df),
            'max_watermark': df[CONFIG['pipeline']['watermark_column']].max()
        }

    except Exception as e:
        logger.error(f"Load failed: {e}")
        raise

# ============================================
# PIPELINE METRICS
# ============================================

def log_pipeline_metrics(metrics: Dict[str, Any]):
    """Log pipeline execution metrics."""
    logger.info("=" * 50)
    logger.info("PIPELINE METRICS")
    logger.info("=" * 50)
    for key, value in metrics.items():
        logger.info(f"{key}: {value}")
    logger.info("=" * 50)

# ============================================
# MAIN PIPELINE
# ============================================

def run_pipeline():
    """Execute the complete ETL pipeline."""
    pipeline_start = time.time()
    metrics = {
        'pipeline_name': CONFIG['pipeline']['name'],
        'start_time': datetime.now(),
        'status': 'FAILED',
        'rows_extracted': 0,
        'rows_transformed': 0,
        'rows_loaded': 0,
        'duration_seconds': 0,
        'error_message': None
    }

    source_conn = None
    target_conn = None

    try:
        logger.info("=" * 50)
        logger.info(f"Starting ETL Pipeline: {CONFIG['pipeline']['name']}")
        logger.info("=" * 50)

        # 1. Establish connections
        source_conn = get_source_connection()
        target_conn = get_target_connection()

        # 2. Get last watermark
        last_watermark = get_last_watermark(target_conn)

        # 3. Extract
        df_extracted = extract_data(source_conn, last_watermark)
        metrics['rows_extracted'] = len(df_extracted)

        if df_extracted.empty:
            logger.info("No new data to process")
            metrics['status'] = 'SUCCESS'
            return metrics

        # 4. Transform
        df_transformed = transform_data(df_extracted)
        metrics['rows_transformed'] = len(df_transformed)

        # 5. Load
        load_result = load_data(df_transformed, target_conn)
        metrics['rows_loaded'] = load_result['rows_loaded']

        # 6. Update watermark
        if load_result.get('max_watermark'):
            update_watermark(target_conn, load_result['max_watermark'])

        # 7. Success
        metrics['status'] = 'SUCCESS'
        logger.info("Pipeline completed successfully")

    except Exception as e:
        metrics['error_message'] = str(e)
        logger.error(f"Pipeline failed: {e}", exc_info=True)
        raise

    finally:
        # Calculate duration
        metrics['duration_seconds'] = round(time.time() - pipeline_start, 2)
        metrics['end_time'] = datetime.now()

        # Log metrics
        log_pipeline_metrics(metrics)

        # Close connections
        if source_conn:
            source_conn.dispose()
        if target_conn:
            target_conn.dispose()

    return metrics

# ============================================
# ENTRY POINT
# ============================================

if __name__ == "__main__":
    try:
        metrics = run_pipeline()
        sys.exit(0 if metrics['status'] == 'SUCCESS' else 1)
    except Exception as e:
        logger.critical(f"Pipeline execution failed: {e}")
        sys.exit(1)
