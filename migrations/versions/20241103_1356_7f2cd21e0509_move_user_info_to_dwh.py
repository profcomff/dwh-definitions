"""move_user_info_to_dwh

Revision ID: 7f2cd21e0509
Revises: cf7557c43271
Create Date: 2024-11-03 13:56:02.161497

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '7f2cd21e0509'
down_revision = 'cf7557c43271'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("DWH_USER_INFO")
    op.create_table(
        'info',
        sa.Column('user_id', sa.Integer(), nullable=False),
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
        sa.PrimaryKeyConstraint('user_id'),
        schema='DWH_USER_INFO',
    )
    op.create_group(
        "test_dwh_dwh_user_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_read"
    )
    op.create_group(
        "test_dwh_dwh_user_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_write"
    )
    op.create_group(
        "test_dwh_dwh_user_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_all"
    )
    op.grant_on_schema(
        "test_dwh_dwh_user_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_read",
        "DWH_USER_INFO",
    )
    op.grant_on_schema(
        "test_dwh_dwh_user_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_write",
        "DWH_USER_INFO",
    )
    op.grant_on_schema(
        "test_dwh_dwh_user_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_all",
        "DWH_USER_INFO",
    )
    op.grant_on_table(
        "test_dwh_dwh_user_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_read",
        ['SELECT'],
        '"DWH_USER_INFO".info',
    )
    op.grant_on_table(
        "test_dwh_dwh_user_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_USER_INFO".info',
    )
    op.grant_on_table(
        "test_dwh_dwh_user_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_all",
        ['ALL'],
        '"DWH_USER_INFO".info',
    )
    op.create_index(op.f('ix_DWH_USER_INFO_info_user_id'), 'info', ['user_id'], unique=False, schema='DWH_USER_INFO')
    op.grant_on_table(
        "test_dwh_dwh_user_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_read",
        ['SELECT'],
        '"DWH_USER_INFO".info',
    )
    op.grant_on_table(
        "test_dwh_dwh_user_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_USER_INFO".info',
    )
    op.grant_on_table(
        "test_dwh_dwh_user_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_all",
        ['ALL'],
        '"DWH_USER_INFO".info',
    )
    op.drop_index('ix_ODS_INFO_info_user_id', table_name='info', schema='ODS_INFO')
    op.revoke_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info',
    )
    op.drop_table('info', schema='ODS_INFO')


def downgrade():
    op.create_table(
        'info',
        sa.Column('user_id', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('vk_name', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('hometown', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('location', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('github_name', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('telegram_name', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('home_phone_number', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('education_level', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('university', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('group', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('faculty', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('position', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('student_id_number', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('department', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('mode_of_study', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('birth_date', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('photo', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('sex', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('job', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('work_location', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('user_id', name='info_pkey'),
        schema='ODS_INFO',
    )
    op.grant_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info',
    )
    op.grant_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info',
    )
    op.grant_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info',
    )
    op.create_index('ix_ODS_INFO_info_user_id', 'info', ['user_id'], unique=False, schema='ODS_INFO')
    op.revoke_on_table(
        "test_dwh_dwh_user_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_all",
        ['ALL'],
        '"DWH_USER_INFO".info',
    )
    op.revoke_on_table(
        "test_dwh_dwh_user_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_USER_INFO".info',
    )
    op.revoke_on_table(
        "test_dwh_dwh_user_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_read",
        ['SELECT'],
        '"DWH_USER_INFO".info',
    )
    op.drop_index(op.f('ix_DWH_USER_INFO_info_user_id'), table_name='info', schema='DWH_USER_INFO')
    op.revoke_on_table(
        "test_dwh_dwh_user_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_all",
        ['ALL'],
        '"DWH_USER_INFO".info',
    )
    op.revoke_on_table(
        "test_dwh_dwh_user_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_USER_INFO".info',
    )
    op.revoke_on_table(
        "test_dwh_dwh_user_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_read",
        ['SELECT'],
        '"DWH_USER_INFO".info',
    )
    op.revoke_on_schema(
        "test_dwh_dwh_user_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_all",
        "DWH_USER_INFO",
    )
    op.revoke_on_schema(
        "test_dwh_dwh_user_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_write",
        "DWH_USER_INFO",
    )
    op.revoke_on_schema(
        "test_dwh_dwh_user_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_read",
        "DWH_USER_INFO",
    )
    op.drop_table('info', schema='DWH_USER_INFO')
    op.delete_group(
        "test_dwh_dwh_user_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_all"
    )
    op.delete_group(
        "test_dwh_dwh_user_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_write"
    )
    op.delete_group(
        "test_dwh_dwh_user_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_user_info_read"
    )
    op.drop_table_schema("DWH_USER_INFO")
