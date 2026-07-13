import os
import boto3

BUCKET_NAME = "shruthika-customer-churn-model"

s3 = boto3.client("s3")

LOCAL_DIR = "registered_model/artifacts"

for file in os.listdir(LOCAL_DIR):

    local_path = os.path.join(LOCAL_DIR, file)

    s3_key = f"registered_model/artifacts/{file}"

    s3.upload_file(local_path, BUCKET_NAME, s3_key)
print("Upload Complete!")