"use client";

import React, { useState, useRef } from "react";
import Image from "next/image";
import { UploadCloud, CheckCircle2, XCircle, AlertCircle, Eye } from "lucide-react";
import { Card, Button, StatusBadge } from "@/components/ui";
import { predictImpeller, InspectionPrediction } from "@/lib/api";

type ViewMode = "original" | "heatmap" | "overlay";

export default function InspectionPage() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [prediction, setPrediction] = useState<InspectionPrediction | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [viewMode, setViewMode] = useState<ViewMode>("overlay");
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0];
      setSelectedFile(file);
      setPreviewUrl(URL.createObjectURL(file));
      setPrediction(null);
      setError(null);
    }
  };

  const handleInspect = async () => {
    if (!selectedFile) return;
    setLoading(true);
    setError(null);

    try {
      const result = await predictImpeller(selectedFile, true);
      setPrediction(result);
    } catch (err: any) {
      setError(err.message || "Failed to inspect image");
    } finally {
      setLoading(false);
    }
  };

  const getActiveImageUrl = () => {
    if (!prediction?.gradcam_urls) return previewUrl;
    const apiBase = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

    if (viewMode === "heatmap" && prediction.gradcam_urls.heatmap) {
      return `${apiBase}${prediction.gradcam_urls.heatmap}`;
    }
    if (viewMode === "overlay" && prediction.gradcam_urls.overlay) {
      return `${apiBase}${prediction.gradcam_urls.overlay}`;
    }
    if (viewMode === "original" && prediction.gradcam_urls.original) {
      return `${apiBase}${prediction.gradcam_urls.original}`;
    }
    return previewUrl;
  };

  return (
    <div className="space-y-6">
      {/* Page Title */}
      <div className="border-b border-[#D8DEE4] pb-4">
        <h1 className="text-2xl font-bold tracking-tight text-[#111820]">Inspection Workbench</h1>
        <p className="text-sm text-[#627282] mt-0.5">
          Real-time impeller visual inspection with 3-mode Grad-CAM explainability.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Upload & Controls Column */}
        <div className="lg:col-span-5 space-y-4">
          <Card title="Impeller Image Input">
            <div
              onClick={() => fileInputRef.current?.click()}
              className="border-2 border-dashed border-[#D8DEE4] hover:border-[#476985] rounded p-6 text-center cursor-pointer transition-colors bg-[#F3F4F6]/50"
            >
              <input
                ref={fileInputRef}
                type="file"
                accept="image/jpeg,image/png"
                className="hidden"
                onChange={handleFileChange}
              />
              <UploadCloud size={36} className="mx-auto text-[#627282] mb-2" />
              <div className="text-xs font-medium text-[#111820]">
                {selectedFile ? selectedFile.name : "Click to select or drop an impeller image"}
              </div>
              <div className="text-[11px] text-[#627282] mt-1">
                Supported: JPEG, PNG (512x512 Grayscale / RGB)
              </div>
            </div>

            <div className="mt-4 flex gap-2">
              <Button
                variant="primary"
                className="flex-1"
                disabled={!selectedFile || loading}
                onClick={handleInspect}
              >
                {loading ? "Inspecting & Computing Grad-CAM..." : "Execute Inspection"}
              </Button>
            </div>

            {error && (
              <div className="mt-3 p-3 bg-[#FBEBEB] text-[#B83232] rounded text-xs flex items-center gap-2 border border-[#B83232]/20">
                <AlertCircle size={16} />
                <span>{error}</span>
              </div>
            )}
          </Card>

          {/* Model Verdict Card */}
          {prediction && (
            <Card title="Inspection Verdict">
              <div className="space-y-4">
                <div className="flex items-center justify-between border-b border-[#D8DEE4] pb-3">
                  <div>
                    <div className="text-xs text-[#627282] font-mono">QUALITY DECISION</div>
                    <div className="text-2xl font-bold font-mono tracking-tight mt-0.5">
                      {prediction.decision === "ACCEPT" ? (
                        <span className="text-[#1E7E4A]">ACCEPT</span>
                      ) : (
                        <span className="text-[#B83232]">REJECT</span>
                      )}
                    </div>
                  </div>
                  <StatusBadge status={prediction.predicted_class} />
                </div>

                <div className="grid grid-cols-2 gap-3 text-xs">
                  <div>
                    <span className="text-[#627282] block">Defect Probability</span>
                    <span className="font-mono font-bold text-sm text-[#111820]">
                      {(prediction.defect_probability * 100).toFixed(2)}%
                    </span>
                  </div>
                  <div>
                    <span className="text-[#627282] block">Threshold Applied</span>
                    <span className="font-mono font-bold text-sm text-[#111820]">
                      {(prediction.threshold_applied * 100).toFixed(0)}%
                    </span>
                  </div>
                  <div>
                    <span className="text-[#627282] block">Inference Latency</span>
                    <span className="font-mono font-bold text-sm text-[#111820]">
                      {prediction.inference_latency_ms.toFixed(1)} ms
                    </span>
                  </div>
                  <div>
                    <span className="text-[#627282] block">Serving Model</span>
                    <span className="font-mono font-bold text-sm text-[#111820]">
                      {prediction.model_name}
                    </span>
                  </div>
                </div>
              </div>
            </Card>
          )}
        </div>

        {/* Visual Inspection & Grad-CAM Column */}
        <div className="lg:col-span-7 space-y-4">
          <Card title="Visual Inspection & Explainability">
            {prediction && (
              <div className="flex items-center gap-2 mb-3 border-b border-[#D8DEE4] pb-3">
                <span className="text-xs text-[#627282] font-medium mr-1 flex items-center gap-1">
                  <Eye size={14} /> Grad-CAM View:
                </span>
                {(["original", "heatmap", "overlay"] as ViewMode[]).map((mode) => (
                  <button
                    key={mode}
                    onClick={() => setViewMode(mode)}
                    className={`px-3 py-1 rounded text-xs font-mono uppercase transition-colors ${
                      viewMode === mode
                        ? "bg-[#202A35] text-white font-semibold"
                        : "bg-[#E5E9EE] text-[#111820] hover:bg-[#D8DEE4]"
                    }`}
                  >
                    {mode}
                  </button>
                ))}
              </div>
            )}

            <div className="w-full h-96 bg-[#202A35] rounded flex items-center justify-center overflow-hidden border border-[#D8DEE4] relative">
              {getActiveImageUrl() ? (
                // eslint-disable-next-line @next/next/no-img-element
                <img
                  src={getActiveImageUrl()!}
                  alt="Impeller Inspection"
                  className="max-h-full max-w-full object-contain"
                />
              ) : (
                <div className="text-center text-gray-400 text-xs">
                  Upload an image to inspect
                </div>
              )}
            </div>

            {prediction && (
              <div className="mt-3 text-[11px] text-[#627282] font-mono flex items-center justify-between">
                <span>Prediction ID: {prediction.prediction_id}</span>
                <span>Active Mode: {viewMode.toUpperCase()}</span>
              </div>
            )}
          </Card>
        </div>
      </div>
    </div>
  );
}
