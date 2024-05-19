"""Add container log in ODS

Revision ID: 45fc3ad3a4db
Revises: 6f659c404b5f
Create Date: 2024-05-07 04:36:38.538129

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '45fc3ad3a4db'
down_revision = '6f659c404b5f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("ODS_INFRA_LOGS")
    op.create_table(
        'container_log',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('record', sa.JSON(), nullable=False),
        sa.Column('container_name', sa.String(), nullable=False),
        sa.Column('create_ts', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_INFRA_LOGS',
    )
    op.create_group(
        "test_dwh_ods_infra_logs_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_infra_logs_read"
    )
    op.create_group(
        "test_dwh_ods_infra_logs_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_infra_logs_write"
    )
    op.create_group(
        "test_dwh_ods_infra_logs_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_infra_logs_all"
    )
    op.grant_on_schema(
        "test_dwh_ods_infra_logs_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_infra_logs_read",
        "ODS_INFRA_LOGS",
    )
    op.grant_on_schema(
        (
            "test_dwh_ods_infra_logs_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_ods_infra_logs_write"
        ),
        "ODS_INFRA_LOGS",
    )
    op.grant_on_schema(
        "test_dwh_ods_infra_logs_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_infra_logs_all",
        "ODS_INFRA_LOGS",
    )
    op.grant_on_table(
        "test_dwh_ods_infra_logs_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_infra_logs_read",
        ['SELECT'],
        '"ODS_INFRA_LOGS".container_log',
    )
    op.grant_on_table(
        (
            "test_dwh_ods_infra_logs_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_ods_infra_logs_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFRA_LOGS".container_log',
    )
    op.grant_on_table(
        "test_dwh_ods_infra_logs_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_infra_logs_all",
        ['ALL'],
        '"ODS_INFRA_LOGS".container_log',
    )


def downgrade():
    op.revoke_on_schema(
        "test_dwh_ods_infra_logs_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_infra_logs_all",
        "ODS_INFRA_LOGS",
    )
    op.revoke_on_schema(
        (
            "test_dwh_ods_infra_logs_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_ods_infra_logs_write"
        ),
        "ODS_INFRA_LOGS",
    )
    op.revoke_on_schema(
        (
            "test_dwh_ods_infra_logs_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_ods_infra_logs_read"
        ),
        "ODS_INFRA_LOGS",
    )
    op.drop_table('container_log', schema='ODS_INFRA_LOGS')
    op.delete_group(
        "test_dwh_ods_infra_logs_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_infra_logs_all"
    )
    op.delete_group(
        "test_dwh_ods_infra_logs_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_infra_logs_write"
    )
    op.delete_group(
        "test_dwh_ods_infra_logs_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_infra_logs_read"
    )
    op.drop_table_schema("ODS_INFRA_LOGS")
