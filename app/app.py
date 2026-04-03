#PIPELINE CONTROLLER

from src.data_preprocessing import preprocess_data
from src.feature_engineering import create_features
from src.train_model import train_model
from src.evaluate_model import evaluate_model

def main():
    # Step 1: Load + clean data
    data = preprocess_data("data/raw/data.csv")

    # Step 2: Feature engineering
    data = create_features(data)

    # Step 3: Train model
    model = train_model(data)

    # Step 4: Evaluate
    evaluate_model(model, data)

if __name__ == "__main__":
    main()