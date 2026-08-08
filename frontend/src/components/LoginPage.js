import React, { useState } from 'react';

export default function LoginPage({ onLogin }) {
  const [email, setEmail] = useState('vinothini@cybershield.com');
  const [password, setPassword] = useState('password123');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (email && password) {
      onLogin({ email, role: 'Security Analyst' });
    }
  };

  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      minHeight: '100vh',
      width: '100vw',
      backgroundColor: '#020617',
      fontFamily: 'sans-serif'
    }}>
      <div style={{
        backgroundColor: '#0f172a',
        border: '1px solid #1e293b',
        borderRadius: '12px',
        padding: '32px',
        width: '380px',
        textAlign: 'center',
        boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.5)'
      }}>
        <div style={{ fontSize: '40px', marginBottom: '12px' }}>🛡️</div>
        <h2 style={{ fontSize: '20px', color: '#fff', margin: '0 0 6px 0', fontWeight: 'bold' }}>Insider Threat System</h2>
        <p style={{ fontSize: '11px', color: '#94a3b8', margin: '0 0 24px 0' }}>Enterprise Security Portal Authentication</p>

        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          <div style={{ textAlign: 'left' }}>
            <label style={{ fontSize: '11px', color: '#cbd5e1', display: 'block', marginBottom: '6px' }}>User Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              style={{
                width: '100%',
                padding: '10px',
                borderRadius: '6px',
                border: '1px solid #334155',
                backgroundColor: '#1e293b',
                color: '#fff',
                fontSize: '12px',
                boxSizing: 'border-box'
              }}
              required
            />
          </div>

          <div style={{ textAlign: 'left' }}>
            <label style={{ fontSize: '11px', color: '#cbd5e1', display: 'block', marginBottom: '6px' }}>Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              style={{
                width: '100%',
                padding: '10px',
                borderRadius: '6px',
                border: '1px solid #334155',
                backgroundColor: '#1e293b',
                color: '#fff',
                fontSize: '12px',
                boxSizing: 'border-box'
              }}
              required
            />
          </div>

          <button
            type="submit"
            style={{
              marginTop: '10px',
              padding: '12px',
              borderRadius: '6px',
              border: 'none',
              backgroundColor: '#38bdf8',
              color: '#0f172a',
              fontWeight: 'bold',
              fontSize: '13px',
              cursor: 'pointer'
            }}
          >
            Authenticate Session
          </button>
        </form>
      </div>
    </div>
  );
}