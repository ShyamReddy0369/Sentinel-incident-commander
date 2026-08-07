import { Bell, Search } from "lucide-react";

export default function Header() {
  return (
    <header className="flex h-20 items-center justify-between border-b border-slate-800 bg-[#0B1120] px-8">
      <div>
        <h2 className="text-2xl font-bold">
          Mission Control
        </h2>

        <p className="text-slate-400">
          Enterprise Autonomous AI Operations
        </p>
      </div>

      <div className="flex items-center gap-4">
        <div className="flex items-center gap-2 rounded-xl bg-slate-900 px-4 py-2">
          <Search size={18} />

          <input
            placeholder="Search..."
            className="bg-transparent outline-none"
          />
        </div>

        <Bell size={22} />

        <div className="flex items-center gap-2 rounded-full bg-green-500/20 px-4 py-2">
          <div className="h-3 w-3 animate-pulse rounded-full bg-green-500" />

          <span className="text-green-400 font-semibold">
            LIVE
          </span>
        </div>
      </div>
    </header>
  );
}