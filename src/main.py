from utils import (
    __logger,
    __app,
    __request,
    __response,
    __cache,
    __delete_cache,
    __clear_cache,
)

from question_generation import (
    generate_questions as __generate_questions,
    user_prompt as __user_prompt,
)
from constants import PORT


# CORS configuration
@__app.hook("after_request")
def enable_cors():
    __response.headers["Access-Control-Allow-Origin"] = "*"
    __response.headers["Access-Control-Allow-Methods"] = (
        "GET, POST, PUT, DELETE, OPTIONS"
    )
    __response.headers["Access-Control-Allow-Headers"] = (
        "Origin, X-Requested-With, Content-Type, Accept, Authorization"
    )


# handle OPTIONS requests explicitly for CORS preflight
@__app.route("/generate-questions", method="OPTIONS")
def handle_options():
    __response.status = 200
    return {}


def handle_response(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            __status_code = result.get("status_code", 200)
            __payload = result.get("payload", {})
            __message = result.get("message", "Success")

            __response.status = __status_code
            return {
                "status": True,
                "payload": __payload,
                "message": __message,
                "status_code": __status_code,
            }
        except Exception as e:
            __logger.error(f"Error in processing request: {str(e)}", exc_info=True)
            __response.status = 500
            return {
                "status": False,
                "payload": {},
                "message": str(e),
                "status_code": 500,
            }

    return wrapper


@__app.route("/ping")
@handle_response
@__cache
def ping():
    return {"payload": {}, "message": "PONG", "status_code": 200}


@__app.route("/generate-questions", method="POST")
@handle_response
@__cache
def generate_questions():
    # get form data from the request
    difficulty_level = __request.forms.get("difficulty_level")
    programming_language = __request.forms.get("programming_language")
    topics = __request.forms.get("topics")

    # log input data for debugging
    __logger.debug(
        f"Received data: difficulty_level={difficulty_level}, programming_language={programming_language}, topics={topics}"
    )

    # basic form validation
    if not difficulty_level or not programming_language or not topics:
        __logger.warning("Missing required fields")
        __response.status = 400
        return {
            "status": False,
            "payload": {},
            "message": "Missing required fields (difficulty_level, programming_language, topics)",
            "status_code": 400,
        }

    # generate questions
    try:
        questions = __generate_questions(
            user_query=__user_prompt(
                num_questions=1,
                difficulty_level=difficulty_level,
                programming_language=programming_language,
                topics=topics,
            )
        )
        __logger.info(
            f"Questions successfully generated for difficulty_level={difficulty_level}, programming_language={programming_language}, topics={topics}"
        )
        return {
            "payload": questions,
            # "payload": {},
            "message": "Questions Generated Successfully",
            "status_code": 200,
        }

    except Exception as e:
        __logger.error(f"Error generating questions: {str(e)}", exc_info=True)
        __response.status = 500
        return {
            "status": False,
            "payload": {},
            "message": f"Error generating questions: {str(e)}",
            "status_code": 500,
        }


@__app.route("/clear-cache", method="POST")
@handle_response
def clear_cache():
    __key = __request.forms.get("key")
    # delete specific cache based on key else clear the entire cache
    __delete_cache(__key) if __key else __clear_cache()

    return {
        "status": True,
        "payload": {},
        "message": "Cache cleared successfully",
        "status_code": 200,
    }


if __name__ == "__main__":
    # run the app on localhost and port 8080
    __app.run(host="localhost", port=PORT)
