# Orchestration Skill

This skill provides comprehensive patterns for workflow orchestration using Apache Airflow, Prefect, and other orchestration tools.

## Apache Airflow Patterns

### 1. Basic DAG Structure

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Default arguments for all tasks
default_args = {
    'owner': 'data-engineering',
    'depends_on_past': False,
    'email': ['alerts@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(minutes=30)
}

# DAG definition
dag = DAG(
    'customer_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for customer data',
    schedule_interval='0 2 * * *',  # Daily at 2 AM UTC
    start_date=days_ago(1),
    catchup=False,  # Don't backfill historical runs
    tags=['etl', 'customer', 'daily'],
    max_active_runs=1  # Prevent concurrent runs
)
```

### 2. Sequential Task Pattern

```python
def extract_data(**context):
    """Extract data from source."""
    # Extract logic
    return {'row_count': 1000}

def transform_data(**context):
    """Transform extracted data."""
    # Get data from previous task
    ti = context['ti']
    extract_result = ti.xcom_pull(task_ids='extract')
    # Transform logic
    return {'transformed_rows': extract_result['row_count']}

def load_data(**context):
    """Load transformed data."""
    # Load logic
    pass

# Create tasks
extract = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    dag=dag
)

transform = PythonOperator(
    task_id='transform',
    python_callable=transform_data,
    dag=dag
)

load = PythonOperator(
    task_id='load',
    python_callable=load_data,
    dag=dag
)

# Define dependencies (sequential)
extract >> transform >> load
```

### 3. Parallel Task Pattern

```python
from airflow.operators.dummy import DummyOperator

# Start marker
start = DummyOperator(task_id='start', dag=dag)

# Parallel extraction tasks
extract_customers = PythonOperator(
    task_id='extract_customers',
    python_callable=extract_customers_func,
    dag=dag
)

extract_orders = PythonOperator(
    task_id='extract_orders',
    python_callable=extract_orders_func,
    dag=dag
)

extract_products = PythonOperator(
    task_id='extract_products',
    python_callable=extract_products_func,
    dag=dag
)

# Merge results
merge = PythonOperator(
    task_id='merge_data',
    python_callable=merge_func,
    dag=dag
)

# End marker
end = DummyOperator(task_id='end', dag=dag)

# Define dependencies (parallel extraction, then merge)
start >> [extract_customers, extract_orders, extract_products] >> merge >> end
```

### 4. Conditional Branching Pattern

```python
from airflow.operators.python import BranchPythonOperator

def check_data_quality(**context):
    """Check data quality and decide next step."""
    ti = context['ti']
    row_count = ti.xcom_pull(task_ids='extract')['row_count']

    if row_count > 0:
        return 'process_data'  # Task ID to execute
    else:
        return 'send_alert'  # Alternative task ID

# Branch operator
quality_check = BranchPythonOperator(
    task_id='quality_check',
    python_callable=check_data_quality,
    dag=dag
)

process_data = PythonOperator(
    task_id='process_data',
    python_callable=process_func,
    dag=dag
)

send_alert = PythonOperator(
    task_id='send_alert',
    python_callable=alert_func,
    dag=dag
)

# Dependencies with branching
extract >> quality_check >> [process_data, send_alert]
```

### 5. Dynamic Task Generation

```python
from airflow.utils.task_group import TaskGroup

def create_processing_tasks(source_list):
    """Dynamically create tasks for each source."""
    tasks = []

    for source in source_list:
        task = PythonOperator(
            task_id=f'process_{source}',
            python_callable=process_source,
            op_args=[source],
            dag=dag
        )
        tasks.append(task)

    return tasks

# Create tasks for multiple sources
sources = ['mysql', 'postgres', 'mongodb']
processing_tasks = create_processing_tasks(sources)

# Set dependencies
start >> processing_tasks >> end
```

### 6. Task Groups for Organization

```python
with TaskGroup('extraction_group', tooltip='Extract from all sources') as extraction_group:
    extract_db1 = PythonOperator(task_id='extract_db1', python_callable=extract1)
    extract_db2 = PythonOperator(task_id='extract_db2', python_callable=extract2)
    extract_api = PythonOperator(task_id='extract_api', python_callable=extract3)

with TaskGroup('transformation_group', tooltip='Transform all data') as transformation_group:
    clean_data = PythonOperator(task_id='clean', python_callable=clean)
    enrich_data = PythonOperator(task_id='enrich', python_callable=enrich)
    clean_data >> enrich_data

# Task group dependencies
extraction_group >> transformation_group >> load
```

## Scheduling Patterns

### 1. Time-Based Scheduling

```python
# Daily at specific time
schedule_interval='0 2 * * *'  # 2 AM daily

# Hourly
schedule_interval='0 * * * *'  # Every hour

# Weekly on Monday
schedule_interval='0 2 * * 1'  # 2 AM every Monday

# Monthly on 1st
schedule_interval='0 2 1 * *'  # 2 AM on 1st of month

# Using timedelta
schedule_interval=timedelta(hours=6)  # Every 6 hours

# Using Airflow presets
from airflow.timetables.interval import CronDataIntervalTimetable
schedule_interval='@daily'  # Midnight daily
schedule_interval='@hourly'
schedule_interval='@weekly'
```

### 2. Event-Based Triggers (Sensors)

```python
from airflow.sensors.filesystem import FileSensor
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

# Wait for file to appear
wait_for_file = FileSensor(
    task_id='wait_for_file',
    filepath='/data/input/customers.csv',
    poke_interval=60,  # Check every 60 seconds
    timeout=3600,  # Timeout after 1 hour
    mode='poke',
    dag=dag
)

# Wait for S3 object
wait_for_s3 = S3KeySensor(
    task_id='wait_for_s3',
    bucket_name='my-bucket',
    bucket_key='data/customers/*.csv',
    wildcard_match=True,
    aws_conn_id='aws_default',
    dag=dag
)

# Wait for another DAG to complete
wait_for_upstream_dag = ExternalTaskSensor(
    task_id='wait_for_upstream',
    external_dag_id='upstream_dag',
    external_task_id='final_task',
    timeout=3600,
    dag=dag
)

wait_for_file >> extract >> transform >> load
```

### 3. Backfill and Catchup

```python
# Disable catchup (don't run historical DAG runs)
dag = DAG(
    'my_dag',
    catchup=False,  # Only run for current interval
    ...
)

# Enable catchup for historical data processing
dag = DAG(
    'my_dag',
    catchup=True,
    start_date=datetime(2024, 1, 1),  # Will backfill from this date
    ...
)

# Use execution_date in tasks
def process_data(**context):
    execution_date = context['execution_date']
    # Process data for this specific date
    print(f"Processing data for {execution_date}")
```

## Error Handling Patterns

### 1. Retry Configuration

```python
# Task-level retry configuration
task = PythonOperator(
    task_id='my_task',
    python_callable=my_func,
    retries=5,
    retry_delay=timedelta(minutes=5),
    retry_exponential_backoff=True,
    max_retry_delay=timedelta(hours=1),
    dag=dag
)

# Custom retry logic
def my_func_with_retry(**context):
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            # Attempt operation
            return result
        except Exception as e:
            if attempt == max_attempts - 1:
                raise
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(5 * (attempt + 1))  # Exponential backoff
```

### 2. Failure Callbacks

```python
def on_failure_callback(context):
    """Send alert when task fails."""
    task_instance = context['task_instance']
    dag_id = context['dag'].dag_id
    task_id = task_instance.task_id
    execution_date = context['execution_date']

    # Send Slack notification
    send_slack_alert(
        f"Task {dag_id}.{task_id} failed at {execution_date}"
    )

def on_retry_callback(context):
    """Log retry attempt."""
    print(f"Retrying task after failure...")

def on_success_callback(context):
    """Log success."""
    print(f"Task completed successfully")

task = PythonOperator(
    task_id='my_task',
    python_callable=my_func,
    on_failure_callback=on_failure_callback,
    on_retry_callback=on_retry_callback,
    on_success_callback=on_success_callback,
    dag=dag
)
```

### 3. Trigger Rules

```python
from airflow.utils.trigger_rule import TriggerRule

# Default: all_success (all upstream tasks succeeded)
task1 = PythonOperator(
    task_id='task1',
    python_callable=func1,
    dag=dag
)

# Run if at least one upstream task succeeded
task2 = PythonOperator(
    task_id='task2',
    python_callable=func2,
    trigger_rule=TriggerRule.ONE_SUCCESS,
    dag=dag
)

# Run if any upstream task failed
task3 = PythonOperator(
    task_id='task3',
    python_callable=func3,
    trigger_rule=TriggerRule.ONE_FAILED,
    dag=dag
)

# Always run regardless of upstream status
cleanup = PythonOperator(
    task_id='cleanup',
    python_callable=cleanup_func,
    trigger_rule=TriggerRule.ALL_DONE,
    dag=dag
)

[task1, task2, task3] >> cleanup
```

## Monitoring & Alerting

### 1. SLA Monitoring

```python
from airflow.models import DAG
from datetime import timedelta

# Set SLA at DAG level
default_args = {
    'sla': timedelta(hours=2),  # Task should complete within 2 hours
    'sla_miss_callback': handle_sla_miss
}

def handle_sla_miss(dag, task_list, blocking_task_list, slas, blocking_tis):
    """Handle SLA miss."""
    for sla in slas:
        print(f"SLA missed for {sla.task_id} at {sla.execution_date}")
        send_alert(f"SLA missed for {sla.task_id}")

# Task-specific SLA
task = PythonOperator(
    task_id='critical_task',
    python_callable=func,
    sla=timedelta(minutes=30),  # This task must complete in 30 min
    dag=dag
)
```

### 2. Custom Metrics

```python
from airflow.metrics import Stats

def my_task_func(**context):
    start_time = time.time()

    # Your processing logic
    row_count = process_data()

    # Log custom metrics
    Stats.incr('custom.tasks.success')
    Stats.gauge('custom.rows_processed', row_count)
    Stats.timing('custom.task_duration', time.time() - start_time)

    return row_count
```

### 3. Health Checks

```python
from airflow.sensors.base import BaseSensorOperator

class DataQualityCheckSensor(BaseSensorOperator):
    """Custom sensor for data quality checks."""

    def __init__(self, table_name, quality_threshold=0.95, **kwargs):
        super().__init__(**kwargs)
        self.table_name = table_name
        self.quality_threshold = quality_threshold

    def poke(self, context):
        """Check if data quality meets threshold."""
        quality_score = check_data_quality(self.table_name)
        self.log.info(f"Quality score: {quality_score}")

        if quality_score >= self.quality_threshold:
            return True
        else:
            self.log.warning(f"Quality score {quality_score} below threshold")
            return False

# Use custom sensor
quality_check = DataQualityCheckSensor(
    task_id='quality_check',
    table_name='customers',
    quality_threshold=0.95,
    poke_interval=300,  # Check every 5 minutes
    timeout=3600,
    dag=dag
)
```

## Advanced Patterns

### 1. Data Passing with XCom

```python
def extract(**context):
    data = {'customers': 1000, 'orders': 5000}
    # Push data to XCom (small data only)
    return data

def transform(**context):
    ti = context['ti']
    # Pull data from XCom
    data = ti.xcom_pull(task_ids='extract')
    print(f"Processing {data['customers']} customers")

    # Push results
    ti.xcom_push(key='transformed_count', value=data['customers'])

def load(**context):
    ti = context['ti']
    # Pull specific key
    count = ti.xcom_pull(task_ids='transform', key='transformed_count')
    print(f"Loading {count} records")
```

### 2. Connection Management

```python
from airflow.hooks.base import BaseHook
from airflow.providers.postgres.hooks.postgres import PostgresHook

def extract_from_db(**context):
    # Get connection using Hook
    postgres_hook = PostgresHook(postgres_conn_id='postgres_default')

    # Execute query
    df = postgres_hook.get_pandas_df(
        sql="SELECT * FROM customers WHERE updated_at > %(date)s",
        parameters={'date': '2024-01-01'}
    )

    return len(df)
```

### 3. Resource Pools

```python
# Define pools in Airflow UI or via CLI:
# airflow pools set my_pool 5 "Pool for database connections"

# Use pool in task
task = PythonOperator(
    task_id='db_task',
    python_callable=db_func,
    pool='my_pool',  # Limit concurrent executions
    dag=dag
)
```

## Prefect Patterns

### 1. Basic Flow

```python
from prefect import flow, task

@task(retries=3, retry_delay_seconds=60)
def extract():
    """Extract data."""
    return {'row_count': 1000}

@task
def transform(data):
    """Transform data."""
    return {'processed': data['row_count']}

@task
def load(data):
    """Load data."""
    print(f"Loading {data['processed']} records")

@flow(name="customer-etl")
def customer_etl_flow():
    """Main ETL flow."""
    extracted = extract()
    transformed = transform(extracted)
    load(transformed)

# Run flow
if __name__ == "__main__":
    customer_etl_flow()
```

### 2. Parallel Execution

```python
from prefect import flow, task
from prefect.task_runners import ConcurrentTaskRunner

@task
def process_source(source_name):
    """Process individual source."""
    print(f"Processing {source_name}")
    return {'source': source_name, 'count': 100}

@flow(task_runner=ConcurrentTaskRunner())
def parallel_extraction():
    """Extract from multiple sources in parallel."""
    sources = ['mysql', 'postgres', 'mongodb']

    # Submit tasks in parallel
    futures = [process_source.submit(source) for source in sources]

    # Wait for all tasks
    results = [future.result() for future in futures]
    return results
```

## Best Practices

### 1. Idempotency
- Design tasks to produce same results when run multiple times
- Use upsert operations instead of inserts
- Clean up before processing (delete temp files)

### 2. Small Tasks
- Break large operations into smaller tasks
- Easier to retry individual failures
- Better visibility into progress

### 3. Configuration Management
```python
from airflow.models import Variable

# Store configuration in Airflow Variables
db_host = Variable.get("db_host")
api_key = Variable.get("api_key", default_var="default_key")

# Use connections for credentials
```

### 4. Testing
```python
# Test task functions independently
def test_extract():
    context = {'execution_date': datetime.now()}
    result = extract_data(**context)
    assert result['row_count'] > 0

# Test DAG structure
from airflow.models import DagBag

def test_dag_loading():
    dagbag = DagBag()
    dag = dagbag.get_dag('customer_etl_pipeline')
    assert dag is not None
    assert len(dag.tasks) == 3
```

### 5. Documentation
```python
dag = DAG(
    'customer_etl',
    description='Loads customer data from MySQL to Snowflake',
    doc_md="""
    # Customer ETL Pipeline

    ## Purpose
    Extract customer data from MySQL, transform it, and load into Snowflake.

    ## Schedule
    Runs daily at 2 AM UTC

    ## Dependencies
    - Requires MySQL connection 'mysql_prod'
    - Requires Snowflake connection 'snowflake_warehouse'

    ## Alerts
    Sends email on failure to data-team@example.com
    """,
    tags=['etl', 'customer', 'daily']
)
```

## Common Patterns Summary

1. **Sequential Pipeline**: `task1 >> task2 >> task3`
2. **Parallel Processing**: `start >> [task1, task2, task3] >> end`
3. **Branching**: Use BranchPythonOperator for conditional logic
4. **Dynamic Tasks**: Generate tasks based on configuration
5. **Sensors**: Wait for external events before processing
6. **Task Groups**: Organize related tasks together
7. **Error Handling**: Use callbacks and trigger rules
8. **Resource Management**: Use pools to limit concurrency
9. **Data Passing**: Use XCom for small data, external storage for large data
10. **Monitoring**: Implement SLAs, metrics, and health checks
