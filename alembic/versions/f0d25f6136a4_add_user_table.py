"""add user table

Revision ID: f0d25f6136a4
Revises: 5aa879690a01
Create Date: 2023-08-01 12:38:19.896867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0d25f6136a4'
down_revision = '5aa879690a01'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                   sa.Column('id', sa.Integer(), nullable=False),
                   sa.Column('email', sa.String(), nullable=False),
                   sa.Column('password', sa.String(), nullable=False),
                   sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                             server_default=sa.text('now()'), nullable=False),
                   sa.PrimaryKeyConstraint('id'),
                   sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
