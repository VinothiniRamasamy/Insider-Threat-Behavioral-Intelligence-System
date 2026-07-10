import React, { useState } from "react";
import axios from "axios";
import "./App.css";


function App() {

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

    catch(error) {

      console.error(error);

      alert("Prediction Failed!");

    }

  };



  return (

    <div className="container">


      <div className="card">


        <h1>
          🛡 AI-Powered Insider Threat Detection
        </h1>


        <p className="subtitle">
          User Behavior Analysis using Machine Learning
        </p>



        <div className="grid">


          <input type="number" name="http_count"
          placeholder="HTTP Count"
          onChange={handleChange}/>


          <input type="number" name="after_hours"
          placeholder="After Hours Activity (1/0)"
          onChange={handleChange}/>


          <input type="number" name="unique_pc"
          placeholder="Unique PC Count"
          onChange={handleChange}/>


          <input type="number" name="unique_url"
          placeholder="Unique URL Count"
          onChange={handleChange}/>


          <input type="number" name="logon_count"
          placeholder="Logon Count"
          onChange={handleChange}/>


          <input type="number" name="device_count"
          placeholder="Device Count"
          onChange={handleChange}/>


          <input type="number" name="device_activity"
          placeholder="Device Activity"
          onChange={handleChange}/>


          <input type="number" name="file_count"
          placeholder="File Count"
          onChange={handleChange}/>


          <input type="number" name="unique_files"
          placeholder="Unique Files"
          onChange={handleChange}/>


          <input type="number" name="email_count"
          placeholder="Email Count"
          onChange={handleChange}/>


          <input type="number" name="total_attachment"
          placeholder="Total Attachment"
          onChange={handleChange}/>


          <input type="number" name="unique_receivers"
          placeholder="Unique Receivers"
          onChange={handleChange}/>



        </div>




        <button onClick={predict}>
          🔍 Analyze Behavior
        </button>





        {result && (

          <div
          className={
            result.prediction === "Insider"
            ? "result danger"
            : "result safe"
          }>



            <h2>

            {result.prediction === "Insider"
            ? "🚨 Insider Threat Detected"
            : "✅ Normal User"}

            </h2>



            <h3>
              Confidence: {result.confidence}%
            </h3>



            <progress

              value={result.confidence}

              max="100"

              style={{
                width:"100%",
                height:"20px"
              }}

            />



            <hr />



            <h3>
              🔍 Important Factors
            </h3>




            {
              result.explanation &&

              Object.entries(result.explanation)

              .slice(0,5)

              .map(([feature,value]) => (


                <div key={feature}>


                  <p>

                  <b>{feature}</b>
                  :
                  {value}

                  </p>



                  <progress

                  value={value}

                  max="0.3"

                  style={{
                    width:"100%",
                    height:"12px"
                  }}

                  />



                </div>


              ))
            }





          </div>

        )}



      </div>


    </div>

  );

}


export default App;