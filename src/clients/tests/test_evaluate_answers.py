import sys
from pathlib import Path

# add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))


import json
from clients import Client, OpenAI, Bedrock

# load the evaluate_answers.json file
with open("clients/payload/request_examples/evaluate_answers.json", "r") as file:
    evaluate_answers_data = json.load(file)

# create the client
client = Client(client_type=Bedrock.__name__)
questions = client.evaluate_answers(user_code=evaluate_answers_data)

print("➡ questions:", questions)
