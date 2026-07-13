# Customer Churn Prediction - MLOps Deployment

An end-to-end Machine Learning project demonstrating model training, experiment tracking, cloud storage, API development, containerization, and cloud deployment using AWS.

---

## Project Overview

This project predicts whether a customer is likely to churn using an XGBoost classification model.

The trained model is tracked with MLflow, stored in Amazon S3, and served through a FastAPI REST API deployed on AWS Elastic Beanstalk using Docker.

---

## Architecture

```

Customer Dataset
│
▼
Data Preprocessing
│
▼
XGBoost Model
│
▼
MLflow Tracking
│
▼
Model Registry
│
▼
Amazon S3
│
▼
FastAPI
│
▼
Docker
│
▼
AWS Elastic Beanstalk
│
▼
REST API (/predict)

```

---

## Technologies Used

- Python
- Scikit-learn
- XGBoost
- MLflow
- FastAPI
- Docker
- AWS S3
- AWS Elastic Beanstalk
- Boto3
- Git & GitHub

---

## Features

- Customer churn prediction
- MLflow experiment tracking
- Model Registry
- Secure model storage in Amazon S3
- Automatic model download during application startup
- Docker containerization
- REST API using FastAPI
- AWS Elastic Beanstalk deployment
- Interactive Swagger documentation

---

## Project Structure

```

app.py
download_model.py
config.py
Dockerfile
Procfile
requirements.txt
train.py
upload_to_s3.py

```

---

## Model Workflow

1. Train XGBoost model
2. Log experiments using MLflow
3. Register the best model
4. Upload model artifacts to Amazon S3
5. FastAPI downloads the model during startup
6. Load model
7. Predict customer churn
8. Return prediction as JSON

---

## API Endpoint

### POST /predict

### Request

```json
{
    "Age":35,
    "Tenure":5,
    "Total_Spend":1500,
    "Contract_Length":12
}
```
### Response
```
{
    "churn_prediction":0
}

```

### Deployment

The application is deployed on AWS Elastic Beanstalk.

FastAPI automatically downloads the trained model from Amazon S3 before serving prediction requests.
```
