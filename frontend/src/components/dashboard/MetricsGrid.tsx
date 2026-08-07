import {
  Activity,
  BrainCircuit,
  Cpu,
  ShieldAlert,
} from "lucide-react";

import MetricCard from "./MetricCard";

const metrics = [
  {
    title: "CPU Usage",
    value: "34%",
    subtitle: "Healthy",
    icon: Cpu,
    color: "#2563EB",
  },
  {
    title: "Memory",
    value: "62%",
    subtitle: "Normal",
    icon: Activity,
    color: "#16A34A",
  },
  {
    title: "Incidents",
    value: "03",
    subtitle: "1 Critical",
    icon: ShieldAlert,
    color: "#DC2626",
  },
  {
    title: "AI Agents",
    value: "05",
    subtitle: "All Online",
    icon: BrainCircuit,
    color: "#7C3AED",
  },
];

export default function MetricsGrid() {
  return (
    <section className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {metrics.map((metric) => (
        <MetricCard
          key={metric.title}
          title={metric.title}
          value={metric.value}
          subtitle={metric.subtitle}
          icon={metric.icon}
          color={metric.color}
        />
      ))}
    </section>
  );
}