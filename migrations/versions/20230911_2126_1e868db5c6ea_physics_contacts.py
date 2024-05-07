"""physics contacts

Revision ID: 1e868db5c6ea
Revises: 77d9cf76373d
Create Date: 2023-09-11 21:26:56.710172

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '1e868db5c6ea'
down_revision = '77d9cf76373d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("STG_PHYSICS")
    op.create_table(
        'contacts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('phone', sa.String(), nullable=True),
        sa.Column('workplace', sa.String(), nullable=True),
        sa.Column('upload_ts', sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_PHYSICS',
    )
    op.create_group(
        "test_dwh_stg_physics_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_read"
    )
    op.create_group(
        "test_dwh_stg_physics_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_write"
    )
    op.create_group(
        "test_dwh_stg_physics_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_all"
    )
    op.grant_on_schema(
        "test_dwh_stg_physics_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_read",
        "STG_PHYSICS",
    )
    op.grant_on_schema(
        "test_dwh_stg_physics_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_write",
        "STG_PHYSICS",
    )
    op.grant_on_schema(
        "test_dwh_stg_physics_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_all",
        "STG_PHYSICS",
    )
    op.grant_on_table(
        "test_dwh_stg_physics_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_read",
        ['SELECT'],
        '"STG_PHYSICS".contacts',
    )
    op.grant_on_table(
        "test_dwh_stg_physics_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PHYSICS".contacts',
    )
    op.grant_on_table(
        "test_dwh_stg_physics_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_all",
        ['ALL'],
        '"STG_PHYSICS".contacts',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_stg_physics_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_all",
        ['ALL'],
        '"STG_PHYSICS".contacts',
    )
    op.revoke_on_table(
        "test_dwh_stg_physics_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_PHYSICS".contacts',
    )
    op.revoke_on_table(
        "test_dwh_stg_physics_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_read",
        ['SELECT'],
        '"STG_PHYSICS".contacts',
    )
    op.revoke_on_schema(
        "test_dwh_stg_physics_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_all",
        "STG_PHYSICS",
    )
    op.revoke_on_schema(
        "test_dwh_stg_physics_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_write",
        "STG_PHYSICS",
    )
    op.revoke_on_schema(
        "test_dwh_stg_physics_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_read",
        "STG_PHYSICS",
    )
    op.drop_table('contacts', schema='STG_PHYSICS')
    op.delete_group(
        "test_dwh_stg_physics_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_all"
    )
    op.delete_group(
        "test_dwh_stg_physics_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_write"
    )
    op.delete_group(
        "test_dwh_stg_physics_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_physics_read"
    )
    op.drop_table_schema("STG_PHYSICS")
