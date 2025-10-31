"""
Data Quality Checks Template
Comprehensive data validation suite for automated quality monitoring.
"""

import pandas as pd
import numpy as np
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional
import re

# ============================================
# LOGGING SETUP
# ============================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('data_quality_checks')

# ============================================
# VALIDATION FUNCTIONS
# ============================================

class DataQualityChecker:
    """Comprehensive data quality validation suite."""

    def __init__(self, df: pd.DataFrame, table_name: str):
        """
        Initialize quality checker.

        Args:
            df: DataFrame to validate
            table_name: Name of the table being validated
        """
        self.df = df
        self.table_name = table_name
        self.results = {
            'table_name': table_name,
            'timestamp': datetime.now(),
            'row_count': len(df),
            'column_count': len(df.columns),
            'checks': {}
        }

    # ============================================
    # COMPLETENESS CHECKS
    # ============================================

    def check_nulls(self, required_columns: List[str]) -> Dict[str, Any]:
        """Check for null values in required columns."""
        logger.info("Running null value checks...")

        results = {}
        for col in required_columns:
            if col not in self.df.columns:
                results[col] = {
                    'status': 'ERROR',
                    'message': f'Column {col} not found in dataframe'
                }
                continue

            null_count = self.df[col].isnull().sum()
            null_pct = (null_count / len(self.df)) * 100

            results[col] = {
                'null_count': null_count,
                'null_percentage': round(null_pct, 2),
                'passed': null_count == 0,
                'severity': 'HIGH' if null_count > 0 else 'NONE'
            }

        self.results['checks']['null_checks'] = results
        return results

    def check_completeness_score(self) -> Dict[str, Any]:
        """Calculate overall completeness score."""
        logger.info("Calculating completeness score...")

        total_cells = self.df.size
        null_cells = self.df.isnull().sum().sum()
        completeness = ((total_cells - null_cells) / total_cells) * 100

        result = {
            'total_cells': total_cells,
            'null_cells': null_cells,
            'completeness_percentage': round(completeness, 2),
            'passed': completeness >= 95,
            'threshold': 95
        }

        self.results['checks']['completeness_score'] = result
        return result

    # ============================================
    # ACCURACY CHECKS
    # ============================================

    def check_data_types(self, expected_types: Dict[str, str]) -> Dict[str, Any]:
        """Validate column data types."""
        logger.info("Validating data types...")

        results = {}
        for col, expected_type in expected_types.items():
            if col not in self.df.columns:
                results[col] = {
                    'status': 'ERROR',
                    'message': f'Column {col} not found'
                }
                continue

            actual_type = str(self.df[col].dtype)
            passed = actual_type == expected_type or (
                expected_type in ['int64', 'float64'] and actual_type in ['int64', 'float64']
            )

            results[col] = {
                'expected_type': expected_type,
                'actual_type': actual_type,
                'passed': passed,
                'severity': 'MEDIUM' if not passed else 'NONE'
            }

        self.results['checks']['data_type_checks'] = results
        return results

    def check_formats(self, format_rules: Dict[str, str]) -> Dict[str, Any]:
        """Validate data formats using regex patterns."""
        logger.info("Validating data formats...")

        patterns = {
            'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            'phone': r'^\+?1?\d{9,15}$',
            'zipcode': r'^\d{5}(-\d{4})?$',
            'ssn': r'^\d{3}-\d{2}-\d{4}$',
            'url': r'^https?://[^\s]+$',
            'ipv4': r'^(\d{1,3}\.){3}\d{1,3}$',
            'uuid': r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        }

        results = {}
        for col, format_type in format_rules.items():
            if col not in self.df.columns:
                continue

            pattern = patterns.get(format_type)
            if pattern:
                valid_mask = self.df[col].astype(str).str.match(pattern, na=False)
                invalid_count = (~valid_mask & self.df[col].notna()).sum()
                invalid_pct = (invalid_count / len(self.df)) * 100

                results[col] = {
                    'format': format_type,
                    'invalid_count': invalid_count,
                    'invalid_percentage': round(invalid_pct, 2),
                    'passed': invalid_count == 0,
                    'severity': 'HIGH' if invalid_pct > 5 else ('MEDIUM' if invalid_pct > 0 else 'NONE')
                }

        self.results['checks']['format_checks'] = results
        return results

    def check_ranges(self, range_rules: Dict[str, tuple]) -> Dict[str, Any]:
        """Validate numeric values are within expected ranges."""
        logger.info("Validating value ranges...")

        results = {}
        for col, (min_val, max_val) in range_rules.items():
            if col not in self.df.columns:
                continue

            out_of_range = self.df[
                (self.df[col] < min_val) | (self.df[col] > max_val)
            ][col].count()

            out_of_range_pct = (out_of_range / len(self.df)) * 100

            results[col] = {
                'min_expected': min_val,
                'max_expected': max_val,
                'min_actual': float(self.df[col].min()),
                'max_actual': float(self.df[col].max()),
                'out_of_range_count': out_of_range,
                'out_of_range_percentage': round(out_of_range_pct, 2),
                'passed': out_of_range == 0,
                'severity': 'HIGH' if out_of_range_pct > 5 else ('MEDIUM' if out_of_range > 0 else 'NONE')
            }

        self.results['checks']['range_checks'] = results
        return results

    # ============================================
    # CONSISTENCY CHECKS
    # ============================================

    def check_referential_integrity(
        self,
        reference_df: pd.DataFrame,
        fk_col: str,
        pk_col: str
    ) -> Dict[str, Any]:
        """Check foreign key relationships."""
        logger.info(f"Checking referential integrity for {fk_col}...")

        if fk_col not in self.df.columns:
            return {'status': 'ERROR', 'message': f'Column {fk_col} not found'}

        orphaned_records = self.df[~self.df[fk_col].isin(reference_df[pk_col])]
        orphaned_count = len(orphaned_records)
        orphaned_pct = (orphaned_count / len(self.df)) * 100

        result = {
            'foreign_key': fk_col,
            'primary_key': pk_col,
            'total_records': len(self.df),
            'orphaned_records': orphaned_count,
            'orphaned_percentage': round(orphaned_pct, 2),
            'passed': orphaned_count == 0,
            'severity': 'HIGH' if orphaned_count > 0 else 'NONE',
            'orphaned_keys': orphaned_records[fk_col].unique().tolist()[:10]  # Limit to 10
        }

        self.results['checks']['referential_integrity'] = result
        return result

    def check_cross_field_validation(self, rules: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Validate relationships between fields."""
        logger.info("Validating cross-field rules...")

        results = {}

        for rule in rules:
            rule_name = rule['name']
            rule_expr = rule['expression']

            try:
                # Evaluate rule expression
                invalid = self.df.query(f"not ({rule_expr})")
                invalid_count = len(invalid)
                invalid_pct = (invalid_count / len(self.df)) * 100

                results[rule_name] = {
                    'rule': rule_expr,
                    'invalid_count': invalid_count,
                    'invalid_percentage': round(invalid_pct, 2),
                    'passed': invalid_count == 0,
                    'severity': rule.get('severity', 'MEDIUM')
                }

            except Exception as e:
                results[rule_name] = {
                    'status': 'ERROR',
                    'message': f'Rule evaluation failed: {e}'
                }

        self.results['checks']['cross_field_validation'] = results
        return results

    # ============================================
    # UNIQUENESS CHECKS
    # ============================================

    def check_duplicates(self, key_columns: List[str]) -> Dict[str, Any]:
        """Check for duplicate records based on key columns."""
        logger.info(f"Checking duplicates on {key_columns}...")

        duplicates = self.df[self.df.duplicated(subset=key_columns, keep=False)]
        duplicate_count = len(duplicates)
        duplicate_pct = (duplicate_count / len(self.df)) * 100

        result = {
            'key_columns': key_columns,
            'total_records': len(self.df),
            'duplicate_records': duplicate_count,
            'duplicate_percentage': round(duplicate_pct, 2),
            'passed': duplicate_count == 0,
            'severity': 'HIGH' if duplicate_count > 0 else 'NONE'
        }

        self.results['checks']['duplicate_check'] = result
        return result

    def check_primary_key(self, pk_columns: List[str]) -> Dict[str, Any]:
        """Validate primary key uniqueness and non-null."""
        logger.info(f"Validating primary key: {pk_columns}...")

        # Check for nulls
        null_count = self.df[pk_columns].isnull().any(axis=1).sum()

        # Check for duplicates
        dup_count = self.df.duplicated(subset=pk_columns).sum()

        result = {
            'primary_key_columns': pk_columns,
            'null_count': null_count,
            'duplicate_count': dup_count,
            'passed': null_count == 0 and dup_count == 0,
            'severity': 'CRITICAL' if (null_count > 0 or dup_count > 0) else 'NONE'
        }

        self.results['checks']['primary_key_check'] = result
        return result

    # ============================================
    # TIMELINESS CHECKS
    # ============================================

    def check_data_freshness(
        self,
        timestamp_col: str,
        max_age_hours: int = 24
    ) -> Dict[str, Any]:
        """Check if data is fresh (recently updated)."""
        logger.info("Checking data freshness...")

        if timestamp_col not in self.df.columns:
            return {'status': 'ERROR', 'message': f'Column {timestamp_col} not found'}

        latest_timestamp = pd.to_datetime(self.df[timestamp_col]).max()
        age_hours = (pd.Timestamp.now() - latest_timestamp).total_seconds() / 3600

        result = {
            'timestamp_column': timestamp_col,
            'latest_timestamp': str(latest_timestamp),
            'age_hours': round(age_hours, 2),
            'max_age_hours': max_age_hours,
            'passed': age_hours <= max_age_hours,
            'severity': 'HIGH' if age_hours > max_age_hours else 'NONE',
            'status': 'fresh' if age_hours <= max_age_hours else 'stale'
        }

        self.results['checks']['freshness_check'] = result
        return result

    # ============================================
    # ANOMALY DETECTION
    # ============================================

    def detect_outliers_iqr(self, columns: List[str]) -> Dict[str, Any]:
        """Detect outliers using Interquartile Range (IQR) method."""
        logger.info("Detecting outliers using IQR method...")

        results = {}
        for col in columns:
            if col not in self.df.columns or not pd.api.types.is_numeric_dtype(self.df[col]):
                continue

            series = self.df[col].dropna()
            Q1 = series.quantile(0.25)
            Q3 = series.quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            outliers = series[(series < lower_bound) | (series > upper_bound)]
            outlier_pct = (len(outliers) / len(series)) * 100

            results[col] = {
                'method': 'IQR',
                'lower_bound': float(lower_bound),
                'upper_bound': float(upper_bound),
                'outlier_count': len(outliers),
                'outlier_percentage': round(outlier_pct, 2),
                'severity': 'MEDIUM' if outlier_pct > 5 else 'LOW'
            }

        self.results['checks']['outlier_detection'] = results
        return results

    # ============================================
    # DATA PROFILING
    # ============================================

    def profile_dataset(self) -> Dict[str, Any]:
        """Generate comprehensive dataset profile."""
        logger.info("Profiling dataset...")

        profile = {
            'row_count': len(self.df),
            'column_count': len(self.df.columns),
            'memory_usage_mb': round(self.df.memory_usage(deep=True).sum() / (1024**2), 2),
            'columns': {}
        }

        for col in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[col]):
                profile['columns'][col] = {
                    'type': 'numeric',
                    'count': int(self.df[col].count()),
                    'null_count': int(self.df[col].isnull().sum()),
                    'null_percentage': round((self.df[col].isnull().sum() / len(self.df)) * 100, 2),
                    'mean': float(self.df[col].mean()),
                    'median': float(self.df[col].median()),
                    'std': float(self.df[col].std()),
                    'min': float(self.df[col].min()),
                    'max': float(self.df[col].max()),
                    'unique_count': int(self.df[col].nunique())
                }
            else:
                value_counts = self.df[col].value_counts()
                profile['columns'][col] = {
                    'type': 'categorical',
                    'count': int(self.df[col].count()),
                    'null_count': int(self.df[col].isnull().sum()),
                    'null_percentage': round((self.df[col].isnull().sum() / len(self.df)) * 100, 2),
                    'unique_count': int(self.df[col].nunique()),
                    'top_values': value_counts.head(5).to_dict()
                }

        self.results['profile'] = profile
        return profile

    # ============================================
    # QUALITY SCORE
    # ============================================

    def calculate_quality_score(self) -> Dict[str, Any]:
        """Calculate overall data quality score."""
        logger.info("Calculating quality score...")

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

        # Calculate dimension scores based on passed checks
        checks = self.results.get('checks', {})

        # Completeness
        if 'null_checks' in checks:
            passed = sum(1 for check in checks['null_checks'].values() if check.get('passed', False))
            total = len(checks['null_checks'])
            scores['completeness'] = (passed / total * 100) if total > 0 else 100

        # Accuracy
        accuracy_checks = ['data_type_checks', 'format_checks', 'range_checks']
        accuracy_passed = 0
        accuracy_total = 0
        for check_type in accuracy_checks:
            if check_type in checks:
                accuracy_passed += sum(1 for c in checks[check_type].values() if c.get('passed', False))
                accuracy_total += len(checks[check_type])
        scores['accuracy'] = (accuracy_passed / accuracy_total * 100) if accuracy_total > 0 else 100

        # Uniqueness
        if 'duplicate_check' in checks:
            scores['uniqueness'] = 100 if checks['duplicate_check'].get('passed', False) else 0

        # Calculate weighted overall score
        overall_score = sum(scores[dim] * weights[dim] for dim in scores)

        quality_score = {
            'overall_score': round(overall_score, 2),
            'dimension_scores': scores,
            'weights': weights,
            'grade': self._get_quality_grade(overall_score)
        }

        self.results['quality_score'] = quality_score
        return quality_score

    def _get_quality_grade(self, score: float) -> str:
        """Assign quality grade based on score."""
        if score >= 95: return 'A'
        if score >= 85: return 'B'
        if score >= 75: return 'C'
        if score >= 60: return 'D'
        return 'F'

    # ============================================
    # REPORT GENERATION
    # ============================================

    def generate_report(self) -> Dict[str, Any]:
        """Generate comprehensive quality report."""
        logger.info("Generating quality report...")

        # Calculate quality score if not already done
        if 'quality_score' not in self.results:
            self.calculate_quality_score()

        return self.results

    def print_summary(self):
        """Print quality check summary."""
        print("\n" + "=" * 60)
        print(f"DATA QUALITY REPORT: {self.table_name}")
        print("=" * 60)
        print(f"Timestamp: {self.results['timestamp']}")
        print(f"Row Count: {self.results['row_count']}")
        print(f"Column Count: {self.results['column_count']}")
        print("-" * 60)

        if 'quality_score' in self.results:
            qs = self.results['quality_score']
            print(f"Overall Quality Score: {qs['overall_score']}/100 (Grade: {qs['grade']})")
            print("\nDimension Scores:")
            for dim, score in qs['dimension_scores'].items():
                print(f"  {dim.capitalize()}: {score:.2f}")

        print("-" * 60)
        print(f"Total Checks Run: {len(self.results.get('checks', {}))}")
        print("=" * 60 + "\n")

# ============================================
# EXAMPLE USAGE
# ============================================

if __name__ == "__main__":
    # Sample data
    df = pd.DataFrame({
        'customer_id': [1, 2, 3, 4, 5],
        'email': ['john@example.com', 'jane@example.com', 'invalid-email', 'bob@example.com', 'alice@example.com'],
        'age': [25, 30, 35, 200, 45],  # 200 is outlier
        'created_at': pd.date_range('2024-01-01', periods=5),
        'updated_at': pd.date_range('2024-01-01', periods=5)
    })

    # Initialize checker
    checker = DataQualityChecker(df, 'customers')

    # Run checks
    checker.check_nulls(['customer_id', 'email'])
    checker.check_formats({'email': 'email'})
    checker.check_ranges({'age': (0, 120)})
    checker.check_duplicates(['customer_id'])
    checker.check_data_freshness('updated_at', max_age_hours=24)
    checker.detect_outliers_iqr(['age'])
    checker.profile_dataset()
    checker.calculate_quality_score()

    # Generate report
    report = checker.generate_report()
    checker.print_summary()
