# VISIONqc: Industrial Pump Impeller Defect Inspection & MLOps Platform

[![VISIONqc CI Pipeline](https://github.com/shubhambharnuke/VISIONqc/actions/workflows/ci.yml/badge.svg)](https://github.com/shubhambharnuke/VISIONqc/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Next.js 16](https://img.shields.io/badge/Next.js-16-black.svg)](https://nextjs.org/)
[![MLflow 3.10](https://img.shields.io/badge/MLflow-3.10-0194E2.svg)](https://mlflow.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](https://www.docker.com/)

VisionQC is an end-to-end industrial MLOps platform engineered for automated casting defect inspection of submersible pump impellers. It replaces manual inspection with high-precision computer vision (100% Defect Recall, 0 False Negatives), explainable Grad-CAM heatmaps, automated Airflow retraining pipelines, and full observability.

---

## Key Highlights & Performance

- **Champion Model:** EfficientNet-B0 (Transfer Learning) with 4.01M parameters.
- **Defect Recall:** **100.0%** (117 / 117 defect samples detected on holdout test set).
- **False Negative Rate:** **0.00%** (Zero missed defective impellers).
- **Inference Latency:** **24.86 ms** per image (P95 latency well within the <100ms industrial target).
- **Explainability:** 3-mode Grad-CAM localization (Original, Heatmap, Overlay) showing exact casting flaws.
- **Dataset Versioning:** 1,300 images (519 OK, 781 DEFECTIVE) versioned with DVC (`dataset-v1.0`).
- **Orchestration:** Airflow DAGs for model training, scheduled retraining, quality gates, and MLflow registry.
- **Observability:** Prometheus instrumentation (`/metrics`), Grafana dashboards, and Kolmogorov-Smirnov statistical feature drift detection.

---

## Repository Structure

```text
VISIONqc/
├── frontend/               # Next.js 16 App Router UI (React 19, TypeScript, Tailwind)
│   ├── src/app/            # 9 Workstation routes: Overview, Inspection, Experiments, etc.
│   └── Dockerfile          # Multi-stage production build
├── backend/                # FastAPI serving engine & SQLAlchemy ORM
│   ├── app/                # Routers, schemas, connection pools, model service
│   └── Dockerfile          # Slim container with PyTorch and OpenCV
├── ml/                     # Machine Learning engine
│   ├── models/             # Custom CNN, ResNet18, EfficientNet-B0
│   ├── preprocessing/      # Dataset validation, canonical transforms, stratified split
│   ├── explainability/     # Grad-CAM module
│   ├── training/           # PyTorch training loops & MLflow tracking utilities
│   ├── evaluation/         # Strict quality gate evaluator & comparative report
│   └── drift/              # Image feature extractor & Kolmogorov-Smirnov detector
├── airflow/                # Orchestration DAGs
│   └── dags/               # training_dag.py & retraining_dag.py
├── monitoring/             # Observability
│   ├── prometheus/         # Prometheus scrape configuration
│   └── grafana/            # Grafana datasource provisioning
├── configs/                # Preprocessing, training, and model configs (YAML)
├── docs/                   # Data Card, Model Card, Performance Report, Architecture
├── tests/unit/             # Pytest test suite (16 passing tests)
├── docker-compose.yml      # Orchestrates Postgres, Backend, Frontend, Prometheus, Grafana
└── dvc.yaml                # DVC data pipeline manifest
```

---

## Quickstart & Local Setup

### 1. Prerequisites
- Python 3.12+
- Node.js 20+ & npm
- Docker Desktop (for full containerized stack)

### 2. Clone and Install Dependencies
```bash
git clone https://github.com/shubhambharnuke/VISIONqc.git
cd VISIONqc

# Python virtual environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Frontend dependencies
cd frontend
npm install
cd ..
```

### 3. Run Automated Tests
```bash
python -m pytest tests/unit/ -v
```
All 16 unit tests across preprocessing, model architectures, Grad-CAM, drift detection, and FastAPI endpoints will execute and pass.

### 4. Start Local Services

**Option A: Run Directly on Host**
```bash
# Terminal 1 - FastAPI Backend
python -m uvicorn backend.app.main:app --reload --port 8000

# Terminal 2 - Next.js Frontend
cd frontend
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) for the VisionQC Industrial Dashboard and [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive Swagger API documentation.

**Option B: Launch Complete Stack via Docker Compose**
```bash
docker compose up -d --build
```
- **Frontend Dashboard:** [http://localhost:3000](http://localhost:3000)
- **FastAPI API & Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Prometheus Metrics:** [http://localhost:9090](http://localhost:9090)
- **Grafana Monitoring:** [http://localhost:3001](http://localhost:3001) (Credentials: `admin` / `admin`)
- **PostgreSQL 16:** `localhost:5432`

---

## Quality Gate Criteria

A trained model candidate must satisfy all strict manufacturing thresholds to be promoted to `Production`:

| Gate Criterion | Requirement | EfficientNet-B0 Score | Result |
|---|---|---|---|
| Defect Recall | ≥ 95.0% | **100.0%** | **PASSED** |
| Accuracy | ≥ 90.0% | **100.0%** | **PASSED** |
| F1 Score | ≥ 0.90 | **1.000** | **PASSED** |
| False Negative Rate | ≤ 5.0% | **0.00%** | **PASSED** |
| Inference Latency | ≤ 100.0 ms | **24.86 ms** | **PASSED** |

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
