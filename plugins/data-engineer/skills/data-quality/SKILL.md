# Data Quality Skill

This skill provides comprehensive techniques for data validation, profiling, anomaly detection, and quality monitoring.

## Data Validation Patterns

### 1. Completeness Checks

#### Null Value Validation
```python
def check_nulls(df, required_columns):
    """Check for null values in required columns."""
    results = {}
    for col in required_columns:
        null_count = df[col].isnull().sum()
        null_pct = (null_count / len(df)) * 100
        results[col] = {
            'null_count': null_count,
            'null_percentage': null_pct,
            'passed': null_count == 0
        }
    return results
```

#### Record Count Validation
```python
def validate_record_count(actual_count, expected_count, tolerance=0.05):
    """Validate record count is within tolerance."""
    if expected_count == 0:
        return actual_count == 0

    diff_pct = abs(actual_count - expected_count) / expected_count
    return {
        'actual_count': actual_count,
        'expected_count': expected_count,
        'difference_pct': diff_pct * 100,
        'passed': diff_pct <= tolerance
    }
```

### 2. Accuracy Checks

#### Data Type Validation
```python
def validate_data_types(df, expected_types):
    """Validate column data types match expectations."""
    results = {}
    for col, expected_type in expected_types.items():
        actual_type = str(df[col].dtype)
        results[col] = {
            'expected_type': expected_type,
            'actual_type': actual_type,
            'passed': actual_type == expected_type
        }
    return results
```

#### Format Validation
```python
import re

def validate_formats(df, format_rules):
    """Validate data formats using regex patterns."""
    results = {}

    patterns = {
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'phone': r'^\+?1?\d{9,15}$',
        'zipcode': r'^\d{5}(-\d{4})?$',
        'ssn': r'^\d{3}-\d{2}-\d{4}$',
        'url': r'^https?://[^\s]+$',
        'ipv4': r'^(\d{1,3}\.){3}\d{1,3}$'
    }

    for col, format_type in format_rules.items():
        pattern = patterns.get(format_type)
        if pattern:
            valid_mask = df[col].astype(str).str.match(pattern, na=False)
            invalid_count = (~valid_mask & df[col].notna()).sum()
            results[col] = {
                'format': format_type,
                'invalid_count': invalid_count,
                'invalid_percentage': (invalid_count / len(df)) * 100,
                'passed': invalid_count == 0
            }

    return results
```

#### Range Validation
```python
def validate_ranges(df, range_rules):
    """Validate numeric values are within expected ranges."""
    results = {}

    for col, (min_val, max_val) in range_rules.items():
        out_of_range = df[
            (df[col] < min_val) | (df[col] > max_val)
        ][col].count()

        results[col] = {
            'min_expected': min_val,
            'max_expected': max_val,
            'min_actual': df[col].min(),
            'max_actual': df[col].max(),
            'out_of_range_count': out_of_range,
            'passed': out_of_range == 0
        }

    return results
```

### 3. Consistency Checks

#### Referential Integrity
```python
def check_referential_integrity(df, reference_df, fk_col, pk_col):
    """Check foreign key relationships."""
    orphaned_records = df[~df[fk_col].isin(reference_df[pk_col])]

    return {
        'total_records': len(df),
        'orphaned_records': len(orphaned_records),
        'orphaned_percentage': (len(orphaned_records) / len(df)) * 100,
        'passed': len(orphaned_records) == 0,
        'orphaned_keys': orphaned_records[fk_col].unique().tolist()
    }
```

#### Cross-Field Validation
```python
def validate_cross_fields(df, rules):
    """Validate relationships between fields."""
    results = {}

    # Example: end_date >= start_date
    if 'date_range' in rules:
        invalid = df[df['end_date'] < df['start_date']]
        results['date_range'] = {
            'rule': 'end_date >= start_date',
            'invalid_count': len(invalid),
            'passed': len(invalid) == 0
        }

    # Example: discount_amount <= total_amount
    if 'discount_validation' in rules:
        invalid = df[df['discount_amount'] > df['total_amount']]
        results['discount_validation'] = {
            'rule': 'discount_amount <= total_amount',
            'invalid_count': len(invalid),
            'passed': len(invalid) == 0
        }

    # Example: age calculation from birthdate
    if 'age_consistency' in rules:
        df['calculated_age'] = (pd.Timestamp.now() - df['birthdate']).dt.days // 365
        inconsistent = df[abs(df['age'] - df['calculated_age']) > 1]
        results['age_consistency'] = {
            'rule': 'age matches birthdate',
            'inconsistent_count': len(inconsistent),
            'passed': len(inconsistent) == 0
        }

    return results
```

### 4. Uniqueness Checks

#### Duplicate Detection
```python
def check_duplicates(df, key_columns):
    """Check for duplicate records based on key columns."""
    duplicates = df[df.duplicated(subset=key_columns, keep=False)]

    return {
        'total_records': len(df),
        'duplicate_records': len(duplicates),
        'duplicate_percentage': (len(duplicates) / len(df)) * 100,
        'passed': len(duplicates) == 0,
        'duplicate_keys': duplicates[key_columns].drop_duplicates().to_dict('records')
    }
```

#### Primary Key Validation
```python
def validate_primary_key(df, pk_columns):
    """Validate primary key uniqueness and non-null."""
    results = {
        'columns': pk_columns,
        'checks': {}
    }

    # Check for nulls
    null_count = df[pk_columns].isnull().any(axis=1).sum()
    results['checks']['null_check'] = {
        'null_count': null_count,
        'passed': null_count == 0
    }

    # Check for duplicates
    dup_count = df.duplicated(subset=pk_columns).sum()
    results['checks']['uniqueness_check'] = {
        'duplicate_count': dup_count,
        'passed': dup_count == 0
    }

    results['passed'] = all(check['passed'] for check in results['checks'].values())

    return results
```

### 5. Timeliness Checks

#### Data Freshness
```python
def check_data_freshness(df, timestamp_col, max_age_hours=24):
    """Check if data is fresh (recently updated)."""
    latest_timestamp = df[timestamp_col].max()
    age_hours = (pd.Timestamp.now() - latest_timestamp).total_seconds() / 3600

    return {
        'latest_timestamp': latest_timestamp,
        'age_hours': age_hours,
        'max_age_hours': max_age_hours,
        'passed': age_hours <= max_age_hours,
        'status': 'fresh' if age_hours <= max_age_hours else 'stale'
    }
```

## Data Profiling

### Statistical Profiling
```python
def profile_numeric_column(series):
    """Generate statistical profile for numeric column."""
    return {
        'count': series.count(),
        'null_count': series.isnull().sum(),
        'null_percentage': (series.isnull().sum() / len(series)) * 100,
        'mean': series.mean(),
        'median': series.median(),
        'std': series.std(),
        'min': series.min(),
        'max': series.max(),
        'q25': series.quantile(0.25),
        'q75': series.quantile(0.75),
        'unique_count': series.nunique(),
        'zeros': (series == 0).sum()
    }

def profile_categorical_column(series, top_n=10):
    """Generate profile for categorical column."""
    value_counts = series.value_counts()

    return {
        'count': series.count(),
        'null_count': series.isnull().sum(),
        'null_percentage': (series.isnull().sum() / len(series)) * 100,
        'unique_count': series.nunique(),
        'cardinality': series.nunique() / len(series),
        'mode': series.mode()[0] if not series.mode().empty else None,
        'top_values': value_counts.head(top_n).to_dict()
    }

def profile_dataset(df):
    """Generate comprehensive dataset profile."""
    profile = {
        'row_count': len(df),
        'column_count': len(df.columns),
        'memory_usage_mb': df.memory_usage(deep=True).sum() / (1024**2),
        'columns': {}
    }

    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            profile['columns'][col] = profile_numeric_column(df[col])
        else:
            profile['columns'][col] = profile_categorical_column(df[col])

    return profile
```

## Anomaly Detection

### Statistical Outlier Detection
```python
def detect_outliers_iqr(series):
    """Detect outliers using Interquartile Range (IQR) method."""
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = series[(series < lower_bound) | (series > upper_bound)]

    return {
        'lower_bound': lower_bound,
        'upper_bound': upper_bound,
        'outlier_count': len(outliers),
        'outlier_percentage': (len(outliers) / len(series)) * 100,
        'outlier_values': outliers.tolist()
    }

def detect_outliers_zscore(series, threshold=3):
    """Detect outliers using Z-score method."""
    z_scores = np.abs((series - series.mean()) / series.std())
    outliers = series[z_scores > threshold]

    return {
        'threshold': threshold,
        'outlier_count': len(outliers),
        'outlier_percentage': (len(outliers) / len(series)) * 100,
        'outlier_values': outliers.tolist()
    }
```

### Pattern Anomalies
```python
def detect_value_distribution_change(current_df, historical_df, column):
    """Detect significant changes in value distribution."""
    current_dist = current_df[column].value_counts(normalize=True)
    historical_dist = historical_df[column].value_counts(normalize=True)

    # Compare distributions using KL divergence
    all_values = set(current_dist.index) | set(historical_dist.index)

    kl_divergence = 0
    for value in all_values:
        p = current_dist.get(value, 1e-10)
        q = historical_dist.get(value, 1e-10)
        kl_divergence += p * np.log(p / q)

    return {
        'kl_divergence': kl_divergence,
        'significant_change': kl_divergence > 0.1,
        'new_values': list(set(current_dist.index) - set(historical_dist.index)),
        'missing_values': list(set(historical_dist.index) - set(current_dist.index))
    }
```

### Time Series Anomalies
```python
def detect_volume_anomalies(df, timestamp_col, window='1D', threshold=2):
    """Detect anomalies in data volume over time."""
    daily_counts = df.groupby(pd.Grouper(key=timestamp_col, freq=window)).size()

    mean = daily_counts.mean()
    std = daily_counts.std()

    anomalies = daily_counts[np.abs(daily_counts - mean) > threshold * std]

    return {
        'mean_volume': mean,
        'std_volume': std,
        'threshold': threshold,
        'anomalous_periods': anomalies.to_dict(),
        'anomaly_count': len(anomalies)
    }
```

## Quality Scoring

### Calculate Overall Quality Score
```python
def calculate_quality_score(validation_results):
    """Calculate overall data quality score from validation results."""
    scores = {
        'completeness': 0,
        'accuracy': 0,
        'consistency': 0,
        'uniqueness': 0,
        'timeliness': 0
    }

    weights = {
        'completeness': 0.25,
        'accuracy': 0.25,
        'consistency': 0.20,
        'uniqueness': 0.15,
        'timeliness': 0.15
    }

    # Calculate individual scores based on passed checks
    for category, checks in validation_results.items():
        if category in scores:
            passed = sum(1 for check in checks if check.get('passed', False))
            total = len(checks)
            scores[category] = (passed / total * 100) if total > 0 else 0

    # Calculate weighted overall score
    overall_score = sum(scores[cat] * weights[cat] for cat in scores)

    return {
        'overall_score': round(overall_score, 2),
        'dimension_scores': scores,
        'weights': weights,
        'grade': get_quality_grade(overall_score)
    }

def get_quality_grade(score):
    """Assign quality grade based on score."""
    if score >= 95: return 'A'
    if score >= 85: return 'B'
    if score >= 75: return 'C'
    if score >= 60: return 'D'
    return 'F'
```

## Quality Monitoring

### Quality Trend Analysis
```python
def track_quality_metrics(df, table_name, connection):
    """Track quality metrics over time for trend analysis."""
    metrics = {
        'timestamp': pd.Timestamp.now(),
        'table_name': table_name,
        'row_count': len(df),
        'null_percentage': (df.isnull().sum().sum() / df.size) * 100,
        'duplicate_percentage': (df.duplicated().sum() / len(df)) * 100,
        'unique_values_avg': df.nunique().mean()
    }

    # Store metrics for historical tracking
    metrics_df = pd.DataFrame([metrics])
    metrics_df.to_sql(
        'data_quality_metrics',
        connection,
        if_exists='append',
        index=False
    )

    return metrics
```

### Automated Quality Alerts
```python
def check_quality_thresholds(quality_score, thresholds):
    """Check if quality metrics breach defined thresholds."""
    alerts = []

    if quality_score['overall_score'] < thresholds.get('overall_score', 80):
        alerts.append({
            'severity': 'HIGH',
            'message': f"Overall quality score {quality_score['overall_score']} below threshold",
            'threshold': thresholds['overall_score']
        })

    for dimension, score in quality_score['dimension_scores'].items():
        threshold = thresholds.get(f'{dimension}_score', 75)
        if score < threshold:
            alerts.append({
                'severity': 'MEDIUM',
                'message': f"{dimension.capitalize()} score {score} below threshold",
                'threshold': threshold
            })

    return alerts
```

## Comprehensive Quality Report

```python
def generate_quality_report(df, validation_config):
    """Generate comprehensive data quality report."""
    report = {
        'metadata': {
            'timestamp': pd.Timestamp.now(),
            'row_count': len(df),
            'column_count': len(df.columns)
        },
        'validation_results': {},
        'profile': profile_dataset(df),
        'anomalies': {},
        'quality_score': None
    }

    # Run all validations
    if 'completeness' in validation_config:
        report['validation_results']['completeness'] = [
            check_nulls(df, validation_config['completeness']['required_columns'])
        ]

    if 'accuracy' in validation_config:
        report['validation_results']['accuracy'] = [
            validate_formats(df, validation_config['accuracy'].get('format_rules', {})),
            validate_ranges(df, validation_config['accuracy'].get('range_rules', {}))
        ]

    if 'uniqueness' in validation_config:
        report['validation_results']['uniqueness'] = [
            check_duplicates(df, validation_config['uniqueness']['key_columns'])
        ]

    # Detect anomalies
    for col in df.select_dtypes(include=[np.number]).columns:
        report['anomalies'][col] = detect_outliers_iqr(df[col])

    # Calculate overall quality score
    report['quality_score'] = calculate_quality_score(report['validation_results'])

    return report
```

## Best Practices

1. **Define Clear Thresholds**: Set acceptable thresholds for each quality metric
2. **Automate Checks**: Integrate quality checks into ETL pipelines
3. **Track Trends**: Monitor quality metrics over time to detect degradation
4. **Alert on Issues**: Set up automated alerts for quality breaches
5. **Document Rules**: Clearly document all validation rules and business logic
6. **Profile Regularly**: Profile data to understand distributions and patterns
7. **Test Incrementally**: Validate data at each stage of transformation
8. **Use Statistical Methods**: Employ statistical techniques for anomaly detection
9. **Maintain Baselines**: Establish baseline metrics for comparison
10. **Report Actionably**: Provide clear, actionable quality reports

## Common Quality Issues

1. **Incomplete data**: Missing required fields, null values
2. **Invalid formats**: Emails, phone numbers, dates not matching expected patterns
3. **Out of range values**: Numbers outside expected min/max
4. **Duplicates**: Duplicate records based on business keys
5. **Referential integrity**: Orphaned foreign keys
6. **Inconsistent values**: Cross-field validation failures
7. **Stale data**: Data not updated within expected timeframe
8. **Distribution shifts**: Significant changes in value distributions
9. **Volume anomalies**: Unexpected spikes or drops in data volume
10. **Schema drift**: Data types or structures changing unexpectedly
