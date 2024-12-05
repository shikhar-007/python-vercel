import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([]);

  // Fetch data from the Python backend
  useEffect(() => {
    fetch("/api/data")
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>React + Python + MongoDB App</h1>
      <h3>Data from MongoDB:</h3>
      <ul>
        {data.map((item, index) => (
          <li key={index}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;

