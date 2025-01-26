class ROUTES:
    CACHE_ROUTE = "/delete-cache"
    EVALUATION_ROUTE = "/evaluate-answers"
    HEALTHCHECK_ROUTE = "/ping"
    DB_HEALTHCHECK_ROUTE = "/db-healthcheck"
    QUESTION_ROUTE = "/generate-questions"
    FEEDBACK_ROUTE = "/feedback"
    CONTACT_ROUTE = "/contact"


class PATH:
    MODEL_PATH = "app/dao/models"
    PROJECT_ROOT = ""
    MIGRATION_PATH = "migrations/versions"


class ClientSettings:
    BATCH_SIZE = 10
