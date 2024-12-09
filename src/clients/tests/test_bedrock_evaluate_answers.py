from bedrock_client import BaseClient
from bedrock_client.strategy.generate_questions_strategy import (
    GenerateQuestionsStrategy,
)
from bedrock_client.strategy.evaluate_answers_strategy import EvaluateAnswersStrategy

# Initialize strategies
generate_strategy = GenerateQuestionsStrategy()
evaluate_strategy = EvaluateAnswersStrategy()

# Generate questions
bedrock_client = BaseClient(strategy=generate_strategy)
response = bedrock_client.execute(
    model_id="your-model-id", input_text="Generate questions on Python loops."
)
print(response)

# Evaluate answers
bedrock_client.strategy = evaluate_strategy
response = bedrock_client.execute(
    model_id="your-model-id", input_text="Evaluate this answer: '...'"
)
print(response)
