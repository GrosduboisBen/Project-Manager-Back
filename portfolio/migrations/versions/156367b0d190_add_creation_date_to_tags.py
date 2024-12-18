"""Add creation_date to tags

Revision ID: 156367b0d190
Revises: 4fa9e36a11b4
Create Date: 2024-12-18 11:55:18.562687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '156367b0d190'
down_revision: Union[str, None] = '4fa9e36a11b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tags', sa.Column('creation_date', sa.TIMESTAMP(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tags', 'creation_date')
    # ### end Alembic commands ###