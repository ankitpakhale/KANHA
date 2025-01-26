from app.framework import App, Request
from app.utils import logger, cache, handle_response, ROUTES
from app.services import contact_service


class ContactRoute:
    """
    Singleton class to handle and register routes for contact.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @handle_response
    # @cache
    def __contact_handler(self):
        """
        Handle the contact status.
        """
        logger.debug("__contact route called")
        # retrieve data from request and make a dictionary object
        payload = dict(
            full_name=Request.forms.get("full_name"),
            email=Request.forms.get("email"),
            phone=Request.forms.get("phone"),
            subject=Request.forms.get("subject"),
            message=Request.forms.get("message"),
        )

        # pass contact data to contact service
        response = contact_service().contact(payload=payload)
        logger.debug("contacts saved successfully")
        return {
            "payload": response,
            "message": "contacts saved successfully",
            "status_code": 200,
        }

    def register(self):
        """
        Register the route of contact.
        """
        App.route(ROUTES.CONTACT_ROUTE, method="POST", callback=self.__contact_handler)


# singleton instance of ContactRoute
contact_route_obj = ContactRoute()
