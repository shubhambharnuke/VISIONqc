# VisionQC Performance Report — Three-Model Comparison & Evaluation

**Project:** VisionQC — Automated Manufacturing Defect Inspection & MLOps Platform  
**Document:** `docs/performance-report.md`  
**Date:** 14 November 2026  
**Status:** Multi-Model Comparison Completed  

---

## 1. Overview of Evaluated Architectures
To satisfy PRD §5.3 requirements, three computer vision architectures were trained on the identical 70/15/15 stratified casting dataset and evaluated on the untouched test split (195 images: 78 OK, 117 DEFECTIVE):

1. **Custom CNN (Baseline):** 4-stage convolutional neural network trained from scratch (1.44M parameters).
2. **ResNet18 (Candidate 1):** Pretrained residual architecture fine-tuned with custom binary classification head (11.18M parameters).
3. **EfficientNet-B0 (Candidate 2):** Pretrained compound-scaled parameter-efficient architecture (4.01M parameters).

---

## 2. Test Set Evaluation Comparison (195 Samples)

| Evaluation Metric | Custom CNN (Baseline) | ResNet18 (Candidate 1) | EfficientNet-B0 (Candidate 2) | Winning Architecture |
|---|---|---|---|---|
| **Defect Recall** *(Priority)* | 94.87% (111 / 117) | 99.15% (116 / 117) | **100.00%** (117 / 117) | **EfficientNet-B0** |
| **Defect Precision** | 88.10% | **100.00%** | **100.00%** | **Tie (ResNet18 / EfficientNet)** |
| **Accuracy** | 89.23% | 99.49% | **100.00%** | **EfficientNet-B0** |
| **F1-Score** | 91.36% | 99.57% | **100.00%** | **EfficientNet-B0** |
| **ROC-AUC** | 0.9712 | **1.0000** | **1.0000** | **Tie (ResNet18 / EfficientNet)** |
| **False Negative Rate (FNR)** | 5.13% (6 missed) | 0.85% (1 missed) | **0.00%** (0 missed) | **EfficientNet-B0** |
| **Inference Latency (CPU)** | **22.46 ms/image** | 27.48 ms/image | 24.86 ms/image | **Custom CNN** |
| **Trainable Parameters** | **1,438,465** | 11,177,025 | 4,008,829 | **Custom CNN** |

---

## 3. Confusion Matrix Breakdown

### Custom CNN
- **True Negatives (OK):** 63 / 78
- **False Positives (False Defect Alarm):** 15 / 78
- **False Negatives (Missed Defects):** 6 / 117
- **True Positives (Detected Defects):** 111 / 117

### ResNet18
- **True Negatives (OK):** 78 / 78 (100% specificity)
- **False Positives:** 0 / 78
- **False Negatives (Missed Defects):** 1 / 117
- **True Positives (Detected Defects):** 116 / 117

### EfficientNet-B0
- **True Negatives (OK):** 78 / 78 (100% specificity)
- **False Positives:** 0 / 78
- **False Negatives (Missed Defects):** 0 / 117 (Zero defects escaped inspection)
- **True Positives (Detected Defects):** 117 / 117

---

## 4. Production Model Selection Rationale
**Selected Champion Model:** `EfficientNet-B0`

### Justification:
1. **Critical Defect Recall:** In manufacturing quality control, undetected defective impellers lead to pump failures. EfficientNet-B0 attained **100% recall** with zero false negatives on the test set.
2. **False Positive Elimination:** Both candidate models eliminated false rejections, preserving acceptable casting parts from unwarranted scrap.
3. **Parameter & Latency Efficiency:** EfficientNet-B0 has **64% fewer parameters** than ResNet18 (4.01M vs 11.18M) and executes inference in just **24.86 ms/image**, well within the PRD latency budget (< 2,000 ms).
4. **Operating Threshold:** Recorded as `0.50` in `configs/model_config.yaml`.
