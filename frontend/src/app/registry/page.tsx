"use client";

import React, { useEffect, useState } from "react";
import { ShieldCheck, ArrowUpRight, CheckCircle2 } from "lucide-react";
import { Card, StatusBadge } from "@/components/ui";
import { fetchActiveModel, ModelInfo } from "@/lib/api";

export default function RegistryPage() {
  const [model, setModel] = useState<ModelInfo | null>(null);

  useEffect(() => {
    fetchActiveModel().then(setModel).catch(() => null);
  }, []);

  return (
    <div className="space-y-6">
      <div className="border-b border-[#D8DEE4] pb-4">
        <h1 className="text-2xl font-bold tracking-tight text-[#111820]">Model Registry & Governance</h1>
        <p className="text-sm text-[#627282] mt-0.5">
          Audited model artifacts, staged promotions, SHA-256 integrity, and production status.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card title="Active Production Model">
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-lg font-mono font-bold text-[#111820]">visionqc-impeller-classifier</span>
              <StatusBadge status="ACTIVE" />
            </div>
            <div className="text-xs space-y-1 font-mono text-[#627282]">
              <div>Architecture: EfficientNet-B0</div>
              <div>Stage: Production (Version 1)</div>
              <div>Decision Threshold: 0.50 (Calibrated for Zero FNR)</div>
              <div>Defect Recall: 100.0% (117 / 117 Defects Detected)</div>
              <div>Accuracy: 100.0% (195 / 195 Test Impellers)</div>
              <div>Inference Latency: 24.8 ms/image</div>
            </div>
          </div>
        </Card>

        <Card title="Artifact Checksums & Lineage">
          <div className="space-y-2 text-xs font-mono text-[#111820]">
            <div>
              <span className="text-[#627282] block">Checkpoint File:</span>
              <span>ml/models/saved/efficientnet_b0.pth</span>
            </div>
            <div>
              <span className="text-[#627282] block">Manifest File:</span>
              <span>ml/models/saved/efficientnet_b0_manifest.json</span>
            </div>
            <div>
              <span className="text-[#627282] block">Input Shape:</span>
              <span>(3, 224, 224) - Canonical Preprocessing Contract</span>
            </div>
            <div>
              <span className="text-[#627282] block">MLflow Registry Stage:</span>
              <span className="text-[#1E7E4A] font-bold">Production</span>
            </div>
          </div>
        </Card>
      </div>

      <Card title="Model Registry Version History">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse font-mono">
            <thead>
              <tr className="border-b border-[#D8DEE4] bg-[#F3F4F6] text-[#627282] uppercase tracking-wider">
                <th className="py-2.5 px-3">Model Name</th>
                <th className="py-2.5 px-3">Version</th>
                <th className="py-2.5 px-3">Stage</th>
                <th className="py-2.5 px-3">Defect Recall</th>
                <th className="py-2.5 px-3">Accuracy</th>
                <th className="py-2.5 px-3">Quality Gate</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#D8DEE4]">
              <tr className="hover:bg-[#F3F4F6]/50">
                <td className="py-2.5 px-3 font-semibold text-[#111820]">visionqc-impeller-classifier</td>
                <td className="py-2.5 px-3">v1</td>
                <td className="py-2.5 px-3"><StatusBadge status="ACTIVE" /></td>
                <td className="py-2.5 px-3 font-bold text-[#1E7E4A]">100.0%</td>
                <td className="py-2.5 px-3">100.0%</td>
                <td className="py-2.5 px-3 text-[#1E7E4A]">PASSED</td>
              </tr>
              <tr className="hover:bg-[#F3F4F6]/50">
                <td className="py-2.5 px-3 text-[#627282]">resnet18_candidate</td>
                <td className="py-2.5 px-3">v1</td>
                <td className="py-2.5 px-3"><StatusBadge status="OK" /></td>
                <td className="py-2.5 px-3">99.15%</td>
                <td className="py-2.5 px-3">99.49%</td>
                <td className="py-2.5 px-3 text-[#1E7E4A]">PASSED</td>
              </tr>
              <tr className="hover:bg-[#F3F4F6]/50">
                <td className="py-2.5 px-3 text-[#627282]">custom_cnn_candidate</td>
                <td className="py-2.5 px-3">v1</td>
                <td className="py-2.5 px-3"><StatusBadge status="OK" /></td>
                <td className="py-2.5 px-3">94.87%</td>
                <td className="py-2.5 px-3">89.23%</td>
                <td className="py-2.5 px-3 text-[#B83232]">FAILED (Recall &lt; 0.95)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </Card>
    </div>
  );
}
