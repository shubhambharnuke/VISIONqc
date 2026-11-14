"""
VisionQC SQLAlchemy Database Models
Defines all operational and metadata persistence tables required by PRD & techstack:
- predictions: inspection records, classification outputs, Grad-CAM links
- model_deployments: current active model and deployment version history
- dataset_versions: DVC dataset releases and sample counts
- pipeline_runs: Airflow execution history
- drift_reports: data drift scores and alert states
- retraining_jobs: retraining run tracking
- audit_logs: administrative actions and promotion audits
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, JSON, Text
from backend.app.database.connection import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(String(64), primary_key=True, index=True) # UUID or hash
    image_filename = Column(String(255), nullable=False)
    predicted_class = Column(String(32), nullable=False) # "OK" or "DEFECTIVE"
    defect_probability = Column(Float, nullable=False)
    decision = Column(String(32), nullable=False) # "ACCEPT" or "REJECT"
    threshold_applied = Column(Float, default=0.50)
    model_name = Column(String(64), nullable=False)
    model_version = Column(String(32), nullable=False)
    inference_latency_ms = Column(Float, nullable=False)
    has_gradcam = Column(Boolean, default=False)
    gradcam_paths = Column(JSON, nullable=True) # {"original": ..., "heatmap": ..., "overlay": ...}
    created_at = Column(DateTime, default=datetime.utcnow, index=True)

class ModelDeployment(Base):
    __tablename__ = "model_deployments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String(64), nullable=False)
    architecture = Column(String(64), nullable=False)
    version = Column(String(32), nullable=False)
    checkpoint_path = Column(String(255), nullable=False)
    threshold = Column(Float, default=0.50)
    defect_recall = Column(Float, nullable=False)
    accuracy = Column(Float, nullable=False)
    status = Column(String(32), default="ACTIVE") # "ACTIVE", "REPLACED", "STAGING"
    deployed_at = Column(DateTime, default=datetime.utcnow)

class DatasetVersion(Base):
    __tablename__ = "dataset_versions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    version_tag = Column(String(64), unique=True, nullable=False) # "dataset-v1.0"
    total_images = Column(Integer, nullable=False)
    ok_count = Column(Integer, nullable=False)
    defective_count = Column(Integer, nullable=False)
    dvc_hash = Column(String(128), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class PipelineRun(Base):
    __tablename__ = "pipeline_runs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dag_id = Column(String(64), nullable=False)
    dag_run_id = Column(String(128), nullable=False)
    status = Column(String(32), nullable=False) # "SUCCESS", "FAILED", "RUNNING"
    duration_seconds = Column(Float, nullable=True)
    triggered_by = Column(String(64), default="manual")
    created_at = Column(DateTime, default=datetime.utcnow)

class DriftReport(Base):
    __tablename__ = "drift_reports"

    id = Column(Integer, primary_key=True, autoincrement=True)
    drift_score = Column(Float, nullable=False)
    drift_detected = Column(Boolean, default=False)
    severity = Column(String(32), default="LOW") # "LOW", "MEDIUM", "HIGH"
    sample_count = Column(Integer, nullable=False)
    drifted_features = Column(JSON, nullable=True)
    evaluated_at = Column(DateTime, default=datetime.utcnow)

class RetrainingJob(Base):
    __tablename__ = "retraining_jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trigger_reason = Column(String(255), nullable=False) # "DATA_DRIFT", "MANUAL_REQUEST"
    dataset_version = Column(String(64), nullable=False)
    status = Column(String(32), default="REQUESTED") # "REQUESTED", "TRAINING", "EVALUATED", "PASSED", "PROMOTED", "REJECTED"
    candidate_metrics = Column(JSON, nullable=True)
    quality_gate_passed = Column(Boolean, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    action = Column(String(64), nullable=False) # "MODEL_PROMOTION", "RETRAINING_TRIGGER"
    performed_by = Column(String(64), default="system")
    details = Column(JSON, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
