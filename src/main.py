from framework import App
from routes import question_routes_obj, evaluation_routes_obj


# register question routes
question_routes_obj.register()
evaluation_routes_obj.register()


if __name__ == "__main__":
    App.run(host="0.0.0.0", port=8080)
