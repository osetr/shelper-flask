"""Initial migration.

Revision ID: 8546a3ae42ac
Revises: 
Create Date: 2020-07-29 18:39:36.313067

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8546a3ae42ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('login', table_name='clients')
    op.drop_table('clients')
    op.drop_table('exercises')
    op.drop_table('trainings')
    op.drop_table('feedbacks')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedbacks',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.VARCHAR(length=40), nullable=False),
    sa.Column('text', mysql.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['clients.id'], name='feedbacks_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('trainings',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('training_id', mysql.VARCHAR(length=40), nullable=False),
    sa.Column('user_id', mysql.VARCHAR(length=40), nullable=False),
    sa.Column('comment', mysql.VARCHAR(length=40), nullable=True),
    sa.Column('date', sa.DATE(), nullable=False),
    sa.Column('weight', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('exercise_name', mysql.VARCHAR(length=40), nullable=False),
    sa.Column('exercise_weight', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['clients.id'], name='trainings_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('exercises',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.VARCHAR(length=40), nullable=False),
    sa.Column('date_time', mysql.DATETIME(), nullable=True),
    sa.Column('muscules_type', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('exercise_name', mysql.VARCHAR(length=40), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['clients.id'], name='exercises_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('clients',
    sa.Column('id', mysql.VARCHAR(length=40), nullable=False),
    sa.Column('login', mysql.VARCHAR(length=15), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('hashed_password', mysql.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('login', 'clients', ['login'], unique=True)
    # ### end Alembic commands ###
