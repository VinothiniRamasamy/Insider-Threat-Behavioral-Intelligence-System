import React from 'react';

export default function ReportsPage() {
  const downloadPDF = () => {
    window.open('http://localhost:8000/api/v1/export/pdf', '_blank');
  };

  const downloadExcel = () => {
    window.open('http://localhost:8000/api/v1/export/excel', '_blank');
  };

  return (
    <div style={{ color: '#fff' }}>
      <h2 style={{ fontSize: '18px', marginBottom: '16px' }}>📄 Reports & Export Engine (Module 12)</h2>
      <p style={{ fontSize: '12px', color: '#94a3b8', marginBottom: '24px' }}>
        Generate and download official PDF Incident Case Files and Excel Audit Logs for compliance.
      </p>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
        <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', padding: '24px', borderRadius: '8px' }}>
          <h3 style={{ margin: '0 0 8px 0', fontSize: '16px' }}>📕 PDF Incident Report</h3>
          <p style={{ fontSize: '12px', color: '#94a3b8', marginBottom: '20px' }}>Exports comprehensive threat summary and risk metrics in PDF format.</p>
          <button 
            onClick={downloadPDF}
            style={{ backgroundColor: '#ef4444', border: 'none', color: '#fff', padding: '10px 18px', borderRadius: '6px', cursor: 'pointer', fontSize: '12px', fontWeight: 'bold' }}
          >
            Download PDF Report
          </button>
        </div>

        <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', padding: '24px', borderRadius: '8px' }}>
          <h3 style={{ margin: '0 0 8px 0', fontSize: '16px' }}>📗 Excel Audit Log</h3>
          <p style={{ fontSize: '12px', color: '#94a3b8', marginBottom: '20px' }}>Exports raw threat alerts, timestamps, and user risk scores in XLSX format.</p>
          <button 
            onClick={downloadExcel}
            style={{ backgroundColor: '#10b981', border: 'none', color: '#fff', padding: '10px 18px', borderRadius: '6px', cursor: 'pointer', fontSize: '12px', fontWeight: 'bold' }}
          >
            Download Excel Log
          </button>
        </div>
      </div>
    </div>
  );
}