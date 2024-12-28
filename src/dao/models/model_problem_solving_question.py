from sqlalchemy import Column, String, JSON
from sqlalchemy.orm import Mapped
from src.dao.models.base import BaseModel
from typing import Optional, List


class ProblemSolvingQuestion(BaseModel):
    """
    ProblemSolvingQuestion Model
    Represents the ProblemSolvingQuestion table in the database.
    """

    # table name for the ProblemSolvingQuestion model
    __tablename__ = "problem_solving_questions"

    problem_description: Mapped[str] = Column(String, nullable=False)
    input_format: Mapped[str] = Column(String, nullable=False)
    output_format: Mapped[str] = Column(String, nullable=False)
    constraints: Mapped[Optional[str]] = Column(String, nullable=True)
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
            problem_description={self.problem_description!r},
            input_format={self.input_format!r},
            output_format={self.output_format!r},
            constraints={self.constraints!r},
            examples={self.examples!r},
            edge_cases={self.edge_cases!r}
        )"""
