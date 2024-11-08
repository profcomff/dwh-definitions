"""scd2 change pk2

Revision ID: b9ae5eb51c58
Revises: 2dfbf0d32704
Create Date: 2024-11-03 19:07:36.862862

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'b9ae5eb51c58'
down_revision = '2dfbf0d32704'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("ODS_INFO")
    op.create_table_schema("ODS_AUTH")
    op.create_table(
        'auth_method',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('auth_method', sa.String(), nullable=True),
        sa.Column('param', sa.String(), nullable=True),
        sa.Column('value', sa.String(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('update_ts', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.Column('valid_from_dt', sa.Date(), nullable=True),
        sa.Column('valid_to_dt', sa.Date(), nullable=True),
        schema='ODS_AUTH',
        comment='\n    Historical table for STG_AUTH.auth_method\n    ',
    )
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('update_ts', sa.DateTime(), nullable=True),
        sa.Column('valid_from_dt', sa.Date(), nullable=True),
        sa.Column('valid_to_dt', sa.Date(), nullable=True),
        schema='ODS_AUTH',
        comment='\n    Historical table for STG_AUTH.user\n    ',
    )
    op.create_table(
        'info_hist',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('param_id', sa.Integer(), nullable=True),
        sa.Column('source_id', sa.Integer(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=True),
        sa.Column('value', sa.String(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('modify_ts', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.Column('valid_from_dt', sa.Date(), nullable=True),
        sa.Column('valid_to_dt', sa.Date(), nullable=True),
        schema='ODS_INFO',
        comment='\n    SCD2 historical table based on STG_USERDATA.info\n    ',
    )
    op.create_table(
        'param_hist',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('category_id', sa.Integer(), nullable=True),
        sa.Column('is_required', sa.Boolean(), nullable=True),
        sa.Column('changeable', sa.Boolean(), nullable=True),
        sa.Column('type', sa.String(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('modify_ts', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.Column('validation', sa.String(), nullable=True),
        sa.Column('valid_from_dt', sa.Date(), nullable=True),
        sa.Column('valid_to_dt', sa.Date(), nullable=True),
        schema='ODS_INFO',
        comment='\n    SCD2 historical table based on STG_USERDATA.param\n    ',
    )
    op.create_group("test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read")
    op.create_group(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write"
    )
    op.create_group("test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all")
    op.create_group("test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read")
    op.create_group(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write"
    )
    op.create_group("test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all")
    op.grant_on_schema(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read", "ODS_INFO"
    )
    op.grant_on_schema(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write", "ODS_INFO"
    )
    op.grant_on_schema(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all", "ODS_INFO"
    )
    op.grant_on_schema(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read", "ODS_AUTH"
    )
    op.grant_on_schema(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write", "ODS_AUTH"
    )
    op.grant_on_schema(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all", "ODS_AUTH"
    )
    op.grant_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".param_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".param_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".param_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".param_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".param_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".param_hist',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_schema(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all", "ODS_AUTH"
    )
    op.revoke_on_schema(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write", "ODS_AUTH"
    )
    op.revoke_on_schema(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read", "ODS_AUTH"
    )
    op.revoke_on_schema(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all", "ODS_INFO"
    )
    op.revoke_on_schema(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write", "ODS_INFO"
    )
    op.revoke_on_schema(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read", "ODS_INFO"
    )
    op.drop_table('param_hist', schema='ODS_INFO')
    op.drop_table('info_hist', schema='ODS_INFO')
    op.drop_table('user', schema='ODS_AUTH')
    op.drop_table('auth_method', schema='ODS_AUTH')
    op.delete_group("test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all")
    op.delete_group(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write"
    )
    op.delete_group("test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read")
    op.delete_group("test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all")
    op.delete_group(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write"
    )
    op.delete_group("test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read")
    op.drop_table_schema("ODS_AUTH")
    op.drop_table_schema("ODS_INFO")
