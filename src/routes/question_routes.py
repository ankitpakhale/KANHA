from framework import App, Request
from services.question_service import question_service_obj
from services.validation_manager import validation_manager_obj
from utils import __logger


class QuestionRoutes:
    """
    Class to handle and register routes for question generation.
    """

    def __init__(self):
        """
        Initialize the Validation Manager and Question Service.
        """
        self.validation_manager = validation_manager_obj
        self.question_service = question_service_obj

    def generate_questions(self):
        """
        Handle the generation of questions based on the payload.
        """
        # retrieve data from request
        difficulty_level = Request.forms.get("difficulty_level")
        programming_language = Request.forms.get("programming_language")
        topics = Request.forms.get("topics")

        # validate the payload
        validation_result = self.validation_manager(
            difficulty_level,
            programming_language,
            topics,
        )
        print(f">>>>>>>>>>>>>>>>>>> validation_result: {validation_result}")
        if not validation_result:
            raise "Error occured during validation"

        # generate questions using the service
        questions = self.question_service(
            difficulty_level,
            programming_language,
            topics,
        )
        print(f">>>>>>>>>>>>>>>>>>>>>> questions: {questions}")
        return {"questions": questions}, 200

    def register(self):
        """
        Register the route for question generation.
        """
        App.route(
            "/generate-questions", method="POST", callback=self.generate_questions
        )
