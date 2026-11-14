"""
VisionQC Multi-Model Trainer Extension
Provides unified training and evaluation functions for:
- Custom CNN (baseline)
- ResNet18 (candidate 1)
- EfficientNet-B0 (candidate 2)
"""

import copy
import json
import time
from pathlib import Path
from typing import Dict, Any, Tuple
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import yaml

from ml.data.dataset import get_dataloaders
from ml.models.custom_cnn import CustomCNN
from ml.models.resnet18 import VisionQCResNet18
from ml.models.efficientnet_b0 import VisionQCEfficientNetB0
from ml.evaluation.evaluate import compute_classification_metrics, plot_evaluation_charts

CONFIG_PATH = Path("configs/training_config.yaml")

def set_seed(seed: int = 42):
    torch.manual_seed(seed)
    np.random.seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def evaluate_loader(
    model: nn.Module,
    loader: DataLoader,
    device: torch.device,
    threshold: float = 0.5
) -> Tuple[float, Dict[str, Any], np.ndarray, np.ndarray, float]:
    model.eval()
    criterion = nn.BCEWithLogitsLoss()
    total_loss = 0.0
    all_targets = []
    all_probs = []

    start_time = time.perf_counter()
    with torch.no_grad():
        for inputs, targets in loader:
            inputs = inputs.to(device)
            targets = targets.float().to(device)
            logits = model(inputs)
            loss = criterion(logits, targets)
            total_loss += loss.item() * inputs.size(0)

            probs = torch.sigmoid(logits)
            all_probs.extend(probs.cpu().numpy())
            all_targets.extend(targets.cpu().numpy())
    elapsed = time.perf_counter() - start_time
    avg_latency_ms = (elapsed / len(loader.dataset)) * 1000.0

    avg_loss = total_loss / len(loader.dataset)
    y_true = np.array(all_targets)
    y_prob = np.array(all_probs)
    metrics = compute_classification_metrics(y_true, y_prob, threshold=threshold)
    metrics["latency_ms_per_image"] = round(avg_latency_ms, 2)
    return avg_loss, metrics, y_true, y_prob, avg_latency_ms

def train_model(model_type: str = "resnet18") -> Dict[str, Any]:
    with open(CONFIG_PATH, "r") as f:
        full_cfg = yaml.safe_load(f)

    cfg = full_cfg[model_type]
    set_seed(full_cfg["general"].get("seed", 42))
    device = torch.device(full_cfg["general"].get("device", "cpu"))

    dataloaders = get_dataloaders(batch_size=cfg["batch_size"], num_workers=full_cfg["general"].get("num_workers", 0))

    if model_type == "resnet18":
        model = VisionQCResNet18(pretrained=cfg.get("pretrained", True), freeze_backbone=cfg.get("freeze_backbone", False))
        display_name = "ResNet18"
    elif model_type == "efficientnet_b0":
        model = VisionQCEfficientNetB0(pretrained=cfg.get("pretrained", True), freeze_backbone=cfg.get("freeze_backbone", False))
        display_name = "EfficientNet-B0"
    elif model_type == "custom_cnn":
        model = CustomCNN()
        display_name = "Custom CNN"
    else:
        raise ValueError(f"Unknown model_type: {model_type}")

    model = model.to(device)
    criterion = nn.BCEWithLogitsLoss()

    optimizer = torch.optim.Adam(
        filter(lambda p: p.requires_grad, model.parameters()),
        lr=cfg["learning_rate"],
        weight_decay=cfg["weight_decay"]
    )

    best_loss = float("inf")
    best_weights = None
    history = []

    print(f"\n--- Training {display_name} on {device} ({cfg['epochs']} epochs) ---")

    for epoch in range(1, cfg["epochs"] + 1):
        model.train()
        running_loss = 0.0

        for inputs, targets in dataloaders["train"]:
            inputs = inputs.to(device)
            targets = targets.float().to(device)

            optimizer.zero_grad()
            logits = model(inputs)
            loss = criterion(logits, targets)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * inputs.size(0)

        train_loss = running_loss / len(dataloaders["train"].dataset)
        val_loss, val_metrics, _, _, _ = evaluate_loader(model, dataloaders["val"], device)

        history.append({
            "epoch": epoch,
            "train_loss": round(train_loss, 4),
            "val_loss": round(val_loss, 4),
            "val_accuracy": val_metrics["accuracy"],
            "val_defect_recall": val_metrics["recall_defect"],
            "val_f1": val_metrics["f1_score"]
        })

        print(f"Epoch {epoch:02d}/{cfg['epochs']:02d} | Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f} | Val Acc: {val_metrics['accuracy']:.4f} | Defect Recall: {val_metrics['recall_defect']:.4f}")

        if val_loss < best_loss:
            best_loss = val_loss
            best_weights = copy.deepcopy(model.state_dict())

    if best_weights is not None:
        model.load_state_dict(best_weights)

    test_loss, test_metrics, y_test, y_probs, latency_ms = evaluate_loader(model, dataloaders["test"], device)
    print(f"\n--- Final Test Set Evaluation ({display_name}) ---")
    print(f"Accuracy: {test_metrics['accuracy']:.4f} | Defect Recall: {test_metrics['recall_defect']:.4f} | F1: {test_metrics['f1_score']:.4f} | ROC-AUC: {test_metrics['roc_auc']:.4f} | Latency: {latency_ms:.2f}ms/img")

    eval_out_dir = Path("docs/evaluation")
    plot_evaluation_charts(y_test, y_probs, eval_out_dir, display_name)

    save_path = Path(cfg["save_path"])
    save_path.parent.mkdir(parents=True, exist_ok=True)
    torch.save({
        "model_architecture": display_name,
        "state_dict": model.state_dict(),
        "config": cfg,
        "test_metrics": test_metrics
    }, save_path)
    print(f"Saved {display_name} checkpoint to: {save_path}")

    # Save metrics JSON
    metrics_path = eval_out_dir / f"{model_type}_test_metrics.json"
    with open(metrics_path, "w") as f:
        json.dump(test_metrics, f, indent=2)

    return {
        "model_type": model_type,
        "display_name": display_name,
        "history": history,
        "test_metrics": test_metrics,
        "checkpoint_path": str(save_path)
    }

if __name__ == "__main__":
    import sys
    m_type = sys.argv[1] if len(sys.argv) > 1 else "resnet18"
    train_model(m_type)
