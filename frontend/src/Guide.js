import React from "react";
import "./Guide.css";

function Guide({ onContinue }) {

  const features = [
    {
      title: "HTTP Count",
      desc: "Total number of web requests or websites accessed by the employee."
    },
    {
      title: "Unique URL",
      desc: "Number of different websites visited."
    },
    {
      title: "Logon Count",
      desc: "Total employee login and logout activities."
    },
    {
      title: "Unique PC",
      desc: "Number of different computers used by the employee."
    },
    {
      title: "After Hours Activity",
      desc: "0 = No activity after office hours, 1 = Activity detected after office hours."
    },
    {
      title: "Device Count",
      desc: "Number of external devices connected (USB, HDD, Mobile, etc.)."
    },
    {
      title: "Device Activity",
      desc: "Total activities performed using connected devices."
    },
    {
      title: "File Count",
      desc: "Total number of files accessed."
    },
    {
      title: "Unique Files",
      desc: "Number of different files accessed."
    },
    {
      title: "Email Count",
      desc: "Total emails sent."
    },
    {
      title: "Total Attachment",
      desc: "Total attachments shared through emails."
    },
    {
      title: "Unique Receivers",
      desc: "Number of different recipients who received emails."
    }
  ];

  return (

    <div className="guide-container">

      <div className="guide-header">

        <h1>Employee Behavior Guide</h1>

        <p>
          Please review the behavioral metrics before submitting employee activity for AI analysis.
        </p>

      </div>

      <div className="feature-grid">

        {features.map((item, index) => (

          <div className="feature-card" key={index}>

            <h3>{item.title}</h3>

            <p>{item.desc}</p>

          </div>

        ))}

      </div>

      <div className="guide-footer">

        <button
          className="continue-btn"
          onClick={onContinue}
        >
          Continue to Prediction →
        </button>

      </div>

    </div>

  );

}

export default Guide;