import {
  AlertTriangle,
  CheckCircle2,
  ShieldAlert,
} from "lucide-react";

const incidents = [
  {
    service: "Authentication Service",
    severity: "CRITICAL",
    color: "text-red-500",
    icon: ShieldAlert,
  },
  {
    service: "Payment Service",
    severity: "WARNING",
    color: "text-yellow-400",
    icon: AlertTriangle,
  },
  {
    service: "Inventory Service",
    severity: "RESOLVED",
    color: "text-green-500",
    icon: CheckCircle2,
  },
];

export default function IncidentFeed() {
  return (
    <div className="rounded-2xl border border-slate-800 bg-[#111827] p-6 shadow-xl">
      <h2 className="mb-6 text-2xl font-bold">
        Live Incident Feed
      </h2>

      <div className="space-y-4">

        {incidents.map((incident) => {
          const Icon = incident.icon;

          return (
            <div
              key={incident.service}
              className="flex items-center justify-between rounded-xl bg-slate-900 p-4"
            >
              <div className="flex items-center gap-3">
                <Icon
                  className={incident.color}
                  size={22}
                />

                <div>
                  <h3 className="font-semibold">
                    {incident.service}
                  </h3>

                  <p className={incident.color}>
                    {incident.severity}
                  </p>
                </div>
              </div>
            </div>
          );
        })}

      </div>
    </div>
  );
}