import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os



def train_model():

    base_dir = os.path.dirname(os.path.dirname(__file__))

    data_path = os.path.join(base_dir, "data", "training_data.csv")
    model_path = os.path.join(base_dir, "models", "candidate_model.pkl")

    df=pd.read_csv(data_path)
    X=df[["skill_match","repo_score","activity_score","language_score"]]
    y=df["final_score"]

    model=RandomForestRegressor(n_estimators=100,random_state=42)
    model.fit(X,y)
    joblib.dump(model,model_path)
    print("model trained and saved")

if __name__=="__main__":
    train_model()