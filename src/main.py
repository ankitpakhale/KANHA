from framework import App
from routes.question_routes import QuestionRoutes


# register question routes
question_routes = QuestionRoutes()
question_routes.register()


if __name__ == "__main__":
    App.run(host="0.0.0.0", port=8080)
