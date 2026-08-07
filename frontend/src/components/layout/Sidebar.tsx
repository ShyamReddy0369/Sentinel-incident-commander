import {
  Activity,
  Brain,
  LayoutDashboard,
  Network,
  Settings,
} from "lucide-react";

const menu = [
  { icon: LayoutDashboard, title: "Dashboard" },
  { icon: Activity, title: "Incidents" },
  { icon: Brain, title: "AI Brain" },
  { icon: Network, title: "Topology" },
  { icon: Settings, title: "Settings" },
];

export default function Sidebar() {
  return (
    <aside className="w-72 border-r border-slate-800 bg-[#0B1120]">
      <div className="border-b border-slate-800 p-8">
        <h1 className="text-3xl font-bold text-cyan-400">
          Sentinel
        </h1>

        <p className="mt-2 text-slate-400">
          Mission Control
        </p>
      </div>

      <nav className="p-4">
        {menu.map((item) => {
          const Icon = item.icon;

          return (
            <button
              key={item.title}
              className="mb-2 flex w-full items-center gap-4 rounded-xl p-4 transition hover:bg-slate-800"
            >
              <Icon size={20} />

              <span>{item.title}</span>
            </button>
          );
        })}
      </nav>
    </aside>
  );
}