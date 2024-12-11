from .question_route import question_route_obj
from .evaluation_route import evaluation_route_obj
from .healthcheck_route import healthcheck_route_obj


# TODO: make a RouteManager that retrieve data from request and pass it to appropriate service, creating individual file for specific route is not feasiabl option
__all__ = [
    "question_route_obj",
    "evaluation_route_obj",
    "healthcheck_route_obj",
]
