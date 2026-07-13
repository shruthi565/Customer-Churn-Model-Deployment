import os
import boto3
from xgboost import XGBClassifier
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# S3 Configuration
BUCKET_NAME = "shruthika-customer-churn-model"
S3_MODEL_PATH = "registered_model/artifacts/model.ubj"
LOCAL_MODEL_PATH = "model/model.ubj"

def download_model_from_s3():
    if os.path.exists(LOCAL_MODEL_PATH):
        print("Model already exists")
        return
    print("Model not found. Downloading from S3...")
    os.makedirs("model", exist_ok=True)
    s3 = boto3.client("s3")
    s3.download_file(BUCKET_NAME,S3_MODEL_PATH,LOCAL_MODEL_PATH)
    print("Model downloaded successfully")

# Download model when application starts
download_model_from_s3()

# Load model
model = XGBClassifier()
model.load_model(LOCAL_MODEL_PATH)

print("Model loaded successfully")

class CustomerData(BaseModel):
    Age: int
    Tenture: int
    Total_Spend: float
    Contract_Length:int

@app.post("/predict")
def predict(data: CustomerData):

    try:
        input_data = [[
            data.Age,
            data.Tenture,
            data.Total_Spend,
            data.Contract_Length
        ]]


        prediction = model.predict(input_data)

        return {
            "churn_prediction": int(prediction[0])
        }

    except Exception as e:
        return {
            "error": str(e)
        }
    