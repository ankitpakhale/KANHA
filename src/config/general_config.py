import os
from config import BaseConfig


class GeneralConfig(BaseConfig):
    ENV = os.getenv("ENV", "local")
    PORT = int(os.getenv("PORT", 8080))  # convert to integer
    Q_GENERATOR = os.getenv(
        "Q_GENERATOR", "OpenAIClient"
    )  # default Q_GENERATOR is OpenAIClient

    # validation: Ensure Q_GENERATOR can only be "OpenAIClient" or "AWSBedrockClient"
    if Q_GENERATOR not in ["OpenAIClient", "AWSBedrockClient"]:
        raise ValueError(
            f"Invalid Q_GENERATOR value: {Q_GENERATOR}. Must be 'OpenAIClient' or 'AWSBedrockClient'."
        )
