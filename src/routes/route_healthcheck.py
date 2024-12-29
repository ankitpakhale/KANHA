from src.framework import App
from src.utils import logger, cache, handle_response, ROUTES


class HealthcheckRoute:
    """
    Singleton class to handle and register routes for healthcheck.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @handle_response
    def __healthcheck_handler(self):
        """
        Handle the healthcheck status.
        """
        logger.debug("__healthcheck route called")
        return {
            "payload": {},
            "message": "PONG",
            "status_code": 200,
        }

    def register(self):
        """
        Register the route of healthcheck.
        """
        App.route(
            ROUTES.HEALTHCHECK_ROUTE, method="GET", callback=self.__healthcheck_handler
        )


# singleton instance of HealthcheckRoute
healthcheck_route_obj = HealthcheckRoute()
