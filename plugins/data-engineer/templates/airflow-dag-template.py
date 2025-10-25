"""
Airflow DAG Template
Production-ready DAG with best practices for error handling, monitoring, and alerting.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
from airflow.exceptions import AirflowException
from datetime import datetime, timedelta
import logging
import pandas as pd

# ============================================
# CONFIGURATION
# ============================================

# Get configuration from Airflow Variables
PIPELINE_CONFIG = {
    'source_connection_id': Variable.get('source_connection_id', default_var='postgres_source'),
    'target_connection_id': Variable.get('target_connection_id', default_var='postgres_target'),
    'source_table': Variable.get('source_table', default_var='customers'),
    'target_table': Variable.get('target_table', default_var='customers'),
    'batch_size': int(Variable.get('batch_size', default_var='10000')),
}

# Default arguments for all tasks
default_args = {
    'owner': 'data-engineering',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['data-alerts@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(minutes=30),
    'execution_timeout': timedelta(hours=2),
}

# ============================================
# CALLBACK FUNCTIONS
# ============================================

def on_failure_callback(context):
    """Handle task failure with custom alerting."""
    task_instance = context['task_instance']
    dag_id = context['dag'].dag_id
    task_id = task_instance.task_id
    execution_date = context['execution_date']
    exception = context.get('exception')

    error_message = (
        f"Task Failed!\n"
        f"DAG: {dag_id}\n"
        f"Task: {task_id}\n"
        f"Execution Date: {execution_date}\n"
        f"Error: {exception}\n"
        f"Log URL: {task_instance.log_url}"
    )

    logging.error(error_message)
    # Add custom alerting here (Slack, PagerDuty, etc.)
    # send_slack_alert(error_message)

def on_retry_callback(context):
    """Log retry attempts."""
    task_instance = context['task_instance']
    logging.warning(
        f"Task {task_instance.task_id} is being retried. "
        f"Attempt {task_instance.try_number} of {task_instance.max_tries}"
    )

def on_success_callback(context):
    """Handle successful task completion."""
    task_instance = context['task_instance']
    logging.info(f"Task {task_instance.task_id} completed successfully")

# ============================================
# DAG DEFINITION
# ============================================

dag = DAG(
    dag_id='customer_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for customer data with comprehensive error handling',
    schedule_interval='0 2 * * *',  # Daily at 2 AM UTC
    catchup=False,
    max_active_runs=1,
    tags=['etl', 'customer', 'production'],
    doc_md="""
    # Customer ETL Pipeline

    ## Purpose
    Extracts customer data from PostgreSQL source, transforms it, and loads into the target warehouse.

    ## Schedule
    Runs daily at 2 AM UTC

    ## Dependencies
    - Source: PostgreSQL database (connection: postgres_source)
    - Target: PostgreSQL warehouse (connection: postgres_target)

    ## Tasks
    1. **validate_connections**: Verify database connectivity
    2. **check_source_data**: Validate source data availability and quality
    3. **extract**: Extract data from source database
    4. **transform**: Apply business rules and data cleansing
    5. **load**: Load transformed data to target warehouse
    6. **validate_load**: Verify data loaded correctly
    7. **cleanup**: Clean up staging tables and temporary resources

    ## Alerts
    - Email notifications on failure: data-alerts@example.com
    - Retries: 3 attempts with exponential backoff

    ## SLA
    - Task execution timeout: 2 hours
    - Expected completion time: 30 minutes
    """
)

# ============================================
# TASK FUNCTIONS
# ============================================

def validate_connections(**context):
    """Validate that required database connections are accessible."""
    logging.info("Validating database connections...")

    # Test source connection
    try:
        source_hook = PostgresHook(postgres_conn_id=PIPELINE_CONFIG['source_connection_id'])
        source_hook.get_first("SELECT 1")
        logging.info("Source connection validated successfully")
    except Exception as e:
        raise AirflowException(f"Source connection validation failed: {e}")

    # Test target connection
    try:
        target_hook = PostgresHook(postgres_conn_id=PIPELINE_CONFIG['target_connection_id'])
        target_hook.get_first("SELECT 1")
        logging.info("Target connection validated successfully")
    except Exception as e:
        raise AirflowException(f"Target connection validation failed: {e}")

    return {'status': 'connections_valid'}

def check_source_data(**context):
    """Check source data availability and quality."""
    logging.info("Checking source data...")

    source_hook = PostgresHook(postgres_conn_id=PIPELINE_CONFIG['source_connection_id'])
    table_name = PIPELINE_CONFIG['source_table']

    # Check if table exists and has data
    check_query = f"""
        SELECT
            COUNT(*) as total_rows,
            MAX(updated_at) as last_update
        FROM {table_name}
    """

    result = source_hook.get_first(check_query)
    total_rows, last_update = result

    if total_rows == 0:
        raise AirflowException(f"Source table {table_name} is empty")

    logging.info(f"Source table has {total_rows} rows, last updated: {last_update}")

    # Push metadata to XCom
    return {
        'total_rows': total_rows,
        'last_update': str(last_update)
    }

def extract(**context):
    """Extract data from source database."""
    logging.info("Starting data extraction...")

    ti = context['ti']
    execution_date = context['execution_date']

    source_hook = PostgresHook(postgres_conn_id=PIPELINE_CONFIG['source_connection_id'])
    table_name = PIPELINE_CONFIG['source_table']

    # Get last watermark (execution_date - 1 day for daily runs)
    last_watermark = execution_date - timedelta(days=1)

    # Incremental extraction query
    extract_query = f"""
        SELECT *
        FROM {table_name}
        WHERE updated_at > '{last_watermark}'
        ORDER BY updated_at
    """

    # Extract data
    df = source_hook.get_pandas_df(extract_query)
    row_count = len(df)

    if row_count == 0:
        logging.info("No new data to extract")
        return {'rows_extracted': 0}

    logging.info(f"Extracted {row_count} rows")

    # Save to staging (use Airflow's temp directory or external storage)
    staging_file = f"/tmp/{context['dag'].dag_id}_{context['task'].task_id}_{execution_date}.csv"
    df.to_csv(staging_file, index=False)

    # Push metadata to XCom
    ti.xcom_push(key='staging_file', value=staging_file)
    ti.xcom_push(key='rows_extracted', value=row_count)

    return {'rows_extracted': row_count, 'staging_file': staging_file}

def transform(**context):
    """Transform extracted data."""
    logging.info("Starting data transformation...")

    ti = context['ti']

    # Get staging file from XCom
    staging_file = ti.xcom_pull(task_ids='extract', key='staging_file')
    rows_extracted = ti.xcom_pull(task_ids='extract', key='rows_extracted')

    if rows_extracted == 0:
        logging.info("No data to transform")
        return {'rows_transformed': 0}

    # Load data from staging
    df = pd.read_csv(staging_file)
    logging.info(f"Loaded {len(df)} rows for transformation")

    # 1. Remove duplicates
    original_count = len(df)
    df = df.drop_duplicates(subset=['customer_id'], keep='last')
    logging.info(f"Removed {original_count - len(df)} duplicate records")

    # 2. Data cleansing
    df['email'] = df['email'].fillna('unknown@example.com')
    df['phone'] = df['phone'].fillna('')

    # Trim whitespace
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()

    # 3. Data standardization
    df['email'] = df['email'].str.lower()
    df['country'] = df['country'].str.upper()

    # 4. Data validation
    invalid_emails = ~df['email'].str.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', na=False)
    if invalid_emails.any():
        logging.warning(f"Found {invalid_emails.sum()} records with invalid email format")

    # Save transformed data
    transformed_file = staging_file.replace('.csv', '_transformed.csv')
    df.to_csv(transformed_file, index=False)

    # Push metadata to XCom
    ti.xcom_push(key='transformed_file', value=transformed_file)
    ti.xcom_push(key='rows_transformed', value=len(df))

    logging.info(f"Transformation completed. {len(df)} rows ready for loading")
    return {'rows_transformed': len(df), 'transformed_file': transformed_file}

def load(**context):
    """Load transformed data to target warehouse."""
    logging.info("Starting data load...")

    ti = context['ti']

    # Get transformed file from XCom
    transformed_file = ti.xcom_pull(task_ids='transform', key='transformed_file')
    rows_transformed = ti.xcom_pull(task_ids='transform', key='rows_transformed')

    if rows_transformed == 0:
        logging.info("No data to load")
        return {'rows_loaded': 0}

    # Load transformed data
    df = pd.read_csv(transformed_file)

    target_hook = PostgresHook(postgres_conn_id=PIPELINE_CONFIG['target_connection_id'])
    table_name = PIPELINE_CONFIG['target_table']
    staging_table = f"{table_name}_staging"

    # Load to staging table using pandas
    engine = target_hook.get_sqlalchemy_engine()
    df.to_sql(
        staging_table,
        engine,
        if_exists='replace',
        index=False,
        method='multi',
        chunksize=PIPELINE_CONFIG['batch_size']
    )

    logging.info(f"Loaded {len(df)} rows to staging table: {staging_table}")

    # Merge staging to production
    merge_query = f"""
        INSERT INTO {table_name} (customer_id, email, phone, country, updated_at)
        SELECT customer_id, email, phone, country, updated_at
        FROM {staging_table}
        ON CONFLICT (customer_id)
        DO UPDATE SET
            email = EXCLUDED.email,
            phone = EXCLUDED.phone,
            country = EXCLUDED.country,
            updated_at = EXCLUDED.updated_at
    """

    target_hook.run(merge_query)
    logging.info(f"Merged {len(df)} rows into {table_name}")

    # Push metadata to XCom
    ti.xcom_push(key='rows_loaded', value=len(df))

    return {'rows_loaded': len(df)}

def validate_load(**context):
    """Validate that data was loaded correctly."""
    logging.info("Validating data load...")

    ti = context['ti']
    rows_loaded = ti.xcom_pull(task_ids='load', key='rows_loaded')

    if rows_loaded == 0:
        logging.info("No data loaded, skipping validation")
        return {'validation_status': 'skipped'}

    target_hook = PostgresHook(postgres_conn_id=PIPELINE_CONFIG['target_connection_id'])
    table_name = PIPELINE_CONFIG['target_table']

    # Validate row count
    validation_query = f"""
        SELECT
            COUNT(*) as total_rows,
            COUNT(CASE WHEN email IS NULL OR email = '' THEN 1 END) as null_emails,
            MAX(updated_at) as last_update
        FROM {table_name}
    """

    result = target_hook.get_first(validation_query)
    total_rows, null_emails, last_update = result

    logging.info(f"Validation results: total_rows={total_rows}, null_emails={null_emails}, last_update={last_update}")

    # Check for data quality issues
    if null_emails > 0:
        logging.warning(f"Found {null_emails} records with null emails")

    return {
        'validation_status': 'passed',
        'total_rows': total_rows,
        'null_emails': null_emails
    }

def cleanup(**context):
    """Clean up staging resources."""
    logging.info("Cleaning up staging resources...")

    import os

    ti = context['ti']

    # Clean up staging files
    staging_file = ti.xcom_pull(task_ids='extract', key='staging_file')
    transformed_file = ti.xcom_pull(task_ids='transform', key='transformed_file')

    for file_path in [staging_file, transformed_file]:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
            logging.info(f"Removed staging file: {file_path}")

    # Clean up staging table
    target_hook = PostgresHook(postgres_conn_id=PIPELINE_CONFIG['target_connection_id'])
    table_name = PIPELINE_CONFIG['target_table']
    staging_table = f"{table_name}_staging"

    try:
        target_hook.run(f"DROP TABLE IF EXISTS {staging_table}")
        logging.info(f"Dropped staging table: {staging_table}")
    except Exception as e:
        logging.warning(f"Could not drop staging table: {e}")

    logging.info("Cleanup completed")
    return {'cleanup_status': 'completed'}

# ============================================
# TASK DEFINITIONS
# ============================================

start = DummyOperator(
    task_id='start',
    dag=dag
)

validate_connections_task = PythonOperator(
    task_id='validate_connections',
    python_callable=validate_connections,
    on_failure_callback=on_failure_callback,
    on_retry_callback=on_retry_callback,
    dag=dag
)

check_source_data_task = PythonOperator(
    task_id='check_source_data',
    python_callable=check_source_data,
    on_failure_callback=on_failure_callback,
    on_retry_callback=on_retry_callback,
    dag=dag
)

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract,
    on_failure_callback=on_failure_callback,
    on_retry_callback=on_retry_callback,
    on_success_callback=on_success_callback,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform,
    on_failure_callback=on_failure_callback,
    on_retry_callback=on_retry_callback,
    on_success_callback=on_success_callback,
    dag=dag
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load,
    on_failure_callback=on_failure_callback,
    on_retry_callback=on_retry_callback,
    on_success_callback=on_success_callback,
    dag=dag
)

validate_load_task = PythonOperator(
    task_id='validate_load',
    python_callable=validate_load,
    on_failure_callback=on_failure_callback,
    dag=dag
)

cleanup_task = PythonOperator(
    task_id='cleanup',
    python_callable=cleanup,
    trigger_rule='all_done',  # Always run cleanup, even if previous tasks failed
    dag=dag
)

end = DummyOperator(
    task_id='end',
    trigger_rule='all_success',
    dag=dag
)

# ============================================
# TASK DEPENDENCIES
# ============================================

start >> validate_connections_task >> check_source_data_task >> extract_task
extract_task >> transform_task >> load_task >> validate_load_task
validate_load_task >> cleanup_task >> end
