import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

def load_and_preprocess(filepath="data/rockfall_data.csv"):

    # ── 1. Load data ──────────────────────────────────────────
    df = pd.read_csv(filepath)
    print(f"📂 Loaded data: {df.shape[0]} rows, {df.shape[1]} columns")
    print(df.head())

    # ── 2. Check for missing values ───────────────────────────
    print("\n🔍 Missing values:\n", df.isnull().sum())
    df.dropna(inplace=True)

    # ── 3. Define features (X) and target (y) ────────────────
    feature_cols = [
        "slope_angle", "rock_hardness", "rainfall_mm",
        "seismic_activity", "temp_change", "vegetation_cover",
        "crack_density", "distance_to_fault"
    ]
    X = df[feature_cols]
    y = df["rockfall"]                  # 0 or 1

    # ── 4. Split into train and test sets ─────────────────────
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"\n✂️  Train: {X_train.shape[0]} rows | Test: {X_test.shape[0]} rows")

    # ── 5. Scale features (important for some models) ─────────
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled  = scaler.transform(X_test)

    # ── 6. Save the scaler for later use ──────────────────────
    os.makedirs("models", exist_ok=True)
    joblib.dump(scaler, "models/scaler.pkl")
    print("💾 Scaler saved to models/scaler.pkl")

    return X_train_scaled, X_test_scaled, y_train, y_test, feature_cols


if __name__ == "__main__":
    load_and_preprocess()