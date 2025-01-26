from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import Mapped
from app.dao.models.base import BaseModel


class Contact(BaseModel):
    """
    Contact Model
    Represents the Contact table in the database.
    """

    # table name for the contact model
    __tablename__ = "contact"

    # define fields using Mapped[] for SQLAlchemy 2.x
    full_name: Mapped[str] = Column(Text)
    email: Mapped[str] = Column(Text, nullable=True)
    phone: Mapped[str] = Column(Text, nullable=True)
    subject: Mapped[str] = Column(Text, nullable=True)
    message: Mapped[str] = Column(Text)

    def __repr__(self) -> str:
        """
        Custom String Representation Of The Contact Objects.
        This method returns a detailed string with the contact's attributes,
        useful for debugging and logging purposes.
        """
        return f"""Contact(
            id={self.id!r},
            created_at={self.created_at!r},
            full_name={self.full_name!r},
            email={self.email!r},
            phone={self.phone!r},
            subject={self.subject!r},
            message={self.message!r},
        )"""
