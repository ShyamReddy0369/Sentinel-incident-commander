import { BrainCircuit, CheckCircle2 } from "lucide-react";
import { motion } from "framer-motion";

export default function AIBrain() {
  return (
    <motion.div
      whileHover={{ scale: 1.01 }}
      className="rounded-2xl border border-slate-800 bg-[#111827] p-6 shadow-xl"
    >
      <div className="mb-6 flex items-center gap-3">
        <BrainCircuit className="text-cyan-400" size={30} />

        <div>
          <h2 className="text-2xl font-bold">
            Sentinel AI Brain
          </h2>

          <p className="text-slate-400">
            Autonomous Diagnosis Engine
          </p>
        </div>
      </div>

      <div className="space-y-6">

        <div>
          <p className="text-sm text-slate-400">
            Root Cause
          </p>

          <p className="mt-2 text-lg font-semibold text-red-400">
            CPU Spike detected in Authentication Service
          </p>
        </div>

        <div>
          <p className="text-sm text-slate-400">
            Confidence
          </p>

          <h3 className="mt-2 text-4xl font-bold text-cyan-400">
            98%
          </h3>
        </div>

        <div>
          <p className="text-sm text-slate-400">
            Recommendation
          </p>

          <div className="mt-3 flex items-start gap-3 rounded-xl bg-slate-900 p-4">
            <CheckCircle2
              className="mt-1 text-green-500"
              size={20}
            />

            <span className="text-slate-300">
              Restart Authentication Service and
              monitor CPU usage for 5 minutes.
            </span>
          </div>
        </div>

      </div>
    </motion.div>
  );
}