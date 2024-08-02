"""empty message

Revision ID: 33309138795a
Revises: 0d1fae4a86d7
Create Date: 2024-08-02 09:09:56.387451

"""

from alembic import op
import sqlalchemy as sa
import os


# revision identifiers, used by Alembic.
revision = '33309138795a'
down_revision = '0d1fae4a86d7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("ODS_MYMSUAPI")
    op.create_table_schema("STG_MYMSUAPI")
    op.create_table(
        'ods_timetable_api_flattened',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group_name', sa.String(), nullable=False),
        sa.Column('discipline_name', sa.String(), nullable=False),
        sa.Column('discipline_id', sa.Integer(), nullable=False),
        sa.Column('classroom_name', sa.String(), nullable=False),
        sa.Column('classroom_id', sa.Integer(), nullable=False),
        sa.Column('lesson_type_text', sa.String(), nullable=False),
        sa.Column('lesson_from_dttm_ts', sa.DateTime(), nullable=False),
        sa.Column('lesson_to_dttm_ts', sa.DateTime(), nullable=False),
        sa.Column('teacher_full_name', sa.String(), nullable=False),
        sa.Column('study_group_id', sa.Integer(), nullable=False),
        sa.Column('study_group_name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_MYMSUAPI',
    )
    op.create_table(
        'raw_timetable_api',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group_name', sa.String(), nullable=False),
        sa.Column('discipline_name', sa.String(), nullable=False),
        sa.Column('discipline_id', sa.Integer(), nullable=False),
        sa.Column('classroom_name', sa.String(), nullable=False),
        sa.Column('classroom_id', sa.Integer(), nullable=False),
        sa.Column('lesson_type_text', sa.String(), nullable=False),
        sa.Column('lesson_from_dttm_ts', sa.TIMESTAMP(), nullable=False),
        sa.Column('lesson_to_dttm_ts', sa.TIMESTAMP(), nullable=False),
        sa.Column('teacher_users', sa.JSON(), nullable=False),
        sa.Column('study_groups', sa.JSON(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_MYMSUAPI',
    )
    op.create_group(
        "test_dwh_ods_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_read"
    )
    op.create_group(
        "test_dwh_ods_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_write"
    )
    op.create_group(
        "test_dwh_ods_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_all"
    )
    op.create_group(
        "test_dwh_stg_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_read"
    )
    op.create_group(
        "test_dwh_stg_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_write"
    )
    op.create_group(
        "test_dwh_stg_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_all"
    )
    op.grant_on_schema(
        "test_dwh_ods_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_read",
        "ODS_MYMSUAPI",
    )
    op.grant_on_schema(
        "test_dwh_ods_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_write",
        "ODS_MYMSUAPI",
    )
    op.grant_on_schema(
        "test_dwh_ods_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_all",
        "ODS_MYMSUAPI",
    )
    op.grant_on_schema(
        "test_dwh_stg_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_read",
        "STG_MYMSUAPI",
    )
    op.grant_on_schema(
        "test_dwh_stg_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_write",
        "STG_MYMSUAPI",
    )
    op.grant_on_schema(
        "test_dwh_stg_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_all",
        "STG_MYMSUAPI",
    )
    op.grant_on_table(
        "test_dwh_ods_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_read",
        ['SELECT'],
        '"ODS_MYMSUAPI".ods_timetable_api_flattened',
    )
    op.grant_on_table(
        "test_dwh_ods_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_MYMSUAPI".ods_timetable_api_flattened',
    )
    op.grant_on_table(
        "test_dwh_ods_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_all",
        ['ALL'],
        '"ODS_MYMSUAPI".ods_timetable_api_flattened',
    )
    op.grant_on_table(
        "test_dwh_stg_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_read",
        ['SELECT'],
        '"STG_MYMSUAPI".raw_timetable_api',
    )
    op.grant_on_table(
        "test_dwh_stg_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_MYMSUAPI".raw_timetable_api',
    )
    op.grant_on_table(
        "test_dwh_stg_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_all",
        ['ALL'],
        '"STG_MYMSUAPI".raw_timetable_api',
    )
    op.grant_on_table(
        "test_dwh_ods_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_read",
        ['SELECT'],
        '"ODS_MYMSUAPI".ods_timetable_api_flattened',
    )
    op.grant_on_table(
        "test_dwh_ods_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_MYMSUAPI".ods_timetable_api_flattened',
    )
    op.grant_on_table(
        "test_dwh_ods_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_all",
        ['ALL'],
        '"ODS_MYMSUAPI".ods_timetable_api_flattened',
    )
    op.grant_on_table(
        "test_dwh_stg_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_read",
        ['SELECT'],
        '"STG_MYMSUAPI".raw_timetable_api',
    )
    op.grant_on_table(
        "test_dwh_stg_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_MYMSUAPI".raw_timetable_api',
    )
    op.grant_on_table(
        "test_dwh_stg_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_all",
        ['ALL'],
        '"STG_MYMSUAPI".raw_timetable_api',
    )
    op.add_column('dim_event_act', sa.Column('source_name', sa.String(), nullable=True), schema='DM_TIMETABLE')
    op.add_column('dim_group_act', sa.Column('source_name', sa.String(), nullable=True), schema='DM_TIMETABLE')
    op.add_column('dim_lecturer_act', sa.Column('source_name', sa.String(), nullable=True), schema='DM_TIMETABLE')
    op.add_column('dim_room_act', sa.Column('room_api_id', sa.Integer(), nullable=False), schema='DM_TIMETABLE')
    op.add_column('dim_room_act', sa.Column('room_name', sa.String(), nullable=True), schema='DM_TIMETABLE')
    op.add_column('dim_room_act', sa.Column('room_is_deleted', sa.Boolean(), nullable=False), schema='DM_TIMETABLE')
    op.add_column('dim_room_act', sa.Column('room_department', sa.String(), nullable=True), schema='DM_TIMETABLE')
    op.add_column('dim_room_act', sa.Column('source_name', sa.String(), nullable=True), schema='DM_TIMETABLE')

def downgrade():
    op.add_column(
        'dim_room_act', sa.Column('api_id', sa.INTEGER(), autoincrement=False, nullable=False), schema='DM_TIMETABLE'
    )
    op.add_column(
        'dim_room_act', sa.Column('department', sa.VARCHAR(), autoincrement=False, nullable=True), schema='DM_TIMETABLE'
    )
    op.add_column(
        'dim_room_act',
        sa.Column('is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=False),
        schema='DM_TIMETABLE',
    )
    op.add_column(
        'dim_room_act', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True), schema='DM_TIMETABLE'
    )
    op.drop_column('dim_room_act', 'source_name', schema='DM_TIMETABLE')
    op.drop_column('dim_room_act', 'room_department', schema='DM_TIMETABLE')
    op.drop_column('dim_room_act', 'room_is_deleted', schema='DM_TIMETABLE')
    op.drop_column('dim_room_act', 'room_name', schema='DM_TIMETABLE')
    op.drop_column('dim_room_act', 'room_api_id', schema='DM_TIMETABLE')
    op.drop_column('dim_lecturer_act', 'source_name', schema='DM_TIMETABLE')
    op.drop_column('dim_group_act', 'source_name', schema='DM_TIMETABLE')
    op.drop_column('dim_event_act', 'source_name', schema='DM_TIMETABLE')
    op.revoke_on_table(
        "test_dwh_stg_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_all",
        ['ALL'],
        '"STG_MYMSUAPI".raw_timetable_api',
    )
    op.revoke_on_table(
        "test_dwh_stg_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_MYMSUAPI".raw_timetable_api',
    )
    op.revoke_on_table(
        "test_dwh_stg_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_read",
        ['SELECT'],
        '"STG_MYMSUAPI".raw_timetable_api',
    )
    op.revoke_on_table(
        "test_dwh_ods_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_all",
        ['ALL'],
        '"ODS_MYMSUAPI".ods_timetable_api_flattened',
    )
    op.revoke_on_table(
        "test_dwh_ods_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_MYMSUAPI".ods_timetable_api_flattened',
    )
    op.revoke_on_table(
        "test_dwh_ods_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_read",
        ['SELECT'],
        '"ODS_MYMSUAPI".ods_timetable_api_flattened',
    )
    op.revoke_on_table(
        "test_dwh_stg_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_all",
        ['ALL'],
        '"STG_MYMSUAPI".raw_timetable_api',
    )
    op.revoke_on_table(
        "test_dwh_stg_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_MYMSUAPI".raw_timetable_api',
    )
    op.revoke_on_table(
        "test_dwh_stg_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_read",
        ['SELECT'],
        '"STG_MYMSUAPI".raw_timetable_api',
    )
    op.revoke_on_table(
        "test_dwh_ods_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_all",
        ['ALL'],
        '"ODS_MYMSUAPI".ods_timetable_api_flattened',
    )
    op.revoke_on_table(
        "test_dwh_ods_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_MYMSUAPI".ods_timetable_api_flattened',
    )
    op.revoke_on_table(
        "test_dwh_ods_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_read",
        ['SELECT'],
        '"ODS_MYMSUAPI".ods_timetable_api_flattened',
    )
    op.revoke_on_schema(
        "test_dwh_stg_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_all",
        "STG_MYMSUAPI",
    )
    op.revoke_on_schema(
        "test_dwh_stg_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_write",
        "STG_MYMSUAPI",
    )
    op.revoke_on_schema(
        "test_dwh_stg_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_read",
        "STG_MYMSUAPI",
    )
    op.revoke_on_schema(
        "test_dwh_ods_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_all",
        "ODS_MYMSUAPI",
    )
    op.revoke_on_schema(
        "test_dwh_ods_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_write",
        "ODS_MYMSUAPI",
    )
    op.revoke_on_schema(
        "test_dwh_ods_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_read",
        "ODS_MYMSUAPI",
    )
    op.drop_table('raw_timetable_api', schema='STG_MYMSUAPI')
    op.drop_table('ods_timetable_api_flattened', schema='ODS_MYMSUAPI')
    op.delete_group(
        "test_dwh_stg_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_all"
    )
    op.delete_group(
        "test_dwh_stg_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_write"
    )
    op.delete_group(
        "test_dwh_stg_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_mymsuapi_read"
    )
    op.delete_group(
        "test_dwh_ods_mymsuapi_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_all"
    )
    op.delete_group(
        "test_dwh_ods_mymsuapi_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_write"
    )
    op.delete_group(
        "test_dwh_ods_mymsuapi_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_mymsuapi_read"
    )
    op.drop_table_schema("STG_MYMSUAPI")
    op.drop_table_schema("ODS_MYMSUAPI")
