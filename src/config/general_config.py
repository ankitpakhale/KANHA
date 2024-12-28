import os
from src.config import BaseConfig


CLIENT_LIST = ["OpenAI", "Bedrock"]


class GeneralConfig(BaseConfig):
    ENV = os.getenv("ENV", "local")
    APP_PORT = int(os.getenv("APP_PORT", 8080))  # convert to integer
    APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
    ACTIVE_CLIENT = os.getenv(
        "ACTIVE_CLIENT", "OpenAI"
    )  # default ACTIVE_CLIENT is OpenAI

    # validation: Ensure ACTIVE_CLIENT can only be "OpenAI" or "Bedrock"
    if ACTIVE_CLIENT not in CLIENT_LIST:
        raise ValueError(
            f"Invalid ACTIVE_CLIENT value: {ACTIVE_CLIENT}. Must be {', '.join(CLIENT_LIST)}."
        )
