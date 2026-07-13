import pandas as pd
import mlflow
import mlflow.xgboost
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier

# MLflow Configuration
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Customer_Churn_Prediction")
print("Tracking URI:", mlflow.get_tracking_uri())
experiment = mlflow.get_experiment_by_name("Customer_Churn_Prediction")
print(experiment)

# Load Dataset
df = pd.read_csv("customer_data.csv", sep="\t")
print("Dataset Columns:")
print(df.columns)

# Encode Categorical Columns
encoder = LabelEncoder()
df["Contract Length"] = encoder.fit_transform(df["Contract Length"])

# Features and Target
X = df[[
        "Age",
        "Tenure",
        "Total Spend",
        "Contract Length"
    ]]
y = df["Churn"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.20,random_state=42)

# Start MLflow Run
with mlflow.start_run():

    # Create Model
    model = XGBClassifier(random_state=42,eval_metric="logloss")
    # Train Model
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)

    print("\nAccuracy:", accuracy)
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    # Log Parameters
    mlflow.log_param("Algorithm", "XGBoost")
    mlflow.log_param("Random_State", 42)
    mlflow.log_param("Test_Size", 0.20)

    # Log Metrics
    mlflow.log_metric("Accuracy", accuracy)

    # Register Model
    mlflow.xgboost.log_model(xgb_model=model,name="model",registered_model_name="Customer_Churn_Model")
    print("\nModel registered successfully in MLflow.")

# Save Local Files
joblib.dump(model, "churn_model.joblib")
joblib.dump(encoder, "label_encoder.joblib")

print("\nModel saved successfully.")
print("Label Encoder saved successfully.")
