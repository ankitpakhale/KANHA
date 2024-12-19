from .route_question import question_route_obj
from .route_evaluation import evaluation_route_obj
from .route_healthcheck import healthcheck_route_obj
from .route_cache import cache_route_obj
from .route_feedback import feedback_route_obj


# TODO: make a RouteManager that retrieve data from request and pass it to appropriate service, creating individual file for specific route is not feasiabl option
__all__ = [
    "question_route_obj",
    "evaluation_route_obj",
    "healthcheck_route_obj",
    "cache_route_obj",
    "feedback_route_obj",
]
