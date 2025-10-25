# ML Development Skill

Comprehensive patterns and techniques for machine learning model development, training, and optimization.

## Training Patterns

### Scikit-learn Training Pipeline

#### Basic Classification Pipeline
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score

# Create pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train with cross-validation
cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring='f1_weighted')
print(f"CV F1 Score: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

# Final training
pipeline.fit(X_train, y_train)

# Evaluate
from sklearn.metrics import classification_report
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))
```

#### Regression Pipeline
```python
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score

# Create polynomial regression pipeline
pipeline = Pipeline([
    ('poly', PolynomialFeatures(degree=2)),
    ('scaler', StandardScaler()),
    ('regressor', Ridge(alpha=1.0))
])

# Train
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"RMSE: {rmse:.4f}, R²: {r2:.4f}")
```

## Hyperparameter Tuning

### Grid Search
```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Define parameter grid
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2']
}

# Setup grid search
grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='f1_weighted',
    n_jobs=-1,
    verbose=1
)

# Execute search
grid_search.fit(X_train, y_train)

# Results
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best CV score: {grid_search.best_score_:.4f}")

# Get best model
best_model = grid_search.best_estimator_
```

### Randomized Search
```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform
import xgboost as xgb

# Define parameter distributions
param_dist = {
    'max_depth': randint(3, 10),
    'learning_rate': uniform(0.01, 0.3),
    'n_estimators': randint(100, 500),
    'subsample': uniform(0.6, 0.4),
    'colsample_bytree': uniform(0.6, 0.4),
    'min_child_weight': randint(1, 10),
    'gamma': uniform(0, 0.5)
}

# Setup randomized search
random_search = RandomizedSearchCV(
    xgb.XGBClassifier(random_state=42, eval_metric='logloss'),
    param_distributions=param_dist,
    n_iter=100,  # Number of parameter settings to sample
    cv=5,
    scoring='roc_auc',
    n_jobs=-1,
    random_state=42,
    verbose=1
)

# Execute search
random_search.fit(X_train, y_train)

print(f"Best parameters: {random_search.best_params_}")
print(f"Best ROC-AUC: {random_search.best_score_:.4f}")
```

### Bayesian Optimization with Optuna
```python
import optuna
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score

def objective(trial):
    """Objective function for Optuna"""

    # Suggest hyperparameters
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 300),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3, log=True),
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'min_samples_split': trial.suggest_int('min_samples_split', 2, 20),
        'min_samples_leaf': trial.suggest_int('min_samples_leaf', 1, 10),
        'subsample': trial.suggest_float('subsample', 0.6, 1.0)
    }

    # Create and evaluate model
    model = GradientBoostingClassifier(**params, random_state=42)
    score = cross_val_score(model, X_train, y_train, cv=5, scoring='f1_weighted').mean()

    return score

# Create study
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=50, show_progress_bar=True)

# Results
print(f"Best parameters: {study.best_params}")
print(f"Best F1 score: {study.best_value:.4f}")

# Train final model with best parameters
best_model = GradientBoostingClassifier(**study.best_params, random_state=42)
best_model.fit(X_train, y_train)
```

## Cross-Validation Techniques

### K-Fold Cross-Validation
```python
from sklearn.model_selection import KFold, cross_validate

# Standard K-Fold
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Multiple scoring metrics
scoring = ['accuracy', 'precision_weighted', 'recall_weighted', 'f1_weighted']

cv_results = cross_validate(
    model, X_train, y_train,
    cv=kfold,
    scoring=scoring,
    return_train_score=True,
    n_jobs=-1
)

# Print results
for metric in scoring:
    test_scores = cv_results[f'test_{metric}']
    print(f"{metric}: {test_scores.mean():.4f} (+/- {test_scores.std():.4f})")
```

### Stratified K-Fold (for Classification)
```python
from sklearn.model_selection import StratifiedKFold

# Ensures class distribution is preserved in each fold
stratified_kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

cv_scores = cross_val_score(
    model, X_train, y_train,
    cv=stratified_kfold,
    scoring='f1_weighted'
)

print(f"Stratified CV F1: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
```

### Time Series Cross-Validation
```python
from sklearn.model_selection import TimeSeriesSplit

# For time series data - preserves temporal order
tscv = TimeSeriesSplit(n_splits=5)

for train_idx, val_idx in tscv.split(X):
    X_train_fold, X_val_fold = X[train_idx], X[val_idx]
    y_train_fold, y_val_fold = y[train_idx], y[val_idx]

    # Train and evaluate
    model.fit(X_train_fold, y_train_fold)
    score = model.score(X_val_fold, y_val_fold)
    print(f"Fold score: {score:.4f}")
```

## Model Selection

### Comparing Multiple Models
```python
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
import xgboost as xgb

# Define models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    'SVM': SVC(kernel='rbf', random_state=42),
    'XGBoost': xgb.XGBClassifier(random_state=42, eval_metric='logloss')
}

# Compare models
results = []

for name, model in models.items():
    # Cross-validation
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='f1_weighted')

    results.append({
        'Model': name,
        'Mean F1': scores.mean(),
        'Std F1': scores.std(),
        'Min F1': scores.min(),
        'Max F1': scores.max()
    })

# Create comparison DataFrame
results_df = pd.DataFrame(results).sort_values('Mean F1', ascending=False)
print(results_df)
```

### Ensemble Methods

#### Voting Classifier
```python
from sklearn.ensemble import VotingClassifier

# Create ensemble
ensemble = VotingClassifier(
    estimators=[
        ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
        ('gb', GradientBoostingClassifier(random_state=42)),
        ('xgb', xgb.XGBClassifier(random_state=42, eval_metric='logloss'))
    ],
    voting='soft'  # Use predicted probabilities
)

# Train ensemble
ensemble.fit(X_train, y_train)

# Evaluate
y_pred = ensemble.predict(X_test)
print(f"Ensemble F1: {f1_score(y_test, y_pred, average='weighted'):.4f}")
```

#### Stacking Classifier
```python
from sklearn.ensemble import StackingClassifier

# Define base models
base_models = [
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('gb', GradientBoostingClassifier(random_state=42)),
    ('xgb', xgb.XGBClassifier(random_state=42, eval_metric='logloss'))
]

# Define meta-model
meta_model = LogisticRegression(max_iter=1000)

# Create stacking ensemble
stacking = StackingClassifier(
    estimators=base_models,
    final_estimator=meta_model,
    cv=5
)

# Train
stacking.fit(X_train, y_train)

# Evaluate
y_pred = stacking.predict(X_test)
print(f"Stacking F1: {f1_score(y_test, y_pred, average='weighted'):.4f}")
```

## PyTorch Training

### Basic Neural Network Training
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# Define model
class NeuralNet(nn.Module):
    def __init__(self, input_dim, hidden_dims, output_dim, dropout=0.3):
        super(NeuralNet, self).__init__()

        layers = []
        prev_dim = input_dim

        for hidden_dim in hidden_dims:
            layers.append(nn.Linear(prev_dim, hidden_dim))
            layers.append(nn.BatchNorm1d(hidden_dim))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(dropout))
            prev_dim = hidden_dim

        layers.append(nn.Linear(prev_dim, output_dim))
        self.network = nn.Sequential(*layers)

    def forward(self, x):
        return self.network(x)

# Prepare data
X_train_tensor = torch.FloatTensor(X_train)
y_train_tensor = torch.LongTensor(y_train)
X_val_tensor = torch.FloatTensor(X_val)
y_val_tensor = torch.LongTensor(y_val)

train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
val_dataset = TensorDataset(X_val_tensor, y_val_tensor)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32)

# Initialize model
model = NeuralNet(
    input_dim=X_train.shape[1],
    hidden_dims=[64, 32],
    output_dim=len(np.unique(y_train))
)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
num_epochs = 50
best_val_loss = float('inf')
patience = 5
patience_counter = 0

for epoch in range(num_epochs):
    # Training phase
    model.train()
    train_loss = 0

    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()

    # Validation phase
    model.eval()
    val_loss = 0

    with torch.no_grad():
        for X_batch, y_batch in val_loader:
            outputs = model(X_batch)
            loss = criterion(outputs, y_batch)
            val_loss += loss.item()

    avg_train_loss = train_loss / len(train_loader)
    avg_val_loss = val_loss / len(val_loader)

    print(f"Epoch {epoch+1}/{num_epochs} - Train Loss: {avg_train_loss:.4f}, Val Loss: {avg_val_loss:.4f}")

    # Early stopping
    if avg_val_loss < best_val_loss:
        best_val_loss = avg_val_loss
        patience_counter = 0
        torch.save(model.state_dict(), 'best_model.pth')
    else:
        patience_counter += 1
        if patience_counter >= patience:
            print("Early stopping triggered")
            break

# Load best model
model.load_state_dict(torch.load('best_model.pth'))
```

### Learning Rate Scheduling
```python
from torch.optim.lr_scheduler import ReduceLROnPlateau, CosineAnnealingLR

# Reduce LR on plateau
scheduler = ReduceLROnPlateau(
    optimizer,
    mode='min',
    factor=0.5,
    patience=3,
    verbose=True
)

# In training loop
for epoch in range(num_epochs):
    # ... training code ...

    # Step scheduler
    scheduler.step(avg_val_loss)

# Or use Cosine Annealing
scheduler = CosineAnnealingLR(optimizer, T_max=num_epochs)

for epoch in range(num_epochs):
    # ... training code ...
    scheduler.step()
```

## Handling Imbalanced Data

### Class Weights
```python
from sklearn.utils.class_weight import compute_class_weight

# Compute class weights
class_weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
class_weight_dict = dict(enumerate(class_weights))

# Use in model
model = RandomForestClassifier(
    n_estimators=100,
    class_weight='balanced',  # or pass class_weight_dict
    random_state=42
)
```

### SMOTE (Synthetic Minority Over-sampling)
```python
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline

# Create pipeline with SMOTE
pipeline = ImbPipeline([
    ('scaler', StandardScaler()),
    ('smote', SMOTE(random_state=42)),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Train (SMOTE is applied only to training data)
pipeline.fit(X_train, y_train)
```

### Stratified Sampling
```python
# Ensure balanced class distribution in splits
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y  # Preserve class distribution
)
```

## Model Persistence

### Saving and Loading
```python
import joblib
import pickle

# Save with joblib (recommended for scikit-learn)
joblib.dump(model, 'model.pkl')
model_loaded = joblib.load('model.pkl')

# Save with pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model.pkl', 'rb') as f:
    model_loaded = pickle.load(f)

# Save PyTorch model
torch.save(model.state_dict(), 'model.pth')
model.load_state_dict(torch.load('model.pth'))
```

## Best Practices

### Reproducibility
```python
import random
import numpy as np
import torch

def set_seed(seed=42):
    """Set random seeds for reproducibility"""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

set_seed(42)
```

### Train/Val/Test Split
```python
# Split into train (70%), validation (15%), test (15%)
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp
)
```

### Pipeline Best Practices
```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Create comprehensive pipeline
numerical_features = ['age', 'income']
categorical_features = ['gender', 'occupation']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numerical_features),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
])

full_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Train and save entire pipeline
full_pipeline.fit(X_train, y_train)
joblib.dump(full_pipeline, 'full_pipeline.pkl')

# Ensures consistent preprocessing in production
```

## Quick Reference

### Common Algorithms

**Classification:**
- Logistic Regression: Linear, fast, interpretable
- Random Forest: Non-linear, robust, handles mixed data
- XGBoost/LightGBM: High performance, handles missing values
- SVM: Effective in high dimensions, kernel methods
- Neural Networks: Complex patterns, requires more data

**Regression:**
- Linear Regression: Simple, interpretable, fast
- Ridge/Lasso: Regularized linear models
- Random Forest: Non-linear, robust
- XGBoost: High performance, ensemble method
- Neural Networks: Complex non-linear relationships

### Hyperparameter Tuning Comparison

| Method | Speed | Quality | Use When |
|--------|-------|---------|----------|
| Grid Search | Slow | Good | Small parameter space |
| Random Search | Medium | Good | Large parameter space |
| Bayesian (Optuna) | Fast | Best | Expensive models, many parameters |
