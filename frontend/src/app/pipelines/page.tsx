"use client";

import React, { useEffect, useState } from "react";
import { GitBranch, Play, CheckCircle2, AlertTriangle, Clock } from "lucide-react";
import { Card, Button, StatusBadge } from "@/components/ui";
import { fetchPipelines } from "@/lib/api";

export default function PipelinesPage() {
  const [pipelines, setPipelines] = useState<any[]>([]);

  useEffect(() => {
    fetchPipelines()
      .then((data) => setPipelines(data))
      .catch(() => setPipelines([]));
  }, []);

  return (
    <div className="space-y-6">
      <div className="border-b border-[#D8DEE4] pb-4">
        <h1 className="text-2xl font-bold tracking-tight text-[#111820]">Airflow Orchestration Pipelines</h1>
        <p className="text-sm text-[#627282] mt-0.5">
          Automated DAGs for model training, scheduled retraining, quality-gate enforcement, and deployment.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card title="Training DAG (visionqc_training_pipeline)">
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-sm font-mono font-bold text-[#111820]">visionqc_training_pipeline</span>
              <StatusBadge status="ACTIVE" />
            </div>
            <p className="text-xs text-[#627282]">
              Triggered on new DVC commits or manual dispatch. Runs data validation, preprocessing, candidate training, evaluation, and quality gate check.
            </p>
            <div className="text-xs font-mono bg-[#F3F4F6] p-2.5 rounded border border-[#D8DEE4] space-y-1">
              <div>Schedule: Manual / Webhook</div>
              <div>Quality Gate: Recall ≥ 0.95, Acc ≥ 0.90, FNR ≤ 0.05</div>
              <div>Tasks: 6 sequential steps</div>
            </div>
          </div>
        </Card>

        <Card title="Retraining DAG (visionqc_retraining_pipeline)">
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-sm font-mono font-bold text-[#111820]">visionqc_retraining_pipeline</span>
              <StatusBadge status="ACTIVE" />
            </div>
            <p className="text-xs text-[#627282]">
              Triggered upon drift detection alert or scheduled intervals. Evaluates candidate models against production champion before promoting.
            </p>
            <div className="text-xs font-mono bg-[#F3F4F6] p-2.5 rounded border border-[#D8DEE4] space-y-1">
              <div>Schedule: @weekly or Drift Event</div>
              <div>Promotion: Automatic if Champion Outperformed</div>
              <div>Safety Rollback: Preserved previous version</div>
            </div>
          </div>
        </Card>
      </div>

      <Card title="Pipeline Execution Stages">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse font-mono">
            <thead>
              <tr className="border-b border-[#D8DEE4] bg-[#F3F4F6] text-[#627282] uppercase tracking-wider">
                <th className="py-2.5 px-3">Step Index</th>
                <th className="py-2.5 px-3">Task Name</th>
                <th className="py-2.5 px-3">Operator</th>
                <th className="py-2.5 px-3">Status</th>
                <th className="py-2.5 px-3">Artifact Produced</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#D8DEE4]">
              <tr className="hover:bg-[#F3F4F6]/50">
                <td className="py-2.5 px-3">01</td>
                <td className="py-2.5 px-3 font-semibold text-[#111820]">validate_dataset</td>
                <td className="py-2.5 px-3">PythonOperator</td>
                <td className="py-2.5 px-3"><StatusBadge status="OK" /></td>
                <td className="py-2.5 px-3">docs/dataset_validation_report.json</td>
              </tr>
              <tr className="hover:bg-[#F3F4F6]/50">
                <td className="py-2.5 px-3">02</td>
                <td className="py-2.5 px-3 font-semibold text-[#111820]">split_dataset</td>
                <td className="py-2.5 px-3">PythonOperator</td>
                <td className="py-2.5 px-3"><StatusBadge status="OK" /></td>
                <td className="py-2.5 px-3">docs/split_metadata.json</td>
              </tr>
              <tr className="hover:bg-[#F3F4F6]/50">
                <td className="py-2.5 px-3">03</td>
                <td className="py-2.5 px-3 font-semibold text-[#111820]">train_candidate</td>
                <td className="py-2.5 px-3">PythonOperator</td>
                <td className="py-2.5 px-3"><StatusBadge status="OK" /></td>
                <td className="py-2.5 px-3">ml/models/saved/efficientnet_b0.pth</td>
              </tr>
              <tr className="hover:bg-[#F3F4F6]/50">
                <td className="py-2.5 px-3">04</td>
                <td className="py-2.5 px-3 font-semibold text-[#111820]">evaluate_model</td>
                <td className="py-2.5 px-3">PythonOperator</td>
                <td className="py-2.5 px-3"><StatusBadge status="OK" /></td>
                <td className="py-2.5 px-3">docs/evaluation/model_comparison_report.json</td>
              </tr>
              <tr className="hover:bg-[#F3F4F6]/50">
                <td className="py-2.5 px-3">05</td>
                <td className="py-2.5 px-3 font-semibold text-[#111820]">enforce_quality_gate</td>
                <td className="py-2.5 px-3">BranchPythonOperator</td>
                <td className="py-2.5 px-3"><StatusBadge status="OK" /></td>
                <td className="py-2.5 px-3">Quality Gate Decision: PASSED</td>
              </tr>
              <tr className="hover:bg-[#F3F4F6]/50">
                <td className="py-2.5 px-3">06</td>
                <td className="py-2.5 px-3 font-semibold text-[#111820]">register_model</td>
                <td className="py-2.5 px-3">PythonOperator</td>
                <td className="py-2.5 px-3"><StatusBadge status="OK" /></td>
                <td className="py-2.5 px-3">MLflow Registry: Production v1</td>
              </tr>
            </tbody>
          </table>
        </div>
      </Card>
    </div>
  );
}
