"""ODS-fix

Revision ID: da8ef5f7e99f
Revises: 45b2b6c9d08c
Create Date: 2024-11-21 20:11:05.451937

"""
from alembic import op
import sqlalchemy as sa
import os


# revision identifiers, used by Alembic.
revision = 'da8ef5f7e99f'
down_revision = '45b2b6c9d08c'
branch_labels = None
depends_on = None


def upgrade():
    # создание таблицы ODS_USER.info
    # в этот раз добавлены все необходимые колонки
    op.create_table_schema("ODS_USER")
    op.create_table('info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('vk_name', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('hometown', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('github_name', sa.String(), nullable=True),
    sa.Column('telegram_name', sa.String(), nullable=True),
    sa.Column('home_phone_number', sa.String(), nullable=True),
    sa.Column('education_level', sa.String(), nullable=True),
    sa.Column('university', sa.String(), nullable=True),
    sa.Column('group', sa.String(), nullable=True),
    sa.Column('faculty', sa.String(), nullable=True),
    sa.Column('position', sa.String(), nullable=True),
    sa.Column('student_id_number', sa.String(), nullable=True),
    sa.Column('department', sa.String(), nullable=True),
    sa.Column('mode_of_study', sa.String(), nullable=True),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('birth_date', sa.String(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('job', sa.String(), nullable=True),
    sa.Column('work_location', sa.String(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='ODS_USER'
    )
    op.create_group("test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read")
    op.create_group("test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write")
    op.create_group("test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all")
    op.grant_on_schema("test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read", "ODS_USER")
    op.grant_on_schema("test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write", "ODS_USER")
    op.grant_on_schema("test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all", "ODS_USER")
    op.grant_on_table("test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read", ['SELECT'], '"ODS_USER".info')
    op.grant_on_table("test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write", ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'], '"ODS_USER".info')
    op.grant_on_table("test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all", ['ALL'], '"ODS_USER".info')
    op.create_index(op.f('ix_ODS_USER_info_id'), 'info', ['id'], unique=False, schema='ODS_USER')
    op.grant_on_table("test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read", ['SELECT'], '"ODS_USER".info')
    op.grant_on_table("test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write", ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'], '"ODS_USER".info')
    op.grant_on_table("test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all", ['ALL'], '"ODS_USER".info')
    # ### end Alembic commands ###


def downgrade():
    op.revoke_on_table("test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all", ['ALL'], '"ODS_USER".info')
    op.revoke_on_table("test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write", ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'], '"ODS_USER".info')
    op.revoke_on_table("test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read", ['SELECT'], '"ODS_USER".info')
    op.drop_index(op.f('ix_ODS_USER_info_id'), table_name='info', schema='ODS_USER')
    op.revoke_on_table("test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all", ['ALL'], '"ODS_USER".info')
    op.revoke_on_table("test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write", ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'], '"ODS_USER".info')
    op.revoke_on_table("test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read", ['SELECT'], '"ODS_USER".info')
    op.revoke_on_schema("test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all", "ODS_USER")
    op.revoke_on_schema("test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write", "ODS_USER")
    op.revoke_on_schema("test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read", "ODS_USER")
    op.drop_table('info', schema='ODS_USER')
    op.delete_group("test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all")
    op.delete_group("test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write")
    op.delete_group("test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read")
    op.drop_table_schema("ODS_USER")
    # ### end Alembic commands ###
