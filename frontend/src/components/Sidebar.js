import React from 'react';

export default function Sidebar({ activeTab, setActiveTab }) {
  const menuItems = [
    { id: 'dashboard', label: '📊 Executive Dashboard', module: 'Mod 10' },
    { id: 'monitoring', label: '📡 Live Stream Monitor', module: 'Mod 3' },
    { id: 'baselines', label: '🧬 UEBA Baselines', module: 'Mod 4 & 8' },
    { id: 'alerts', label: '🚨 Incident Alerts', module: 'Mod 5, 6 & 9' },
    { id: 'investigate', label: '🔍 Investigation Console', module: 'Mod 7' },
    { id: 'reports', label: '📄 Reports & Exports', module: 'Mod 12' },
  ];

  return (
    <aside style={{ width: '250px', backgroundColor: '#0f172a', borderRight: '1px solid #1e293b', padding: '16px', color: '#cbd5e1', minHeight: '100vh' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '30px' }}>
        <div style={{ fontSize: '24px' }}>🛡️</div>
        <div>
          <h2 style={{ fontSize: '14px', margin: 0, color: '#fff' }}>UEBA Intelligence</h2>
          <p style={{ fontSize: '10px', margin: 0, color: '#94a3b8' }}>Insider Threat Platform</p>
        </div>
      </div>

      <nav style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
        {menuItems.map((item) => (
          <button
            key={item.id}
            onClick={() => setActiveTab(item.id)}
            style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '10px 12px',
              borderRadius: '8px',
              border: activeTab === item.id ? '1px solid #06b6d4' : '1px solid transparent',
              backgroundColor: activeTab === item.id ? '#083344' : 'transparent',
              color: activeTab === item.id ? '#38bdf8' : '#94a3b8',
              cursor: 'pointer',
              textAlign: 'left'
            }}
          >
            <span style={{ fontSize: '12px', fontWeight: '500' }}>{item.label}</span>
            <span style={{ fontSize: '9px', background: '#1e293b', padding: '2px 6px', borderRadius: '4px', color: '#64748b' }}>
              {item.module}
            </span>
          </button>
        ))}
      </nav>
    </aside>
  );
}