from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped
from .base import BaseModel


class Feedback(BaseModel):
    """
    Feedback Model
    Represents the feedback table in the database.
    """

    # table name for the Feedback model
    __tablename__ = "feedback"

    # Define fields using Mapped[] for SQLAlchemy 2.x
    rating: Mapped[int] = Column(Integer)
    comments: Mapped[str] = Column(String)
    frequency_of_use: Mapped[str] = Column(String, nullable=True)
    purpose_of_use: Mapped[str] = Column(String, nullable=True)
    ease_of_use: Mapped[str] = Column(String, nullable=True)
    specific_features: Mapped[str] = Column(String, nullable=True)

    def __repr__(self) -> str:
        """
        Custom String Representation Of The Feedback Objects.
        This method returns a detailed string with the feedback's attributes,
        useful for debugging and logging purposes.
        """
        return f"""Feedback(
            id={self.id!r},
            created_at={self.created_at!r},
            rating={self.rating!r},
            comments={self.comments!r},
            frequency_of_use={self.frequency_of_use!r},
            purpose_of_use={self.purpose_of_use!r},
            ease_of_use={self.ease_of_use!r},
            specific_features={self.specific_features!r}
        )"""
