"""empty message

Revision ID: 56d90a3a925a
Revises: None
Create Date: 2016-08-19 10:02:20.476312

"""

# revision identifiers, used by Alembic.
revision = '56d90a3a925a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    ### end Alembic commands ###
