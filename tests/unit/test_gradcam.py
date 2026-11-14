"""
VisionQC Grad-CAM Unit Tests
Validates that Grad-CAM can hook and generate valid heatmaps for all 3 supported architectures:
1. Custom CNN
2. ResNet18
3. EfficientNet-B0
"""

from pathlib import Path
import numpy as np
import torch
from ml.explainability.gradcam import GradCAM, get_target_layer
from ml.models.custom_cnn import CustomCNN
from ml.models.resnet18 import VisionQCResNet18
from ml.models.efficientnet_b0 import VisionQCEfficientNetB0

def test_gradcam_custom_cnn():
    model = CustomCNN()
    target_layer = get_target_layer("Custom CNN", model)
    cam = GradCAM(model, target_layer)
    dummy_input = torch.randn(1, 3, 224, 224)
    heatmap = cam.generate_heatmap(dummy_input)
    cam.remove_hooks()
    assert isinstance(heatmap, np.ndarray), "Heatmap must be a numpy array"
    assert heatmap.ndim == 2, f"Heatmap must be 2D, got shape {heatmap.shape}"
    assert 0.0 <= np.max(heatmap) <= 1.0, "Heatmap values must be normalized to [0, 1]"

def test_gradcam_resnet18():
    model = VisionQCResNet18(pretrained=False)
    target_layer = get_target_layer("ResNet18", model)
    cam = GradCAM(model, target_layer)
    dummy_input = torch.randn(1, 3, 224, 224)
    heatmap = cam.generate_heatmap(dummy_input)
    cam.remove_hooks()
    assert isinstance(heatmap, np.ndarray)
    assert heatmap.ndim == 2
    assert 0.0 <= np.max(heatmap) <= 1.0

def test_gradcam_efficientnet():
    model = VisionQCEfficientNetB0(pretrained=False)
    target_layer = get_target_layer("EfficientNet-B0", model)
    cam = GradCAM(model, target_layer)
    dummy_input = torch.randn(1, 3, 224, 224)
    heatmap = cam.generate_heatmap(dummy_input)
    cam.remove_hooks()
    assert isinstance(heatmap, np.ndarray)
    assert heatmap.ndim == 2
    assert 0.0 <= np.max(heatmap) <= 1.0

if __name__ == "__main__":
    test_gradcam_custom_cnn()
    test_gradcam_resnet18()
    test_gradcam_efficientnet()
    print("All 3 Grad-CAM architecture unit tests passed successfully.")
