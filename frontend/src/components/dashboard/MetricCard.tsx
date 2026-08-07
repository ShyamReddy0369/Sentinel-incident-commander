import type { LucideIcon } from "lucide-react";

interface MetricCardProps {
  title: string;
  value: string;
  subtitle: string;
  icon: LucideIcon;
  color: string;
}

export default function MetricCard({
  title,
  value,
  subtitle,
  icon: Icon,
  color,
}: MetricCardProps) {
  return (
    <div
      className="rounded-2xl border border-slate-800 bg-[#111827] p-6 shadow-xl"
    >
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm uppercase tracking-wider text-slate-400">
            {title}
          </p>

          <h2 className="mt-3 text-4xl font-bold text-white">
            {value}
          </h2>

          <p className="mt-2 text-sm text-slate-500">
            {subtitle}
          </p>
        </div>

        <div
          className="flex h-14 w-14 items-center justify-center rounded-xl"
          style={{ backgroundColor: color }}
        >
          <Icon size={28} color="white" />
        </div>
      </div>
    </div>
  );
}