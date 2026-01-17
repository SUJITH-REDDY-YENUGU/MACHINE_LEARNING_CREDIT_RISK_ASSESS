from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load artifacts
model = joblib.load("models/base_xgboost_model.pkl")
scaler = joblib.load("models/scaler.pkl")
encoders = joblib.load("models/encoders_dict.pkl")

# Define schema with correct dtypes
class LoanApplication(BaseModel):
    person_age: float
    person_gender: str
    person_education: str
    person_income: float
    person_emp_exp: int
    person_home_ownership: str
    loan_amnt: float
    loan_intent: str
    loan_int_rate: float
    loan_percent_income: float
    cb_person_cred_hist_length: float
    credit_score: int
    previous_loan_defaults_on_file: str
    debt_to_income: float
    age_group: str

@app.get("/")
def root():
    return {"message": "Credit Risk API is running!"}

@app.post("/predict")
def predict(application: LoanApplication):
    df = pd.DataFrame([application.dict()])

    # Apply encoders
    for col, encoder in encoders.items():
        df[col] = encoder.transform(df[col].astype(str))

    # Apply scaler
    scaling_cols = ["person_age","person_income","loan_amnt","credit_score","loan_int_rate"]
    df[scaling_cols] = scaler.transform(df[scaling_cols])

    prediction = model.predict(df)[0]
    return {"loan_status": int(prediction)}