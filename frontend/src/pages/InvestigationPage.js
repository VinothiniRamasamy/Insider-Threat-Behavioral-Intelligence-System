import React from 'react';

export default function InvestigationPage({ selectedUser }) {
  const targetUser = selectedUser || 'AAE0190';

  const downloadPDFReport = () => {
    window.open(`http://localhost:8000/api/v1/export/pdf?user=${targetUser}`, '_blank');
  };

  const downloadExcelReport = () => {
    window.open(`http://localhost:8000/api/v1/export/excel?user=${targetUser}`, '_blank');
  };

  return (
    <div style={{ color: '#fff' }}>
      <h2 style={{ fontSize: '18px', marginBottom: '16px' }}>🔍 Threat Investigation Module (Module 7)</h2>
      
      {/* Target User Banner */}
      <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', padding: '20px', borderRadius: '8px', marginBottom: '20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <span style={{ fontSize: '11px', color: '#94a3b8' }}>Investigating Target Subject</span>
          <h3 style={{ margin: '4px 0 0 0', fontSize: '18px', color: '#38bdf8' }}>User ID: {targetUser}</h3>
          <p style={{ margin: '4px 0 0 0', fontSize: '12px', color: '#cbd5e1' }}>Threat Verdict: <strong style={{ color: '#ef4444' }}>High Risk (Data Exfiltration Candidate)</strong></p>
        </div>

        {/* Individual Case File Download Buttons */}
        <div style={{ display: 'flex', gap: '10px' }}>
          <button 
            onClick={downloadPDFReport}
            style={{ backgroundColor: '#ef4444', border: 'none', color: '#fff', padding: '10px 14px', borderRadius: '6px', cursor: 'pointer', fontSize: '12px', fontWeight: 'bold' }}
          >
            Download PDF Case Report
          </button>
          <button 
            onClick={downloadExcelReport}
            style={{ backgroundColor: '#10b981', border: 'none', color: '#fff', padding: '10px 14px', borderRadius: '6px', cursor: 'pointer', fontSize: '12px', fontWeight: 'bold' }}
          >
            Download Excel Audit Log
          </button>
        </div>
      </div>

      {/* SHAP & Feature Deviation Table */}
      <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', padding: '20px', borderRadius: '8px' }}>
        <h4 style={{ margin: '0 0 12px 0', fontSize: '14px', color: '#cbd5e1' }}>🧬 SHAP Feature Attribution & Behavioral Deviation Breakdown</h4>
        <p style={{ fontSize: '12px', color: '#94a3b8', marginBottom: '16px' }}>
          Explains why the UEBA model flagged this user by comparing real-time behavior against established historical baselines.
        </p>

        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '12px', textAlign: 'left' }}>
          <thead>
            <tr style={{ backgroundColor: '#1e293b', color: '#94a3b8' }}>
              <th style={{ padding: '10px' }}>Behavioral Metric</th>
              <th style={{ padding: '10px' }}>Observed Activity</th>
              <th style={{ padding: '10px' }}>Historical Baseline</th>
              <th style={{ padding: '10px' }}>SHAP Contribution Score</th>
              <th style={{ padding: '10px' }}>Risk Flag</th>
            </tr>
          </thead>
          <tbody>
            <tr style={{ borderBottom: '1px solid #1e293b' }}>
              <td style={{ padding: '10px', fontWeight: 'bold' }}>Files Copied to USB</td>
              <td style={{ padding: '10px', color: '#f97316' }}>45 files</td>
              <td style={{ padding: '10px', color: '#94a3b8' }}>0.0 / day</td>
              <td style={{ padding: '10px', fontWeight: 'bold', color: '#ef4444' }}>+35.4 pts</td>
              <td style={{ padding: '10px' }}><span style={{ background: '#7f1d1d', color: '#fff', padding: '2px 6px', borderRadius: '4px', fontSize: '10px' }}>CRITICAL</span></td>
            </tr>
            <tr style={{ borderBottom: '1px solid #1e293b' }}>
              <td style={{ padding: '10px', fontWeight: 'bold' }}>Off-Hours USB Activity</td>
              <td style={{ padding: '10px', color: '#f97316' }}>12 events</td>
              <td style={{ padding: '10px', color: '#94a3b8' }}>0.0 / day</td>
              <td style={{ padding: '10px', fontWeight: 'bold', color: '#ef4444' }}>+28.2 pts</td>
              <td style={{ padding: '10px' }}><span style={{ background: '#7f1d1d', color: '#fff', padding: '2px 6px', borderRadius: '4px', fontSize: '10px' }}>CRITICAL</span></td>
            </tr>
            <tr style={{ borderBottom: '1px solid #1e293b' }}>
              <td style={{ padding: '10px', fontWeight: 'bold' }}>Total Email Attachment Size</td>
              <td style={{ padding: '10px', color: '#f97316' }}>312 MB</td>
              <td style={{ padding: '10px', color: '#94a3b8' }}>3.8 MB / day</td>
              <td style={{ padding: '10px', fontWeight: 'bold', color: '#f97316' }}>+18.9 pts</td>
              <td style={{ padding: '10px' }}><span style={{ background: '#7c2d12', color: '#fff', padding: '2px 6px', borderRadius: '4px', fontSize: '10px' }}>HIGH</span></td>
            </tr>
            <tr style={{ borderBottom: '1px solid #1e293b' }}>
              <td style={{ padding: '10px', fontWeight: 'bold' }}>External Email Recipients</td>
              <td style={{ padding: '10px', color: '#f97316' }}>18 emails</td>
              <td style={{ padding: '10px', color: '#94a3b8' }}>1.2 / day</td>
              <td style={{ padding: '10px', fontWeight: 'bold', color: '#f97316' }}>+12.1 pts</td>
              <td style={{ padding: '10px' }}><span style={{ background: '#7c2d12', color: '#fff', padding: '2px 6px', borderRadius: '4px', fontSize: '10px' }}>HIGH</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}