"""changes in mcq model

Revision ID: 5140ff82c41c
Revises: 3cd87035f6bb
Create Date: 2024-12-29 15:44:09.066914

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5140ff82c41c"
down_revision: Union[str, None] = "3cd87035f6bb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "multiple_choice_question",
        "question",
        existing_type=sa.TEXT(),
        type_=sa.String(),
        existing_nullable=False,
    )
    op.alter_column(
        "multiple_choice_question",
        "option_1",
        existing_type=sa.TEXT(),
        type_=sa.String(),
        existing_nullable=False,
    )
    op.alter_column(
        "multiple_choice_question",
        "option_2",
        existing_type=sa.TEXT(),
        type_=sa.String(),
        existing_nullable=False,
    )
    op.alter_column(
        "multiple_choice_question",
        "option_3",
        existing_type=sa.TEXT(),
        type_=sa.String(),
        existing_nullable=False,
    )
    op.alter_column(
        "multiple_choice_question",
        "option_4",
        existing_type=sa.TEXT(),
        type_=sa.String(),
        existing_nullable=False,
    )
    op.alter_column(
        "multiple_choice_question",
        "correct_answer",
        existing_type=sa.TEXT(),
        type_=sa.String(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "multiple_choice_question",
        "correct_answer",
        existing_type=sa.String(),
        type_=sa.TEXT(),
        existing_nullable=False,
    )
    op.alter_column(
        "multiple_choice_question",
        "option_4",
        existing_type=sa.String(),
        type_=sa.TEXT(),
        existing_nullable=False,
    )
    op.alter_column(
        "multiple_choice_question",
        "option_3",
        existing_type=sa.String(),
        type_=sa.TEXT(),
        existing_nullable=False,
    )
    op.alter_column(
        "multiple_choice_question",
        "option_2",
        existing_type=sa.String(),
        type_=sa.TEXT(),
        existing_nullable=False,
    )
    op.alter_column(
        "multiple_choice_question",
        "option_1",
        existing_type=sa.String(),
        type_=sa.TEXT(),
        existing_nullable=False,
    )
    op.alter_column(
        "multiple_choice_question",
        "question",
        existing_type=sa.String(),
        type_=sa.TEXT(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###