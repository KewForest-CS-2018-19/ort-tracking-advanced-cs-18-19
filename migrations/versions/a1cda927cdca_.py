"""empty message

Revision ID: a1cda927cdca
Revises: 
Create Date: 2019-03-11 11:47:53.825194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1cda927cdca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('date_joined', sa.Date(), nullable=True))
    op.create_index(op.f('ix_user_date_joined'), 'user', ['date_joined'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_date_joined'), table_name='user')
    op.drop_column('user', 'date_joined')
    # ### end Alembic commands ###
