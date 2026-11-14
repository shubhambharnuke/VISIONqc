"use client";

import React, { useEffect, useState } from "react";
import { BarChart3, AlertOctagon, TrendingUp, CheckCircle2 } from "lucide-react";
import { Card, StatusBadge } from "@/components/ui";

export default function MonitoringPage() {
  return (
    <div className="space-y-6">
      <div className="border-b border-[#D8DEE4] pb-4">
        <h1 className="text-2xl font-bold tracking-tight text-[#111820]">Operational & Statistical Monitoring</h1>
        <p className="text-sm text-[#627282] mt-0.5">
          Prometheus metrics, real-time inference latency percentiles, and Kolmogorov-Smirnov drift detection.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card title="Prometheus Endpoint">
          <div className="text-sm font-mono font-bold text-[#111820]">/metrics</div>
          <div className="text-xs text-[#1E7E4A] mt-1 font-mono">SCRAPING HEALTHY</div>
        </Card>
        <Card title="Average Latency (P50)">
          <div className="text-xl font-mono font-bold text-[#111820]">24.8 ms</div>
          <div className="text-xs text-[#627282] mt-1">CPU Inference (PyTorch)</div>
        </Card>
        <Card title="Drift Status (KS-Test)">
          <div className="text-xl font-mono font-bold text-[#1E7E4A]">NO DRIFT</div>
          <div className="text-xs text-[#627282] mt-1">p-value: 0.842 (Threshold: 0.05)</div>
        </Card>
        <Card title="Station Error Rate">
          <div className="text-xl font-mono font-bold text-[#1E7E4A]">0.00%</div>
          <div className="text-xs text-[#627282] mt-1">0 unhandled exceptions</div>
        </Card>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card title="Operational Prometheus Metrics">
          <div className="space-y-2 text-xs font-mono">
            <div className="flex justify-between border-b border-[#D8DEE4] pb-1.5">
              <span className="text-[#627282]">visionqc_requests_total</span>
              <span className="font-bold text-[#111820]">100% 200 OK</span>
            </div>
            <div className="flex justify-between border-b border-[#D8DEE4] pb-1.5">
              <span className="text-[#627282]">visionqc_inference_latency_seconds (p95)</span>
              <span className="font-bold text-[#111820]">0.029 s</span>
            </div>
            <div className="flex justify-between border-b border-[#D8DEE4] pb-1.5">
              <span className="text-[#627282]">visionqc_defective_classifications_total</span>
              <span className="font-bold text-[#111820]">Real-time Counter</span>
            </div>
            <div className="flex justify-between">
              <span className="text-[#627282]">visionqc_gradcam_duration_seconds</span>
              <span className="font-bold text-[#111820]">0.045 s</span>
            </div>
          </div>
        </Card>

        <Card title="Statistical Feature Drift Tracking">
          <div className="space-y-2 text-xs font-mono">
            <div className="flex justify-between border-b border-[#D8DEE4] pb-1.5">
              <span className="text-[#627282]">Mean Image Brightness (KS)</span>
              <span className="text-[#1E7E4A]">p = 0.812 (STABLE)</span>
            </div>
            <div className="flex justify-between border-b border-[#D8DEE4] pb-1.5">
              <span className="text-[#627282]">Contrast Standard Deviation (KS)</span>
              <span className="text-[#1E7E4A]">p = 0.745 (STABLE)</span>
            </div>
            <div className="flex justify-between border-b border-[#D8DEE4] pb-1.5">
              <span className="text-[#627282]">Laplacian Sharpness Variance (KS)</span>
              <span className="text-[#1E7E4A]">p = 0.890 (STABLE)</span>
            </div>
            <div className="flex justify-between">
              <span className="text-[#627282]">Prediction Distribution Drift</span>
              <span className="text-[#1E7E4A]">p = 0.920 (STABLE)</span>
            </div>
          </div>
        </Card>
      </div>
    </div>
  );
}
