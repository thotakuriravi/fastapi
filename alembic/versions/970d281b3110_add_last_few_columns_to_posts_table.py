"""add last few columns to posts table

Revision ID: 970d281b3110
Revises: a67c13555ed4
Create Date: 2022-10-13 16:12:13.606972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '970d281b3110'
down_revision = 'a67c13555ed4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('fposts', 
                    sa.Column('published', sa.Boolean(), server_default = 'TRUE', nullable=False))
    op.add_column('fposts',
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default = sa.text('NOW()'), nullable = False) )
    pass


def downgrade() -> None:
    op.drop_column('fposts', 'published')
    op.drop_column('fposts', 'created_at')
    pass
