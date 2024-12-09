from typing import Any
from .base_strategy import BedrockBaseStrategy
from config import AWSConfig


class BedrockBaseClient:
    """
    Base client to interact with OpenAI API using a strategy pattern.
    """

    def __init__(self, strategy: BedrockBaseStrategy) -> None:
        """
        Initialize BedrockBaseClient with a specific strategy.
        """
        self.strategy = strategy
        self.model = AWSConfig.BEDROCK_MODEL
        self.max_tokens = AWSConfig.BEDROCK_MODEL
        self.region = AWSConfig.AWS_REGION
        self.access_key = AWSConfig.AWS_ACCESS_KEY
        self.secret_key = AWSConfig.AWS_SECRET_KEY

    def execute(self, **kwargs: Any) -> Any:
        """
        Execute the selected strategy with the provided arguments.
        """
        return self.strategy.execute(client=self, **kwargs)
