from sqlalchemy.orm import sessionmaker
from src.dao.database_config import DatabaseConfig
from src.dao.models import BaseModel


class DatabaseManager:
    """
    Database Manager Class
    Handles database engine creation, session management, and table creation.
    """

    def __init__(self):
        self.engine = DatabaseConfig.create_engine()
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def create_tables(self):
        """
        Create all tables in the database.
        """
        BaseModel.metadata.create_all(self.engine)

    def get_session(self):
        """
        Get a new database session.
        """
        return self.SessionLocal()


db_manager = DatabaseManager
