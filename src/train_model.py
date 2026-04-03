import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import (
    accuracy_score, classification_report,
    confusion_matrix, ConfusionMatrixDisplay
)
import joblib
from preprocess import load_and_preprocess


def train_and_evaluate():

    # ── 1. Load preprocessed data ─────────────────────────────
    X_train, X_test, y_train, y_test, feature_cols = load_and_preprocess()

    # ── 2. Define models to compare ───────────────────────────
    models = {
        "Random Forest":         RandomForestClassifier(n_estimators=100, random_state=42),
        "Gradient Boosting":     GradientBoostingClassifier(n_estimators=100, random_state=42),
        "XGBoost":               XGBClassifier(n_estimators=100, random_state=42,
                                               eval_metric="logloss", verbosity=0),
    }

    best_model      = None
    best_accuracy   = 0
    best_model_name = ""

    # ── 3. Train and evaluate each model ──────────────────────
    for name, model in models.items():
        print(f"\n🤖 Training: {name} ...")
        model.fit(X_train, y_train)

        y_pred   = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"   Accuracy: {accuracy * 100:.2f}%")
        print(classification_report(y_test, y_pred, target_names=["No Rockfall", "Rockfall"]))

        if accuracy > best_accuracy:
            best_accuracy   = accuracy
            best_model      = model
            best_model_name = name

    # ── 4. Save the best model ────────────────────────────────
    joblib.dump(best_model, "models/rockfall_model.pkl")
    print(f"\n🏆 Best Model: {best_model_name} ({best_accuracy * 100:.2f}%)")
    print("💾 Saved to models/rockfall_model.pkl")

    # ── 5. Plot confusion matrix ──────────────────────────────
    y_pred_best = best_model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred_best)
    disp = ConfusionMatrixDisplay(cm, display_labels=["No Rockfall", "Rockfall"])
    disp.plot(cmap="Blues")
    plt.title(f"Confusion Matrix — {best_model_name}")
    plt.savefig("models/confusion_matrix.png")
    plt.show()
    print("📊 Confusion matrix saved to models/confusion_matrix.png")

    # ── 6. Feature importance chart ───────────────────────────
    if hasattr(best_model, "feature_importances_"):
        importances = best_model.feature_importances_
        indices     = np.argsort(importances)[::-1]

        plt.figure(figsize=(10, 5))
        plt.bar(range(len(feature_cols)),
                importances[indices], color="steelblue")
        plt.xticks(range(len(feature_cols)),
                   [feature_cols[i] for i in indices], rotation=45)
        plt.title("Feature Importance")
        plt.tight_layout()
        plt.savefig("models/feature_importance.png")
        plt.show()
        print("📊 Feature importance saved to models/feature_importance.png")


if __name__ == "__main__":
    train_and_evaluate()