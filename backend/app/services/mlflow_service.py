"""
VisionQC MLflow Backend Service
Exposes reusable query service functions to retrieve:
- Experiment list and metadata
- Run history, hyperparameters, and evaluation metrics
- Model Registry versions, status, and active Production model details
"""

from typing import Dict, List, Any, Optional
import mlflow
from mlflow.tracking import MlflowClient

from ml.training.mlflow_utils import DEFAULT_TRACKING_URI, DEFAULT_EXPERIMENT_NAME

class MLflowService:
    def __init__(self, tracking_uri: str = DEFAULT_TRACKING_URI):
        self.tracking_uri = tracking_uri
        mlflow.set_tracking_uri(self.tracking_uri)
        self.client = MlflowClient(tracking_uri=self.tracking_uri)

    def get_experiments(self) -> List[Dict[str, Any]]:
        experiments = self.client.search_experiments()
        out = []
        for exp in experiments:
            out.append({
                "experiment_id": exp.experiment_id,
                "name": exp.name,
                "artifact_location": exp.artifact_location,
                "lifecycle_stage": exp.lifecycle_stage,
                "tags": exp.tags
            })
        return out

    def get_runs(self, experiment_name: str = DEFAULT_EXPERIMENT_NAME) -> List[Dict[str, Any]]:
        exp = self.client.get_experiment_by_name(experiment_name)
        if not exp:
            return []
        
        runs = self.client.search_runs(experiment_ids=[exp.experiment_id], order_by=["attributes.start_time DESC"])
        out = []
        for r in runs:
            out.append({
                "run_id": r.info.run_id,
                "run_name": r.data.tags.get("mlflow.runName", "unnamed"),
                "status": r.info.status,
                "start_time": r.info.start_time,
                "end_time": r.info.end_time,
                "duration_ms": (r.info.end_time - r.info.start_time) if r.info.end_time else None,
                "params": r.data.params,
                "metrics": r.data.metrics,
                "tags": r.data.tags
            })
        return out

    def get_registered_models(self) -> List[Dict[str, Any]]:
        models = self.client.search_registered_models()
        out = []
        for m in models:
            versions = []
            for v in m.latest_versions:
                versions.append({
                    "version": v.version,
                    "stage": v.current_stage,
                    "status": v.status,
                    "source": v.source,
                    "run_id": v.run_id,
                    "tags": v.tags,
                    "description": v.description
                })
            out.append({
                "name": m.name,
                "description": m.description,
                "tags": m.tags,
                "versions": versions
            })
        return out

    def get_production_model(self, model_name: str = "visionqc-impeller-classifier") -> Optional[Dict[str, Any]]:
        try:
            versions = self.client.search_model_versions(f"name = '{model_name}'")
            for v in versions:
                if v.tags.get("stage") == "Production" or v.current_stage == "Production":
                    return {
                        "name": model_name,
                        "version": v.version,
                        "run_id": v.run_id,
                        "source": v.source,
                        "threshold": float(v.tags.get("threshold", 0.5)),
                        "defect_recall": float(v.tags.get("defect_recall", 1.0)),
                        "description": v.description
                    }
        except Exception:
            return None
        return None

if __name__ == "__main__":
    svc = MLflowService()
    runs = svc.get_runs()
    print(f"Retrieved {len(runs)} runs from MLflow:")
    for r in runs:
        print(f" - {r['run_name']}: Accuracy = {r['metrics'].get('accuracy')}, Defect Recall = {r['metrics'].get('recall_defect')}")

    prod = svc.get_production_model()
    print(f"\nProduction Model in Registry: {prod}")
