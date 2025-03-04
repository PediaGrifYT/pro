import { useState } from "react";

function App() {
    const [symptoms, setSymptoms] = useState("");
    const [result, setResult] = useState("");

    const handleSubmit = async () => {
        const response = await fetch("http://localhost:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ symptoms: symptoms.split(",") })
        });

        const data = await response.json();
        setResult(data.disease);
    };

    return (
        <div style={{ textAlign: "center", marginTop: "50px" }}>
            <h1>Medical Health Prediction</h1>
            <input 
                type="text" 
                value={symptoms} 
                onChange={(e) => setSymptoms(e.target.value)} 
                placeholder="Enter symptoms (comma-separated)"
                style={{ padding: "10px", width: "300px", marginRight: "10px" }}
            />
            <button onClick={handleSubmit} style={{ padding: "10px 20px" }}>Predict</button>
            {result && <h2>Possible Condition: {result}</h2>}
        </div>
    );
}

export default App;
