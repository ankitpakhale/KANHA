from framework import App, Request
from services import evaluation_service_obj
from utils import __logger, ResponseManager
import json


class EvaluationRoutes:
    """
    Singleton class to handle and register routes for answer evaluation.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @ResponseManager.handle_response
    def __evaluate_answer(self):
        """
        Handle the evaluation of answers based on the payload.
        """
        # retrieve data from request
        answers_payload = dict(user_code=json.loads(Request.forms.get("user_code")))

        # generate questions using the service
        response = evaluation_service_obj(**answers_payload)
        print("Response successfully generated")
        return {
            "payload": response,
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
