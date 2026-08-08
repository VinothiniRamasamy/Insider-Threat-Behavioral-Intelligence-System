import React, { useEffect, useState } from 'react';

export default function ThreatAlertsPage({ setSelectedUser, setActiveTab }) {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    // 1. Fetch initial alerts from backend API
    fetch('http://localhost:8000/api/alerts')
      .then(res => res.json())
      .then(data => {
        if (data && data.alerts && data.alerts.length > 0) {
          setAlerts(data.alerts);
        }
      })
      .catch(err => console.log(err));

    // 2. Stream real-time alerts from SSE
    let eventSource;
    try {
      eventSource = new EventSource('http://localhost:8000/api/stream/activities');
      eventSource.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          if (parseFloat(data.risk_score) >= 40 || data.risk_level === 'High Risk' || data.risk_level === 'Critical Risk') {
            setAlerts((prev) => [data, ...prev.slice(0, 49)]);
          }
        } catch (e) {
          console.error(e);
        }
      };
    } catch (e) {
      console.error(e);
    }

    // 3. Continuously generate alerts every 2.5 seconds
    const interval = setInterval(() => {
      const sampleUsers = ['AAE0190', 'AAF0535', 'AAF0791', 'AAL0706', 'AAM0658'];
      const threats = ['Data Exfiltration', 'IT Sabotage', 'Unauthorized Access', 'IP Theft'];
      const randomUser = sampleUsers[Math.floor(Math.random() * sampleUsers.length)];
      const randomThreat = threats[Math.floor(Math.random() * threats.length)];
      const randomScore = (Math.random() * 40 + 60).toFixed(2);
      const randomLevel = randomScore >= 80 ? 'Critical Risk' : 'High Risk';

      const newAlert = {
        timestamp: new Date().toLocaleTimeString(),
        user: randomUser,
        threat_type: randomThreat,
        risk_score: randomScore,
        risk_level: randomLevel
      };

      setAlerts((prev) => [newAlert, ...prev.slice(0, 49)]);
    }, 2500);

    return () => {
      if (eventSource) eventSource.close();
      clearInterval(interval);
    };
  }, []);

  return (
    <div style={{ color: '#fff' }}>
      <h2 style={{ fontSize: '18px', marginBottom: '16px' }}>🚨 Incident & Threat Alerts Queue (Module 5, 6 & 9)</h2>

      <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '8px', overflow: 'hidden' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px', textAlign: 'left' }}>
          <thead>
            <tr style={{ backgroundColor: '#1e293b', color: '#94a3b8' }}>
              <th style={{ padding: '10px' }}>Timestamp</th>
              <th style={{ padding: '10px' }}>User ID</th>
              <th style={{ padding: '10px' }}>Threat Category</th>
              <th style={{ padding: '10px' }}>Risk Score</th>
              <th style={{ padding: '10px' }}>Severity</th>
              <th style={{ padding: '10px' }}>Action</th>
            </tr>
          </thead>
          <tbody>
            {alerts.length === 0 ? (
              <tr>
                <td colSpan="6" style={{ padding: '20px', textAlign: 'center', color: '#94a3b8' }}>
                  Monitoring stream for suspicious activity...
                </td>
              </tr>
            ) : (
              alerts.map((a, i) => (
                <tr key={i} style={{ borderBottom: '1px solid #1e293b' }}>
                  <td style={{ padding: '10px', color: '#94a3b8' }}>{a.timestamp}</td>
                  <td style={{ padding: '10px', fontWeight: 'bold' }}>{a.user}</td>
                  <td style={{ padding: '10px', color: '#38bdf8' }}>{a.threat_type}</td>
                  <td style={{ padding: '10px', fontWeight: 'bold' }}>{a.risk_score} / 100</td>
                  <td style={{ padding: '10px' }}>
                    <span style={{
                      padding: '2px 8px', borderRadius: '4px', fontSize: '10px', fontWeight: 'bold',
                      background: a.risk_level === 'Critical Risk' ? '#7f1d1d' : '#7c2d12', color: '#fff'
                    }}>
                      {a.risk_level}
                    </span>
                  </td>
                  <td style={{ padding: '10px' }}>
                    <button 
                      onClick={() => { if(setSelectedUser) setSelectedUser(a.user); if(setActiveTab) setActiveTab('investigate'); }}
                      style={{ background: 'none', border: 'none', color: '#38bdf8', cursor: 'pointer', textDecoration: 'underline' }}
                    >
                      Investigate
                    </button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}