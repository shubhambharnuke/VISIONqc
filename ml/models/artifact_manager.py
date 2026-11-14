"""
VisionQC Model Artifact Manager
Manages standard packaging and integrity verification of trained model artifacts:
- Model weights (.pth)
- Architecture metadata
- Preprocessing contract
- Classification threshold
- Evaluation metrics
- Dataset DVC reference version
"""

import hashlib
import json
from pathlib import Path
from typing import Dict, Any
import torch

ARTIFACT_DIR = Path("ml/models/saved")

def compute_sha256(filepath: Path) -> str:
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

def package_model_artifact(
    model_name: str,
    checkpoint_path: str | Path,
    metadata_out_path: str | Path = None
) -> Dict[str, Any]:
    checkpoint_path = Path(checkpoint_path)
    if not checkpoint_path.exists():
        raise FileNotFoundError(f"Checkpoint not found at: {checkpoint_path}")

    chk = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    file_hash = compute_sha256(checkpoint_path)
    file_size_mb = round(checkpoint_path.stat().st_size / (1024 * 1024), 2)

    artifact_manifest = {
        "model_name": model_name,
        "checkpoint_file": checkpoint_path.name,
        "checkpoint_path": str(checkpoint_path),
        "file_size_mb": file_size_mb,
        "sha256": file_hash,
        "dataset_version_tag": "dataset-v1.0",
        "dvc_tracked": True,
        "preprocessing": {
            "target_size": [224, 224],
            "channels": 3,
            "normalization_mean": [0.485, 0.456, 0.406],
            "normalization_std": [0.229, 0.224, 0.225]
        },
        "operating_threshold": 0.50,
        "metrics": chk.get("test_metrics", {})
    }

    if metadata_out_path is None:
        metadata_out_path = checkpoint_path.with_suffix(".json")

    metadata_out_path = Path(metadata_out_path)
    with open(metadata_out_path, "w") as f:
        json.dump(artifact_manifest, f, indent=2)

    print(f"Packaged artifact manifest: {metadata_out_path}")
    return artifact_manifest

def verify_artifact_integrity(manifest_path: str | Path) -> bool:
    manifest_path = Path(manifest_path)
    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    chk_path = Path(manifest["checkpoint_path"])
    if not chk_path.exists():
        print(f"Error: Model file {chk_path} is missing.")
        return False

    current_hash = compute_sha256(chk_path)
    if current_hash != manifest["sha256"]:
        print("Error: SHA256 checksum mismatch! Artifact may be corrupted.")
        return False

    try:
        chk = torch.load(chk_path, map_location="cpu", weights_only=False)
        if "state_dict" not in chk:
            print("Error: Missing 'state_dict' in checkpoint.")
            return False
    except Exception as e:
        print(f"Error loading checkpoint: {e}")
        return False

    print(f"Artifact integrity verified: {manifest['model_name']} ({chk_path.name})")
    return True

if __name__ == "__main__":
    for name, pth in [
        ("Custom CNN", ARTIFACT_DIR / "custom_cnn_baseline.pth"),
        ("ResNet18", ARTIFACT_DIR / "resnet18_candidate.pth"),
        ("EfficientNet-B0", ARTIFACT_DIR / "efficientnet_b0_candidate.pth")
    ]:
        if pth.exists():
            manifest = package_model_artifact(name, pth)
            assert verify_artifact_integrity(pth.with_suffix(".json"))
