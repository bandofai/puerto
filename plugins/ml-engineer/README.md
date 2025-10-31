# ML Engineer Plugin

A comprehensive machine learning development plugin for Puerto, providing specialized agents, skills, and templates for the complete ML lifecycle - from feature engineering through model deployment.

## Overview

The ML Engineer plugin enables you to build, train, evaluate, and deploy machine learning models with industry-standard practices and tools. It supports multiple ML frameworks including scikit-learn, PyTorch, and TensorFlow.

## Agents

### 1. Model Trainer (Sonnet)
**Purpose**: Train machine learning models with automated hyperparameter tuning and validation

**Capabilities**:
- Train models with scikit-learn, PyTorch, TensorFlow
- Hyperparameter tuning (GridSearch, RandomSearch, Bayesian)
- Cross-validation strategies (K-Fold, Stratified, Time Series)
- Model selection and comparison
- Training pipeline automation

**Use When**:
- Training new ML models
- Comparing multiple model architectures
- Optimizing model hyperparameters
- Setting up training pipelines

**Example**:
```
@model-trainer Train a gradient boosting classifier on customer_data.csv to predict churn.
Use 5-fold cross-validation and tune the hyperparameters.
```

### 2. Feature Engineer (Sonnet)
**Purpose**: Create, transform, and select features for optimal model performance

**Capabilities**:
- Feature creation and extraction
- Encoding (one-hot, label, target, ordinal)
- Scaling and normalization (StandardScaler, MinMaxScaler, RobustScaler)
- Dimensionality reduction (PCA, t-SNE, UMAP)
- Feature selection (statistical, model-based, recursive)
- Handling missing values and outliers

**Use When**:
- Preparing raw data for modeling
- Creating derived features
- Reducing feature dimensionality
- Selecting most important features
- Handling categorical variables

**Example**:
```
@feature-engineer Create features from the sales_data.csv dataset.
Handle missing values, encode categorical variables, and select the top 20 most important features.
```

### 3. Model Evaluator (Sonnet)
**Purpose**: Comprehensively evaluate model performance with multiple metrics and visualizations

**Capabilities**:
- Classification metrics (accuracy, precision, recall, F1, ROC-AUC)
- Regression metrics (MAE, MSE, RMSE, R², MAPE)
- Confusion matrices and classification reports
- ROC and Precision-Recall curves
- Feature importance analysis
- Cross-validation scoring
- Model comparison and statistical testing

**Use When**:
- Evaluating trained models
- Comparing model performance
- Analyzing prediction errors
- Understanding feature importance
- Validating model robustness

**Example**:
```
@model-evaluator Evaluate the trained model on the test set.
Generate ROC curves, confusion matrix, and feature importance plots.
```

### 4. Model Deployer (Haiku)
**Purpose**: Deploy models to production with versioning and API creation

**Capabilities**:
- Save models in multiple formats (pickle, joblib, ONNX)
- Create REST APIs (Flask, FastAPI)
- Model versioning and registry
- Docker containerization
- Inference endpoint creation
- Model metadata tracking

**Use When**:
- Deploying models to production
- Creating prediction APIs
- Versioning model artifacts
- Setting up model serving infrastructure
- Containerizing ML applications

**Example**:
```
@model-deployer Deploy the churn prediction model as a FastAPI endpoint.
Save the model with version 1.0.0 and create a Docker container.
```

## Skills

### 1. ML Development
**Focus**: Training patterns, hyperparameter tuning, and model selection

**Includes**:
- Scikit-learn training patterns
- PyTorch model training
- TensorFlow/Keras workflows
- Hyperparameter optimization strategies
- Cross-validation techniques
- Model ensemble methods
- Training best practices

**Load**: The skill is automatically available to relevant agents

### 2. Feature Engineering
**Focus**: Feature creation, selection, and transformation techniques

**Includes**:
- Feature extraction methods
- Encoding strategies
- Scaling and normalization
- Dimensionality reduction
- Feature selection algorithms
- Handling imbalanced data
- Domain-specific feature engineering

**Load**: The skill is automatically available to relevant agents

### 3. Model Deployment
**Focus**: Model serving, API creation, and production deployment

**Includes**:
- Model serialization formats
- REST API patterns (Flask/FastAPI)
- Model versioning strategies
- Monitoring and logging
- Docker deployment
- Cloud deployment (AWS, GCP, Azure)
- MLOps best practices

**Load**: The skill is automatically available to relevant agents

## Templates

### training-pipeline.py
A complete, production-ready ML training pipeline template that includes:
- Data loading and validation
- Train/validation/test splitting
- Feature preprocessing pipeline
- Model training with cross-validation
- Hyperparameter tuning
- Model evaluation and metrics
- Model saving and versioning

**Usage**:
```python
# Customize for your specific use case
python training-pipeline.py --data data.csv --target target_column --model xgboost
```

### model-api.py
A FastAPI-based model serving template that includes:
- Model loading and caching
- Request validation with Pydantic
- Batch and single predictions
- Health check endpoints
- Logging and monitoring
- Error handling
- API documentation

**Usage**:
```python
# Start the API server
uvicorn model-api:app --host 0.0.0.0 --port 8000
```

## Installation

### Basic Setup
```bash
# Install core ML dependencies
pip install scikit-learn pandas numpy matplotlib seaborn joblib
```

### Deep Learning (Optional)
```bash
# For PyTorch
pip install torch torchvision

# For TensorFlow
pip install tensorflow

# For gradient boosting
pip install xgboost lightgbm
```

### Deployment (Optional)
```bash
# For model serving
pip install fastapi uvicorn pydantic

# For experiment tracking
pip install mlflow wandb
```

## Workflow Examples

### Complete ML Pipeline
```
1. @feature-engineer Analyze the dataset and create features from raw_data.csv
2. @model-trainer Train multiple models (RandomForest, XGBoost, LightGBM) and compare performance
3. @model-evaluator Evaluate all models and generate comprehensive performance reports
4. @model-deployer Deploy the best model as a FastAPI service with versioning
```

### Model Optimization
```
1. @feature-engineer Perform feature selection to identify top 15 features
2. @model-trainer Retrain the model with selected features and optimize hyperparameters
3. @model-evaluator Compare performance with original model
```

### Production Deployment
```
1. @model-evaluator Validate model performance on hold-out test set
2. @model-deployer Save model artifacts and create production API
3. @model-deployer Create Docker container and deployment documentation
```

## Best Practices

### Data Preparation
- Always split data before any preprocessing
- Use pipelines to prevent data leakage
- Validate data quality and distributions
- Handle missing values appropriately
- Document all transformations

### Model Training
- Use cross-validation for robust performance estimates
- Start simple, then increase complexity
- Track all experiments and hyperparameters
- Save random seeds for reproducibility
- Monitor for overfitting

### Feature Engineering
- Create features based on domain knowledge
- Remove highly correlated features
- Scale features appropriately for the algorithm
- Test feature importance regularly
- Document feature creation logic

### Model Evaluation
- Use multiple evaluation metrics
- Test on truly unseen data
- Check for bias and fairness
- Analyze error patterns
- Compare against baseline models

### Deployment
- Version all models and data
- Implement proper logging
- Monitor model performance in production
- Set up automated retraining
- Document model requirements and dependencies

## Common Use Cases

1. **Classification Tasks**: Customer churn, fraud detection, sentiment analysis
2. **Regression Tasks**: Price prediction, demand forecasting, risk scoring
3. **Time Series**: Sales forecasting, anomaly detection, trend analysis
4. **Computer Vision**: Image classification, object detection (with PyTorch/TensorFlow)
5. **NLP**: Text classification, named entity recognition, embeddings

## Troubleshooting

### Model Performance Issues
- Check for data leakage
- Verify train/test split stratification
- Ensure proper feature scaling
- Review hyperparameter ranges
- Check for class imbalance

### Training Issues
- Verify data types and formats
- Check for NaN or infinite values
- Ensure sufficient training data
- Monitor memory usage
- Validate target variable distribution

### Deployment Issues
- Test API with sample requests
- Verify model file compatibility
- Check dependency versions
- Ensure proper error handling
- Monitor resource usage

## Integration

This plugin integrates well with:
- **Data Analyst**: For data exploration and preprocessing
- **Backend Architect**: For production deployment architecture
- **DevOps Engineer**: For CI/CD and infrastructure setup
- **QA Automation**: For model testing and validation

## Support

For issues, questions, or contributions, please refer to the Puerto documentation and the ML Engineer plugin examples.
