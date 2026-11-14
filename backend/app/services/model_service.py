"""
VisionQC Model Serving Manager
- Loads the active champion model (EfficientNet-B0) into memory at startup
- Caches the weights (no per-request reloads)
- Exposes inference and Grad-CAM generation methods
"""

import time
import uuid
from pathlib import Path
from typing import Dict, Any, Tuple
import numpy as np
from PIL import Image
import torch
import yaml

from ml.models.efficientnet_b0 import VisionQCEfficientNetB0
from ml.models.resnet18 import VisionQCResNet18
from ml.models.custom_cnn import CustomCNN
from ml.preprocessing.preprocess import get_transforms
from ml.explainability.gradcam import generate_gradcam_explanation

CONFIG_PATH = Path("configs/model_config.yaml")

class ModelServingService:
    def __init__(self, config_path: Path = CONFIG_PATH):
        self.config_path = config_path
        self.model = None
        self.model_info = {}
        self.transform = get_transforms(is_train=False)
        self.load_active_model()

    def load_active_model(self):
        with open(self.config_path, "r") as f:
            cfg = yaml.safe_load(f)["active_model"]

        name = cfg["name"]
        chk_path = Path(cfg["checkpoint_path"])

        if not chk_path.exists():
            print(f"Notice: Checkpoint {chk_path} not found on disk (CI/testing environment). Initializing unweighted architecture.")
            chk_path = None

        print(f"Loading active model '{name}' from {chk_path}...")
        if "EfficientNet" in name:
            model = VisionQCEfficientNetB0(pretrained=False)
        elif "ResNet" in name:
            model = VisionQCResNet18(pretrained=False)
        else:
            model = CustomCNN()

        if chk_path and chk_path.exists():
            checkpoint = torch.load(chk_path, map_location="cpu", weights_only=False)
            model.load_state_dict(checkpoint["state_dict"])
        model.eval()

        self.model = model
        self.model_info = {
            "model_name": name,
            "architecture": cfg.get("architecture", name),
            "version": cfg.get("version", "v1.0"),
            "threshold": float(cfg.get("threshold", 0.50)),
            "checkpoint_path": str(chk_path),
            "device": "cpu"
        }
        print(f"Active model '{name}' loaded successfully into memory.")

    def predict(
        self,
        image_bytes: bytes,
        filename: str = "upload.jpg",
        generate_gradcam: bool = True
    ) -> Dict[str, Any]:
        import io
        pred_id = f"insp_{uuid.uuid4().hex[:12]}"

        # Validate and open image
        try:
            img = Image.open(io.BytesIO(image_bytes))
            img.verify()
            img = Image.open(io.BytesIO(image_bytes)) # Reopen after verify
        except Exception as e:
            raise ValueError(f"Invalid image content: {e}")

        # Preprocess
        tensor = self.transform(img).unsqueeze(0) # [1, 3, 224, 224]

        # Inference with latency measurement
        start = time.perf_counter()
        with torch.no_grad():
            logits = self.model(tensor)
            prob = float(torch.sigmoid(logits)[0].item())
        elapsed_ms = (time.perf_counter() - start) * 1000.0

        threshold = self.model_info["threshold"]
        is_defective = prob >= threshold
        pred_class = "DEFECTIVE" if is_defective else "OK"
        decision = "REJECT" if is_defective else "ACCEPT"

        gradcam_paths = None
        if generate_gradcam:
            out_dir = Path("static/gradcam") / pred_id
            out_dir.mkdir(parents=True, exist_ok=True)
            temp_img_path = out_dir / filename
            img.save(temp_img_path)

            cam_result = generate_gradcam_explanation(
                image_path=temp_img_path,
                model=self.model,
                model_name=self.model_info["model_name"],
                output_dir=out_dir
            )
            gradcam_paths = {
                "original": f"/static/gradcam/{pred_id}/{filename}",
                "heatmap": f"/static/gradcam/{pred_id}/{temp_img_path.stem}_heatmap.jpg",
                "overlay": f"/static/gradcam/{pred_id}/{temp_img_path.stem}_overlay.jpg"
            }

        return {
            "prediction_id": pred_id,
            "predicted_class": pred_class,
            "defect_probability": round(prob, 4),
            "decision": decision,
            "threshold_applied": threshold,
            "model_name": self.model_info["model_name"],
            "model_version": self.model_info["version"],
            "inference_latency_ms": round(elapsed_ms, 2),
            "has_gradcam": generate_gradcam,
            "gradcam_urls": gradcam_paths
        }

model_service = ModelServingService()
