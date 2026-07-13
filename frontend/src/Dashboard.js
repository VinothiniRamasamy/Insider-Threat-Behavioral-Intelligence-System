import React, { useState } from "react";
import axios from "axios";
import "./Dashboard.css";

function Dashboard({ user, onLogout }) {

  const [formData, setFormData] = useState({

    http_count: "",
    after_hours: "",
    unique_pc: "",
    unique_url: "",
    logon_count: "",
    device_count: "",
    device_activity: "",
    file_count: "",
    unique_files: "",
    email_count: "",
    total_attachment: "",
    unique_receivers: "",

  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {

    setFormData({

      ...formData,

      [e.target.name]: Number(e.target.value)

    });

  };

  const predict = async () => {

    try {

      const response = await axios.post(

        "http://127.0.0.1:8000/predict",

        formData

      );

      setResult(response.data);

    }

    catch (error) {

      console.error(error);

      alert("Prediction Failed!");

    }

  };

  return (

    <div className="dashboard">

          <div className="topbar">

        <div>

          <h1>🛡 CyberShield Technologies</h1>

          <p>AI-Powered Insider Threat Behavioral Intelligence System</p>

        </div>

        <div className="user-info">

          <h3>Welcome, {user.name}</h3>

          <p>{user.role}</p>

          <button onClick={onLogout}>
            Logout
          </button>

        </div>

      </div>


      <div className="dashboard-card">

        <h2>Employee Behavioral Activity Input</h2>

        <p className="subtitle">
          Enter employee behavioral metrics. Each field below represents an activity
          collected from enterprise systems.
        </p>

        <div className="grid">


          <div className="input-card">
            <label>HTTP Count</label>
            <small>Total web requests made by the employee.</small>
            <input type="number" name="http_count" onChange={handleChange}/>
          </div>


          <div className="input-card">
            <label>Unique URL</label>
            <small>Number of different websites visited.</small>
            <input type="number" name="unique_url" onChange={handleChange}/>
          </div>


          <div className="input-card">
            <label>Logon Count</label>
            <small>Total login/logout activities.</small>
            <input type="number" name="logon_count" onChange={handleChange}/>
          </div>


          <div className="input-card">
            <label>Unique PC</label>
            <small>Different computers used.</small>
            <input type="number" name="unique_pc" onChange={handleChange}/>
          </div>


          <div className="input-card">
            <label>After Hours Activity</label>
            <small>0 = No &nbsp;&nbsp; 1 = Yes</small>
            <input type="number" name="after_hours" onChange={handleChange}/>
          </div>


          <div className="input-card">
            <label>Device Count</label>
            <small>Total connected devices.</small>
            <input type="number" name="device_count" onChange={handleChange}/>
          </div>


          <div className="input-card">
            <label>Device Activity</label>
            <small>Activities performed using devices.</small>
            <input type="number" name="device_activity" onChange={handleChange}/>
          </div>


          <div className="input-card">
            <label>File Count</label>
            <small>Total accessed files.</small>
            <input type="number" name="file_count" onChange={handleChange}/>
          </div>


          <div className="input-card">
            <label>Unique Files</label>
            <small>Different files accessed.</small>
            <input type="number" name="unique_files" onChange={handleChange}/>
          </div>


          <div className="input-card">
            <label>Email Count</label>
            <small>Total emails sent.</small>
            <input type="number" name="email_count" onChange={handleChange}/>
          </div>


          <div className="input-card">
            <label>Total Attachment</label>
            <small>Email attachments shared.</small>
            <input type="number" name="total_attachment" onChange={handleChange}/>
          </div>


          <div className="input-card">
            <label>Unique Receivers</label>
            <small>Different email recipients.</small>
            <input type="number" name="unique_receivers" onChange={handleChange}/>
          </div>

        </div>

        <button
          className="predict-btn"
          onClick={predict}
        >
          🔍 Analyze Employee Behavior
        </button>
                {result && (

          <div
            className={
              result.prediction === "Insider"
                ? "result danger"
                : "result safe"
            }
          >

            <h2>
              {result.prediction === "Insider"
                ? "🚨 Insider Threat Detected"
                : "✅ Normal User"}
            </h2>

            <h3>
              Confidence : {result.confidence}%
            </h3>

            <progress
              value={result.confidence}
              max="100"
              style={{
                width: "100%",
                height: "18px",
                marginBottom: "20px"
              }}
            />

            <hr />

            <h3>🔍 Top Important Factors</h3>

            {result.explanation &&
              Object.entries(result.explanation)
                .slice(0, 5)
                .map(([feature, value]) => (

                  <div key={feature} className="factor">

                    <p>
                      <b>{feature}</b> : {value}
                    </p>

                    <progress
                      value={value}
                      max="0.3"
                      style={{
                        width: "100%",
                        height: "10px"
                      }}
                    />

                  </div>

                ))}

          </div>

        )}

      </div>

    </div>

  );

}

export default Dashboard;