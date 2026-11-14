"""
Unit and integration tests for FastAPI backend and model serving API.
"""
import io
import pytest
from fastapi.testclient import TestClient
from PIL import Image

from backend.app.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client


def create_test_image_bytes(format="JPEG", color="gray"):
    img = Image.new("L" if color == "gray" else "RGB", (512, 512), color=128)
    buf = io.BytesIO()
    img.save(buf, format=format)
    buf.seek(0)
    return buf.getvalue()


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["app_name"] == "VisionQC"
    assert data["active_model_loaded"] is True
    assert data["model_name"] == "EfficientNet-B0"


def test_model_info(client):
    response = client.get("/model-info")
    assert response.status_code == 200
    data = response.json()
    assert data["model_name"] == "EfficientNet-B0"
    assert "EfficientNet" in data["architecture"]
    assert "threshold" in data


def test_active_models(client):
    response = client.get("/api/v1/models/active")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data["name"] == "visionqc-impeller-classifier" or data["model_name"] == "EfficientNet-B0"


def test_inspection_prediction_success(client):
    img_bytes = create_test_image_bytes()
    files = {"file": ("test_impeller.jpg", img_bytes, "image/jpeg")}
    data = {"explain": "true"}

    response = client.post("/api/v1/inspection/predict", files=files, data=data)
    assert response.status_code == 200
    res = response.json()

    assert "prediction_id" in res
    assert res["predicted_class"] in ["OK", "DEFECTIVE"]
    assert res["decision"] in ["ACCEPT", "REJECT"]
    assert 0.0 <= res["defect_probability"] <= 1.0
    assert "inference_latency_ms" in res
    assert res["inference_latency_ms"] > 0
    assert res["has_gradcam"] is True
    assert res["gradcam_urls"] is not None
    assert "heatmap" in res["gradcam_urls"]
    assert "overlay" in res["gradcam_urls"]


def test_prediction_invalid_file_type(client):
    files = {"file": ("test.txt", b"not an image", "text/plain")}
    response = client.post("/api/v1/inspection/predict", files=files)
    assert response.status_code == 400
    assert "Unsupported image format" in response.json()["detail"]


def test_inspection_history(client):
    response = client.get("/api/v1/inspection/history?limit=10")
    assert response.status_code == 200
    res = response.json()
    assert isinstance(res, list)
    assert len(res) >= 1
    assert "prediction_id" in res[0]
    assert "predicted_class" in res[0]


def test_metrics_endpoint(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "visionqc_requests_total" in response.text
    assert "visionqc_inference_latency_seconds" in response.text
