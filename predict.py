import pandas as pd
import joblib
from config import MODEL_PATH, FEATURE_PATH

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURE_PATH)

def predict_customer(data):

    input_df = pd.DataFrame([data])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    return pred, prob
