from framework import App
from routes import (
    healthcheck_route_obj,
    question_route_obj,
    evaluation_route_obj,
    cache_route_obj,
    feedback_route_obj,
)
from config.general_config import GeneralConfig
from utils import logger


# register routes
healthcheck_route_obj.register()
question_route_obj.register()
evaluation_route_obj.register()
cache_route_obj.register()
feedback_route_obj.register()


if __name__ == "__main__":
    # get the port from general configurations
    __port = GeneralConfig.APP_PORT
    __host = GeneralConfig.APP_HOST
    logger.debug(f"➡ Starting server on {__port} port...")
    logger.debug(f"➡ Starting server on {__host} host...")
    App.run(host=__host, port=__port)
