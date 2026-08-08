import React, { useEffect, useState } from 'react';

export default function LiveMonitoringPage({ setSelectedUser, setActiveTab }) {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    let eventSource;
    try {
      // Connecting to backend stream endpoint
      eventSource = new EventSource('http://localhost:8000/api/v1/stream');

      eventSource.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          
          const threatMap = {
            0: 'Data Exfiltration',
            1: 'IT Sabotage',
            2: 'IP Theft',
            3: 'Normal Behavior',
            4: 'Unauthorized Access'
          };

          const formattedLog = {
            timestamp: new Date().toLocaleTimeString(),
            user: data.user,
            threat_type: threatMap[data.prediction] || 'Normal Behavior',
            risk_score: data.risk_score,
            risk_level: data.risk_level
          };

          setLogs((prev) => [formattedLog, ...prev.slice(0, 49)]);
        } catch (e) {
          console.error(e);
        }
      };

      eventSource.onerror = (e) => {
        console.warn("Stream reconnecting...", e);
      };
    } catch (e) {
      console.error(e);
    }

    return () => {
      if (eventSource) eventSource.close();
    };
  }, []);

  return (
    <div style={{ color: '#fff' }}>
      <h2 style={{ fontSize: '18px', marginBottom: '16px' }}>📡 Live Stream Monitoring Engine (Module 3)</h2>
      <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '8px', overflow: 'hidden' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px', textAlign: 'left' }}>
          <thead>
            <tr style={{ backgroundColor: '#1e293b', color: '#94a3b8' }}>
              <th style={{ padding: '10px' }}>Time</th>
              <th style={{ padding: '10px' }}>User</th>
              <th style={{ padding: '10px' }}>Predicted Threat</th>
              <th style={{ padding: '10px' }}>Risk Score</th>
              <th style={{ padding: '10px' }}>Level</th>
              <th style={{ padding: '10px' }}>Action</th>
            </tr>
          </thead>
          <tbody>
            {logs.length === 0 ? (
              <tr>
                <td colSpan="6" style={{ padding: '20px', textAlign: 'center', color: '#94a3b8' }}>
                  Connecting to live dataset event stream...
                </td>
              </tr>
            ) : (
              logs.map((log, i) => (
                <tr key={i} style={{ borderBottom: '1px solid #1e293b' }}>
                  <td style={{ padding: '10px', color: '#94a3b8' }}>{log.timestamp}</td>
                  <td style={{ padding: '10px', fontWeight: 'bold' }}>{log.user}</td>
                  <td style={{ padding: '10px', color: '#38bdf8' }}>{log.threat_type}</td>
                  <td style={{ padding: '10px', fontWeight: 'bold' }}>{log.risk_score} pts</td>
                  <td style={{ padding: '10px' }}>
                    <span style={{
                      padding: '2px 8px', borderRadius: '4px', fontSize: '10px', fontWeight: 'bold',
                      background: log.risk_level === 'High Risk' ? '#7f1d1d' : log.risk_level === 'Medium Risk' ? '#7c2d12' : '#065f46',
                      color: '#fff'
                    }}>
                      {log.risk_level}
                    </span>
                  </td>
                  <td style={{ padding: '10px' }}>
                    <button 
                      onClick={() => { if(setSelectedUser) setSelectedUser(log.user); if(setActiveTab) setActiveTab('investigate'); }}
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