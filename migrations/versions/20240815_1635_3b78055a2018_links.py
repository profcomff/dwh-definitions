"""links

Revision ID: 3b78055a2018
Revises: ec6f952103aa
Create Date: 2024-08-15 16:35:42.157636

"""

import os

import sqlalchemy as sa
from alembic import op


revision = '3b78055a2018'
down_revision = 'ec6f952103aa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'ods_link_timetable_cabinet',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group', sa.String(), nullable=True),
        sa.Column('event_tr', sa.String(), nullable=True),
        sa.Column('cabinet_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_TIMETABLE',
    )
    op.create_table(
        'ods_link_timetable_group',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group', sa.String(), nullable=True),
        sa.Column('event_tr', sa.String(), nullable=True),
        sa.Column('group_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_TIMETABLE',
    )
    op.create_table(
        'ods_link_timetable_lesson',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group', sa.String(), nullable=True),
        sa.Column('event_tr', sa.String(), nullable=True),
        sa.Column('lesson_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_TIMETABLE',
    )
    op.create_table(
        'ods_link_timetable_teacher',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('group', sa.String(), nullable=True),
        sa.Column('event_tr', sa.String(), nullable=True),
        sa.Column('teacher_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_TIMETABLE',
    )
    op.create_index(
        op.f('ix_ODS_TIMETABLE_ods_link_timetable_cabinet_id'),
        'ods_link_timetable_cabinet',
        ['id'],
        unique=False,
        schema='ODS_TIMETABLE',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_link_timetable_cabinet',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_link_timetable_cabinet',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_link_timetable_cabinet',
    )
    op.create_index(
        op.f('ix_ODS_TIMETABLE_ods_link_timetable_group_id'),
        'ods_link_timetable_group',
        ['id'],
        unique=False,
        schema='ODS_TIMETABLE',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_link_timetable_group',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_link_timetable_group',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_link_timetable_group',
    )
    op.create_index(
        op.f('ix_ODS_TIMETABLE_ods_link_timetable_lesson_id'),
        'ods_link_timetable_lesson',
        ['id'],
        unique=False,
        schema='ODS_TIMETABLE',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_link_timetable_lesson',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_link_timetable_lesson',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_link_timetable_lesson',
    )
    op.create_index(
        op.f('ix_ODS_TIMETABLE_ods_link_timetable_teacher_id'),
        'ods_link_timetable_teacher',
        ['id'],
        unique=False,
        schema='ODS_TIMETABLE',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_link_timetable_teacher',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_link_timetable_teacher',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_link_timetable_teacher',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_link_timetable_teacher',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_link_timetable_teacher',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_link_timetable_teacher',
    )
    op.drop_index(
        op.f('ix_ODS_TIMETABLE_ods_link_timetable_teacher_id'),
        table_name='ods_link_timetable_teacher',
        schema='ODS_TIMETABLE',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_link_timetable_lesson',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_link_timetable_lesson',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_link_timetable_lesson',
    )
    op.drop_index(
        op.f('ix_ODS_TIMETABLE_ods_link_timetable_lesson_id'),
        table_name='ods_link_timetable_lesson',
        schema='ODS_TIMETABLE',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_link_timetable_group',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_link_timetable_group',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_link_timetable_group',
    )
    op.drop_index(
        op.f('ix_ODS_TIMETABLE_ods_link_timetable_group_id'),
        table_name='ods_link_timetable_group',
        schema='ODS_TIMETABLE',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_link_timetable_cabinet',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_link_timetable_cabinet',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_link_timetable_cabinet',
    )
    op.drop_index(
        op.f('ix_ODS_TIMETABLE_ods_link_timetable_cabinet_id'),
        table_name='ods_link_timetable_cabinet',
        schema='ODS_TIMETABLE',
    )
    op.drop_table('ods_link_timetable_teacher', schema='ODS_TIMETABLE')
    op.drop_table('ods_link_timetable_lesson', schema='ODS_TIMETABLE')
    op.drop_table('ods_link_timetable_group', schema='ODS_TIMETABLE')
    op.drop_table('ods_link_timetable_cabinet', schema='ODS_TIMETABLE')
