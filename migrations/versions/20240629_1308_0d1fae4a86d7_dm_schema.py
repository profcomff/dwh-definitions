"""DM schema

Revision ID: 0d1fae4a86d7
Revises: 5714921e11a0
Create Date: 2024-06-29 13:08:38.345305

"""

import os

import sqlalchemy as sa
from alembic import op


revision = '0d1fae4a86d7'
down_revision = '5714921e11a0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'dim_event_act',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('event_name_text', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='DM_TIMETABLE',
    )
    op.create_table(
        'dim_group_act',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group_api_id', sa.Integer(), nullable=False),
        sa.Column('group_name_text', sa.String(), nullable=True),
        sa.Column('group_number', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='DM_TIMETABLE',
    )
    op.create_table(
        'dim_lecturer_act',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('lecturer_api_id', sa.Integer(), nullable=False),
        sa.Column('lecturer_first_name', sa.String(), nullable=True),
        sa.Column('lecturer_middle_name', sa.String(), nullable=True),
        sa.Column('lecturer_last_name', sa.String(), nullable=True),
        sa.Column('lecturer_avatar_id', sa.Integer(), nullable=True),
        sa.Column('lecturer_description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='DM_TIMETABLE',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dim_lecturer_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dim_lecturer_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dim_lecturer_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dim_group_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dim_group_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dim_group_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dim_event_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dim_event_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dim_event_act',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dim_event_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dim_event_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dim_event_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dim_group_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dim_group_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dim_group_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dim_lecturer_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dim_lecturer_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dim_lecturer_act',
    )
    op.drop_table('dim_lecturer_act', schema='DM_TIMETABLE')
    op.drop_table('dim_group_act', schema='DM_TIMETABLE')
    op.drop_table('dim_event_act', schema='DM_TIMETABLE')
