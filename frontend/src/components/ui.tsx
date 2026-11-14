import React from "react";
import { cn } from "@/lib/utils";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "destructive" | "ghost";
  size?: "sm" | "md" | "lg";
}

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = "primary",
  size = "md",
  className,
  ...props
}) => {
  const base = "inline-flex items-center justify-center font-medium rounded transition-colors focus:outline-none focus:ring-2 focus:ring-offset-1 disabled:opacity-50 disabled:cursor-not-allowed";
  
  const sizes = {
    sm: "px-2.5 py-1 text-xs",
    md: "px-4 py-2 text-sm",
    lg: "px-5 py-2.5 text-base",
  };

  const variants = {
    primary: "bg-[#202A35] text-white hover:bg-[#111820] focus:ring-[#476985]",
    secondary: "bg-[#E5E9EE] text-[#111820] border border-[#D8DEE4] hover:bg-[#D8DEE4] focus:ring-[#8BA4B8]",
    destructive: "bg-[#B83232] text-white hover:bg-[#992222] focus:ring-[#B83232]",
    ghost: "bg-transparent text-[#627282] hover:bg-[#E5E9EE] hover:text-[#111820] focus:ring-[#8BA4B8]",
  };

  return (
    <button
      className={cn(base, sizes[size], variants[variant], className)}
      {...props}
    >
      {children}
    </button>
  );
};

export const Card: React.FC<{ children: React.ReactNode; className?: string; title?: string }> = ({
  children,
  className,
  title,
}) => {
  return (
    <div className={cn("bg-white border border-[#D8DEE4] rounded p-5 shadow-xs", className)}>
      {title && (
        <h3 className="text-xs font-semibold uppercase tracking-wider text-[#627282] mb-3">
          {title}
        </h3>
      )}
      {children}
    </div>
  );
};

export const StatusBadge: React.FC<{ status: "OK" | "DEFECTIVE" | "REVIEW" | "RUNNING" | string }> = ({
  status,
}) => {
  const s = status.toUpperCase();
  const styles: Record<string, string> = {
    OK: "bg-[#E8F5EE] text-[#1E7E4A] border-[#1E7E4A]/20",
    ACCEPT: "bg-[#E8F5EE] text-[#1E7E4A] border-[#1E7E4A]/20",
    HEALTHY: "bg-[#E8F5EE] text-[#1E7E4A] border-[#1E7E4A]/20",
    ACTIVE: "bg-[#E8F5EE] text-[#1E7E4A] border-[#1E7E4A]/20",
    DEFECTIVE: "bg-[#FBEBEB] text-[#B83232] border-[#B83232]/20",
    REJECT: "bg-[#FBEBEB] text-[#B83232] border-[#B83232]/20",
    FAILED: "bg-[#FBEBEB] text-[#B83232] border-[#B83232]/20",
    REVIEW: "bg-[#FEF6EB] text-[#C47A15] border-[#C47A15]/20",
    RUNNING: "bg-[#EBF2FE] text-[#2463EB] border-[#2463EB]/20",
  };

  const currentStyle = styles[s] || "bg-[#E5E9EE] text-[#627282] border-[#D8DEE4]";

  return (
    <span className={cn("inline-flex items-center px-2 py-0.5 rounded text-xs font-medium border font-mono tracking-tight", currentStyle)}>
      {s}
    </span>
  );
};
