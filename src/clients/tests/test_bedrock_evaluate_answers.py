import sys
from pathlib import Path

# add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from clients.bedrock_client import BedrockBaseClient, EvaluateAnswersStrategy

# instantiate BedrockClient with EvaluateAnswersStrategy
client = BedrockBaseClient(EvaluateAnswersStrategy())

evaluation = client.execute(
    user_code={"Q1": "def example(): pass", "Q2": "for i in range(5): print(i)"}
)
print("➡ evaluation:", evaluation)
