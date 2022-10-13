"""create posts table

Revision ID: f9c9eb0a39cb
Revises: 
Create Date: 2022-10-12 21:06:55.575003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9c9eb0a39cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('fposts', sa.Column("id", sa.Integer(), nullable=False, primary_key = True), 
                            sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_table('fposts')
    pass
