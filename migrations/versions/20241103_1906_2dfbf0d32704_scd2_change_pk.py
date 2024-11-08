"""scd2 change pk

Revision ID: 2dfbf0d32704
Revises: dc5fba8fbf1d
Create Date: 2024-11-03 19:06:49.108410

"""

import os

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '2dfbf0d32704'
down_revision = 'dc5fba8fbf1d'
branch_labels = None
depends_on = None


def upgrade():
    op.revoke_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_schema(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read", "ODS_INFO"
    )
    op.revoke_on_schema(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write", "ODS_INFO"
    )
    op.revoke_on_schema(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all", "ODS_INFO"
    )
    op.revoke_on_schema(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read", "ODS_AUTH"
    )
    op.revoke_on_schema(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write", "ODS_AUTH"
    )
    op.revoke_on_schema(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all", "ODS_AUTH"
    )
    op.drop_table('auth_method', schema='ODS_AUTH')
    op.drop_table('user', schema='ODS_AUTH')
    op.drop_table('param_hist', schema='ODS_INFO')
    op.drop_table('info_hist', schema='ODS_INFO')
    op.delete_group("test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read")
    op.delete_group(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write"
    )
    op.delete_group("test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all")
    op.delete_group("test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read")
    op.delete_group(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write"
    )
    op.delete_group("test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all")
    op.drop_table_schema("ODS_INFO")
    op.drop_table_schema("ODS_AUTH")


def downgrade():
    op.create_table_schema("ODS_AUTH")
    op.create_table_schema("ODS_INFO")
    op.create_table(
        'info_hist',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('param_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('source_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('value', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('create_ts', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('modify_ts', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column('valid_from_dt', sa.DATE(), autoincrement=False, nullable=True),
        sa.Column('valid_to_dt', sa.DATE(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name='info_hist_pkey'),
        schema='ODS_INFO',
        comment='\n    SCD2 historical table based on STG_USERDATA.info\n    ',
    )
    op.create_table(
        'param_hist',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('is_required', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column('changeable', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('create_ts', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('modify_ts', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column('validation', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('valid_from_dt', sa.DATE(), autoincrement=False, nullable=True),
        sa.Column('valid_to_dt', sa.DATE(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name='param_hist_pkey'),
        schema='ODS_INFO',
        comment='\n    SCD2 historical table based on STG_USERDATA.param\n    ',
    )
    op.create_table(
        'user',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column('create_ts', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('update_ts', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('valid_from_dt', sa.DATE(), autoincrement=False, nullable=True),
        sa.Column('valid_to_dt', sa.DATE(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name='user_pkey'),
        schema='ODS_AUTH',
        comment='\n    Historical table for STG_AUTH.user\n    ',
    )
    op.create_table(
        'auth_method',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('auth_method', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('param', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('value', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('create_ts', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('update_ts', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column('valid_from_dt', sa.DATE(), autoincrement=False, nullable=True),
        sa.Column('valid_to_dt', sa.DATE(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name='auth_method_pkey'),
        schema='ODS_AUTH',
        comment='\n    Historical table for STG_AUTH.auth_method\n    ',
    )
    op.create_group("test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all")
    op.create_group(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write"
    )
    op.create_group("test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read")
    op.create_group("test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all")
    op.create_group(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write"
    )
    op.create_group("test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read")
    op.grant_on_schema(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all", "ODS_AUTH"
    )
    op.grant_on_schema(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write", "ODS_AUTH"
    )
    op.grant_on_schema(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read", "ODS_AUTH"
    )
    op.grant_on_schema(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all", "ODS_INFO"
    )
    op.grant_on_schema(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write", "ODS_INFO"
    )
    op.grant_on_schema(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read", "ODS_INFO"
    )
    op.grant_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".param_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".param_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".param_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".param_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".param_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".param_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".auth_method',
    )
