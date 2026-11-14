# VisionQC 5-Minute Demonstration Script

This document details the live demonstration flow for the **VisionQC** platform, suitable for presentation to reviewers, stakeholders, and academic evaluators.

---

## ⏱ Demo Outline (Total Time: ~5 Minutes)

| Time | Section | Key Talking Points & Action |
|------|---------|-----------------------------|
| **00:00 - 00:45** | **1. Overview & Architecture** | Introduce VisionQC as an industrial quality inspection and MLOps platform for manufacturing casting defects. Point out the stack: PyTorch, FastAPI, Next.js, PostgreSQL, MLflow, Prometheus/Grafana, and Docker. |
| **00:45 - 01:45** | **2. Inspection Workbench (Live Demo)** | Open frontend at `http://localhost:3000/inspection`. Upload a casting image (`def_front` sample). Show immediate inference: classification (`DEFECTIVE` / `OK`), confidence score, and latency. |
| **01:45 - 02:30** | **3. Explainability with Grad-CAM** | Toggle Grad-CAM view modes: Overlay, Side-by-side, Heatmap only, Raw input. Show defect attribution focusing on the casting crack/pinhole defects. |
| **02:30 - 03:15** | **4. MLflow Model Governance** | Show MLflow experiment comparison across Custom CNN, ResNet-18, and EfficientNet-B0. Highlight why EfficientNet-B0 was promoted (F1-score > 0.98, low latency). |
| **03:15 - 03:50** | **5. Prometheus & Grafana Monitoring** | Show live Grafana dashboard (`http://localhost:3001`): inspection request throughput, error rate (0%), and P95 latency (< 35ms). Show Prometheus scrape targets. |
| **03:50 - 04:30** | **6. Data Drift Simulation & Retraining** | Navigate to `/drift` page. Show Kolmogorov-Smirnov test tracking feature distribution shifts. Trigger the automated retraining workflow and show quality gate rejection/approval logic. |
| **04:30 - 05:00** | **7. Summary & Q&A** | Highlight end-to-end automation, reproducible DVC pipelines, CI/CD validation in GitHub Actions, and production readiness. |

---

## 📋 Pre-Flight Checklist

1. [ ] Start Docker Compose stack: `docker compose up -d`
2. [ ] Confirm Backend is healthy: `curl http://localhost:8000/health`
3. [ ] Confirm Frontend is reachable: `http://localhost:3000`
4. [ ] Prepare sample casting images in an easily accessible folder:
   - Sample OK image: `ml/casting_data/test/ok_front/cast_ok_0_1.jpeg`
   - Sample Defective image: `ml/casting_data/test/def_front/cast_def_0_0.jpeg`
