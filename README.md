# NOTE
Create a models folder in project root directory this is important and run the notebooks to get scaler , encoders and models please do run all notebooks.


# 💳 Credit Risk Prediction System

## 📌 Overview
This project is an **end-to-end machine learning pipeline** for predicting credit risk (loan approval vs. default).  
It covers the full workflow:
- Data preprocessing & feature engineering
- Exploratory Data Analysis (EDA)
- Model building & optimization
- Handling class imbalance (SMOTE)
- Model evaluation & comparison
- Deployment demos with **FastAPI** (backend API) and **Streamlit** (frontend UI)

The goal is to help financial institutions **reduce loan defaults** by identifying high-risk applicants.

---

## 📂 Project Structure

```
project/
│
├── data/
│   ├── raw/                # original dataset
│   ├── processed/          # cleaned dataset
│
├── models/                 # saved encoders, scalers, baseline, optimized, balanced models
│
├── notebooks/              # 01 to 08 Jupyter notebooks
│   ├── 01_data_understanding.ipynb
│   ├── 02_preprocessing_feature_engineering.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_model_building.ipynb
│   ├── 05_model_optimization.ipynb
│   ├── 06_handling_imbalanced_data.ipynb
│   ├── 07_model_evaluation.ipynb
│   └── 08_final_documentation.ipynb
│
├── src/
│   ├── fastapi_app.py      # FastAPI backend demo
│   ├── streamlit_app.py    # Streamlit frontend demo (calls FastAPI)
│   └── __init__.py
│
└── README.md               # project documentation
```

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone <your-repo-url>
cd project
pip install -r requirements.txt
```

Recommended packages:
- `pandas`
- `numpy`
- `scikit-learn`
- `xgboost`
- `imblearn`
- `matplotlib`
- `seaborn`
- `fastapi`
- `uvicorn`
- `streamlit`
- `joblib`

---

## 🚀 Usage

### 1. Run FastAPI Backend
Start the API server:

```bash
uvicorn src.fastapi_app:app --reload
```

- API root: `http://127.0.0.1:8000/` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2F")  
- Interactive docs: `http://127.0.0.1:8000/docs` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fdocs")

#### Example Request (POST `/predict`)
```json
{
  "person_age": 30,
  "person_gender": "male",
  "person_education": "Bachelor",
  "person_income": 50000,
  "person_emp_exp": 5,
  "person_home_ownership": "RENT",
  "loan_amnt": 10000,
  "loan_intent": "PERSONAL",
  "loan_int_rate": 10.5,
  "loan_percent_income": 0.2,
  "cb_person_cred_hist_length": 10,
  "credit_score": 650,
  "previous_loan_defaults_on_file": "No",
  "debt_to_income": 0.25,
  "age_group": "Adult"
}
```

Response:
```json
{
  "loan_status": 1
}
```

---

### 2. Run Streamlit Frontend
Launch the UI:

```bash
streamlit run src/streamlit_app.py
```

- Opens a browser window with input fields (dropdowns + numeric inputs).
- On submit, Streamlit sends the payload to FastAPI and displays the prediction.

---

## 📊 Workflow Summary
- **Notebook 01:** Data understanding  
- **Notebook 02:** Preprocessing & feature engineering  
- **Notebook 03:** Exploratory Data Analysis (EDA)  
- **Notebook 04:** Baseline model building  
- **Notebook 05:** Hyperparameter optimization  
- **Notebook 06:** Handling class imbalance (SMOTE)  
- **Notebook 07:** Model evaluation (metrics, confusion matrices, ROC curves)  
- **Notebook 08:** Final documentation  

---

## 🔮 Future Work
- **Deployment:** Containerize with Docker, deploy to cloud (AWS/GCP/Azure).  
- **Monitoring:** Add drift detection and retraining pipelines.  
- **Explainability:** Integrate SHAP/LIME for interpretable predictions.  
- **Integration:** Build dashboards for loan officers with Streamlit or Power BI.  

---

# 🚀 Deployment

This project is deployed with a **FastAPI backend** on Hugging Face Spaces and a **Streamlit frontend** on Streamlit Community Cloud. Together, they provide a full-stack solution for credit risk assessment.

---

## ⚙️ Backend (FastAPI on Hugging Face Spaces)

- Hosted at:  
  [https://sujith2121-credit-risk-assessment-fastapi.hf.space](https://sujith2121-credit-risk-assessment-fastapi.hf.space)

- Interactive API docs (Swagger UI):  
  [https://sujith2121-credit-risk-assessment-fastapi.hf.space/docs](https://sujith2121-credit-risk-assessment-fastapi.hf.space/docs)

- Endpoint:  
  `POST /predict`  
  Accepts applicant details (age, income, credit score, etc.) and returns loan status prediction.

---

## 🎨 Frontend (Streamlit on Streamlit Community Cloud)

- Hosted at:  
  [https://credit-risk-assessment-stream.streamlit.app/](https://credit-risk-assessment-stream.streamlit.app/)

- Provides a user-friendly interface to input applicant details and view predictions.

---

## 📝 Important Note

Since both apps are hosted on **free tiers**:
- Hugging Face Spaces and Streamlit Community Cloud may **go to sleep when idle**.  
- When accessed after inactivity, they may take a few seconds to **wake up** before responding.  
- This is expected behavior — just wait briefly and the apps will be ready.

---

## 🔗 Related Links

- Backend API Docs: [FastAPI Swagger UI](https://sujith2121-credit-risk-assessment-fastapi.hf.space/docs)  
- Frontend App: [Streamlit UI](https://credit-risk-assessment-stream.streamlit.app/)


## 👨‍💻 Author
- **Yenugu Sujith Reddy**  
- B.Tech Computer Science, VIT (expected 2027)  
- Skilled in Python, ML/DL, FastAPI, Django, cloud-native deployment, and visualization.

---
```

---

