"""delete ODS_timetable_act

Revision ID: e39e8d93e4d9
Revises: b9023536db5b
Create Date: 2024-11-26 07:45:22.916622

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'e39e8d93e4d9'
down_revision = 'b9023536db5b'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_index(
        'ix_ODS_TIMETABLE_ods_timetable_act_event_text', table_name='ods_timetable_act', schema='ODS_TIMETABLE'
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.drop_table('ods_timetable_act', schema='ODS_TIMETABLE')


def downgrade():
    op.create_table(
        'ods_timetable_act',
        sa.Column('event_text', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('time_interval_text', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('group_text', sa.VARCHAR(), autoincrement=False, nullable=True),
        schema='ODS_TIMETABLE',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_timetable_act',
    )
    op.create_index(
        'ix_ODS_TIMETABLE_ods_timetable_act_event_text',
        'ods_timetable_act',
        ['event_text'],
        unique=False,
        schema='ODS_TIMETABLE',
    )
