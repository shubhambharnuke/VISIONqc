"""
VisionQC EfficientNet-B0 Transfer Learning Model
- Architecture: Pretrained EfficientNet-B0 from TorchVision (DEFAULT weights)
- Modified final classifier: classifier -> Dropout(0.2) -> Linear(1280, 1) for binary defect classification
- Parameter-efficient computer vision architecture (~4.01M parameters)
"""

import torch
import torch.nn as nn
from torchvision.models import efficientnet_b0, EfficientNet_B0_Weights

class VisionQCEfficientNetB0(nn.Module):
    def __init__(self, pretrained: bool = True, freeze_backbone: bool = False):
        super().__init__()
        weights = EfficientNet_B0_Weights.DEFAULT if pretrained else None
        self.backbone = efficientnet_b0(weights=weights)

        if freeze_backbone:
            for param in self.backbone.parameters():
                param.requires_grad = False

        in_features = self.backbone.classifier[1].in_features
        # Replace classifier head with custom binary classifier
        self.backbone.classifier = nn.Sequential(
            nn.Dropout(p=0.3),
            nn.Linear(in_features, 1)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        logits = self.backbone(x)
        return logits.squeeze(-1) # Output shape: [batch_size]

if __name__ == "__main__":
    model = VisionQCEfficientNetB0(pretrained=True)
    dummy_input = torch.randn(4, 3, 224, 224)
    out = model(dummy_input)
    print("EfficientNet-B0 initialized successfully.")
    print(f"Input: {dummy_input.shape} -> Output: {out.shape}")
    total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Trainable parameters: {total_params:,}")
