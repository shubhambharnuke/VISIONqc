"""
Image feature extractor for statistical drift detection in VisionQC.
Extracts:
1. Mean pixel brightness
2. Standard deviation of pixel intensities
3. Contrast ratio / dynamic range
4. Sharpness variance (Laplacian)
5. Intensity histogram bins
"""

from typing import Dict, List, Union
import numpy as np
import cv2
from PIL import Image


class ImageFeatureExtractor:
    def __init__(self, bins: int = 16):
        self.bins = bins

    def extract_from_array(self, image_np: np.ndarray) -> Dict[str, float]:
        """
        Extract numerical features from an image numpy array.
        Handles grayscale (H, W) or RGB (H, W, C).
        """
        if image_np.ndim == 3 and image_np.shape[2] == 3:
            gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
        elif image_np.ndim == 2:
            gray = image_np
        else:
            gray = image_np[:, :, 0]

        # 1. Mean brightness
        mean_brightness = float(np.mean(gray))

        # 2. Standard deviation of intensity
        std_intensity = float(np.std(gray))

        # 3. Contrast (Michelson-like contrast: (max - min) / (max + min + eps))
        min_val = float(np.min(gray))
        max_val = float(np.max(gray))
        contrast = (max_val - min_val) / (max_val + min_val + 1e-7)

        # 4. Sharpness (Variance of Laplacian)
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        sharpness_var = float(laplacian.var())

        # 5. Histogram distribution features
        hist, _ = np.histogram(gray, bins=self.bins, range=(0, 256), density=True)
        hist_features = {f"hist_bin_{i}": float(hist[i]) for i in range(self.bins)}

        features = {
            "mean_brightness": mean_brightness,
            "std_intensity": std_intensity,
            "contrast": contrast,
            "sharpness": sharpness_var,
        }
        features.update(hist_features)
        return features

    def extract_from_path(self, image_path: str) -> Dict[str, float]:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise ValueError(f"Could not read image from {image_path}")
        return self.extract_from_array(img)

    def extract_from_bytes(self, image_bytes: bytes) -> Dict[str, float]:
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise ValueError("Failed to decode image bytes")
        return self.extract_from_array(img)
