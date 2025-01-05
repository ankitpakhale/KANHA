from app.framework import App
from app.utils import logger, cache, handle_response, ROUTES
import psycopg2
from psycopg2 import OperationalError


# TODO: fix this db healthcheck route logic
class DBHealthcheckRoute:
    """
    Singleton class to handle and register routes for db healthcheck.
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
        connection = psycopg2.connect(
            dbname="your_database_name",
            user="your_database_user",
            password="your_database_password",
            host="your_database_host",
            port="your_database_port",
        )

        # check if the connection is successful
        connection.close()
        return {
            "payload": {},
            "message": "Database connection successful",
            "status_code": 200,
        }

    def register(self):
        """
        Register the route of healthcheck.
        """
        App.route(
            ROUTES.DB_HEALTHCHECK_ROUTE,
            method="GET",
            callback=self.__healthcheck_handler,
        )


# singleton instance of DBHealthcheckRoute
healthcheck_route_obj = DBHealthcheckRoute()
