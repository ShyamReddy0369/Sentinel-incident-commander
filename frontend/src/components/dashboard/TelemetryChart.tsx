import {
  LineChart,
  Line,
  XAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

const data = [
  { time: "10:00", cpu: 35 },
  { time: "10:05", cpu: 42 },
  { time: "10:10", cpu: 38 },
  { time: "10:15", cpu: 61 },
  { time: "10:20", cpu: 55 },
  { time: "10:25", cpu: 73 },
  { time: "10:30", cpu: 58 },
];

export default function TelemetryChart() {
  return (
    <div className="rounded-2xl border border-slate-800 bg-[#111827] p-6 shadow-xl">
      <h2 className="mb-6 text-2xl font-bold text-white">
        Live CPU Telemetry
      </h2>

      <div className="h-80">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <CartesianGrid stroke="#334155" strokeDasharray="3 3" />

            <XAxis
              dataKey="time"
              stroke="#94A3B8"
            />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="cpu"
              stroke="#06B6D4"
              strokeWidth={4}
              dot={{ r: 4 }}
              activeDot={{ r: 8 }}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}