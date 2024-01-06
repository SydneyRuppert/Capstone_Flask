"""empty message

Revision ID: 14c83810b075
Revises: 875ab8831c0e
Create Date: 2024-01-05 18:05:03.345559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14c83810b075'
down_revision = '875ab8831c0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uid', sa.String(), nullable=True))
        batch_op.drop_constraint('contact_user_token_fkey', type_='foreignkey')
        batch_op.drop_column('user_token')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_token', sa.VARCHAR(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('contact_user_token_fkey', 'user', ['user_token'], ['token'])
        batch_op.drop_column('uid')

    # ### end Alembic commands ###
