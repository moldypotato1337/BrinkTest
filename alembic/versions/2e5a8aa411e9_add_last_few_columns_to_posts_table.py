"""add last few columns to posts table

Revision ID: 2e5a8aa411e9
Revises: a77642202dac
Create Date: 2023-08-01 12:50:36.420368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e5a8aa411e9'
down_revision = 'a77642202dac'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
                  'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
                  ('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
