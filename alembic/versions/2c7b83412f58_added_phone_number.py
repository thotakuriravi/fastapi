"""added phone number

Revision ID: 2c7b83412f58
Revises: 2c3c50f524fd
Create Date: 2022-10-13 16:36:20.001898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c7b83412f58'
down_revision = '2c3c50f524fd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fusers', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('fusers', 'phone_number')
    # ### end Alembic commands ###
