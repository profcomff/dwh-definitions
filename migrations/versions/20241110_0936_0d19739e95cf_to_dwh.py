"""to_dwh

Revision ID: 0d19739e95cf
Revises: 9fcb159af046
Create Date: 2024-11-10 09:36:33.067024

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '0d19739e95cf'
down_revision = '9fcb159af046'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("DWH_AUTH_USER")
    op.create_table(
        'info',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('phone_number', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='DWH_AUTH_USER',
    )
    op.create_group(
        "test_dwh_dwh_auth_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_read"
    )
    op.create_group(
        "test_dwh_dwh_auth_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_write"
    )
    op.create_group(
        "test_dwh_dwh_auth_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_all"
    )
    op.grant_on_schema(
        "test_dwh_dwh_auth_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_read",
        "DWH_AUTH_USER",
    )
    op.grant_on_schema(
        "test_dwh_dwh_auth_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_write",
        "DWH_AUTH_USER",
    )
    op.grant_on_schema(
        "test_dwh_dwh_auth_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_all",
        "DWH_AUTH_USER",
    )
    op.grant_on_table(
        "test_dwh_dwh_auth_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_read",
        ['SELECT'],
        '"DWH_AUTH_USER".info',
    )
    op.grant_on_table(
        "test_dwh_dwh_auth_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_AUTH_USER".info',
    )
    op.grant_on_table(
        "test_dwh_dwh_auth_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_all",
        ['ALL'],
        '"DWH_AUTH_USER".info',
    )
    op.create_index(op.f('ix_DWH_AUTH_USER_info_id'), 'info', ['id'], unique=False, schema='DWH_AUTH_USER')
    op.drop_index('ix_ODS_USER_info_id', table_name='info', schema='ODS_USER')
    op.revoke_on_table(
        "test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read",
        ['SELECT'],
        '"ODS_USER".info',
    )
    op.revoke_on_table(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USER".info',
    )
    op.revoke_on_table(
        "test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all",
        ['ALL'],
        '"ODS_USER".info',
    )
    op.revoke_on_schema(
        "test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read", "ODS_USER"
    )
    op.revoke_on_schema(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write", "ODS_USER"
    )
    op.revoke_on_schema(
        "test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all", "ODS_USER"
    )
    op.drop_table('info', schema='ODS_USER')
    op.delete_group("test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read")
    op.delete_group(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write"
    )
    op.delete_group("test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all")
    op.drop_table_schema("ODS_USER")


def downgrade():
    op.create_table_schema("ODS_USER")
    op.create_table(
        'info',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name='info_pkey'),
        schema='ODS_USER',
    )
    op.create_group("test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all")
    op.create_group(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write"
    )
    op.create_group("test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read")
    op.grant_on_schema(
        "test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all", "ODS_USER"
    )
    op.grant_on_schema(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write", "ODS_USER"
    )
    op.grant_on_schema(
        "test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read", "ODS_USER"
    )
    op.grant_on_table(
        "test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all",
        ['ALL'],
        '"ODS_USER".info',
    )
    op.grant_on_table(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USER".info',
    )
    op.grant_on_table(
        "test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read",
        ['SELECT'],
        '"ODS_USER".info',
    )
    op.create_index('ix_ODS_USER_info_id', 'info', ['id'], unique=False, schema='ODS_USER')
    op.drop_index(op.f('ix_DWH_AUTH_USER_info_id'), table_name='info', schema='DWH_AUTH_USER')
    op.revoke_on_table(
        "test_dwh_dwh_auth_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_all",
        ['ALL'],
        '"DWH_AUTH_USER".info',
    )
    op.revoke_on_table(
        "test_dwh_dwh_auth_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DWH_AUTH_USER".info',
    )
    op.revoke_on_table(
        "test_dwh_dwh_auth_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_read",
        ['SELECT'],
        '"DWH_AUTH_USER".info',
    )
    op.revoke_on_schema(
        "test_dwh_dwh_auth_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_all",
        "DWH_AUTH_USER",
    )
    op.revoke_on_schema(
        "test_dwh_dwh_auth_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_write",
        "DWH_AUTH_USER",
    )
    op.revoke_on_schema(
        "test_dwh_dwh_auth_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_read",
        "DWH_AUTH_USER",
    )
    op.drop_table('info', schema='DWH_AUTH_USER')
    op.delete_group(
        "test_dwh_dwh_auth_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_all"
    )
    op.delete_group(
        "test_dwh_dwh_auth_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_write"
    )
    op.delete_group(
        "test_dwh_dwh_auth_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dwh_auth_user_read"
    )
    op.drop_table_schema("DWH_AUTH_USER")
