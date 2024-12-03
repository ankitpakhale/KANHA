from bottle import Bottle, request, response

from question_generation import (
    user_prompt as __user_prompt,
    generate_questions as __generate_questions,
)
from functools import lru_cache

app = Bottle()


def handle_response(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            __status_code = result.get("status_code", 200)
            __payload = result.get("payload")
            __message = result.get("message")

            response.status = __status_code
            return {
                "status": True,
                "payload": __payload,
                "message": __message,
                "status_code": __status_code,
            }
        except Exception as e:
            response.status = 500
            return {
                "status": False,
                "payload": {},
                "message": str(e),
                "status_code": 500,
            }

    return wrapper


@app.route("/ping")
@handle_response
@lru_cache()
def ping():
    return {"payload": {}, "message": "PONG", "status_code": 200}


@app.route("/generate-questions", method="POST")
@handle_response
@lru_cache()
def generate_questions():
    # get form data from the request
    difficulty_level = request.forms.get("difficulty_level")
    programming_language = request.forms.get("programming_language")
    topics = request.forms.get("topics")

    # generate questions using the provided form data
    questions = __generate_questions(
        user_query=__user_prompt(
            # num_questions=2,  # remove this in PROD code
            difficulty_level=difficulty_level,
            programming_language=programming_language,
            topics=topics,
        )
    )
    return {
        "payload": questions,
        "message": "Questions Generated Successfully",
        "status_code": 200,
    }


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
