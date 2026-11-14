"""
VisionQC Custom CNN Baseline Architecture
- Conv Block 1: 3 -> 32 channels, 3x3 kernel, ReLU, MaxPool
- Conv Block 2: 32 -> 64 channels, 3x3 kernel, ReLU, MaxPool
- Conv Block 3: 64 -> 128 channels, 3x3 kernel, ReLU, MaxPool
- Conv Block 4: 128 -> 256 channels, 3x3 kernel, ReLU, AdaptiveAvgPool(4, 4)
- Classifier: Flatten -> Linear(256*4*4, 256) -> ReLU -> Dropout(0.4) -> Linear(256, 1)
- Binary classification output (single logit for BCEWithLogitsLoss)
"""

import torch
import torch.nn as nn

class CustomCNN(nn.Module):
    def __init__(self, in_channels: int = 3, dropout_rate: float = 0.4):
        super().__init__()
        
        self.features = nn.Sequential(
            # Block 1: 224x224 -> 112x112
            nn.Conv2d(in_channels, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=False),
            nn.MaxPool2d(kernel_size=2, stride=2),
            
            # Block 2: 112x112 -> 56x56
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=False),
            nn.MaxPool2d(kernel_size=2, stride=2),
            
            # Block 3: 56x56 -> 28x28
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=False),
            nn.MaxPool2d(kernel_size=2, stride=2),
            
            # Block 4: 28x28 -> 14x14
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.AdaptiveAvgPool2d((4, 4)) # Output fixed at 256 x 4 x 4
        )
        
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(256 * 4 * 4, 256),
            nn.ReLU(inplace=False),
            nn.Dropout(p=dropout_rate),
            nn.Linear(256, 1) # Single logit for binary classification
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        feat = self.features(x)
        logits = self.classifier(feat)
        return logits.squeeze(-1) # Output shape: [batch_size]

if __name__ == "__main__":
    model = CustomCNN()
    dummy_input = torch.randn(4, 3, 224, 224)
    out = model(dummy_input)
    print("Model initialized successfully.")
    print(f"Input shape: {dummy_input.shape} -> Output logit shape: {out.shape}")
    total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Total trainable parameters: {total_params:,}")
