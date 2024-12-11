from framework import App, Request, Response
from services import question_service_obj
from utils import __logger, ResponseManager
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

    @ResponseManager.handle_response
    def __generate_questions(self):
        """
        handle the generation of questions based on the payload.
        """
        # retrieve data from request and make a dictionary object
        print(
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>> difficulty_level",
            Request.forms.get("difficulty_level"),
        )
        print(
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>> programming_language",
            Request.forms.get("programming_language"),
        )
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>> topics", Request.forms.get("topics"))

        # parse the 'topics' field which was sent as a json string
        topics = literal_eval(Request.forms.get("topics"))

        questions_payload = dict(
            difficulty_level=Request.forms.get("difficulty_level"),
            programming_language=Request.forms.get("programming_language"),
            topics=topics,
        )

        # generate questions using the service
        response = question_service_obj(**questions_payload)
        print("response successfully generated")
        return {
            "payload": response,
            "message": "questions generated successfully",
            "status_code": 200,
        }

    def register(self):
        """
        Register the route for question generation.
        """
        App.route(
            "/generate-questions", method="POST", callback=self.__generate_questions
        )


# singleton instance of QuestionRoute
question_route_obj = QuestionRoute()
