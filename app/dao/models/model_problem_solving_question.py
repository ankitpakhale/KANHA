from sqlalchemy import Column, String, JSON, Text
from sqlalchemy.orm import Mapped
from app.dao.models.base import BaseModel
from typing import Optional, List


class ProblemSolvingQuestion(BaseModel):
    """
    ProblemSolvingQuestion Model
    Represents the ProblemSolvingQuestion table in the database.
    """

    # table name for the ProblemSolvingQuestion model
    __tablename__ = "problem_solving_questions"

    difficulty_level: Mapped[str] = Column(Text, nullable=False)
    problem_description: Mapped[str] = Column(Text, nullable=False)
    input_format: Mapped[str] = Column(Text, nullable=False)
    output_format: Mapped[str] = Column(Text, nullable=False)
    constraints: Mapped[Optional[str]] = Column(Text, nullable=True)
    examples: Mapped[Optional[List[dict]]] = Column(JSON, nullable=True)
    edge_cases: Mapped[Optional[List[dict]]] = Column(JSON, nullable=True)

    def __repr__(self) -> str:
        """
        Custom String Representation Of The ProblemSolvingQuestion Objects.
        This method returns a detailed string with the ProblemSolvingQuestion's attributes,
        useful for debugging and logging purposes.
        """
        return f"""ProblemSolvingQuestion(
            id={self.id!r},
            created_at={self.created_at!r},
            difficulty_level={self.difficulty_level!r},
            problem_description={self.problem_description!r},
            input_format={self.input_format!r},
            output_format={self.output_format!r},
            constraints={self.constraints!r},
            examples={self.examples!r},
            edge_cases={self.edge_cases!r}
        )"""
