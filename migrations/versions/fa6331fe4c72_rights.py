"""rights

Revision ID: fa6331fe4c72
Revises: 0a24041f09d1
Create Date: 2023-08-27 12:52:22.735632

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'fa6331fe4c72'
down_revision = '0a24041f09d1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_group("test_dwh_STG_UNION_MEMBER_read")
    op.create_group("test_dwh_STG_UNION_MEMBER_write")
    op.create_group("test_dwh_STG_UNION_MEMBER_all")
    op.grant_rights("test_dwh_STG_UNION_MEMBER_read", "['SELECT']", '"STG_UNION_MEMBER".union_member')
    op.grant_rights(
        "test_dwh_STG_UNION_MEMBER_write",
        "['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE']",
        '"STG_UNION_MEMBER".union_member',
    )
    op.grant_rights("test_dwh_STG_UNION_MEMBER_all", "['ALL']", '"STG_UNION_MEMBER".union_member')


def downgrade():
    op.revoke_rights("test_dwh_STG_UNION_MEMBER_all", "['ALL']", '"STG_UNION_MEMBER".union_member')
    op.revoke_rights(
        "test_dwh_STG_UNION_MEMBER_write",
        "['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE']",
        '"STG_UNION_MEMBER".union_member',
    )
    op.revoke_rights("test_dwh_STG_UNION_MEMBER_read", "['SELECT']", '"STG_UNION_MEMBER".union_member')
    op.delete_group("test_dwh_STG_UNION_MEMBER_all")
    op.delete_group("test_dwh_STG_UNION_MEMBER_write")
    op.delete_group("test_dwh_STG_UNION_MEMBER_read")
