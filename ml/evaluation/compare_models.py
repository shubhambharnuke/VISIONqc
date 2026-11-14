"""
VisionQC Model Comparison & Threshold Optimization Module
- Standardizes side-by-side evaluation across all 3 trained models:
  1. Custom CNN Baseline
  2. ResNet18 Candidate
  3. EfficientNet-B0 Candidate
- Evaluates Defect Recall, Precision, Accuracy, F1, ROC-AUC, FNR, and Inference Latency
- Performs Threshold Sweep on validation set
- Generates model comparison charts and writes model_comparison_report.json
"""

import json
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import torch
import yaml

from ml.data.dataset import get_dataloaders
from ml.models.custom_cnn import CustomCNN
from ml.models.resnet18 import VisionQCResNet18
from ml.models.efficientnet_b0 import VisionQCEfficientNetB0
from ml.evaluation.evaluate import compute_classification_metrics

EVAL_DIR = Path("docs/evaluation")
EVAL_DIR.mkdir(parents=True, exist_ok=True)

MODELS = {
    "Custom CNN": {
        "class": CustomCNN,
        "checkpoint": "ml/models/saved/custom_cnn_baseline.pth",
        "params": 1438465
    },
    "ResNet18": {
        "class": lambda: VisionQCResNet18(pretrained=False),
        "checkpoint": "ml/models/saved/resnet18_candidate.pth",
        "params": 11177025
    },
    "EfficientNet-B0": {
        "class": lambda: VisionQCEfficientNetB0(pretrained=False),
        "checkpoint": "ml/models/saved/efficientnet_b0_candidate.pth",
        "params": 4008829
    }
}

def load_checkpoint_model(model_info):
    model = model_info["class"]()
    chk = torch.load(model_info["checkpoint"], map_location="cpu", weights_only=False)
    model.load_state_dict(chk["state_dict"])
    model.eval()
    return model

def run_comparison():
    dataloaders = get_dataloaders(batch_size=32)
    device = torch.device("cpu")
    comparison_results = {}

    for name, info in MODELS.items():
        print(f"Evaluating {name} on test set...")
        model = load_checkpoint_model(info)
        
        all_targets = []
        all_probs = []
        import time
        start_time = time.perf_counter()
        with torch.no_grad():
            for inputs, targets in dataloaders["test"]:
                logits = model(inputs)
                probs = torch.sigmoid(logits)
                all_probs.extend(probs.numpy())
                all_targets.extend(targets.numpy())
        elapsed = time.perf_counter() - start_time
        latency_ms = (elapsed / len(dataloaders["test"].dataset)) * 1000.0

        y_true = np.array(all_targets)
        y_prob = np.array(all_probs)

        # Baseline threshold 0.5 metrics
        metrics = compute_classification_metrics(y_true, y_prob, threshold=0.5)
        metrics["latency_ms_per_image"] = round(latency_ms, 2)
        metrics["param_count"] = info["params"]

        comparison_results[name] = metrics

    # 1. Comparison Bar Chart
    models = list(comparison_results.keys())
    recalls = [comparison_results[m]["recall_defect"] * 100 for m in models]
    accuracies = [comparison_results[m]["accuracy"] * 100 for m in models]
    f1s = [comparison_results[m]["f1_score"] * 100 for m in models]
    latencies = [comparison_results[m]["latency_ms_per_image"] for m in models]

    x = np.arange(len(models))
    width = 0.25

    fig, ax1 = plt.subplots(figsize=(8, 5))
    rects1 = ax1.bar(x - width, recalls, width, label='Defect Recall (%)', color='#34765B')
    rects2 = ax1.bar(x, accuracies, width, label='Accuracy (%)', color='#476985')
    rects3 = ax1.bar(x + width, f1s, width, label='F1-Score (%)', color='#7892A8')

    ax1.set_ylabel('Percentage (%)', fontweight='bold')
    ax1.set_title('VisionQC — Model Architecture Comparison', fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(models, fontweight='bold')
    ax1.set_ylim(80, 105)
    ax1.legend(loc='lower left')
    ax1.grid(True, linestyle=':', alpha=0.5)

    for r in rects1 + rects2 + rects3:
        h = r.get_height()
        ax1.annotate(f'{h:.1f}%', xy=(r.get_x() + r.get_width() / 2, h),
                     xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    fig.savefig(EVAL_DIR / "model_comparison_barchart.png", dpi=150)
    plt.close()

    # Save summary report
    with open(EVAL_DIR / "model_comparison_report.json", "w") as f:
        json.dump(comparison_results, f, indent=2)

    print("\n--- Model Comparison Summary ---")
    print(json.dumps(comparison_results, indent=2))
    return comparison_results

def run_threshold_optimization(selected_model_name: str = "EfficientNet-B0"):
    dataloaders = get_dataloaders(batch_size=32)
    model = load_checkpoint_model(MODELS[selected_model_name])

    all_targets = []
    all_probs = []
    with torch.no_grad():
        for inputs, targets in dataloaders["val"]:
            logits = model(inputs)
            probs = torch.sigmoid(logits)
            all_probs.extend(probs.numpy())
            all_targets.extend(targets.numpy())

    y_true = np.array(all_targets)
    y_prob = np.array(all_probs)

    thresholds = np.linspace(0.1, 0.9, 17)
    sweep_results = []
    best_threshold = 0.5
    best_f1 = 0.0

    for t in thresholds:
        m = compute_classification_metrics(y_true, y_prob, threshold=t)
        sweep_results.append({
            "threshold": round(float(t), 2),
            "recall_defect": m["recall_defect"],
            "precision": m["precision"],
            "f1_score": m["f1_score"],
            "fnr": m["false_negative_rate"]
        })
        if m["f1_score"] > best_f1:
            best_f1 = m["f1_score"]
            best_threshold = round(float(t), 2)

    with open(EVAL_DIR / "threshold_optimization_results.json", "w") as f:
        json.dump({
            "model": selected_model_name,
            "optimal_threshold": best_threshold,
            "sweep": sweep_results
        }, f, indent=2)

    print(f"\n--- Threshold Optimization for {selected_model_name} ---")
    print(f"Optimal Threshold (Max F1 on Validation): {best_threshold}")
    return best_threshold

if __name__ == "__main__":
    run_comparison()
    run_threshold_optimization("EfficientNet-B0")
