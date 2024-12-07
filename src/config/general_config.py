import os
from config import BaseConfig


class GeneralConfig(BaseConfig):
    ENV = os.getenv("ENV", "local")
    PORT = int(os.getenv("PORT", 8080))  # convert to integer
