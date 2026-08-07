import { useMemo } from 'react';
import { getDashboardSummary } from '../services/incidentService';

export const useDashboard = () => useMemo(() => getDashboardSummary(), []);
