from framework import App, Request
from utils import ROUTES
from services import evaluation_service_obj
from utils import logger, cache, handle_response
import json


class EvaluationRoute:
    """
    Singleton class to handle and register routes for answer evaluation.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @handle_response
    @cache
    def __evaluate_answer_handler(self):
        """
        Handle the evaluation of answers based on the payload.
        """
        logger.debug("__evaluate_answer route called")

        # retrieve data from request
        _request_data = Request.forms.get("user_code")
        payload = json.loads(_request_data)

        # generate questions using the service
        response = evaluation_service_obj(payload=payload)
        logger.debug("Response successfully generated")
        return {
            "payload": response,
            "message": "Answers Evaluated Successfully",
            "status_code": 200,
        }

    def register(self):
        """
        Register the route for question generation.
        """
        App.route(
            ROUTES.EVALUATION_ROUTE,
            method="POST",
            callback=self.__evaluate_answer_handler,
        )


# singleton instance of EvaluationRoute
evaluation_route_obj = EvaluationRoute()
