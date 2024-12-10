import sys
from pathlib import Path

# add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))


from clients import Factory, OpenAI, Bedrock

# create the client
client = Factory(client_type=Bedrock.__name__)
questions = client.generate_questions(
    num_questions=2,
    difficulty_level="easy",
    programming_language="python",
    topics=["loops", "functions"],
)
print("➡ questions:", questions)
