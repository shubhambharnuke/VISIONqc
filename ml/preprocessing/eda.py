"""
VisionQC Exploratory Data Analysis (EDA) Module
Calculates:
- Class distribution statistics and chart
- Sample image comparison grid
- Image pixel intensity distributions and histogram plots
- Mean brightness, standard deviation, contrast, and Laplacian sharpness statistics per class
- Summary EDA report output to docs/eda/
"""

import json
from pathlib import Path
import cv2
import matplotlib.pyplot as plt
import numpy as np

RAW_DIR = Path("ml/data/raw")
EDA_OUT_DIR = Path("docs/eda")
CLASSES = ["ok", "defective"]

def compute_image_stats(image_path: Path):
    # Read as grayscale
    img = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    
    mean_val = float(np.mean(img))
    std_val = float(np.std(img))
    # Contrast: standard deviation or dynamic range (max - min)
    dynamic_range = float(np.max(img) - np.min(img))
    # Sharpness: variance of Laplacian
    laplacian_var = float(cv2.Laplacian(img, cv2.CV_64F).var())
    
    return {
        "mean_brightness": mean_val,
        "std_dev": std_val,
        "contrast_dynamic_range": dynamic_range,
        "sharpness_laplacian_var": laplacian_var,
        "hist": cv2.calcHist([img], [0], None, [256], [0, 256]).flatten()
    }

def run_eda():
    EDA_OUT_DIR.mkdir(parents=True, exist_ok=True)
    
    results = {
        "classes": {},
        "overall": {
            "total_images": 0
        }
    }
    
    class_images = {}
    aggregated_hist = {}
    
    for c in CLASSES:
        c_dir = RAW_DIR / c
        images = [f for f in c_dir.iterdir() if f.is_file() and f.name != ".gitkeep"]
        class_images[c] = images
        results["overall"]["total_images"] += len(images)
        
        means = []
        stds = []
        contrasts = []
        sharpnesses = []
        hist_sum = np.zeros(256)
        
        for img_path in images:
            stats = compute_image_stats(img_path)
            if stats:
                means.append(stats["mean_brightness"])
                stds.append(stats["std_dev"])
                contrasts.append(stats["contrast_dynamic_range"])
                sharpnesses.append(stats["sharpness_laplacian_var"])
                hist_sum += stats["hist"]
                
        aggregated_hist[c] = hist_sum / len(images)
        
        results["classes"][c] = {
            "count": len(images),
            "percentage": round((len(images) / 1300.0) * 100, 2),
            "mean_brightness": {
                "mean": round(float(np.mean(means)), 2),
                "std": round(float(np.std(means)), 2)
            },
            "pixel_std_dev": {
                "mean": round(float(np.mean(stds)), 2),
                "std": round(float(np.std(stds)), 2)
            },
            "contrast_range": {
                "mean": round(float(np.mean(contrasts)), 2),
                "std": round(float(np.std(contrasts)), 2)
            },
            "sharpness_laplacian": {
                "mean": round(float(np.mean(sharpnesses)), 2),
                "std": round(float(np.std(sharpnesses)), 2)
            }
        }

    # 1. Class Distribution Bar Chart
    fig, ax = plt.subplots(figsize=(6, 4))
    counts = [results["classes"][c]["count"] for c in CLASSES]
    colors = ["#34765B", "#B64B46"] # Brand semantic colors
    ax.bar([c.upper() for c in CLASSES], counts, color=colors, width=0.5)
    ax.set_ylabel("Count")
    ax.set_title("VisionQC — Casting Impeller Class Distribution")
    for i, v in enumerate(counts):
        ax.text(i, v + 15, f"{v} ({results['classes'][CLASSES[i]]['percentage']}%)", ha='center', fontweight='bold')
    ax.set_ylim(0, 900)
    plt.tight_layout()
    fig.savefig(EDA_OUT_DIR / "class_distribution.png", dpi=150)
    plt.close()

    # 2. Pixel Intensity Distribution Comparison
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(aggregated_hist["ok"], label="OK", color="#34765B", linewidth=2)
    ax.plot(aggregated_hist["defective"], label="DEFECTIVE", color="#B64B46", linewidth=2, linestyle="--")
    ax.set_title("Average Pixel Intensity Histogram by Class")
    ax.set_xlabel("Pixel Value (0-255)")
    ax.set_ylabel("Normalized Frequency")
    ax.legend()
    ax.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    fig.savefig(EDA_OUT_DIR / "pixel_intensity_histograms.png", dpi=150)
    plt.close()

    # 3. Sample Images Grid (3 OK, 3 DEFECTIVE)
    fig, axes = plt.subplots(2, 3, figsize=(9, 6))
    for i in range(3):
        # OK row
        ok_img = cv2.imread(str(class_images["ok"][i]), cv2.IMREAD_GRAYSCALE)
        axes[0, i].imshow(ok_img, cmap='gray')
        axes[0, i].set_title(f"OK Sample {i+1}")
        axes[0, i].axis("off")
        
        # Defective row
        def_img = cv2.imread(str(class_images["defective"][i]), cv2.IMREAD_GRAYSCALE)
        axes[1, i].imshow(def_img, cmap='gray')
        axes[1, i].set_title(f"DEFECTIVE Sample {i+1}")
        axes[1, i].axis("off")
        
    plt.suptitle("Sample Impeller Inspection Images", fontsize=14, fontweight='bold')
    plt.tight_layout()
    fig.savefig(EDA_OUT_DIR / "sample_inspection_grid.png", dpi=150)
    plt.close()

    # Save summary report JSON
    with open(EDA_OUT_DIR / "eda_report.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n--- EDA Complete ---")
    print(json.dumps(results, indent=2))
    print(f"EDA artifacts saved to: {EDA_OUT_DIR}")
    return results

if __name__ == "__main__":
    run_eda()
