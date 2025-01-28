from typing import Optional, Any, Union, Dict
from app.config import GeneralConfig
from .client_types import BedrockClient, OpenAIClient


class Client:
    def __init__(self, client_type: Optional[Any] = GeneralConfig.ACTIVE_CLIENT) -> Any:
        __client_type = (
            OpenAIClient if client_type == OpenAIClient.__name__ else BedrockClient
        )
        self.client_type = __client_type()

    def generate_questions(self, payload: Dict[str, str]):
        return self.client_type.generate_questions(payload)

    def evaluate_answers(self, payload: Union[list, dict]):
        return self.client_type.evaluate_answers(payload)
