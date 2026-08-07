import DashboardLayout from "../layouts/DashboardLayout";

import MetricsGrid from "../components/dashboard/MetricsGrid";
import AIBrain from "../components/dashboard/AIBrain";
import IncidentFeed from "../components/dashboard/IncidentFeed";
import TelemetryChart from "../components/dashboard/TelemetryChart";

export default function DashboardPage() {
  return (
    <DashboardLayout>
      <div className="space-y-8">
        <div>
          <h1 className="text-5xl font-bold text-white">
            Sentinel Mission Control
          </h1>

          <p className="mt-2 text-lg text-slate-400">
            Enterprise Autonomous Infrastructure Monitoring Platform
          </p>
        </div>

        <MetricsGrid />

        <div className="grid gap-8 lg:grid-cols-2">
          <AIBrain />
          <IncidentFeed />
        </div>

        {/* Live Telemetry Chart */}
        <TelemetryChart />
      </div>
    </DashboardLayout>
  );
}