from typing import Optional, Any
from config import GeneralConfig
from .client_list import Bedrock, OpenAI


class Factory:
    def __init__(self, client_type: Optional[Any] = GeneralConfig.ACTIVE_CLIENT) -> Any:
        __client_type = OpenAI if client_type == OpenAI.__name__ else Bedrock
        self.client_type = __client_type()

    def generate_questions(self, **kwargs):
        return self.client_type.generate_questions(**kwargs)

    def evaluate_answers(self, **kwargs):
        return self.client_type.evaluate_answers(**kwargs)
