import joblib
import numpy as np
import os

base_dir = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(base_dir, "models", "candidate_model.pkl")

model = None
if os.path.exists(model_path):
    model = joblib.load(model_path)


def predict_ml_score(skill_results, breakdown):

    if model is None:
        return 0

    features = np.array([[ 
        skill_results["match_percentage"],
        breakdown.get("repos", 0),
        breakdown.get("activity", 0),
        breakdown.get("languages", 0)
    ]])

    prediction = model.predict(features)[0]
    return prediction