"""
Unit tests for VisionQC Drift Feature Extractor and KS-Test Detector.
"""

import numpy as np
import pytest
from ml.drift.feature_extractor import ImageFeatureExtractor
from ml.drift.drift_detector import KolmogorovSmirnovDriftDetector


def test_feature_extractor_synthetic():
    extractor = ImageFeatureExtractor(bins=16)
    img = np.full((100, 100), 128, dtype=np.uint8)

    feats = extractor.extract_from_array(img)
    assert "mean_brightness" in feats
    assert feats["mean_brightness"] == 128.0
    assert feats["std_intensity"] == 0.0
    assert "sharpness" in feats
    assert "hist_bin_0" in feats


def test_ks_drift_detector_stable():
    detector = KolmogorovSmirnovDriftDetector(p_value_threshold=0.05, min_observations=20)

    # Reference and current from identical Gaussian distribution
    np.random.seed(42)
    ref = {"mean_brightness": np.random.normal(128, 10, 50).tolist()}
    cur = {"mean_brightness": np.random.normal(128, 10, 50).tolist()}

    res = detector.detect_drift(ref, cur)
    assert res["drift_detected"] is False
    assert len(res["drifted_features"]) == 0
    assert res["features"]["mean_brightness"]["p_value"] > 0.05


def test_ks_drift_detector_detects_shift():
    detector = KolmogorovSmirnovDriftDetector(p_value_threshold=0.05, min_observations=20)

    np.random.seed(42)
    ref = {"mean_brightness": np.random.normal(128, 5, 50).tolist()}
    # Perturb current distribution with heavy brightness shift (+40)
    cur = {"mean_brightness": np.random.normal(168, 5, 50).tolist()}

    res = detector.detect_drift(ref, cur)
    assert res["drift_detected"] is True
    assert "mean_brightness" in res["drifted_features"]
    assert res["features"]["mean_brightness"]["p_value"] < 0.001
