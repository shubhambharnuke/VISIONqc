"""
VisionQC Stratified Dataset Splitting Script
- Performs reproducible stratified split (70% train, 15% val, 15% test)
- Fixed random seed = 42
- Copies original images to ml/data/split/{train,val,test}/{ok,defective}/
- Verifies zero sample overlap/leakage between splits
- Exports split metadata to docs/split_metadata.json
"""

import json
import shutil
from pathlib import Path
import yaml
from sklearn.model_selection import train_test_split

CONFIG_PATH = Path("configs/preprocessing_config.yaml")
RAW_DIR = Path("ml/data/raw")
SPLIT_DIR = Path("ml/data/split")
CLASSES = ["ok", "defective"]

def generate_splits():
    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)
    
    seed = config["split"]["random_seed"]
    train_ratio = config["split"]["train_ratio"]
    val_ratio = config["split"]["val_ratio"]
    test_ratio = config["split"]["test_ratio"]
    
    val_test_ratio = val_ratio + test_ratio
    relative_test_ratio = test_ratio / val_test_ratio
    
    # Collect all image file paths and labels
    all_items = []
    for c in CLASSES:
        c_dir = RAW_DIR / c
        files = [f for f in c_dir.iterdir() if f.is_file() and f.name != ".gitkeep"]
        for f in files:
            all_items.append((str(f.resolve()), c, f.name))
            
    filepaths = [x[0] for x in all_items]
    labels = [x[1] for x in all_items]
    filenames = [x[2] for x in all_items]
    
    # First split: Train vs (Val + Test)
    train_files, val_test_files, train_labels, val_test_labels, train_names, val_test_names = train_test_split(
        filepaths, labels, filenames,
        test_size=val_test_ratio,
        random_state=seed,
        stratify=labels
    )
    
    # Second split: Val vs Test
    val_files, test_files, val_labels, test_labels, val_names, test_names = train_test_split(
        val_test_files, val_test_labels, val_test_names,
        test_size=relative_test_ratio,
        random_state=seed,
        stratify=val_test_labels
    )
    
    splits = {
        "train": (train_files, train_labels, train_names),
        "val": (val_files, val_labels, val_names),
        "test": (test_files, test_labels, test_names)
    }
    
    # Reset split directory cleanly
    if SPLIT_DIR.exists():
        shutil.rmtree(SPLIT_DIR)
        
    metadata = {
        "random_seed": seed,
        "split_ratios": {"train": train_ratio, "val": val_ratio, "test": test_ratio},
        "counts": {}
    }
    
    leakage_check = set()
    
    for split_name, (files, lbls, names) in splits.items():
        metadata["counts"][split_name] = {"total": len(files), "classes": {}}
        for src_path, label, filename in zip(files, lbls, names):
            # Check leakage
            if src_path in leakage_check:
                raise ValueError(f"Data leakage detected! {src_path} present in multiple splits.")
            leakage_check.add(src_path)
            
            # Destination path
            dest_dir = SPLIT_DIR / split_name / label
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_path, dest_dir / filename)
            
            metadata["counts"][split_name]["classes"][label] = metadata["counts"][split_name]["classes"].get(label, 0) + 1

    # Keep .gitkeep in each directory
    for s in ["train", "val", "test"]:
        for c in CLASSES:
            (SPLIT_DIR / s / c / ".gitkeep").touch()
            
    with open("docs/split_metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)
        
    print("\n--- Stratified Split Completed ---")
    print(json.dumps(metadata, indent=2))
    print(f"Total images placed across splits: {len(leakage_check)}")
    print(f"Leakage validation: ZERO overlap between Train, Validation, and Test.\n")
    return metadata

if __name__ == "__main__":
    generate_splits()
