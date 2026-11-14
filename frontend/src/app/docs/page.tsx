"use client";

import React from "react";
import { FileText, BookOpen, Layers, Terminal } from "lucide-react";
import { Card } from "@/components/ui";

export default function DocsPage() {
  return (
    <div className="space-y-6">
      <div className="border-b border-[#D8DEE4] pb-4">
        <h1 className="text-2xl font-bold tracking-tight text-[#111820]">System Documentation & Architecture</h1>
        <p className="text-sm text-[#627282] mt-0.5">
          API references, engineering contracts, and architectural sitemap for VISIONqc.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card title="Architecture Overview">
          <div className="space-y-3 text-xs text-[#111820]">
            <p>
              VISIONqc is an end-to-end industrial MLOps system built for binary defect inspection of pump impellers (casting defects, pinholes, burrs).
            </p>
            <div className="space-y-1 font-mono text-[#627282]">
              <div>• Data Engine: DVC + Git versioning (1,300 images)</div>
              <div>• ML Pipeline: PyTorch + TorchVision Transfer Learning</div>
              <div>• Tracking & Registry: MLflow 3.10 with SQLite/Postgres backend</div>
              <div>• Orchestration: Apache Airflow DAGs</div>
              <div>• Serving Engine: FastAPI + PyTorch CPU/GPU inference + Grad-CAM</div>
              <div>• Observability: Prometheus scrape endpoint + Grafana</div>
            </div>
          </div>
        </Card>

        <Card title="Canonical API Contracts">
          <div className="space-y-3 text-xs font-mono">
            <div>
              <div className="font-bold text-[#111820]">POST /api/v1/inspection/predict</div>
              <div className="text-[#627282]">Multipart form upload (image/jpeg, image/png). Returns classification, defect probability, and Grad-CAM URLs.</div>
            </div>
            <div>
              <div className="font-bold text-[#111820]">GET /health</div>
              <div className="text-[#627282]">Liveness and model-loaded readiness check.</div>
            </div>
            <div>
              <div className="font-bold text-[#111820]">GET /metrics</div>
              <div className="text-[#627282]">Prometheus formatted metrics exporter.</div>
            </div>
          </div>
        </Card>
      </div>
    </div>
  );
}
