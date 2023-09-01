"""add social

Revision ID: 4df46ea2b0f9
Revises: fa6331fe4c72
Create Date: 2023-09-01 21:26:00.694456

"""
import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '4df46ea2b0f9'
down_revision = 'fa6331fe4c72'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'social_activity',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('system', sa.String(), nullable=False),
        sa.Column('message', sa.JSON(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_SOCIAL',
    )
    op.create_table(
        'test', sa.Column('id', sa.Integer(), nullable=False), sa.PrimaryKeyConstraint('id'), schema='TESTS_DATABASE'
    )
    op.create_group(
        "test_dwh_tests_database_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_read"
    )
    op.create_group(
        "test_dwh_tests_database_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_write"
    )
    op.create_group(
        "test_dwh_tests_database_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_all"
    )
    op.create_group(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read"
    )
    op.create_group(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write"
    )
    op.create_group(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all"
    )
    op.grant_on_schema(
        "test_dwh_tests_database_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_read",
        "TESTS_DATABASE",
    )
    op.grant_on_schema(
        "test_dwh_tests_database_write"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_tests_database_write",
        "TESTS_DATABASE",
    )
    op.grant_on_schema(
        "test_dwh_tests_database_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_all",
        "TESTS_DATABASE",
    )
    op.grant_on_schema(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        "STG_SOCIAL",
    )
    op.grant_on_schema(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        "STG_SOCIAL",
    )
    op.grant_on_schema(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        "STG_SOCIAL",
    )
    op.grant_on_table(
        "test_dwh_tests_database_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_read",
        ['SELECT'],
        '"TESTS_DATABASE".test',
    )
    op.grant_on_table(
        "test_dwh_tests_database_write"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_tests_database_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"TESTS_DATABASE".test',
    )
    op.grant_on_table(
        "test_dwh_tests_database_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_all",
        ['ALL'],
        '"TESTS_DATABASE".test',
    )
    op.grant_on_table(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        ['SELECT'],
        '"STG_SOCIAL".social_activity',
    )
    op.grant_on_table(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SOCIAL".social_activity',
    )
    op.grant_on_table(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        ['ALL'],
        '"STG_SOCIAL".social_activity',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        ['ALL'],
        '"STG_SOCIAL".social_activity',
    )
    op.revoke_on_table(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_SOCIAL".social_activity',
    )
    op.revoke_on_table(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        ['SELECT'],
        '"STG_SOCIAL".social_activity',
    )
    op.revoke_on_table(
        "test_dwh_tests_database_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_all",
        ['ALL'],
        '"TESTS_DATABASE".test',
    )
    op.revoke_on_table(
        "test_dwh_tests_database_write"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_tests_database_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"TESTS_DATABASE".test',
    )
    op.revoke_on_table(
        "test_dwh_tests_database_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_read",
        ['SELECT'],
        '"TESTS_DATABASE".test',
    )
    op.revoke_on_schema(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all",
        "STG_SOCIAL",
    )
    op.revoke_on_schema(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write",
        "STG_SOCIAL",
    )
    op.revoke_on_schema(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read",
        "STG_SOCIAL",
    )
    op.revoke_on_schema(
        "test_dwh_tests_database_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_all",
        "TESTS_DATABASE",
    )
    op.revoke_on_schema(
        "test_dwh_tests_database_write"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_tests_database_write",
        "TESTS_DATABASE",
    )
    op.revoke_on_schema(
        "test_dwh_tests_database_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_read",
        "TESTS_DATABASE",
    )
    op.drop_table('test', schema='TESTS_DATABASE')
    op.drop_table('social_activity', schema='STG_SOCIAL')
    op.delete_group(
        "test_dwh_stg_social_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_all"
    )
    op.delete_group(
        "test_dwh_stg_social_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_write"
    )
    op.delete_group(
        "test_dwh_stg_social_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_social_read"
    )
    op.delete_group(
        "test_dwh_tests_database_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_all"
    )
    op.delete_group(
        "test_dwh_tests_database_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_write"
    )
    op.delete_group(
        "test_dwh_tests_database_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_tests_database_read"
    )
