"""
VisionQC Inspection Router
Provides endpoints for:
- POST /api/v1/inspection/predict: image upload, inference, Grad-CAM, database persistence
- GET /api/v1/inspection/history: historical inspection records
"""

from typing import List
from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from backend.app.database.connection import get_db
from backend.app.database.models import Prediction
from backend.app.schemas.inspection import PredictionResponse
from backend.app.services.model_service import model_service

router = APIRouter(prefix="/inspection", tags=["Inspection"])

@router.post("/predict", response_model=PredictionResponse)
async def inspect_impeller_image(
    file: UploadFile = File(..., description="Pump impeller image file"),
    explain: bool = Form(True, description="Generate Grad-CAM visualization"),
    db: Session = Depends(get_db)
):
    # 1. Validate file extension
    ext = file.filename.split(".")[-1].lower() if "." in file.filename else ""
    if ext not in ["jpg", "jpeg", "png"]:
        raise HTTPException(status_code=400, detail="Unsupported image format. Allowed: .jpg, .jpeg, .png")

    # 2. Read bytes and check size (limit: 10MB)
    contents = await file.read()
    if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File size exceeds maximum 10MB limit")

    # 3. Model Inference & Grad-CAM
    try:
        result = model_service.predict(contents, filename=file.filename, generate_gradcam=explain)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Image decoding error: {str(e)}")

    # 4. Persist Prediction record in PostgreSQL/SQLite
    pred_record = Prediction(
        id=result["prediction_id"],
        image_filename=file.filename,
        predicted_class=result["predicted_class"],
        defect_probability=result["defect_probability"],
        decision=result["decision"],
        threshold_applied=result["threshold_applied"],
        model_name=result["model_name"],
        model_version=result["model_version"],
        inference_latency_ms=result["inference_latency_ms"],
        has_gradcam=result["has_gradcam"],
        gradcam_paths=result["gradcam_urls"]
    )
    db.add(pred_record)
    db.commit()

    return result

@router.get("/history", response_model=List[PredictionResponse])
def get_inspection_history(
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    records = db.query(Prediction).order_by(Prediction.created_at.desc()).limit(limit).all()
    return [
        {
            "prediction_id": r.id,
            "predicted_class": r.predicted_class,
            "defect_probability": r.defect_probability,
            "decision": r.decision,
            "threshold_applied": r.threshold_applied,
            "model_name": r.model_name,
            "model_version": r.model_version,
            "inference_latency_ms": r.inference_latency_ms,
            "has_gradcam": r.has_gradcam,
            "gradcam_urls": r.gradcam_paths
        }
        for r in records
    ]
