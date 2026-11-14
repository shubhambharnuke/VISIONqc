"""
VisionQC FastAPI Main Application Entrypoint
- Mounts CORS middleware
- Serves static Grad-CAM images
- Mounts all versioned /api/v1 routers
- Compatibility routes (GET /health, POST /predict, GET /model-info)
- Prometheus metrics instrumentation endpoint (/metrics)
"""

from pathlib import Path
from fastapi import FastAPI, UploadFile, File, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from prometheus_client import make_asgi_app, Counter, Histogram
from sqlalchemy.orm import Session

from backend.app.core.config import settings
from backend.app.database.connection import engine, Base, get_db
from backend.app.api.v1.inspection import router as inspection_router
from backend.app.api.v1.endpoints import (
    models_router,
    experiments_router,
    datasets_router,
    pipelines_router,
    monitoring_router,
    drift_router,
    retraining_router,
)
from backend.app.services.model_service import model_service
from backend.app.schemas.inspection import PredictionResponse, HealthResponse

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="VisionQC Automated Manufacturing Defect Inspection & MLOps Platform REST API"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files for Grad-CAM images
static_dir = Path("static/gradcam")
static_dir.mkdir(parents=True, exist_ok=True)
app.mount("/static/gradcam", StaticFiles(directory="static/gradcam"), name="gradcam")

# Prometheus Metrics Endpoint
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

# Prometheus Metric Counters
REQUEST_COUNTER = Counter("visionqc_requests_total", "Total API Requests", ["endpoint", "status"])
LATENCY_HISTOGRAM = Histogram("visionqc_inference_latency_seconds", "Inference latency in seconds")

# Mount Versioned API Routers
app.include_router(inspection_router, prefix=settings.API_V1_STR)
app.include_router(models_router, prefix=settings.API_V1_STR)
app.include_router(experiments_router, prefix=settings.API_V1_STR)
app.include_router(datasets_router, prefix=settings.API_V1_STR)
app.include_router(pipelines_router, prefix=settings.API_V1_STR)
app.include_router(monitoring_router, prefix=settings.API_V1_STR)
app.include_router(drift_router, prefix=settings.API_V1_STR)
app.include_router(retraining_router, prefix=settings.API_V1_STR)

# --- Canonical Compatibility Routes ---
@app.get("/health", response_model=HealthResponse, tags=["Compatibility"])
def health_check():
    return {
        "status": "healthy",
        "app_name": settings.PROJECT_NAME,
        "environment": settings.APP_ENV,
        "active_model_loaded": model_service.model is not None,
        "model_name": model_service.model_info.get("model_name"),
        "model_version": model_service.model_info.get("version")
    }

@app.get("/model-info", tags=["Compatibility"])
def get_model_info_compatibility():
    return model_service.model_info

@app.post("/predict", response_model=PredictionResponse, tags=["Compatibility"])
async def predict_compatibility(
    file: UploadFile = File(...),
    explain: bool = Form(True),
    db: Session = Depends(get_db)
):
    from backend.app.api.v1.inspection import inspect_impeller_image
    return await inspect_impeller_image(file=file, explain=explain, db=db)
