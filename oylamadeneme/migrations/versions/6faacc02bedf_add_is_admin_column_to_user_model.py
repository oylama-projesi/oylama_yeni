"""Add is_admin column to User model

Revision ID: 6faacc02bedf
Revises: 
Create Date: 2024-05-22 21:55:25.560763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6faacc02bedf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('poll_options')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    op.create_table('poll_options',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('option', sa.VARCHAR(length=100), nullable=False),
    sa.Column('poll_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['poll_id'], ['poll.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
