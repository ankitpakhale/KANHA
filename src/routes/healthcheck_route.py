from framework import App, Request
from utils import __logger, ResponseManager
import json


class HealthcheckRoute:
    """
    Singleton class to handle and register routes for answer evaluation.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @ResponseManager.handle_response
    def __healthcheck(self):
        """
        Handle the evaluation of answers based on the payload.
        """
        return {
            "payload": {},
            "message": "PONG",
            "status_code": 200,
        }

    def register(self):
        """
        Register the route for question generation.
        """
        App.route("/ping", method="GET", callback=self.__healthcheck)


# singleton instance of EvaluationRoutes
healthcheck_route_obj = HealthcheckRoute()
