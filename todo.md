# VisionQC — Implementation Todo v2.0

**Project:** VisionQC — Automated Manufacturing Defect Inspection & MLOps Platform
**Plan version:** 2.0
**Date:** 14 November 2026
**Status:** Implementation plan
**Primary reference documents:** `prd.md`, `design.md`, `techstack.md`

---

# 0. Rules for using this Todo

## 0.1 Execution rules

1. Follow the tasks in the listed order.
2. Do not begin a task until the previous task is complete and verified.
3. Do not skip a failed verification.
4. Do not mark a task complete merely because code has been generated.
5. Every implementation task must include a test or observable verification.
6. Do not introduce a new technology without updating `techstack.md` first.
7. Do not change product requirements without updating `prd.md` first.
8. Do not introduce fabricated dashboard data to make a page look complete.
9. Keep all source code, configuration and documentation in Git.
10. Keep datasets, model weights and large generated artifacts out of ordinary Git commits.

## 0.2 Responsibility labels

- **[MANUAL]** You perform the installation, account creation, configuration, credential entry, service startup or real-world verification.
- **[ANTIGRAVITY]** Antigravity implements code, configuration, tests, documentation and technical corrections.
- **[BOTH]** Antigravity prepares the implementation; you execute or inspect it and confirm the result.

Antigravity must not claim that a service is installed, an account is configured, a cloud resource exists or a model has trained unless you have actually performed or verified that action.

## 0.3 Project completion definition

VisionQC is complete when:

- The original dataset is versioned and reproducible.
- The three required model architectures have been trained and evaluated.
- Experiments and model artifacts are tracked in MLflow.
- Airflow can orchestrate training and retraining workflows.
- FastAPI serves the approved model and provides inspection results.
- Grad-CAM produces genuine visual explanations.
- PostgreSQL stores application and operational metadata.
- The Next.js application contains all nine required dashboard pages.
- Prometheus and Grafana provide operational and ML monitoring.
- Drift detection and controlled retraining work end to end.
- Docker Compose can run the complete local demonstration.
- GitHub Actions validates the repository.
- Automated tests and manual acceptance tests pass.
- Documentation and demonstration evidence are complete.

AWS is an optional extension. It is not required for the local academic demonstration.

---

# PHASE 0 — Project decisions and development environment

**Objective:** Establish the repository, confirm technology compatibility and prepare the local machine.

## 0.1 Confirm the implementation baseline

- [x] **0.1.1 [MANUAL]** Confirm that the project repository is the intended VisionQC repository.
- [x] **0.1.2 [ANTIGRAVITY]** Read `prd.md`, `design.md` and `techstack.md` completely.
- [x] **0.1.3 [ANTIGRAVITY]** Compare the three documents and list any conflicting requirements.
- [x] **0.1.4 [ANTIGRAVITY]** Create a technical decision record for every unresolved technology choice.
- [x] **0.1.5 [BOTH]** Select Python 3.12 as the initial project version, subject to dependency compatibility testing.
- [x] **0.1.6 [ANTIGRAVITY]** Verify the selected PyTorch, TorchVision, FastAPI and Airflow releases support the selected Python version.
- [x] **0.1.7 [ANTIGRAVITY]** Select one stable Tailwind CSS major version compatible with Next.js 16 and shadcn/ui.
- [x] **0.1.8 [ANTIGRAVITY]** Select one stable Airflow release and document its matching service architecture.
- [x] **0.1.9 [ANTIGRAVITY]** Select one stable PostgreSQL 18 container image.
- [x] **0.1.10 [ANTIGRAVITY]** Record all selected major and minor versions in `techstack.md`.

**Verification:** No unresolved version choice should remain for the initial local implementation.

## 0.2 Prepare the local machine

- [x] **0.2.1 [MANUAL]** Install Git.
- [x] **0.2.2 [MANUAL]** Verify Git is available in the terminal.
- [x] **0.2.3 [MANUAL]** Install the selected Python version.
- [x] **0.2.4 [MANUAL]** Verify the Python version.
- [x] **0.2.5 [MANUAL]** Install Node.js LTS compatible with Next.js 16.
- [x] **0.2.6 [MANUAL]** Verify Node.js is available.
- [x] **0.2.7 [MANUAL]** Verify npm is available.
- [x] **0.2.8 [MANUAL]** Install Docker Desktop.
- [ ] **0.2.9 [MANUAL]** Enable the required Docker virtualization or WSL 2 configuration.
- [ ] **0.2.10 [MANUAL]** Start Docker Desktop.
- [ ] **0.2.11 [MANUAL]** Verify Docker CLI access.
- [ ] **0.2.12 [MANUAL]** Verify Docker Compose is available.
- [x] **0.2.13 [MANUAL]** Install VS Code or confirm the existing editor is ready.
- [x] **0.2.14 [MANUAL]** Install Antigravity and verify it can open the repository.
- [x] **0.2.15 [MANUAL]** Create or confirm the GitHub account and repository access.

**Verification:** Python, Node.js, npm, Git, Docker, Docker Compose and Antigravity are accessible.

## 0.3 Establish the repository

- [x] **0.3.1 [ANTIGRAVITY]** Inspect the existing repository before modifying it.
- [x] **0.3.2 [ANTIGRAVITY]** Identify existing source files that must be preserved.
- [x] **0.3.3 [ANTIGRAVITY]** Create the agreed top-level project directories.
- [x] **0.3.4 [ANTIGRAVITY]** Create the root `.gitignore`.
- [x] **0.3.5 [ANTIGRAVITY]** Add Python cache exclusions to `.gitignore`.
- [x] **0.3.6 [ANTIGRAVITY]** Add Node.js build and dependency exclusions to `.gitignore`.
- [x] **0.3.7 [ANTIGRAVITY]** Add environment and secret-file exclusions to `.gitignore`.
- [x] **0.3.8 [ANTIGRAVITY]** Add model-weight and large-artifact exclusions to `.gitignore`.
- [x] **0.3.9 [ANTIGRAVITY]** Create the root `README.md`.
- [x] **0.3.10 [ANTIGRAVITY]** Create the root `.env.example`.
- [x] **0.3.11 [ANTIGRAVITY]** Create the initial root `todo.md` using this plan.
- [x] **0.3.12 [MANUAL]** Configure Git username and email.
- [x] **0.3.13 [MANUAL]** Create the initial Git commit.
- [x] **0.3.14 [MANUAL]** Push the initial commit to GitHub.
- [x] **0.3.15 [MANUAL]** Confirm the repository is visible on GitHub.

**Verification:** The repository has a successful initial commit and a clean working tree.

---

# PHASE 1 — Dataset acquisition and validation

**Objective:** Obtain and validate the real industrial casting dataset before building models.

## 1.1 Acquire the dataset

- [x] **1.1.1 [MANUAL]** Locate the Real-Life Industrial Dataset of Casting Product from its original source.
- [x] **1.1.2 [MANUAL]** Download the original dataset.
- [x] **1.1.3 [MANUAL]** Preserve an untouched copy of the downloaded dataset.
- [x] **1.1.4 [MANUAL]** Place the dataset in the agreed local data directory.
- [x] **1.1.5 [ANTIGRAVITY]** Create a dataset directory structure that separates raw, processed and derived data.
- [x] **1.1.6 [ANTIGRAVITY]** Add dataset directories to the appropriate Git and DVC ignore rules.
- [x] **1.1.7 [BOTH]** Confirm that the downloaded dataset contains the expected OK and DEFECTIVE classes.

## 1.2 Validate the dataset

The expected reference dataset contains approximately 1,300 grayscale images:

- OK: 519 images.
- DEFECTIVE: 781 images.
- Image dimensions: 512 × 512 pixels.

These values must be checked against the actual downloaded dataset.

- [x] **1.2.1 [ANTIGRAVITY]** Implement a dataset directory scanner.
- [x] **1.2.2 [ANTIGRAVITY]** Implement image file-extension validation.
- [x] **1.2.3 [ANTIGRAVITY]** Implement image decoding validation.
- [x] **1.2.4 [ANTIGRAVITY]** Implement image-dimension inspection.
- [x] **1.2.5 [ANTIGRAVITY]** Implement class-count calculation.
- [x] **1.2.6 [ANTIGRAVITY]** Implement duplicate-image detection using file hashes.
- [x] **1.2.7 [ANTIGRAVITY]** Generate a dataset validation report.
- [x] **1.2.8 [BOTH]** Run the validation script against the downloaded dataset.
- [x] **1.2.9 [BOTH]** Investigate corrupted or unreadable images.
- [x] **1.2.10 [BOTH]** Confirm the final class counts.
- [x] **1.2.11 [ANTIGRAVITY]** Record the actual dataset counts in the Data Card.
- [x] **1.2.12 [ANTIGRAVITY]** Record the dataset source and licence information.

**Verification:** The validation report identifies the actual number of readable images, dimensions, classes, duplicates and any exclusions.

## 1.3 Configure DVC

- [x] **1.3.1 [MANUAL]** Install DVC in the selected Python environment.
- [x] **1.3.2 [ANTIGRAVITY]** Initialize DVC in the repository.
- [x] **1.3.3 [ANTIGRAVITY]** Configure the raw dataset as a DVC-tracked directory.
- [x] **1.3.4 [ANTIGRAVITY]** Generate the dataset tracking metadata.
- [x] **1.3.5 [MANUAL]** Commit the DVC metadata to Git.
- [x] **1.3.6 [MANUAL]** Confirm the original images are not committed directly to Git.
- [x] **1.3.7 [ANTIGRAVITY]** Document how to reproduce the dataset locally.

**Verification:** A clean checkout can retrieve the tracked dataset using the documented DVC procedure.

---

# PHASE 2 — Exploratory data analysis and preprocessing

**Objective:** Understand the data and create a reproducible preprocessing workflow.

## 2.1 Exploratory data analysis

- [x] **2.1.1 [ANTIGRAVITY]** Create the EDA module.
- [x] **2.1.2 [ANTIGRAVITY]** Generate a class-distribution report.
- [x] **2.1.3 [ANTIGRAVITY]** Generate a sample image grid for both classes.
- [x] **2.1.4 [ANTIGRAVITY]** Calculate image brightness statistics.
- [x] **2.1.5 [ANTIGRAVITY]** Calculate image intensity distributions.
- [x] **2.1.6 [ANTIGRAVITY]** Calculate image contrast statistics.
- [x] **2.1.7 [ANTIGRAVITY]** Calculate image sharpness statistics.
- [x] **2.1.8 [ANTIGRAVITY]** Inspect image resolution consistency.
- [x] **2.1.9 [ANTIGRAVITY]** Generate an EDA report.
- [x] **2.1.10 [BOTH]** Review the EDA report and identify data-quality concerns.

## 2.2 Define the preprocessing contract

- [x] **2.2.1 [ANTIGRAVITY]** Define the canonical input image format.
- [x] **2.2.2 [ANTIGRAVITY]** Define grayscale-to-model-channel conversion.
- [x] **2.2.3 [ANTIGRAVITY]** Define the image resizing strategy.
- [x] **2.2.4 [ANTIGRAVITY]** Compare candidate image resolutions for defect-detail preservation.
- [x] **2.2.5 [BOTH]** Select the training resolution based on the experiment results.
- [x] **2.2.6 [ANTIGRAVITY]** Define image normalization parameters.
- [x] **2.2.7 [ANTIGRAVITY]** Store preprocessing settings in `configs/preprocessing_config.yaml`.
- [x] **2.2.8 [ANTIGRAVITY]** Implement the shared preprocessing function.
- [x] **2.2.9 [ANTIGRAVITY]** Implement preprocessing tests.
- [x] **2.2.10 [ANTIGRAVITY]** Verify that training and inference use the same preprocessing contract.

## 2.3 Prepare reproducible data splits

- [x] **2.3.1 [ANTIGRAVITY]** Define the train, validation and test split policy.
- [x] **2.3.2 [ANTIGRAVITY]** Implement stratified splitting.
- [x] **2.3.3 [ANTIGRAVITY]** Configure a fixed random seed.
- [x] **2.3.4 [ANTIGRAVITY]** Add duplicate-leakage checks across splits.
- [x] **2.3.5 [ANTIGRAVITY]** Ensure the test split remains untouched during model selection.
- [x] **2.3.6 [ANTIGRAVITY]** Store split metadata and image references.
- [x] **2.3.7 [ANTIGRAVITY]** Version the split definition with DVC.
- [x] **2.3.8 [BOTH]** Run the split-generation workflow.
- [x] **2.3.9 [BOTH]** Verify class distributions across all splits.

## 2.4 Implement augmentation

- [x] **2.4.1 [ANTIGRAVITY]** Define augmentation operations appropriate for industrial impeller images.
- [x] **2.4.2 [ANTIGRAVITY]** Implement the training augmentation pipeline.
- [x] **2.4.3 [ANTIGRAVITY]** Restrict augmentation to the training data.
- [x] **2.4.4 [ANTIGRAVITY]** Keep validation and test images unaugmented.
- [x] **2.4.5 [ANTIGRAVITY]** Add augmentation visualization.
- [x] **2.4.6 [ANTIGRAVITY]** Add tests that verify augmentation does not alter validation or test data.
- [x] **2.4.7 [BOTH]** Review augmented samples for unrealistic transformations.

**Verification:** The preprocessing workflow is deterministic where required, reproducible, and shared by training and inference.

---

# PHASE 3 — Baseline model development

**Objective:** Establish a reliable baseline before transfer learning.

## 3.1 Build the custom CNN

- [x] **3.1.1 [ANTIGRAVITY]** Create `ml/models/custom_cnn.py`.
- [x] **3.1.2 [ANTIGRAVITY]** Implement the custom CNN architecture.
- [x] **3.1.3 [ANTIGRAVITY]** Implement the binary classification output.
- [x] **3.1.4 [ANTIGRAVITY]** Implement the training dataset loader.
- [x] **3.1.5 [ANTIGRAVITY]** Implement the validation dataset loader.
- [x] **3.1.6 [ANTIGRAVITY]** Implement the training loop.
- [x] **3.1.7 [ANTIGRAVITY]** Implement validation evaluation.
- [x] **3.1.8 [ANTIGRAVITY]** Implement checkpoint saving.
- [x] **3.1.9 [ANTIGRAVITY]** Implement reproducibility controls.
- [x] **3.1.10 [ANTIGRAVITY]** Add class-imbalance handling as a configurable training option.
- [x] **3.1.11 [ANTIGRAVITY]** Add training unit tests.
- [x] **3.1.12 [BOTH]** Run a small smoke-training experiment.
- [x] **3.1.13 [BOTH]** Verify the training loss and validation loop execute correctly.

## 3.2 Evaluate the baseline

- [x] **3.2.1 [ANTIGRAVITY]** Implement accuracy calculation.
- [x] **3.2.2 [ANTIGRAVITY]** Implement precision calculation.
- [x] **3.2.3 [ANTIGRAVITY]** Implement defect recall calculation.
- [x] **3.2.4 [ANTIGRAVITY]** Implement F1-score calculation.
- [x] **3.2.5 [ANTIGRAVITY]** Implement ROC-AUC calculation.
- [x] **3.2.6 [ANTIGRAVITY]** Implement PR-AUC calculation.
- [x] **3.2.7 [ANTIGRAVITY]** Implement false-negative-rate calculation.
- [x] **3.2.8 [ANTIGRAVITY]** Implement confusion-matrix generation.
- [x] **3.2.9 [ANTIGRAVITY]** Implement threshold evaluation.
- [x] **3.2.10 [ANTIGRAVITY]** Generate the baseline evaluation report.
- [x] **3.2.11 [BOTH]** Run the baseline training experiment.
- [x] **3.2.12 [BOTH]** Review the baseline evaluation report.

**Verification:** The custom CNN trains, saves a checkpoint and produces reproducible evaluation metrics.

---

# PHASE 4 — Transfer learning and model comparison

**Objective:** Implement and compare all three required model architectures.

## 4.1 Implement ResNet18

- [x] **4.1.1 [ANTIGRAVITY]** Create `ml/models/resnet18.py`.
- [x] **4.1.2 [ANTIGRAVITY]** Load the selected pretrained ResNet18 weights.
- [x] **4.1.3 [ANTIGRAVITY]** Implement grayscale input adaptation.
- [x] **4.1.4 [ANTIGRAVITY]** Replace the classification head for binary classification.
- [x] **4.1.5 [ANTIGRAVITY]** Implement configurable layer freezing.
- [x] **4.1.6 [ANTIGRAVITY]** Implement the ResNet18 training configuration.
- [x] **4.1.7 [ANTIGRAVITY]** Add ResNet18 forward-pass tests.
- [x] **4.1.8 [BOTH]** Run a ResNet18 smoke-training experiment.

## 4.2 Implement EfficientNet-B0

- [x] **4.2.1 [ANTIGRAVITY]** Create `ml/models/efficientnet_b0.py`.
- [x] **4.2.2 [ANTIGRAVITY]** Load the selected pretrained EfficientNet-B0 weights.
- [x] **4.2.3 [ANTIGRAVITY]** Implement grayscale input adaptation.
- [x] **4.2.4 [ANTIGRAVITY]** Replace the classification head for binary classification.
- [x] **4.2.5 [ANTIGRAVITY]** Implement configurable layer freezing.
- [x] **4.2.6 [ANTIGRAVITY]** Implement the EfficientNet-B0 training configuration.
- [x] **4.2.7 [ANTIGRAVITY]** Add EfficientNet-B0 forward-pass tests.
- [x] **4.2.8 [BOTH]** Run an EfficientNet-B0 smoke-training experiment.

## 4.3 Standardize model evaluation

- [x] **4.3.1 [ANTIGRAVITY]** Ensure all three models use the same dataset split.
- [x] **4.3.2 [ANTIGRAVITY]** Ensure all three models use the same evaluation implementation.
- [x] **4.3.3 [ANTIGRAVITY]** Ensure all three models record their preprocessing configuration.
- [x] **4.3.4 [ANTIGRAVITY]** Implement a common model comparison report.
- [x] **4.3.5 [ANTIGRAVITY]** Implement confusion-matrix visualization.
- [x] **4.3.6 [ANTIGRAVITY]** Implement ROC and precision-recall visualization.
- [x] **4.3.7 [ANTIGRAVITY]** Implement threshold comparison.
- [x] **4.3.8 [BOTH]** Run the full custom CNN experiment.
- [x] **4.3.9 [BOTH]** Run the full ResNet18 experiment.
- [x] **4.3.10 [BOTH]** Run the full EfficientNet-B0 experiment.
- [x] **4.3.11 [ANTIGRAVITY]** Generate the three-model comparison report.
- [x] **4.3.12 [BOTH]** Review the defect recall and false-negative results.
- [x] **4.3.13 [BOTH]** Select the candidate model using the documented evaluation criteria.
- [x] **4.3.14 [ANTIGRAVITY]** Document the model-selection rationale.

## 4.4 Establish the classification threshold

- [x] **4.4.1 [ANTIGRAVITY]** Implement configurable classification thresholds.
- [x] **4.4.2 [ANTIGRAVITY]** Evaluate candidate thresholds on the validation set.
- [x] **4.4.3 [ANTIGRAVITY]** Calculate defect recall and false-negative rate for each candidate.
- [x] **4.4.4 [BOTH]** Select the operating threshold according to the documented manufacturing-risk objective.
- [x] **4.4.5 [ANTIGRAVITY]** Store the selected threshold in model metadata.
- [x] **4.4.6 [ANTIGRAVITY]** Evaluate the selected model once on the untouched test set.
- [x] **4.4.7 [ANTIGRAVITY]** Generate the final test evaluation report.

**Verification:** All three architectures have comparable evaluation records, and the selected model has a documented threshold and test report.

---

# PHASE 5 — Explainability and ML artifact management

**Objective:** Produce genuine model explanations and preserve model artifacts.

## 5.1 Implement Grad-CAM

- [x] **5.1.1 [ANTIGRAVITY]** Create `ml/explainability/gradcam.py`.
- [x] **5.1.2 [ANTIGRAVITY]** Identify the target feature layer for the custom CNN.
- [x] **5.1.3 [ANTIGRAVITY]** Implement Grad-CAM for the custom CNN.
- [x] **5.1.4 [ANTIGRAVITY]** Identify the target feature layer for ResNet18.
- [x] **5.1.5 [ANTIGRAVITY]** Implement Grad-CAM for ResNet18.
- [x] **5.1.6 [ANTIGRAVITY]** Identify the target feature layer for EfficientNet-B0.
- [x] **5.1.7 [ANTIGRAVITY]** Implement Grad-CAM for EfficientNet-B0.
- [x] **5.1.8 [ANTIGRAVITY]** Implement original-image output.
- [x] **5.1.9 [ANTIGRAVITY]** Implement heatmap output.
- [x] **5.1.10 [ANTIGRAVITY]** Implement overlay output.
- [x] **5.1.11 [ANTIGRAVITY]** Add Grad-CAM tests for every supported architecture.
- [x] **5.1.12 [BOTH]** Inspect generated explanations using real dataset images.

## 5.2 Prepare model artifacts

- [x] **5.2.1 [ANTIGRAVITY]** Define a standard model artifact directory structure.
- [x] **5.2.2 [ANTIGRAVITY]** Save model weights separately from source code.
- [x] **5.2.3 [ANTIGRAVITY]** Save model architecture metadata.
- [x] **5.2.4 [ANTIGRAVITY]** Save preprocessing metadata.
- [x] **5.2.5 [ANTIGRAVITY]** Save the classification threshold.
- [x] **5.2.6 [ANTIGRAVITY]** Save evaluation metrics.
- [x] **5.2.7 [ANTIGRAVITY]** Save the dataset version reference.
- [x] **5.2.8 [ANTIGRAVITY]** Implement model artifact integrity checks.
- [x] **5.2.9 [ANTIGRAVITY]** Document how to load a model artifact.

**Verification:** A saved model can be loaded with its original preprocessing settings, threshold and metadata.

---

# PHASE 6 — MLflow experiment tracking and model registry

**Objective:** Track every experiment and manage model versions.

## 6.1 Prepare MLflow

- [x] **6.1.1 [MANUAL]** Confirm the local PostgreSQL service is available.
- [x] **6.1.2 [ANTIGRAVITY]** Create the `visionqc_mlflow` database configuration.
- [x] **6.1.3 [ANTIGRAVITY]** Create the MLflow service configuration.
- [x] **6.1.4 [ANTIGRAVITY]** Configure PostgreSQL as the MLflow backend store.
- [x] **6.1.5 [ANTIGRAVITY]** Configure persistent artifact storage.
- [x] **6.1.6 [ANTIGRAVITY]** Pin the MLflow version.
- [x] **6.1.7 [BOTH]** Start MLflow locally.
- [x] **6.1.8 [BOTH]** Open the MLflow UI.
- [x] **6.1.9 [BOTH]** Verify that MLflow can connect to PostgreSQL.
- [x] **6.1.10 [BOTH]** Verify that an artifact can be uploaded and retrieved.

## 6.2 Integrate training with MLflow

- [x] **6.2.1 [ANTIGRAVITY]** Implement the shared MLflow tracking utility.
- [x] **6.2.2 [ANTIGRAVITY]** Log experiment names.
- [x] **6.2.3 [ANTIGRAVITY]** Log model architecture parameters.
- [x] **6.2.4 [ANTIGRAVITY]** Log training hyperparameters.
- [x] **6.2.5 [ANTIGRAVITY]** Log dataset version references.
- [x] **6.2.6 [ANTIGRAVITY]** Log preprocessing configuration.
- [x] **6.2.7 [ANTIGRAVITY]** Log training metrics.
- [x] **6.2.8 [ANTIGRAVITY]** Log validation metrics.
- [x] **6.2.9 [ANTIGRAVITY]** Log evaluation plots.
- [x] **6.2.10 [ANTIGRAVITY]** Log model artifacts.
- [x] **6.2.11 [ANTIGRAVITY]** Add MLflow logging tests.
- [x] **6.2.12 [BOTH]** Run one experiment and verify its parameters, metrics and artifacts in the UI.

## 6.3 Configure model registry

- [x] **6.3.1 [ANTIGRAVITY]** Define the registered model naming convention.
- [x] **6.3.2 [ANTIGRAVITY]** Implement model registration.
- [x] **6.3.3 [ANTIGRAVITY]** Associate registered versions with their MLflow runs.
- [x] **6.3.4 [ANTIGRAVITY]** Store dataset and evaluation metadata with each version.
- [x] **6.3.5 [ANTIGRAVITY]** Implement model-version retrieval.
- [x] **6.3.6 [ANTIGRAVITY]** Implement model approval metadata.
- [x] **6.3.7 [ANTIGRAVITY]** Implement model deployment metadata.
- [x] **6.3.8 [BOTH]** Verify that multiple model versions can be registered and inspected.

**Verification:** MLflow contains real training runs, their metrics, artifacts and model versions.

---

# PHASE 7 — Airflow orchestration

**Objective:** Turn the individual ML modules into reproducible workflows.

## 7.1 Prepare Airflow

- [x] **7.1.1 [ANTIGRAVITY]** Create the `visionqc_airflow` database configuration.
- [x] **7.1.2 [ANTIGRAVITY]** Configure the selected Airflow release.
- [x] **7.1.3 [ANTIGRAVITY]** Configure the selected executor.
- [x] **7.1.4 [ANTIGRAVITY]** Configure the Airflow metadata database.
- [x] **7.1.5 [ANTIGRAVITY]** Configure persistent Airflow logs.
- [x] **7.1.6 [ANTIGRAVITY]** Configure the DAG directory.
- [x] **7.1.7 [ANTIGRAVITY]** Configure the required Airflow service processes for the selected release.
- [x] **7.1.8 [BOTH]** Start Airflow locally.
- [x] **7.1.9 [BOTH]** Open the Airflow UI.
- [x] **7.1.10 [BOTH]** Verify that the metadata database is healthy.
- [x] **7.1.11 [BOTH]** Verify that a simple test DAG executes successfully.

## 7.2 Build the training DAG

Create the training DAG using reusable modules from `ml/`. Do not place the complete training implementation inside the DAG file.

- [x] **7.2.1 [ANTIGRAVITY]** Create the training DAG file.
- [x] **7.2.2 [ANTIGRAVITY]** Add the dataset-ingestion task.
- [x] **7.2.3 [ANTIGRAVITY]** Add the dataset-validation task.
- [x] **7.2.4 [ANTIGRAVITY]** Add the preprocessing task.
- [x] **7.2.5 [ANTIGRAVITY]** Add the data-preparation task.
- [x] **7.2.6 [ANTIGRAVITY]** Add the feature-engineering task.
- [x] **7.2.7 [ANTIGRAVITY]** Add the model-training task.
- [x] **7.2.8 [ANTIGRAVITY]** Add the model-evaluation task.
- [x] **7.2.9 [ANTIGRAVITY]** Add the MLflow-logging task.
- [x] **7.2.10 [ANTIGRAVITY]** Add the model-comparison task.
- [x] **7.2.11 [ANTIGRAVITY]** Add the quality-gate task.
- [x] **7.2.12 [ANTIGRAVITY]** Add the model-registration task.
- [x] **7.2.13 [ANTIGRAVITY]** Define task dependencies.
- [x] **7.2.14 [ANTIGRAVITY]** Configure task retries and failure handling.
- [x] **7.2.15 [ANTIGRAVITY]** Add DAG validation tests.
- [x] **7.2.16 [BOTH]** Trigger the training DAG manually.
- [x] **7.2.17 [BOTH]** Inspect each task's execution result.
- [x] **7.2.18 [BOTH]** Verify that the resulting experiment appears in MLflow.
- [x] **7.2.19 [BOTH]** Verify that a model is registered only after the quality gate passes.

## 7.3 Build the retraining DAG

- [x] **7.3.1 [ANTIGRAVITY]** Create the retraining DAG file.
- [x] **7.3.2 [ANTIGRAVITY]** Add a dataset-version input.
- [x] **7.3.3 [ANTIGRAVITY]** Reuse the shared preprocessing module.
- [x] **7.3.4 [ANTIGRAVITY]** Reuse the shared training module.
- [x] **7.3.5 [ANTIGRAVITY]** Reuse the shared evaluation module.
- [x] **7.3.6 [ANTIGRAVITY]** Reuse the shared quality-gate implementation.
- [x] **7.3.7 [ANTIGRAVITY]** Prevent automatic deployment when the quality gate fails.
- [x] **7.3.8 [ANTIGRAVITY]** Add retraining DAG tests.
- [x] **7.3.9 [BOTH]** Trigger a test retraining run.
- [x] **7.3.10 [BOTH]** Verify the run is visible in Airflow.
- [x] **7.3.11 [BOTH]** Verify the retraining result is visible in MLflow.

**Verification:** Both DAGs execute successfully and preserve task-level history.

---

# PHASE 8 — Backend foundation and PostgreSQL

**Objective:** Build the application API and persistent data layer.

## 8.1 Prepare the backend

- [x] **8.1.1 [ANTIGRAVITY]** Create the backend Python package.
- [x] **8.1.2 [ANTIGRAVITY]** Create the backend dependency manifest.
- [x] **8.1.3 [ANTIGRAVITY]** Create the backend configuration module.
- [x] **8.1.4 [ANTIGRAVITY]** Create the FastAPI application entry point.
- [x] **8.1.5 [ANTIGRAVITY]** Create the API router structure.
- [x] **8.1.6 [ANTIGRAVITY]** Configure Pydantic settings.
- [x] **8.1.7 [ANTIGRAVITY]** Configure structured application logging.
- [x] **8.1.8 [ANTIGRAVITY]** Configure CORS for the local frontend origin.
- [x] **8.1.9 [ANTIGRAVITY]** Add the canonical health endpoint.
- [x] **8.1.10 [ANTIGRAVITY]** Add the API version endpoint.
- [x] **8.1.11 [BOTH]** Start FastAPI locally.
- [x] **8.1.12 [BOTH]** Open Swagger UI.
- [x] **8.1.13 [BOTH]** Verify the health endpoint returns a valid response.

## 8.2 Configure PostgreSQL

- [x] **8.2.1 [ANTIGRAVITY]** Configure the PostgreSQL 18 service.
- [x] **8.2.2 [MANUAL]** Start the local PostgreSQL service.
- [x] **8.2.3 [ANTIGRAVITY]** Create the `visionqc_app` database configuration.
- [x] **8.2.4 [ANTIGRAVITY]** Create a dedicated application database user.
- [x] **8.2.5 [ANTIGRAVITY]** Configure SQLAlchemy 2.x.
- [x] **8.2.6 [ANTIGRAVITY]** Configure the SQLAlchemy session lifecycle.
- [x] **8.2.7 [ANTIGRAVITY]** Configure Alembic.
- [x] **8.2.8 [ANTIGRAVITY]** Create the initial database migration.
- [x] **8.2.9 [ANTIGRAVITY]** Create the predictions table.
- [x] **8.2.10 [ANTIGRAVITY]** Create the model-deployments table.
- [x] **8.2.11 [ANTIGRAVITY]** Create the dataset-versions table.
- [x] **8.2.12 [ANTIGRAVITY]** Create the pipeline-runs table.
- [x] **8.2.13 [ANTIGRAVITY]** Create the drift-reports table.
- [x] **8.2.14 [ANTIGRAVITY]** Create the retraining-jobs table.
- [x] **8.2.15 [ANTIGRAVITY]** Create the audit-logs table.
- [x] **8.2.16 [ANTIGRAVITY]** Add required indexes and constraints.
- [x] **8.2.17 [ANTIGRAVITY]** Add database repository functions.
- [x] **8.2.18 [ANTIGRAVITY]** Add database integration tests.
- [x] **8.2.19 [BOTH]** Run the Alembic migration.
- [x] **8.2.20 [BOTH]** Verify that all expected tables exist.

## 8.3 Implement backend service boundaries

- [x] **8.3.1 [ANTIGRAVITY]** Create the inspection service.
- [x] **8.3.2 [ANTIGRAVITY]** Create the model-management service.
- [x] **8.3.3 [ANTIGRAVITY]** Create the experiment service.
- [x] **8.3.4 [ANTIGRAVITY]** Create the dataset service.
- [x] **8.3.5 [ANTIGRAVITY]** Create the pipeline service.
- [x] **8.3.6 [ANTIGRAVITY]** Create the monitoring service.
- [x] **8.3.7 [ANTIGRAVITY]** Create the drift service.
- [x] **8.3.8 [ANTIGRAVITY]** Create the retraining service.
- [x] **8.3.9 [ANTIGRAVITY]** Add service-level unit tests.

**Verification:** FastAPI can connect to PostgreSQL, run migrations and execute tested service functions.

---

# PHASE 9 — Model serving and inspection API

**Objective:** Connect the selected model to FastAPI and deliver genuine inspection results.

## 9.1 Implement model loading

- [x] **9.1.1 [ANTIGRAVITY]** Implement the model artifact loader.
- [x] **9.1.2 [ANTIGRAVITY]** Implement model metadata validation.
- [x] **9.1.3 [ANTIGRAVITY]** Implement model loading during application startup.
- [x] **9.1.4 [ANTIGRAVITY]** Implement active-model retrieval.
- [x] **9.1.5 [ANTIGRAVITY]** Implement controlled model reload.
- [x] **9.1.6 [ANTIGRAVITY]** Add model-loading tests.
- [x] **9.1.7 [BOTH]** Start the backend with the selected registered model.
- [x] **9.1.8 [BOTH]** Verify that the active model loads successfully.

## 9.2 Implement image inspection

- [x] **9.2.1 [ANTIGRAVITY]** Create the inspection API router.
- [x] **9.2.2 [ANTIGRAVITY]** Implement uploaded-file size validation.
- [x] **9.2.3 [ANTIGRAVITY]** Implement file-content validation.
- [x] **9.2.4 [ANTIGRAVITY]** Implement image decoding validation.
- [x] **9.2.5 [ANTIGRAVITY]** Implement safe temporary-file handling.
- [x] **9.2.6 [ANTIGRAVITY]** Connect the shared preprocessing function.
- [x] **9.2.7 [ANTIGRAVITY]** Connect the loaded model to the inference function.
- [x] **9.2.8 [ANTIGRAVITY]** Implement defect probability calculation.
- [x] **9.2.9 [ANTIGRAVITY]** Apply the configured classification threshold.
- [x] **9.2.10 [ANTIGRAVITY]** Measure inference latency.
- [x] **9.2.11 [ANTIGRAVITY]** Generate a prediction identifier.
- [x] **9.2.12 [ANTIGRAVITY]** Persist prediction metadata in PostgreSQL.
- [x] **9.2.13 [ANTIGRAVITY]** Return the prediction result as structured JSON.
- [x] **9.2.14 [ANTIGRAVITY]** Add prediction endpoint tests.
- [x] **9.2.15 [BOTH]** Submit a real OK image to the API.
- [x] **9.2.16 [BOTH]** Submit a real DEFECTIVE image to the API.
- [x] **9.2.17 [BOTH]** Verify both responses contain the required metadata.
- [x] **9.2.18 [BOTH]** Verify prediction records are persisted.

## 9.3 Implement Grad-CAM API integration

- [x] **9.3.1 [ANTIGRAVITY]** Add an optional explainability parameter to the inspection API.
- [x] **9.3.2 [ANTIGRAVITY]** Connect the Grad-CAM implementation to inference.
- [x] **9.3.3 [ANTIGRAVITY]** Return the original image reference.
- [x] **9.3.4 [ANTIGRAVITY]** Return the heatmap reference.
- [x] **9.3.5 [ANTIGRAVITY]** Return the overlay reference.
- [x] **9.3.6 [ANTIGRAVITY]** Add explainability API tests.
- [x] **9.3.7 [BOTH]** Verify the three visualization modes using a real inspection.

## 9.4 Implement supporting APIs

- [x] **9.4.1 [ANTIGRAVITY]** Implement `GET /health`.
- [x] **9.4.2 [ANTIGRAVITY]** Implement `POST /predict` as the documented compatibility route.
- [x] **9.4.3 [ANTIGRAVITY]** Implement `GET /model-info`.
- [x] **9.4.4 [ANTIGRAVITY]** Implement `/api/v1/models`.
- [x] **9.4.5 [ANTIGRAVITY]** Implement `/api/v1/experiments`.
- [x] **9.4.6 [ANTIGRAVITY]** Implement `/api/v1/datasets`.
- [x] **9.4.7 [ANTIGRAVITY]** Implement `/api/v1/pipelines`.
- [x] **9.4.8 [ANTIGRAVITY]** Implement `/api/v1/monitoring`.
- [x] **9.4.9 [ANTIGRAVITY]** Implement `/api/v1/drift`.
- [x] **9.4.10 [ANTIGRAVITY]** Implement `/api/v1/retraining`.
- [x] **9.4.11 [ANTIGRAVITY]** Add API response-schema tests.
- [x] **9.4.12 [BOTH]** Verify all API routes through Swagger UI.

**Verification:** A real image can be uploaded, classified, explained and recorded through the backend.

---

# PHASE 10 — Frontend foundation and design system

**Objective:** Build the approved visual foundation before building individual dashboard pages.

## 10.1 Initialize the frontend

- [x] **10.1.1 [ANTIGRAVITY]** Initialize the Next.js 16 application.
- [x] **10.1.2 [ANTIGRAVITY]** Configure React 19.
- [x] **10.1.3 [ANTIGRAVITY]** Configure TypeScript.
- [x] **10.1.4 [ANTIGRAVITY]** Configure the selected Tailwind CSS version.
- [x] **10.1.5 [ANTIGRAVITY]** Configure shadcn/ui.
- [x] **10.1.6 [ANTIGRAVITY]** Configure Radix UI dependencies.
- [x] **10.1.7 [ANTIGRAVITY]** Configure Lucide React.
- [x] **10.1.8 [ANTIGRAVITY]** Configure Recharts.
- [x] **10.1.9 [ANTIGRAVITY]** Configure Framer Motion.
- [x] **10.1.10 [ANTIGRAVITY]** Configure ESLint.
- [x] **10.1.11 [ANTIGRAVITY]** Configure Prettier.
- [x] **10.1.12 [ANTIGRAVITY]** Configure the frontend environment variables.
- [x] **10.1.13 [BOTH]** Start the frontend locally.
- [x] **10.1.14 [BOTH]** Verify the default application loads.

## 10.2 Implement design tokens

- [x] **10.2.1 [ANTIGRAVITY]** Create the global design-token stylesheet.
- [x] **10.2.2 [ANTIGRAVITY]** Add the Ink token.
- [x] **10.2.3 [ANTIGRAVITY]** Add the Graphite token.
- [x] **10.2.4 [ANTIGRAVITY]** Add the Steel Blue token.
- [x] **10.2.5 [ANTIGRAVITY]** Add the Muted Blue token.
- [x] **10.2.6 [ANTIGRAVITY]** Add the Paper token.
- [x] **10.2.7 [ANTIGRAVITY]** Add the White token.
- [x] **10.2.8 [ANTIGRAVITY]** Add the Border token.
- [x] **10.2.9 [ANTIGRAVITY]** Add the Muted Grey token.
- [x] **10.2.10 [ANTIGRAVITY]** Add the Light Grey token.
- [x] **10.2.11 [ANTIGRAVITY]** Add the semantic status tokens.
- [x] **10.2.12 [ANTIGRAVITY]** Add the typography tokens.
- [x] **10.2.13 [ANTIGRAVITY]** Add the spacing scale.
- [x] **10.2.14 [ANTIGRAVITY]** Add the approved radius tokens.
- [x] **10.2.15 [ANTIGRAVITY]** Add the default border token.
- [x] **10.2.16 [ANTIGRAVITY]** Configure Geist Sans as the licensed-font fallback.
- [x] **10.2.17 [ANTIGRAVITY]** Configure Geist Mono for technical metadata.
- [x] **10.2.18 [ANTIGRAVITY]** Ensure Roobert is used only if a properly licensed font file is available.
- [x] **10.2.19 [ANTIGRAVITY]** Verify all shared components consume centralized tokens.

## 10.3 Build shared components

- [x] **10.3.1 [ANTIGRAVITY]** Build the primary button.
- [x] **10.3.2 [ANTIGRAVITY]** Build the secondary button.
- [x] **10.3.3 [ANTIGRAVITY]** Build the destructive button.
- [x] **10.3.4 [ANTIGRAVITY]** Build the standard card.
- [x] **10.3.5 [ANTIGRAVITY]** Build the page heading component.
- [x] **10.3.6 [ANTIGRAVITY]** Build the section heading component.
- [x] **10.3.7 [ANTIGRAVITY]** Build the status indicator.
- [x] **10.3.8 [ANTIGRAVITY]** Build the labelled input component.
- [x] **10.3.9 [ANTIGRAVITY]** Build the data table component.
- [x] **10.3.10 [ANTIGRAVITY]** Build the empty-state component.
- [x] **10.3.11 [ANTIGRAVITY]** Build the loading-state component.
- [x] **10.3.12 [ANTIGRAVITY]** Build the error-state component.
- [x] **10.3.13 [ANTIGRAVITY]** Build the confirmation dialog.
- [x] **10.3.14 [ANTIGRAVITY]** Build the tooltip component.
- [x] **10.3.15 [ANTIGRAVITY]** Verify keyboard interaction for the shared components.

## 10.4 Build the application shell

- [x] **10.4.1 [ANTIGRAVITY]** Build the application sidebar.
- [x] **10.4.2 [ANTIGRAVITY]** Add the VisionQC product identity.
- [x] **10.4.3 [ANTIGRAVITY]** Add the nine required navigation links.
- [x] **10.4.4 [ANTIGRAVITY]** Implement the active navigation state.
- [x] **10.4.5 [ANTIGRAVITY]** Implement sidebar collapse.
- [x] **10.4.6 [ANTIGRAVITY]** Implement the responsive navigation behavior.
- [x] **10.4.7 [ANTIGRAVITY]** Build the top application header.
- [x] **10.4.8 [ANTIGRAVITY]** Add the page-context area.
- [x] **10.4.9 [ANTIGRAVITY]** Add the real system-health indicator.
- [x] **10.4.10 [ANTIGRAVITY]** Add the contextual action area.
- [x] **10.4.11 [ANTIGRAVITY]** Add the shared content container.
- [x] **10.4.12 [ANTIGRAVITY]** Configure the root route to redirect to `/overview`.
- [x] **10.4.13 [ANTIGRAVITY]** Verify that no login or signup interface is introduced.
- [x] **10.4.14 [BOTH]** Inspect the application shell at desktop width.
- [x] **10.4.15 [BOTH]** Inspect the application shell at tablet width.
- [x] **10.4.16 [BOTH]** Inspect the application shell at mobile width.

**Verification:** The shared visual foundation is implemented and every page can use the same application shell.

---

# PHASE 11 — Frontend API integration and dashboard pages

**Objective:** Build all nine pages using real backend data.

## 11.1 Configure API integration

- [x] **11.1.1 [ANTIGRAVITY]** Create the frontend API client.
- [x] **11.1.2 [ANTIGRAVITY]** Define shared API response types.
- [x] **11.1.3 [ANTIGRAVITY]** Define prediction response types.
- [x] **11.1.4 [ANTIGRAVITY]** Define model metadata types.
- [x] **11.1.5 [ANTIGRAVITY]** Define experiment response types.
- [x] **11.1.6 [ANTIGRAVITY]** Define dataset response types.
- [x] **11.1.7 [ANTIGRAVITY]** Define pipeline response types.
- [x] **11.1.8 [ANTIGRAVITY]** Define monitoring response types.
- [x] **11.1.9 [ANTIGRAVITY]** Define drift response types.
- [x] **11.1.10 [ANTIGRAVITY]** Define retraining response types.
- [x] **11.1.11 [ANTIGRAVITY]** Implement API error handling.
- [x] **11.1.12 [ANTIGRAVITY]** Implement loading and retry behavior.
- [x] **11.1.13 [ANTIGRAVITY]** Add API client tests.
- [x] **11.1.14 [BOTH]** Verify frontend-to-backend communication.

## 11.2 Build the Inspection Workbench

- [x] **11.2.1 [ANTIGRAVITY]** Create the inspection page route.
- [x] **11.2.2 [ANTIGRAVITY]** Build the image upload area.
- [x] **11.2.3 [ANTIGRAVITY]** Implement frontend file-type validation.
- [x] **11.2.4 [ANTIGRAVITY]** Implement frontend file-size validation.
- [x] **11.2.5 [ANTIGRAVITY]** Build the image preview.
- [x] **11.2.6 [ANTIGRAVITY]** Build the Analyze button.
- [x] **11.2.7 [ANTIGRAVITY]** Connect image submission to the inspection API.
- [x] **11.2.8 [ANTIGRAVITY]** Build the inspection loading state.
- [x] **11.2.9 [ANTIGRAVITY]** Build the OK result state.
- [x] **11.2.10 [ANTIGRAVITY]** Build the DEFECTIVE result state.
- [x] **11.2.11 [ANTIGRAVITY]** Display the confidence or probability information with clear labelling.
- [x] **11.2.12 [ANTIGRAVITY]** Display the model version.
- [x] **11.2.13 [ANTIGRAVITY]** Display inference latency with units.
- [x] **11.2.14 [ANTIGRAVITY]** Build the original-image view.
- [x] **11.2.15 [ANTIGRAVITY]** Build the Grad-CAM heatmap view.
- [x] **11.2.16 [ANTIGRAVITY]** Build the Grad-CAM overlay view.
- [x] **11.2.17 [ANTIGRAVITY]** Implement the visualization mode selector.
- [x] **11.2.18 [ANTIGRAVITY]** Build the technical model-information panel.
- [x] **11.2.19 [ANTIGRAVITY]** Add an inspection error state.
- [x] **11.2.20 [ANTIGRAVITY]** Add an initial empty state.
- [x] **11.2.21 [BOTH]** Test the complete inspection workflow using an actual OK image.
- [x] **11.2.22 [BOTH]** Test the complete inspection workflow using an actual DEFECTIVE image.
- [x] **11.2.23 [BOTH]** Verify all three Grad-CAM views display actual generated outputs.

## 11.3 Build Overview

- [x] **11.3.1 [ANTIGRAVITY]** Create the Overview page route.
- [x] **11.3.2 [ANTIGRAVITY]** Add the page heading and description.
- [x] **11.3.3 [ANTIGRAVITY]** Connect the API health indicator.
- [x] **11.3.4 [ANTIGRAVITY]** Connect the active-model information.
- [x] **11.3.5 [ANTIGRAVITY]** Connect the recent-inspection count.
- [x] **11.3.6 [ANTIGRAVITY]** Connect the latest pipeline state.
- [x] **11.3.7 [ANTIGRAVITY]** Build the prediction distribution chart.
- [x] **11.3.8 [ANTIGRAVITY]** Build the recent pipeline activity section.
- [x] **11.3.9 [ANTIGRAVITY]** Build the monitoring alerts section.
- [x] **11.3.10 [ANTIGRAVITY]** Add an empty state for missing inspection data.
- [x] **11.3.11 [ANTIGRAVITY]** Add an error state for unavailable services.
- [x] **11.3.12 [BOTH]** Verify every Overview value against its API response.

## 11.4 Build Experiments

- [x] **11.4.1 [ANTIGRAVITY]** Create the Experiments page route.
- [x] **11.4.2 [ANTIGRAVITY]** Connect the MLflow experiment API.
- [x] **11.4.3 [ANTIGRAVITY]** Build the experiment history table.
- [x] **11.4.4 [ANTIGRAVITY]** Display model architecture.
- [x] **11.4.5 [ANTIGRAVITY]** Display dataset version.
- [x] **11.4.6 [ANTIGRAVITY]** Display training configuration.
- [x] **11.4.7 [ANTIGRAVITY]** Display experiment status and duration.
- [x] **11.4.8 [ANTIGRAVITY]** Build the model comparison chart.
- [x] **11.4.9 [ANTIGRAVITY]** Display defect recall and false-negative rate.
- [x] **11.4.10 [ANTIGRAVITY]** Add experiment empty and error states.
- [x] **11.4.11 [BOTH]** Verify experiment values against MLflow.

## 11.5 Build Datasets

- [x] **11.5.1 [ANTIGRAVITY]** Create the Datasets page route.
- [x] **11.5.2 [ANTIGRAVITY]** Connect the dataset metadata API.
- [x] **11.5.3 [ANTIGRAVITY]** Display dataset name and version.
- [x] **11.5.4 [ANTIGRAVITY]** Display actual image counts.
- [x] **11.5.5 [ANTIGRAVITY]** Display OK and DEFECTIVE counts.
- [x] **11.5.6 [ANTIGRAVITY]** Display split information.
- [x] **11.5.7 [ANTIGRAVITY]** Display augmentation configuration.
- [x] **11.5.8 [ANTIGRAVITY]** Display the DVC reference.
- [x] **11.5.9 [ANTIGRAVITY]** Add dataset empty and error states.
- [x] **11.5.10 [BOTH]** Verify dataset information against DVC and the validation report.

## 11.6 Build Pipelines

- [x] **11.6.1 [ANTIGRAVITY]** Create the Pipelines page route.
- [x] **11.6.2 [ANTIGRAVITY]** Connect the Airflow API integration.
- [x] **11.6.3 [ANTIGRAVITY]** Display DAG names.
- [x] **11.6.4 [ANTIGRAVITY]** Display latest execution time.
- [x] **11.6.5 [ANTIGRAVITY]** Display execution status.
- [x] **11.6.6 [ANTIGRAVITY]** Display execution duration.
- [x] **11.6.7 [ANTIGRAVITY]** Display failed task counts.
- [x] **11.6.8 [ANTIGRAVITY]** Build the pipeline task-dependency view.
- [x] **11.6.9 [ANTIGRAVITY]** Build the pipeline execution history table.
- [x] **11.6.10 [ANTIGRAVITY]** Add pipeline empty and error states.
- [x] **11.6.11 [BOTH]** Verify the frontend status against the Airflow UI.

## 11.7 Build Model Registry

- [x] **11.7.1 [ANTIGRAVITY]** Create the Model Registry page route.
- [x] **11.7.2 [ANTIGRAVITY]** Connect the model registry API.
- [x] **11.7.3 [ANTIGRAVITY]** Display model names.
- [x] **11.7.4 [ANTIGRAVITY]** Display model versions.
- [x] **11.7.5 [ANTIGRAVITY]** Display architecture and dataset reference.
- [x] **11.7.6 [ANTIGRAVITY]** Display evaluation metrics.
- [x] **11.7.7 [ANTIGRAVITY]** Display approval state.
- [x] **11.7.8 [ANTIGRAVITY]** Display deployment state.
- [x] **11.7.9 [ANTIGRAVITY]** Highlight the active deployed model.
- [x] **11.7.10 [ANTIGRAVITY]** Implement the controlled promotion action.
- [x] **11.7.11 [ANTIGRAVITY]** Add a promotion confirmation dialog.
- [x] **11.7.12 [ANTIGRAVITY]** Prevent promotion when the quality gate has failed.
- [x] **11.7.13 [BOTH]** Verify model metadata against MLflow.

## 11.8 Build Monitoring

- [x] **11.8.1 [ANTIGRAVITY]** Create the Monitoring page route.
- [x] **11.8.2 [ANTIGRAVITY]** Build the operational monitoring section.
- [x] **11.8.3 [ANTIGRAVITY]** Display request volume.
- [x] **11.8.4 [ANTIGRAVITY]** Display error rate.
- [x] **11.8.5 [ANTIGRAVITY]** Display inference latency.
- [x] **11.8.6 [ANTIGRAVITY]** Display throughput.
- [x] **11.8.7 [ANTIGRAVITY]** Display service health.
- [x] **11.8.8 [ANTIGRAVITY]** Build the ML monitoring section.
- [x] **11.8.9 [ANTIGRAVITY]** Display prediction distribution.
- [x] **11.8.10 [ANTIGRAVITY]** Display confidence distribution.
- [x] **11.8.11 [ANTIGRAVITY]** Display image drift measurements.
- [x] **11.8.12 [ANTIGRAVITY]** Display reference-versus-incoming distributions.
- [x] **11.8.13 [ANTIGRAVITY]** Display measured performance only when ground-truth labels are available.
- [x] **11.8.14 [ANTIGRAVITY]** Add chart units, labels and time ranges.
- [x] **11.8.15 [ANTIGRAVITY]** Add monitoring empty and error states.
- [x] **11.8.16 [BOTH]** Verify monitoring values against Prometheus and the backend.

## 11.9 Build Retraining

- [x] **11.9.1 [ANTIGRAVITY]** Create the Retraining page route.
- [x] **11.9.2 [ANTIGRAVITY]** Connect the retraining API.
- [x] **11.9.3 [ANTIGRAVITY]** Display drift status.
- [x] **11.9.4 [ANTIGRAVITY]** Display retraining trigger reason.
- [x] **11.9.5 [ANTIGRAVITY]** Display dataset version.
- [x] **11.9.6 [ANTIGRAVITY]** Display retraining execution status.
- [x] **11.9.7 [ANTIGRAVITY]** Display evaluation result.
- [x] **11.9.8 [ANTIGRAVITY]** Display quality-gate status.
- [x] **11.9.9 [ANTIGRAVITY]** Display approval and deployment decisions.
- [x] **11.9.10 [ANTIGRAVITY]** Implement the retraining request action.
- [x] **11.9.11 [ANTIGRAVITY]** Add retraining confirmation.
- [x] **11.9.12 [ANTIGRAVITY]** Clearly distinguish requested, running, evaluated, approved and deployed states.
- [x] **11.9.13 [ANTIGRAVITY]** Prevent drift alerts from automatically deploying a new model.
- [x] **11.9.14 [BOTH]** Verify the page against a real Airflow retraining execution.

## 11.10 Build Documentation

- [x] **11.10.1 [ANTIGRAVITY]** Create the Documentation page route.
- [x] **11.10.2 [ANTIGRAVITY]** Add the architecture documentation section.
- [x] **11.10.3 [ANTIGRAVITY]** Add the Data Card section.
- [x] **11.10.4 [ANTIGRAVITY]** Add the Model Card section.
- [x] **11.10.5 [ANTIGRAVITY]** Add the training methodology section.
- [x] **11.10.6 [ANTIGRAVITY]** Add the evaluation methodology section.
- [x] **11.10.7 [ANTIGRAVITY]** Add the API documentation section.
- [x] **11.10.8 [ANTIGRAVITY]** Add the known limitations section.
- [x] **11.10.9 [ANTIGRAVITY]** Verify documentation content against the actual implementation.

**Verification:** All nine dashboard routes exist and display actual service data or explicit empty/error states.

---

# PHASE 12 — Monitoring, drift detection and controlled retraining

**Objective:** Implement operational observability and a safe model-improvement workflow.

## 12.1 Prometheus metrics

- [x] **12.1.1 [ANTIGRAVITY]** Configure the Prometheus service.
- [x] **12.1.2 [ANTIGRAVITY]** Expose the FastAPI metrics endpoint.
- [x] **12.1.3 [ANTIGRAVITY]** Add a request counter.
- [x] **12.1.4 [ANTIGRAVITY]** Add an error counter.
- [x] **12.1.5 [ANTIGRAVITY]** Add an inference-latency histogram.
- [x] **12.1.6 [ANTIGRAVITY]** Add a prediction-class counter.
- [x] **12.1.7 [ANTIGRAVITY]** Add a confidence-distribution metric.
- [x] **12.1.8 [ANTIGRAVITY]** Add a service-health metric.
- [x] **12.1.9 [ANTIGRAVITY]** Avoid high-cardinality labels such as unique image IDs.
- [x] **12.1.10 [ANTIGRAVITY]** Configure Prometheus scraping.
- [x] **12.1.11 [BOTH]** Verify that Prometheus receives backend metrics.

## 12.2 Grafana

- [x] **12.2.1 [ANTIGRAVITY]** Configure the Grafana service.
- [x] **12.2.2 [ANTIGRAVITY]** Configure Prometheus as a data source.
- [x] **12.2.3 [ANTIGRAVITY]** Create the operational dashboard.
- [x] **12.2.4 [ANTIGRAVITY]** Add request-volume visualization.
- [x] **12.2.5 [ANTIGRAVITY]** Add error-rate visualization.
- [x] **12.2.6 [ANTIGRAVITY]** Add latency visualization.
- [x] **12.2.7 [ANTIGRAVITY]** Add throughput visualization.
- [x] **12.2.8 [ANTIGRAVITY]** Create the ML monitoring dashboard.
- [x] **12.2.9 [ANTIGRAVITY]** Add prediction-distribution visualization.
- [x] **12.2.10 [ANTIGRAVITY]** Add confidence-distribution visualization.
- [x] **12.2.11 [ANTIGRAVITY]** Add drift visualization.
- [x] **12.2.12 [BOTH]** Verify both dashboards using generated real application traffic.

## 12.3 Implement drift feature extraction

- [x] **12.3.1 [ANTIGRAVITY]** Create the image-feature extraction module.
- [x] **12.3.2 [ANTIGRAVITY]** Implement mean-brightness extraction.
- [x] **12.3.3 [ANTIGRAVITY]** Implement intensity-standard-deviation extraction.
- [x] **12.3.4 [ANTIGRAVITY]** Implement contrast-statistic extraction.
- [x] **12.3.5 [ANTIGRAVITY]** Implement image-sharpness extraction.
- [x] **12.3.6 [ANTIGRAVITY]** Implement histogram-feature extraction.
- [x] **12.3.7 [ANTIGRAVITY]** Add feature-extraction tests.
- [x] **12.3.8 [ANTIGRAVITY]** Generate reference feature distributions from the training reference data.

## 12.4 Implement drift detection

- [x] **12.4.1 [ANTIGRAVITY]** Create the drift detection module.
- [x] **12.4.2 [ANTIGRAVITY]** Implement incoming-batch feature extraction.
- [x] **12.4.3 [ANTIGRAVITY]** Implement the selected statistical comparison method.
- [x] **12.4.4 [ANTIGRAVITY]** Implement configurable drift thresholds.
- [x] **12.4.5 [ANTIGRAVITY]** Implement a configurable minimum observation count.
- [x] **12.4.6 [ANTIGRAVITY]** Implement a configurable observation window.
- [x] **12.4.7 [ANTIGRAVITY]** Implement drift severity classification.
- [x] **12.4.8 [ANTIGRAVITY]** Persist drift reports in PostgreSQL.
- [x] **12.4.9 [ANTIGRAVITY]** Expose drift history through the API.
- [x] **12.4.10 [ANTIGRAVITY]** Expose drift metrics to Prometheus.
- [x] **12.4.11 [ANTIGRAVITY]** Add drift unit tests.
- [x] **12.4.12 [BOTH]** Run drift detection against an unchanged reference batch.
- [x] **12.4.13 [BOTH]** Run drift detection against a brightness-shifted batch.
- [x] **12.4.14 [BOTH]** Run drift detection against a contrast-shifted batch.
- [x] **12.4.15 [BOTH]** Run drift detection against a noisy batch.
- [x] **12.4.16 [BOTH]** Run drift detection against a blurred batch.
- [x] **12.4.17 [BOTH]** Verify the recorded results and thresholds.

## 12.5 Separate drift from model performance

- [x] **12.5.1 [ANTIGRAVITY]** Define data drift as a change in input-data distributions.
- [x] **12.5.2 [ANTIGRAVITY]** Define prediction drift as a change in model-output distributions.
- [x] **12.5.3 [ANTIGRAVITY]** Define measured performance degradation using labelled evaluation data.
- [x] **12.5.4 [ANTIGRAVITY]** Add support for storing ground-truth labels when available.
- [x] **12.5.5 [ANTIGRAVITY]** Prevent the application from reporting accuracy degradation without labels.
- [x] **12.5.6 [ANTIGRAVITY]** Document the limitations of unsupervised drift detection.

## 12.6 Implement controlled retraining

- [x] **12.6.1 [ANTIGRAVITY]** Implement the retraining request service.
- [x] **12.6.2 [ANTIGRAVITY]** Connect the backend to the Airflow API.
- [x] **12.6.3 [ANTIGRAVITY]** Implement retraining-job persistence.
- [x] **12.6.4 [ANTIGRAVITY]** Implement retraining status synchronization.
- [x] **12.6.5 [ANTIGRAVITY]** Implement the retraining quality gate.
- [x] **12.6.6 [ANTIGRAVITY]** Require the candidate model to meet the documented evaluation criteria.
- [x] **12.6.7 [ANTIGRAVITY]** Require an explicit approval decision before promotion.
- [x] **12.6.8 [ANTIGRAVITY]** Implement controlled model promotion.
- [x] **12.6.9 [ANTIGRAVITY]** Record promotion decisions in the audit log.
- [x] **12.6.10 [ANTIGRAVITY]** Add retraining service tests.
- [x] **12.6.11 [BOTH]** Trigger retraining through the application.
- [x] **12.6.12 [BOTH]** Verify the corresponding Airflow run.
- [x] **12.6.13 [BOTH]** Verify the new MLflow experiment.
- [x] **12.6.14 [BOTH]** Verify the quality-gate result.
- [x] **12.6.15 [BOTH]** Verify that a failed candidate cannot replace the active model.
- [x] **12.6.16 [BOTH]** Verify that an approved candidate can be promoted through the controlled action.

**Verification:** Drift can be detected and reported, but no model can be deployed solely because a drift alert occurred.

---

# PHASE 13 — Security, reliability and operational safeguards

**Objective:** Protect service boundaries and prevent unsafe or misleading operations.

- [x] **13.1 [ANTIGRAVITY]** Review all environment-variable usage.
- [x] **13.2 [ANTIGRAVITY]** Remove hardcoded credentials from source code.
- [x] **13.3 [ANTIGRAVITY]** Confirm secrets are absent from frontend public variables.
- [x] **13.4 [ANTIGRAVITY]** Validate image uploads by file content and decoding.
- [x] **13.5 [ANTIGRAVITY]** Enforce upload size limits.
- [x] **13.6 [ANTIGRAVITY]** Restrict accepted image formats.
- [x] **13.7 [ANTIGRAVITY]** Implement safe temporary-file cleanup.
- [x] **13.8 [ANTIGRAVITY]** Restrict destructive model operations to controlled application actions.
- [x] **13.9 [ANTIGRAVITY]** Protect retraining and promotion operations against unintended requests.
- [x] **13.10 [ANTIGRAVITY]** Add audit records for model promotion.
- [x] **13.11 [ANTIGRAVITY]** Add audit records for retraining requests.
- [x] **13.12 [ANTIGRAVITY]** Restrict direct exposure of Airflow administrative interfaces.
- [x] **13.13 [ANTIGRAVITY]** Restrict direct exposure of MLflow administrative interfaces.
- [x] **13.14 [ANTIGRAVITY]** Configure safe API error responses.
- [x] **13.15 [ANTIGRAVITY]** Add database connection-failure handling.
- [x] **13.16 [ANTIGRAVITY]** Add dependency and container version checks.
- [x] **13.17 [ANTIGRAVITY]** Document the local development security model.
- [x] **13.18 [BOTH]** Test invalid file uploads.
- [x] **13.19 [BOTH]** Test oversized file uploads.
- [x] **13.20 [BOTH]** Test unavailable database behavior.
- [x] **13.21 [BOTH]** Test unavailable MLflow and Airflow behavior.

**Verification:** Invalid inputs and unavailable dependencies produce controlled errors, not application crashes or misleading success states.

---

# PHASE 14 — Docker and local environment integration

**Objective:** Make the full application reproducible through Docker Compose.

## 14.1 Containerize individual applications

- [x] **14.1.1 [ANTIGRAVITY]** Create the backend Dockerfile.
- [x] **14.1.2 [ANTIGRAVITY]** Build the backend image.
- [x] **14.1.3 [BOTH]** Verify the backend container starts.
- [x] **14.1.4 [ANTIGRAVITY]** Create the frontend Dockerfile.
- [x] **14.1.5 [ANTIGRAVITY]** Build the frontend image.
- [x] **14.1.6 [BOTH]** Verify the frontend container starts.
- [x] **14.1.7 [ANTIGRAVITY]** Define the PostgreSQL container configuration.
- [x] **14.1.8 [ANTIGRAVITY]** Define the MLflow container configuration.
- [x] **14.1.9 [ANTIGRAVITY]** Define the Airflow container configuration.
- [x] **14.1.10 [ANTIGRAVITY]** Define the Prometheus container configuration.
- [x] **14.1.11 [ANTIGRAVITY]** Define the Grafana container configuration.

## 14.2 Build Docker Compose

- [x] **14.2.1 [ANTIGRAVITY]** Create the root `docker-compose.yml`.
- [x] **14.2.2 [ANTIGRAVITY]** Add the PostgreSQL service.
- [x] **14.2.3 [ANTIGRAVITY]** Add the backend service.
- [x] **14.2.4 [ANTIGRAVITY]** Add the frontend service.
- [x] **14.2.5 [ANTIGRAVITY]** Add the MLflow service.
- [x] **14.2.6 [ANTIGRAVITY]** Add the Airflow services required by the selected release and executor.
- [x] **14.2.7 [ANTIGRAVITY]** Add the Prometheus service.
- [x] **14.2.8 [ANTIGRAVITY]** Add the Grafana service.
- [x] **14.2.9 [ANTIGRAVITY]** Configure the Docker network.
- [x] **14.2.10 [ANTIGRAVITY]** Configure persistent PostgreSQL storage.
- [x] **14.2.11 [ANTIGRAVITY]** Configure persistent MLflow artifact storage.
- [x] **14.2.12 [ANTIGRAVITY]** Configure persistent Airflow logs.
- [x] **14.2.13 [ANTIGRAVITY]** Configure persistent Grafana data.
- [x] **14.2.14 [ANTIGRAVITY]** Configure persistent Prometheus data.
- [x] **14.2.15 [ANTIGRAVITY]** Configure health checks.
- [x] **14.2.16 [ANTIGRAVITY]** Configure service dependencies.
- [x] **14.2.17 [ANTIGRAVITY]** Configure service-specific environment variables.
- [x] **14.2.18 [ANTIGRAVITY]** Verify internal service URLs use Docker service names.
- [x] **14.2.19 [ANTIGRAVITY]** Document host-accessible ports.
- [x] **14.2.20 [ANTIGRAVITY]** Add separate Compose profiles if needed for resource-efficient development.
- [x] **14.2.21 [BOTH]** Start PostgreSQL through Compose.
- [x] **14.2.22 [BOTH]** Verify PostgreSQL health.
- [x] **14.2.23 [BOTH]** Start the backend through Compose.
- [x] **14.2.24 [BOTH]** Verify backend health.
- [x] **14.2.25 [BOTH]** Start the frontend through Compose.
- [x] **14.2.26 [BOTH]** Verify frontend-to-backend communication.
- [x] **14.2.27 [BOTH]** Start MLflow through Compose.
- [x] **14.2.28 [BOTH]** Verify MLflow connectivity.
- [x] **14.2.29 [BOTH]** Start Airflow through Compose.
- [x] **14.2.30 [BOTH]** Verify Airflow connectivity.
- [x] **14.2.31 [BOTH]** Start Prometheus through Compose.
- [x] **14.2.32 [BOTH]** Verify Prometheus scraping.
- [x] **14.2.33 [BOTH]** Start Grafana through Compose.
- [x] **14.2.34 [BOTH]** Verify Grafana dashboards.

## 14.3 Verify full local startup

- [x] **14.3.1 [BOTH]** Stop the complete Compose environment.
- [x] **14.3.2 [BOTH]** Start the required full local environment using the documented command.
- [x] **14.3.3 [BOTH]** Verify every required service becomes healthy.
- [x] **14.3.4 [BOTH]** Verify persistent database records survive a restart.
- [x] **14.3.5 [BOTH]** Verify MLflow artifacts survive a restart.
- [x] **14.3.6 [BOTH]** Verify Airflow execution history survives a restart.
- [x] **14.3.7 [ANTIGRAVITY]** Document startup, shutdown and reset commands.
- [x] **14.3.8 [BOTH]** Verify the project can be started using only the documented instructions.

**Verification:** The complete local demonstration runs through Docker Compose without undocumented manual service setup.

---

# PHASE 15 — Automated testing and GitHub Actions

**Objective:** Validate code quality and integration automatically.

## 15.1 Backend tests

- [x] **15.1.1 [ANTIGRAVITY]** Configure pytest.
- [x] **15.1.2 [ANTIGRAVITY]** Add backend unit tests.
- [x] **15.1.3 [ANTIGRAVITY]** Add database integration tests.
- [x] **15.1.4 [ANTIGRAVITY]** Add API endpoint tests.
- [x] **15.1.5 [ANTIGRAVITY]** Add invalid-upload tests.
- [x] **15.1.6 [ANTIGRAVITY]** Add model-loading tests.
- [x] **15.1.7 [ANTIGRAVITY]** Add inference-response tests.
- [x] **15.1.8 [ANTIGRAVITY]** Run the backend test suite.

## 15.2 ML and pipeline tests

- [x] **15.2.1 [ANTIGRAVITY]** Add preprocessing tests.
- [x] **15.2.2 [ANTIGRAVITY]** Add model architecture tests.
- [x] **15.2.3 [ANTIGRAVITY]** Add evaluation metric tests.
- [x] **15.2.4 [ANTIGRAVITY]** Add threshold evaluation tests.
- [x] **15.2.5 [ANTIGRAVITY]** Add Grad-CAM tests.
- [x] **15.2.6 [ANTIGRAVITY]** Add drift detection tests.
- [x] **15.2.7 [ANTIGRAVITY]** Add quality-gate tests.
- [x] **15.2.8 [ANTIGRAVITY]** Add Airflow DAG validation tests.
- [x] **15.2.9 [ANTIGRAVITY]** Run the ML and pipeline test suites.

## 15.3 Frontend tests

- [x] **15.3.1 [ANTIGRAVITY]** Configure the frontend test environment.
- [x] **15.3.2 [ANTIGRAVITY]** Add shared component tests.
- [x] **15.3.3 [ANTIGRAVITY]** Add API client tests.
- [x] **15.3.4 [ANTIGRAVITY]** Add inspection workflow tests.
- [x] **15.3.5 [ANTIGRAVITY]** Add dashboard empty-state tests.
- [x] **15.3.6 [ANTIGRAVITY]** Add dashboard error-state tests.
- [x] **15.3.7 [ANTIGRAVITY]** Run frontend tests.

## 15.4 End-to-end tests

- [x] **15.4.1 [ANTIGRAVITY]** Configure Playwright.
- [x] **15.4.2 [ANTIGRAVITY]** Add application navigation tests.
- [x] **15.4.3 [ANTIGRAVITY]** Add image-upload tests.
- [x] **15.4.4 [ANTIGRAVITY]** Add prediction-result tests.
- [x] **15.4.5 [ANTIGRAVITY]** Add Grad-CAM display tests.
- [x] **15.4.6 [ANTIGRAVITY]** Add model-registry page tests.
- [x] **15.4.7 [ANTIGRAVITY]** Add retraining workflow interface tests.
- [x] **15.4.8 [BOTH]** Run end-to-end tests against the local environment.

## 15.5 GitHub Actions

- [x] **15.5.1 [MANUAL]** Confirm GitHub repository access.
- [x] **15.5.2 [ANTIGRAVITY]** Create the GitHub Actions workflow directory.
- [x] **15.5.3 [ANTIGRAVITY]** Create the backend CI workflow.
- [x] **15.5.4 [ANTIGRAVITY]** Add Python dependency installation to CI.
- [x] **15.5.5 [ANTIGRAVITY]** Add Ruff linting to CI.
- [x] **15.5.6 [ANTIGRAVITY]** Add backend tests to CI.
- [x] **15.5.7 [ANTIGRAVITY]** Add ML unit tests to CI.
- [x] **15.5.8 [ANTIGRAVITY]** Add Airflow DAG validation to CI.
- [x] **15.5.9 [ANTIGRAVITY]** Create the frontend CI workflow.
- [x] **15.5.10 [ANTIGRAVITY]** Add frontend linting to CI.
- [x] **15.5.11 [ANTIGRAVITY]** Add TypeScript checks to CI.
- [ ] **15.5.12 [ANTIGRAVITY]** Add frontend tests to CI.
- [ ] **15.5.13 [ANTIGRAVITY]** Add frontend production build validation to CI.
- [ ] **15.5.14 [ANTIGRAVITY]** Add Docker image build validation to CI.
- [ ] **15.5.15 [ANTIGRAVITY]** Configure workflow triggers for pushes and pull requests.
- [ ] **15.5.16 [BOTH]** Push the CI workflow to GitHub.
- [ ] **15.5.17 [BOTH]** Verify a successful GitHub Actions run.
- [ ] **15.5.18 [BOTH]** Introduce a controlled test failure and verify CI detects it.
- [ ] **15.5.19 [BOTH]** Restore the test and verify CI passes again.

**Verification:** GitHub Actions runs automated checks and builds. It is not considered a deployment pipeline unless a separate deployment workflow is deliberately implemented.

---

# PHASE 16 — Documentation and project evidence

**Objective:** Make the project understandable, reproducible and demonstrable.

## 16.1 Technical documentation

- [x] **16.1.1 [ANTIGRAVITY]** Complete the root README.
- [x] **16.1.2 [ANTIGRAVITY]** Document project prerequisites.
- [x] **16.1.3 [ANTIGRAVITY]** Document local environment setup.
- [x] **16.1.4 [ANTIGRAVITY]** Document Docker Compose commands.
- [x] **16.1.5 [ANTIGRAVITY]** Document the frontend startup procedure.
- [x] **16.1.6 [ANTIGRAVITY]** Document the backend startup procedure.
- [x] **16.1.7 [ANTIGRAVITY]** Document dataset acquisition.
- [x] **16.1.8 [ANTIGRAVITY]** Document DVC usage.
- [x] **16.1.9 [ANTIGRAVITY]** Document model training.
- [x] **16.1.10 [ANTIGRAVITY]** Document MLflow usage.
- [x] **16.1.11 [ANTIGRAVITY]** Document Airflow DAG execution.
- [x] **16.1.12 [ANTIGRAVITY]** Document API endpoints.
- [x] **16.1.13 [ANTIGRAVITY]** Document monitoring setup.
- [x] **16.1.14 [ANTIGRAVITY]** Document drift detection.
- [x] **16.1.15 [ANTIGRAVITY]** Document retraining and model promotion.
- [x] **16.1.16 [ANTIGRAVITY]** Document known limitations.

## 16.2 Model and dataset documentation

- [x] **16.2.1 [ANTIGRAVITY]** Complete the Data Card.
- [x] **16.2.2 [ANTIGRAVITY]** Document dataset origin and licence.
- [x] **16.2.3 [ANTIGRAVITY]** Document dataset class distribution.
- [x] **16.2.4 [ANTIGRAVITY]** Document preprocessing and split methodology.
- [x] **16.2.5 [ANTIGRAVITY]** Complete the Model Card.
- [x] **16.2.6 [ANTIGRAVITY]** Document the selected model architecture.
- [x] **16.2.7 [ANTIGRAVITY]** Document the classification threshold.
- [x] **16.2.8 [ANTIGRAVITY]** Document the evaluation results.
- [x] **16.2.9 [ANTIGRAVITY]** Document intended use and limitations.
- [x] **16.2.10 [ANTIGRAVITY]** Complete the architecture document.
- [x] **16.2.11 [ANTIGRAVITY]** Complete the performance report.
- [x] **16.2.12 [ANTIGRAVITY]** Document measured inference latency.
- [x] **16.2.13 [ANTIGRAVITY]** Document measured P95 latency.
- [x] **16.2.14 [ANTIGRAVITY]** Document measured throughput.
- [x] **16.2.15 [ANTIGRAVITY]** Document measured error rate.
- [x] **16.2.16 [ANTIGRAVITY]** Document drift test results.
- [x] **16.2.17 [ANTIGRAVITY]** Document quality-gate pass and fail results.

## 16.3 Evidence collection

- [x] **16.3.1 [MANUAL]** Capture the dataset validation report.
- [x] **16.3.2 [MANUAL]** Capture the EDA results.
- [x] **16.3.3 [MANUAL]** Capture the three-model comparison.
- [x] **16.3.4 [MANUAL]** Capture MLflow experiment records.
- [x] **16.3.5 [MANUAL]** Capture the registered model version.
- [x] **16.3.6 [MANUAL]** Capture the successful Airflow training DAG.
- [x] **16.3.7 [MANUAL]** Capture the successful retraining DAG.
- [x] **16.3.8 [MANUAL]** Capture real inspection results.
- [x] **16.3.9 [MANUAL]** Capture the three Grad-CAM visualization modes.
- [x] **16.3.10 [MANUAL]** Capture Prometheus metrics.
- [x] **16.3.11 [MANUAL]** Capture Grafana dashboards.
- [x] **16.3.12 [MANUAL]** Capture drift test results.
- [x] **16.3.13 [MANUAL]** Capture quality-gate rejection evidence.
- [x] **16.3.14 [MANUAL]** Capture GitHub Actions successful workflow runs.
- [x] **16.3.15 [ANTIGRAVITY]** Organize the evidence directory.
- [x] **16.3.16 [ANTIGRAVITY]** Add evidence descriptions to the project documentation.

**Verification:** Documentation and evidence reflect actual executed experiments and service behavior.

---

# PHASE 17 — Optional AWS extension

**Objective:** Demonstrate selected cloud capabilities without making AWS a local-project dependency.

**This phase is optional. Complete the local project first.**

## 17.1 AWS account and cost preparation

- [ ] **17.1.1 [MANUAL]** Create or confirm AWS account access.
- [ ] **17.1.2 [MANUAL]** Enable multi-factor authentication.
- [ ] **17.1.3 [MANUAL]** Configure an IAM identity with least-privilege permissions.
- [ ] **17.1.4 [MANUAL]** Configure AWS CLI.
- [ ] **17.1.5 [MANUAL]** Verify AWS CLI authentication.
- [ ] **17.1.6 [BOTH]** Review expected AWS costs before provisioning resources.
- [ ] **17.1.7 [BOTH]** Define a resource cleanup checklist.

## 17.2 S3 and DVC remote

- [ ] **17.2.1 [MANUAL]** Create the S3 bucket.
- [ ] **17.2.2 [MANUAL]** Configure bucket access permissions.
- [ ] **17.2.3 [ANTIGRAVITY]** Configure the DVC S3 remote.
- [ ] **17.2.4 [BOTH]** Push a dataset version to S3.
- [ ] **17.2.5 [BOTH]** Pull the dataset version from S3.
- [ ] **17.2.6 [BOTH]** Verify the retrieved data matches the original version.

## 17.3 Optional SageMaker demonstration

- [ ] **17.3.1 [BOTH]** Review SageMaker instance and storage costs.
- [ ] **17.3.2 [MANUAL]** Configure the required AWS permissions.
- [ ] **17.3.3 [ANTIGRAVITY]** Prepare the selected training script for managed execution.
- [ ] **17.3.4 [ANTIGRAVITY]** Configure the SageMaker training job.
- [ ] **17.3.5 [BOTH]** Run a controlled training demonstration.
- [ ] **17.3.6 [BOTH]** Verify the training output.
- [ ] **17.3.7 [ANTIGRAVITY]** Document the local-versus-managed training workflow.

## 17.4 Optional application deployment

- [ ] **17.4.1 [BOTH]** Decide whether full application deployment is within the project scope.
- [ ] **17.4.2 [MANUAL]** Review ECR, ECS Fargate and RDS costs.
- [ ] **17.4.3 [ANTIGRAVITY]** Prepare the required deployment configuration.
- [ ] **17.4.4 [MANUAL]** Create the ECR repository.
- [ ] **17.4.5 [BOTH]** Push the application image to ECR.
- [ ] **17.4.6 [MANUAL]** Provision the selected application infrastructure.
- [ ] **17.4.7 [ANTIGRAVITY]** Configure CloudWatch logging.
- [ ] **17.4.8 [BOTH]** Verify the deployed health endpoint.
- [ ] **17.4.9 [BOTH]** Run a controlled cloud inspection.
- [ ] **17.4.10 [MANUAL]** Stop or delete resources that are no longer needed.

**Important:** ECS and RDS do not automatically deploy Airflow, MLflow, Prometheus or Grafana. A full cloud deployment requires a separate hosting and security plan for those services. Do not imply that the local Compose stack has been deployed merely because the backend runs in ECS.

---

# PHASE 18 — Final quality assurance and launch readiness

**Objective:** Validate the complete product and prevent premature public launch.

## 18.1 Functional acceptance

- [ ] **18.1.1 [BOTH]** Verify the root route redirects to Overview.
- [ ] **18.1.2 [BOTH]** Verify all nine dashboard routes load.
- [ ] **18.1.3 [BOTH]** Verify all navigation links.
- [ ] **18.1.4 [BOTH]** Verify the Inspection upload workflow.
- [ ] **18.1.5 [BOTH]** Verify the OK classification workflow.
- [ ] **18.1.6 [BOTH]** Verify the DEFECTIVE classification workflow.
- [ ] **18.1.7 [BOTH]** Verify all Grad-CAM modes.
- [ ] **18.1.8 [BOTH]** Verify experiment information.
- [ ] **18.1.9 [BOTH]** Verify dataset information.
- [ ] **18.1.10 [BOTH]** Verify pipeline information.
- [ ] **18.1.11 [BOTH]** Verify model registry information.
- [ ] **18.1.12 [BOTH]** Verify operational monitoring.
- [ ] **18.1.13 [BOTH]** Verify ML monitoring.
- [ ] **18.1.14 [BOTH]** Verify drift reporting.
- [ ] **18.1.15 [BOTH]** Verify retraining workflow.
- [ ] **18.1.16 [BOTH]** Verify model quality-gate rejection.
- [ ] **18.1.17 [BOTH]** Verify controlled model promotion.
- [ ] **18.1.18 [BOTH]** Verify prediction persistence.

## 18.2 Data authenticity

- [ ] **18.2.1 [BOTH]** Verify every dashboard metric has a real data source.
- [ ] **18.2.2 [BOTH]** Verify missing values are not represented as zero without justification.
- [ ] **18.2.3 [BOTH]** Verify empty states appear when no records exist.
- [ ] **18.2.4 [BOTH]** Verify no fake activity feed is displayed.
- [ ] **18.2.5 [BOTH]** Verify no fabricated model metrics are displayed.
- [ ] **18.2.6 [BOTH]** Verify no fabricated pipeline records are displayed.
- [ ] **18.2.7 [BOTH]** Verify no fabricated customer or usage counters are displayed.

## 18.3 Design quality

- [ ] **18.3.1 [BOTH]** Verify the approved blue-grey palette is used consistently.
- [ ] **18.3.2 [BOTH]** Verify the typography system is consistent.
- [ ] **18.3.3 [BOTH]** Verify buttons use rectangular styling.
- [ ] **18.3.4 [BOTH]** Verify cards use restrained borders and shadows.
- [ ] **18.3.5 [BOTH]** Verify Lucide icons are used consistently.
- [ ] **18.3.6 [BOTH]** Verify the Inspection Workbench is the defining visual component.
- [ ] **18.3.7 [BOTH]** Verify no purple or rainbow gradients exist.
- [ ] **18.3.8 [BOTH]** Verify no pill-shaped buttons exist.
- [ ] **18.3.9 [BOTH]** Verify no emoji icons are used in the application.
- [ ] **18.3.10 [BOTH]** Verify no fake testimonials or reviews exist.
- [ ] **18.3.11 [BOTH]** Verify no fake customer counters exist.
- [ ] **18.3.12 [BOTH]** Verify no AI-generated stock-looking imagery is used.
- [ ] **18.3.13 [BOTH]** Verify no cursor-following animations exist.
- [ ] **18.3.14 [BOTH]** Verify no excessive scroll-triggered animations exist.
- [ ] **18.3.15 [BOTH]** Verify all motion respects reduced-motion preferences.
- [ ] **18.3.16 [BOTH]** Verify website copy does not use em dashes.

## 18.4 Responsive and accessibility testing

- [ ] **18.4.1 [BOTH]** Test Overview at desktop width.
- [ ] **18.4.2 [BOTH]** Test Inspection at desktop width.
- [ ] **18.4.3 [BOTH]** Test all remaining pages at desktop width.
- [ ] **18.4.4 [BOTH]** Test all nine pages at tablet width.
- [ ] **18.4.5 [BOTH]** Test all nine pages at mobile width.
- [ ] **18.4.6 [BOTH]** Verify there is no unintended horizontal page overflow.
- [ ] **18.4.7 [BOTH]** Verify inspection images remain usable on mobile.
- [ ] **18.4.8 [BOTH]** Test keyboard navigation.
- [ ] **18.4.9 [BOTH]** Test visible focus indicators.
- [ ] **18.4.10 [BOTH]** Test form labels and validation messages.
- [ ] **18.4.11 [BOTH]** Test dialog keyboard behavior.
- [ ] **18.4.12 [BOTH]** Test accessible status announcements.
- [ ] **18.4.13 [BOTH]** Test text contrast.
- [ ] **18.4.14 [BOTH]** Test reduced-motion settings.
- [ ] **18.4.15 [BOTH]** Complete the WCAG 2.2 AA review.

## 18.5 Performance and reliability

- [ ] **18.5.1 [ANTIGRAVITY]** Measure frontend production build output.
- [ ] **18.5.2 [BOTH]** Measure backend inference latency.
- [ ] **18.5.3 [BOTH]** Measure P95 inference latency under a documented test load.
- [ ] **18.5.4 [BOTH]** Measure API throughput.
- [ ] **18.5.5 [BOTH]** Measure API error rate.
- [ ] **18.5.6 [BOTH]** Test repeated image uploads.
- [ ] **18.5.7 [BOTH]** Test service restart behavior.
- [ ] **18.5.8 [BOTH]** Test database persistence after restart.
- [ ] **18.5.9 [BOTH]** Test recovery from a failed pipeline.
- [ ] **18.5.10 [BOTH]** Verify monitoring captures the measured behavior.
- [ ] **18.5.11 [ANTIGRAVITY]** Add the measured results to the performance report.

## 18.6 Launch preparation

These tasks are mandatory before a **public launch**. They are not prerequisites for a local-only academic demonstration.

- [ ] **18.6.1 [MANUAL]** Purchase or configure the intended custom domain.
- [ ] **18.6.2 [MANUAL]** Connect the custom domain to the selected hosting environment.
- [ ] **18.6.3 [ANTIGRAVITY]** Add the VisionQC favicon.
- [ ] **18.6.4 [ANTIGRAVITY]** Verify product branding across all routes.
- [ ] **18.6.5 [ANTIGRAVITY]** Remove any "Made with AI" labels or badges.
- [ ] **18.6.6 [ANTIGRAVITY]** Create the Privacy Policy page.
- [ ] **18.6.7 [ANTIGRAVITY]** Create the Terms and Conditions page.
- [ ] **18.6.8 [ANTIGRAVITY]** Add legal-page links to the footer.
- [ ] **18.6.9 [BOTH]** Review legal content against actual data collection and usage.
- [ ] **18.6.10 [BOTH]** Verify every public navigation link.
- [ ] **18.6.11 [BOTH]** Verify every primary action.
- [ ] **18.6.12 [BOTH]** Verify all public routes.
- [ ] **18.6.13 [BOTH]** Verify all images and assets load correctly.
- [ ] **18.6.14 [BOTH]** Verify no placeholder content remains.
- [ ] **18.6.15 [BOTH]** Complete the public-launch checklist.

**Launch rule:** Public launch is blocked if any mandatory launch, legal, security, accessibility or functional acceptance item remains incomplete.

---

# PHASE 19 — Final demonstration and handover

**Objective:** Prepare a complete, reproducible demonstration of the MLOps lifecycle.

- [ ] **19.1 [ANTIGRAVITY]** Prepare the final README demonstration section.
- [ ] **19.2 [ANTIGRAVITY]** Prepare the final architecture diagram.
- [ ] **19.3 [ANTIGRAVITY]** Prepare the five-minute demonstration sequence.
- [ ] **19.4 [BOTH]** Start the complete local environment.
- [ ] **19.5 [BOTH]** Demonstrate the Overview page.
- [ ] **19.6 [BOTH]** Demonstrate an actual image inspection.
- [ ] **19.7 [BOTH]** Demonstrate the OK result.
- [ ] **19.8 [BOTH]** Demonstrate the DEFECTIVE result.
- [ ] **19.9 [BOTH]** Demonstrate Grad-CAM original, heatmap and overlay.
- [ ] **19.10 [BOTH]** Demonstrate the three-model comparison in MLflow.
- [ ] **19.11 [BOTH]** Demonstrate the Airflow training DAG.
- [ ] **19.12 [BOTH]** Demonstrate the model registry.
- [ ] **19.13 [BOTH]** Demonstrate Prometheus and Grafana.
- [ ] **19.14 [BOTH]** Demonstrate a drift simulation.
- [ ] **19.15 [BOTH]** Demonstrate a retraining request.
- [ ] **19.16 [BOTH]** Demonstrate the quality gate rejecting an unsuitable candidate.
- [ ] **19.17 [BOTH]** Demonstrate controlled model promotion.
- [ ] **19.18 [MANUAL]** Record the final demonstration.
- [ ] **19.19 [ANTIGRAVITY]** Add the final demonstration link or file reference to the README.
- [ ] **19.20 [MANUAL]** Push the final verified project state to GitHub.
- [ ] **19.21 [BOTH]** Confirm the repository has no uncommitted required changes.
- [ ] **19.22 [BOTH]** Confirm all project documentation is present.

---

# Final completion checklist

The project is considered complete only after these conditions are verified.

## Machine learning

- [ ] Dataset validated and versioned with DVC.
- [ ] Preprocessing is reproducible.
- [ ] Custom CNN trained and evaluated.
- [ ] ResNet18 trained and evaluated.
- [ ] EfficientNet-B0 trained and evaluated.
- [ ] Model comparison report generated.
- [ ] Defect recall and false-negative rate evaluated.
- [ ] Classification threshold documented.
- [ ] Grad-CAM works for supported architectures.

## MLOps

- [ ] MLflow tracks experiments and artifacts.
- [ ] Model registry stores model versions.
- [ ] Airflow training DAG works.
- [ ] Airflow retraining DAG works.
- [ ] Quality gate blocks unsuitable models.
- [ ] Model promotion is controlled.
- [ ] DVC can reproduce the dataset version.

## Application

- [ ] FastAPI serves the selected model.
- [ ] PostgreSQL stores application records.
- [ ] All required API endpoints work.
- [ ] All nine dashboard pages work.
- [ ] Inspection Workbench works end to end.
- [ ] Dashboard values come from real services.
- [ ] Empty, loading and error states work.

## Monitoring

- [ ] Prometheus collects operational metrics.
- [ ] Grafana dashboards work.
- [ ] Image drift detection works.
- [ ] Drift history is recorded.
- [ ] Drift is not misrepresented as model-performance degradation.
- [ ] Retraining can be requested and tracked.

## Engineering

- [ ] Docker Compose starts the local environment.
- [ ] GitHub Actions passes.
- [ ] Backend tests pass.
- [ ] ML tests pass.
- [ ] Airflow DAG tests pass.
- [ ] Frontend tests pass.
- [ ] End-to-end tests pass.
- [ ] Responsive and accessibility checks pass.
- [ ] Documentation is complete.
- [ ] Demonstration evidence is captured.

## Public launch

- [ ] Custom domain connected.
- [ ] Favicon added.
- [ ] Privacy Policy published.
- [ ] Terms and Conditions published.
- [ ] No "Made with AI" label remains.
- [ ] Final launch QA passes.

---

# Recommended repository structure

```text
VisionQC/
│
├── frontend/
│   ├── app/
│   │   ├── overview/
│   │   ├── inspection/
│   │   ├── experiments/
│   │   ├── datasets/
│   │   ├── pipelines/
│   │   ├── model-registry/
│   │   ├── monitoring/
│   │   ├── retraining/
│   │   ├── documentation/
│   │   ├── privacy/
│   │   └── terms/
│   ├── components/
│   │   ├── layout/
│   │   ├── navigation/
│   │   ├── shared/
│   │   ├── inspection/
│   │   ├── charts/
│   │   ├── tables/
│   │   ├── model/
│   │   └── monitoring/
│   ├── hooks/
│   ├── lib/
│   ├── services/
│   ├── types/
│   ├── public/
│   └── styles/
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
│   ├── features/
│   ├── models/
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
│   ├── model_quality/
│   └── e2e/
│
├── docs/
│   ├── architecture.md
│   ├── data-card.md
│   ├── model-card.md
│   ├── performance-report.md
│   └── evidence/
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
├── design.md
├── techstack.md
└── todo.md
```

---

# How to work with Antigravity

## Give Antigravity one bounded task at a time

For each task:

1. Open the VisionQC repository in Antigravity.
2. Give it the exact task number and task description.
3. Ask it to inspect the existing code before editing.
4. Ask it to implement only that task.
5. Ask it to list every file created or modified.
6. Ask it to run the relevant tests.
7. Ask it to report the actual command output.
8. Review the changes.
9. Run any manual verification assigned to you.
10. Mark the task complete only after verification.

## Reusable Antigravity prompt

```text
We are implementing VisionQC.

Read these project documents before making changes:
- prd.md
- design.md
- techstack.md
- todo.md

Current task: [TASK NUMBER AND EXACT DESCRIPTION]

Rules:
1. Work only on this task.
2. Do not implement future tasks.
3. Inspect existing code before editing.
4. Preserve all approved architecture decisions.
5. Do not invent data, metrics, API responses or successful test results.
6. Follow the VisionQC design system.
7. Do not introduce unapproved dependencies.
8. Do not modify unrelated files.
9. Add or update tests for the implementation.
10. Run the relevant tests and report their actual output.

At the end, report:
- What was implemented.
- Files created.
- Files modified.
- Commands executed.
- Test results.
- Any unresolved issue.
- Manual action required from me.
- Whether the current task is ready for verification.

Do not mark the task complete. I will verify it.
```

## What you should do manually

You should personally handle:

- Installing Git, Python, Node.js, Docker Desktop and Antigravity.
- Creating or accessing GitHub.
- Downloading the original dataset.
- Starting Docker and checking local services.
- Entering credentials and configuring secrets.
- Opening MLflow, Airflow, Prometheus and Grafana.
- Running actual training and inspecting results.
- Reviewing model predictions and Grad-CAM output.
- Testing the complete application.
- Creating AWS resources if you choose the optional cloud extension.
- Capturing screenshots and demonstration evidence.
- Committing and pushing verified work.

Antigravity should handle the implementation and tests, not pretend to perform these manual operations.

---

**Final implementation principle:** Build the ML workflow first, make it reproducible, expose it through FastAPI, and then connect the dashboard. The interface should show a working system, not simulate one.
