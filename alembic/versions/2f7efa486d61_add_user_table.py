"""add user table

Revision ID: 2f7efa486d61
Revises: 107a2c7e4df3
Create Date: 2022-10-13 15:34:01.052928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f7efa486d61'
down_revision = '107a2c7e4df3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('fusers', 
                    sa.Column("id", sa.Integer(), nullable = False),
                    sa.Column("email", sa.String(), nullable = False),
                    sa.Column("password", sa.String(), nullable = False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), 
                                    server_default = sa.text('now()'), nullable = False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                  )
    pass


def downgrade() -> None:
    op.drop_table('fusers')
    pass
