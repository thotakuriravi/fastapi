"""add foreign-key to post table

Revision ID: a67c13555ed4
Revises: 2f7efa486d61
Create Date: 2022-10-13 16:03:50.842295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a67c13555ed4'
down_revision = '2f7efa486d61'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('fposts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('post_user_fkey', source_table='fposts', 
                          referent_table='fusers', local_cols=['owner_id'],
                            remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fkey', table_name="fposts")
    op.drop_column("fposts", 'owner_id')
    pass
