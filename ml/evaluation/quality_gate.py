"""
VisionQC Model Quality Gate Module
Applies strict evaluation criteria before allowing a candidate model
to be registered or promoted to Production:
- Minimum Defect Recall >= 0.95 (Crucial to prevent defective impellers escaping)
- Minimum Accuracy >= 0.90
- Minimum F1-Score >= 0.90
- Maximum False Negative Rate <= 0.05
- Maximum Latency <= 100.0 ms
"""

import json
from pathlib import Path
from typing import Dict, Any, Tuple
import yaml

CONFIG_PATH = Path("configs/model_config.yaml")

def check_quality_gate(metrics: Dict[str, Any], config_path: Path = CONFIG_PATH) -> Tuple[bool, Dict[str, Any]]:
    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)
    
    thresholds = cfg.get("quality_gate", {
        "min_defect_recall": 0.95,
        "min_accuracy": 0.90,
        "min_f1_score": 0.90,
        "max_false_negative_rate": 0.05,
        "max_latency_ms": 100.0
    })

    reasons = []
    passed = True

    # Check recall
    recall = metrics.get("recall_defect", 0.0)
    if recall < thresholds["min_defect_recall"]:
        passed = False
        reasons.append(f"Defect Recall ({recall:.4f}) below threshold ({thresholds['min_defect_recall']})")

    # Check accuracy
    acc = metrics.get("accuracy", 0.0)
    if acc < thresholds["min_accuracy"]:
        passed = False
        reasons.append(f"Accuracy ({acc:.4f}) below threshold ({thresholds['min_accuracy']})")

    # Check F1
    f1 = metrics.get("f1_score", 0.0)
    if f1 < thresholds["min_f1_score"]:
        passed = False
        reasons.append(f"F1-Score ({f1:.4f}) below threshold ({thresholds['min_f1_score']})")

    # Check FNR
    fnr = metrics.get("false_negative_rate", 1.0)
    if fnr > thresholds["max_false_negative_rate"]:
        passed = False
        reasons.append(f"False Negative Rate ({fnr:.4f}) exceeds threshold ({thresholds['max_false_negative_rate']})")

    # Check latency
    lat = metrics.get("latency_ms_per_image", metrics.get("latency_ms", 0.0))
    if lat > thresholds["max_latency_ms"]:
        passed = False
        reasons.append(f"Inference Latency ({lat:.2f}ms) exceeds threshold ({thresholds['max_latency_ms']}ms)")

    decision = {
        "passed": passed,
        "metrics_evaluated": {
            "defect_recall": recall,
            "accuracy": acc,
            "f1_score": f1,
            "false_negative_rate": fnr,
            "latency_ms": lat
        },
        "thresholds": thresholds,
        "reasons": reasons
    }

    status_str = "PASSED (APPROVED FOR REGISTRATION)" if passed else "FAILED (REJECTED FROM PROMOTION)"
    print(f"\n--- Quality Gate Decision: {status_str} ---")
    for r in reasons:
        print(f" [!] {r}")

    return passed, decision

if __name__ == "__main__":
    # Test with good metrics (EfficientNet-B0)
    good_metrics = {"accuracy": 1.0, "recall_defect": 1.0, "f1_score": 1.0, "false_negative_rate": 0.0, "latency_ms": 24.86}
    p, _ = check_quality_gate(good_metrics)
    assert p is True, "Good model should pass quality gate"

    # Test with substandard model
    bad_metrics = {"accuracy": 0.85, "recall_defect": 0.80, "f1_score": 0.82, "false_negative_rate": 0.20, "latency_ms": 25.0}
    p, _ = check_quality_gate(bad_metrics)
    assert p is False, "Substandard model must fail quality gate"
    print("Quality gate unit validation succeeded.")
