import os
import boto3

BUCKET_NAME = "shruthika-customer-churn-model"

LOCAL_DIR = "downloaded_model"

os.makedirs(LOCAL_DIR, exist_ok=True)

s3 = boto3.client("s3")

files = [
    "MLmodel",
    "model.ubj",
    "conda.yaml",
    "python_env.yaml",
    "requirements.txt"
]

for file in files:

    print(f"Downloading {file}...")

    s3.download_file(
        BUCKET_NAME,
        f"registered_model/artifacts/{file}",
        os.path.join(LOCAL_DIR, file)
    )

print("Download successful!")