"""Rights

Revision ID: fa6331fe4c72
Revises: 0a24041f09d1
Create Date: 2023-08-28 13:35:51.998963

"""

import os

from alembic import op


# revision identifiers, used by Alembic.
revision = 'fa6331fe4c72'
down_revision = '0a24041f09d1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_group(
        "test_dwh_stg_union_member_read"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_stg_union_member_read"
    )
    op.create_group(
        "test_dwh_stg_union_member_write"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_stg_union_member_write"
    )
    op.create_group(
        "test_dwh_stg_union_member_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_union_member_all"
    )
    op.grant_on_schema(
        (
            "test_dwh_stg_union_member_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_union_member_read"
        ),
        "STG_UNION_MEMBER",
    )
    op.grant_on_schema(
        (
            "test_dwh_stg_union_member_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_union_member_write"
        ),
        "STG_UNION_MEMBER",
    )
    op.grant_on_schema(
        (
            "test_dwh_stg_union_member_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_union_member_all"
        ),
        "STG_UNION_MEMBER",
    )
    op.grant_on_table(
        (
            "test_dwh_stg_union_member_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_union_member_read"
        ),
        ['SELECT'],
        '"STG_UNION_MEMBER".union_member',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_union_member_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_union_member_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_UNION_MEMBER".union_member',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_union_member_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_union_member_all"
        ),
        ['ALL'],
        '"STG_UNION_MEMBER".union_member',
    )


def downgrade():
    op.revoke_on_table(
        (
            "test_dwh_stg_union_member_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_union_member_all"
        ),
        ['ALL'],
        '"STG_UNION_MEMBER".union_member',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_union_member_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_union_member_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_UNION_MEMBER".union_member',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_union_member_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_union_member_read"
        ),
        ['SELECT'],
        '"STG_UNION_MEMBER".union_member',
    )
    op.revoke_on_schema(
        (
            "test_dwh_stg_union_member_all"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_union_member_all"
        ),
        "STG_UNION_MEMBER",
    )
    op.revoke_on_schema(
        (
            "test_dwh_stg_union_member_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_union_member_write"
        ),
        "STG_UNION_MEMBER",
    )
    op.revoke_on_schema(
        (
            "test_dwh_stg_union_member_read"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_union_member_read"
        ),
        "STG_UNION_MEMBER",
    )
    op.delete_group(
        "test_dwh_stg_union_member_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_union_member_all"
    )
    op.delete_group(
        "test_dwh_stg_union_member_write"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_stg_union_member_write"
    )
    op.delete_group(
        "test_dwh_stg_union_member_read"
        if os.getenv("ENVIRONMENT") != "production"
        else "prod_dwh_stg_union_member_read"
    )
