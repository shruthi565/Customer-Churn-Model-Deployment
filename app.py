import os
import boto3

from xgboost import XGBClassifier
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI()
# Frontend Configuration
app.mount("/static", StaticFiles(directory="frontend"),name="static")
@app.get("/")
def home():
    return FileResponse("frontend/index.html")

# S3 Model Configuration
BUCKET_NAME = "shruthika-customer-churn-model"
S3_MODEL_PATH = "registered_model/artifacts/model.ubj"
LOCAL_MODEL_PATH = "model/model.ubj"



def download_model_from_s3():
    if os.path.exists(LOCAL_MODEL_PATH):
        print("Model already exists")
        return
    print("Downloading model from S3...")
    os.makedirs("model", exist_ok=True)
    s3 = boto3.client("s3")

    s3.download_file(BUCKET_NAME,S3_MODEL_PATH,LOCAL_MODEL_PATH)
    print("Model downloaded successfully")

# Download model during startup
download_model_from_s3()

# Load XGBoost Model
model = XGBClassifier()
model.load_model(LOCAL_MODEL_PATH)
print("Model loaded successfully")

# Input Schema
class CustomerData(BaseModel):
    Age: int
    Tenure: int
    Total_Spend: float
    Contract_Length: int

# Prediction API
@app.post("/predict")
def predict(data: CustomerData):
    try:
        input_data = [[
            data.Age,
            data.Tenure,
            data.Total_Spend,
            data.Contract_Length
        ]]
        prediction = model.predict(input_data)
        result = int(prediction[0])
        return {
            "churn_prediction": result,
            "message":"Customer will churn"
            if result == 1
            else
            "Customer will stay"
        }
    except Exception as e:
        return {
            "error": str(e)

        }
