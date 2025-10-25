# Feature Engineering Skill

Comprehensive techniques for feature creation, transformation, selection, and engineering for machine learning.

## Feature Creation

### Temporal Features
```python
import pandas as pd
import numpy as np

def extract_datetime_features(df, date_column):
    """Extract comprehensive features from datetime column"""

    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column])

    # Basic temporal features
    df['year'] = df[date_column].dt.year
    df['month'] = df[date_column].dt.month
    df['day'] = df[date_column].dt.day
    df['day_of_week'] = df[date_column].dt.dayofweek
    df['day_of_year'] = df[date_column].dt.dayofyear
    df['week_of_year'] = df[date_column].dt.isocalendar().week
    df['quarter'] = df[date_column].dt.quarter

    # Advanced temporal features
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    df['is_month_start'] = df[date_column].dt.is_month_start.astype(int)
    df['is_month_end'] = df[date_column].dt.is_month_end.astype(int)
    df['is_quarter_start'] = df[date_column].dt.is_quarter_start.astype(int)
    df['is_quarter_end'] = df[date_column].dt.is_quarter_end.astype(int)

    # Time-based features
    df['hour'] = df[date_column].dt.hour
    df['minute'] = df[date_column].dt.minute

    # Cyclical encoding (for periodic features)
    df['day_of_week_sin'] = np.sin(2 * np.pi * df['day_of_week'] / 7)
    df['day_of_week_cos'] = np.cos(2 * np.pi * df['day_of_week'] / 7)
    df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
    df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)

    return df
```

### Interaction Features
```python
def create_interaction_features(df, feature_pairs):
    """Create interaction features between feature pairs"""

    df = df.copy()

    for feat1, feat2 in feature_pairs:
        # Multiplication
        df[f'{feat1}_x_{feat2}'] = df[feat1] * df[feat2]

        # Division (with safety)
        df[f'{feat1}_div_{feat2}'] = df[feat1] / (df[feat2] + 1e-8)
        df[f'{feat2}_div_{feat1}'] = df[feat2] / (df[feat1] + 1e-8)

        # Addition
        df[f'{feat1}_plus_{feat2}'] = df[feat1] + df[feat2]

        # Subtraction
        df[f'{feat1}_minus_{feat2}'] = df[feat1] - df[feat2]

    return df

# Example usage
feature_pairs = [('age', 'income'), ('hours_worked', 'rate')]
df = create_interaction_features(df, feature_pairs)
```

### Aggregation Features
```python
def create_aggregation_features(df, group_columns, agg_columns, agg_funcs=['mean', 'sum', 'std', 'min', 'max']):
    """Create aggregation features grouped by specified columns"""

    df = df.copy()

    for group_col in group_columns:
        for agg_col in agg_columns:
            for func in agg_funcs:
                feature_name = f'{group_col}_{agg_col}_{func}'

                # Calculate aggregation
                agg_values = df.groupby(group_col)[agg_col].transform(func)
                df[feature_name] = agg_values

    return df

# Example: Customer-level aggregations
df = create_aggregation_features(
    df,
    group_columns=['customer_id'],
    agg_columns=['purchase_amount', 'quantity'],
    agg_funcs=['mean', 'sum', 'std', 'count']
)
```

### Polynomial Features
```python
from sklearn.preprocessing import PolynomialFeatures

def create_polynomial_features(X, degree=2, include_bias=False):
    """Create polynomial and interaction features"""

    poly = PolynomialFeatures(degree=degree, include_bias=include_bias)
    X_poly = poly.fit_transform(X)

    # Get feature names
    feature_names = poly.get_feature_names_out()

    return X_poly, feature_names, poly

# Usage
X_poly, poly_names, poly_transformer = create_polynomial_features(X_train[['age', 'income']], degree=2)
```

### Mathematical Transformations
```python
def create_math_transformations(df, columns):
    """Apply mathematical transformations to create new features"""

    df = df.copy()

    for col in columns:
        # Square
        df[f'{col}_squared'] = df[col] ** 2

        # Cube
        df[f'{col}_cubed'] = df[col] ** 3

        # Square root (handle negatives)
        df[f'{col}_sqrt'] = np.sqrt(np.abs(df[col]))

        # Log transformation (handle zeros and negatives)
        df[f'{col}_log'] = np.log1p(np.abs(df[col]))

        # Reciprocal (with safety)
        df[f'{col}_reciprocal'] = 1 / (df[col] + 1e-8)

        # Exponential (clip for safety)
        df[f'{col}_exp'] = np.exp(np.clip(df[col], -10, 10))

    return df
```

## Feature Encoding

### One-Hot Encoding
```python
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def one_hot_encode(df, columns, drop_first=False):
    """One-hot encode categorical variables"""

    encoder = OneHotEncoder(
        sparse_output=False,
        drop='first' if drop_first else None,
        handle_unknown='ignore'
    )

    # Encode
    encoded = encoder.fit_transform(df[columns])

    # Get feature names
    feature_names = encoder.get_feature_names_out(columns)

    # Create DataFrame
    encoded_df = pd.DataFrame(encoded, columns=feature_names, index=df.index)

    # Drop original columns and concatenate encoded ones
    df = df.drop(columns=columns)
    df = pd.concat([df, encoded_df], axis=1)

    return df, encoder
```

### Label Encoding
```python
from sklearn.preprocessing import LabelEncoder

def label_encode(df, columns):
    """Label encode categorical variables"""

    df = df.copy()
    encoders = {}

    for col in columns:
        encoder = LabelEncoder()
        df[f'{col}_encoded'] = encoder.fit_transform(df[col].astype(str))
        encoders[col] = encoder

    return df, encoders
```

### Target Encoding
```python
def target_encode(X_train, X_test, y_train, categorical_cols, smoothing=1.0):
    """
    Target encoding with smoothing to prevent overfitting
    Also known as mean encoding
    """

    X_train = X_train.copy()
    X_test = X_test.copy()

    global_mean = y_train.mean()

    for col in categorical_cols:
        # Calculate statistics per category
        agg = pd.DataFrame({
            'target_mean': X_train.groupby(col)[y_train.name].mean(),
            'count': X_train.groupby(col)[y_train.name].count()
        })

        # Apply smoothing: (count * mean + smoothing * global_mean) / (count + smoothing)
        agg['target_encoded'] = (
            (agg['count'] * agg['target_mean'] + smoothing * global_mean) /
            (agg['count'] + smoothing)
        )

        # Map to train and test
        X_train[f'{col}_target_enc'] = X_train[col].map(agg['target_encoded']).fillna(global_mean)
        X_test[f'{col}_target_enc'] = X_test[col].map(agg['target_encoded']).fillna(global_mean)

    return X_train, X_test

# Usage
X_train_encoded, X_test_encoded = target_encode(
    X_train, X_test, y_train,
    categorical_cols=['category', 'region'],
    smoothing=10.0
)
```

### Frequency Encoding
```python
def frequency_encode(X_train, X_test, columns):
    """Encode categories by their frequency"""

    X_train = X_train.copy()
    X_test = X_test.copy()

    for col in columns:
        # Calculate frequencies
        freq = X_train[col].value_counts(normalize=True).to_dict()

        # Map frequencies
        X_train[f'{col}_freq'] = X_train[col].map(freq).fillna(0)
        X_test[f'{col}_freq'] = X_test[col].map(freq).fillna(0)

    return X_train, X_test
```

### Ordinal Encoding
```python
from sklearn.preprocessing import OrdinalEncoder

def ordinal_encode(df, column, categories):
    """Encode ordinal categorical variables with specified order"""

    encoder = OrdinalEncoder(categories=[categories])
    df[f'{column}_ordinal'] = encoder.fit_transform(df[[column]])

    return df, encoder

# Example: Education level
df, encoder = ordinal_encode(
    df,
    column='education',
    categories=['High School', 'Bachelor', 'Master', 'PhD']
)
```

## Feature Scaling

### Standard Scaling
```python
from sklearn.preprocessing import StandardScaler

def standard_scale(X_train, X_test, columns):
    """Standardize features to zero mean and unit variance"""

    scaler = StandardScaler()

    X_train_scaled = X_train.copy()
    X_test_scaled = X_test.copy()

    X_train_scaled[columns] = scaler.fit_transform(X_train[columns])
    X_test_scaled[columns] = scaler.transform(X_test[columns])

    return X_train_scaled, X_test_scaled, scaler
```

### Min-Max Scaling
```python
from sklearn.preprocessing import MinMaxScaler

def minmax_scale(X_train, X_test, columns, feature_range=(0, 1)):
    """Scale features to a given range"""

    scaler = MinMaxScaler(feature_range=feature_range)

    X_train_scaled = X_train.copy()
    X_test_scaled = X_test.copy()

    X_train_scaled[columns] = scaler.fit_transform(X_train[columns])
    X_test_scaled[columns] = scaler.transform(X_test[columns])

    return X_train_scaled, X_test_scaled, scaler
```

### Robust Scaling
```python
from sklearn.preprocessing import RobustScaler

def robust_scale(X_train, X_test, columns):
    """Scale features using statistics robust to outliers"""

    scaler = RobustScaler()

    X_train_scaled = X_train.copy()
    X_test_scaled = X_test.copy()

    X_train_scaled[columns] = scaler.fit_transform(X_train[columns])
    X_test_scaled[columns] = scaler.transform(X_test[columns])

    return X_train_scaled, X_test_scaled, scaler
```

## Feature Selection

### Correlation-Based Selection
```python
def remove_correlated_features(df, threshold=0.95):
    """Remove highly correlated features"""

    # Calculate correlation matrix
    corr_matrix = df.corr().abs()

    # Get upper triangle
    upper = corr_matrix.where(
        np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
    )

    # Find features with correlation > threshold
    to_drop = [column for column in upper.columns if any(upper[column] > threshold)]

    print(f"Removing {len(to_drop)} highly correlated features")
    print(f"Features to drop: {to_drop}")

    return df.drop(columns=to_drop), to_drop
```

### Variance Threshold
```python
from sklearn.feature_selection import VarianceThreshold

def remove_low_variance_features(X_train, X_test, threshold=0.01):
    """Remove features with low variance"""

    selector = VarianceThreshold(threshold=threshold)

    X_train_selected = selector.fit_transform(X_train)
    X_test_selected = selector.transform(X_test)

    # Get selected feature names
    selected_features = X_train.columns[selector.get_support()].tolist()

    print(f"Selected {len(selected_features)} features out of {X_train.shape[1]}")

    return X_train_selected, X_test_selected, selected_features, selector
```

### Statistical Feature Selection
```python
from sklearn.feature_selection import SelectKBest, chi2, f_classif, mutual_info_classif

def select_k_best_features(X_train, X_test, y_train, k=20, score_func='mutual_info'):
    """Select top k features based on statistical tests"""

    # Choose scoring function
    score_functions = {
        'chi2': chi2,
        'f_classif': f_classif,
        'mutual_info': mutual_info_classif
    }

    score_func_obj = score_functions.get(score_func, mutual_info_classif)

    # Select features
    selector = SelectKBest(score_func=score_func_obj, k=k)

    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)

    # Get feature scores
    feature_scores = pd.DataFrame({
        'feature': X_train.columns,
        'score': selector.scores_
    }).sort_values('score', ascending=False)

    # Get selected features
    selected_features = X_train.columns[selector.get_support()].tolist()

    return X_train_selected, X_test_selected, selected_features, feature_scores
```

### Model-Based Feature Selection
```python
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier

def select_features_from_model(X_train, X_test, y_train, threshold='median'):
    """Select features based on model importance"""

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Select features
    selector = SelectFromModel(model, threshold=threshold, prefit=True)

    X_train_selected = selector.transform(X_train)
    X_test_selected = selector.transform(X_test)

    # Get feature importance
    feature_importance = pd.DataFrame({
        'feature': X_train.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)

    # Get selected features
    selected_features = X_train.columns[selector.get_support()].tolist()

    print(f"Selected {len(selected_features)} features")

    return X_train_selected, X_test_selected, selected_features, feature_importance
```

### Recursive Feature Elimination
```python
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

def recursive_feature_elimination(X_train, X_test, y_train, n_features=20):
    """Recursively eliminate features"""

    # Create model
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # RFE
    rfe = RFE(estimator=model, n_features_to_select=n_features, step=1)
    rfe.fit(X_train, y_train)

    # Transform data
    X_train_selected = rfe.transform(X_train)
    X_test_selected = rfe.transform(X_test)

    # Get selected features
    selected_features = X_train.columns[rfe.get_support()].tolist()

    # Get feature ranking
    feature_ranking = pd.DataFrame({
        'feature': X_train.columns,
        'ranking': rfe.ranking_
    }).sort_values('ranking')

    print(f"Selected {len(selected_features)} features")

    return X_train_selected, X_test_selected, selected_features, feature_ranking
```

## Dimensionality Reduction

### PCA (Principal Component Analysis)
```python
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def apply_pca(X_train, X_test, n_components=0.95):
    """
    Apply PCA for dimensionality reduction

    Args:
        n_components: If < 1, select components to preserve this variance ratio
                     If >= 1, select this many components
    """

    pca = PCA(n_components=n_components, random_state=42)

    X_train_pca = pca.fit_transform(X_train)
    X_test_pca = pca.transform(X_test)

    print(f"Original dimensions: {X_train.shape[1]}")
    print(f"Reduced dimensions: {X_train_pca.shape[1]}")
    print(f"Explained variance: {pca.explained_variance_ratio_.sum():.4f}")

    # Visualize explained variance
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(pca.explained_variance_ratio_)), pca.explained_variance_ratio_)
    plt.xlabel('Principal Component')
    plt.ylabel('Explained Variance Ratio')
    plt.title('PCA Explained Variance')
    plt.savefig('pca_variance.png', dpi=300, bbox_inches='tight')
    plt.close()

    return X_train_pca, X_test_pca, pca
```

### t-SNE for Visualization
```python
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def apply_tsne(X, y, n_components=2, perplexity=30):
    """Apply t-SNE for visualization (use on sample for speed)"""

    # Sample data if too large
    if len(X) > 5000:
        sample_idx = np.random.choice(len(X), 5000, replace=False)
        X_sample = X[sample_idx]
        y_sample = y[sample_idx]
    else:
        X_sample = X
        y_sample = y

    # Apply t-SNE
    tsne = TSNE(n_components=n_components, perplexity=perplexity, random_state=42)
    X_tsne = tsne.fit_transform(X_sample)

    # Visualize
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y_sample, cmap='viridis', alpha=0.6)
    plt.colorbar(scatter)
    plt.xlabel('t-SNE Component 1')
    plt.ylabel('t-SNE Component 2')
    plt.title('t-SNE Visualization')
    plt.savefig('tsne_visualization.png', dpi=300, bbox_inches='tight')
    plt.close()

    return X_tsne
```

## Missing Value Handling

### Simple Imputation
```python
from sklearn.impute import SimpleImputer

def simple_imputation(X_train, X_test, numerical_strategy='median', categorical_strategy='most_frequent'):
    """Impute missing values with simple strategies"""

    X_train_imputed = X_train.copy()
    X_test_imputed = X_test.copy()

    # Numerical columns
    num_cols = X_train.select_dtypes(include=[np.number]).columns
    num_imputer = SimpleImputer(strategy=numerical_strategy)
    X_train_imputed[num_cols] = num_imputer.fit_transform(X_train[num_cols])
    X_test_imputed[num_cols] = num_imputer.transform(X_test[num_cols])

    # Categorical columns
    cat_cols = X_train.select_dtypes(exclude=[np.number]).columns
    cat_imputer = SimpleImputer(strategy=categorical_strategy)
    X_train_imputed[cat_cols] = cat_imputer.fit_transform(X_train[cat_cols])
    X_test_imputed[cat_cols] = cat_imputer.transform(X_test[cat_cols])

    return X_train_imputed, X_test_imputed, num_imputer, cat_imputer
```

### KNN Imputation
```python
from sklearn.impute import KNNImputer

def knn_imputation(X_train, X_test, n_neighbors=5):
    """Impute missing values using K-Nearest Neighbors"""

    imputer = KNNImputer(n_neighbors=n_neighbors)

    X_train_imputed = imputer.fit_transform(X_train)
    X_test_imputed = imputer.transform(X_test)

    return X_train_imputed, X_test_imputed, imputer
```

## Complete Feature Engineering Pipeline

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

def create_feature_pipeline(numerical_features, categorical_features):
    """Create a comprehensive feature engineering pipeline"""

    # Numerical pipeline
    numerical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    # Categorical pipeline
    categorical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    # Combine pipelines
    preprocessor = ColumnTransformer([
        ('num', numerical_pipeline, numerical_features),
        ('cat', categorical_pipeline, categorical_features)
    ])

    return preprocessor

# Usage
numerical_features = ['age', 'income', 'balance']
categorical_features = ['gender', 'occupation', 'region']

preprocessor = create_feature_pipeline(numerical_features, categorical_features)

# Fit and transform
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# Get feature names
feature_names = (
    numerical_features +
    preprocessor.named_transformers_['cat']
        .named_steps['encoder']
        .get_feature_names_out(categorical_features).tolist()
)
```

## Best Practices

### Feature Engineering Checklist
1. **Understand the data**: Explore distributions, correlations, missing values
2. **Domain knowledge**: Create features based on business understanding
3. **Handle missing values**: Before encoding and scaling
4. **Encode categories**: Choose appropriate method for cardinality
5. **Scale features**: Based on algorithm requirements
6. **Create interactions**: Between related features
7. **Select features**: Remove redundant and irrelevant features
8. **Validate**: Check for data leakage, test on holdout set
9. **Document**: Keep track of all transformations

### Preventing Data Leakage
```python
# CORRECT: Fit on train, transform both
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# WRONG: Fit on all data
# scaler = StandardScaler()
# X_all_scaled = scaler.fit_transform(X)  # Data leakage!
```

### Pipeline for Production
```python
# Save entire preprocessing pipeline
import joblib

# Create and fit pipeline
pipeline = create_feature_pipeline(numerical_features, categorical_features)
pipeline.fit(X_train, y_train)

# Save
joblib.dump(pipeline, 'preprocessing_pipeline.pkl')

# Load and use in production
pipeline_loaded = joblib.load('preprocessing_pipeline.pkl')
X_new_processed = pipeline_loaded.transform(X_new)
```
