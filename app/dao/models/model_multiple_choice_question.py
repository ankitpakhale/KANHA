from sqlalchemy import Column, String, Text
from sqlalchemy.orm import Mapped
from app.dao.models import BaseModel


class MultipleChoiceQuestion(BaseModel):
    """
    MultipleChoiceQuestion Model
    Represents the MultipleChoiceQuestion table in the database.
    """

    # table name for the MultipleChoiceQuestion model
    __tablename__ = "multiple_choice_question"
    difficulty_level: Mapped[str] = Column(Text, nullable=False)
    question: Mapped[str] = Column(Text, nullable=False)
    option_1: Mapped[str] = Column(Text, nullable=False)
    option_2: Mapped[str] = Column(Text, nullable=False)
    option_3: Mapped[str] = Column(Text, nullable=False)
    option_4: Mapped[str] = Column(Text, nullable=False)
    correct_answer: Mapped[str] = Column(Text, nullable=False)
    required_time: Mapped[str] = Column(Text, nullable=False)

    def __repr__(self) -> str:
        """
        Custom String Representation Of The MultipleChoiceQuestion Objects.
        This method returns a detailed string with the MultipleChoiceQuestion's attributes,
        useful for debugging and logging purposes.
        """
        return f"""MultipleChoiceQuestion(
            id={self.id!r},
            created_at={self.created_at!r},
            difficulty_level={self.difficulty_level!r},
            question={self.question!r},
            option_1={self.option_1!r},
            option_2={self.option_2!r},
            option_3={self.option_3!r},
            option_4={self.option_4!r},
            correct_answer={self.correct_answer!r},
            required_time={self.required_time!r}
        )"""
