from flask import Flask, request, jsonify, render_template_string
import sys
sys.path.append("../src")
from predict import predict_rockfall

app = Flask(__name__)

# Simple HTML form — no separate HTML file needed
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Rockfall Prediction</title>
    <style>
        body { font-family: Arial; max-width: 600px; margin: 40px auto; padding: 20px; }
        h1   { color: #b22222; }
        input { width: 100%; padding: 8px; margin: 6px 0 16px; box-sizing: border-box; }
        button { background: #b22222; color: white; padding: 12px 24px;
                 border: none; cursor: pointer; font-size: 16px; border-radius: 4px; }
        #result { margin-top: 24px; padding: 16px; border-radius: 8px;
                  background: #f5f5f5; font-size: 18px; }
    </style>
</head>
<body>
    <h1>🏔️ Rockfall Prediction AI</h1>

    <label>Slope Angle (degrees)</label>
    <input type="number" id="slope_angle"       placeholder="e.g. 45" />

    <label>Rock Hardness (1-10)</label>
    <input type="number" id="rock_hardness"     placeholder="e.g. 5" />

    <label>Rainfall (mm/day)</label>
    <input type="number" id="rainfall_mm"       placeholder="e.g. 80" />

    <label>Seismic Activity (Richter)</label>
    <input type="number" id="seismic_activity"  placeholder="e.g. 2.5" step="0.1" />

    <label>Temperature Change (°C)</label>
    <input type="number" id="temp_change"       placeholder="e.g. 5" />

    <label>Vegetation Cover (%)</label>
    <input type="number" id="vegetation_cover"  placeholder="e.g. 30" />

    <label>Crack Density (per m²)</label>
    <input type="number" id="crack_density"     placeholder="e.g. 4" />

    <label>Distance to Fault (km)</label>
    <input type="number" id="distance_to_fault" placeholder="e.g. 10" />

    <button onclick="predict()">🔮 Predict</button>
    <div id="result"></div>

    <script>
        async function predict() {
            const fields = [
                "slope_angle","rock_hardness","rainfall_mm","seismic_activity",
                "temp_change","vegetation_cover","crack_density","distance_to_fault"
            ];
            const data = {};
            fields.forEach(f => data[f] = parseFloat(document.getElementById(f).value));

            const res  = await fetch("/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data)
            });
            const json = await res.json();
            document.getElementById("result").innerHTML = `
                <strong>${json.prediction}</strong><br>
                Probability: ${json.probability}<br>
                Risk Level: ${json.risk_level}
            `;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/predict", methods=["POST"])
def predict():
    data   = request.json
    result = predict_rockfall(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)