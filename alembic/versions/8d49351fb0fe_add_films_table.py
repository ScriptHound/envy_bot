"""Add films table

Revision ID: 8d49351fb0fe
Revises: baea7698c731
Create Date: 2021-02-14 03:54:34.124248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d49351fb0fe'
down_revision = 'baea7698c731'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'films',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('film_name', sa.Unicode(300), nullable=False),
        sa.Column('date_created', sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table('films')
