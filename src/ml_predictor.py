import joblib
import numpy as np
import os

base_dir = os.path.dirname(os.path.dirname(__file__))

data_path = os.path.join(base_dir, "models", "candidate_model.pkl")

model = joblib.load(data_path)


def predict_ml_score(skill_results, breakdown):

    features = np.array([[
        skill_results["match_percentage"],
        breakdown["repos"],
        breakdown["activity"],
        breakdown["languages"]
    ]])

    prediction = model.predict(features)[0]

    return prediction