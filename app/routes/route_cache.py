from app.framework import App, Request
from app.utils import logger, cache, handle_response, clear_cache, delete_cache, ROUTES


class CacheRoute:
    """
    Singleton class to handle and register routes for answer evaluation.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @handle_response
    def __cache_handler(self):
        """
        Handle the evaluation of answers based on the payload.
        """
        logger.debug("__cache route called")
        # retrieve data from request
        __cache_key = Request.forms.get("cache_key")
        if __cache_key:
            delete_cache(__cache_key)
            __msg = f"Cache deleted successfully for key {__cache_key}"
        else:
            clear_cache()
            __msg = "Cache deleted successfully"
        logger.debug(__msg)

        return {
            "payload": {},
            "message": __msg,
            "status_code": 200,
        }

    def register(self):
        """
        Register the route for question generation.
        """
        App.route(ROUTES.CACHE_ROUTE, method="POST", callback=self.__cache_handler)


# singleton instance of CacheRoute
cache_route_obj = CacheRoute()
