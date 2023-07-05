import boto3
import os
from dotenv import load_dotenv

load_dotenv()


s3 = boto3.resource(
    service_name="s3",
    region_name="us-east-1",
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)

if os.environ["AWS_S3_BUCKET_NAME"] not in s3.buckets.all():
    raise Exception("S3: bucket not found")

bucket = s3.Bucket(os.environ["AWS_S3_BUCKET_NAME"])
