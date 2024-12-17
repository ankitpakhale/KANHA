from framework import App, Request
from services import question_service_obj
from utils import logger, cache, handle_response
from ast import literal_eval
from .constants import QUESTION_ROUTE


class QuestionRoute:
    """
    Singleton class to handle and register routes for question generation.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @handle_response
    # @cache
    def __generate_questions_handler(self):
        """
        handle the generation of questions based on the payload.
        """
        logger.debug("__generate_questions route called")

        # parse the 'topics' field which was sent as a json string
        topics = literal_eval(Request.forms.get("topics"))

        # retrieve data from request and make a dictionary object
        questions_payload = dict(
            difficulty_level=Request.forms.get("difficulty_level"),
            programming_language=Request.forms.get("programming_language"),
            topics=topics,
        )

        logger.error(f"➡ questions_payload: {questions_payload}")

        # generate questions using the service
        response = question_service_obj(payload=questions_payload)
        logger.debug("response successfully generated")
        return {
            "payload": response,
            "message": "Questions generated successfully",
            "status_code": 200,
        }

    def register(self):
        """
        Register the route for question generation.
        """
        App.route(
            QUESTION_ROUTE, method="POST", callback=self.__generate_questions_handler
        )


# singleton instance of QuestionRoute
question_route_obj = QuestionRoute()
