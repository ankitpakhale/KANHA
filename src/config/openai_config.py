import os
from config import BaseConfig


class OpenAIConfig(BaseConfig):
    """OpenAI API configuration"""

    # general openai api settings
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_TEMPERATURE = float(
        os.getenv("OPENAI_TEMPERATURE", 0.2)
    )  # default temperature

    # model-specific settings
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")  # default model
    OPENAI_COMPLETION_TIMEOUT = int(
        os.getenv("OPENAI_COMPLETION_TIMEOUT", 90)
    )  # deafult timeout in seconds
    OPENAI_MAX_TOKENS = int(
        os.getenv("OPENAI_MAX_TOKENS", 4096)
    )  # default max tokens for responses

    @staticmethod
    def validate():
        """ensures that required openai configurations are available"""
        if not OpenAIConfig.OPENAI_API_KEY:
            raise EnvironmentError("Missing OPENAI_API_KEY in environment variables.")
