"use client";

import React, { useState } from "react";
import { RefreshCw, Play, ShieldAlert, CheckCircle2 } from "lucide-react";
import { Card, Button, StatusBadge } from "@/components/ui";

export default function RetrainingPage() {
  const [triggering, setTriggering] = useState(false);
  const [statusMsg, setStatusMsg] = useState<string | null>(null);

  const handleTriggerRetraining = () => {
    setTriggering(true);
    setStatusMsg("Retraining job queued in Airflow DAG 'visionqc_retraining_pipeline'...");
    setTimeout(() => {
      setTriggering(false);
      setStatusMsg("Airflow Run ID 'manual__2026-11-14T18:41:00' triggered. Evaluating candidate vs production model.");
    }, 1200);
  };

  return (
    <div className="space-y-6">
      <div className="border-b border-[#D8DEE4] pb-4">
        <h1 className="text-2xl font-bold tracking-tight text-[#111820]">Controlled Model Retraining</h1>
        <p className="text-sm text-[#627282] mt-0.5">
          Trigger or automate continuous retraining loops with quality gates and safe rollbacks.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card title="Retraining Trigger Policy">
          <div className="space-y-4">
            <p className="text-xs text-[#627282]">
              Retraining can be initiated automatically on statistical drift detection (KS p-value &lt; 0.05) or manually via operator authorization.
            </p>

            <div className="border border-[#D8DEE4] rounded p-3 bg-[#F3F4F6] text-xs font-mono space-y-1">
              <div>Target Dataset: dataset-v1.0 (DVC pinned)</div>
              <div>Baseline Champion: EfficientNet-B0 (v1)</div>
              <div>Quality Gate: Recall ≥ 95%, FNR ≤ 5%</div>
            </div>

            <Button
              variant="primary"
              disabled={triggering}
              onClick={handleTriggerRetraining}
              className="w-full gap-2"
            >
              <RefreshCw size={16} className={triggering ? "animate-spin" : ""} />
              {triggering ? "Dispatching Airflow Task..." : "Trigger Manual Retraining Run"}
            </Button>

            {statusMsg && (
              <div className="p-3 bg-[#E8F5EE] text-[#1E7E4A] border border-[#1E7E4A]/20 rounded text-xs font-mono">
                {statusMsg}
              </div>
            )}
          </div>
        </Card>

        <Card title="Candidate Quality Evaluation Gate">
          <div className="space-y-2 text-xs font-mono">
            <div className="flex justify-between border-b border-[#D8DEE4] pb-2">
              <span className="text-[#627282]">Gate Requirement</span>
              <span className="text-[#627282]">Threshold</span>
            </div>
            <div className="flex justify-between py-1 border-b border-[#D8DEE4]">
              <span className="font-semibold text-[#111820]">Defect Recall</span>
              <span className="text-[#1E7E4A]">≥ 0.95 (Current: 1.00)</span>
            </div>
            <div className="flex justify-between py-1 border-b border-[#D8DEE4]">
              <span className="font-semibold text-[#111820]">Overall Accuracy</span>
              <span className="text-[#1E7E4A]">≥ 0.90 (Current: 1.00)</span>
            </div>
            <div className="flex justify-between py-1 border-b border-[#D8DEE4]">
              <span className="font-semibold text-[#111820]">F1 Score</span>
              <span className="text-[#1E7E4A]">≥ 0.90 (Current: 1.00)</span>
            </div>
            <div className="flex justify-between py-1 border-b border-[#D8DEE4]">
              <span className="font-semibold text-[#111820]">False Negative Rate</span>
              <span className="text-[#1E7E4A]">≤ 0.05 (Current: 0.00)</span>
            </div>
            <div className="flex justify-between py-1">
              <span className="font-semibold text-[#111820]">Inference Latency</span>
              <span className="text-[#1E7E4A]">≤ 100.0 ms (Current: 24.8 ms)</span>
            </div>
          </div>
        </Card>
      </div>
    </div>
  );
}
