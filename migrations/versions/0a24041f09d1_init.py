"""init

Revision ID: 0a24041f09d1
Revises: 
Create Date: 2023-08-25 15:42:44.112719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a24041f09d1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("STG_UNION_MEMBER")
    op.create_table(
        'union_member',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('type_of_learning', sa.String(), nullable=False),
        sa.Column('rzd_status', sa.String(), nullable=False),
        sa.Column('academic_level', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('faculty', sa.String(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=False),
        sa.Column('last_name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('date_of_birth', sa.String(), nullable=False),
        sa.Column('phone_number', sa.String(), nullable=False),
        sa.Column('image', sa.String(), nullable=False),
        sa.Column('rzd_datetime', sa.String(), nullable=False),
        sa.Column('rzd_number', sa.String(), nullable=False),
        sa.Column('grade_level', sa.Integer(), nullable=False),
        sa.Column('has_student_id', sa.Boolean(), nullable=False),
        sa.Column('entry_date', sa.String(), nullable=False),
        sa.Column('status_gain_date', sa.String(), nullable=False),
        sa.Column('card_id', sa.Integer(), nullable=False),
        sa.Column('card_status', sa.String(), nullable=False),
        sa.Column('card_date', sa.String(), nullable=False),
        sa.Column('card_number', sa.String(), nullable=False),
        sa.Column('card_user', sa.String(), nullable=False),
        sa.Column('card', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_UNION_MEMBER',
    )
    op.create_group("dwh_stg_union_member_read")
    op.create_group("dwh_stg_union_member_write")
    op.create_group("dwh_stg_union_member_all")
    op.grant_rights("dwh_stg_union_member_read", "['SELECT']", '"STG_UNION_MEMBER".union_member')
    op.grant_rights(
        "dwh_stg_union_member_write", "['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE']", '"STG_UNION_MEMBER".union_member'
    )
    op.grant_rights("dwh_stg_union_member_all", "['ALL']", '"STG_UNION_MEMBER".union_member')


def downgrade():
    op.revoke_rights("dwh_stg_union_member_all", "['ALL']", '"STG_UNION_MEMBER".union_member')
    op.revoke_rights(
        "dwh_stg_union_member_write", "['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE']", '"STG_UNION_MEMBER".union_member'
    )
    op.revoke_rights("dwh_stg_union_member_read", "['SELECT']", '"STG_UNION_MEMBER".union_member')
    op.drop_table('union_member', schema='STG_UNION_MEMBER')
    op.delete_group("dwh_stg_union_member_all")
    op.delete_group("dwh_stg_union_member_write")
    op.delete_group("dwh_stg_union_member_read")
    op.drop_table_schema("STG_UNION_MEMBER")
