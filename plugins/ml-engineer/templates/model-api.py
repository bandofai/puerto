#!/usr/bin/env python3
"""
ML Model Serving API
A production-ready FastAPI template for serving machine learning models

Features:
    - Model loading and caching
    - Request validation with Pydantic
    - Batch and single predictions
    - Health check endpoints
    - Logging and monitoring
    - Error handling
    - API documentation

Usage:
    uvicorn model-api:app --host 0.0.0.0 --port 8000 --workers 4

    # With reload for development
    uvicorn model-api:app --reload

Testing:
    curl -X POST "http://localhost:8000/predict" \\
         -H "Content-Type: application/json" \\
         -d '{"features": {"age": 35, "income": 50000}}'
"""

import logging
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("api.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# =============================================================================
# Configuration
# =============================================================================

MODEL_PATH = "model.pkl"
PREPROCESSOR_PATH = "preprocessor.pkl"
METADATA_PATH = "metadata.json"
MODEL_VERSION = "1.0.0"
MAX_BATCH_SIZE = 1000

# =============================================================================
# Pydantic Models (Request/Response Schemas)
# =============================================================================

class HealthResponse(BaseModel):
    """Health check response"""
    status: str = Field(..., description="Service health status")
    model_loaded: bool = Field(..., description="Whether model is loaded")
    model_version: str = Field(..., description="Model version")
    timestamp: str = Field(..., description="Current timestamp")


class PredictionInput(BaseModel):
    """Single prediction request"""
    features: Dict[str, float] = Field(..., description="Feature dictionary")

    @validator("features")
    def validate_features(cls, v):
        if not v:
            raise ValueError("Features dictionary cannot be empty")
        return v

    class Config:
        schema_extra = {
            "example": {
                "features": {
                    "age": 35,
                    "income": 50000,
                    "credit_score": 700
                }
            }
        }


class PredictionOutput(BaseModel):
    """Single prediction response"""
    prediction: int = Field(..., description="Predicted class")
    probability: float = Field(..., description="Prediction probability/confidence")
    model_version: str = Field(..., description="Model version used")
    timestamp: str = Field(..., description="Prediction timestamp")

    class Config:
        schema_extra = {
            "example": {
                "prediction": 1,
                "probability": 0.87,
                "model_version": "1.0.0",
                "timestamp": "2024-01-01T12:00:00"
            }
        }


class BatchPredictionInput(BaseModel):
    """Batch prediction request"""
    instances: List[Dict[str, float]] = Field(..., description="List of feature dictionaries")

    @validator("instances")
    def validate_instances(cls, v):
        if not v:
            raise ValueError("Instances list cannot be empty")
        if len(v) > MAX_BATCH_SIZE:
            raise ValueError(f"Maximum batch size is {MAX_BATCH_SIZE}")
        return v

    class Config:
        schema_extra = {
            "example": {
                "instances": [
                    {"age": 35, "income": 50000, "credit_score": 700},
                    {"age": 42, "income": 75000, "credit_score": 800}
                ]
            }
        }


class BatchPredictionOutput(BaseModel):
    """Batch prediction response"""
    predictions: List[int] = Field(..., description="List of predicted classes")
    probabilities: List[float] = Field(..., description="List of prediction probabilities")
    count: int = Field(..., description="Number of predictions")
    model_version: str = Field(..., description="Model version used")
    timestamp: str = Field(..., description="Prediction timestamp")


class ModelInfo(BaseModel):
    """Model information response"""
    model_version: str
    model_type: str
    features: List[str]
    num_features: int
    created_at: str
    metrics: Optional[Dict[str, float]] = None


class ErrorResponse(BaseModel):
    """Error response"""
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Detailed error information")
    timestamp: str = Field(..., description="Error timestamp")


# =============================================================================
# FastAPI Application
# =============================================================================

app = FastAPI(
    title="ML Model Serving API",
    description="Production-ready API for serving machine learning models",
    version=MODEL_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables for model artifacts
model = None
preprocessor = None
feature_names = None
metadata = None


# =============================================================================
# Middleware
# =============================================================================

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all requests with timing"""
    start_time = time.time()

    # Generate request ID
    request_id = f"{int(start_time * 1000)}"

    # Log request
    logger.info(f"[{request_id}] {request.method} {request.url.path}")

    # Process request
    response = await call_next(request)

    # Calculate duration
    duration = time.time() - start_time

    # Log response
    logger.info(f"[{request_id}] Status: {response.status_code} - Duration: {duration:.4f}s")

    return response


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler"""
    logger.error(f"Global exception: {exc}", exc_info=True)

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponse(
            error="Internal server error",
            detail=str(exc),
            timestamp=datetime.now().isoformat()
        ).dict()
    )


# =============================================================================
# Startup/Shutdown Events
# =============================================================================

@app.on_event("startup")
async def load_model_artifacts():
    """Load model artifacts on startup"""
    global model, preprocessor, feature_names, metadata

    try:
        logger.info("Loading model artifacts...")

        # Check if files exist
        if not Path(MODEL_PATH).exists():
            raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
        if not Path(PREPROCESSOR_PATH).exists():
            raise FileNotFoundError(f"Preprocessor file not found: {PREPROCESSOR_PATH}")

        # Load model and preprocessor
        model = joblib.load(MODEL_PATH)
        preprocessor = joblib.load(PREPROCESSOR_PATH)

        logger.info(f"Model type: {type(model).__name__}")
        logger.info(f"Preprocessor type: {type(preprocessor).__name__}")

        # Load metadata if available
        if Path(METADATA_PATH).exists():
            import json
            with open(METADATA_PATH, "r") as f:
                metadata = json.load(f)
            feature_names = metadata.get("features", [])
            logger.info(f"Loaded metadata with {len(feature_names)} features")
        else:
            logger.warning(f"Metadata file not found: {METADATA_PATH}")
            feature_names = []

        logger.info("Model artifacts loaded successfully")

    except Exception as e:
        logger.error(f"Failed to load model artifacts: {e}", exc_info=True)
        raise


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    logger.info("Shutting down API server...")


# =============================================================================
# API Endpoints
# =============================================================================

@app.get("/", tags=["Info"])
async def root():
    """Root endpoint with API information"""
    return {
        "name": "ML Model Serving API",
        "version": MODEL_VERSION,
        "status": "running",
        "documentation": "/docs",
        "health_check": "/health"
    }


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        model_loaded=model is not None,
        model_version=MODEL_VERSION,
        timestamp=datetime.now().isoformat()
    )


@app.get("/model/info", response_model=ModelInfo, tags=["Model"])
async def get_model_info():
    """Get model information and metadata"""
    if metadata is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model metadata not available"
        )

    return ModelInfo(
        model_version=MODEL_VERSION,
        model_type=metadata.get("model_type", "unknown"),
        features=feature_names,
        num_features=len(feature_names),
        created_at=metadata.get("created_at", "unknown"),
        metrics=metadata.get("metrics")
    )


@app.get("/model/features", tags=["Model"])
async def get_features():
    """Get list of required features"""
    if not feature_names:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Feature names not available"
        )

    return {
        "features": feature_names,
        "count": len(feature_names),
        "example": {feat: 0.0 for feat in feature_names[:5]}
    }


@app.post("/predict", response_model=PredictionOutput, tags=["Prediction"])
async def predict(input_data: PredictionInput):
    """
    Make a single prediction

    Returns the predicted class and probability/confidence score.
    """
    try:
        # Log request
        logger.info(f"Single prediction request: {len(input_data.features)} features")

        # Convert to DataFrame
        df = pd.DataFrame([input_data.features])

        # Validate features
        if feature_names:
            missing_features = set(feature_names) - set(df.columns)
            if missing_features:
                raise ValueError(f"Missing required features: {missing_features}")

            # Reorder columns to match training
            df = df[feature_names]

        # Preprocess
        X = preprocessor.transform(df)

        # Predict
        prediction = int(model.predict(X)[0])

        # Get probability if available
        if hasattr(model, "predict_proba"):
            probability = float(model.predict_proba(X)[0].max())
        else:
            probability = 1.0  # Default for models without probability

        # Log successful prediction
        logger.info(f"Prediction: {prediction}, Probability: {probability:.4f}")

        return PredictionOutput(
            prediction=prediction,
            probability=probability,
            model_version=MODEL_VERSION,
            timestamp=datetime.now().isoformat()
        )

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except Exception as e:
        logger.error(f"Prediction failed: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Prediction failed: {str(e)}"
        )


@app.post("/predict/batch", response_model=BatchPredictionOutput, tags=["Prediction"])
async def predict_batch(input_data: BatchPredictionInput):
    """
    Make batch predictions

    Process multiple instances in a single request for efficiency.
    Maximum batch size: {MAX_BATCH_SIZE}
    """
    try:
        # Log request
        logger.info(f"Batch prediction request: {len(input_data.instances)} instances")

        # Convert to DataFrame
        df = pd.DataFrame(input_data.instances)

        # Validate features
        if feature_names:
            missing_features = set(feature_names) - set(df.columns)
            if missing_features:
                raise ValueError(f"Missing required features: {missing_features}")

            # Reorder columns
            df = df[feature_names]

        # Preprocess
        X = preprocessor.transform(df)

        # Predict
        predictions = model.predict(X).tolist()

        # Get probabilities if available
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(X).max(axis=1).tolist()
        else:
            probabilities = [1.0] * len(predictions)

        # Log successful predictions
        logger.info(f"Batch prediction completed: {len(predictions)} predictions")

        return BatchPredictionOutput(
            predictions=predictions,
            probabilities=probabilities,
            count=len(predictions),
            model_version=MODEL_VERSION,
            timestamp=datetime.now().isoformat()
        )

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except Exception as e:
        logger.error(f"Batch prediction failed: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Batch prediction failed: {str(e)}"
        )


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "model-api:app",
        host="0.0.0.0",
        port=8000,
        workers=4,
        log_level="info"
    )
