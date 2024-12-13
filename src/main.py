from framework import App
from routes import healthcheck_route_obj, question_route_obj, evaluation_route_obj
from config.general_config import GeneralConfig

# register question routes
healthcheck_route_obj.register()
question_route_obj.register()
evaluation_route_obj.register()


if __name__ == "__main__":
    # get the port from general configurations
    __port = GeneralConfig.APP_PORT
    __host = GeneralConfig.APP_HOST
    print(f"➡ Starting server on {__port} port...")
    print(f"➡ Starting server on {__host} host...")
    App.run(host=__host, port=__port)
