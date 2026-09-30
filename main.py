import pandas as pd
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("churn_pipeline.pkl")

class Customer(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.get("/")
def home():
    return {
        "message":"Yes it's working amigo:"
    }

@app.post("/predict")
def predict(customer:Customer):
    customer_data=pd.DataFrame([customer.model_dump()])

    prediction = int(model.predict(customer_data)[0])

    if prediction == 1:
        result = "Customer is likely to churn"
    else:
        result = "Customer is likely to stay" 

    return {
        "prediction":prediction,
        "result":result
    }  