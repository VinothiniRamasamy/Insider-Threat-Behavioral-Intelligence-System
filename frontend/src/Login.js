import React, { useState } from "react";
import "./Login.css";

function Login({ onLogin }) {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");


  // Employee Accounts
  const users = [
    {
      email: "vinothini@cybershield.com",
      password: "vino123",
      name: "Vinothini",
      role: "Employee",
    },
    {
      email: "rahul@cybershield.com",
      password: "rahul123",
      name: "Rahul",
      role: "Employee",
    },
    {
      email: "priya@cybershield.com",
      password: "priya123",
      name: "Priya",
      role: "Employee",
    },
    {
      email: "arun@cybershield.com",
      password: "arun123",
      name: "Arun",
      role: "Employee",
    }
  ];


  // Employee Login
  const handleLogin = (e) => {

    e.preventDefault();

    setError("");


    const user = users.find(
      (u) =>
        u.email.toLowerCase() === email.trim().toLowerCase() &&
        u.password === password.trim()
    );


    if (user) {

      onLogin(user);

    } 
    else {

      setError("Invalid email address or password.");

    }

  };



  // Admin Login
  const adminLogin = () => {

    const adminEmail = prompt("Admin Email");
    const adminPassword = prompt("Admin Password");


    if (
      adminEmail === "admin@cybershield.com" &&
      adminPassword === "admin123"
    ) {

      onLogin({
        name: "Administrator",
        email: adminEmail,
        role: "Administrator",
      });

    } 
    else {

      alert("Invalid administrator credentials.");

    }

  };



  return (

    <div className="login-container">


      {/* Left Panel */}

      <div className="left-panel">

        <h1>
          CYBERSHIELD AI
        </h1>


        <h2>
          Insider Threat Behavioral Intelligence System
        </h2>


        <p>
          Monitor employee behavioral activities using Artificial Intelligence,
          detect suspicious insider threats, and provide explainable predictions
          for enhanced organizational security.
        </p>


      </div>



      {/* Right Panel */}

      <div className="right-panel">


        <div className="login-card">


          <h2>
            Employee Sign In
          </h2>


          <p className="welcome">
            Sign in to access the Behavioral Intelligence Dashboard.
          </p>



          <form onSubmit={handleLogin}>


            <label>
              Email Address
            </label>


            <input
              type="email"
              placeholder="employee@cybershield.com"
              value={email}
              onChange={(e)=>{

                setEmail(e.target.value);
                setError("");

              }}
              required
            />



            <label>
              Password
            </label>


            <input
              type="password"
              placeholder="Enter your password"
              value={password}
              onChange={(e)=>{

                setPassword(e.target.value);
                setError("");

              }}
              required
            />



            {
              error && (
                <p className="error">
                  {error}
                </p>
              )
            }



            <button
              type="submit"
              className="login-btn"
            >

              Sign In

            </button>



          </form>




          <div className="admin-link">


            <span>
              Administrator?
            </span>


            <button
              className="link-button"
              onClick={adminLogin}
            >

              Admin Login

            </button>


          </div>



        </div>


      </div>


    </div>

  );

}


export default Login;