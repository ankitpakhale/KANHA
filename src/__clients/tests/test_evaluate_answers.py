import sys
from pathlib import Path

# add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from clients.openai_client import OpenAIBaseClient, EvaluateAnswersStrategy

# instantiate OpenAIClient with EvaluateAnswersStrategy
client = OpenAIBaseClient(EvaluateAnswersStrategy())

evaluation = client.execute(
    user_code={"Q1": "def example(): pass", "Q2": "for i in range(5): print(i)"}
)
print("➡ evaluation:", evaluation)
