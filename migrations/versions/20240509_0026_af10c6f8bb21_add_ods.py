"""add+ods

Revision ID: af10c6f8bb21
Revises: 1100c470c547
Create Date: 2024-05-09 00:26:03.448401

"""

import os

import sqlalchemy as sa
from alembic import op


revision = 'af10c6f8bb21'
down_revision = '1100c470c547'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("ODS_TIMETABLE")
    op.create_table(
        'ods_timetable_act',
        sa.Column('event_text', sa.String(), nullable=True),
        sa.Column('time_interval_text', sa.String(), nullable=True),
        sa.Column('group_text', sa.String(), nullable=True),
        schema='ODS_TIMETABLE',
    )
    op.create_group(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_read"
    )
    op.create_group(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_write"
    )
    op.create_group(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_all"
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
    op.create_index(
        op.f('ix_ODS_TIMETABLE_ods_timetable_act_event_text'),
        'ods_timetable_act',
        ['event_text'],
        unique=False,
        schema='ODS_TIMETABLE',
    )


def downgrade():
    op.delete_group(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_all"
    )
    op.delete_group(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_write"
    )
    op.delete_group(
        "test_dwh_dm_infra_logs_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_read"
    )
    op.drop_table('ods_timetable_act', schema='ODS_TIMETABLE')
    op.drop_table_schema("ODS_TIMETABLE")
    op.drop_index(
        op.f('ix_ODS_TIMETABLE_ods_timetable_act_event_text'), table_name='ods_timetable_act', schema='ODS_TIMETABLE'
    )
