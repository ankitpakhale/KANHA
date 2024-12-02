import os
import openai
from dotenv import load_dotenv
from prompt import QUESTION_GENERATION_SYSTEM_PROMPT

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


def generate_questions(user_query):
    """
    Generates a list of questions based on the provided prompt using OpenAI's GPT API.
    """
    try:
        # construct the input for the API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": QUESTION_GENERATION_SYSTEM_PROMPT},
                {"role": "user", "content": user_query},
            ],
            temperature=0.2,  # reduce creativity for strict adherence
            max_tokens=1500,  # adjust to allow for full responses
        )
        # parse the response
        content = response.choices[0].message["content"].strip()

        # convert to dict if JSON-like
        return eval(content)

    except openai.APIError as e:
        print("➡ error occurred: {e}:")
        return []


# example usage
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
