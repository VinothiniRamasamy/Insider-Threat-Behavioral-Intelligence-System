import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import LoginPage from './components/LoginPage';
import DashboardPage from './pages/DashboardPage';
import LiveMonitoringPage from './pages/LiveMonitoringPage';
import BehavioralProfilingPage from './pages/BehavioralProfilingPage';
import ThreatAlertsPage from './pages/ThreatAlertsPage';
import InvestigationPage from './pages/InvestigationPage';
import ReportsPage from './pages/ReportsPage';

export default function App() {
  const [user, setUser] = useState(null);
  const [activeTab, setActiveTab] = useState('dashboard');
  const [selectedUser, setSelectedUser] = useState('AAE0190');

  if (!user) {
    return <LoginPage onLogin={(userData) => setUser(userData)} />;
  }

  const renderPage = () => {
    switch (activeTab) {
      case 'dashboard':
        return <DashboardPage setActiveTab={setActiveTab} />;
      case 'monitoring':
        return <LiveMonitoringPage setSelectedUser={setSelectedUser} setActiveTab={setActiveTab} />;
      case 'baselines':
        return <BehavioralProfilingPage />;
      case 'alerts':
        return <ThreatAlertsPage setSelectedUser={setSelectedUser} setActiveTab={setActiveTab} />;
      case 'investigate':
        return <InvestigationPage selectedUser={selectedUser} />;
      case 'reports':
        return <ReportsPage />;
      default:
        return <DashboardPage setActiveTab={setActiveTab} />;
    }
  };

  return (
    <div style={{ display: 'flex', backgroundColor: '#020617', minHeight: '100vh', fontFamily: 'sans-serif' }}>
      <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />
      <main style={{ flex: 1, padding: '24px', overflowY: 'auto' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', borderBottom: '1px solid #1e293b', paddingBottom: '12px' }}>
          <span style={{ fontSize: '12px', color: '#94a3b8' }}>Session Active: <strong style={{ color: '#38bdf8' }}>{user.email}</strong> ({user.role})</span>
          <button 
            onClick={() => setUser(null)} 
            style={{ background: '#334155', border: 'none', color: '#fff', padding: '6px 12px', borderRadius: '4px', fontSize: '11px', cursor: 'pointer' }}
          >
            Logout
          </button>
        </div>
        {renderPage()}
      </main>
    </div>
  );
}