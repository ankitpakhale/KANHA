from ..base import BedrockBaseStrategy
from typing import Any


class GenerateQuestionsStrategy(BedrockBaseStrategy):
    """
    Strategy to generate questions using AWS Bedrock.
    """

    def execute(self, client: Any, model_id: str, input_text: str) -> Any:
        """
        Executes question generation using Bedrock.
        """
        response = client.invoke_model(
            modelId=model_id,
            contentType="application/json",
            body={"prompt": input_text, "maxTokens": 100},
        )
        print("➡ GenerateQuestionsStrategy:", response["body"])
        return response["body"]
