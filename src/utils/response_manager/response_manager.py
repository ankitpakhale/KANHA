from typing import Callable, Any, Dict, Type
from framework import Response
from utils import logger
import json


class ResponseHandler:
    """
    Class to handle standardized response and exception handling logic.
    """

    # exception mapping for handling various exceptions
    EXCEPTION_MAPPING = {
        # json and validation errors
        json.decoder.JSONDecodeError: {
            "status_code": 502,
            "message": "validation error",
        },
        AssertionError: {
            "status_code": 400,
            "message": "validation error",
        },
        ValueError: {
            "status_code": 400,
            "message": "invalid value provided, default keys are difficulty_level, programming_language & topics",
        },
        KeyError: {
            "status_code": 400,
            "message": "missing required key in the request data",
        },
        # file and permission errors
        FileNotFoundError: {
            "status_code": 404,
            "message": "requested file not found",
        },
        PermissionError: {
            "status_code": 403,
            "message": "permission denied for the requested operation",
        },
        # # database errors
        # sqlalchemy.exc.IntegrityError: {
        #     "status_code": 409,
        #     "message": "database integrity constraint violated",
        # },
        # sqlalchemy.exc.OperationalError: {
        #     "status_code": 500,
        #     "message": "database operation failed",
        # },
        # # network and request errors
        # requests.exceptions.ConnectionError: {
        #     "status_code": 503,
        #     "message": "failed to connect to the remote service",
        # },
        # requests.exceptions.Timeout: {
        #     "status_code": 504,
        #     "message": "the request to the remote service timed out",
        # },
        # # async errors
        # asyncio.TimeoutError: {
        #     "status_code": 504,
        #     "message": "async operation timed out",
        # },
        # default exception
        Exception: {
            "status_code": 500,
            "message": "internal server error",
        },
    }

    def __init__(self) -> None:
        self.status_code = 200

    def set_status(self, status_code: int) -> None:
        """
        Sets the HTTP response status code.
        """
        self.status_code = status_code
        Response.status = status_code

    def handle_exception(self, exception: Exception) -> Dict[str, Any]:
        """
        Handles exceptions by returning a standardized error response.
        """
        exception_type = type(exception)
        exception_info = self.EXCEPTION_MAPPING.get(
            exception_type, self.EXCEPTION_MAPPING[Exception]
        )

        # log the error
        logger.critical(
            f"Error ({exception_info['status_code']}): {exception_info['message']}: {str(exception)}",
            exc_info=True,
        )

        # set the response status
        self.set_status(exception_info["status_code"])

        # return standardized error response
        return {
            "status": False,
            "payload": {},
            "message": f"{exception_info['message']}: {str(exception)}",
            "status_code": exception_info["status_code"],
        }

    def handle_success(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handles successful responses by returning a standardized success response.
        """
        self.set_status(result.get("status_code", 200))
        return {
            "status": True,
            "payload": result.get("payload", {}),
            "message": result.get("message", "Success"),
            "status_code": self.status_code,
        }


def handle_response(func: Callable) -> Callable:
    """
    Decorator to wrap a function with centralized response handling.
    """
    handler = ResponseHandler()

    def wrapper(*args, **kwargs) -> Dict[str, Any]:
        try:
            # execute the decorated function
            result = func(*args, **kwargs)
            # handle the success response
            return handler.handle_success(result)
        except tuple(ResponseHandler.EXCEPTION_MAPPING.keys()) as e:
            # handle the error response
            return handler.handle_exception(e)

    return wrapper
