"""empty message

Revision ID: 1043d3c5b9f6
Revises: 
Create Date: 2019-09-27 22:26:40.196209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1043d3c5b9f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('zzt_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('is_vip', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('zzt_template',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('view_num', sa.Integer(), nullable=True),
    sa.Column('is_vip', sa.Integer(), nullable=True),
    sa.Column('collect_num', sa.Integer(), nullable=True),
    sa.Column('down_num', sa.Integer(), nullable=True),
    sa.Column('img', sa.String(length=255), nullable=False),
    sa.Column('file_name', sa.String(length=255), nullable=False),
    sa.Column('file_type', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['zzt_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('zzt_upload',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('down_type', sa.Integer(), nullable=True),
    sa.Column('img', sa.String(length=255), nullable=False),
    sa.Column('file_name', sa.String(length=255), nullable=False),
    sa.Column('file_type', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['zzt_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('file_name')
    )
    op.create_table('zzt_collect',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('template_id', sa.Integer(), nullable=False),
    sa.Column('user_template', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['template_id'], ['zzt_template.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['zzt_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_template')
    )
    op.create_table('zzt_download',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('template_id', sa.Integer(), nullable=False),
    sa.Column('user_template', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['template_id'], ['zzt_template.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['zzt_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_template')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('zzt_download')
    op.drop_table('zzt_collect')
    op.drop_table('zzt_upload')
    op.drop_table('zzt_template')
    op.drop_table('zzt_user')
    # ### end Alembic commands ###