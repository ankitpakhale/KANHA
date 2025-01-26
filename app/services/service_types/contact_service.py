from typing import Union
from app.services import validation_manager
from app.utils import logger
from app.dao import Contact, db_session  # noqa: E402
from app.control_panel import control_panel_manager


# TODO: change name to contact
class ContactService:
    def __contact(self, payload: Union[list, dict]):
        """
        Initializes the database layer and save user contact.
        """
        # validate the data
        validation_manager(service_type="contact", validation_type="request").validate(
            payload
        )
        logger.debug("Payload varified successfully at contact Service!!!")

        # create the database session
        session = db_session()

        # use the selected entry in contact_entry
        contact_entry = Contact(
            full_name=payload.get("full_name"),
            email=payload.get("email"),
            phone=payload.get("phone"),
            subject=payload.get("subject"),
            message=payload.get("message"),
        )

        session.add(contact_entry)
        session.commit()

        logger.debug("contact added in Database successfully!!!")

        return {}

    def contact(self, payload: Union[list, dict]):
        if control_panel_manager.get_setting("SAVE_CONTACT_IN_DB"):
            status = self.__contact(payload)
        else:
            logger.warning(
                """
                The 'SAVE_CONTACT_IN_DB' setting is currently disabled in the control panel.
                If this setting was not intentionally turned off, please enable it to allow saving
                contact in the database.

                WARNING: With this setting disabled, contact will not be persisted in the database.
                This behavior is typically used in testing environments. Ensure that this setting is enabled
                in production to retain valuable contact data and avoid potential issues with missing or lost contact.
                """
            )
            status = {}
        return status


# singleton instance of ContactService
contact_service = ContactService
