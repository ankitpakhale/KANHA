from framework import Response
from utils import __logger


class ResponseManager:
    """
    Centralized handler for API responses, ensuring a consistent response format
    and error management across the application.
    """

    @staticmethod
    def handle_response(func):
        """
        Decorator to wrap a function with centralized try-except handling
        and enforce a standard response structure.
        """

        def wrapper(*args, **kwargs):
            try:
                # execute the decorated function
                result = func(*args, **kwargs)

                # extract response details
                status_code = result.get("status_code", 200)
                payload = result.get("payload", {})
                message = result.get("message", "Success")

                # set the response status code
                Response.status = status_code

                # return the standardized response
                return {
                    "status": True,
                    "payload": payload,
                    "message": message,
                    "status_code": status_code,
                }
            except Exception as e:
                # log the exception details
                print(f"Error in processing request: {str(e)}", exc_info=True)

                # set the HTTP response status to 500 (Internal Server Error)
                Response.status = 500

                # return an error response in the standardized format
                return {
                    "status": False,
                    "payload": {},
                    "message": f"Internal Server Error: {str(e)}",
                    "status_code": 500,
                }

        return wrapper
