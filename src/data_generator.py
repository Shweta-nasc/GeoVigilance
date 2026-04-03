import pandas as pd
import numpy as np

def generate_rockfall_data(n_samples=2000, save_path="data/rockfall_data.csv"):
    np.random.seed(42)

    # ── Features ──────────────────────────────────────────────
    slope_angle        = np.random.uniform(10, 80, n_samples)      # degrees
    rock_hardness      = np.random.uniform(1, 10, n_samples)       # 1=soft, 10=hard
    rainfall_mm        = np.random.uniform(0, 200, n_samples)      # mm per day
    seismic_activity   = np.random.uniform(0, 5, n_samples)        # Richter scale
    temp_change        = np.random.uniform(-10, 15, n_samples)     # celsius change
    vegetation_cover   = np.random.uniform(0, 100, n_samples)      # percentage
    crack_density      = np.random.uniform(0, 10, n_samples)       # cracks per m²
    distance_to_fault  = np.random.uniform(0, 50, n_samples)       # km

    # ── Label logic (based on real geological knowledge) ──────
    risk_score = (
          0.35 * (slope_angle / 80)
        + 0.20 * (rainfall_mm / 200)
        + 0.20 * (seismic_activity / 5)
        + 0.10 * (crack_density / 10)
        + 0.08 * (temp_change / 15)
        - 0.05 * (rock_hardness / 10)
        - 0.02 * (vegetation_cover / 100)
        + np.random.normal(0, 0.05, n_samples)   # noise
    )

    # Binary label: 1 = rockfall likely, 0 = not likely
    label = (risk_score > 0.40).astype(int)

    # Risk level: Low / Medium / High
    risk_level = pd.cut(
        risk_score,
        bins=[-999, 0.25, 0.50, 999],
        labels=["Low", "Medium", "High"]
    )

    # ── Build DataFrame ───────────────────────────────────────
    df = pd.DataFrame({
        "slope_angle":       slope_angle,
        "rock_hardness":     rock_hardness,
        "rainfall_mm":       rainfall_mm,
        "seismic_activity":  seismic_activity,
        "temp_change":       temp_change,
        "vegetation_cover":  vegetation_cover,
        "crack_density":     crack_density,
        "distance_to_fault": distance_to_fault,
        "risk_level":        risk_level,
        "rockfall":          label            # ← this is what we predict
    })

    df.to_csv(save_path, index=False)
    print(f"✅ Dataset created: {n_samples} rows saved to {save_path}")
    return df


if __name__ == "__main__":
    generate_rockfall_data()