"""ODS.user.info

Revision ID: 9fcb159af046
Revises: b9ae5eb51c58
Create Date: 2024-11-08 18:45:55.547982

"""

import os

import sqlalchemy as sa
from alembic import op


revision = '9fcb159af046'
down_revision = 'b9ae5eb51c58'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("ODS_USER")
    op.create_table(
        'info',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('phone_number', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_USER',
    )
    op.create_group("test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read")
    op.create_group(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write"
    )
    op.create_group("test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all")
    op.grant_on_schema(
        "test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read", "ODS_USER"
    )
    op.grant_on_schema(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write", "ODS_USER"
    )
    op.grant_on_schema(
        "test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all", "ODS_USER"
    )
    op.grant_on_table(
        "test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read",
        ['SELECT'],
        '"ODS_USER".info',
    )
    op.grant_on_table(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USER".info',
    )
    op.grant_on_table(
        "test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all",
        ['ALL'],
        '"ODS_USER".info',
    )
    op.create_index(op.f('ix_ODS_USER_info_id'), 'info', ['id'], unique=False, schema='ODS_USER')
    op.grant_on_table(
        "test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read",
        ['SELECT'],
        '"ODS_USER".info',
    )
    op.grant_on_table(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USER".info',
    )
    op.grant_on_table(
        "test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all",
        ['ALL'],
        '"ODS_USER".info',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all",
        ['ALL'],
        '"ODS_USER".info',
    )
    op.revoke_on_table(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USER".info',
    )
    op.revoke_on_table(
        "test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read",
        ['SELECT'],
        '"ODS_USER".info',
    )
    op.drop_index(op.f('ix_ODS_USER_info_id'), table_name='info', schema='ODS_USER')
    op.revoke_on_table(
        "test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all",
        ['ALL'],
        '"ODS_USER".info',
    )
    op.revoke_on_table(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_USER".info',
    )
    op.revoke_on_table(
        "test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read",
        ['SELECT'],
        '"ODS_USER".info',
    )
    op.revoke_on_schema(
        "test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all", "ODS_USER"
    )
    op.revoke_on_schema(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write", "ODS_USER"
    )
    op.revoke_on_schema(
        "test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read", "ODS_USER"
    )
    op.drop_table('info', schema='ODS_USER')
    op.delete_group("test_dwh_ods_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_all")
    op.delete_group(
        "test_dwh_ods_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_write"
    )
    op.delete_group("test_dwh_ods_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_user_read")
    op.drop_table_schema("ODS_USER")
