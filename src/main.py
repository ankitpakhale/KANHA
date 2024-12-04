from bottle import Bottle, request, response
import logging
from question_generation import (
    generate_questions as __generate_questions,
    user_prompt as __user_prompt,
)
from functools import lru_cache

# set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create the Bottle app
app = Bottle()


# CORS configuration
@app.hook("after_request")
def enable_cors():
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers[
        "Access-Control-Allow-Headers"
    ] = "Origin, X-Requested-With, Content-Type, Accept, Authorization"


# handle OPTIONS requests explicitly for CORS preflight
@app.route("/generate-questions", method="OPTIONS")
def handle_options():
    response.status = 200
    return {}


def handle_response(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            __status_code = result.get("status_code", 200)
            __payload = result.get("payload", {})
            __message = result.get("message", "Success")

            response.status = __status_code
            return {
                "status": True,
                "payload": __payload,
                "message": __message,
                "status_code": __status_code,
            }
        except Exception as e:
            logger.error(f"Error in processing request: {str(e)}", exc_info=True)
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

    # log input data for debugging
    logger.debug(
        f"Received data: difficulty_level={difficulty_level}, programming_language={programming_language}, topics={topics}"
    )

    # basic form validation
    if not difficulty_level or not programming_language or not topics:
        logger.warning("Missing required fields")
        response.status = 400
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
        logger.info(
            f"Questions successfully generated for difficulty_level={difficulty_level}, programming_language={programming_language}, topics={topics}"
        )
        return {
            "payload": questions,
            "message": "Questions Generated Successfully",
            "status_code": 200,
        }

    except Exception as e:
        logger.error(f"Error generating questions: {str(e)}", exc_info=True)
        response.status = 500
        return {
            "status": False,
            "payload": {},
            "message": f"Error generating questions: {str(e)}",
            "status_code": 500,
        }


if __name__ == "__main__":
    # run the app on localhost and port 8080
    app.run(host="localhost", port=8080)
