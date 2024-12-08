from clients.openai_client import answer_evaluation_client

# instantiate OpenAIClient with EvaluateAnswersStrategy
evaluation = answer_evaluation_client.execute(
    user_code={"Q1": "def example(): pass", "Q2": "for i in range(5): print(i)"}
)
print("➡ evaluation:", evaluation)
