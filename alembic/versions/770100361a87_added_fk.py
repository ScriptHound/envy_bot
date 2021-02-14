"""Added FK

Revision ID: 770100361a87
Revises: 8d49351fb0fe
Create Date: 2021-02-14 05:56:34.500352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '770100361a87'
down_revision = '8d49351fb0fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('films', sa.Column('user', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'films', 'users', ['user'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'films', type_='foreignkey')
    op.drop_column('films', 'user')
    # ### end Alembic commands ###
