"""rights

Revision ID: 9b3f53bed971
Revises: 0a24041f09d1
Create Date: 2023-08-24 20:49:19.841621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b3f53bed971'
down_revision = '0a24041f09d1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_group("dwh_stg_union_member_read")
    op.create_group("dwh_stg_union_member_write")
    op.create_group("dwh_stg_union_member_all")
    op.grant_rights("dwh_stg_union_member_read", '"STG_UNION_MEMBER".union_member')
    op.grant_rights("dwh_stg_union_member_write", '"STG_UNION_MEMBER".union_member')
    op.grant_rights("dwh_stg_union_member_all", '"STG_UNION_MEMBER".union_member')


def downgrade():
    op.revoke_rights("dwh_stg_union_member_all", "STG_UNION_MEMBER.union_member")
    op.revoke_rights("dwh_stg_union_member_write", "STG_UNION_MEMBER.union_member")
    op.revoke_rights("dwh_stg_union_member_read", "STG_UNION_MEMBER.union_member")
    op.delete_group("dwh_stg_union_member_all")
    op.delete_group("dwh_stg_union_member_write")
    op.delete_group("dwh_stg_union_member_read")
