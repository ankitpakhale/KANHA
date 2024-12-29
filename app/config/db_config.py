import os
from app.config import BaseConfig


class DBConfig(BaseConfig):
    """Database-related configuration"""

    # postgres-specific settings
    PG_USERNAME = os.getenv("PG_USERNAME", "postgres")
    PG_PASSWORD = os.getenv("PG_PASSWORD", "pgpass")
    PG_NAME = os.getenv("PG_NAME", "kanha")
    PG_HOST = os.getenv("PG_HOST", "localhost")
    PG_PORT = int(os.getenv("PG_PORT", 5432))

    @staticmethod
    def validate():
        """ensures that required postgres configurations are available"""
        missing_keys = []
        for key in [
            "PG_USERNAME",
            "PG_PASSWORD",
            "PG_NAME",
            "PG_HOST",
            "PG_PORT",
        ]:
            if not getattr(DBConfig, key):
                missing_keys.append(key)
        if missing_keys:
            raise EnvironmentError(
                f"Missing Postgres DB configuration keys: {', '.join(missing_keys)}"
            )
