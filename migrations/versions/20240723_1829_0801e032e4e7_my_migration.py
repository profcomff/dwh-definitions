"""my migration

Revision ID: 0801e032e4e7
Revises: 0d1fae4a86d7
Create Date: 2024-07-23 18:29:37.398287

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '0801e032e4e7'
down_revision = '0d1fae4a86d7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("ODS_INFO")
    op.create_table_schema("ODS_TIMETABLE")
    op.create_table(
        'info',
        sa.Column('user_id', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('phone_number', sa.String(), nullable=True),
        sa.Column('vk_name', sa.String(), nullable=True),
        sa.Column('city', sa.String(), nullable=True),
        sa.Column('hometown', sa.String(), nullable=True),
        sa.Column('location', sa.String(), nullable=True),
        sa.Column('github_name', sa.String(), nullable=True),
        sa.Column('telegram_name', sa.String(), nullable=True),
        sa.Column('home_phone_number', sa.String(), nullable=True),
        sa.Column('education_level', sa.String(), nullable=True),
        sa.Column('university', sa.String(), nullable=True),
        sa.Column('group', sa.String(), nullable=True),
        sa.Column('faculty', sa.String(), nullable=True),
        sa.Column('position', sa.String(), nullable=True),
        sa.Column('student_id_number', sa.String(), nullable=True),
        sa.Column('department', sa.String(), nullable=True),
        sa.Column('mode_of_study', sa.String(), nullable=True),
        sa.Column('full_name', sa.String(), nullable=True),
        sa.Column('birth_date', sa.String(), nullable=True),
        sa.Column('photo', sa.String(), nullable=True),
        sa.Column('sex', sa.String(), nullable=True),
        sa.Column('job', sa.String(), nullable=True),
        sa.Column('work_location', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('user_id'),
        schema='ODS_INFO',
    )
    op.create_table(
        'ods_timetable_act',
        sa.Column('event_text', sa.String(), nullable=True),
        sa.Column('time_interval_text', sa.String(), nullable=True),
        sa.Column('group_text', sa.String(), nullable=True),
        schema='ODS_TIMETABLE',
    )
    op.create_group("test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read")
    op.create_group(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write"
    )
    op.create_group("test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all")
    op.create_group(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read"
    )
    op.create_group(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write"
    )
    op.create_group(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all"
    )
    op.grant_on_schema(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read", "ODS_INFO"
    )
    op.grant_on_schema(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write", "ODS_INFO"
    )
    op.grant_on_schema(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all", "ODS_INFO"
    )
    op.grant_on_schema(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        "ODS_TIMETABLE",
    )
    op.grant_on_schema(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        "ODS_TIMETABLE",
    )
    op.grant_on_schema(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        "ODS_TIMETABLE",
    )
    op.grant_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info',
    )
    op.grant_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info',
    )
    op.grant_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.create_index(op.f('ix_ODS_INFO_info_user_id'), 'info', ['user_id'], unique=False, schema='ODS_INFO')
    op.grant_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info',
    )
    op.grant_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info',
    )
    op.grant_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info',
    )
    op.create_index(
        op.f('ix_ODS_TIMETABLE_ods_timetable_act_event_text'),
        'ods_timetable_act',
        ['event_text'],
        unique=False,
        schema='ODS_TIMETABLE',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.add_column('dim_room_act', sa.Column('room_api_id', sa.Integer(), nullable=False), schema='DM_TIMETABLE')
    op.add_column('dim_room_act', sa.Column('room_name', sa.String(), nullable=True), schema='DM_TIMETABLE')
    op.add_column('dim_room_act', sa.Column('room_is_deleted', sa.Boolean(), nullable=False), schema='DM_TIMETABLE')
    op.add_column('dim_room_act', sa.Column('room_department', sa.String(), nullable=True), schema='DM_TIMETABLE')
    op.drop_column('dim_room_act', 'is_deleted', schema='DM_TIMETABLE')
    op.drop_column('dim_room_act', 'api_id', schema='DM_TIMETABLE')
    op.drop_column('dim_room_act', 'name', schema='DM_TIMETABLE')
    op.drop_column('dim_room_act', 'department', schema='DM_TIMETABLE')
    # ### end Alembic commands ###


def downgrade():
    op.add_column(
        'dim_room_act', sa.Column('department', sa.VARCHAR(), autoincrement=False, nullable=True), schema='DM_TIMETABLE'
    )
    op.add_column(
        'dim_room_act', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True), schema='DM_TIMETABLE'
    )
    op.add_column(
        'dim_room_act', sa.Column('api_id', sa.INTEGER(), autoincrement=False, nullable=False), schema='DM_TIMETABLE'
    )
    op.add_column(
        'dim_room_act',
        sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=False),
        schema='DM_TIMETABLE',
    )
    op.drop_column('dim_room_act', 'room_department', schema='DM_TIMETABLE')
    op.drop_column('dim_room_act', 'room_is_deleted', schema='DM_TIMETABLE')
    op.drop_column('dim_room_act', 'room_name', schema='DM_TIMETABLE')
    op.drop_column('dim_room_act', 'room_api_id', schema='DM_TIMETABLE')
    op.revoke_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.drop_index(
        op.f('ix_ODS_TIMETABLE_ods_timetable_act_event_text'), table_name='ods_timetable_act', schema='ODS_TIMETABLE'
    )
    op.revoke_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info',
    )
    op.drop_index(op.f('ix_ODS_INFO_info_user_id'), table_name='info', schema='ODS_INFO')
    op.revoke_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info',
    )
    op.revoke_on_schema(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        "ODS_TIMETABLE",
    )
    op.revoke_on_schema(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        "ODS_TIMETABLE",
    )
    op.revoke_on_schema(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        "ODS_TIMETABLE",
    )
    op.revoke_on_schema(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all", "ODS_INFO"
    )
    op.revoke_on_schema(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write", "ODS_INFO"
    )
    op.revoke_on_schema(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read", "ODS_INFO"
    )
    op.drop_table('ods_timetable_act', schema='ODS_TIMETABLE')
    op.drop_table('info', schema='ODS_INFO')
    op.delete_group(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all"
    )
    op.delete_group(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write"
    )
    op.delete_group(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read"
    )
    op.delete_group("test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all")
    op.delete_group(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write"
    )
    op.delete_group("test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read")
    op.drop_table_schema("ODS_TIMETABLE")
    op.drop_table_schema("ODS_INFO")
    # ### end Alembic commands ###
