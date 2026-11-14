"""
VisionQC Automated Training DAG
Orchestrates the complete ML training pipeline using reusable modules from ml/:
1. dataset_ingestion: verifies raw casting dataset availability
2. dataset_validation: checks image corruption, dimensions, and classes
3. data_preprocessing: executes reproducible stratified splitting
4. model_training: trains the computer vision model
5. model_evaluation: computes test set metrics (defect recall, FNR, latency)
6. mlflow_logging: logs parameters, metrics, and artifacts to MLflow
7. quality_gate: enforces minimum defect recall (>=0.95) and latency thresholds
8. model_registration: registers the model in MLflow Model Registry upon gate approval
"""

from datetime import datetime, timedelta
import sys
from pathlib import Path

# Add project root to path for standalone execution and DAG parsing
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
    from airflow.operators.bash import BashOperator
    AIRFLOW_AVAILABLE = True
except ImportError:
    AIRFLOW_AVAILABLE = False

default_args = {
    "owner": "visionqc_mlops",
    "depends_on_past": False,
    "start_date": datetime(2026, 11, 1),
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

if AIRFLOW_AVAILABLE:
    with DAG(
        dag_id="visionqc_training_pipeline",
        default_args=default_args,
        description="VisionQC automated computer vision training, evaluation, and registry pipeline",
        schedule_interval=None, # Triggered manually or by retraining triggers
        catchup=False,
        tags=["visionqc", "mlops", "defect_inspection", "training"]
    ) as dag:

        t1_ingest = BashOperator(
            task_id="dataset_ingestion",
            bash_command="python -m ml.pipeline_tasks dataset_ingestion"
        )

        t2_validate = BashOperator(
            task_id="dataset_validation",
            bash_command="python -m ml.pipeline_tasks dataset_validation"
        )

        t3_preprocess = BashOperator(
            task_id="data_preprocessing",
            bash_command="python -m ml.pipeline_tasks data_preprocessing"
        )

        t4_train = BashOperator(
            task_id="model_training",
            bash_command="python -m ml.pipeline_tasks model_training"
        )

        t5_quality_gate = BashOperator(
            task_id="quality_gate",
            bash_command="python -m ml.pipeline_tasks quality_gate"
        )

        t6_register = BashOperator(
            task_id="model_registration",
            bash_command="python -m ml.pipeline_tasks model_registration"
        )

        # Sequential dependency pipeline
        t1_ingest >> t2_validate >> t3_preprocess >> t4_train >> t5_quality_gate >> t6_register
else:
    # DAG Definition placeholder for local environment before full Airflow container starts
    print("Airflow package not locally installed in host venv (runs in Docker container).")
