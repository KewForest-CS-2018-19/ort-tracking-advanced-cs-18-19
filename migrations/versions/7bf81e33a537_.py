"""empty message

Revision ID: 7bf81e33a537
Revises: 
Create Date: 2019-04-15 12:18:46.845645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bf81e33a537'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('school',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('notes', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('date_joined', sa.Date(), nullable=True),
    sa.Column('url', sa.String(length=128), nullable=True),
    sa.Column('number_of_students', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_school_date_joined'), 'school', ['date_joined'], unique=False)
    op.create_index(op.f('ix_school_name'), 'school', ['name'], unique=True)
    op.create_index(op.f('ix_school_notes'), 'school', ['notes'], unique=False)
    op.create_index(op.f('ix_school_number_of_students'), 'school', ['number_of_students'], unique=False)
    op.create_index(op.f('ix_school_url'), 'school', ['url'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('date_joined', sa.Date(), nullable=True),
    sa.Column('school_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['school_id'], ['school.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_date_joined'), 'user', ['date_joined'], unique=False)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('notes', sa.String(length=128), nullable=True),
    sa.Column('wdate', sa.Date(), nullable=True),
    sa.Column('weight_of_ort', sa.String(length=128), nullable=True),
    sa.Column('weight_of_compost', sa.String(length=128), nullable=True),
    sa.Column('groups', sa.String(length=128), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('school_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['school_id'], ['school.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_data_groups'), 'data', ['groups'], unique=False)
    op.create_index(op.f('ix_data_notes'), 'data', ['notes'], unique=False)
    op.create_index(op.f('ix_data_wdate'), 'data', ['wdate'], unique=False)
    op.create_index(op.f('ix_data_weight_of_compost'), 'data', ['weight_of_compost'], unique=False)
    op.create_index(op.f('ix_data_weight_of_ort'), 'data', ['weight_of_ort'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_data_weight_of_ort'), table_name='data')
    op.drop_index(op.f('ix_data_weight_of_compost'), table_name='data')
    op.drop_index(op.f('ix_data_wdate'), table_name='data')
    op.drop_index(op.f('ix_data_notes'), table_name='data')
    op.drop_index(op.f('ix_data_groups'), table_name='data')
    op.drop_table('data')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index(op.f('ix_user_date_joined'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_school_url'), table_name='school')
    op.drop_index(op.f('ix_school_number_of_students'), table_name='school')
    op.drop_index(op.f('ix_school_notes'), table_name='school')
    op.drop_index(op.f('ix_school_name'), table_name='school')
    op.drop_index(op.f('ix_school_date_joined'), table_name='school')
    op.drop_table('school')
    # ### end Alembic commands ###