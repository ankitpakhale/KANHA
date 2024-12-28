import os
from src.config import BaseConfig


class AWSConfig(BaseConfig):
    """AWS-related configuration"""

    # aws general settings
    AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")  # default region
    AWS_ACCESS_KEY = os.getenv(
        "AWS_ACCESS_KEY", ""
    )  # aws access key from environment variables
    AWS_SECRET_KEY = os.getenv(
        "AWS_SECRET_KEY", ""
    )  # aws secret key from environment variables

    # bedrock-specific settings
    BEDROCK_ENDPOINT = os.getenv(
        "BEDROCK_ENDPOINT", "https://bedrock.amazonaws.com"
    )  # default bedrock endpoint
    BEDROCK_MODEL = os.getenv(
        "BEDROCK_MODEL", "amazon.titan-tg1-large"
    )  # default bedrock model
    BEDROCK_MAX_TOKENS = int(
        os.getenv("BEDROCK_MAX_TOKENS", 4096)
    )  # default max tokens for responses
    BEDROCK_TEMPERATURE = float(
        os.getenv("BEDROCK_TEMPERATURE", 0.3)
    )  # default bedrock temperature

    # rds-specific settings
    RDS_HOST = os.getenv("RDS_HOST", "localhost")  # default RDS host
    RDS_PORT = int(os.getenv("RDS_PORT", 5432))  # default RDS port
    RDS_USERNAME = os.getenv("RDS_USERNAME", "postgres")  # default RDS username
    RDS_PASSWORD = os.getenv("RDS_PASSWORD", "password")  # default RDS password
    RDS_DATABASE = os.getenv("RDS_DATABASE", "kanha_db")  # default RDS database

    # s3-specific settings
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "")

    @staticmethod
    def validate():
        """ensures that required aws configurations are available"""
        missing_keys = []
        for key in [
            "AWS_ACCESS_KEY",
            "AWS_SECRET_KEY",
            "BEDROCK_ENDPOINT",
            "S3_BUCKET_NAME",
        ]:
            if not getattr(AWSConfig, key):
                missing_keys.append(key)
        if missing_keys:
            raise EnvironmentError(
                f"Missing AWS configuration keys: {', '.join(missing_keys)}"
            )
