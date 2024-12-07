import os
import openai
import json
import time
from dotenv import load_dotenv
from constants import (
    TEMPERATURE,
    MAX_TOKENS,
    GPT_MODEL,
)
from prompts import question_generation_system_prompt, answer_evaluation_prompt

load_dotenv()

# set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def user_prompt(
    num_questions: int = 20,
    difficulty_level: str = "easy",
    programming_language: str = "python",
    topics: str = "all",
):
    return f"""
    Generate a {num_questions} personalized questions for a programming assessment based on the
    following user inputs:

    1. Difficulty Level: {difficulty_level}
    2. Programming Language: {programming_language}
    3. Topics: {topics}
    """


def __generate_questions(user_query: str):
    """
    Generates a list of questions based on the provided prompt using OpenAI's GPT API.
    """
    # make the API request
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": question_generation_system_prompt},
            {"role": "user", "content": user_query},
        ],
        temperature=TEMPERATURE,  # reduce creativity for strict adherence
        max_tokens=MAX_TOKENS,  # adjust to allow for full responses
    )

    # parse and clean the response
    content = response.choices[0].message["content"].strip()

    try:
        # try to parse the response into JSON
        parsed_response = json.loads(content)

        # ensure it's an array of question objects
        if not isinstance(parsed_response, list):
            raise ValueError("The response is not a valid list of questions.")

        for question in parsed_response:
            if "q_type" not in question or "question" not in question:
                raise ValueError("Missing required fields in one or more questions.")

        return parsed_response

    except (json.JSONDecodeError, ValueError) as e:
        # if the response is invalid, raise an error with relevant information
        print(f"Error generating valid JSON: {e}")
        print("Invalid response content:", content)
        raise


def __retry_mechanism(func, arguments, retry: int = 3, delay: int = 1):
    """
    Retry mechanism to ensure valid data is returned from GPT.
    """
    for attempt in range(1, retry + 1):
        try:
            print(f"➡ Attempt {attempt} of {retry}")
            result = func(arguments)
            print("➡ Request completed successfully.")
            return result
        except Exception as e:
            print(f"➡ Error on attempt {attempt}: {e}")

            # if the error is related to invalid data, modify the prompt and try again
            if "invalid JSON" in str(e) or "missing required fields" in str(e):
                print(f"➡ Retrying with adjusted prompt for attempt {attempt + 1}")
                arguments = user_prompt(
                    num_questions=2,  # Or modify based on requirements
                    difficulty_level="medium",  # Modify if necessary
                    programming_language="python",
                    topics="all",
                )  # Adjust as needed for next retry

        # if all retries fail, raise an exception
        if attempt == retry:
            raise Exception("All retry attempts failed.")

        # exponential backoff
        time.sleep(delay * attempt)


def generate_questions(user_query: str):
    """
    Generates a list of questions based on the provided prompt using OpenAI's GPT API.
    """
    return __retry_mechanism(__generate_questions, user_query)


if __name__ == "__main__":
    try:
        questions = generate_questions(
            user_query=user_prompt(
                num_questions=2,
                difficulty_level="easy",
                programming_language="python",
                topics="Type Hinting",
            )
        )
        print("➡ Questions:", json.dumps(questions, indent=4))
    except Exception as e:
        print(f"❌ Failed to generate questions: {e}")
