# VisionQC: Automated Impeller Visual Inspection Platform System Architecture

## 1. System Overview
VisionQC is an industrial-grade MLOps manufacturing quality control system engineered specifically for cast submersible pump impellers. It automates surface defect classification (burrs, pinholes, casting shrinkages) and bridges deep learning with automated ML lifecycle governance.

```
                           +-----------------------------------+
                           |        Industrial Camera /        |
                           |       Station Image Ingestion     |
                           +-----------------+-----------------+
                                             |
                                             v
                           +-----------------+-----------------+
                           |        Next.js 16 AppShell        |
                           |   (React 19, TypeScript, Tailwind)|
                           |  - Inspection Workbench (Grad-CAM)|
                           |  - Model Registry & Governance    |
                           |  - Operational & Drift Monitoring |
                           +-----------------+-----------------+
                                             |
                         REST API (HTTP / JSON / Multipart)
                                             |
                                             v
+--------------------------------------------+---------------------------------------------+
|                                    FastAPI Serving Backend                               |
|                                                                                          |
|  +--------------------+   +-----------------------+   +-------------------------------+  |
|  | /health & /metrics |   | /api/v1/inspection    |   | /api/v1/models & /experiments |  |
|  +--------------------+   +-----------+-----------+   +---------------+---------------+  |
|                                       |                               |                  |
|                                       v                               v                  |
|                       +---------------+---------------+   +-----------+---------------+  |
|                       |  PyTorch EfficientNet-B0     |   |   PostgreSQL 16 / SQLite  |  |
|                       |  - Canonical Preprocessing   |   |   - Predictions History   |  |
|                       |  - Grad-CAM 3-Mode Heatmaps  |   |   - Model Deployments     |  |
|                       |  - Latency: 24.8 ms / image  |   |   - Drift Records         |  |
|                       +---------------+---------------+   +---------------------------+  |
+---------------------------------------+--------------------------------------------------+
                                        |
                 +----------------------+----------------------+
                 |                                             |
                 v                                             v
+----------------+----------------+           +----------------+----------------+
|       MLflow 3.10 Registry      |           |     Apache Airflow 2.10 DAGs    |
| - Champion: EfficientNet-B0     |           | - Training DAG                  |
| - Run Metrics & Checkpoints     |           | - Retraining Pipeline           |
| - Stage: Production (v1)        |           | - Quality Gate (Recall >= 95%)  |
+---------------------------------+           +---------------------------------+
                 |                                             |
                 +----------------------+----------------------+
                                        |
                                        v
                      +-----------------+-----------------+
                      |     Prometheus & Grafana 10.4     |
                      | - Request Counters                |
                      | - P95 Latency & Throughput        |
                      | - Kolmogorov-Smirnov Feature Drift|
                      +-----------------------------------+
```

## 2. Core Subsystems & Components

### 2.1 Machine Learning & Explainability Pipeline
- **Champion Architecture:** EfficientNet-B0 (4.01M parameters) transfer-learned with fine-tuning.
- **Defect Recall:** 100.0% on test holdout (0 false negatives).
- **Latency:** 24.8 ms/image on standard CPU.
- **Explainability:** Real-time Grad-CAM outputting original, heatmap, and overlay images saved to static directories.

### 2.2 Data Engine & DVC
- **Tracking:** 1,300 pump impeller images (519 OK, 781 DEFECTIVE).
- **Split:** 70% Train (910), 15% Validation (195), 15% Test (195) stratified.
- **DVC Pointers:** `ml/data/raw.dvc` committed to Git.

### 2.3 Serving & Persistence API
- **FastAPI:** Async REST engine with CORS, Pydantic v2 schemas, and dependency injection.
- **Database:** SQLAlchemy 2.x ORM models mapped to PostgreSQL with SQLite fallback.
- **Prometheus Metrics:** Integrated metrics exporter at `/metrics`.

### 2.4 Industrial Frontend Dashboard
- **Stack:** Next.js 16 (Turbopack, App Router), React 19, TypeScript, Tailwind CSS, Lucide React.
- **Theme:** Industrial blue-grey palette (`#111820` Ink, `#202A35` Graphite, `#476985` Steel Blue, `#F3F4F6` Paper).
- **Nine Workstations:** Overview, Inspection Workbench, Experiments, Datasets, Pipelines, Model Registry, Monitoring, Retraining, Documentation.
