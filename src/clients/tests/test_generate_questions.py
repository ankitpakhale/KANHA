from clients.openai_client import question_generation_client

# instantiate OpenAIClient with GenerateQuestionsStrategy
questions = question_generation_client.execute(
    num_questions=2,
    difficulty_level="easy",
    programming_language="python",
    topics=["loops", "functions"],
)
print("➡ questions:", questions)
