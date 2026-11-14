# VisionQC - Technical Stack & Architecture

**Document:** `techstack.md`  
**Version:** 1.1  
**Date:** 14 November 2026  
**Project:** VisionQC - Automated Manufacturing Defect Inspection & MLOps Platform  
**Purpose:** Define the technologies, frameworks, libraries, infrastructure and implementation decisions used to build VisionQC.

---

# 1. Technical Stack Overview

VisionQC will use a modular, Python-first architecture with a modern web frontend.

The system will be divided into five major areas:

1. Frontend: User interface and dashboard.
2. Backend: REST APIs, application logic and model serving.
3. Machine Learning: Image processing, training and inference.
4. MLOps Infrastructure: Dataset versioning, experiment tracking, orchestration and monitoring.
5. Deployment: Containerization, CI/CD and cloud integration.

## 1.1 Recommended Technology Stack

| Layer | Recommended Technology | Purpose |
|---|---|---|
| Frontend framework | Next.js 16 + React 19 | Dashboard and user interface |
| Language | TypeScript | Type-safe frontend development |
| Styling | Tailwind CSS | Responsive styling |
| UI components | shadcn/ui + Radix UI | Accessible reusable components |
| Icons | Lucide React | Consistent interface icons |
| Charts | Recharts | ML and operational visualizations |
| Animations | Framer Motion | Interface transitions and animations |
| Backend | FastAPI | REST API and model serving |
| Backend language | Python 3.12 or 3.13 | Application and ML development |
| Database | PostgreSQL 18 | Application data and metadata |
| ORM | SQLAlchemy 2.x | Database operations |
| Database migrations | Alembic | Schema versioning |
| ML framework | PyTorch | Model development and inference |
| Image processing | OpenCV + Pillow | Image validation and preprocessing |
| Evaluation | Scikit-learn | Model evaluation metrics |
| Explainability | Grad-CAM | Model prediction visualization |
| Dataset versioning | DVC + Git | Dataset reproducibility |
| Experiment tracking | MLflow | Experiment management |
| Pipeline orchestration | Apache Airflow | Automated training and retraining |
| Containerization | Docker | Application packaging |
| Service orchestration | Docker Compose | Local multi-service deployment |
| CI/CD | GitHub Actions | Automated testing and build validation |
| Metrics collection | Prometheus | Application and ML metrics |
| Monitoring dashboard | Grafana | Monitoring visualization |
| Cloud storage | AWS S3 | Dataset and model artifact storage |
| Cloud ML | AWS SageMaker | Optional managed ML execution |
| Cloud monitoring | AWS CloudWatch | Cloud logs and monitoring |
| Version control | Git + GitHub | Source code management |

**Version policy:** Use stable, supported releases rather than preview, beta or release-candidate versions. Pin actual dependency versions in lockfiles and dependency manifests after verifying compatibility.

---

# 2. Frontend Technology Stack

## 2.1 Next.js 16 + React 19

**Role:** Main frontend framework.

Next.js will be used to build the VisionQC dashboard and all user-facing pages.

### Why Next.js?

- Built on React and supports component-based development.
- Provides file-based routing through the App Router.
- Supports server and client components.
- Offers good TypeScript integration.
- Supports efficient rendering and code splitting.
- Provides a maintainable structure for a multi-page dashboard.

### Why not plain React with Vite?

Vite is an excellent choice for standalone frontend applications. However, VisionQC benefits from Next.js routing, server-side capabilities and structured application organization.

The dashboard will use Next.js rather than introducing multiple frontend frameworks.

## 2.2 TypeScript

**Role:** Frontend programming language.

TypeScript will be used instead of plain JavaScript.

Benefits:

- Detects many type-related errors during development.
- Provides better IDE autocomplete.
- Makes API response handling more predictable.
- Helps maintain reusable components.
- Improves collaboration between team members.

All API response types, component props and shared frontend interfaces should be defined using TypeScript.

## 2.3 Tailwind CSS

**Role:** Styling and responsive layout.

Tailwind CSS will provide utility-based styling.

Benefits:

- Consistent spacing and typography.
- Responsive dashboard layouts.
- Reusable design patterns.
- Faster interface development.
- Easy integration with component libraries.

## 2.4 shadcn/ui + Radix UI

**Role:** Reusable interface components.

These will be used for:

- Buttons.
- Dialogs.
- Dropdowns.
- Tabs.
- Tables.
- Tooltips.
- Select menus.
- Form controls.
- Navigation elements.

shadcn/ui provides customizable component source code, while Radix UI provides accessible interaction primitives.

## 2.5 Lucide React

**Role:** Icons.

Lucide will provide consistent icons across the application.

Examples:

- Dashboard.
- Database.
- Image inspection.
- Model registry.
- Pipelines.
- Monitoring.
- Settings.

Avoid mixing multiple icon libraries.

## 2.6 Recharts

**Role:** Data visualization.

Recharts will visualize:

- Prediction distribution.
- Model comparison.
- Accuracy and recall.
- Confidence distribution.
- API latency.
- Request volume.
- Drift measurements.
- Training history.

Charts must use actual API or monitoring data. Do not create fabricated performance metrics.

## 2.7 Framer Motion

**Role:** Animations and transitions.

Use it for:

- Page transitions.
- Dashboard panel transitions.
- Modal animations.
- Loading states.
- Expandable sections.
- Subtle interaction feedback.

Animations should improve usability without slowing down the dashboard.

---

# 3. Backend Technology Stack

## 3.1 FastAPI

**Role:** Main backend framework.

FastAPI will act as the central API layer connecting the frontend, ML model and supporting services.

### Why FastAPI?

- Native Python support.
- Good integration with PyTorch and OpenCV.
- Automatic API documentation through OpenAPI and Swagger UI.
- Request validation using Pydantic.
- Asynchronous endpoint support.
- Dependency injection for shared services.
- Strong support for structured API responses.

FastAPI is particularly suitable because the entire ML pipeline is already based on Python.

### Main backend responsibilities

1. Image upload and validation.
2. Image preprocessing.
3. Model inference.
4. Grad-CAM generation.
5. Prediction history.
6. Model information retrieval.
7. Dashboard data APIs.
8. Experiment and dataset information APIs.
9. Pipeline status integration.
10. Monitoring and drift information APIs.
11. Retraining workflow integration.

## 3.2 Python

**Recommended version:** Python 3.12 or 3.13, subject to compatibility testing.

Python will be used for:

- Backend development.
- ML model training.
- Image processing.
- Dataset validation.
- Drift detection.
- Airflow DAGs.
- MLflow integration.
- Grad-CAM.
- Automated testing.

Use one primary Python version across the backend, training and inference environments wherever the selected library versions permit it.

## 3.3 Pydantic

**Role:** Data validation and serialization.

Pydantic will validate:

- API request bodies.
- Prediction responses.
- Model metadata.
- Configuration values.
- Pipeline-related request data.

This reduces inconsistent data handling between the frontend and backend.

## 3.4 API Structure

The backend should use modular routers rather than placing every endpoint in one file.

Proposed API structure:

| Router | Responsibility |
|---|---|
| `/api/v1/inspection` | Image upload and predictions |
| `/api/v1/models` | Model information and deployed version |
| `/api/v1/experiments` | Experiment information from MLflow |
| `/api/v1/datasets` | Dataset metadata and versions |
| `/api/v1/pipelines` | Airflow pipeline information |
| `/api/v1/monitoring` | Operational and ML monitoring data |
| `/api/v1/drift` | Drift status and measurements |
| `/api/v1/retraining` | Retraining workflow information |

The core endpoints required by the PRD will remain available:

- `GET /health`
- `POST /predict`
- `GET /model-info`

They can be retained as compatibility routes while the versioned API is developed.

---

# 4. Database Technology Stack

## 4.1 PostgreSQL 18

**Role:** Primary application database.

PostgreSQL will store the operational and application data required by VisionQC.

### Why PostgreSQL?

- Reliable relational database.
- Supports structured and transactional data.
- Provides constraints and indexing.
- Supports complex queries and relationships.
- Suitable for prediction history, model deployment information and system metadata.
- Can run locally through Docker.
- Has a clear migration and upgrade path.

### What will PostgreSQL store?

| Table | Purpose |
|---|---|
| `predictions` | Inspection results and prediction metadata |
| `model_deployments` | Currently deployed model information |
| `dataset_versions` | Dataset metadata and version references |
| `pipeline_runs` | Pipeline execution summaries |
| `drift_reports` | Drift measurements and detection results |
| `retraining_jobs` | Retraining workflow information |
| `audit_logs` | Important system actions |

The final schema should be designed around the actual API workflows.

### What should NOT be stored directly in PostgreSQL?

Large binary files such as:

- Original training images.
- Uploaded image collections.
- Model weight files.
- Large training artifacts.

These should be stored in a filesystem or object storage.

PostgreSQL should store their paths, identifiers, hashes and relevant metadata.

## 4.2 SQLAlchemy 2.x

**Role:** Object Relational Mapper (ORM).

SQLAlchemy will connect FastAPI to PostgreSQL.

Benefits:

- Structured database access.
- Reusable database models.
- Transaction management.
- Relationship handling.
- Maintainable query logic.

## 4.3 Alembic

**Role:** Database schema migrations.

Alembic will track database structure changes.

For example:

- Adding a prediction column.
- Creating a new table.
- Updating a relationship.
- Changing a data type.

This avoids manually rebuilding the database whenever the schema changes.

## 4.4 Database Separation

The project will have separate database ownership for different services.

| Database | Owner | Purpose |
|---|---|---|
| `visionqc_app` | FastAPI | Predictions and application records |
| `visionqc_mlflow` | MLflow | Experiment and registry metadata |
| `visionqc_airflow` | Airflow | DAG execution and scheduler metadata |

These databases can run on the same PostgreSQL server during local development, but each service must have its own database and credentials.

This prevents MLflow and Airflow from directly managing application tables.

---

# 5. Machine Learning Technology Stack

## 5.1 PyTorch

**Role:** Model development, training and inference.

PyTorch will be used to build the three required architectures:

1. Custom CNN.
2. ResNet18.
3. EfficientNet-B0.

### Why PyTorch?

- Strong computer vision ecosystem.
- Flexible model architecture development.
- Good transfer-learning support.
- GPU acceleration when available.
- Integration with TorchVision.
- Straightforward inference implementation.

PyTorch will be the primary ML framework. Avoid maintaining separate implementations in TensorFlow or Keras.

## 5.2 TorchVision

**Role:** Pretrained model architectures and image transformations.

Used for:

- ResNet18.
- EfficientNet-B0.
- Pretrained weights.
- Image transformations.
- Dataset utilities.

## 5.3 OpenCV

**Role:** Image processing.

OpenCV will handle:

- Image reading.
- Image resizing.
- Grayscale conversion.
- Brightness adjustments.
- Contrast adjustments.
- Noise simulation.
- Blur simulation.
- Image statistical feature extraction.

## 5.4 Pillow

**Role:** Image loading and validation.

Pillow will be used where convenient for:

- Image decoding.
- Image format conversion.
- Basic image validation.
- Integration with Python image workflows.

## 5.5 Scikit-learn

**Role:** Model evaluation and statistical utilities.

Used for:

- Train/validation/test split utilities where appropriate.
- Precision.
- Recall.
- F1-score.
- ROC-AUC.
- PR-AUC.
- Confusion matrix.
- Classification threshold evaluation.
- Drift-related statistical calculations where appropriate.

## 5.6 Grad-CAM

**Role:** Model explainability.

Grad-CAM will generate heatmaps for supported CNN-based model architectures.

It will be used to:

1. Identify the relevant feature layer.
2. Calculate gradients for the selected class.
3. Generate a class activation map.
4. Resize the heatmap.
5. Overlay the heatmap on the original image.
6. Return the visualization to the frontend.

The implementation must be tested separately for each supported architecture.

---

# 6. Dataset Management and Versioning

## 6.1 DVC + Git

**Role:** Dataset and ML artifact versioning.

Git will track source code and configuration files.

DVC will track dataset versions and large ML-related files.

### Why DVC?

- Dataset changes can be versioned.
- Experiments can be associated with specific datasets.
- Large files need not be committed directly to Git.
- Dataset reproducibility improves.
- Supports local and remote storage.

### Recommended strategy

- Git: Source code, configuration and documentation.
- DVC: Dataset version metadata and data artifacts.
- Local storage: Initial dataset storage.
- AWS S3: Optional DVC remote for cloud demonstration.

### Dataset rules

1. Preserve the original dataset.
2. Validate image integrity.
3. Identify duplicate images.
4. Split original images before augmentation.
5. Apply augmentation only to training data.
6. Keep validation and test data unchanged.
7. Record the random seed.
8. Associate each experiment with a DVC revision.

The primary evaluation dataset must remain separate from augmented training data.

---

# 7. Experiment Tracking and Model Registry

## 7.1 MLflow

**Role:** Experiment tracking and model lifecycle management.

MLflow will record:

- Experiment names.
- Model architectures.
- Hyperparameters.
- Dataset versions.
- Training metrics.
- Evaluation metrics.
- Training artifacts.
- Model versions.
- Registration metadata.

### Why MLflow?

- Integrates directly with Python and PyTorch.
- Provides an experiment tracking interface.
- Supports artifact storage.
- Provides model registry functionality.
- Helps compare model runs.
- Improves reproducibility and traceability.

### MLflow responsibilities

| Component | Responsibility |
|---|---|
| Tracking | Record experiment parameters and metrics |
| Artifacts | Store model weights, plots and reports |
| Registry | Maintain approved model versions |
| Model metadata | Associate versions with datasets and metrics |

### Model promotion

The selected model should move through a controlled lifecycle:

`Training → Evaluation → Quality Gate → Registration → Approval → Deployment`

A model must not be promoted simply because its training completed successfully.

---

# 8. Pipeline Orchestration

## 8.1 Apache Airflow

**Role:** Automate training, evaluation and retraining workflows.

Airflow will orchestrate the ML lifecycle using Directed Acyclic Graphs (DAGs).

### Why Airflow?

- Supports task dependencies.
- Provides scheduled and manual execution.
- Offers retry and failure handling.
- Maintains pipeline execution history.
- Provides a visual DAG interface.
- Supports Python-based ML workflows.

### Main training DAG

The training DAG will contain:

1. Dataset ingestion.
2. Dataset validation.
3. Data preprocessing.
4. Data preparation.
5. Model training.
6. Model evaluation.
7. MLflow logging.
8. Model comparison.
9. Quality-gate validation.
10. Model registration.

### Retraining DAG

The retraining workflow will reuse the same training and evaluation logic with a new dataset version or training configuration.

### Important implementation rule

Airflow orchestrates the work. It should not contain all the ML training logic inside one large DAG file.

Training and evaluation logic should be implemented as reusable Python modules, which Airflow tasks invoke.

---

# 9. Backend Model Serving

## 9.1 FastAPI + PyTorch

FastAPI will load the selected approved model and expose inference endpoints.

### Prediction flow

1. Receive uploaded image.
2. Validate file size and content.
3. Decode the image.
4. Apply the same preprocessing used during training.
5. Load the active model if it is not already loaded.
6. Run inference.
7. Calculate defect probability.
8. Apply the configured classification threshold.
9. Measure inference latency.
10. Generate Grad-CAM when requested.
11. Save prediction metadata.
12. Return a structured JSON response.

### Model response structure

The response should contain:

- Prediction ID.
- Predicted class.
- Defect probability.
- Decision recommendation.
- Model name.
- Model version.
- Inference latency.
- Optional Grad-CAM reference.

Do not return model weights or internal infrastructure credentials through the API.

### Model loading strategy

Load the active model during application startup or through a controlled model-loading mechanism.

Avoid reloading the complete model for every prediction.

Model version changes should be handled through a controlled deployment or reload process.

---

# 10. Monitoring and Observability

## 10.1 Prometheus

**Role:** Metrics collection.

Prometheus will collect metrics exposed by the FastAPI application and other instrumented services.

### Metrics to expose

- Total requests.
- Successful requests.
- Failed requests.
- API error rate.
- Inference latency.
- Request throughput.
- Prediction class counts.
- Confidence distribution.
- Service health.

Use appropriate metric types:

- Counter: Total requests and errors.
- Gauge: Current service or drift status.
- Histogram: Inference latency.

Avoid creating excessive metric labels with unique values such as image IDs.

## 10.2 Grafana

**Role:** Monitoring visualization.

Grafana will provide dashboards for:

### Operational monitoring

- Request volume.
- API errors.
- Latency.
- Service availability.
- Throughput.

### ML monitoring

- OK predictions.
- DEFECTIVE predictions.
- Confidence distribution.
- Drift measurements.
- Model version information where available.

Grafana will retrieve metrics from Prometheus and can use other appropriate data sources when necessary.

## 10.3 Drift Detection

**Role:** Identify changes in incoming image distributions.

Use OpenCV and Python statistical utilities to extract image features such as:

- Mean brightness.
- Standard deviation.
- Contrast-related statistics.
- Image sharpness.
- Selected image histogram values.

Compare reference and incoming distributions using a documented method.

The drift component should:

1. Establish a reference dataset.
2. Collect incoming image batches.
3. Extract image statistics.
4. Compare distributions.
5. Calculate drift scores.
6. Apply configurable thresholds.
7. Record the result.
8. Expose drift metrics for Grafana.

Drift detection must be treated separately from verified model performance. Without ground-truth labels, the system cannot claim that accuracy has declined.

---

# 11. CI/CD Technology Stack

## 11.1 GitHub Actions

**Role:** Automated code validation and CI/CD.

GitHub Actions will execute automated workflows whenever code is pushed or a pull request is opened.

### Recommended workflow

1. Checkout repository.
2. Set up Python.
3. Install dependencies.
4. Run linting and formatting checks.
5. Run preprocessing tests.
6. Run prediction tests.
7. Run API tests.
8. Run configuration and integration checks.
9. Build Docker images.
10. Run applicable service health checks.
11. Report workflow status.

### Model-quality validation

Where model artifacts are available, a separate validation workflow should check required model metadata and evaluation thresholds before promotion.

### Why GitHub Actions?

- Direct integration with GitHub.
- Supports automated testing.
- Supports Docker image builds.
- No separate CI/CD server is required.
- Suitable for the scope of this academic project.

**Final decision:** GitHub Actions is the required CI/CD tool. Jenkins is not required and will not be added to the initial architecture.

---

# 12. Containerization and Local Deployment

## 12.1 Docker

**Role:** Package application components into containers.

Docker will package:

- Frontend.
- FastAPI.
- MLflow.
- Airflow.
- Prometheus.
- Grafana.
- PostgreSQL.

Each service should have an appropriate Docker configuration.

## 12.2 Docker Compose

**Role:** Manage the complete local environment.

Docker Compose will define:

- Services.
- Networks.
- Volumes.
- Environment variables.
- Health checks.
- Startup dependencies.
- Port mappings.

### Recommended local services

| Service | Container Responsibility |
|---|---|
| `frontend` | Next.js dashboard |
| `backend` | FastAPI application |
| `postgres` | Application and service databases |
| `mlflow` | Experiment tracking and model registry |
| `airflow-webserver` | Airflow web interface |
| `airflow-scheduler` | DAG scheduling |
| `airflow-worker` | Task execution, if using a distributed executor |
| `prometheus` | Metrics collection |
| `grafana` | Monitoring dashboards |

The exact Airflow service configuration depends on the selected executor. For a smaller local setup, use a lightweight supported configuration rather than deploying unnecessary workers.

### Storage

Use Docker volumes for persistent data such as:

- PostgreSQL database files.
- MLflow artifacts.
- Airflow logs.
- Grafana configuration.
- Prometheus data.

Use mounted local directories or DVC-managed storage for datasets and model artifacts.

### Resource management

Airflow, MLflow, PostgreSQL and Grafana can consume significant memory.

Start only the services needed for the current development phase. The full stack should be started for integration testing and final demonstrations.

---

# 13. Deployment Strategy

VisionQC will follow a local-first deployment strategy with an optional AWS extension.

## 13.1 Phase 1: Local Development

**Recommended setup:** Docker Compose.

All required services should run locally.

Benefits:

- No cloud dependency.
- No mandatory paid infrastructure.
- Easier debugging.
- Reproducible environment.
- Suitable for development and academic evaluation.

The project should be fully demonstrable on a local machine.

## 13.2 Phase 2: Cloud Demonstration

**Recommended platform:** AWS.

| Service | Purpose |
|---|---|
| AWS ECR | Store Docker images |
| AWS ECS Fargate | Run containerized application services |
| AWS S3 | Store datasets and model artifacts |
| AWS RDS PostgreSQL | Managed application database |
| AWS CloudWatch | Logs and operational monitoring |
| AWS SageMaker | Optional managed ML training or deployment |

### Deployment approach

1. Build Docker images.
2. Push images to ECR.
3. Configure the application environment.
4. Deploy supported services to ECS Fargate.
5. Store required artifacts in S3.
6. Configure database connectivity.
7. Collect logs through CloudWatch.
8. Validate health endpoints.
9. Demonstrate the deployed application.

### Important AWS decision

The AWS implementation is an extension, not a prerequisite.

Airflow deployment should be treated as a separate infrastructure task. Managed Airflow can introduce significant cost and setup complexity, so it is not mandatory for the academic cloud demonstration.

All cloud resources should be stopped or deleted after the demonstration where appropriate.

---

# 14. Project Architecture

## 14.1 High-Level Architecture

```text
                     USER
                       |
                       v
              NEXT.JS FRONTEND
                       |
                       v
                 FASTAPI BACKEND
                       |
        +--------------+---------------+
        |              |               |
        v              v               v
    INSPECTION     DASHBOARD       MODEL INFO
        |              |               |
        v              +---------------+
   PYTORCH MODEL              |
        |                     |
        v                     v
   PREDICTION              POSTGRESQL
        |                     |
        +---------------------+
                       |
          +------------+------------+
          |            |            |
          v            v            v
       MLFLOW       AIRFLOW      MONITORING
          |            |            |
          v            v            v
       MODEL        TRAINING     PROMETHEUS
      REGISTRY      PIPELINE         |
                       |             v
                       v          GRAFANA
                   PYTORCH
                       |
                       v
                   DVC DATASET
```

This is a logical architecture. The individual services may communicate through APIs, shared storage or controlled pipeline interfaces depending on their responsibilities.

## 14.2 Separation of Responsibilities

| Technology | Responsibility |
|---|---|
| Next.js | User interface |
| FastAPI | Application APIs and model serving |
| PostgreSQL | Application persistence |
| PyTorch | Model training and inference |
| DVC | Dataset versioning |
| MLflow | Experiment tracking and model registry |
| Airflow | Pipeline orchestration |
| Docker | Container packaging |
| Docker Compose | Local service orchestration |
| GitHub Actions | Code CI/CD |
| Prometheus | Metrics collection |
| Grafana | Monitoring visualization |
| AWS | Optional cloud infrastructure |

Do not duplicate the responsibilities of these services.

---

# 15. Recommended Project Folder Structure

The repository should follow a modular structure.

```text
VisionQC/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── hooks/
│   ├── lib/
│   ├── services/
│   ├── types/
│   ├── public/
│   ├── package.json
│   └── tsconfig.json
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   ├── tests/
│   ├── alembic/
│   ├── requirements.txt
│   └── Dockerfile
│
├── ml/
│   ├── data/
│   ├── preprocessing/
│   ├── models/
│   │   ├── custom_cnn.py
│   │   ├── resnet18.py
│   │   └── efficientnet_b0.py
│   ├── training/
│   ├── evaluation/
│   ├── explainability/
│   ├── inference/
│   └── drift/
│
├── airflow/
│   ├── dags/
│   ├── plugins/
│   └── config/
│
├── monitoring/
│   ├── prometheus/
│   └── grafana/
│
├── configs/
│   ├── model_config.yaml
│   ├── training_config.yaml
│   └── preprocessing_config.yaml
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── model_quality/
│
├── docs/
│   ├── architecture.md
│   ├── data-card.md
│   ├── model-card.md
│   └── performance-report.md
│
├── scripts/
│
├── .github/
│   └── workflows/
│
├── dvc.yaml
├── params.yaml
├── docker-compose.yml
├── .env.example
├── .gitignore
├── README.md
├── prd.md
├── techstack.md
└── todo.md
```

The folder structure may evolve during implementation, but frontend, backend, ML and infrastructure code should remain logically separated.

---

# 16. Development and Testing Tools

The following tools are recommended for the development process.

| Tool | Purpose |
|---|---|
| VS Code | Main code editor |
| Git | Version control |
| GitHub | Repository and collaboration |
| Postman | API testing |
| Swagger UI | FastAPI API documentation |
| pgAdmin or DBeaver | PostgreSQL management |
| Docker Desktop | Local containers |
| Python virtual environment | Python dependency isolation |
| Ruff | Python linting and formatting |
| Pytest | Python automated testing |
| ESLint | Frontend linting |
| Prettier | Frontend formatting |
| Playwright | Frontend end-to-end testing |
| Antigravity | AI-assisted development |

These tools support development and testing. They do not replace the actual application architecture.

---

# 17. Environment Configuration

Use environment variables for configuration.

A `.env.example` file should document the required variable names without containing real credentials.

Example:

```env
# Application
APP_ENV=development

# Database
DATABASE_URL=postgresql+psycopg://visionqc_user:password@postgres:5432/visionqc_app

# MLflow
MLFLOW_TRACKING_URI=http://mlflow:5000

# Airflow
AIRFLOW_BASE_URL=http://airflow-webserver:8080

# Prometheus
PROMETHEUS_URL=http://prometheus:9090

# Frontend
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api/v1

# AWS - Optional
AWS_REGION=ap-south-1
AWS_S3_BUCKET=
```

Actual configuration must be adjusted for the selected deployment environment.

**Important:**

- Never commit `.env`.
- Keep `.env.example` in Git.
- Use separate credentials for separate services.
- Use Docker service names for internal container communication.
- Use `localhost` only for host-to-container access.
- Never place secret values in `NEXT_PUBLIC_` variables.

---

# 18. Dependency and Compatibility Management

The project must use controlled dependency versions.

### Python

- Maintain a Python version policy.
- Pin dependencies in a lockfile or fully resolved requirements file.
- Test PyTorch, TorchVision, OpenCV, FastAPI and Airflow compatibility.
- Keep ML and API dependencies separated where practical.

### Frontend

- Use a supported Node.js LTS release compatible with the selected Next.js version.
- Commit the package manager lockfile.
- Avoid unverified package upgrades during integration.

### Containers

- Use maintained base images.
- Pin important service image versions.
- Avoid relying on `latest` tags for reproducible builds.
- Rebuild images after security updates.

### Database

- Use PostgreSQL migrations.
- Back up important data.
- Keep service databases separated.
- Test schema migrations before deployment.

---

# 19. Technology Decisions and Alternatives

| Area | Selected Technology | Alternative Considered | Reason for Selection |
|---|---|---|---|
| Frontend | Next.js | React + Vite | Structured dashboard and App Router |
| Language | TypeScript | JavaScript | Type safety and maintainability |
| Backend | FastAPI | Django REST Framework | Python and ML integration |
| Database | PostgreSQL | SQLite / MongoDB | Relational application data and service compatibility |
| ORM | SQLAlchemy | Prisma | Native Python backend integration |
| ML framework | PyTorch | TensorFlow | Flexible computer vision workflow |
| Data versioning | DVC | Git LFS | Dataset-aware ML versioning |
| Experiment tracking | MLflow | Weights & Biases | Local-first experiment tracking and registry |
| Orchestration | Airflow | Prefect | Explicit PRD requirement and DAG visibility |
| Serving | FastAPI | TorchServe | Custom API and application integration |
| CI/CD | GitHub Actions | Jenkins | Required by course scope and direct GitHub integration |
| Monitoring | Prometheus | Datadog | Local metrics collection |
| Visualization | Grafana | Kibana | Prometheus integration |
| Deployment | Docker Compose | Kubernetes | Appropriate complexity for an academic prototype |
| Cloud | AWS | Azure / GCP | Matches the PRD's AWS extension |

---

# 20. Final Technical Decisions

The following decisions form the approved technical baseline.

| Category | Final Decision |
|---|---|
| Frontend | Next.js 16 + React 19 + TypeScript |
| Styling | Tailwind CSS |
| Components | shadcn/ui + Radix UI |
| Charts | Recharts |
| Animations | Framer Motion |
| Backend | FastAPI |
| Language | Python 3.12 or 3.13 |
| Database | PostgreSQL 18 |
| ORM | SQLAlchemy 2.x |
| Migrations | Alembic |
| ML | PyTorch |
| Image processing | OpenCV + Pillow |
| Evaluation | Scikit-learn |
| Explainability | Grad-CAM |
| Data versioning | DVC + Git |
| Experiment tracking | MLflow |
| Orchestration | Apache Airflow |
| API serving | FastAPI |
| Containerization | Docker |
| Local deployment | Docker Compose |
| CI/CD | GitHub Actions |
| Metrics | Prometheus |
| Monitoring UI | Grafana |
| Cloud storage | AWS S3 |
| Cloud deployment | AWS ECS Fargate + ECR |
| Managed database | AWS RDS PostgreSQL |
| Cloud monitoring | AWS CloudWatch |
| Optional managed ML | AWS SageMaker |

---

# 21. Implementation Principles

All development work should follow these principles:

1. **Local-first:** The complete academic demonstration must work without AWS.
2. **Modular architecture:** Keep frontend, backend, ML and infrastructure separate.
3. **Single source of truth:** The PRD defines product behavior; this document defines implementation choices.
4. **Reproducibility:** Track datasets, model configurations, dependencies and experiments.
5. **Real data:** Dashboard metrics must come from actual services and measured results.
6. **Controlled promotion:** A trained model cannot become the deployed model without passing quality gates.
7. **Data validation:** Validate image uploads and maintain consistent preprocessing.
8. **Incremental integration:** Build and test individual services before integrating the full system.
9. **Maintainability:** Prefer readable, reusable modules over unnecessary abstraction.
10. **Scope control:** Do not introduce additional infrastructure unless it directly supports a PRD requirement.

---

# 22. Relationship Between Project Documents

The three main project documents must remain consistent.

| Document | Responsibility |
|---|---|
| `prd.md` | What VisionQC must achieve |
| `techstack.md` | Which technologies and architectural decisions implement it |
| `todo.md` | What developers must build, configure, test and deliver |

Any changes to the product requirements should first be reflected in the PRD, then checked against the technical stack and implementation tasks.

---

**Document status:** Recommended technical architecture baseline.

**Final recommendation:** Build VisionQC using Next.js, FastAPI, PostgreSQL, PyTorch, DVC, MLflow, Airflow, Docker Compose, GitHub Actions, Prometheus and Grafana. Keep AWS as an optional extension.

The stack is intentionally powerful enough to demonstrate a complete MLOps lifecycle without introducing unnecessary enterprise infrastructure.