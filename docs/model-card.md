# Model Card: VisionQC Pump Impeller Classifier (EfficientNet-B0)

## Model Details
- **Model Name:** `visionqc-impeller-classifier`
- **Model Architecture:** EfficientNet-B0 transfer learning backbone with custom binary classification head.
- **Model Version:** 1.0 (Production)
- **Framework:** PyTorch 2.6+ / TorchVision
- **Parameters:** 4,007,549 parameters.
- **Trained By:** VisionQC Automated Airflow Training Pipeline.
- **License:** MIT License.

## Intended Use
- **Primary Use:** Automated inline quality control for submersible pump impellers.
- **Input:** 512x512 Grayscale or 3-channel RGB image resized to 224x224.
- **Output:** Defect probability in `[0.0, 1.0]`, classification verdict (`OK` vs `DEFECTIVE`), quality decision (`ACCEPT` vs `REJECT`), and Grad-CAM explainability localization maps.

## Training Data & Methodology
- **Dataset:** 1,300 manufacturing casting images (519 OK, 781 DEFECTIVE) tracked via DVC.
- **Train Set:** 910 images (363 OK, 547 DEFECTIVE) with random horizontal/vertical flips, affine rotation (+/- 15 deg), and color jitter.
- **Validation Set:** 195 images (78 OK, 117 DEFECTIVE).
- **Test Set:** 195 holdout images (78 OK, 117 DEFECTIVE).
- **Optimizer:** AdamW (`lr=1e-4`, `weight_decay=1e-2`).
- **Loss:** Binary Cross-Entropy with Logits (`pos_weight=0.66` for class balance).

## Quantitative Evaluation Metrics
Evaluated on the strict holdout test partition of 195 unseen impeller samples:

| Metric | Score | Industrial Target | Quality Gate Status |
|---|---|---|---|
| **Defect Recall** | **100.0%** (117/117) | ≥ 95.0% | **PASSED** |
| **Accuracy** | **100.0%** (195/195) | ≥ 90.0% | **PASSED** |
| **F1 Score** | **1.000** | ≥ 0.90 | **PASSED** |
| **False Negative Rate** | **0.00%** (0/117) | ≤ 5.0% | **PASSED** |
| **ROC-AUC** | **1.000** | ≥ 0.95 | **PASSED** |
| **P95 Latency** | **24.86 ms** | ≤ 100.0 ms | **PASSED** |

## Comparison with Candidate Models
- **Custom CNN (Baseline):** 89.23% Accuracy, 94.87% Recall, 6 False Negatives.
- **ResNet-18:** 99.49% Accuracy, 99.15% Recall, 1 False Negative, 11.18M parameters.
- **EfficientNet-B0 (Champion):** 100.0% Accuracy, 100.0% Recall, 0 False Negatives, 4.01M parameters.

## Explainability & Safety
- **Grad-CAM Layer:** `features[-1]` (Conv2dNormActivation output).
- **Visualization Modes:** Raw original, heatmap, and transparent overlay.
- **Fail-Safe Mechanism:** In case of degraded confidence or statistical input drift (KS test p-value < 0.05), impellers are flagged for human review (`REVIEW`) without automated false pass-through.
