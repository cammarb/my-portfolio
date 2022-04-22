"""add date column to blog

Revision ID: a948513a683c
Revises: d04b907bb596
Create Date: 2022-04-20 13:18:45.151509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a948513a683c'
down_revision = 'd04b907bb596'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('date', sa.Date(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog', 'date')
    # ### end Alembic commands ###