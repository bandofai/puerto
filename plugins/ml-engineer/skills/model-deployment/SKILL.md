# Model Deployment Skill

Comprehensive patterns and techniques for deploying machine learning models to production.

## Model Serialization

### Joblib (Recommended for scikit-learn)
```python
import joblib

# Save model
joblib.dump(model, 'model.pkl', compress=3)

# Load model
model = joblib.load('model.pkl')

# Save multiple objects
joblib.dump({
    'model': model,
    'preprocessor': preprocessor,
    'feature_names': feature_names
}, 'model_artifacts.pkl')
```

### Pickle
```python
import pickle

# Save
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Load
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
```

### PyTorch Models
```python
import torch

# Save (state dict - recommended)
torch.save(model.state_dict(), 'model.pth')

# Load
model = MyModel()
model.load_state_dict(torch.load('model.pth'))
model.eval()

# Save entire model
torch.save(model, 'model_complete.pth')
model = torch.load('model_complete.pth')
```

### TensorFlow/Keras Models
```python
import tensorflow as tf

# Save in SavedModel format (recommended)
model.save('saved_model/')

# Load
model = tf.keras.models.load_model('saved_model/')

# Save in H5 format
model.save('model.h5')
model = tf.keras.models.load_model('model.h5')
```

### ONNX (Framework-agnostic)
```python
import torch
import torch.onnx

# PyTorch to ONNX
dummy_input = torch.randn(1, input_size)
torch.onnx.export(
    model,
    dummy_input,
    'model.onnx',
    export_params=True,
    opset_version=11,
    input_names=['input'],
    output_names=['output']
)

# Load and run ONNX model
import onnxruntime as ort

session = ort.InferenceSession('model.onnx')
output = session.run(None, {'input': input_data.numpy()})
```

## REST API Patterns

### FastAPI Model Serving
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
import joblib
import pandas as pd
import numpy as np
from typing import List, Optional
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="ML Model API",
    description="Production ML model serving",
    version="1.0.0"
)

# Global variables for models
model = None
preprocessor = None
feature_names = None

# Load models at startup
@app.on_event("startup")
async def load_models():
    global model, preprocessor, feature_names

    try:
        artifacts = joblib.load('model_artifacts.pkl')
        model = artifacts['model']
        preprocessor = artifacts['preprocessor']
        feature_names = artifacts['feature_names']
        logger.info("Models loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load models: {e}")
        raise

# Request/Response schemas
class PredictionInput(BaseModel):
    features: dict = Field(..., description="Feature dictionary")

    @validator('features')
    def validate_features(cls, v):
        if not v:
            raise ValueError("Features cannot be empty")
        return v

    class Config:
        schema_extra = {
            "example": {
                "features": {
                    "age": 35,
                    "income": 50000,
                    "gender": "M"
                }
            }
        }

class PredictionOutput(BaseModel):
    prediction: int
    probability: float
    model_version: str

class BatchInput(BaseModel):
    instances: List[dict] = Field(..., description="List of feature dictionaries")

    @validator('instances')
    def validate_instances(cls, v):
        if not v:
            raise ValueError("Instances cannot be empty")
        if len(v) > 1000:
            raise ValueError("Maximum batch size is 1000")
        return v

class BatchOutput(BaseModel):
    predictions: List[int]
    probabilities: List[float]
    count: int

# Endpoints
@app.get("/")
async def root():
    return {"message": "ML Model API", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy", "model_loaded": model is not None}

@app.post("/predict", response_model=PredictionOutput)
async def predict(input_data: PredictionInput):
    try:
        # Convert to DataFrame
        df = pd.DataFrame([input_data.features])

        # Validate features
        missing = set(feature_names) - set(df.columns)
        if missing:
            raise ValueError(f"Missing features: {missing}")

        # Reorder columns
        df = df[feature_names]

        # Preprocess and predict
        X = preprocessor.transform(df)
        prediction = int(model.predict(X)[0])
        probability = float(model.predict_proba(X)[0].max())

        return PredictionOutput(
            prediction=prediction,
            probability=probability,
            model_version="1.0.0"
        )
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/predict/batch", response_model=BatchOutput)
async def predict_batch(input_data: BatchInput):
    try:
        # Convert to DataFrame
        df = pd.DataFrame(input_data.instances)

        # Validate and reorder
        missing = set(feature_names) - set(df.columns)
        if missing:
            raise ValueError(f"Missing features: {missing}")

        df = df[feature_names]

        # Predict
        X = preprocessor.transform(df)
        predictions = model.predict(X).tolist()
        probabilities = model.predict_proba(X).max(axis=1).tolist()

        return BatchOutput(
            predictions=predictions,
            probabilities=probabilities,
            count=len(predictions)
        )
    except Exception as e:
        logger.error(f"Batch prediction error: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```

### Flask Model Serving
```python
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model
artifacts = joblib.load('model_artifacts.pkl')
model = artifacts['model']
preprocessor = artifacts['preprocessor']
feature_names = artifacts['feature_names']

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data
        data = request.get_json()

        # Validate
        if 'features' not in data:
            return jsonify({'error': 'Missing features'}), 400

        # Convert to DataFrame
        df = pd.DataFrame([data['features']])

        # Check features
        missing = set(feature_names) - set(df.columns)
        if missing:
            return jsonify({'error': f'Missing features: {missing}'}), 400

        # Reorder
        df = df[feature_names]

        # Predict
        X = preprocessor.transform(df)
        prediction = int(model.predict(X)[0])
        probability = float(model.predict_proba(X)[0].max())

        return jsonify({
            'prediction': prediction,
            'probability': probability
        })

    except Exception as e:
        logger.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

## Docker Deployment

### Dockerfile
```dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app.py .
COPY model_artifacts.pkl .

# Create non-root user
RUN useradd -m -u 1000 mluser && \
    chown -R mluser:mluser /app

USER mluser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Run application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

### requirements.txt
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
scikit-learn==1.3.2
pandas==2.1.3
numpy==1.26.2
joblib==1.3.2
```

### docker-compose.yml
```yaml
version: '3.8'

services:
  ml-api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - MODEL_VERSION=1.0.0
      - LOG_LEVEL=INFO
      - WORKERS=4
    volumes:
      - ./models:/app/models:ro
      - ./logs:/app/logs
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

### Build and Run
```bash
# Build image
docker build -t ml-model-api:latest .

# Run container
docker run -d \
  -p 8000:8000 \
  --name ml-api \
  --restart unless-stopped \
  ml-model-api:latest

# View logs
docker logs -f ml-api

# Stop container
docker stop ml-api

# Using docker-compose
docker-compose up -d
docker-compose logs -f
docker-compose down
```

## Model Versioning

### Version Management System
```python
import json
import joblib
from pathlib import Path
from datetime import datetime
import shutil

class ModelRegistry:
    """Manage model versions with metadata"""

    def __init__(self, registry_path='models'):
        self.registry_path = Path(registry_path)
        self.registry_path.mkdir(exist_ok=True)
        self.registry_file = self.registry_path / 'registry.json'

    def save_model(self, model, preprocessor, metadata, version=None):
        """Save a new model version"""

        # Auto-generate version
        if version is None:
            version = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Create version directory
        version_dir = self.registry_path / f"v_{version}"
        version_dir.mkdir(exist_ok=True)

        # Save artifacts
        artifacts = {
            'model': model,
            'preprocessor': preprocessor,
            'metadata': metadata
        }
        joblib.dump(artifacts, version_dir / 'artifacts.pkl')

        # Save metadata separately
        metadata['version'] = version
        metadata['created_at'] = datetime.now().isoformat()

        with open(version_dir / 'metadata.json', 'w') as f:
            json.dump(metadata, f, indent=2)

        # Update registry
        self._update_registry(version, metadata)

        print(f"Model saved: version {version}")
        return version

    def load_model(self, version='latest'):
        """Load a model version"""

        if version == 'latest':
            version = self._get_latest_version()

        version_dir = self.registry_path / f"v_{version}"

        if not version_dir.exists():
            raise ValueError(f"Version {version} not found")

        artifacts = joblib.load(version_dir / 'artifacts.pkl')
        return artifacts['model'], artifacts['preprocessor'], artifacts['metadata']

    def list_versions(self):
        """List all versions"""

        if not self.registry_file.exists():
            return []

        with open(self.registry_file, 'r') as f:
            registry = json.load(f)

        return registry.get('versions', [])

    def compare_versions(self, version1, version2, metric='accuracy'):
        """Compare two model versions"""

        _, _, meta1 = self.load_model(version1)
        _, _, meta2 = self.load_model(version2)

        score1 = meta1.get('metrics', {}).get(metric, 0)
        score2 = meta2.get('metrics', {}).get(metric, 0)

        print(f"\nVersion Comparison - {metric}")
        print(f"Version {version1}: {score1:.4f}")
        print(f"Version {version2}: {score2:.4f}")
        print(f"Difference: {score2 - score1:.4f}")

        return score1, score2

    def promote_to_production(self, version):
        """Promote a version to production"""

        version_dir = self.registry_path / f"v_{version}"

        if not version_dir.exists():
            raise ValueError(f"Version {version} not found")

        # Create production symlink
        prod_link = self.registry_path / 'production'

        if prod_link.exists():
            prod_link.unlink()

        prod_link.symlink_to(version_dir)

        print(f"Version {version} promoted to production")

    def _update_registry(self, version, metadata):
        """Update registry index"""

        if self.registry_file.exists():
            with open(self.registry_file, 'r') as f:
                registry = json.load(f)
        else:
            registry = {'versions': []}

        registry['versions'].append({
            'version': version,
            'created_at': metadata['created_at'],
            'metrics': metadata.get('metrics', {}),
            'model_type': metadata.get('model_type', 'unknown')
        })

        registry['versions'].sort(key=lambda x: x['created_at'], reverse=True)

        with open(self.registry_file, 'w') as f:
            json.dump(registry, f, indent=2)

    def _get_latest_version(self):
        """Get latest version"""

        versions = self.list_versions()

        if not versions:
            raise ValueError("No models in registry")

        return versions[0]['version']

# Usage example
registry = ModelRegistry()

# Save model
version = registry.save_model(
    model=trained_model,
    preprocessor=preprocessor,
    metadata={
        'model_type': 'RandomForest',
        'features': feature_names,
        'metrics': {
            'accuracy': 0.95,
            'f1': 0.93,
            'roc_auc': 0.97
        },
        'hyperparameters': {
            'n_estimators': 100,
            'max_depth': 20
        }
    }
)

# List versions
versions = registry.list_versions()
print(f"Available versions: {[v['version'] for v in versions]}")

# Load latest
model, preprocessor, metadata = registry.load_model('latest')

# Promote to production
registry.promote_to_production(version)
```

## Monitoring and Logging

### Request Logging
```python
from fastapi import FastAPI, Request
import time
import logging
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('api.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all requests"""

    start_time = time.time()

    # Log request
    logger.info(f"Request: {request.method} {request.url}")

    # Process request
    response = await call_next(request)

    # Calculate duration
    duration = time.time() - start_time

    # Log response
    logger.info(f"Response: {response.status_code} - Duration: {duration:.4f}s")

    return response

@app.post("/predict")
async def predict(input_data: dict):
    try:
        # Log input
        logger.info(f"Prediction input: {json.dumps(input_data)}")

        # Make prediction
        prediction = model.predict([input_data['features']])[0]

        # Log output
        logger.info(f"Prediction output: {prediction}")

        return {"prediction": int(prediction)}

    except Exception as e:
        logger.error(f"Prediction failed: {e}", exc_info=True)
        raise
```

### Performance Monitoring
```python
import time
from functools import wraps
import psutil
import os

def monitor_performance(func):
    """Decorator to monitor function performance"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Start metrics
        start_time = time.time()
        process = psutil.Process(os.getpid())
        start_memory = process.memory_info().rss / 1024 / 1024  # MB

        # Execute function
        result = func(*args, **kwargs)

        # End metrics
        end_time = time.time()
        end_memory = process.memory_info().rss / 1024 / 1024  # MB

        # Log metrics
        logger.info(f"{func.__name__} Performance:")
        logger.info(f"  Duration: {end_time - start_time:.4f}s")
        logger.info(f"  Memory: {end_memory - start_memory:.2f}MB")

        return result

    return wrapper

@monitor_performance
def predict(features):
    return model.predict([features])[0]
```

## Cloud Deployment

### AWS Lambda Deployment
```python
# lambda_function.py
import json
import joblib
import numpy as np

# Load model at cold start
model = joblib.load('model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

def lambda_handler(event, context):
    """AWS Lambda handler"""

    try:
        # Parse input
        body = json.loads(event['body'])
        features = body['features']

        # Preprocess
        X = preprocessor.transform([features])

        # Predict
        prediction = int(model.predict(X)[0])
        probability = float(model.predict_proba(X)[0].max())

        return {
            'statusCode': 200,
            'body': json.dumps({
                'prediction': prediction,
                'probability': probability
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

### Google Cloud Run Deployment
```yaml
# app.yaml
runtime: python39
entrypoint: gunicorn -b :$PORT app:app

env_variables:
  MODEL_PATH: "gs://my-bucket/models/latest"

automatic_scaling:
  target_cpu_utilization: 0.65
  min_instances: 1
  max_instances: 10
```

## Best Practices

### API Design
```python
# ✓ Good: Versioned API
@app.post("/v1/predict")
async def predict_v1(data: PredictionInput):
    pass

# ✓ Good: Clear error messages
raise HTTPException(
    status_code=400,
    detail="Missing required field: 'age'"
)

# ✓ Good: Request validation
class PredictionInput(BaseModel):
    age: int = Field(..., ge=0, le=120)
    income: float = Field(..., ge=0)

# ✓ Good: Response schema
class PredictionOutput(BaseModel):
    prediction: int
    confidence: float
    model_version: str
```

### Security
```python
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

API_KEY = "your-secret-key"
api_key_header = APIKeyHeader(name="X-API-Key")

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key

@app.post("/predict")
async def predict(data: dict, api_key: str = Security(verify_api_key)):
    # Protected endpoint
    pass
```

### Rate Limiting
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/predict")
@limiter.limit("100/minute")
async def predict(request: Request, data: dict):
    # Limited to 100 requests per minute
    pass
```

## Testing

### API Testing
```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_predict():
    response = client.post(
        "/predict",
        json={
            "features": {
                "age": 35,
                "income": 50000
            }
        }
    )
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
```

### Load Testing
```bash
# Using Apache Bench
ab -n 1000 -c 10 -p data.json -T application/json http://localhost:8000/predict

# Using wrk
wrk -t4 -c100 -d30s --timeout 10s http://localhost:8000/predict
```

## Quick Reference

### Deployment Checklist
- [ ] Model serialized and tested
- [ ] Preprocessing pipeline saved
- [ ] API endpoints implemented
- [ ] Request/response validation
- [ ] Error handling
- [ ] Logging configured
- [ ] Health check endpoint
- [ ] Docker container built and tested
- [ ] Environment variables configured
- [ ] Security measures (API keys, rate limiting)
- [ ] Monitoring setup
- [ ] Documentation written
- [ ] Load testing performed
