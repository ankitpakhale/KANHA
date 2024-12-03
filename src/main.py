from bottle import route, run
from question_generation import (
    user_prompt as __user_prompt,
    generate_questions as __generate_questions,
)
from functools import lru_cache


def handle_response(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return {
                "status": True,
                "payload": result.get("payload"),
                "message": result.get("message"),
                "status_code": result.get("status_code"),
            }
        except Exception as e:
            raise {
                "status": False,
                "payload": {},
                "message": str(e),
                "status_code": 500,
            }

    return wrapper


@route("/ping")
@handle_response
@lru_cache()
def ping():
    return {"payload": {}, "message": "PONG", "status_code": 200}


@route("/generate-questions/<difficulty_level>/<programming_language>/<topics>")
@handle_response
@lru_cache()
def generate_questions(difficulty_level, programming_language, topics):
    # TODO: convert this into form data and post request
    questions = __generate_questions(
        user_query=__user_prompt(
            num_questions=2,  # remove this in PROD code
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
    run(host="localhost", port=8080)
