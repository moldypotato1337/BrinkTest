"""add content column to post table

Revision ID: 5aa879690a01
Revises: 21a73d90f295
Create Date: 2023-08-01 12:33:20.413793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5aa879690a01'
down_revision = '21a73d90f295'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
