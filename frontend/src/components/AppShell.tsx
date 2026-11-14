"use client";

import React, { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  Activity,
  Layers,
  FlaskConical,
  Database,
  GitBranch,
  ShieldAlert,
  BarChart3,
  RefreshCw,
  FileText,
  Menu,
  X,
} from "lucide-react";
import { cn } from "@/lib/utils";

const NAV_ITEMS = [
  { name: "Overview", href: "/", icon: Activity },
  { name: "Inspection Workbench", href: "/inspection", icon: Layers },
  { name: "Experiments", href: "/experiments", icon: FlaskConical },
  { name: "Datasets", href: "/datasets", icon: Database },
  { name: "Pipelines", href: "/pipelines", icon: GitBranch },
  { name: "Model Registry", href: "/registry", icon: ShieldAlert },
  { name: "Monitoring", href: "/monitoring", icon: BarChart3 },
  { name: "Retraining", href: "/retraining", icon: RefreshCw },
  { name: "Documentation", href: "/docs", icon: FileText },
];

export const AppShell: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const pathname = usePathname();
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="min-h-screen flex flex-col bg-[#F3F4F6] text-[#111820]">
      {/* Top Application Header */}
      <header className="h-14 bg-[#202A35] text-white flex items-center justify-between px-4 border-b border-[#111820] z-20">
        <div className="flex items-center gap-3">
          <button
            onClick={() => setSidebarOpen(!sidebarOpen)}
            className="md:hidden p-1.5 rounded hover:bg-[#111820] text-gray-300"
            aria-label="Toggle Navigation"
          >
            {sidebarOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
          <div className="flex items-baseline gap-2">
            <span className="font-bold tracking-tight text-lg font-mono text-white">VISIONqc</span>
            <span className="text-xs uppercase px-1.5 py-0.5 rounded bg-[#476985] text-white font-mono">
              v1.0.0
            </span>
          </div>
          <span className="hidden sm:inline text-xs text-[#8BA4B8] border-l border-gray-600 pl-3">
            Industrial Impeller Defect Inspection & MLOps Platform
          </span>
        </div>

        <div className="flex items-center gap-3 font-mono text-xs">
          <span className="flex items-center gap-1.5 px-2 py-1 rounded bg-[#111820] text-[#1E7E4A]">
            <span className="w-2 h-2 rounded-full bg-[#1E7E4A] animate-pulse" />
            OPERATIONAL
          </span>
        </div>
      </header>

      {/* Main Container: Sidebar + Content */}
      <div className="flex-1 flex overflow-hidden">
        {/* Navigation Sidebar */}
        <aside
          className={cn(
            "fixed inset-y-14 left-0 z-10 w-64 bg-[#202A35] border-r border-[#111820] text-gray-200 transform transition-transform duration-150 ease-in-out md:translate-x-0 md:static md:h-[calc(100vh-3.5rem)]",
            sidebarOpen ? "translate-x-0" : "-translate-x-full"
          )}
        >
          <div className="p-3 text-[10px] uppercase font-semibold text-[#8BA4B8] tracking-wider">
            Station Navigation
          </div>
          <nav className="space-y-0.5 px-2">
            {NAV_ITEMS.map((item) => {
              const Icon = item.icon;
              const isActive = pathname === item.href;
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  onClick={() => setSidebarOpen(false)}
                  className={cn(
                    "flex items-center gap-3 px-3 py-2 rounded text-xs font-medium transition-colors",
                    isActive
                      ? "bg-[#476985] text-white"
                      : "text-gray-300 hover:bg-[#111820] hover:text-white"
                  )}
                >
                  <Icon size={16} className={isActive ? "text-white" : "text-[#8BA4B8]"} />
                  {item.name}
                </Link>
              );
            })}
          </nav>

          <div className="absolute bottom-4 left-4 right-4 p-3 bg-[#111820] rounded border border-gray-700 text-[11px] text-[#8BA4B8] font-mono">
            <div>CHAMPION MODEL</div>
            <div className="text-white font-semibold">EfficientNet-B0</div>
            <div className="text-[10px] text-gray-400 mt-1">Defect Recall: 100% | Latency: 24.8ms</div>
          </div>
        </aside>

        {/* Content Viewport */}
        <main className="flex-1 overflow-y-auto p-6 md:p-8 bg-[#F3F4F6]">
          <div className="max-w-7xl mx-auto space-y-6">{children}</div>
        </main>
      </div>
    </div>
  );
};
