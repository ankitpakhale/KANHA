import sys
from pathlib import Path

# Add the `src` directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from clients.openai_client import OpenAIBaseClient, GenerateQuestionsStrategy

# instantiate OpenAIClient with GenerateQuestionsStrategy
client = OpenAIBaseClient(GenerateQuestionsStrategy())

questions = client.execute(
    num_questions=1,
    difficulty_level="easy",
    programming_language="python",
    topics=["loops", "functions"],
)
print("➡ questions:", questions)
