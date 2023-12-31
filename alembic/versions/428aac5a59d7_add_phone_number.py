"""add phone number

Revision ID: 428aac5a59d7
Revises: 905891892131
Create Date: 2023-08-01 13:15:39.654630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '428aac5a59d7'
down_revision = '905891892131'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
