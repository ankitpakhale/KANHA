from . import dependencies


class HealthcheckRoute:
    """
    Singleton class to handle and register routes for healthcheck.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @dependencies.ResponseManager.handle_response
    def __healthcheck(self):
        """
        Handle the healthcheck status.
        """
        dependencies.logger.debug("__healthcheck route called")
        return {
            "payload": {},
            "message": "PONG",
            "status_code": 200,
        }

    def register(self):
        """
        Register the route of healthcheck.
        """
        dependencies.App.route("/ping", method="GET", callback=self.__healthcheck)


# singleton instance of HealthcheckRoute
healthcheck_route_obj = HealthcheckRoute()
