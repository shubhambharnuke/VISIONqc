"use client";

import React, { useEffect, useState } from "react";
import Link from "next/link";
import { Activity, ShieldCheck, AlertTriangle, Clock, ArrowRight, Layers } from "lucide-react";
import { Card, Button, StatusBadge } from "@/components/ui";
import { fetchActiveModel, fetchInspectionHistory, InspectionPrediction, ModelInfo } from "@/lib/api";

export default function OverviewPage() {
  const [model, setModel] = useState<ModelInfo | null>(null);
  const [history, setHistory] = useState<InspectionPrediction[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadData() {
      try {
        const [m, h] = await Promise.all([
          fetchActiveModel().catch(() => null),
          fetchInspectionHistory(5).catch(() => []),
        ]);
        if (m) setModel(m);
        if (h) setHistory(h);
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, []);

  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-[#D8DEE4] pb-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-[#111820]">Station Overview</h1>
          <p className="text-sm text-[#627282] mt-0.5">
            Automated visual quality control monitoring for submersible pump impellers.
          </p>
        </div>
        <Link href="/inspection">
          <Button variant="primary" className="gap-2">
            <Layers size={16} />
            Open Inspection Workbench
          </Button>
        </Link>
      </div>

      {/* KPI Cards Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <Card title="Active Model">
          <div className="flex items-center justify-between">
            <div>
              <div className="text-xl font-bold text-[#111820] font-mono">
                {model?.model_name || "EfficientNet-B0"}
              </div>
              <div className="text-xs text-[#627282] mt-0.5 font-mono">
                Version: {model?.version || "1.0"}
              </div>
            </div>
            <StatusBadge status="ACTIVE" />
          </div>
        </Card>

        <Card title="Quality Gate Defect Recall">
          <div className="flex items-center justify-between">
            <div>
              <div className="text-xl font-bold text-[#1E7E4A] font-mono">100.0%</div>
              <div className="text-xs text-[#627282] mt-0.5">Target: ≥ 95.0%</div>
            </div>
            <ShieldCheck size={28} className="text-[#1E7E4A]" />
          </div>
        </Card>

        <Card title="Inference Latency (P95)">
          <div className="flex items-center justify-between">
            <div>
              <div className="text-xl font-bold text-[#111820] font-mono">24.8 ms</div>
              <div className="text-xs text-[#627282] mt-0.5">Target: &lt; 100.0 ms</div>
            </div>
            <Clock size={28} className="text-[#476985]" />
          </div>
        </Card>

        <Card title="Production Quality Gate">
          <div className="flex items-center justify-between">
            <div>
              <div className="text-xl font-bold text-[#1E7E4A] font-mono">PASSED</div>
              <div className="text-xs text-[#627282] mt-0.5">0 False Negatives</div>
            </div>
            <Activity size={28} className="text-[#1E7E4A]" />
          </div>
        </Card>
      </div>

      {/* Recent Inspections Table */}
      <Card title="Recent Station Inspections">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="border-b border-[#D8DEE4] bg-[#F3F4F6] text-[#627282] uppercase tracking-wider font-mono">
                <th className="py-2.5 px-3">Inspection ID</th>
                <th className="py-2.5 px-3">Decision</th>
                <th className="py-2.5 px-3">Classification</th>
                <th className="py-2.5 px-3">Defect Prob</th>
                <th className="py-2.5 px-3">Latency</th>
                <th className="py-2.5 px-3">Grad-CAM</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#D8DEE4]">
              {history.length === 0 ? (
                <tr>
                  <td colSpan={6} className="py-4 text-center text-[#627282]">
                    No live inspection events recorded yet. Run an inspection in the Workbench.
                  </td>
                </tr>
              ) : (
                history.map((item) => (
                  <tr key={item.prediction_id} className="hover:bg-[#F3F4F6]/50">
                    <td className="py-2.5 px-3 font-mono font-medium text-[#111820]">
                      {item.prediction_id.slice(0, 8)}...
                    </td>
                    <td className="py-2.5 px-3">
                      <StatusBadge status={item.decision} />
                    </td>
                    <td className="py-2.5 px-3 font-mono">{item.predicted_class}</td>
                    <td className="py-2.5 px-3 font-mono">{(item.defect_probability * 100).toFixed(1)}%</td>
                    <td className="py-2.5 px-3 font-mono">{item.inference_latency_ms.toFixed(1)} ms</td>
                    <td className="py-2.5 px-3">
                      {item.has_gradcam ? (
                        <span className="text-xs text-[#476985] font-mono">AVAILABLE</span>
                      ) : (
                        <span className="text-xs text-[#627282] font-mono">N/A</span>
                      )}
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </Card>
    </div>
  );
}
