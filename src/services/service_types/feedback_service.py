from typing import Union
from services import validation_manager_obj
from utils import logger
from dao import Feedback, db_session  # noqa: E402


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

        # create the database session
        session = db_session()

        # use the selected entry in feedback_entry
        feedback_entry = Feedback(
            rating=payload.get("rating"),
            comments=payload.get("comments"),
            frequency_of_use=payload.get("frequency_of_use"),
            purpose_of_use=payload.get("purpose_of_use"),
            ease_of_use=payload.get("ease_of_use"),
            specific_features=payload.get("specific_features"),
        )

        session.add(feedback_entry)
        session.commit()

        logger.debug("Feedback Data added successfully!!!")

        return {}

    def feedback(self, payload: Union[list, dict]):
        return self.__feedback(payload)


def feedback_service_obj(payload: Union[list, dict]):
    feedback_service_result = FeedbackService().feedback(payload)
    return feedback_service_result
