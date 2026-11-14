"""
VisionQC Grad-CAM Explainability Module
Generates visual explanations for CNN predictions by calculating gradients
of the score for class c with respect to feature activation map of the final convolutional layer.
Supports:
1. Custom CNN -> target layer: features[9] (final conv in Block 4)
2. ResNet18 -> target layer: backbone.layer4[-1]
3. EfficientNet-B0 -> target layer: backbone.features[-1]

Provides 3 modes:
- Original Image
- Heatmap (Jet color map)
- Overlay (Superimposed Heatmap on Original)
"""

from pathlib import Path
from typing import Dict, Tuple, Any
import cv2
import numpy as np
from PIL import Image
import torch
import torch.nn as nn
import torch.nn.functional as F

from ml.preprocessing.preprocess import get_transforms

class GradCAM:
    def __init__(self, model: nn.Module, target_layer: nn.Module):
        self.model = model
        self.target_layer = target_layer
        self.gradients = None
        self.activations = None
        
        self.hook_handles = []
        self._register_hooks()

    def _register_hooks(self):
        def forward_hook(module, input, output):
            self.activations = output.detach().clone()

        def backward_hook(module, grad_in, grad_out):
            self.gradients = grad_out[0].detach().clone()

        self.hook_handles.append(self.target_layer.register_forward_hook(forward_hook))
        self.hook_handles.append(self.target_layer.register_full_backward_hook(backward_hook))

    def generate_heatmap(self, input_tensor: torch.Tensor, class_idx: int = 1) -> np.ndarray:
        self.model.eval()
        self.model.zero_grad()

        # Forward pass
        logits = self.model(input_tensor) # Shape: [batch_size]
        score = logits[0] if logits.dim() == 1 else logits[0, 0]

        # Target class gradient (score for DEFECTIVE class)
        score.backward(retain_graph=True)

        # Global average pooling of gradients: weights alpha_k
        pooled_gradients = torch.mean(self.gradients, dim=[0, 2, 3]) # [channels]

        # Weight the channels of the feature activations
        activations = self.activations[0] # [channels, H, W]
        for i in range(activations.size(0)):
            activations[i, :, :] *= pooled_gradients[i]

        # Channel-wise mean of weighted activations + ReLU
        heatmap = torch.mean(activations, dim=0).squeeze().cpu().numpy()
        heatmap = np.maximum(heatmap, 0) # ReLU

        # Normalize heatmap to [0, 1]
        max_val = np.max(heatmap)
        if max_val > 0:
            heatmap /= max_val
        else:
            heatmap = np.zeros_like(heatmap)

        return heatmap

    def remove_hooks(self):
        for h in self.hook_handles:
            h.remove()

def get_target_layer(model_name: str, model: nn.Module) -> nn.Module:
    name_clean = model_name.lower().replace("-", "").replace("_", "").replace(" ", "")
    if "customcnn" in name_clean:
        return model.features[9] # Last conv in Block 4
    elif "resnet18" in name_clean:
        return model.backbone.layer4[-1] # Last Bottleneck/BasicBlock in layer4
    elif "efficientnet" in name_clean:
        return model.backbone.features[-1] # Last Conv2dNormActivation block
    else:
        raise ValueError(f"Unsupported architecture for Grad-CAM: {model_name}")

def generate_gradcam_explanation(
    image_path: str | Path,
    model: nn.Module,
    model_name: str,
    output_dir: str | Path = None
) -> Dict[str, Any]:
    image_path = Path(image_path)
    orig_bgr = cv2.imread(str(image_path))
    h, w = orig_bgr.shape[:2]

    # Preprocess image for model input
    transform = get_transforms(is_train=False)
    with Image.open(image_path) as img:
        input_tensor = transform(img).unsqueeze(0)

    # Attach Grad-CAM
    target_layer = get_target_layer(model_name, model)
    cam = GradCAM(model, target_layer)

    with torch.enable_grad():
        heatmap_raw = cam.generate_heatmap(input_tensor)

    cam.remove_hooks()

    # Resize heatmap to original image dimensions
    heatmap_resized = cv2.resize(heatmap_raw, (w, h))

    # Convert to RGB color heatmap
    heatmap_colored = cv2.applyColorMap(np.uint8(255 * heatmap_resized), cv2.COLORMAP_JET)

    # Superimpose heatmap onto original image
    alpha = 0.4
    overlay = cv2.addWeighted(orig_bgr, 1 - alpha, heatmap_colored, alpha, 0)

    results = {
        "original_image_path": str(image_path),
        "model_name": model_name,
        "heatmap_array": heatmap_resized,
        "output_paths": {}
    }

    if output_dir:
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
        base_name = image_path.stem

        orig_save = out_path / f"{base_name}_original.jpg"
        heat_save = out_path / f"{base_name}_heatmap.jpg"
        over_save = out_path / f"{base_name}_overlay.jpg"

        cv2.imwrite(str(orig_save), orig_bgr)
        cv2.imwrite(str(heat_save), heatmap_colored)
        cv2.imwrite(str(over_save), overlay)

        results["output_paths"] = {
            "original": str(orig_save),
            "heatmap": str(heat_save),
            "overlay": str(over_save)
        }

    return results

if __name__ == "__main__":
    from ml.models.efficientnet_b0 import VisionQCEfficientNetB0
    model = VisionQCEfficientNetB0(pretrained=False)
    chk = torch.load("ml/models/saved/efficientnet_b0_candidate.pth", map_location="cpu", weights_only=False)
    model.load_state_dict(chk["state_dict"])
    
    # Test on a defective test sample
    test_defective = next(Path("ml/data/split/test/defective").glob("*.jpeg"))
    print(f"Generating Grad-CAM for test sample: {test_defective.name}")
    out = generate_gradcam_explanation(test_defective, model, "EfficientNet-B0", "docs/gradcam_samples")
    print("Grad-CAM generated successfully:")
    for mode, path in out["output_paths"].items():
        print(f" - {mode.upper()}: {path}")
