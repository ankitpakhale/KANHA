from config import GeneralConfig, DBConfig
from sqlalchemy import create_engine


class DatabaseConfig:
    """
    Database Configuration Class
    Handles the creation of database engine URLs based on the environment.
    """

    @staticmethod
    def get_engine_url() -> str:
        """
        Generate the database URL based on environment variables.
        """
        db_name = DBConfig.PG_NAME
        db_username = DBConfig.PG_USERNAME
        db_password = DBConfig.PG_PASSWORD
        db_host = DBConfig.PG_HOST
        db_port = DBConfig.PG_PORT

        # TODO: Add AWS S3 and RDS based on specific environment
        database_url = f"postgresql://{db_username}:{
            db_password}@{db_host}:{db_port}/{db_name}"
        # if GeneralConfig.ENV == "dev":
        #     # PostgreSQL database URL for development environment
        #     database_url = f"postgresql://{db_username}:{
        #         db_password}@{db_host}:{db_port}/{db_name}"
        # else:
        #     # Sqlite database URL for local environment
        #     database_url = f"sqlite:///{db_name}.db"

        return database_url

    @staticmethod
    def create_engine():
        """
        Create and return a SQLAlchemy engine.
        """
        return create_engine(DatabaseConfig.get_engine_url())


db_config = DatabaseConfig
