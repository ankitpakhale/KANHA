from app.framework import App
from app.routes import (
    healthcheck_route_obj,
    question_route_obj,
    evaluation_route_obj,
    cache_route_obj,
    feedback_route_obj,
)
from app.config.general_config import GeneralConfig
from app.config.openai_config import OpenAIConfig
from app.utils import logger


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
    logger.info(f"➡ Active Client is {GeneralConfig.ACTIVE_CLIENT}")
    logger.info(f"➡ Client Model is {OpenAIConfig.OPENAI_MODEL}")
    App.run(host=__host, port=__port)
