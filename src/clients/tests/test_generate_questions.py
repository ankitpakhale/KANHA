import sys
from pathlib import Path

# add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from clients import Client, OpenAI, Bedrock
from utils import logger

# create the client
client = Client(client_type=Bedrock.__name__)
questions = client.generate_questions(
    num_questions=2,
    difficulty_level="easy",
    programming_language="python",
    topics=["loops", "functions"],
)
logger.debug("➡ questions:", questions)
