"""adding followers

Revision ID: 665617035244
Revises: 72a3c40a35e1
Create Date: 2020-10-20 15:45:12.761253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '665617035244'
down_revision = '72a3c40a35e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###