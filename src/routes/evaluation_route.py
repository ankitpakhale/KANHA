from . import dependencies
from services import evaluation_service_obj


class EvaluationRoute:
    """
    Singleton class to handle and register routes for answer evaluation.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @dependencies.handle_response
    def __evaluate_answer(self):
        """
        Handle the evaluation of answers based on the payload.
        """
        dependencies.logger.debug("__evaluate_answer route called")
        # retrieve data from request
        answers_payload = dict(
            user_code=dependencies.json.loads(
                dependencies.Request.forms.get("user_code")
            )
        )

        # generate questions using the service
        response = evaluation_service_obj(**answers_payload)
        dependencies.logger.debug("Response successfully generated")
        return {
            "payload": response,
            "message": "Answers Evaluated Successfully",
            "status_code": 200,
        }

    def register(self):
        """
        Register the route for question generation.
        """
        dependencies.App.route(
            "/answer-evaluation", method="POST", callback=self.__evaluate_answer
        )


# singleton instance of EvaluationRoute
evaluation_route_obj = EvaluationRoute()
