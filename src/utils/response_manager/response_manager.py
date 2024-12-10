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
            except AssertionError as ae:
                # log the exception details
                # __logger.critical(f"Assertion Error in processing request: {str(ae)}", exc_info=True)
                print(f"Assertion Error in processing request: {str(ae)}")

                # set the HTTP response status to 500 (Internal Server Error)
                Response.status = 403

                # return an error response in the standardized format
                return {
                    "status": False,
                    "payload": {},
                    "message": f"Validation Error: {str(ae)}",
                    "status_code": 500,
                }
            except Exception as e:
                # log the exception details
                # __logger.critical(f"Error in processing request: {str(e)}", exc_info=True)
                print(f"Error in processing request: {str(e)}")

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
