import os
from config import BaseConfig


class AWSConfig(BaseConfig):
    # AWS Configuration
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
    AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
