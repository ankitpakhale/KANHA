from framework import App, Request
from services import evaluation_service_obj
from services.validation_manager import validation_response_manager_obj
from utils import __logger, ResponseManager


class EvaluationRoutes:
    """
    Singleton class to handle and register routes for answer evaluation.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Initialize the Validation Manager and Answer Service.
        """
        self.answer_service = evaluation_service_obj

    @ResponseManager.handle_response
    def __evaluate_answer(self):
        """
        Handle the evaluation of answers based on the payload.
        """
        # retrieve data from request
        difficulty_level = Request.forms.get("difficulty_level")
        programming_language = Request.forms.get("programming_language")
        topics = Request.forms.get("topics")

        # generate questions using the service
        questions = self.question_service(
            difficulty_level,
            programming_language,
            topics,
        )
        print(f"Questions successfully generated: {questions}")
        return {
            "payload": questions,
            "message": "Questions Generated Successfully",
            "status_code": 200,
        }

    def register(self):
        """
        Register the route for question generation.
        """
        App.route("/answer-evaluation", method="POST", callback=self.__evaluate_answer)


# singleton instance of EvaluationRoutes
evaluation_routes_obj = EvaluationRoutes()
