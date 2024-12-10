from framework import App, Request
from services import question_service_obj
from services.validation_manager import validation_payload_manager_obj
from utils import __logger, ResponseManager
from ast import literal_eval


class QuestionRoutes:
    """
    Singleton class to handle and register routes for question generation.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @ResponseManager.handle_response
    def __generate_questions(self):
        """
        Handle the generation of questions based on the payload.
        """
        # retrieve data from request and make a dictionary object
        questions_payload = dict(
            difficulty_level=Request.forms.get("difficulty_level"),
            programming_language=Request.forms.get("programming_language"),
            # topics=literal_eval(Request.forms.get("topics")),
            topics=Request.forms.get("topics"),
        )
        # generate questions using the service
        questions = question_service_obj(**questions_payload)
        print("Questions successfully generated")
        return {
            "payload": questions,
            "message": "Questions Generated Successfully",
            "status_code": 200,
        }

    def register(self):
        """
        Register the route for question generation.
        """
        App.route(
            "/generate-questions", method="POST", callback=self.__generate_questions
        )


# singleton instance of QuestionRoutes
question_routes_obj = QuestionRoutes()
