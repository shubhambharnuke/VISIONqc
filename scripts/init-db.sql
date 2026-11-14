-- PostgreSQL Initialization Script for VisionQC Multi-Database Architecture
-- Creates separate databases for application state, MLflow tracking, and Airflow orchestration.

CREATE DATABASE visionqc_mlflow;
GRANT ALL PRIVILEGES ON DATABASE visionqc_mlflow TO visionqc;

CREATE DATABASE visionqc_airflow;
GRANT ALL PRIVILEGES ON DATABASE visionqc_airflow TO visionqc;
