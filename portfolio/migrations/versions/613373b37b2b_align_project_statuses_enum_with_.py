"""Align project_statuses enum with PostgreSQL

Revision ID: 613373b37b2b
Revises: 4c08fd62e884
Create Date: 2024-12-18 10:41:50.425726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '613373b37b2b'
down_revision: Union[str, None] = '4c08fd62e884'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
