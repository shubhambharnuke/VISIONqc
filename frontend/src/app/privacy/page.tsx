import Link from 'next/link';
import { ShieldCheck } from 'lucide-react';

export default function PrivacyPage() {
  return (
    <div className="max-w-4xl mx-auto space-y-8 py-8 px-4 text-slate-300">
      <div className="flex items-center space-x-3 border-b border-slate-800 pb-4">
        <ShieldCheck className="w-8 h-8 text-blue-500" />
        <div>
          <h1 className="text-2xl font-bold text-white tracking-tight">Privacy Policy</h1>
          <p className="text-sm text-slate-400">VisionQC Manufacturing Quality Assurance Platform</p>
        </div>
      </div>

      <div className="space-y-6 text-sm leading-relaxed">
        <section className="space-y-2">
          <h2 className="text-base font-semibold text-white">1. Data Collection & Processing</h2>
          <p>
            VisionQC operates within an industrial edge environment. Visual inspection images (pump impeller castings)
            and inference telemetry are processed locally on premises for defect detection and statistical drift monitoring.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-base font-semibold text-white">2. Storage & Governance</h2>
          <p>
            Inspection logs, confidence metrics, and Grad-CAM heatmaps are persisted in internal operational storage (PostgreSQL).
            No telemetry or industrial image assets are transmitted to external third-party services without explicit organizational consent.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-base font-semibold text-white">3. Contact & Compliance</h2>
          <p>
            For compliance inquiries and audit logs, contact the system administrator or quality engineering team.
          </p>
        </section>
      </div>

      <div className="pt-6 border-t border-slate-800">
        <Link href="/" className="text-xs text-blue-400 hover:underline">
          &larr; Return to Overview
        </Link>
      </div>
    </div>
  );
}
