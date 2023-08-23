"""test

Revision ID: a2a4142c633b
Revises: fa8c104793ca
Create Date: 2023-08-23 22:03:57.310826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2a4142c633b'
down_revision = 'fa8c104793ca'
branch_labels = None
depends_on = None


def upgrade():
    op.revoke_rights("dwh_STG_UNION_MEMBER_read", "STG_UNION_MEMBER.new_test")
    op.revoke_rights("dwh_STG_UNION_MEMBER_write", "STG_UNION_MEMBER.new_test")
    op.revoke_rights("dwh_STG_UNION_MEMBER_all", "STG_UNION_MEMBER.new_test")
    op.drop_table('new_test', schema='STG_UNION_MEMBER')


def downgrade():
    op.create_table(
        'new_test',
        sa.Column(
            'id',
            sa.INTEGER(),
            server_default=sa.text('nextval(\'"STG_UNION_MEMBER".new_test_id_seq\'::regclass)'),
            autoincrement=True,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint('id', name='new_test_pkey'),
        schema='STG_UNION_MEMBER',
    )
    op.grant_rights("dwh_STG_UNION_MEMBER_read", "STG_UNION_MEMBER.new_test")
    op.grant_rights("dwh_STG_UNION_MEMBER_write", "STG_UNION_MEMBER.new_test")
    op.grant_rights("dwh_STG_UNION_MEMBER_all", "STG_UNION_MEMBER.new_test")
