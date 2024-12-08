from typing import Any
from .openai_strategy import OpenAIStrategy
from config import OpenAIConfig
import openai


class OpenAIBaseClient:
    """
    Base client to interact with OpenAI API using a strategy pattern.
    """

    def __init__(self, strategy: OpenAIStrategy) -> None:
        """
        Initialize OpenAIBaseClient with a specific strategy.
        """
        self.strategy = strategy
        self.model = OpenAIConfig.OPENAI_MODEL
        self.temperature = float(OpenAIConfig.OPENAI_TEMPERATURE)
        self.max_tokens = int(OpenAIConfig.OPENAI_MAX_TOKENS)
        openai.api_key = OpenAIConfig.OPENAI_API_KEY

    def execute(self, **kwargs: Any) -> Any:
        """
        Execute the selected strategy with the provided arguments.
        """
        return self.strategy.execute(client=self, **kwargs)
