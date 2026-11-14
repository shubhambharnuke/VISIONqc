"use client";

import React, { useEffect, useState } from "react";
import { Database, GitBranch, HardDrive, CheckCircle2 } from "lucide-react";
import { Card, StatusBadge } from "@/components/ui";
import { fetchDatasets } from "@/lib/api";

export default function DatasetsPage() {
  const [datasets, setDatasets] = useState<any[]>([]);

  useEffect(() => {
    fetchDatasets()
      .then((data) => setDatasets(data))
      .catch(() => setDatasets([]));
  }, []);

  return (
    <div className="space-y-6">
      <div className="border-b border-[#D8DEE4] pb-4">
        <h1 className="text-2xl font-bold tracking-tight text-[#111820]">Dataset Management & DVC</h1>
        <p className="text-sm text-[#627282] mt-0.5">
          Version-controlled manufacturing data with immutable SHA-256 hashes and DVC tracking.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card title="Tracked Version">
          <div className="text-lg font-mono font-bold text-[#111820]">dataset-v1.0</div>
          <div className="text-xs text-[#627282] mt-1">DVC pointer: ml/data/raw.dvc</div>
        </Card>
        <Card title="Total Images">
          <div className="text-lg font-mono font-bold text-[#111820]">1,300 Samples</div>
          <div className="text-xs text-[#627282] mt-1">519 OK | 781 DEFECTIVE</div>
        </Card>
        <Card title="Split Strategy">
          <div className="text-lg font-mono font-bold text-[#111820]">70 / 15 / 15 Stratified</div>
          <div className="text-xs text-[#627282] mt-1">Seed: 42 | Zero Cross-Leakage</div>
        </Card>
      </div>

      <Card title="Dataset Partition Details">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="border-b border-[#D8DEE4] bg-[#F3F4F6] text-[#627282] uppercase tracking-wider font-mono">
                <th className="py-2.5 px-3">Split</th>
                <th className="py-2.5 px-3">Total Images</th>
                <th className="py-2.5 px-3">OK Images</th>
                <th className="py-2.5 px-3">DEFECTIVE Images</th>
                <th className="py-2.5 px-3">Defect Ratio</th>
                <th className="py-2.5 px-3">Augmentation</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#D8DEE4] font-mono">
              <tr className="hover:bg-[#F3F4F6]/50">
                <td className="py-2.5 px-3 font-semibold text-[#111820]">Train (70%)</td>
                <td className="py-2.5 px-3">910</td>
                <td className="py-2.5 px-3">363</td>
                <td className="py-2.5 px-3">547</td>
                <td className="py-2.5 px-3">60.1%</td>
                <td className="py-2.5 px-3 text-[#1E7E4A]">Active (Flips, Rotations, Jitter)</td>
              </tr>
              <tr className="hover:bg-[#F3F4F6]/50">
                <td className="py-2.5 px-3 font-semibold text-[#111820]">Validation (15%)</td>
                <td className="py-2.5 px-3">195</td>
                <td className="py-2.5 px-3">78</td>
                <td className="py-2.5 px-3">117</td>
                <td className="py-2.5 px-3">60.0%</td>
                <td className="py-2.5 px-3 text-[#627282]">None (Strict Canonical)</td>
              </tr>
              <tr className="hover:bg-[#F3F4F6]/50">
                <td className="py-2.5 px-3 font-semibold text-[#111820]">Test (15%)</td>
                <td className="py-2.5 px-3">195</td>
                <td className="py-2.5 px-3">78</td>
                <td className="py-2.5 px-3">117</td>
                <td className="py-2.5 px-3">60.0%</td>
                <td className="py-2.5 px-3 text-[#627282]">None (Holdout Final Evaluation)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </Card>
    </div>
  );
}
