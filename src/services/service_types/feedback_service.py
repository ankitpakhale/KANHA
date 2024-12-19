from typing import Union
from services import validation_manager_obj
from utils import logger

# TODO: change name to Feedback


class FeedbackService:
    def __feedback(self, payload: Union[list, dict]):
        """
        Initializes the database layer and save user feedback.
        """
        # validate the data
        validation_manager = validation_manager_obj(
            service_type="feedback", validation_type="request"
        )
        validation_manager.validate(payload)
        logger.debug("Payload varified successfully at Feedback Service!!!")

        # add database layer to store feedback
        return {}

    def feedback(self, payload: Union[list, dict]):
        return self.__feedback(payload)


def feedback_service_obj(payload: Union[list, dict]):
    feedback_service_result = FeedbackService().feedback(payload)
    return feedback_service_result
