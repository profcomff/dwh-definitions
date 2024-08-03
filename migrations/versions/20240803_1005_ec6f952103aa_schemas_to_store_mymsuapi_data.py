"""schemas to store mymsuapi data

Revision ID: ec6f952103aa
Revises: 0801e032e4e7
Create Date: 2024-08-03 10:05:03.253825

"""

import os

import sqlalchemy as sa
from alembic import op


revision = 'ec6f952103aa'
down_revision = '0801e032e4e7'
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
    op.add_column('dim_event_act', sa.Column('source_name', sa.String(), nullable=False), schema='DM_TIMETABLE')
    op.add_column('dim_group_act', sa.Column('source_name', sa.String(), nullable=False), schema='DM_TIMETABLE')
    op.add_column('dim_lecturer_act', sa.Column('source_name', sa.String(), nullable=False), schema='DM_TIMETABLE')
    op.add_column('dim_room_act', sa.Column('source_name', sa.String(), nullable=False), schema='DM_TIMETABLE')


def downgrade():
    op.drop_column('dim_room_act', 'source_name', schema='DM_TIMETABLE')
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
