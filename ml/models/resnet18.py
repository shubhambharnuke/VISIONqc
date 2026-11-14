"""
VisionQC ResNet18 Transfer Learning Model
- Architecture: Pretrained ResNet18 from TorchVision (DEFAULT weights)
- Modified final fully connected layer: fc -> Linear(512, 1) for binary defect classification
- Configurable layer freezing for feature extraction vs full fine-tuning
"""

import torch
import torch.nn as nn
from torchvision.models import resnet18, ResNet18_Weights

class VisionQCResNet18(nn.Module):
    def __init__(self, pretrained: bool = True, freeze_backbone: bool = False):
        super().__init__()
        weights = ResNet18_Weights.DEFAULT if pretrained else None
        self.backbone = resnet18(weights=weights)

        if freeze_backbone:
            for param in self.backbone.parameters():
                param.requires_grad = False

        in_features = self.backbone.fc.in_features
        # Replace classification head with custom binary classifier
        self.backbone.fc = nn.Sequential(
            nn.Dropout(p=0.3),
            nn.Linear(in_features, 1)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        logits = self.backbone(x)
        return logits.squeeze(-1) # Output shape: [batch_size]

if __name__ == "__main__":
    model = VisionQCResNet18(pretrained=True)
    dummy_input = torch.randn(4, 3, 224, 224)
    out = model(dummy_input)
    print("ResNet18 initialized successfully.")
    print(f"Input: {dummy_input.shape} -> Output: {out.shape}")
    total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Trainable parameters: {total_params:,}")
