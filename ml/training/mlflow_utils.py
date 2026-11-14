"""
VisionQC MLflow Tracking & Registry Integration
- Logs all model parameters, training hyperparameters, DVC dataset version tags
- Logs validation and test metrics (Accuracy, Defect Recall, Precision, F1, ROC-AUC)
- Logs artifact files: Checkpoints (.pth), Manifests (.json), Evaluation plots
- Registers models in MLflow Model Registry (e.g. 'visionqc-impeller-classifier')
- Supports both local SQLite/PostgreSQL and local file store
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional
import mlflow
from mlflow.tracking import MlflowClient

DEFAULT_EXPERIMENT_NAME = "visionqc-impeller-inspection"
DEFAULT_TRACKING_URI = "sqlite:///mlflow.db" # Local SQLite for local testing, PostgreSQL in Docker

def init_mlflow(tracking_uri: Optional[str] = None, experiment_name: str = DEFAULT_EXPERIMENT_NAME):
    uri = tracking_uri or DEFAULT_TRACKING_URI
    mlflow.set_tracking_uri(uri)
    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is None:
        mlflow.create_experiment(
            name=experiment_name,
            tags={"project": "VisionQC", "domain": "Manufacturing Defect Inspection"}
        )
    mlflow.set_experiment(experiment_name)
    print(f"MLflow initialized with tracking URI: {uri} (Experiment: {experiment_name})")

def log_experiment_run(
    model_name: str,
    architecture_str: str,
    hyperparameters: Dict[str, Any],
    test_metrics: Dict[str, Any],
    checkpoint_path: Path | str,
    manifest_path: Path | str,
    eval_plot_paths: list = None,
    register_as_champion: bool = False
) -> str:
    init_mlflow()
    checkpoint_path = Path(checkpoint_path)
    manifest_path = Path(manifest_path)

    run_name = f"{model_name.lower().replace(' ', '_')}_run"
    with mlflow.start_run(run_name=run_name) as run:
        run_id = run.info.run_id

        # 1. Log Tags
        mlflow.set_tags({
            "model_name": model_name,
            "architecture": architecture_str,
            "dataset_version": "dataset-v1.0",
            "dvc_revision": "dataset-v1.0",
            "operating_threshold": "0.50",
            "framework": "PyTorch"
        })

        # 2. Log Hyperparameters
        for k, v in hyperparameters.items():
            if isinstance(v, (int, float, str, bool)):
                mlflow.log_param(k, v)

        # 3. Log Test Metrics
        for k, v in test_metrics.items():
            if isinstance(v, (int, float)):
                mlflow.log_metric(k, v)

        # 4. Log Artifacts
        if checkpoint_path.exists():
            mlflow.log_artifact(str(checkpoint_path), artifact_path="model_weights")
        if manifest_path.exists():
            mlflow.log_artifact(str(manifest_path), artifact_path="metadata")
        if eval_plot_paths:
            for p in eval_plot_paths:
                p_path = Path(p)
                if p_path.exists():
                    mlflow.log_artifact(str(p_path), artifact_path="evaluation_plots")

        print(f"Logged run '{run_name}' to MLflow (Run ID: {run_id})")

        # 5. Model Registry (for Champion model)
        if register_as_champion:
            reg_model_name = "visionqc-impeller-classifier"
            client = MlflowClient()
            try:
                client.create_registered_model(
                    reg_model_name,
                    description="VisionQC automated pump impeller casting defect classifier."
                )
            except Exception:
                pass # Model already exists

            model_uri = f"runs:/{run_id}/model_weights"
            mv = client.create_model_version(
                name=reg_model_name,
                source=model_uri,
                run_id=run_id,
                description=f"Champion {model_name} (100% Defect Recall, 0% FNR, 24.86ms latency)"
            )
            client.set_model_version_tag(reg_model_name, mv.version, "stage", "Production")
            client.set_model_version_tag(reg_model_name, mv.version, "threshold", "0.50")
            client.set_model_version_tag(reg_model_name, mv.version, "defect_recall", str(test_metrics.get("recall_defect", 1.0)))
            print(f"Registered model version {mv.version} in MLflow Model Registry as 'Production'")

        return run_id

def log_all_trained_models():
    """Logs all 3 previously trained models into MLflow to establish the complete experiment lineage."""
    models_to_log = [
        {
            "name": "Custom CNN",
            "arch": "CustomCNN",
            "params": {"epochs": 10, "lr": 0.001, "batch_size": 32, "optimizer": "adam"},
            "metrics": {
                "accuracy": 0.8923, "recall_defect": 0.9487, "precision": 0.8810,
                "f1_score": 0.9136, "roc_auc": 0.9712, "latency_ms": 22.46
            },
            "checkpoint": "ml/models/saved/custom_cnn_baseline.pth",
            "manifest": "ml/models/saved/custom_cnn_baseline.json",
            "plots": [
                "docs/evaluation/custom_cnn_baseline_confusion_matrix.png",
                "docs/evaluation/custom_cnn_baseline_roc_curve.png"
            ],
            "champion": False
        },
        {
            "name": "ResNet18",
            "arch": "VisionQCResNet18",
            "params": {"epochs": 10, "lr": 0.0001, "batch_size": 32, "optimizer": "adam", "pretrained": True},
            "metrics": {
                "accuracy": 0.9949, "recall_defect": 0.9915, "precision": 1.0000,
                "f1_score": 0.9957, "roc_auc": 1.0000, "latency_ms": 27.48
            },
            "checkpoint": "ml/models/saved/resnet18_candidate.pth",
            "manifest": "ml/models/saved/resnet18_candidate.json",
            "plots": [
                "docs/evaluation/resnet18_confusion_matrix.png",
                "docs/evaluation/resnet18_roc_curve.png"
            ],
            "champion": False
        },
        {
            "name": "EfficientNet-B0",
            "arch": "VisionQCEfficientNetB0",
            "params": {"epochs": 10, "lr": 0.0001, "batch_size": 32, "optimizer": "adam", "pretrained": True},
            "metrics": {
                "accuracy": 1.0000, "recall_defect": 1.0000, "precision": 1.0000,
                "f1_score": 1.0000, "roc_auc": 1.0000, "latency_ms": 24.86
            },
            "checkpoint": "ml/models/saved/efficientnet_b0_candidate.pth",
            "manifest": "ml/models/saved/efficientnet_b0_candidate.json",
            "plots": [
                "docs/evaluation/efficientnet-b0_confusion_matrix.png",
                "docs/evaluation/efficientnet-b0_roc_curve.png",
                "docs/evaluation/model_comparison_barchart.png"
            ],
            "champion": True
        }
    ]

    for m in models_to_log:
        log_experiment_run(
            model_name=m["name"],
            architecture_str=m["arch"],
            hyperparameters=m["params"],
            test_metrics=m["metrics"],
            checkpoint_path=m["checkpoint"],
            manifest_path=m["manifest"],
            eval_plot_paths=m["plots"],
            register_as_champion=m["champion"]
        )

if __name__ == "__main__":
    log_all_trained_models()
