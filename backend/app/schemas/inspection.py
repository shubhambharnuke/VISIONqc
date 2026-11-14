"""
VisionQC Pydantic API Schemas
Strongly-typed validation for inspection requests, responses, model info, and metadata.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):
    prediction_id: str
    predicted_class: str = Field(..., description="OK or DEFECTIVE")
    defect_probability: float = Field(..., ge=0.0, le=1.0)
    decision: str = Field(..., description="ACCEPT or REJECT")
    threshold_applied: float = 0.50
    model_name: str
    model_version: str
    inference_latency_ms: float
    has_gradcam: bool = False
    gradcam_urls: Optional[Dict[str, str]] = None

class ActiveModelInfo(BaseModel):
    model_name: str
    architecture: str
    version: str
    dataset_version: str = "dataset-v1.0"
    operating_threshold: float = 0.50
    defect_recall: float
    accuracy: float
    status: str = "ACTIVE"
    checkpoint_file: str

class HealthResponse(BaseModel):
    status: str = "healthy"
    app_name: str = "VisionQC"
    environment: str
    active_model_loaded: bool
    model_name: Optional[str] = None
    model_version: Optional[str] = None
