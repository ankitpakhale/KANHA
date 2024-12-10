from typing import Any, Dict
import boto3
import json
from clients import Prompt
from ..base import BedrockBaseStrategy
import requests
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest


class GenerateQuestionsStrategy(BedrockBaseStrategy, Prompt):
    """
    Strategy to generate programming questions using AWS Bedrock.
    """

    # flake8: noqa: F821
    def execute(self, client: "BedrockBaseClient", **kwargs: Any) -> Dict:
        """
        Generate programming questions using Bedrock API.
        """
        # TODO: Add actual logic to get data from Amazon Bedrock
        response_body = [
            {
                "q_type": "MCQ",
                "question": "In Python, which loop is used when the number of iterations is known?",
                "options": ["for loop", "while loop", "do-while loop", "foreach loop"],
                "correct_answer": "for loop",
            },
            {
                "q_type": "MCQ",
                "question": "What is the purpose of a return statement in Python functions?",
                "options": [
                    "To terminate the function execution",
                    "To skip the current iteration",
                    "To print a value to the console",
                    "To define a new variable",
                ],
                "correct_answer": "To terminate the function execution",
            },
        ]
        return response_body
