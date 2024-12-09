from ..base import BedrockBaseStrategy
from typing import Any


class EvaluateAnswersStrategy(BedrockBaseStrategy):
    """
    Strategy to evaluate answers using AWS Bedrock.
    """

    def execute(self, client: Any, model_id: str, input_text: str) -> Any:
        """
        Executes answer evaluation using Bedrock.
        """
        response = client.invoke_model(
            modelId=self.model,
            contentType="application/json",
            body={"prompt": input_text, "maxTokens": 50},
        )
        print("➡ EvaluateAnswersStrategy:", response["body"])
        return response["body"]
