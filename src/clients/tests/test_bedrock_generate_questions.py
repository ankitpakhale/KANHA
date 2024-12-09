import sys
from pathlib import Path

# add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from clients.bedrock_client import BedrockBaseClient, GenerateQuestionsStrategy

# instantiate OpenAIClient with GenerateQuestionsStrategy
client = BedrockBaseClient(GenerateQuestionsStrategy())

questions = client.execute(
    num_questions=2,
    difficulty_level="easy",
    programming_language="python",
    topics=["loops", "functions"],
)
print("➡ questions:", questions)
