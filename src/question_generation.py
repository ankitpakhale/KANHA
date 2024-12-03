import os
import openai
from dotenv import load_dotenv
from constants import (
    QUESTION_GENERATION_SYSTEM_PROMPT,
    TEMPERATURE,
    MAX_TOKENS,
    GPT_MODEL,
)

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
    # construct the input for the API
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[
            {"role": "system", "content": QUESTION_GENERATION_SYSTEM_PROMPT},
            {"role": "user", "content": user_query},
        ],
        temperature=TEMPERATURE,  # reduce creativity for strict adherence
        max_tokens=MAX_TOKENS,  # adjust to allow for full responses
    )
    # parse the response
    content = response.choices[0].message["content"].strip()
    # convert to dict if JSON-like
    return eval(content)


def __retry_mechanism(func: __generate_questions, arguments, retry: int = 3):
    print(f"➡ ############# func:{func}")
    print(f"➡ ############# arguments:{arguments}")
    print(f"➡ ############# Current Retry:{retry}")

    if retry == 0:
        raise Exception("Error in Generating Questions")

    try:
        data = func(arguments)
        print("➡ ###################### Request Completed")
        print(f"➡ ###################### data: {data}")
        return data
    except Exception as e:
        print(f"➡ ###################### Error Occured: {e} \n\n\n\n")
        return __retry_mechanism(func, arguments, retry=retry - 1)


def generate_questions(user_query: str):
    """
    Generates a list of questions based on the provided prompt using OpenAI's GPT API.
    """
    return __retry_mechanism(__generate_questions, user_query)


if __name__ == "__main__":
    questions = generate_questions(
        user_query=user_prompt(
            num_questions=2,
            difficulty_level="easy",
            programming_language="python",
            topics="Type Hinting",
        )
    )
    print("➡ questions:", questions)
