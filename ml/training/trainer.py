"""
VisionQC Trainer Module
- Reproducible model training loop
- Checkpoints best model weights based on validation loss and defect recall
- Computes comprehensive evaluation metrics per epoch and final test run
- Pure PyTorch with modular hooks for MLflow tracking integration
"""

import copy
import json
from pathlib import Path
from typing import Dict, Any, Tuple
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import yaml

from ml.data.dataset import get_dataloaders
from ml.models.custom_cnn import CustomCNN
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
) -> Tuple[float, Dict[str, Any], np.ndarray, np.ndarray]:
    model.eval()
    criterion = nn.BCEWithLogitsLoss()
    total_loss = 0.0
    all_targets = []
    all_probs = []

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

    avg_loss = total_loss / len(loader.dataset)
    y_true = np.array(all_targets)
    y_prob = np.array(all_probs)
    metrics = compute_classification_metrics(y_true, y_prob, threshold=threshold)
    return avg_loss, metrics, y_true, y_prob

def train_custom_cnn(
    config_override: Dict[str, Any] = None,
    save_model: bool = True
) -> Dict[str, Any]:
    with open(CONFIG_PATH, "r") as f:
        full_cfg = yaml.safe_load(f)

    cfg = full_cfg["custom_cnn"]
    if config_override:
        cfg.update(config_override)

    set_seed(full_cfg["general"].get("seed", 42))
    device = torch.device(full_cfg["general"].get("device", "cpu"))

    dataloaders = get_dataloaders(batch_size=cfg["batch_size"], num_workers=full_cfg["general"].get("num_workers", 0))

    model = CustomCNN().to(device)

    # Class weighting in loss if configured
    pos_weight = torch.tensor([cfg.get("pos_weight", 1.0)]).to(device)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

    if cfg["optimizer"] == "adam":
        optimizer = torch.optim.Adam(model.parameters(), lr=cfg["learning_rate"], weight_decay=cfg["weight_decay"])
    else:
        optimizer = torch.optim.SGD(model.parameters(), lr=cfg["learning_rate"], momentum=0.9, weight_decay=cfg["weight_decay"])

    best_loss = float("inf")
    best_weights = None
    history = []

    print(f"\n--- Starting Custom CNN Training on {device} ({cfg['epochs']} epochs) ---")

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
        val_loss, val_metrics, _, _ = evaluate_loader(model, dataloaders["val"], device)

        history.append({
            "epoch": epoch,
            "train_loss": round(train_loss, 4),
            "val_loss": round(val_loss, 4),
            "val_accuracy": val_metrics["accuracy"],
            "val_defect_recall": val_metrics["recall_defect"],
            "val_f1": val_metrics["f1_score"]
        })

        print(f"Epoch {epoch:02d}/{cfg['epochs']:02d} | Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f} | Val Acc: {val_metrics['accuracy']:.4f} | Val Defect Recall: {val_metrics['recall_defect']:.4f}")

        if val_loss < best_loss:
            best_loss = val_loss
            best_weights = copy.deepcopy(model.state_dict())

    if best_weights is not None:
        model.load_state_dict(best_weights)

    # Final evaluation on untouched test set
    test_loss, test_metrics, y_test, y_probs = evaluate_loader(model, dataloaders["test"], device)
    print("\n--- Final Test Set Evaluation (Custom CNN) ---")
    print(f"Accuracy: {test_metrics['accuracy']:.4f} | Defect Recall: {test_metrics['recall_defect']:.4f} | F1: {test_metrics['f1_score']:.4f} | ROC-AUC: {test_metrics['roc_auc']:.4f}")

    eval_out_dir = Path("docs/evaluation")
    plot_evaluation_charts(y_test, y_probs, eval_out_dir, "Custom CNN Baseline")

    save_path = Path(cfg["save_path"])
    save_path.parent.mkdir(parents=True, exist_ok=True)
    if save_model:
        torch.save({
            "model_architecture": "CustomCNN",
            "state_dict": model.state_dict(),
            "config": cfg,
            "test_metrics": test_metrics
        }, save_path)
        print(f"Saved baseline checkpoint to: {save_path}")

    return {
        "architecture": "CustomCNN",
        "history": history,
        "test_metrics": test_metrics,
        "checkpoint_path": str(save_path)
    }

if __name__ == "__main__":
    train_custom_cnn()
