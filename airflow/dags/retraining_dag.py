"""
VisionQC Retraining DAG
Automates retraining workflow when data drift is detected or new dataset version is released:
- Accepts new dataset version input
- Reuses shared validation and preprocessing
- Retrains candidate model
- Enforces quality gate comparison against active model
- Blocks automatic deployment if quality threshold fails
"""

from datetime import datetime, timedelta
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    from airflow import DAG
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
        dag_id="visionqc_retraining_pipeline",
        default_args=default_args,
        description="VisionQC controlled model retraining and evaluation pipeline",
        schedule_interval=None,
        catchup=False,
        tags=["visionqc", "mlops", "retraining"]
    ) as dag:

        t1_validate = BashOperator(
            task_id="retraining_dataset_validation",
            bash_command="python -m ml.pipeline_tasks dataset_validation"
        )

        t2_preprocess = BashOperator(
            task_id="retraining_preprocessing",
            bash_command="python -m ml.pipeline_tasks data_preprocessing"
        )

        t3_train = BashOperator(
            task_id="retraining_candidate_model",
            bash_command="python -m ml.pipeline_tasks model_training"
        )

        t4_quality_gate = BashOperator(
            task_id="retraining_quality_gate",
            bash_command="python -m ml.pipeline_tasks quality_gate"
        )

        t5_register = BashOperator(
            task_id="retraining_model_registration",
            bash_command="python -m ml.pipeline_tasks model_registration"
        )

        t1_validate >> t2_preprocess >> t3_train >> t4_quality_gate >> t5_register
