from app.framework import App, Request
from app.services import question_service
from app.utils import logger, cache, handle_response, ROUTES
from ast import literal_eval


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
    @cache
    def __generate_questions_handler(self):
        """
        handle the generation of questions based on the payload.
        """
        logger.debug("__generate_questions route called")

        # retrieve data from request and make a dictionary object
        # retrieve data from query params and make a dictionary object
        payload = dict(
            difficulty_level=Request.query.get("difficulty_level"),
            programming_language=Request.query.get("programming_language"),
            topics=Request.query.get("topics"),
        )
        print(f"==>> payload: {payload}")

        # generate questions using the service
        response = question_service().generate_questions(payload=payload)
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
            ROUTES.QUESTION_ROUTE,
            method="POST",
            callback=self.__generate_questions_handler,
        )


# singleton instance of QuestionRoute
question_route_obj = QuestionRoute()
