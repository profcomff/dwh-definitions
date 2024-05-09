"""Add container log

Revision ID: 6f659c404b5f
Revises: 45f0a9e06fca
Create Date: 2024-05-07 02:46:24.397656

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '6f659c404b5f'
down_revision = '45f0a9e06fca'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("STG_INFRA")
    op.create_table(
        'container_log',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('record', sa.String(), nullable=True),
        sa.Column('container_name', sa.String(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_INFRA',
    )
    op.create_group(
        "test_dwh_stg_infra_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_read"
    )
    op.create_group(
        "test_dwh_stg_infra_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_write"
    )
    op.create_group("test_dwh_stg_infra_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_all")
    op.grant_on_schema(
        "test_dwh_stg_infra_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_read",
        "STG_INFRA",
    )
    op.grant_on_schema(
        "test_dwh_stg_infra_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_write",
        "STG_INFRA",
    )
    op.grant_on_schema(
        "test_dwh_stg_infra_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_all", "STG_INFRA"
    )
    op.grant_on_table(
        "test_dwh_stg_infra_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_read",
        ['SELECT'],
        '"STG_INFRA".container_log',
    )
    op.grant_on_table(
        "test_dwh_stg_infra_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_INFRA".container_log',
    )
    op.grant_on_table(
        "test_dwh_stg_infra_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_all",
        ['ALL'],
        '"STG_INFRA".container_log',
    )

    # Old
    op.alter_column('union_member', 'card_user', existing_type=sa.VARCHAR(), nullable=True, schema='STG_UNION_MEMBER')


def downgrade():
    op.revoke_on_schema(
        "test_dwh_stg_infra_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_all",
        "STG_INFRA",
    )
    op.revoke_on_schema(
        ("test_dwh_stg_infra_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_write"),
        "STG_INFRA",
    )
    op.revoke_on_schema(
        ("test_dwh_stg_infra_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_read"),
        "STG_INFRA",
    )
    op.drop_table('container_log', schema='STG_INFRA')
    op.delete_group("test_dwh_stg_infra_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_all")
    op.delete_group(
        "test_dwh_stg_infra_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_write"
    )
    op.delete_group(
        "test_dwh_stg_infra_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_read"
    )
    op.drop_table_schema("STG_INFRA")

    # Old
    op.alter_column('union_member', 'card_user', existing_type=sa.VARCHAR(), nullable=False, schema='STG_UNION_MEMBER')
