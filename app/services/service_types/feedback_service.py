from typing import Union
from app.services import validation_manager
from app.utils import logger
from app.dao import Feedback, db_session  # noqa: E402
from app.control_panel import control_panel_manager

# TODO: change name to Feedback


class FeedbackService:
    def __feedback(self, payload: Union[list, dict]):
        """
        Initializes the database layer and save user feedback.
        """
        # validate the data
        validation_manager(service_type="feedback", validation_type="request").validate(
            payload
        )
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
        if control_panel_manager.get_setting("SAVE_FEEDBACK_IN_DB"):
            status = self.__feedback(payload)
        else:
            logger.warning(
                """
                The 'SAVE_FEEDBACK_IN_DB' setting is currently disabled in the control panel.
                If this setting was not intentionally turned off, please enable it to allow saving
                feedback in the database.

                WARNING: With this setting disabled, feedback will not be persisted in the database.
                This behavior is typically used in testing environments. Ensure that this setting is enabled
                in production to retain valuable feedback data and avoid potential issues with missing or lost feedback.
                """
            )
            status = {}
        return status


feedback_service = FeedbackService

# def feedback_service_obj(payload: Union[list, dict]):
#     feedback_service_result = FeedbackService().feedback(payload)
#     return feedback_service_result
