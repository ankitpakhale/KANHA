from typing import Optional, Any, Union
from config import GeneralConfig
from .client_types import Bedrock, OpenAI


class Client:
    def __init__(self, client_type: Optional[Any] = GeneralConfig.ACTIVE_CLIENT) -> Any:
        __client_type = OpenAI if client_type == OpenAI.__name__ else Bedrock
        self.client_type = __client_type()

    def generate_questions(self, payload: Union[list, dict]):
        return self.client_type.generate_questions(payload)

    def evaluate_answers(self, payload: Union[list, dict]):
        return self.client_type.evaluate_answers(payload)
