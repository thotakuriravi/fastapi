"""add content to the posts table

Revision ID: 107a2c7e4df3
Revises: f9c9eb0a39cb
Create Date: 2022-10-13 15:27:37.454288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '107a2c7e4df3'
down_revision = 'f9c9eb0a39cb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('fposts', sa.Column('content', sa.Integer(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('fposts', 'content')
    pass
