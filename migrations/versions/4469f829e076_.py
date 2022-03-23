"""empty message

Revision ID: 4469f829e076
Revises: 
Create Date: 2022-03-22 22:33:16.041041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4469f829e076'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('proptitle', sa.String(length=100), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('num_of_rooms', sa.Integer(), nullable=True),
    sa.Column('num_of_bathrooms', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('proptype', sa.String(length=10), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
