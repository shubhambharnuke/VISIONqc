"""
VisionQC Preprocessing Pipeline Module
Defines canonical transforms for:
- Training: Resizing (224x224), Grayscale-to-RGB expansion (3 channels), Augmentations, Normalization
- Validation / Test / Inference: Resizing (224x224), Grayscale-to-RGB expansion, Normalization (strictly unaugmented)
"""

from pathlib import Path
from PIL import Image
import torch
import torchvision.transforms as T
import yaml

CONFIG_PATH = Path("configs/preprocessing_config.yaml")

def load_preprocessing_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

def get_transforms(is_train: bool = False) -> T.Compose:
    cfg = load_preprocessing_config()
    target_size = tuple(cfg["image"]["target_size"])
    mean = cfg["normalization"]["mean"]
    std = cfg["normalization"]["std"]
    aug_cfg = cfg["augmentation"]

    transform_list = []

    # 1. Resize to canonical target dimension (224x224)
    transform_list.append(T.Resize(target_size))

    # 2. Convert grayscale to 3-channel RGB (required for ResNet/EfficientNet & uniform Custom CNN pipeline)
    transform_list.append(T.Lambda(lambda img: img.convert("RGB")))

    # 3. Augmentations strictly applied only when is_train=True
    if is_train:
        if aug_cfg.get("horizontal_flip", False):
            transform_list.append(T.RandomHorizontalFlip(p=aug_cfg.get("horizontal_flip_prob", 0.5)))
        if aug_cfg.get("vertical_flip", False):
            transform_list.append(T.RandomVerticalFlip(p=aug_cfg.get("vertical_flip_prob", 0.5)))
        if aug_cfg.get("rotation_degrees", 0) > 0:
            transform_list.append(T.RandomRotation(degrees=aug_cfg["rotation_degrees"]))
        if aug_cfg.get("brightness_jitter", 0) > 0 or aug_cfg.get("contrast_jitter", 0) > 0:
            transform_list.append(T.ColorJitter(
                brightness=aug_cfg.get("brightness_jitter", 0),
                contrast=aug_cfg.get("contrast_jitter", 0)
            ))

    # 4. Convert PIL to Tensor [0, 1]
    transform_list.append(T.ToTensor())

    # 5. Standard Normalization
    transform_list.append(T.Normalize(mean=mean, std=std))

    return T.Compose(transform_list)

def preprocess_image(image_path: str | Path) -> torch.Tensor:
    """Preprocess a single image for inference using canonical inference transform."""
    transform = get_transforms(is_train=False)
    with Image.open(image_path) as img:
        tensor = transform(img)
    return tensor.unsqueeze(0) # Add batch dimension: [1, 3, 224, 224]
