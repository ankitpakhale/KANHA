from typing import Any


class ClientFactory:
    def __init__(self, client_type: Any) -> Any:
        self.client_type = client_type

    def generate_questions(self, **kwargs):
        return self.client_type.generate_questions(**kwargs)

    def evaluate_answers(self, **kwargs):
        return self.client_type.evaluate_answers(**kwargs)
