"""Project statuses typo

Revision ID: 5aef7ddd84d4
Revises: 1a81df9b04a5
Create Date: 2025-03-12 14:17:03.591097

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5aef7ddd84d4'
down_revision: Union[str, None] = '1a81df9b04a5'
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
