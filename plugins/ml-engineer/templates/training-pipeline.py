#!/usr/bin/env python3
"""
Complete ML Training Pipeline
A production-ready template for training machine learning models

Usage:
    python training-pipeline.py --data data.csv --target target_column --model xgboost

Features:
    - Data loading and validation
    - Train/validation/test splitting
    - Feature preprocessing pipeline
    - Model training with cross-validation
    - Hyperparameter tuning
    - Model evaluation and metrics
    - Model saving and versioning
"""

import argparse
import json
import warnings
from datetime import datetime
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)
from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV,
    StratifiedKFold,
    train_test_split,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

warnings.filterwarnings("ignore")

# Try to import optional packages
try:
    import xgboost as xgb
    HAS_XGBOOST = True
except ImportError:
    HAS_XGBOOST = False

try:
    import lightgbm as lgb
    HAS_LIGHTGBM = True
except ImportError:
    HAS_LIGHTGBM = False


class MLTrainingPipeline:
    """Complete ML training pipeline"""

    def __init__(self, data_path, target_column, model_type="random_forest", output_dir="output"):
        """
        Initialize training pipeline

        Args:
            data_path: Path to training data CSV
            target_column: Name of target column
            model_type: Type of model to train (logistic, random_forest, gradient_boosting, xgboost, lightgbm)
            output_dir: Directory to save outputs
        """
        self.data_path = data_path
        self.target_column = target_column
        self.model_type = model_type
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        self.data = None
        self.X_train = None
        self.X_val = None
        self.X_test = None
        self.y_train = None
        self.y_val = None
        self.y_test = None
        self.preprocessor = None
        self.model = None
        self.best_model = None
        self.feature_names = None
        self.metrics = {}

    def load_data(self):
        """Load and validate data"""
        print("\n" + "=" * 80)
        print("LOADING DATA")
        print("=" * 80)

        self.data = pd.read_csv(self.data_path)
        print(f"Loaded data shape: {self.data.shape}")
        print(f"\nTarget column: {self.target_column}")
        print(f"Target distribution:\n{self.data[self.target_column].value_counts()}")

        # Check for missing values
        missing = self.data.isnull().sum()
        if missing.any():
            print(f"\nMissing values:\n{missing[missing > 0]}")

        # Data types
        print(f"\nData types:\n{self.data.dtypes.value_counts()}")

    def split_data(self, test_size=0.2, val_size=0.15, random_state=42):
        """Split data into train, validation, and test sets"""
        print("\n" + "=" * 80)
        print("SPLITTING DATA")
        print("=" * 80)

        # Separate features and target
        X = self.data.drop(columns=[self.target_column])
        y = self.data[self.target_column]

        # Split into train+val and test
        X_temp, self.X_test, y_temp, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )

        # Split train into train and validation
        val_size_adjusted = val_size / (1 - test_size)
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(
            X_temp, y_temp, test_size=val_size_adjusted, random_state=random_state, stratify=y_temp
        )

        print(f"Train set: {self.X_train.shape}")
        print(f"Validation set: {self.X_val.shape}")
        print(f"Test set: {self.X_test.shape}")

        # Check stratification
        print("\nClass distribution:")
        print(f"Train: {self.y_train.value_counts(normalize=True).to_dict()}")
        print(f"Val: {self.y_val.value_counts(normalize=True).to_dict()}")
        print(f"Test: {self.y_test.value_counts(normalize=True).to_dict()}")

    def create_preprocessor(self):
        """Create preprocessing pipeline"""
        print("\n" + "=" * 80)
        print("CREATING PREPROCESSOR")
        print("=" * 80)

        # Identify column types
        numerical_features = self.X_train.select_dtypes(include=["int64", "float64"]).columns.tolist()
        categorical_features = self.X_train.select_dtypes(include=["object", "category"]).columns.tolist()

        print(f"Numerical features ({len(numerical_features)}): {numerical_features}")
        print(f"Categorical features ({len(categorical_features)}): {categorical_features}")

        # Numerical pipeline
        numerical_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ])

        # Categorical pipeline
        categorical_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
            ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
        ])

        # Combine pipelines
        self.preprocessor = ColumnTransformer([
            ("num", numerical_pipeline, numerical_features),
            ("cat", categorical_pipeline, categorical_features)
        ])

        # Fit preprocessor
        self.preprocessor.fit(self.X_train)

        # Get feature names after preprocessing
        self.feature_names = (
            numerical_features +
            self.preprocessor.named_transformers_["cat"]
                .named_steps["encoder"]
                .get_feature_names_out(categorical_features).tolist()
        )

        print(f"\nTotal features after preprocessing: {len(self.feature_names)}")

    def get_model(self):
        """Get model based on model_type"""
        models = {
            "logistic": LogisticRegression(max_iter=1000, random_state=42),
            "random_forest": RandomForestClassifier(random_state=42),
            "gradient_boosting": GradientBoostingClassifier(random_state=42)
        }

        if HAS_XGBOOST:
            models["xgboost"] = xgb.XGBClassifier(random_state=42, eval_metric="logloss")

        if HAS_LIGHTGBM:
            models["lightgbm"] = lgb.LGBMClassifier(random_state=42, verbose=-1)

        if self.model_type not in models:
            raise ValueError(f"Unknown model type: {self.model_type}. Available: {list(models.keys())}")

        return models[self.model_type]

    def get_param_grid(self):
        """Get hyperparameter grid for model"""
        param_grids = {
            "logistic": {
                "C": [0.01, 0.1, 1.0, 10.0],
                "penalty": ["l2"],
                "solver": ["lbfgs"]
            },
            "random_forest": {
                "n_estimators": [100, 200, 300],
                "max_depth": [10, 20, 30, None],
                "min_samples_split": [2, 5, 10],
                "min_samples_leaf": [1, 2, 4]
            },
            "gradient_boosting": {
                "n_estimators": [100, 200],
                "learning_rate": [0.01, 0.1, 0.2],
                "max_depth": [3, 5, 7],
                "subsample": [0.8, 1.0]
            },
            "xgboost": {
                "n_estimators": [100, 200, 300],
                "max_depth": [3, 5, 7],
                "learning_rate": [0.01, 0.1, 0.2],
                "subsample": [0.8, 1.0],
                "colsample_bytree": [0.8, 1.0]
            },
            "lightgbm": {
                "n_estimators": [100, 200, 300],
                "max_depth": [3, 5, 7, -1],
                "learning_rate": [0.01, 0.1, 0.2],
                "subsample": [0.8, 1.0]
            }
        }

        return param_grids.get(self.model_type, {})

    def train_model(self, use_grid_search=True, cv_folds=5):
        """Train model with hyperparameter tuning"""
        print("\n" + "=" * 80)
        print("TRAINING MODEL")
        print("=" * 80)

        # Get model
        self.model = self.get_model()
        print(f"Model: {self.model_type}")

        # Preprocess data
        X_train_processed = self.preprocessor.transform(self.X_train)
        X_val_processed = self.preprocessor.transform(self.X_val)

        if use_grid_search:
            print(f"\nPerforming hyperparameter tuning with {cv_folds}-fold cross-validation...")

            param_grid = self.get_param_grid()

            if param_grid:
                # Use RandomizedSearchCV for faster search
                search = RandomizedSearchCV(
                    self.model,
                    param_grid,
                    n_iter=20,
                    cv=StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=42),
                    scoring="f1_weighted",
                    n_jobs=-1,
                    random_state=42,
                    verbose=1
                )

                search.fit(X_train_processed, self.y_train)

                print(f"\nBest parameters: {search.best_params_}")
                print(f"Best CV score: {search.best_score_:.4f}")

                self.best_model = search.best_estimator_
            else:
                print("No parameter grid defined, training with default parameters...")
                self.model.fit(X_train_processed, self.y_train)
                self.best_model = self.model
        else:
            print("Training with default parameters...")
            self.model.fit(X_train_processed, self.y_train)
            self.best_model = self.model

        # Validation set evaluation
        y_val_pred = self.best_model.predict(X_val_processed)
        val_f1 = f1_score(self.y_val, y_val_pred, average="weighted")
        print(f"\nValidation F1 Score: {val_f1:.4f}")

    def evaluate_model(self):
        """Evaluate model on test set"""
        print("\n" + "=" * 80)
        print("EVALUATING MODEL")
        print("=" * 80)

        # Preprocess test data
        X_test_processed = self.preprocessor.transform(self.X_test)

        # Predictions
        y_pred = self.best_model.predict(X_test_processed)
        y_pred_proba = self.best_model.predict_proba(X_test_processed) if hasattr(self.best_model, "predict_proba") else None

        # Calculate metrics
        self.metrics = {
            "accuracy": accuracy_score(self.y_test, y_pred),
            "precision": precision_score(self.y_test, y_pred, average="weighted"),
            "recall": recall_score(self.y_test, y_pred, average="weighted"),
            "f1": f1_score(self.y_test, y_pred, average="weighted")
        }

        if y_pred_proba is not None and len(np.unique(self.y_test)) == 2:
            self.metrics["roc_auc"] = roc_auc_score(self.y_test, y_pred_proba[:, 1])

        # Print metrics
        print("\nTest Set Metrics:")
        for metric, value in self.metrics.items():
            print(f"{metric.upper():<15} {value:.4f}")

        # Classification report
        print("\nClassification Report:")
        print(classification_report(self.y_test, y_pred))

        # Confusion matrix
        self._plot_confusion_matrix(self.y_test, y_pred)

        # ROC curve
        if y_pred_proba is not None and len(np.unique(self.y_test)) == 2:
            self._plot_roc_curve(self.y_test, y_pred_proba[:, 1])

        # Feature importance
        if hasattr(self.best_model, "feature_importances_"):
            self._plot_feature_importance()

    def _plot_confusion_matrix(self, y_true, y_pred):
        """Plot confusion matrix"""
        cm = confusion_matrix(y_true, y_pred)

        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
        plt.title("Confusion Matrix")
        plt.ylabel("True Label")
        plt.xlabel("Predicted Label")
        plt.tight_layout()
        plt.savefig(self.output_dir / "confusion_matrix.png", dpi=300, bbox_inches="tight")
        plt.close()

        print(f"\nConfusion matrix saved to {self.output_dir / 'confusion_matrix.png'}")

    def _plot_roc_curve(self, y_true, y_score):
        """Plot ROC curve"""
        fpr, tpr, _ = roc_curve(y_true, y_score)
        roc_auc = roc_auc_score(y_true, y_score)

        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, linewidth=2, label=f"ROC curve (AUC = {roc_auc:.3f})")
        plt.plot([0, 1], [0, 1], "k--", linewidth=2, label="Random")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("ROC Curve")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(self.output_dir / "roc_curve.png", dpi=300, bbox_inches="tight")
        plt.close()

        print(f"ROC curve saved to {self.output_dir / 'roc_curve.png'}")

    def _plot_feature_importance(self, top_n=20):
        """Plot feature importance"""
        importance_df = pd.DataFrame({
            "feature": self.feature_names,
            "importance": self.best_model.feature_importances_
        }).sort_values("importance", ascending=False)

        plt.figure(figsize=(10, 8))
        plt.barh(importance_df["feature"][:top_n][::-1], importance_df["importance"][:top_n][::-1])
        plt.xlabel("Importance")
        plt.title(f"Top {top_n} Feature Importances")
        plt.tight_layout()
        plt.savefig(self.output_dir / "feature_importance.png", dpi=300, bbox_inches="tight")
        plt.close()

        print(f"Feature importance saved to {self.output_dir / 'feature_importance.png'}")

        # Save to CSV
        importance_df.to_csv(self.output_dir / "feature_importance.csv", index=False)

    def save_model(self, version=None):
        """Save model and artifacts"""
        print("\n" + "=" * 80)
        print("SAVING MODEL")
        print("=" * 80)

        if version is None:
            version = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Create version directory
        version_dir = self.output_dir / f"model_v{version}"
        version_dir.mkdir(exist_ok=True)

        # Save model and preprocessor
        joblib.dump(self.best_model, version_dir / "model.pkl")
        joblib.dump(self.preprocessor, version_dir / "preprocessor.pkl")

        # Save metadata
        metadata = {
            "version": version,
            "created_at": datetime.now().isoformat(),
            "model_type": self.model_type,
            "data_path": str(self.data_path),
            "target_column": self.target_column,
            "features": self.feature_names,
            "metrics": self.metrics,
            "data_shape": {
                "train": self.X_train.shape,
                "val": self.X_val.shape,
                "test": self.X_test.shape
            }
        }

        with open(version_dir / "metadata.json", "w") as f:
            json.dump(metadata, f, indent=2)

        print(f"\nModel saved to {version_dir}")
        print(f"  - model.pkl")
        print(f"  - preprocessor.pkl")
        print(f"  - metadata.json")

    def run(self):
        """Run complete pipeline"""
        print("\n" + "=" * 80)
        print("ML TRAINING PIPELINE")
        print("=" * 80)
        print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        self.load_data()
        self.split_data()
        self.create_preprocessor()
        self.train_model()
        self.evaluate_model()
        self.save_model()

        print("\n" + "=" * 80)
        print("PIPELINE COMPLETE")
        print("=" * 80)
        print(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\nResults saved to: {self.output_dir}")


def main():
    parser = argparse.ArgumentParser(description="ML Training Pipeline")
    parser.add_argument("--data", type=str, required=True, help="Path to training data CSV")
    parser.add_argument("--target", type=str, required=True, help="Name of target column")
    parser.add_argument(
        "--model",
        type=str,
        default="random_forest",
        choices=["logistic", "random_forest", "gradient_boosting", "xgboost", "lightgbm"],
        help="Model type to train"
    )
    parser.add_argument("--output", type=str, default="output", help="Output directory")
    parser.add_argument("--no-grid-search", action="store_true", help="Skip hyperparameter tuning")

    args = parser.parse_args()

    # Create and run pipeline
    pipeline = MLTrainingPipeline(
        data_path=args.data,
        target_column=args.target,
        model_type=args.model,
        output_dir=args.output
    )

    pipeline.run()


if __name__ == "__main__":
    main()
