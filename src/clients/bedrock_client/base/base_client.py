import boto3
from typing import Any
from config import AWSConfig


class BedrockBaseClient:
    """
    Core client for interacting with AWS Bedrock.
    """

    # flake8: noqa: F821
    def __init__(self, strategy: "BedrockStrategy"):
        self.strategy = strategy
        self.client = boto3.client("bedrock")  # AWS Bedrock client initialization

        self.model = AWSConfig.BEDROCK_MODEL

    def execute(self, *args: Any, **kwargs: Any) -> Any:
        """
        Executes the strategy.
        """
        return self.strategy.execute(self.client, *args, **kwargs)
