"""
Statistical Data Drift Detection Module for VisionQC.
Uses two-sample Kolmogorov-Smirnov (KS) tests to detect feature distribution shifts.
Enforces a minimum observation threshold before raising drift flags.
"""

from typing import Dict, List, Any
import numpy as np
from scipy import stats


class KolmogorovSmirnovDriftDetector:
    def __init__(self, p_value_threshold: float = 0.05, min_observations: int = 15):
        """
        :param p_value_threshold: Critical value for KS test (p < threshold implies drift)
        :param min_observations: Minimum batch size required before computing drift
        """
        self.p_value_threshold = p_value_threshold
        self.min_observations = min_observations

    def detect_drift(
        self,
        reference_features: Dict[str, List[float]],
        current_features: Dict[str, List[float]],
    ) -> Dict[str, Any]:
        """
        Run two-sample Kolmogorov-Smirnov test on each extracted feature.
        """
        results = {
            "drift_detected": False,
            "sample_size_current": 0,
            "sample_size_reference": 0,
            "features": {},
            "drifted_features": [],
            "p_value_threshold": self.p_value_threshold,
        }

        # Check sample sizes
        feature_names = [f for f in reference_features if f in current_features]
        if not feature_names:
            return results

        n_ref = len(reference_features[feature_names[0]])
        n_cur = len(current_features[feature_names[0]])
        results["sample_size_reference"] = n_ref
        results["sample_size_current"] = n_cur

        if n_cur < self.min_observations:
            results["warning"] = f"Insufficient sample size ({n_cur} < {self.min_observations}). Drift check deferred."
            return results

        for feat in feature_names:
            ref_arr = np.array(reference_features[feat], dtype=np.float64)
            cur_arr = np.array(current_features[feat], dtype=np.float64)

            # Two-sample KS test
            ks_stat, p_val = stats.ks_2samp(ref_arr, cur_arr)
            is_drifted = bool(p_val < self.p_value_threshold)

            results["features"][feat] = {
                "ks_statistic": float(ks_stat),
                "p_value": float(p_val),
                "drift_detected": is_drifted,
                "ref_mean": float(np.mean(ref_arr)),
                "cur_mean": float(np.mean(cur_arr)),
            }

            if is_drifted:
                results["drifted_features"].append(feat)

        results["drift_detected"] = len(results["drifted_features"]) > 0
        return results
