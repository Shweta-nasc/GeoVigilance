import joblib
import numpy as np

def predict_rockfall(input_data: dict):
    """
    input_data = {
        "slope_angle": 65,
        "rock_hardness": 3,
        "rainfall_mm": 150,
        "seismic_activity": 3.5,
        "temp_change": 8,
        "vegetation_cover": 10,
        "crack_density": 7,
        "distance_to_fault": 2
    }
    """

    # ── 1. Load saved model and scaler ────────────────────────
    model  = joblib.load("models/rockfall_model.pkl")
    scaler = joblib.load("models/scaler.pkl")

    # ── 2. Prepare input in correct order ─────────────────────
    feature_order = [
        "slope_angle", "rock_hardness", "rainfall_mm",
        "seismic_activity", "temp_change", "vegetation_cover",
        "crack_density", "distance_to_fault"
    ]
    values = np.array([[input_data[f] for f in feature_order]])

    # ── 3. Scale and predict ──────────────────────────────────
    values_scaled = scaler.transform(values)
    prediction    = model.predict(values_scaled)[0]
    probability   = model.predict_proba(values_scaled)[0][1]

    result = {
        "prediction":  "⚠️ ROCKFALL LIKELY"    if prediction == 1
                       else "✅ NO ROCKFALL",
        "probability": f"{probability * 100:.1f}%",
        "risk_level":  "HIGH"   if probability > 0.7
                       else "MEDIUM" if probability > 0.4
                       else "LOW"
    }

    print("\n🔮 Prediction Result:")
    for k, v in result.items():
        print(f"   {k}: {v}")

    return result


if __name__ == "__main__":
    # Test with a high-risk scenario
    test_input = {
        "slope_angle":       65,
        "rock_hardness":     2,
        "rainfall_mm":       180,
        "seismic_activity":  4.0,
        "temp_change":       12,
        "vegetation_cover":  5,
        "crack_density":     9,
        "distance_to_fault": 1
    }
    predict_rockfall(test_input)