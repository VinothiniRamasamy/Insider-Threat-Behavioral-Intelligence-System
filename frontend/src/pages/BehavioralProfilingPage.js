import React from 'react';

export default function BehavioralProfilingPage() {
  const sampleUsers = [
    { user: 'AAE0190', logon_mean: '1.97 / day', usb_mean: '0.0 / day', email_mean: '4.36 / day', http_mean: '3.76 / day' },
    { user: 'AAF0535', logon_mean: '0.96 / day', usb_mean: '3.74 / day', email_mean: '0.47 / day', http_mean: '0.37 / day' },
    { user: 'AAF0791', logon_mean: '1.97 / day', usb_mean: '0.0 / day', email_mean: '2.81 / day', http_mean: '2.55 / day' },
    { user: 'AAL0706', logon_mean: '1.97 / day', usb_mean: '0.0 / day', email_mean: '0.31 / day', http_mean: '0.26 / day' },
  ];

  return (
    <div style={{ color: '#fff' }}>
      <h2 style={{ fontSize: '18px', marginBottom: '16px' }}>🧬 Behavioral Profiling & Per-User Baselines (Module 4 & 8)</h2>
      <p style={{ fontSize: '12px', color: '#94a3b8', marginBottom: '20px' }}>
        The system calculates historical daily averages for each employee to establish normal behavior. Deviations from these baselines generate risk scores.
      </p>

      <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '8px', overflow: 'hidden' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px', textAlign: 'left' }}>
          <thead>
            <tr style={{ backgroundColor: '#1e293b', color: '#94a3b8' }}>
              <th style={{ padding: '12px' }}>Employee User ID</th>
              <th style={{ padding: '12px' }}>Avg Logon Count</th>
              <th style={{ padding: '12px' }}>Avg USB Connects</th>
              <th style={{ padding: '12px' }}>Avg Emails Sent</th>
              <th style={{ padding: '12px' }}>Avg HTTP Visits</th>
            </tr>
          </thead>
          <tbody>
            {sampleUsers.map((u, i) => (
              <tr key={i} style={{ borderBottom: '1px solid #1e293b' }}>
                <td style={{ padding: '12px', fontWeight: 'bold', color: '#38bdf8' }}>{u.user}</td>
                <td style={{ padding: '12px' }}>{u.logon_mean}</td>
                <td style={{ padding: '12px' }}>{u.usb_mean}</td>
                <td style={{ padding: '12px' }}>{u.email_mean}</td>
                <td style={{ padding: '12px' }}>{u.http_mean}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}