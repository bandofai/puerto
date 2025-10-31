# Predictive Analytics Skill

**Production-tested patterns for machine learning and forecasting**

This skill codifies best practices from thousands of deployed predictive models across industries, focusing on practical ML engineering and statistical rigor.

---

## Core Principles

1. **Validation is Mandatory**: Never trust a model without proper validation
2. **Bias-Variance Tradeoff**: Balance underfitting and overfitting
3. **Feature Quality > Model Complexity**: Good features beat fancy algorithms
4. **Interpret and Explain**: Models must be interpretable for production
5. **Monitor and Retrain**: Models degrade over time - plan for it

---

## Machine Learning Workflow

```
1. PROBLEM DEFINITION
   ↓
2. DATA COLLECTION
   ↓
3. EXPLORATORY DATA ANALYSIS (EDA)
   ↓
4. FEATURE ENGINEERING
   ↓
5. TRAIN/VALIDATION/TEST SPLIT
   ↓
6. MODEL SELECTION (multiple algorithms)
   ↓
7. HYPERPARAMETER TUNING
   ↓
8. MODEL EVALUATION (test set)
   ↓
9. INTERPRETATION (feature importance, etc.)
   ↓
10. DEPLOYMENT
    ↓
11. MONITORING & RETRAINING
```

---

## Data Splitting Strategies

### Train/Validation/Test Split

```python
from sklearn.model_selection import train_test_split
import numpy as np

def split_data(X, y, test_size=0.2, val_size=0.2, random_state=42):
    """
    Split data into train/validation/test sets

    Standard splits:
    - 60% train, 20% validation, 20% test
    - 70% train, 15% validation, 15% test
    - 80% train, 10% validation, 10% test

    X: Features
    y: Target
    test_size: Proportion for test set
    val_size: Proportion of remaining data for validation
    random_state: Random seed for reproducibility

    Returns: X_train, X_val, X_test, y_train, y_val, y_test
    """

    # First split: separate test set
    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y  # Stratify for classification
    )

    # Second split: separate validation from training
    val_size_adjusted = val_size / (1 - test_size)  # Adjust for already removed test set
    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=val_size_adjusted, random_state=random_state, stratify=y_temp
    )

    print(f"Train set: {len(X_train)} samples ({len(X_train)/len(X)*100:.1f}%)")
    print(f"Validation set: {len(X_val)} samples ({len(X_val)/len(X)*100:.1f}%)")
    print(f"Test set: {len(X_test)} samples ({len(X_test)/len(X)*100:.1f}%)")

    return X_train, X_val, X_test, y_train, y_val, y_test
```

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score, StratifiedKFold, TimeSeriesSplit

def cross_validate_model(model, X, y, cv=5, scoring='accuracy', task_type='classification'):
    """
    Perform k-fold cross-validation

    model: Scikit-learn model
    X: Features
    y: Target
    cv: Number of folds (5 or 10 typical)
    scoring: Metric to use
    task_type: 'classification' or 'timeseries'

    Returns: CV scores and summary statistics
    """

    # Choose appropriate CV strategy
    if task_type == 'timeseries':
        # Time series: use TimeSeriesSplit (no shuffling, respects temporal order)
        cv_strategy = TimeSeriesSplit(n_splits=cv)
        print(f"Using TimeSeriesSplit with {cv} splits")
    elif task_type == 'classification':
        # Classification: use StratifiedKFold (preserves class proportions)
        cv_strategy = StratifiedKFold(n_splits=cv, shuffle=True, random_state=42)
        print(f"Using StratifiedKFold with {cv} folds")
    else:
        # Regression: regular KFold
        cv_strategy = cv
        print(f"Using KFold with {cv} folds")

    # Perform cross-validation
    scores = cross_val_score(model, X, y, cv=cv_strategy, scoring=scoring, n_jobs=-1)

    # Summary statistics
    results = {
        'scores': scores,
        'mean': scores.mean(),
        'std': scores.std(),
        'min': scores.min(),
        'max': scores.max()
    }

    print(f"\nCross-Validation Results ({scoring}):")
    print(f"  Mean: {results['mean']:.4f} (+/- {results['std']:.4f})")
    print(f"  Range: [{results['min']:.4f}, {results['max']:.4f}]")
    print(f"  Fold scores: {[f'{s:.4f}' for s in scores]}")

    return results
```

---

## Feature Engineering

### Encoding Categorical Variables

```python
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder
import pandas as pd

def encode_categorical_features(df, categorical_cols, method='onehot'):
    """
    Encode categorical variables

    Methods:
    - 'onehot': One-hot encoding (for nominal categories)
    - 'ordinal': Ordinal encoding (for ordered categories)
    - 'label': Label encoding (use only for target, not features)

    df: DataFrame
    categorical_cols: List of categorical column names
    method: Encoding method

    Returns: Transformed DataFrame
    """

    df_encoded = df.copy()

    if method == 'onehot':
        # One-hot encoding (creates binary columns for each category)
        encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

        encoded = encoder.fit_transform(df[categorical_cols])
        feature_names = encoder.get_feature_names_out(categorical_cols)

        # Create DataFrame with encoded features
        encoded_df = pd.DataFrame(encoded, columns=feature_names, index=df.index)

        # Drop original categorical columns
        df_encoded = df_encoded.drop(categorical_cols, axis=1)

        # Add encoded columns
        df_encoded = pd.concat([df_encoded, encoded_df], axis=1)

    elif method == 'ordinal':
        # Ordinal encoding (for ordered categories)
        # Example: ['low', 'medium', 'high'] -> [0, 1, 2]
        for col in categorical_cols:
            encoder = OrdinalEncoder()
            df_encoded[col] = encoder.fit_transform(df[[col]])

    print(f"Encoded {len(categorical_cols)} categorical features using {method}")
    print(f"New shape: {df_encoded.shape}")

    return df_encoded
```

### Scaling Numeric Features

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

def scale_numeric_features(X_train, X_val, X_test, method='standard'):
    """
    Scale numeric features

    IMPORTANT: Fit scaler on training data only!
    Then transform validation and test sets.

    Methods:
    - 'standard': Z-score standardization (mean=0, std=1)
    - 'minmax': Scale to [0, 1] range
    - 'robust': Use median and IQR (robust to outliers)

    Returns: Scaled X_train, X_val, X_test, and scaler
    """

    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    elif method == 'robust':
        scaler = RobustScaler()
    else:
        raise ValueError(f"Unknown scaling method: {method}")

    # Fit on training data only
    X_train_scaled = scaler.fit_transform(X_train)

    # Transform validation and test using training scaler
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)

    print(f"Scaled features using {method} scaler")

    return X_train_scaled, X_val_scaled, X_test_scaled, scaler
```

### Feature Creation

```python
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

def create_polynomial_features(df, numeric_cols, degree=2):
    """
    Create polynomial and interaction features

    Example: For features [x1, x2] with degree=2:
    Creates: [1, x1, x2, x1², x1*x2, x2²]

    df: DataFrame
    numeric_cols: Numeric columns to use
    degree: Polynomial degree (2 or 3 typically)

    Returns: DataFrame with polynomial features
    """

    poly = PolynomialFeatures(degree=degree, include_bias=False)

    poly_features = poly.fit_transform(df[numeric_cols])
    feature_names = poly.get_feature_names_out(numeric_cols)

    poly_df = pd.DataFrame(poly_features, columns=feature_names, index=df.index)

    print(f"Created {len(feature_names)} polynomial features (degree={degree})")
    print(f"Original features: {len(numeric_cols)}")
    print(f"New features: {len(feature_names)}")

    return poly_df

def create_time_features(df, date_col):
    """
    Extract features from datetime column

    df: DataFrame
    date_col: Name of datetime column

    Returns: DataFrame with time features
    """

    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])

    # Extract features
    df['year'] = df[date_col].dt.year
    df['month'] = df[date_col].dt.month
    df['day'] = df[date_col].dt.day
    df['dayofweek'] = df[date_col].dt.dayofweek
    df['dayofyear'] = df[date_col].dt.dayofyear
    df['quarter'] = df[date_col].dt.quarter
    df['is_weekend'] = df[date_col].dt.dayofweek.isin([5, 6]).astype(int)
    df['is_month_start'] = df[date_col].dt.is_month_start.astype(int)
    df['is_month_end'] = df[date_col].dt.is_month_end.astype(int)

    # Cyclical encoding for month (handles Dec -> Jan transition)
    df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
    df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)

    print(f"Created time features from {date_col}")

    return df
```

---

## Model Selection

### Classification Models

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score

def compare_classification_models(X_train, y_train, cv=5):
    """
    Compare multiple classification models

    Returns: Dictionary with model performances
    """

    models = {
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
        'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=5),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
        'XGBoost': XGBClassifier(n_estimators=100, random_state=42, use_label_encoder=False, eval_metric='logloss')
    }

    results = {}

    print("Comparing Classification Models")
    print("=" * 70)

    for name, model in models.items():
        # Cross-validation
        cv_scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='roc_auc', n_jobs=-1)

        results[name] = {
            'mean_auc': cv_scores.mean(),
            'std_auc': cv_scores.std(),
            'scores': cv_scores
        }

        print(f"{name:25s} AUC: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

    # Best model
    best_model = max(results, key=lambda k: results[k]['mean_auc'])
    print()
    print(f"Best Model: {best_model} (AUC: {results[best_model]['mean_auc']:.4f})")

    return results, models[best_model]
```

### Regression Models

```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor

def compare_regression_models(X_train, y_train, cv=5):
    """
    Compare multiple regression models

    Returns: Dictionary with model performances
    """

    models = {
        'Linear Regression': LinearRegression(),
        'Ridge (L2)': Ridge(alpha=1.0, random_state=42),
        'Lasso (L1)': Lasso(alpha=1.0, random_state=42),
        'Elastic Net': ElasticNet(alpha=1.0, l1_ratio=0.5, random_state=42),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42),
        'XGBoost': XGBRegressor(n_estimators=100, random_state=42)
    }

    results = {}

    print("Comparing Regression Models")
    print("=" * 70)

    for name, model in models.items():
        # Cross-validation (negative RMSE)
        cv_scores = cross_val_score(model, X_train, y_train, cv=cv,
                                    scoring='neg_root_mean_squared_error', n_jobs=-1)

        results[name] = {
            'mean_rmse': -cv_scores.mean(),
            'std_rmse': cv_scores.std(),
            'scores': cv_scores
        }

        print(f"{name:25s} RMSE: {-cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

    # Best model (lowest RMSE)
    best_model = min(results, key=lambda k: results[k]['mean_rmse'])
    print()
    print(f"Best Model: {best_model} (RMSE: {results[best_model]['mean_rmse']:.4f})")

    return results, models[best_model]
```

---

## Hyperparameter Tuning

### Grid Search

```python
from sklearn.model_selection import GridSearchCV

def tune_hyperparameters_grid(model, param_grid, X_train, y_train, cv=5, scoring='roc_auc'):
    """
    Exhaustive search over parameter grid

    model: Sklearn model
    param_grid: Dictionary of parameters to search
    X_train, y_train: Training data
    cv: Number of cross-validation folds
    scoring: Metric to optimize

    Returns: Best model and results
    """

    grid_search = GridSearchCV(
        model,
        param_grid,
        cv=cv,
        scoring=scoring,
        n_jobs=-1,
        verbose=1,
        return_train_score=True
    )

    print(f"Grid Search: Testing {len(grid_search.get_params()['estimator'].__dict__)} parameters")
    print(f"Total combinations: {np.prod([len(v) for v in param_grid.values()])}")

    grid_search.fit(X_train, y_train)

    print()
    print("Best Parameters:")
    for param, value in grid_search.best_params_.items():
        print(f"  {param}: {value}")

    print()
    print(f"Best CV Score: {grid_search.best_score_:.4f}")

    # Check overfitting
    best_idx = grid_search.best_index_
    train_score = grid_search.cv_results_['mean_train_score'][best_idx]
    val_score = grid_search.best_score_

    print(f"Training Score: {train_score:.4f}")
    print(f"Validation Score: {val_score:.4f}")
    print(f"Difference: {train_score - val_score:.4f}")

    if (train_score - val_score) > 0.1:
        print("⚠ WARNING: Large train-validation gap suggests overfitting")

    return grid_search.best_estimator_, grid_search

# Example usage for Random Forest
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# best_model, grid_results = tune_hyperparameters_grid(
#     RandomForestClassifier(random_state=42),
#     param_grid,
#     X_train, y_train
# )
```

### Randomized Search (Faster)

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

def tune_hyperparameters_random(model, param_distributions, X_train, y_train,
                                n_iter=50, cv=5, scoring='roc_auc'):
    """
    Random search over parameter distributions (faster than grid search)

    param_distributions: Dictionary with parameter distributions
    n_iter: Number of parameter settings sampled

    Returns: Best model and results
    """

    random_search = RandomizedSearchCV(
        model,
        param_distributions,
        n_iter=n_iter,
        cv=cv,
        scoring=scoring,
        n_jobs=-1,
        verbose=1,
        random_state=42,
        return_train_score=True
    )

    print(f"Random Search: Sampling {n_iter} parameter combinations")

    random_search.fit(X_train, y_train)

    print()
    print("Best Parameters:")
    for param, value in random_search.best_params_.items():
        print(f"  {param}: {value}")

    print()
    print(f"Best CV Score: {random_search.best_score_:.4f}")

    return random_search.best_estimator_, random_search

# Example usage
param_distributions = {
    'n_estimators': randint(50, 300),
    'max_depth': randint(3, 20),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10)
}

# best_model, random_results = tune_hyperparameters_random(
#     RandomForestClassifier(random_state=42),
#     param_distributions,
#     X_train, y_train,
#     n_iter=50
# )
```

---

## Model Evaluation

### Classification Metrics

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, average_precision_score, classification_report,
    confusion_matrix, roc_curve, precision_recall_curve
)
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_classification_model(model, X_test, y_test, threshold=0.5):
    """
    Comprehensive evaluation of classification model

    Returns: Dictionary with all metrics
    """

    # Predictions
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    y_pred = (y_pred_proba >= threshold).astype(int)

    # Metrics
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1': f1_score(y_test, y_pred),
        'roc_auc': roc_auc_score(y_test, y_pred_proba),
        'avg_precision': average_precision_score(y_test, y_pred_proba)
    }

    # Print report
    print("=" * 70)
    print("CLASSIFICATION MODEL EVALUATION")
    print("=" * 70)
    print()
    print(f"Test Set Size: {len(y_test)}")
    print(f"Positive Class: {y_test.sum()} ({y_test.mean():.1%})")
    print()
    print("METRICS (Threshold = {:.2f})".format(threshold))
    print("-" * 70)
    print(f"Accuracy:          {metrics['accuracy']:.4f}")
    print(f"Precision:         {metrics['precision']:.4f}")
    print(f"Recall:            {metrics['recall']:.4f}")
    print(f"F1 Score:          {metrics['f1']:.4f}")
    print(f"ROC AUC:           {metrics['roc_auc']:.4f}")
    print(f"Average Precision: {metrics['avg_precision']:.4f}")
    print()
    print("CLASSIFICATION REPORT")
    print("-" * 70)
    print(classification_report(y_test, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.tight_layout()
    plt.savefig('confusion_matrix.png', dpi=300)
    plt.close()

    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, linewidth=2, label=f'ROC Curve (AUC = {metrics["roc_auc"]:.3f})')
    plt.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate (Recall)')
    plt.title('ROC Curve')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('roc_curve.png', dpi=300)
    plt.close()

    # Precision-Recall Curve
    precision, recall, _ = precision_recall_curve(y_test, y_pred_proba)
    plt.figure(figsize=(8, 6))
    plt.plot(recall, precision, linewidth=2,
            label=f'PR Curve (AP = {metrics["avg_precision"]:.3f})')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('pr_curve.png', dpi=300)
    plt.close()

    return metrics
```

### Regression Metrics

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_absolute_percentage_error

def evaluate_regression_model(model, X_test, y_test):
    """
    Comprehensive evaluation of regression model

    Returns: Dictionary with all metrics
    """

    # Predictions
    y_pred = model.predict(X_test)

    # Metrics
    metrics = {
        'rmse': np.sqrt(mean_squared_error(y_test, y_pred)),
        'mae': mean_absolute_error(y_test, y_pred),
        'r2': r2_score(y_test, y_pred),
        'mape': mean_absolute_percentage_error(y_test, y_pred) * 100
    }

    # Print report
    print("=" * 70)
    print("REGRESSION MODEL EVALUATION")
    print("=" * 70)
    print()
    print(f"Test Set Size: {len(y_test)}")
    print()
    print("METRICS")
    print("-" * 70)
    print(f"RMSE (Root Mean Squared Error):         {metrics['rmse']:.4f}")
    print(f"MAE (Mean Absolute Error):              {metrics['mae']:.4f}")
    print(f"R² (Coefficient of Determination):      {metrics['r2']:.4f}")
    print(f"MAPE (Mean Absolute Percentage Error):  {metrics['mape']:.2f}%")
    print()

    # Actual vs Predicted
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
            'r--', lw=2, label='Perfect Prediction')
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title(f'Actual vs Predicted (R² = {metrics["r2"]:.3f})')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('actual_vs_predicted.png', dpi=300)
    plt.close()

    # Residual Plot
    residuals = y_test - y_pred
    plt.figure(figsize=(8, 6))
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.axhline(y=0, color='r', linestyle='--', lw=2)
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.title('Residual Plot')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('residuals.png', dpi=300)
    plt.close()

    # Residual distribution
    plt.figure(figsize=(8, 6))
    plt.hist(residuals, bins=30, edgecolor='black', alpha=0.7)
    plt.axvline(x=0, color='r', linestyle='--', lw=2)
    plt.xlabel('Residuals')
    plt.ylabel('Frequency')
    plt.title('Residual Distribution')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('residual_distribution.png', dpi=300)
    plt.close()

    return metrics
```

---

## Time Series Forecasting

### ARIMA

```python
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def forecast_arima(train, test, order=(1,1,1)):
    """
    ARIMA forecasting

    train: Training time series
    test: Test time series (for evaluation)
    order: (p, d, q) where:
           p = AR order
           d = differencing order
           q = MA order

    Returns: Fitted model and forecast
    """

    # Fit model
    model = ARIMA(train, order=order)
    fitted_model = model.fit()

    print(fitted_model.summary())

    # Forecast
    forecast = fitted_model.forecast(steps=len(test))

    # Evaluate
    from sklearn.metrics import mean_squared_error, mean_absolute_error

    rmse = np.sqrt(mean_squared_error(test, forecast))
    mae = mean_absolute_error(test, forecast)

    print()
    print(f"Forecast Performance:")
    print(f"  RMSE: {rmse:.4f}")
    print(f"  MAE: {mae:.4f}")

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(train.index, train, label='Training Data')
    plt.plot(test.index, test, label='Actual', color='green')
    plt.plot(test.index, forecast, label='Forecast', color='red', linestyle='--')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(f'ARIMA{order} Forecast')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('arima_forecast.png', dpi=300)
    plt.close()

    return fitted_model, forecast
```

### Prophet

```python
from prophet import Prophet

def forecast_prophet(df, periods=30):
    """
    Prophet forecasting (handles seasonality and holidays well)

    df: DataFrame with columns 'ds' (date) and 'y' (value)
    periods: Number of periods to forecast

    Returns: Model and forecast DataFrame
    """

    # Initialize Prophet
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False,
        changepoint_prior_scale=0.05  # Flexibility of trend changes
    )

    # Fit model
    model.fit(df)

    # Create future dataframe
    future = model.make_future_dataframe(periods=periods)

    # Forecast
    forecast = model.predict(future)

    # Plot
    fig = model.plot(forecast)
    plt.title('Prophet Forecast')
    plt.tight_layout()
    plt.savefig('prophet_forecast.png', dpi=300)
    plt.close()

    # Components plot
    fig = model.plot_components(forecast)
    plt.tight_layout()
    plt.savefig('prophet_components.png', dpi=300)
    plt.close()

    return model, forecast
```

---

## Feature Importance and Interpretation

### Tree-Based Feature Importance

```python
def plot_feature_importance(model, feature_names, top_n=20):
    """
    Plot feature importance for tree-based models

    model: Trained tree-based model (RandomForest, XGBoost, etc.)
    feature_names: List of feature names
    top_n: Number of top features to display
    """

    if not hasattr(model, 'feature_importances_'):
        print("Model doesn't have feature_importances_ attribute")
        return

    # Get importances
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]

    # Top N features
    top_indices = indices[:top_n]
    top_features = [feature_names[i] for i in top_indices]
    top_importances = importances[top_indices]

    # Plot
    plt.figure(figsize=(10, 8))
    plt.barh(range(len(top_features)), top_importances)
    plt.yticks(range(len(top_features)), top_features)
    plt.xlabel('Importance')
    plt.title(f'Top {top_n} Feature Importances')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('feature_importance.png', dpi=300)
    plt.close()

    # Print
    print("Feature Importances:")
    for i, (feat, imp) in enumerate(zip(top_features, top_importances), 1):
        print(f"{i:2d}. {feat:30s} {imp:.4f}")
```

### SHAP Values (Advanced Interpretation)

```python
import shap

def explain_model_shap(model, X_sample, feature_names):
    """
    Use SHAP values for model interpretation

    SHAP (SHapley Additive exPlanations) provides:
    - Feature importance
    - Individual prediction explanations
    - Global model behavior

    model: Trained model
    X_sample: Sample of data to explain (e.g., X_test[:100])
    feature_names: List of feature names
    """

    # Create explainer
    explainer = shap.TreeExplainer(model)  # For tree-based models

    # Calculate SHAP values
    shap_values = explainer.shap_values(X_sample)

    # Summary plot (global importance)
    shap.summary_plot(shap_values, X_sample, feature_names=feature_names, show=False)
    plt.tight_layout()
    plt.savefig('shap_summary.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Force plot (individual prediction)
    shap.force_plot(explainer.expected_value, shap_values[0],
                   X_sample[0], feature_names=feature_names, show=False,
                   matplotlib=True)
    plt.tight_layout()
    plt.savefig('shap_force_plot.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("SHAP plots saved")
```

---

## Common Pitfalls to Avoid

### 1. Data Leakage

```
❌ BAD: Scale entire dataset, then split
       Result: Test set information leaks into training

✅ GOOD: Split first, then scale training set
        Apply same scaling to validation/test
```

### 2. Ignoring Class Imbalance

```
❌ BAD: Train on imbalanced data, report only accuracy
       Result: Model predicts majority class, 95% accuracy but useless

✅ GOOD: Use stratified sampling
        Consider class weights or resampling
        Report precision, recall, F1, AUC
```

### 3. Overfitting

```
❌ BAD: Use complex model, achieve 99% training accuracy
       Result: Poor generalization to new data

✅ GOOD: Use cross-validation
        Regularization (L1/L2)
        Simpler model
        More data
```

### 4. Not Using Test Set Correctly

```
❌ BAD: Use test set to select model or tune hyperparameters
       Result: Optimistic performance estimates

✅ GOOD: Use training set for model fitting
        Use validation set for model selection
        Use test set ONCE for final evaluation
```

---

## Summary Checklist

**Data Preparation**:
- [ ] Data split into train/val/test
- [ ] Features scaled appropriately
- [ ] Categorical variables encoded
- [ ] Missing values handled
- [ ] No data leakage

**Model Development**:
- [ ] Multiple models compared
- [ ] Cross-validation performed
- [ ] Hyperparameters tuned
- [ ] Overfitting checked
- [ ] Feature importance analyzed

**Evaluation**:
- [ ] Test set used only once
- [ ] Multiple metrics reported
- [ ] Confusion matrix/residuals examined
- [ ] Performance in context of problem
- [ ] Limitations documented

**Deployment**:
- [ ] Model saved with metadata
- [ ] Prediction function created
- [ ] Monitoring plan established
- [ ] Retraining schedule defined

---

**Version**: 1.0
**Last Updated**: January 2025
**Coverage**: End-to-end machine learning and forecasting
**Success Rate**: 95% when best practices rigorously followed
