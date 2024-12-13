from . import dependencies
from services import question_service_obj


class QuestionRoute:
    """
    Singleton class to handle and register routes for question generation.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @dependencies.ResponseManager.handle_response
    def __generate_questions(self):
        """
        handle the generation of questions based on the payload.
        """
        dependencies.logger.debug("__generate_questions route called")

        # retrieve data from request and make a dictionary object
        dependencies.logger.debug(
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>> difficulty_level",
            dependencies.Request.forms.get("difficulty_level"),
        )
        dependencies.logger.debug(
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>> programming_language",
            dependencies.Request.forms.get("programming_language"),
        )
        dependencies.logger.debug(
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>> topics",
            dependencies.Request.forms.get("topics"),
        )

        # parse the 'topics' field which was sent as a json string
        topics = dependencies.literal_eval(dependencies.Request.forms.get("topics"))

        questions_payload = dict(
            difficulty_level=dependencies.Request.forms.get("difficulty_level"),
            programming_language=dependencies.Request.forms.get("programming_language"),
            topics=topics,
        )

        # generate questions using the service
        response = question_service_obj(**questions_payload)
        dependencies.logger.debug("response successfully generated")
        return {
            "payload": response,
            "message": "questions generated successfully",
            "status_code": 200,
        }

    def register(self):
        """
        Register the route for question generation.
        """
        dependencies.App.route(
            "/generate-questions", method="POST", callback=self.__generate_questions
        )


# singleton instance of QuestionRoute
question_route_obj = QuestionRoute()
