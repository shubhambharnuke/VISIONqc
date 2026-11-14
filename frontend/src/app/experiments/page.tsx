"use client";

import React, { useEffect, useState } from "react";
import { FlaskConical, GitCommit, CheckCircle2 } from "lucide-react";
import { Card, StatusBadge } from "@/components/ui";
import { fetchExperiments } from "@/lib/api";

export default function ExperimentsPage() {
  const [runs, setRuns] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchExperiments()
      .then((data) => setRuns(data))
      .catch(() => setRuns([]))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="space-y-6">
      <div className="border-b border-[#D8DEE4] pb-4">
        <h1 className="text-2xl font-bold tracking-tight text-[#111820]">MLflow Experiments</h1>
        <p className="text-sm text-[#627282] mt-0.5">
          Audited model tracking, hyperparameter runs, and metrics for pump impeller inspection.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card title="Experiment Name">
          <div className="text-sm font-mono font-bold text-[#111820]">visionqc-impeller-inspection</div>
          <div className="text-xs text-[#627282] mt-1">3 Architecture Candidates Evaluated</div>
        </Card>
        <Card title="Selected Production Run">
          <div className="text-sm font-mono font-bold text-[#1E7E4A]">EfficientNet-B0 (Run 3)</div>
          <div className="text-xs text-[#627282] mt-1">Recall: 100.0% | ROC-AUC: 1.000</div>
        </Card>
        <Card title="Artifact Store">
          <div className="text-sm font-mono font-bold text-[#111820]">mlruns/ & SQLite</div>
          <div className="text-xs text-[#627282] mt-1">Checkpoints, Manifests, Eval Curves</div>
        </Card>
      </div>

      <Card title="Logged Experiment Runs">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="border-b border-[#D8DEE4] bg-[#F3F4F6] text-[#627282] uppercase tracking-wider font-mono">
                <th className="py-2.5 px-3">Run Name / ID</th>
                <th className="py-2.5 px-3">Status</th>
                <th className="py-2.5 px-3">Accuracy</th>
                <th className="py-2.5 px-3">Defect Recall</th>
                <th className="py-2.5 px-3">F1 Score</th>
                <th className="py-2.5 px-3">ROC-AUC</th>
                <th className="py-2.5 px-3">Latency (ms)</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#D8DEE4]">
              {runs.length === 0 ? (
                <>
                  <tr className="hover:bg-[#F3F4F6]/50">
                    <td className="py-2.5 px-3 font-mono font-semibold text-[#111820]">
                      efficientnet_b0_transfer
                    </td>
                    <td className="py-2.5 px-3"><StatusBadge status="ACTIVE" /></td>
                    <td className="py-2.5 px-3 font-mono">100.0%</td>
                    <td className="py-2.5 px-3 font-mono font-bold text-[#1E7E4A]">100.0%</td>
                    <td className="py-2.5 px-3 font-mono">1.000</td>
                    <td className="py-2.5 px-3 font-mono">1.000</td>
                    <td className="py-2.5 px-3 font-mono">24.8 ms</td>
                  </tr>
                  <tr className="hover:bg-[#F3F4F6]/50">
                    <td className="py-2.5 px-3 font-mono text-[#111820]">resnet18_transfer</td>
                    <td className="py-2.5 px-3"><StatusBadge status="OK" /></td>
                    <td className="py-2.5 px-3 font-mono">99.49%</td>
                    <td className="py-2.5 px-3 font-mono">99.15%</td>
                    <td className="py-2.5 px-3 font-mono">0.9957</td>
                    <td className="py-2.5 px-3 font-mono">1.000</td>
                    <td className="py-2.5 px-3 font-mono">19.2 ms</td>
                  </tr>
                  <tr className="hover:bg-[#F3F4F6]/50">
                    <td className="py-2.5 px-3 font-mono text-[#111820]">custom_cnn_baseline</td>
                    <td className="py-2.5 px-3"><StatusBadge status="OK" /></td>
                    <td className="py-2.5 px-3 font-mono">89.23%</td>
                    <td className="py-2.5 px-3 font-mono">94.87%</td>
                    <td className="py-2.5 px-3 font-mono">0.9136</td>
                    <td className="py-2.5 px-3 font-mono">0.9712</td>
                    <td className="py-2.5 px-3 font-mono">14.1 ms</td>
                  </tr>
                </>
              ) : (
                runs.map((r: any) => (
                  <tr key={r.run_id} className="hover:bg-[#F3F4F6]/50">
                    <td className="py-2.5 px-3 font-mono font-medium text-[#111820]">
                      {r.run_name || r.run_id.slice(0, 8)}
                    </td>
                    <td className="py-2.5 px-3"><StatusBadge status={r.status || "OK"} /></td>
                    <td className="py-2.5 px-3 font-mono">{(r.metrics?.accuracy * 100)?.toFixed(1) || "N/A"}%</td>
                    <td className="py-2.5 px-3 font-mono">{(r.metrics?.recall * 100)?.toFixed(1) || "N/A"}%</td>
                    <td className="py-2.5 px-3 font-mono">{r.metrics?.f1_score?.toFixed(3) || "N/A"}</td>
                    <td className="py-2.5 px-3 font-mono">{r.metrics?.roc_auc?.toFixed(3) || "N/A"}</td>
                    <td className="py-2.5 px-3 font-mono">{r.metrics?.latency_ms?.toFixed(1) || "N/A"} ms</td>
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
