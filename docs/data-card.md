# Data Card — Real-Life Industrial Dataset of Casting Product

**Project:** VisionQC — Automated Manufacturing Defect Inspection & MLOps Platform  
**Version:** 1.0  
**Date:** 14 November 2026  
**Status:** Validated  

---

## 1. Dataset Overview
- **Name:** Real-Life Industrial Dataset of Casting Product
- **Domain:** Manufacturing Quality Control (Submersible pump impeller casting)
- **Problem Type:** Binary Computer Vision Classification (`OK` vs. `DEFECTIVE`)
- **Original Source:** Pilot industrial inspection line / Kaggle Open Dataset
- **License:** CC BY-SA 4.0

## 2. Dataset Composition & Validation Statistics
- **Total Samples:** 1,300 images
- **Resolution:** 512 × 512 pixels
- **Color Mode:** Grayscale (single channel representation)
- **File Format:** JPEG (`.jpeg`)
- **Corrupted Images:** 0
- **Duplicate Images Detected:** 0

### Class Breakdown
| Class | Sample Count | Percentage | Description |
|---|---|---|---|
| **OK** | 519 | 39.92% | Acceptable impeller with no critical surface or structural defects |
| **DEFECTIVE** | 781 | 60.08% | Casting showing holes, cracks, deformations, or irregularities |
| **Total** | **1,300** | **100.0%** | Baseline inspection distribution |

## 3. Data Integrity & Preprocessing Contract
- All raw images are preserved in `ml/data/raw/{ok,defective}`.
- Data splits (Train / Validation / Test) will be generated reproducibly with fixed random seeds prior to augmentation.
- Augmentation is strictly restricted to training splits to avoid data leakage.
