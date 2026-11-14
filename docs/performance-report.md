# VisionQC Performance Report — Baseline Evaluation

**Project:** VisionQC — Automated Manufacturing Defect Inspection & MLOps Platform  
**Document:** `docs/performance-report.md`  
**Date:** 14 November 2026  
**Status:** Baseline Completed  

---

## 1. Baseline Model: Custom CNN Architecture
A 4-stage convolutional neural network trained from scratch with binary classification output:
- **Optimizer:** Adam (LR: 0.001, Weight Decay: 0.0001)
- **Loss:** BCEWithLogitsLoss
- **Training Epochs:** 10
- **Total Trainable Parameters:** 1,438,465
- **Input Dimension:** 3 × 224 × 224 (grayscale repeated channels)

### Baseline Evaluation Results (Untouched Test Set — 195 samples)
| Metric | Measured Baseline Score |
|---|---|
| **Accuracy** | **89.23%** (174 / 195) |
| **Defect Recall** | **94.87%** (111 / 117 defects identified) |
| **Defect Precision** | **88.09%** |
| **F1-Score** | **91.36%** |
| **ROC-AUC** | **0.9712** |
| **False Negative Rate (FNR)** | **5.13%** (6 missed defects out of 117) |

### Baseline Confusion Matrix
- **True Negatives (OK correctly identified):** 63 / 78 (80.77% specificity)
- **False Positives (OK falsely flagged as defective):** 15 / 78
- **False Negatives (Defective missed):** 6 / 117
- **True Positives (Defective identified):** 111 / 117

### Baseline Artifacts
- Checkpoint: `ml/models/saved/custom_cnn_baseline.pth`
- Visualizations:
  - Confusion Matrix: `docs/evaluation/custom_cnn_baseline_confusion_matrix.png`
  - ROC Curve: `docs/evaluation/custom_cnn_baseline_roc_curve.png`
