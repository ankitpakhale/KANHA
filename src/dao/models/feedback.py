from sqlalchemy import Column, Integer, String
from .base import BaseModel


class Feedback(BaseModel):
    """
    Feedback Model
    Represents the feedback table in the database.
    """

    # table name for the Feedback model
    __tablename__ = "feedback"

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
            created_at={self.created_at!r},
            rating={self.rating!r},
            comments={self.comments!r},
            frequency_of_use={self.frequency_of_use!r},
            purpose_of_use={self.purpose_of_use!r},
            ease_of_use={self.ease_of_use!r},
            specific_features={self.specific_features!r}
        )"""
