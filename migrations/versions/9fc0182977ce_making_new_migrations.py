"""Making new migrations

Revision ID: 9fc0182977ce
Revises: 1448656fe102
Create Date: 2024-12-29 14:15:18.056973

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9fc0182977ce"
down_revision: Union[str, None] = "1448656fe102"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "problem_solving_questions",
        "question_level",
        existing_type=sa.VARCHAR(),
        type_=sa.Text(),
        existing_nullable=False,
    )
    op.alter_column(
        "problem_solving_questions",
        "problem_description",
        existing_type=sa.VARCHAR(),
        type_=sa.Text(),
        existing_nullable=False,
    )
    op.alter_column(
        "problem_solving_questions",
        "input_format",
        existing_type=sa.VARCHAR(),
        type_=sa.Text(),
        existing_nullable=False,
    )
    op.alter_column(
        "problem_solving_questions",
        "output_format",
        existing_type=sa.VARCHAR(),
        type_=sa.Text(),
        existing_nullable=False,
    )
    op.alter_column(
        "problem_solving_questions",
        "constraints",
        existing_type=sa.VARCHAR(),
        type_=sa.Text(),
        existing_nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "problem_solving_questions",
        "constraints",
        existing_type=sa.Text(),
        type_=sa.VARCHAR(),
        existing_nullable=True,
    )
    op.alter_column(
        "problem_solving_questions",
        "output_format",
        existing_type=sa.Text(),
        type_=sa.VARCHAR(),
        existing_nullable=False,
    )
    op.alter_column(
        "problem_solving_questions",
        "input_format",
        existing_type=sa.Text(),
        type_=sa.VARCHAR(),
        existing_nullable=False,
    )
    op.alter_column(
        "problem_solving_questions",
        "problem_description",
        existing_type=sa.Text(),
        type_=sa.VARCHAR(),
        existing_nullable=False,
    )
    op.alter_column(
        "problem_solving_questions",
        "question_level",
        existing_type=sa.Text(),
        type_=sa.VARCHAR(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###