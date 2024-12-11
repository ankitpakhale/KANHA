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
    print(f"➡ Starting server on {__port} port...")
    App.run(host="0.0.0.0", port=__port)
