import type { DashboardSummary } from '../types';

export const getDashboardSummary = (): DashboardSummary => ({
  title: 'Sentinel Mission Control',
  subtitle: 'A clear operating view for incidents, diagnostics, and recovery.',
  cards: [
    {
      title: 'Active incidents',
      description: 'Monitor open incidents and escalations in real time.',
      accent: 'from-cyan-500 to-blue-500',
    },
    {
      title: 'Response health',
      description: 'Track remediation progress and system readiness.',
      accent: 'from-fuchsia-500 to-violet-500',
    },
    {
      title: 'Automation status',
      description: 'Review scheduled chaos tests and recovery actions.',
      accent: 'from-emerald-500 to-lime-500',
    },
  ],
});
