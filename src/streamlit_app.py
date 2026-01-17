import streamlit as st
import requests

st.title("💳 Credit Risk Prediction Demo (via FastAPI)")

# Dropdowns with categorical values
gender = st.selectbox("Gender", ["male", "female"])
education = st.selectbox("Education", ["Bachelor","Associate","High School","Master","Doctorate"])
home = st.selectbox("Home Ownership", ["RENT","MORTGAGE","OWN","OTHER"])
intent = st.selectbox("Loan Intent", ["EDUCATION","MEDICAL","VENTURE","PERSONAL","DEBTCONSOLIDATION","HOMEIMPROVEMENT"])
defaults = st.selectbox("Previous Loan Defaults", ["Yes","No"])
age_group = st.selectbox("Age Group", ["Adult","Senior","Youth"])  # adjust categories if needed

# Numeric inputs
age = st.number_input("Age", min_value=18.0, max_value=100.0, value=30.0)
income = st.number_input("Income", min_value=0.0, value=50000.0)
emp_exp = st.number_input("Employment Experience (years)", min_value=0, value=5)
loan_amnt = st.number_input("Loan Amount", min_value=1000.0, value=10000.0)
loan_int_rate = st.number_input("Loan Interest Rate (%)", min_value=1.0, value=10.0)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
cred_hist_len = st.number_input("Credit History Length", min_value=1.0, value=10.0)

# Derived features
loan_percent_income = loan_amnt / (income + 1)
debt_to_income = loan_amnt / (income + 1)

if st.button("Predict Loan Status"):
    payload = {
        "person_age": age,
        "person_gender": gender,
        "person_education": education,
        "person_income": income,
        "person_emp_exp": emp_exp,
        "person_home_ownership": home,
        "loan_amnt": loan_amnt,
        "loan_intent": intent,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_cred_hist_length": cred_hist_len,
        "credit_score": credit_score,
        "previous_loan_defaults_on_file": defaults,
        "debt_to_income": debt_to_income,
        "age_group": age_group
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"✅ Loan Status Prediction: {result['loan_status']} (0 = High Risk, 1 = Low Risk)")
    else:
        st.error("❌ Error calling API")