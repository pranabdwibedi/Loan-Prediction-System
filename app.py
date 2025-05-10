from fastapi import FastAPI
from pydantic import BaseModel
import joblib 
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

model = joblib.load('loan_status_predictor.pkl')

app = FastAPI()

num_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']
scaler = joblib.load('vector.pkl')

# Gender	Married	Dependents	Education	Self_Employed	ApplicantIncome	CoapplicantIncome	LoanAmount	Loan_Amount_Term	Credit_History	Property_Area

class LoanApproval(BaseModel):
    Gender: float 
    Married: float
    Dependents:float
    Education: float
    Self_Employed: float
    ApplicantIncome:float
    CoapplicantIncome:float
    LoanAmount:float 
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: float

@app.post("/predict")
async def predict_loan_status(application: LoanApproval):
    input_data = pd.DataFrame([application.model_dump()])
    input_data[num_cols] = scaler.transform(input_data[num_cols])

    result = model.predict(input_data)
    
    if result[0] == 1:
        return {'Loan_Status': "Approved"}
    else:
        return {'Loan_Status': "Not Approved"}
    
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["*"] for all origins (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)