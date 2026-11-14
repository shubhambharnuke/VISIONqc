"""
VisionQC Dataset and DataLoader Factory Module
- ImpellerDataset: Custom PyTorch dataset for split images
- get_dataloaders(): Factory function returning train, val, and test DataLoaders
"""

from pathlib import Path
from typing import Dict, Tuple
from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader

from ml.preprocessing.preprocess import get_transforms

CLASS_TO_IDX = {"ok": 0, "defective": 1}
IDX_TO_CLASS = {0: "ok", 1: "defective"}

class ImpellerDataset(Dataset):
    def __init__(self, split_dir: Path, is_train: bool = False):
        self.split_dir = Path(split_dir)
        self.is_train = is_train
        self.transform = get_transforms(is_train=self.is_train)
        
        self.samples = []
        for class_name, label_idx in CLASS_TO_IDX.items():
            class_path = self.split_dir / class_name
            if class_path.exists():
                for f in class_path.iterdir():
                    if f.is_file() and f.name != ".gitkeep":
                        self.samples.append((str(f), label_idx))
                        
    def __len__(self) -> int:
        return len(self.samples)
        
    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, int]:
        img_path, label = self.samples[idx]
        with Image.open(img_path) as img:
            tensor = self.transform(img)
        return tensor, label

def get_dataloaders(
    split_root: str | Path = "ml/data/split",
    batch_size: int = 32,
    num_workers: int = 0
) -> Dict[str, DataLoader]:
    split_root = Path(split_root)
    
    train_dataset = ImpellerDataset(split_root / "train", is_train=True)
    val_dataset = ImpellerDataset(split_root / "val", is_train=False)
    test_dataset = ImpellerDataset(split_root / "test", is_train=False)
    
    dataloaders = {
        "train": DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers),
        "val": DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers),
        "test": DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)
    }
    
    return dataloaders

if __name__ == "__main__":
    dls = get_dataloaders()
    for name, loader in dls.items():
        print(f"{name.upper()} DataLoader: {len(loader.dataset)} samples ({len(loader)} batches)")
    
    sample_batch, sample_labels = next(iter(dls["train"]))
    print(f"Batch shape: {sample_batch.shape}, Labels shape: {sample_labels.shape}")
