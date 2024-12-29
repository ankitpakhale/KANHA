from app.framework import App, Request
from app.utils import logger, cache, handle_response, ROUTES
from app.services import feedback_service_obj


class FeedbackRoute:
    """
    Singleton class to handle and register routes for Feedback.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @handle_response
    @cache
    def __feedback_handler(self):
        """
        Handle the feedback status.
        """
        logger.debug("__feedback route called")
        # retrieve data from request and make a dictionary object
        payload = dict(
            rating=int(Request.forms.get("rating")),
            comments=Request.forms.get("comments"),
            frequency_of_use=Request.forms.get("frequency_of_use"),
            purpose_of_use=Request.forms.get("purpose_of_use"),
            ease_of_use=Request.forms.get("ease_of_use"),
            specific_feature=Request.forms.get("specific_feature"),
        )

        # pass feedback data to feedback service
        response = feedback_service_obj(payload=payload)
        logger.debug("feedbacks received successfully")
        return {
            "payload": response,
            "message": "feedbacks received successfully",
            "status_code": 200,
        }

    def register(self):
        """
        Register the route of feedback.
        """
        App.route(
            ROUTES.FEEDBACK_ROUTE, method="POST", callback=self.__feedback_handler
        )


# singleton instance of FeedbackRoute
feedback_route_obj = FeedbackRoute()
