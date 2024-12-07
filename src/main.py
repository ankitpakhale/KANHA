from framework import App
from routes.question_routes import question_routes_obj


# register question routes
question_routes_obj.register()


if __name__ == "__main__":
    App.run(host="0.0.0.0", port=8080)
