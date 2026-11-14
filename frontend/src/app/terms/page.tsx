import Link from 'next/link';
import { FileText } from 'lucide-react';

export default function TermsPage() {
  return (
    <div className="max-w-4xl mx-auto space-y-8 py-8 px-4 text-slate-300">
      <div className="flex items-center space-x-3 border-b border-slate-800 pb-4">
        <FileText className="w-8 h-8 text-blue-500" />
        <div>
          <h1 className="text-2xl font-bold text-white tracking-tight">Terms of Use</h1>
          <p className="text-sm text-slate-400">VisionQC Automated Quality Control Operations</p>
        </div>
      </div>

      <div className="space-y-6 text-sm leading-relaxed">
        <section className="space-y-2">
          <h2 className="text-base font-semibold text-white">1. Authorized Operational Scope</h2>
          <p>
            VisionQC provides automated defect inspection and machine learning lifecycle management. Decisions generated
            by the platform (ACCEPT / REJECT) are calibrated against verified quality gates but should be audited periodically
            by certified quality engineering personnel.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-base font-semibold text-white">2. Quality Gates & Model Promotion</h2>
          <p>
            Automated retraining DAGs enforce strict quality gates (Defect Recall &ge; 95.0%, False Negative Rate &le; 5.0%).
            Promotion to the production serving tier is strictly gated by compliance evaluation.
          </p>
        </section>

        <section className="space-y-2">
          <h2 className="text-base font-semibold text-white">3. System Integrity & Safety</h2>
          <p>
            Operators are responsible for maintaining calibration of physical industrial cameras and environmental lighting
            to preserve feature distribution integrity and avoid induced data drift.
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
