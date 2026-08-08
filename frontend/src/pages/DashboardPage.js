import React, { useEffect, useState } from 'react';

export default function DashboardPage({ setActiveTab }) {
  const [stats, setStats] = useState({
    total_monitored_users: 1000,
    processed_events: 45995,
    active_alerts: 12,
    threat_breakdown: { critical: 1, high: 3, medium: 5, low: 3 }
  });

  useEffect(() => {
    fetch('http://localhost:8000/api/dashboard/stats')
      .then(res => res.json())
      .then(data => {
        if (data) setStats(data);
      })
      .catch(err => console.log(err));
  }, []);

  return (
    <div style={{ color: '#fff' }}>
      <h2 style={{ fontSize: '18px', marginBottom: '16px' }}>📊 Executive Dashboard (Module 10)</h2>
      
      {/* Metric Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '16px', marginBottom: '24px' }}>
        <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', padding: '16px', borderRadius: '8px' }}>
          <span style={{ fontSize: '11px', color: '#94a3b8' }}>Monitored Users</span>
          <p style={{ fontSize: '24px', fontWeight: 'bold', margin: '8px 0 0 0', color: '#38bdf8' }}>
            {stats?.total_monitored_users ?? 1000}
          </p>
        </div>
        <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', padding: '16px', borderRadius: '8px' }}>
          <span style={{ fontSize: '11px', color: '#94a3b8' }}>Total Processed Events</span>
          <p style={{ fontSize: '24px', fontWeight: 'bold', margin: '8px 0 0 0', color: '#38bdf8' }}>
            {stats?.processed_events ?? 45995}
          </p>
        </div>
        <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', padding: '16px', borderRadius: '8px' }}>
          <span style={{ fontSize: '11px', color: '#94a3b8' }}>Active Threat Alerts</span>
          <p style={{ fontSize: '24px', fontWeight: 'bold', margin: '8px 0 0 0', color: '#f97316' }}>
            {stats?.active_alerts ?? 12}
          </p>
        </div>
        <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', padding: '16px', borderRadius: '8px' }}>
          <span style={{ fontSize: '11px', color: '#94a3b8' }}>Critical Incidents</span>
          <p style={{ fontSize: '24px', fontWeight: 'bold', margin: '8px 0 0 0', color: '#ef4444' }}>
            {stats?.threat_breakdown?.critical ?? 0}
          </p>
        </div>
      </div>

      {/* Quick Action Banner */}
      <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', padding: '20px', borderRadius: '8px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h3 style={{ margin: '0 0 6px 0', fontSize: '14px', color: '#fff' }}>Real-time Threat Monitoring active</h3>
          <p style={{ margin: 0, fontSize: '12px', color: '#94a3b8' }}>Streaming event logs and calculating UEBA risk scores in real-time.</p>
        </div>
        <button 
          onClick={() => setActiveTab('monitoring')}
          style={{ backgroundColor: '#0284c7', border: 'none', color: '#fff', padding: '10px 16px', borderRadius: '6px', cursor: 'pointer', fontSize: '12px', fontWeight: 'bold' }}
        >
          View Live Stream 📡
        </button>
      </div>
    </div>
  );
}