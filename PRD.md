# Product Requirements Document (PRD)
# VisionQC: Automated Manufacturing Defect Inspection & MLOps Platform

**Version:** 1.0  
**Date:** 14 November 2026  
**Project Type:** MLOps Course Project  
**Domain:** Manufacturing Quality Inspection  
**Team Size:** 4 Members

---

# 1. Executive Summary

VisionQC is an end-to-end Machine Learning Operations platform designed to automate the visual quality inspection of cast pump impellers.

The system accepts an image of a pump impeller and uses a trained computer vision model to classify it into one of two categories:

- **OK:** The component appears acceptable.
- **DEFECTIVE:** The component exhibits visual characteristics associated with defects.

Unlike a conventional machine learning project that ends after training a model and reporting its accuracy, VisionQC implements the complete machine learning lifecycle.

It integrates dataset versioning, model experimentation, experiment tracking, automated pipeline orchestration, model deployment, CI/CD, production monitoring, drift detection and controlled model retraining.

The platform will also provide a frontend dashboard through which users can interact with the inspection service, examine model predictions, track experiments, monitor pipeline execution and understand the overall operational status of the ML system.

The central objective is to demonstrate how a machine learning model can be developed, deployed, monitored and continuously improved through a reproducible and automated engineering workflow.

## 1.1 Problem Statement

Traditional manufacturing quality inspection often involves manual examination of components.

This process can introduce several challenges:

1. Inspection may be time-consuming when large numbers of components need to be checked.
2. Human inspection can vary depending on workload and attention.
3. Defects may be overlooked during repetitive inspection.
4. Inspection decisions may lack consistent digital traceability.
5. Updating an inspection model can require manual intervention.
6. There may be limited visibility into model performance after deployment.

VisionQC addresses these challenges by introducing a computer-vision-based inspection system supported by an MLOps infrastructure.

The platform aims to provide consistent image-based predictions, explainability, model traceability and automated operational monitoring.

**Important:** VisionQC is an academic prototype and decision-support system. It will not directly control manufacturing machinery or autonomously reject physical components.

# 2. Product Vision

To build a reproducible, observable and automated machine learning platform that demonstrates how computer vision can support industrial quality inspection throughout the complete ML lifecycle.

## 2.1 Product Goals

| ID | Goal | Expected Outcome |
|---|---|---|
| G1 | Automated inspection | Classify impeller images as OK or DEFECTIVE |
| G2 | Reproducibility | Maintain consistent datasets, experiments and environments |
| G3 | Model comparison | Evaluate multiple ML architectures objectively |
| G4 | Workflow automation | Automate training and evaluation through Airflow |
| G5 | Model lifecycle management | Track and register models using MLflow |
| G6 | Deployment | Provide predictions through a FastAPI REST API |
| G7 | CI/CD | Automate testing and build validation using GitHub Actions |
| G8 | Monitoring | Monitor service health and model behavior |
| G9 | Continuous improvement | Detect drift and support controlled retraining |
| G10 | Explainability | Explain predictions through Grad-CAM |
| G11 | Cloud integration | Demonstrate AWS-based storage, ML execution and monitoring |

## 2.2 Product Objectives

The completed platform should allow a user to:

- Upload an impeller image and receive a classification.
- View the probability/confidence associated with the prediction.
- Understand the classification through a Grad-CAM visualization.
- Identify which model version generated the prediction.
- Compare model experiments and evaluation metrics.
- Observe the status of automated training pipelines.
- Monitor API performance and model prediction behavior.
- Detect simulated data drift.
- Trigger or execute a controlled retraining workflow.
- Inspect the model registry and deployment status.

# 3. Target Users and User Personas

VisionQC has three primary user personas.

## 3.1 Quality Inspector

**Primary responsibility:** Inspect manufactured components.

**Needs:**
- Upload images.
- Receive predictions.
- Examine explanations.
- Review inspection results.

## 3.2 ML Engineer / Data Scientist

**Primary responsibility:** Develop and improve machine learning models.

**Needs:**
- Manage datasets.
- Compare experiments.
- Evaluate model quality.
- Inspect model versions.
- Retrain models.

## 3.3 MLOps / System Administrator

**Primary responsibility:** Maintain the operational ML infrastructure.

**Needs:**
- Monitor services.
- Monitor pipeline execution.
- Track API performance.
- Monitor deployment health.
- Identify errors and drift.

# 4. User Stories

User stories describe the expected capabilities from the perspective of each user.

## 4.1 Image Inspection Module

| ID | User Story | Priority |
|---|---|---|
| US-01 | As an inspector, I want to upload an impeller image so that I can obtain an automated quality prediction. | P0 |
| US-02 | As an inspector, I want to see whether the component is OK or DEFECTIVE. | P0 |
| US-03 | As an inspector, I want to see the defect probability and confidence information. | P0 |
| US-04 | As an inspector, I want to see a Grad-CAM visualization to understand which image regions influenced the prediction. | P1 |
| US-05 | As an inspector, I want to know which model version generated the prediction. | P1 |
| US-06 | As an inspector, I want invalid or unsupported images to produce understandable error messages. | P0 |
| US-07 | As an inspector, I want to see inference latency so that I can understand prediction speed. | P1 |

## 4.2 Dataset Management

| ID | User Story | Priority |
|---|---|---|
| US-08 | As an ML engineer, I want to maintain versioned datasets using DVC. | P0 |
| US-09 | As an ML engineer, I want to validate image dimensions, labels, duplicates and corrupted files before training. | P0 |
| US-10 | As an ML engineer, I want reproducible train, validation and test splits. | P0 |
| US-11 | As an ML engineer, I want augmentation to be applied only to training data. | P0 |
| US-12 | As an ML engineer, I want to associate every experiment with its dataset version. | P0 |

## 4.3 Model Development and Experiment Tracking

| ID | User Story | Priority |
|---|---|---|
| US-13 | As an ML engineer, I want to train a baseline CNN model. | P0 |
| US-14 | As an ML engineer, I want to train ResNet18 and EfficientNet-B0 candidate models. | P0 |
| US-15 | As an ML engineer, I want to compare models using precision, recall, F1-score and AUC. | P0 |
| US-16 | As an ML engineer, I want to track model parameters, metrics and artifacts using MLflow. | P0 |
| US-17 | As an ML engineer, I want to register the selected model with version information. | P0 |
| US-18 | As an ML engineer, I want to optimize the classification threshold based on validation performance. | P1 |

## 4.4 Pipeline Automation

| ID | User Story | Priority |
|---|---|---|
| US-19 | As an MLOps engineer, I want an Airflow DAG to automate the complete training workflow. | P0 |
| US-20 | As an MLOps engineer, I want to see the execution status of every pipeline task. | P0 |
| US-21 | As an MLOps engineer, I want failed pipeline tasks to be identifiable and retryable. | P1 |
| US-22 | As an MLOps engineer, I want models to be registered only after passing evaluation thresholds. | P0 |
| US-23 | As an MLOps engineer, I want retraining to follow the same reproducible pipeline. | P1 |

## 4.5 Deployment and CI/CD

| ID | User Story | Priority |
|---|---|---|
| US-24 | As a developer, I want to expose predictions through FastAPI. | P0 |
| US-25 | As a developer, I want API input validation and error handling. | P0 |
| US-26 | As a developer, I want the application and supporting services to run through Docker Compose. | P0 |
| US-27 | As a developer, I want GitHub Actions to run automated tests when code is pushed or a pull request is opened. | P0 |
| US-28 | As a developer, I want model-quality checks to prevent unsuitable models from being promoted. | P0 |

## 4.6 Monitoring and Drift Detection

| ID | User Story | Priority |
|---|---|---|
| US-29 | As an administrator, I want to monitor API requests, errors and inference latency. | P0 |
| US-30 | As an administrator, I want to monitor OK and DEFECTIVE prediction distributions. | P0 |
| US-31 | As an administrator, I want to detect changes in incoming image distributions. | P0 |
| US-32 | As an administrator, I want to visualize operational metrics in Grafana. | P0 |
| US-33 | As an ML engineer, I want to simulate changes in image brightness, contrast, noise and blur. | P1 |
| US-34 | As an ML engineer, I want to initiate retraining when drift or model-performance degradation warrants it. | P1 |
| US-35 | As an ML engineer, I want retrained models to pass quality checks before deployment. | P0 |

## 4.7 Responsible AI and Documentation

| ID | User Story | Priority |
|---|---|---|
| US-36 | As an ML engineer, I want a Data Card describing the dataset and its limitations. | P0 |
| US-37 | As an ML engineer, I want a Model Card documenting the model and its intended use. | P0 |
| US-38 | As a user, I want the system to communicate its limitations and avoid presenting predictions as guaranteed physical inspections. | P0 |
| US-39 | As an administrator, I want a performance report containing ML, business and operational metrics. | P0 |

**Priority definitions:**
- P0: Mandatory for the core project and final demonstration.
- P1: Important enhancement or extended workflow.
- P2: Optional future enhancement.

# 5. Functional Requirements and Feature List

This section defines what the platform must actually do.

## 5.1 Feature 1: Image-Based Defect Detection

**Priority:** P0

**Technology:** PyTorch + OpenCV + FastAPI.

**Description:**

The system will accept an image of a pump impeller and process it through the trained classification model.

**Functional requirements:**

1. Accept image uploads through the frontend.
2. Validate file format and image readability.
3. Preprocess the image to match model input requirements.
4. Perform inference through the deployed model.
5. Return the predicted class.
6. Return the defect probability.
7. Apply the configured classification threshold.
8. Display ACCEPT or REJECT as a model recommendation.
9. Return the deployed model version and inference latency.
10. Generate an optional Grad-CAM explanation.

**Expected output:**

| Field | Example |
|---|---|
| Image | Uploaded impeller image |
| Predicted class | DEFECTIVE |
| Defect probability | 0.92 |
| Decision | REJECT |
| Model version | v1 |
| Inference latency | Measured at runtime |
| Explanation | Grad-CAM heatmap |

The probability shown is the model's estimated defect probability, not a guarantee of real-world defect severity.

## 5.2 Feature 2: Dataset Management and Versioning

**Priority:** P0

**Technology:** DVC + Git + GitHub.

**Description:**

The dataset must be managed in a reproducible way so that model experiments can be traced back to the exact data used.

**Dataset strategy:**

The primary dataset is the Real-Life Industrial Dataset of Casting Product.

| Dataset Characteristic | Reported Value |
|---|---:|
| Original images | 1,300 |
| Image resolution | 512 × 512 |
| Image type | Grayscale |
| OK images | 519 |
| DEFECTIVE images | 781 |
| Classes | 2 |

The separately provided augmented dataset contains 7,348 images. It will be retained as a secondary resource, not used as the primary evaluation dataset.

**Functional requirements:**

- Download and organize the original dataset.
- Validate labels and image integrity.
- Identify duplicates and corrupted files.
- Generate reproducible train/validation/test splits.
- Apply augmentation only to training images.
- Track dataset versions with DVC.
- Store dataset metadata and preprocessing configurations.
- Associate dataset versions with MLflow experiments.

**Acceptance criteria:**

- DVC successfully tracks the primary dataset.
- Dataset changes can be versioned and retrieved.
- The same seed and configuration reproduce the same data split.
- No augmentation leakage occurs between training and evaluation sets.

## 5.3 Feature 3: Model Training and Comparison

**Priority:** P0

**Technology:** Python + PyTorch + OpenCV.

Three architectures will be evaluated.

### 1. Custom CNN

Role: Baseline.

Purpose: Establish reference performance and computational cost.

### 2. ResNet18

Role: Candidate 1.

Purpose: Evaluate transfer learning using a lightweight residual architecture.

### 3. EfficientNet-B0

Role: Candidate 2.

Purpose: Evaluate parameter-efficient image classification.

**Functional requirements:**

- Train all three architectures.
- Record hyperparameters.
- Evaluate models on the same test dataset.
- Generate confusion matrices.
- Calculate precision, recall, F1-score and AUC.
- Compare inference latency and model size.
- Select the final model based on measured performance.

The system must not assume that the most accurate model is automatically the best model. Defect recall, false rejection, inference performance and deployment suitability must also be considered.

## 5.4 Feature 4: Experiment Tracking and Model Registry

**Priority:** P0

**Technology:** MLflow.

**Description:**

MLflow will provide experiment tracking and model lifecycle management.

**Functional requirements:**

- Create and organize experiments.
- Record model parameters.
- Record evaluation metrics.
- Store training artifacts.
- Record dataset version and model architecture.
- Compare different training runs.
- Register approved models.
- Maintain model versions and metadata.
- Identify the model version currently used by the prediction API.

**Expected experiment metadata:**

| Parameter | Description |
|---|---|
| Model name | CNN / ResNet18 / EfficientNet-B0 |
| Dataset version | DVC version or revision |
| Learning rate | Training configuration |
| Batch size | Training configuration |
| Epochs | Number of training iterations |
| Optimizer | Selected optimizer |
| Accuracy | Overall classification accuracy |
| Recall | Defect detection recall |
| F1-score | Classification balance |
| AUC | Classification discrimination |
| Model artifact | Saved trained model |

## 5.5 Feature 5: Automated ML Pipeline

**Priority:** P0

**Technology:** Apache Airflow.

Airflow will orchestrate the complete ML workflow through a Directed Acyclic Graph (DAG).

**Primary pipeline sequence:**

1. Dataset ingestion.
2. Dataset validation.
3. Data preprocessing.
4. Feature preparation.
5. Model training.
6. Model evaluation.
7. MLflow experiment logging.
8. Model comparison.
9. Model quality gate.
10. Model registration.
11. Pipeline completion.

**Functional requirements:**

- Define pipeline tasks as Airflow operators.
- Establish task dependencies.
- Record execution status.
- Log task errors.
- Support task retries.
- Prevent model registration when quality checks fail.
- Maintain execution history.

**Model quality gate:**

A candidate model must satisfy configurable evaluation criteria before it can be registered as an approved deployment candidate.

The thresholds will be finalized after baseline experiments. They should not be arbitrarily assumed before the model's actual performance is known.

## 5.6 Feature 6: Model Explainability

**Priority:** P1

**Technology:** Grad-CAM.

Grad-CAM will generate a heatmap showing the image regions that contributed strongly to the CNN-based prediction.

**Functional requirements:**

- Generate a heatmap for supported predictions.
- Overlay the heatmap on the original image.
- Display the explanation beside the prediction.
- Allow users to inspect the highlighted regions.
- Clearly communicate that the visualization is an explanation of model behavior, not a certified defect measurement.

## 5.7 Feature 7: Prediction API

**Priority:** P0

**Technology:** FastAPI.

The API provides the communication layer between the frontend and trained model.

| Endpoint | Method | Purpose |
|---|---|---|
| `/health` | GET | Check service health |
| `/predict` | POST | Submit an impeller image and receive a prediction |
| `/model-info` | GET | Retrieve deployed model version and metadata |

**Additional requirements:**

- Input validation.
- Image preprocessing.
- Prediction response serialization.
- Error handling.
- Inference latency measurement.
- Model loading and initialization.
- API documentation through Swagger/OpenAPI.

## 5.8 Feature 8: Docker Containerization

**Priority:** P0

**Technology:** Docker + Docker Compose.

The system must run in a reproducible multi-service environment.

The intended local deployment includes:

- Frontend application.
- FastAPI prediction service.
- MLflow.
- Apache Airflow.
- Prometheus.
- Grafana.

Docker Compose will manage service configuration, networking, environment variables, volumes and startup dependencies.

## 5.9 Feature 9: CI/CD Automation

**Priority:** P0

**Technology:** GitHub Actions.

The CI/CD workflow will automatically validate code changes.

**Required checks:**

1. Checkout repository.
2. Set up required Python environment.
3. Install dependencies.
4. Run preprocessing unit tests.
5. Run prediction unit tests.
6. Run API integration tests.
7. Build Docker image.
8. Validate service startup and health.
9. Perform model-quality checks where applicable.
10. Report workflow success or failure.

**CI/CD tool decision:** The course requirements explicitly specify GitHub Actions. Therefore, GitHub Actions is the required CI/CD implementation for VisionQC. Jenkins is not part of the mandatory architecture and should not be added as a second CI/CD system unless the project scope is deliberately changed.

## 5.10 Feature 10: Monitoring and Observability

**Priority:** P0

**Technology:** Prometheus + Grafana.

The monitoring system will track two main categories.

### A. Operational Monitoring

- Total API requests.
- Successful requests.
- Failed requests.
- API error rate.
- Average inference latency.
- p50 inference latency.
- p95 inference latency.
- Prediction throughput.
- Service health.

### B. Machine Learning Monitoring

- OK versus DEFECTIVE prediction distribution.
- Confidence distribution.
- Image statistical drift.
- Feature or representation drift where implemented.
- Model performance when verified ground-truth labels become available.

Grafana will visualize these metrics through dashboards, while Prometheus will collect and store the time-series metrics exposed by the relevant services.

## 5.11 Feature 11: Data Drift Detection

**Priority:** P0

**Description:**

The platform must identify whether incoming images differ significantly from the reference dataset.

The project will simulate production changes using:

- Brightness variation.
- Contrast variation.
- Image noise.
- Mild blur.
- Exposure changes.

The drift detection component will compare the incoming image distribution with the reference distribution using a documented statistical or image-feature-based method.

**Expected workflow:**

1. Establish a reference distribution.
2. Generate or receive incoming image batches.
3. Extract the selected image statistics or features.
4. Compare distributions.
5. Calculate a drift metric.
6. Apply a configured threshold.
7. Record the result.
8. Display the drift status in Grafana.

A critical distinction must be maintained: data drift does not automatically prove that model accuracy has declined. Actual model performance degradation can only be measured when verified labels are available.

## 5.12 Feature 12: Automated Retraining

**Priority:** P1

**Description:**

The platform will support controlled model retraining when drift or performance degradation justifies further investigation.

**Workflow:**

1. Drift or performance alert is generated.
2. New data is collected and validated.
3. DVC creates a new dataset version.
4. Airflow initiates the retraining workflow.
5. Candidate models are trained.
6. MLflow records the experiments.
7. New candidates are evaluated.
8. Quality gates compare candidates against deployment requirements.
9. Approved candidates are registered.
10. The selected version can be promoted for deployment.

A drift alert must not automatically replace the currently deployed model. Model promotion must remain conditional on evaluation and quality checks.

## 5.13 Feature 13: AWS Cloud Extension

**Priority:** P1

**Technology:** AWS S3 + SageMaker + CloudWatch.

The cloud extension will demonstrate how the locally developed platform can be integrated with AWS services.

| AWS Service | Intended Role |
|---|---|
| S3 | Store datasets and model artifacts |
| SageMaker | Demonstrate managed ML training or deployment |
| CloudWatch | Logging and monitoring |

The cloud implementation should remain a controlled extension of the local system, not a prerequisite for basic local execution.

Cloud resources must be removed after the demonstration to avoid unnecessary costs.

# 6. Frontend and Dashboard Requirements

The frontend is the central interface through which users interact with VisionQC.

It must present information from the actual backend services rather than relying on hardcoded demonstration data.

The dashboard should make the complete ML lifecycle understandable, from dataset ingestion to model deployment and monitoring.

## 6.1 Dashboard Structure

The application will contain the following pages:

| Page | Main Functionality |
|---|---|
| Overview | Overall system status and important ML metrics |
| Inspection | Image upload, prediction and Grad-CAM explanation |
| Experiments | Compare model architectures and training runs |
| Dataset | Dataset information, versions and validation |
| Pipelines | Airflow DAG execution status |
| Model Registry | Registered models, versions and deployment status |
| Monitoring | API metrics, prediction distribution and drift |
| Retraining | Retraining status and candidate evaluation |
| Documentation | Data Card, Model Card and system information |

## 6.2 Overview Dashboard

**Purpose:** Give users a consolidated view of the platform.

Expected information:

- Current deployed model version.
- Model registration status.
- Dataset version.
- Latest pipeline execution.
- API health.
- Total predictions.
- Prediction distribution.
- Inference latency.
- Recent pipeline failures.
- Drift status.

All metrics must be retrieved from actual backend services or monitoring data.

## 6.3 Inspection Dashboard

**Purpose:** Provide the primary user-facing inspection functionality.

Expected components:

1. Image upload area.
2. Uploaded image preview.
3. Analyze image action.
4. Prediction result.
5. Defect probability.
6. ACCEPT / REJECT recommendation.
7. Grad-CAM visualization.
8. Model version.
9. Inference latency.

The interface must distinguish between an image that has not been analyzed and a completed prediction.

## 6.4 Experiments Dashboard

**Purpose:** Provide visibility into model development.

Expected components:

- Experiment list.
- Model architecture.
- Training parameters.
- Dataset version.
- Accuracy.
- Precision.
- Recall.
- F1-score.
- AUC.
- Training duration.
- Model artifact reference.

Users should be able to compare the Custom CNN, ResNet18 and EfficientNet-B0.

## 6.5 Dataset Dashboard

**Purpose:** Show the current dataset and its version history.

Expected components:

- Dataset name.
- Dataset version.
- Total image count.
- OK image count.
- DEFECTIVE image count.
- Image dimensions.
- Dataset validation status.
- Train/validation/test split information.
- DVC version information.

## 6.6 Pipeline Dashboard

**Purpose:** Show automated workflow execution.

Expected components:

- Airflow DAG name.
- Pipeline execution history.
- Current execution status.
- Individual task status.
- Execution duration.
- Failed task information.
- Retry information.
- Latest successful execution.

Users should be able to navigate to the relevant Airflow interface for detailed execution information.

## 6.7 Model Registry Dashboard

**Purpose:** Provide model lifecycle visibility.

Expected components:

- Model name.
- Model architecture.
- Model version.
- Associated dataset version.
- Evaluation metrics.
- Registration timestamp.
- Model status.
- Current deployment version.

The platform must distinguish between a candidate model, an approved model and the currently deployed model.

## 6.8 Monitoring Dashboard

**Purpose:** Display real-time or periodically refreshed operational and ML metrics.

Expected components:

- API request count.
- API error rate.
- Average and p95 latency.
- Prediction throughput.
- Prediction distribution.
- Confidence distribution.
- Drift score.
- Drift status.
- Model performance when labels become available.

## 6.9 Retraining Dashboard

**Purpose:** Communicate the status of model improvement workflows.

Expected components:

- Drift detection status.
- Retraining trigger information.
- New dataset version.
- Retraining pipeline status.
- Candidate model metrics.
- Quality-gate result.
- Model promotion status.

**Frontend integration principle:** The frontend should communicate with FastAPI and the appropriate monitoring/orchestration interfaces. It should not independently execute training or access model files directly.

# 7. End-to-End Product Workflow

The following workflow defines how the different features work together.

1. **Data acquisition:** Obtain the original impeller image dataset.
2. **Data versioning:** Validate and version the dataset using DVC.
3. **Model development:** Train Custom CNN, ResNet18 and EfficientNet-B0.
4. **Experiment tracking:** Log metrics, parameters and artifacts in MLflow.
5. **Automated orchestration:** Airflow executes the complete training DAG.
6. **Model evaluation:** Compare models and apply quality gates.
7. **Model registration:** Register the approved model in MLflow.
8. **Deployment:** Load the selected model through FastAPI.
9. **Containerization and CI/CD:** Run services with Docker and validate changes with GitHub Actions.
10. **Prediction:** Users upload images through the frontend and receive predictions.
11. **Monitoring:** Prometheus collects metrics and Grafana visualizes them.
12. **Drift detection:** Detect changes in incoming image distributions.
13. **Controlled retraining:** Generate, evaluate and register new candidate models.
14. **Model promotion:** Promote a candidate only after passing the required quality checks.

This workflow is the central product behavior. The individual technologies must be integrated into one functioning lifecycle rather than demonstrated as unrelated tools.

# 8. Success Metrics and KPIs

The success of VisionQC will be measured across five categories:

1. Machine learning performance.
2. Business impact.
3. System performance.
4. MLOps automation.
5. Operational reliability.

## 8.1 Machine Learning Metrics

| Metric | Definition | Target |
|---|---|---|
| Accuracy | Correct predictions / total predictions | Report actual result; establish baseline |
| Defect recall | Correctly detected defective samples / actual defective samples | Prioritize high recall |
| Precision | Correct defective predictions / predicted defective samples | Maximize without compromising recall |
| F1-score | Harmonic mean of precision and recall | Improve over baseline |
| ROC-AUC | Classification discrimination | Report measured result |
| PR-AUC | Precision-recall performance | Report measured result |
| False-negative rate | Defective components incorrectly classified as OK | Minimize |
| Confusion matrix | Distribution of correct and incorrect classifications | Required |

**Important success criterion:** Model selection must prioritize detecting defective components. A model with high accuracy but poor defect recall should not automatically be selected.

## 8.2 Business Metrics

| Metric | Purpose |
|---|---|
| Defective components detected | Measure defect identification |
| False rejection rate | Measure acceptable components incorrectly rejected |
| Inspection throughput | Measure images inspected per unit time |
| Potential manual workload reduction | Estimate inspection effort saved |
| Estimated inspection error cost | Compare false-negative and false-positive costs |

The business impact should be demonstrated using documented assumptions. It must not be presented as actual manufacturer savings without real operational evidence.

## 8.3 System Performance Metrics

These are proposed initial engineering targets for the academic demonstration, not measured results or mandatory course thresholds.

| Metric | Proposed Target |
|---|---:|
| p95 inference latency | Under 2 seconds |
| API error rate under normal test conditions | Under 1% |
| API health-check response | Successful |
| Prediction response | Valid structured response |
| Docker service startup | All required services healthy |
| Prediction throughput | Measure and report actual value |
| Monitoring refresh | Near-real-time or configured interval |

Inference latency should be measured separately from image upload time and network transfer time.

## 8.4 MLOps Metrics

| Metric | Success Criterion |
|---|---|
| Dataset versioning | DVC successfully tracks dataset versions |
| Model experiments | Minimum 3 architectures evaluated |
| Experiment tracking | All required runs recorded in MLflow |
| Model registration | Selected model registered with version metadata |
| Airflow automation | Complete training DAG executes successfully |
| CI/CD | GitHub Actions workflow passes |
| Docker | Application starts using Docker Compose |
| Monitoring | Required metrics visible in Grafana |
| Drift detection | Simulated drift is detected and documented |
| Retraining | New candidate model produced |
| Model promotion | Quality gate prevents unsuitable promotion |

## 8.5 Responsible AI Metrics

- Data Card completed.
- Model Card completed.
- Grad-CAM explanation generated.
- Intended-use statement documented.
- Model limitations documented.
- Dataset source and license documented.
- Bias/fairness considerations reviewed where relevant.
- Predictions presented as decision support rather than guaranteed inspection outcomes.

# 9. Non-Functional Requirements

These requirements define the quality attributes of the product.

| Category | Requirement |
|---|---|
| Performance | Predictions should complete within the defined latency target under test conditions. |
| Reliability | API failures should be handled without crashing the complete platform. |
| Scalability | Services should be independently configurable and extensible. |
| Maintainability | Code should follow modular architecture and clear separation of concerns. |
| Reproducibility | Dataset, model configurations and dependencies must be versioned. |
| Security | Validate uploads, protect credentials and avoid exposing secrets in source control. |
| Usability | Dashboard should present predictions and system information clearly. |
| Observability | Application and pipeline failures must be traceable. |
| Portability | Local environment should be reproducible through Docker Compose. |
| Documentation | Installation, architecture, APIs and workflows must be documented. |

## 9.1 Security Requirements

- Restrict accepted image file types.
- Validate image contents rather than relying only on file extensions.
- Set reasonable upload size limits.
- Keep AWS credentials and API secrets in environment variables or secure secret storage.
- Avoid committing `.env` files containing secrets.
- Do not expose internal infrastructure credentials through the frontend.
- Keep dependencies and container images maintained.

# 10. Technical Architecture Requirements

The architecture must support the complete product lifecycle.

| Layer | Technology | Responsibility |
|---|---|---|
| Frontend | React / Next.js | User dashboard and interaction |
| Backend | FastAPI | API and model serving |
| ML development | PyTorch + OpenCV | Model development and image processing |
| Explainability | Grad-CAM | Visual model explanations |
| Data versioning | DVC + Git | Dataset and code versioning |
| Experiment management | MLflow | Experiment tracking and model registry |
| Orchestration | Apache Airflow | Automated ML workflow and retraining |
| Containerization | Docker + Docker Compose | Reproducible service deployment |
| CI/CD | GitHub Actions | Automated testing and build validation |
| Monitoring | Prometheus | Metrics collection |
| Visualization | Grafana | Monitoring dashboards |
| Cloud | AWS S3 + SageMaker + CloudWatch | Cloud storage, ML execution and monitoring |

**Architecture clarification:**

- Airflow orchestrates ML pipeline tasks.
- MLflow manages experiments and model registration.
- GitHub Actions handles code validation and CI/CD.
- Docker packages services.
- Prometheus and Grafana handle operational and ML monitoring.

These tools have different responsibilities and should not be treated as interchangeable.

# 11. Project Scope

## 11.1 In Scope

- Binary classification of pump-impeller images.
- Dataset validation and DVC versioning.
- Image preprocessing and training augmentation.
- Three model architectures.
- MLflow experiment tracking.
- Model registry.
- Airflow training orchestration.
- FastAPI inference service.
- Grad-CAM explanations.
- Docker-based local environment.
- GitHub Actions CI/CD.
- Prometheus and Grafana.
- Data drift simulation and detection.
- Controlled retraining and model promotion.
- AWS cloud extension.
- Frontend dashboard.
- Data Card and Model Card.
- Performance reporting and final demonstration.

## 11.2 Out of Scope

The following features are not required for the initial academic release:

- Direct integration with factory cameras.
- Real-time conveyor belt inspection.
- Direct control of manufacturing machinery.
- Autonomous physical rejection of components.
- Classification of unrelated manufactured products.
- Multi-factory enterprise deployment.
- Production-grade industrial certification.
- Guaranteed performance under untested lighting and camera conditions.
- Fully automated cloud infrastructure provisioning.

# 12. Final Project Deliverables

The following deliverables define what must be available when VisionQC is submitted.

| No. | Deliverable | Evidence |
|---:|---|---|
| 1 | GitHub repository | Repository with meaningful commit history |
| 2 | Project README | Architecture, setup and execution instructions |
| 3 | DVC implementation | Dataset versioning evidence |
| 4 | ML models | Baseline CNN, ResNet18, EfficientNet-B0 |
| 5 | MLflow | Experiment tracking and registry screenshots |
| 6 | Airflow | DAG source and successful execution screenshot |
| 7 | FastAPI | Swagger/OpenAPI documentation screenshot |
| 8 | Docker | Dockerfile and Docker Compose configuration |
| 9 | GitHub Actions | Successful CI/CD workflow |
| 10 | Prometheus/Grafana | Monitoring dashboard |
| 11 | Drift detection | Simulated drift evidence |
| 12 | Retraining | Candidate retraining and quality-gate evidence |
| 13 | Responsible AI | Data Card, Model Card and intended-use statement |
| 14 | Performance report | ML, business and operational metrics |
| 15 | Final presentation | Five-minute demonstration |
| 16 | Individual assessment | Viva preparation |

# 13. Implementation Roadmap

The following is the proposed eight-week implementation roadmap.

| Phase | Week | Primary Activities | Expected Output |
|---|---|---|---|
| 0 | 1 | Repository, environment, dataset and DVC | Versioned dataset |
| 1 | 2 | EDA, validation, preprocessing, baseline CNN | Baseline model |
| 2 | 3 | ResNet18, EfficientNet-B0 and evaluation | Model comparison |
| 3 | 4 | MLflow experiments and registry | Registered model |
| 4 | 5 | Airflow pipeline and automation | Successful training DAG |
| 5 | 6 | FastAPI, Docker and GitHub Actions | Deployable application |
| 6 | 7 | Prometheus, Grafana and drift simulation | Monitoring system |
| 7 | 8 | Retraining, AWS, integration and documentation | Complete VisionQC |

The frontend can be developed incrementally alongside these phases rather than waiting until the backend is complete.

# 14. Team Responsibilities

The project is designed for four members.

| Member | Ownership Area | Major Responsibilities |
|---|---|---|
| Member 1 | Data & Computer Vision | Dataset, DVC, preprocessing, baseline CNN, Grad-CAM |
| Member 2 | ML & Experimentation | ResNet18, EfficientNet-B0, evaluation, MLflow |
| Member 3 | MLOps Pipeline | Airflow, pipeline automation, quality gates, retraining |
| Member 4 | Deployment & Monitoring | FastAPI, Docker, GitHub Actions, Prometheus, Grafana, AWS |

These are ownership areas, not isolated responsibilities. All four members should understand the overall architecture and complete data-to-deployment workflow.

# 15. Risks and Mitigation

| Risk | Potential Impact | Mitigation |
|---|---|---|
| Small original dataset | Overfitting and poor generalization | Careful augmentation and validation |
| Dataset leakage | Misleading evaluation results | Split original images before augmentation |
| High false-negative rate | Defective items classified as acceptable | Prioritize defect recall and optimize threshold |
| Airflow complexity | Delayed pipeline integration | Build and test DAG incrementally |
| MLflow integration issues | Missing experiment lineage | Standardize logging interfaces early |
| Docker resource usage | Slow local development | Start only required services during development |
| Drift false alarms | Unnecessary retraining | Validate drift thresholds |
| Model degradation | Poor inspection performance | Enforce quality gates |
| AWS costs | Unnecessary cloud expenses | Use limited resources and clean up after demonstration |
| Integration failures | Incomplete final demonstration | Establish regular end-to-end integration checkpoints |

# 16. Acceptance Criteria

VisionQC will be considered ready for final submission when the following conditions are satisfied.

## A. Machine Learning

- [ ] Original dataset has been validated.
- [ ] DVC tracks the primary dataset.
- [ ] Reproducible train/validation/test splits exist.
- [ ] Three model architectures have been trained.
- [ ] Models have been evaluated using appropriate metrics.
- [ ] Grad-CAM explanations can be generated.
- [ ] The selected model is registered in MLflow.

## B. MLOps

- [ ] Airflow executes the training workflow.
- [ ] MLflow records parameters, metrics and artifacts.
- [ ] Model-quality gates are implemented.
- [ ] FastAPI serves predictions.
- [ ] Docker Compose starts the required services.
- [ ] GitHub Actions executes automated tests successfully.

## C. Monitoring

- [ ] Prometheus collects application metrics.
- [ ] Grafana displays operational metrics.
- [ ] Prediction distributions are monitored.
- [ ] Drift simulation is implemented.
- [ ] Drift detection is demonstrated.
- [ ] Retraining generates a new candidate.
- [ ] An unsuitable candidate cannot be promoted.

## D. Product and Documentation

- [ ] Frontend communicates with the backend.
- [ ] Image inspection works end to end.
- [ ] Prediction results display correctly.
- [ ] Model version information is visible.
- [ ] Data Card and Model Card are complete.
- [ ] README contains reproducible setup instructions.
- [ ] AWS extension is demonstrated.
- [ ] Five-minute demonstration is ready.

# 17. Final Product Definition

VisionQC is not simply an image-classification application.

It is a complete academic MLOps platform that demonstrates how an industrial computer vision solution can move through the entire machine learning lifecycle.

Its success will be determined by three fundamental capabilities:

1. **Predict:** Accurately identify potentially defective pump impellers using computer vision.
2. **Operate:** Manage, deploy and monitor machine learning models through an automated and reproducible infrastructure.
3. **Improve:** Detect changes in incoming data, retrain candidate models and promote only models that satisfy quality requirements.

The project should demonstrate a complete, connected workflow rather than a collection of independent technology demonstrations.

# 18. Important Project Decisions

These decisions should remain consistent across the PRD, technical documentation, frontend implementation and development tasks.

| Decision | Final Choice |
|---|---|
| Project name | VisionQC |
| ML problem | Binary image classification |
| Dataset | Real-Life Industrial Dataset of Casting Product |
| Primary dataset | Original 1,300 images |
| ML framework | PyTorch |
| Image processing | OpenCV |
| Baseline | Custom CNN |
| Candidate models | ResNet18 and EfficientNet-B0 |
| Dataset versioning | DVC |
| Experiment tracking | MLflow |
| Pipeline orchestration | Apache Airflow |
| Backend | FastAPI |
| Frontend | React / Next.js |
| CI/CD | GitHub Actions |
| CI/CD alternative | Jenkins not required |
| Containerization | Docker + Docker Compose |
| Monitoring | Prometheus |
| Dashboard visualization | Grafana |
| Explainability | Grad-CAM |
| Cloud extension | AWS S3, SageMaker, CloudWatch |

---

**Document status:** Product requirements baseline.

**Usage:** This PRD is the single source of truth for VisionQC product requirements. The technical stack, implementation tasks and frontend behavior should remain consistent with this document.

The `techstack.md` file should describe implementation technologies and their configurations, while `todo.md` should contain actionable development tasks derived from these requirements.