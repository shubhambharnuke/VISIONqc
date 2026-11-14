"""
VisionQC Core Application Settings
Managed via pydantic-settings from environment variables with safe defaults.
"""

from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    APP_ENV: str = "development"
    PROJECT_NAME: str = "VisionQC"
    API_V1_STR: str = "/api/v1"
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Database
    DATABASE_URL: str = "sqlite:///./visionqc_app.db" # Default fallback to SQLite, PostgreSQL in Docker/Prod

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000"
    ]

    # MLflow
    MLFLOW_TRACKING_URI: str = "sqlite:///mlflow.db"

    # Airflow
    AIRFLOW_BASE_URL: str = "http://airflow-webserver:8080/api/v1"

    # Monitoring
    PROMETHEUS_METRICS_ENABLED: bool = True

settings = Settings()
