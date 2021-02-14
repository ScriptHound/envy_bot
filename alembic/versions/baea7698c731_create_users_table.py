"""create users table

Revision ID: baea7698c731
Revises: 
Create Date: 2021-02-14 03:53:34.634632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baea7698c731'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.String(100), nullable=False),
        sa.Column('username', sa.Unicode(150))
    )


def downgrade():
    op.drop_table('users')
