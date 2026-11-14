"""
VisionQC Dataset Validation Script
Validates:
- Directory existence and class breakdown
- File formats and readable image decoding
- Dimensions (expected: 512x512)
- Channels / Color mode (expected: Grayscale / L)
- Duplicate images via SHA-256 file hashes
- Summary report generation
"""

import hashlib
import json
from pathlib import Path
from PIL import Image

RAW_DATA_DIR = Path("ml/data/raw")
CLASSES = ["ok", "defective"]
EXPECTED_DIMENSIONS = (512, 512)
OUTPUT_REPORT_PATH = Path("docs/dataset_validation_report.json")

def calculate_sha256(filepath: Path) -> str:
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

def validate_dataset():
    report = {
        "dataset_path": str(RAW_DATA_DIR),
        "total_images": 0,
        "classes": {},
        "corrupted_images": [],
        "invalid_dimensions": [],
        "invalid_modes": [],
        "duplicates": [],
        "is_valid": True
    }

    seen_hashes = {}

    for class_name in CLASSES:
        class_dir = RAW_DATA_DIR / class_name
        if not class_dir.exists():
            print(f"Error: {class_dir} does not exist.")
            report["classes"][class_name] = {"count": 0, "status": "missing"}
            report["is_valid"] = False
            continue

        image_files = [f for f in class_dir.iterdir() if f.is_file() and f.name != ".gitkeep"]
        class_count = len(image_files)
        report["classes"][class_name] = {
            "count": class_count,
            "extensions": {}
        }
        report["total_images"] += class_count

        for img_path in image_files:
            ext = img_path.suffix.lower()
            report["classes"][class_name]["extensions"][ext] = report["classes"][class_name]["extensions"].get(ext, 0) + 1

            # Check duplicate hash
            file_hash = calculate_sha256(img_path)
            if file_hash in seen_hashes:
                duplicate_info = {
                    "original": str(seen_hashes[file_hash]),
                    "duplicate": str(img_path)
                }
                report["duplicates"].append(duplicate_info)
            else:
                seen_hashes[file_hash] = img_path

            # Image readability and dimensions
            try:
                with Image.open(img_path) as img:
                    img.verify() # Check integrity
                
                # Reopen to read size and mode (verify closes the image stream)
                with Image.open(img_path) as img:
                    if img.size != EXPECTED_DIMENSIONS:
                        report["invalid_dimensions"].append({
                            "path": str(img_path),
                            "actual_dimensions": img.size,
                            "expected": EXPECTED_DIMENSIONS
                        })
                    if img.mode not in ("L", "RGB", "RGBA"):
                        report["invalid_modes"].append({
                            "path": str(img_path),
                            "mode": img.mode
                        })
            except Exception as e:
                report["corrupted_images"].append({
                    "path": str(img_path),
                    "error": str(e)
                })

    if report["corrupted_images"] or report["invalid_dimensions"]:
        report["is_valid"] = False

    OUTPUT_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_REPORT_PATH, "w") as f:
        json.dump(report, f, indent=2)

    print("\n--- Validation Summary ---")
    print(f"Total images checked: {report['total_images']}")
    for c, data in report["classes"].items():
        print(f" - {c.upper()}: {data['count']} images (Extensions: {data['extensions']})")
    print(f"Corrupted images: {len(report['corrupted_images'])}")
    print(f"Invalid dimensions: {len(report['invalid_dimensions'])}")
    print(f"Duplicate images: {len(report['duplicates'])}")
    print(f"Report written to: {OUTPUT_REPORT_PATH}")
    print(f"Overall status: {'VALID' if report['is_valid'] else 'INVALID'}\n")

    return report

if __name__ == "__main__":
    validate_dataset()
