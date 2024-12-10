from typing import Optional
from ..base import Base
from config import AWSConfig


class Bedrock(Base):
    def __init__(self) -> None:
        # config data
        self.model = AWSConfig.BEDROCK_MODEL
        self.temperature = AWSConfig.BEDROCK_TEMPERATURE
        self.max_tokens = AWSConfig.BEDROCK_MAX_TOKENS

    def generate_questions(
        self,
        difficulty_level: str,
        programming_language: str,
        topics: list,
        num_questions: Optional[int] = 20,
    ):
        """
        Core logic to generate questions from OpenAI client
        """
        __system_prompt = self.get_question_generation_system_prompt(
            difficulty_level=difficulty_level,
            programming_language=programming_language,
            topics=topics,
            num_questions=num_questions,
        )
        __user_prompt = self.get_question_generation_user_prompt(
            difficulty_level=difficulty_level,
            programming_language=programming_language,
            topics=topics,
            num_questions=num_questions,
        )
        __generation = [
            {
                "q_type": "MCQ",
                "question": "In Python, which loop is used when a specific condition needs to be checked before each iteration?",
                "options": ["for loop", "while loop", "do-while loop", "foreach loop"],
                "correct_answer": "while loop",
            },
            {
                "q_type": "MCQ",
                "question": "Which keyword is used to define a function in Python?",
                "options": ["method", "def", "func", "define"],
                "correct_answer": "def",
            },
            {
                "q_type": "MCQ",
                "question": "What is the purpose of a return statement in a Python function?",
                "options": [
                    "To stop the function execution",
                    "To return a value from the function",
                    "To print a message",
                    "To define a new variable",
                ],
                "correct_answer": "To return a value from the function",
            },
            {
                "q_type": "MCQ",
                "question": "Which of the following is true about the range() function in Python?",
                "options": [
                    "It generates a list of numbers",
                    "It is used to iterate over a sequence of numbers",
                    "It is used to define a range for a loop",
                    "It is used to check the length of a list",
                ],
                "correct_answer": "It is used to iterate over a sequence of numbers",
            },
            {
                "q_type": "MCQ",
                "question": "What is the output of the following code snippet?\n\n```python\nfor i in range(3):\n    print(i)\n```",
                "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2 3 4"],
                "correct_answer": "0 1 2",
            },
            {
                "q_type": "MCQ",
                "question": "Which keyword is used to exit a loop prematurely in Python?",
                "options": ["break", "stop", "exit", "end"],
                "correct_answer": "break",
            },
            {
                "q_type": "MCQ",
                "question": "What is the purpose of the 'pass' statement in Python?",
                "options": [
                    "To terminate the program",
                    "To skip a block of code",
                    "To print a message",
                    "To define a new function",
                ],
                "correct_answer": "To skip a block of code",
            },
            {
                "q_type": "MCQ",
                "question": "Which of the following is true about recursion in Python?",
                "options": [
                    "It is not supported in Python",
                    "It is a loop structure",
                    "It is a function calling itself",
                    "It can only be used with while loops",
                ],
                "correct_answer": "It is a function calling itself",
            },
            {
                "q_type": "MCQ",
                "question": "What is the purpose of the 'continue' statement in Python?",
                "options": [
                    "To exit the loop",
                    "To skip the current iteration and continue with the next",
                    "To restart the loop",
                    "To print a message",
                ],
                "correct_answer": "To skip the current iteration and continue with the next",
            },
            {
                "q_type": "MCQ",
                "question": "Which of the following is true about functions in Python?",
                "options": [
                    "A function can only return one value",
                    "A function can have multiple return statements",
                    "A function cannot accept arguments",
                    "A function cannot call another function",
                ],
                "correct_answer": "A function can have multiple return statements",
            },
            {
                "q_type": "MCQ",
                "question": "What does the 'def' keyword stand for in Python?",
                "options": ["Define", "Declare", "Defend", "Default"],
                "correct_answer": "Define",
            },
            {
                "q_type": "MCQ",
                "question": "Which of the following is true about function arguments in Python?",
                "options": [
                    "All arguments in Python functions are required",
                    "Default arguments must be placed before non-default arguments",
                    "Keyword arguments cannot be used in Python functions",
                    "Arguments in Python functions are not type-specific",
                ],
                "correct_answer": "Default arguments must be placed before non-default arguments",
            },
            {
                "q_type": "MCQ",
                "question": "What is the purpose of the 'lambda' keyword in Python?",
                "options": [
                    "To define a new class",
                    "To create anonymous functions",
                    "To import external modules",
                    "To handle exceptions",
                ],
                "correct_answer": "To create anonymous functions",
            },
            {
                "q_type": "MCQ",
                "question": "Which of the following is true about the 'global' keyword in Python?",
                "options": [
                    "It is used to define a global variable",
                    "It is used to declare a function as global",
                    "It is used to access a global variable within a function",
                    "It is used to restrict variable scope",
                ],
                "correct_answer": "It is used to access a global variable within a function",
            },
            {
                "q_type": "MCQ",
                "question": "What is the output of the following code snippet?\n\n```python\nx = 5\n\ndef func():\n    x = 10\n    print(x)\n\nfunc()\nprint(x)\n```",
                "options": ["5 10", "10 5", "10 10", "5 5"],
                "correct_answer": "10 5",
            },
            {
                "q_type": "MCQ",
                "question": "Which of the following is true about the 'return' statement in Python functions?",
                "options": [
                    "A function can have multiple return statements",
                    "The return statement is mandatory in all functions",
                    "The return statement can only return integers",
                    "The return statement stops the function execution",
                ],
                "correct_answer": "The return statement stops the function execution",
            },
            {
                "q_type": "MCQ",
                "question": "What is the purpose of the 'yield' keyword in Python?",
                "options": [
                    "To return a value from a function",
                    "To define a new variable",
                    "To stop the function execution",
                    "To create a generator",
                ],
                "correct_answer": "To create a generator",
            },
            {
                "q_type": "MCQ",
                "question": "Which of the following is true about the 'pass' statement in Python?",
                "options": [
                    "It is used to exit a loop",
                    "It is used to skip a block of code",
                    "It is used to define a new function",
                    "It is used to print a message",
                ],
                "correct_answer": "It is used to skip a block of code",
            },
            {
                "q_type": "MCQ",
                "question": "What is the purpose of the 'assert' statement in Python?",
                "options": [
                    "To handle exceptions",
                    "To define a new variable",
                    "To check if a condition is true",
                    "To stop the program",
                ],
                "correct_answer": "To check if a condition is true",
            },
            {
                "q_type": "MCQ",
                "question": "Which keyword is used to define a default argument in a Python function?",
                "options": ["default", "def", "defaultarg", "None of the above"],
                "correct_answer": "None of the above",
            },
        ]

        return __generation

    def evaluate_answers(self, user_code: dict):
        """
        Core logic to evaluate users answer using OpenAI client
        """
        __system_prompt = self.get_answer_evaluation_system_prompt(user_code=user_code)
        __user_prompt = self.get_answer_evaluation_user_prompt(user_code=user_code)

        __evaluation = [
            {
                "q_id": "psq01223211122",
                "feedback": [
                    {
                        "correctness": "The function correctly finds the maximum product of three numbers from the list. It handles both positive and negative integers by sorting the list and considering the cases where the maximum product can be achieved by multiplying the two smallest numbers with the largest number or by multiplying the three largest numbers."
                    },
                    {
                        "areas_for_improvement": "1. The function does not handle the case where the list contains both negative and positive integers. In such cases, the maximum product can be achieved by either multiplying the three largest positive numbers or by multiplying the two smallest (most negative) numbers with the largest positive number. This case is not considered in the current implementation.\n2. The function sorts the entire list, which has a time complexity of O(nlogn). This can be improved by finding the three largest numbers and two smallest numbers in a single pass through the list, which would have a time complexity of O(n).\n3. The function could benefit from more descriptive variable names for better readability."
                    },
                    {
                        "strengths": "The function correctly handles cases where the maximum product is achieved by either multiplying the two smallest numbers with the largest number or by multiplying the three largest numbers. The code is concise and easy to understand."
                    },
                ],
                "points": "4",
            },
            {
                "q_id": "psq01293211122",
                "feedback": [
                    {
                        "correctness": "The function correctly finds the longest common prefix string amongst an array of strings. It handles the case where there is no common prefix and returns an empty string."
                    },
                    {
                        "areas_for_improvement": "1. The function could be optimized by using the zip function to compare characters of the strings simultaneously instead of iterating character by character.\n2. The variable name 'strs' could be more descriptive to indicate that it represents an array of strings.\n3. The comment '# Start by assuming the first string is the prefix' is misleading as it actually assigns the first string as the prefix, not assumes it."
                    },
                    {
                        "strengths": "The function correctly handles finding the longest common prefix and the case where there is no common prefix. The code is structured and easy to follow."
                    },
                ],
                "points": "7",
            },
        ]

        return __evaluation
