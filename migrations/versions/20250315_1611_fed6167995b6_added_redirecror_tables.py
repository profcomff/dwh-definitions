"""added redirecror tables

Revision ID: fed6167995b6
Revises: c335441a4bf8
Create Date: 2025-03-15 16:11:05.343147

"""

import os

import sqlalchemy as sa
from alembic import op


revision = 'fed6167995b6'
down_revision = 'c335441a4bf8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("STG_REDIRECTOR")
    op.create_table(
        'link',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('url_from', sa.String(), nullable=False),
        sa.Column('url_to', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('url_from'),
        schema='STG_REDIRECTOR',
        info={'sensitive': False},
    )
    op.create_table(
        'redirect_fact',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('link_id', sa.Integer(), nullable=False),
        sa.Column('method', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('user_agent', sa.String(), nullable=False),
        sa.Column('browser_family', sa.String(), nullable=True),
        sa.Column('browser_version', sa.String(), nullable=True),
        sa.Column('os_family', sa.String(), nullable=True),
        sa.Column('os_version', sa.String(), nullable=True),
        sa.Column('device_family', sa.String(), nullable=True),
        sa.Column('device_brand', sa.String(), nullable=True),
        sa.Column('device_model', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_REDIRECTOR',
        info={'sensitive': False},
    )
    op.create_group(
        "test_dwh_stg_redirector_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_read"
    )
    op.create_group(
        "test_dwh_stg_redirector_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_write"
    )
    op.create_group(
        "test_dwh_stg_redirector_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_all"
    )
    op.grant_on_schema(
        "test_dwh_stg_redirector_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_read",
        "STG_REDIRECTOR",
    )
    op.grant_on_schema(
        (
            "test_dwh_stg_redirector_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_redirector_write"
        ),
        "STG_REDIRECTOR",
    )
    op.grant_on_schema(
        "test_dwh_stg_redirector_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_all",
        "STG_REDIRECTOR",
    )
    op.grant_on_table(
        "test_dwh_stg_redirector_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_read",
        ['SELECT'],
        '"STG_REDIRECTOR".link',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_redirector_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_redirector_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_REDIRECTOR".link',
    )
    op.grant_on_table(
        "test_dwh_stg_redirector_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_all",
        ['ALL'],
        '"STG_REDIRECTOR".link',
    )
    op.grant_on_table(
        "test_dwh_stg_redirector_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_read",
        ['SELECT'],
        '"STG_REDIRECTOR".redirect_fact',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_redirector_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_redirector_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_REDIRECTOR".redirect_fact',
    )
    op.grant_on_table(
        "test_dwh_stg_redirector_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_all",
        ['ALL'],
        '"STG_REDIRECTOR".redirect_fact',
    )


def downgrade():
    op.create_table_schema("DM_RATING")
    op.drop_table('redirect_fact', schema='STG_REDIRECTOR')
    op.drop_table('link', schema='STG_REDIRECTOR')
    op.delete_group(
        "test_dwh_stg_redirector_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_all"
    )
    op.delete_group(
        "test_dwh_stg_redirector_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_write"
    )
    op.delete_group(
        "test_dwh_stg_redirector_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_redirector_read"
    )
    op.drop_table_schema("STG_REDIRECTOR")
