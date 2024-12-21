import uuid
import os
from config import DBConfig, GeneralConfig
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, sessionmaker


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

        if GeneralConfig.ENV == "dev":
            # PostgreSQL database URL for development environment
            database_url = f"postgresql://{db_username}:{
                db_password}@{db_host}:{db_port}/{db_name}"
        else:
            # Sqlite database URL for local environment
            database_url = f"sqlite:///{db_name}.db"

        return database_url

    @staticmethod
    def create_engine():
        """
        Create and return a SQLAlchemy engine.
        """
        return create_engine(DatabaseConfig.get_engine_url())


class BaseModel(DeclarativeBase):
    """
    Base Class For Declarative Models.
    All model classes should inherit from this base class.
    """

    pass


class Feedback(BaseModel):
    """
    Feedback Model
    Represents the feedback table in the database.
    """

    # table name for the Feedback model
    __tablename__ = "feedback"

    id = Column(
        UUID(as_uuid=True) if os.getenv("ENV") == "dev" else String(36),
        primary_key=True,
        default=uuid.uuid4,  # generate a UUID automatically for new records
    )
    rating = Column(Integer)
    comments = Column(String)
    frequency_of_use = Column(String)
    purpose_of_use = Column(String)
    ease_of_use = Column(String)
    specific_features = Column(String)

    def __repr__(self) -> str:
        """
        Custom String Representation Of The Feedback Objects.
        This method returns a detailed string with the feedback's attributes,
        useful for debugging and logging purposes.
        """
        return f"""Feedback(
            id={self.id!r},
            rating={self.rating!r},
            comments={self.comments!r},
            frequency_of_use={self.frequency_of_use!r},
            purpose_of_use={self.purpose_of_use!r},
            ease_of_use={self.ease_of_use!r},
            specific_features={self.specific_features!r}
        )"""


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


# usage example
if __name__ == "__main__":
    # initialize the database manager
    db_manager = DatabaseManager()

    # create tables
    db_manager.create_tables()

    # example of creating a session and adding data
    with db_manager.get_session() as session:
        feedback_entry = Feedback(
            rating=10,
            comments="Great app!",
            frequency_of_use="Daily",
            purpose_of_use="Work",
            ease_of_use="Very Easy",
            specific_features="Reporting",
        )
        session.add(feedback_entry)
        session.commit()
