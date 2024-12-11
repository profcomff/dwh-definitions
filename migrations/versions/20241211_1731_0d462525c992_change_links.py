"""change_links

Revision ID: 0d462525c992
Revises: f31bd2cf406f
Create Date: 2024-12-11 17:31:28.920934

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '0d462525c992'
down_revision = 'f31bd2cf406f'
branch_labels = None
depends_on = None


def upgrade():
    # alembic cannot do it properly, so you need to manually handle columns
    # ods_link_timetable_lesson
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_group drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_group add COLUMN IF not EXISTS id UUID')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_group drop COLUMN IF EXISTS group_id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_group add COLUMN IF not EXISTS group_id UUID')
    # ods_link_timetable_group
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_lesson drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_lesson add COLUMN IF not EXISTS id UUID')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_lesson drop COLUMN IF EXISTS lesson_id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_lesson add COLUMN IF not EXISTS lesson_id UUID')
    # ods_link_timetable_teacher
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_teacher drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_teacher add COLUMN IF not EXISTS id UUID')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_teacher drop COLUMN IF EXISTS teacher_id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_teacher add COLUMN IF not EXISTS teacher_id UUID')
    # ods_timetable_act
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_timetable_act drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_timetable_act add COLUMN IF not EXISTS id UUID')
    op.create_table(
        'ods_link_timetable_room',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column(
            'timetable_alias',
            sa.String(),
            nullable=True,
            comment='Техническое поле для построения пайплайна сборки расписания',
        ),
        sa.Column(
            'event_id',
            sa.UUID(),
            nullable=True,
            comment='Идентификатор события, полученного в результате парсинга ras.phys.msu',
        ),
        sa.Column('room_id', sa.UUID(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_TIMETABLE',
    )
    op.create_table(
        'ods_manual_timetable_constraints',
        sa.Column(
            'event_id',
            sa.UUID(),
            nullable=False,
            comment='Идентификатор события, полученного в результате парсинга ras.phys.msu',
        ),
        sa.Column('empty_room_flg', sa.UUID(), nullable=True, comment='Флаг: в событии не указан кабинет'),
        sa.Column('empty_lecturer_flg', sa.UUID(), nullable=True, comment='Флаг: в событии не указан преподаватель'),
        sa.Column('empty_group_flg', sa.UUID(), nullable=True, comment='Флаг: в событии не указан премет'),
        sa.PrimaryKeyConstraint('event_id'),
        schema='ODS_TIMETABLE',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_link_timetable_room',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_link_timetable_room',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_link_timetable_room',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_manual_timetable_constraints',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_manual_timetable_constraints',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_manual_timetable_constraints',
    )
    op.drop_index(
        'ix_ODS_TIMETABLE_ods_link_timetable_cabinet_id',
        table_name='ods_link_timetable_cabinet',
        schema='ODS_TIMETABLE',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_link_timetable_cabinet',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_link_timetable_cabinet',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_link_timetable_cabinet',
    )
    op.add_column(
        'ods_link_timetable_group',
        sa.Column(
            'timetable_alias',
            sa.String(),
            nullable=True,
            comment='Техническое поле для построения пайплайна сборки расписания',
        ),
        schema='ODS_TIMETABLE',
    )
    op.add_column(
        'ods_link_timetable_group',
        sa.Column(
            'event_id',
            sa.UUID(),
            nullable=True,
            comment='Идентификатор события, полученного в результате парсинга ras.phys.msu',
        ),
        schema='ODS_TIMETABLE',
    )
    op.alter_column(
        'ods_link_timetable_group',
        'id',
        existing_type=sa.INTEGER(),
        type_=sa.UUID(),
        nullable=False,
        schema='ODS_TIMETABLE',
    )
    op.alter_column(
        'ods_link_timetable_group',
        'group_id',
        existing_type=sa.INTEGER(),
        type_=sa.UUID(),
        existing_nullable=True,
        schema='ODS_TIMETABLE',
    )
    op.add_column(
        'ods_link_timetable_lesson',
        sa.Column(
            'timetable_alias',
            sa.String(),
            nullable=False,
            comment='Техническое поле для построения пайплайна сборки расписания',
        ),
        schema='ODS_TIMETABLE',
    )
    op.add_column(
        'ods_link_timetable_lesson',
        sa.Column(
            'event_id',
            sa.UUID(),
            nullable=True,
            comment='Идентификатор события, полученного в результате парсинга ras.phys.msu',
        ),
        schema='ODS_TIMETABLE',
    )
    op.alter_column(
        'ods_link_timetable_lesson',
        'id',
        existing_type=sa.INTEGER(),
        type_=sa.UUID(),
        nullable=False,
        schema='ODS_TIMETABLE',
    )
    op.alter_column(
        'ods_link_timetable_lesson',
        'lesson_id',
        existing_type=sa.INTEGER(),
        type_=sa.UUID(),
        existing_nullable=True,
        schema='ODS_TIMETABLE',
    )
    op.drop_column('ods_link_timetable_lesson', 'group', schema='ODS_TIMETABLE')
    op.drop_column('ods_link_timetable_lesson', 'event_tr', schema='ODS_TIMETABLE')
    op.add_column(
        'ods_link_timetable_teacher',
        sa.Column(
            'timetable_alias',
            sa.String(),
            nullable=False,
            comment='Техническое поле для построения пайплайна сборки расписания',
        ),
        schema='ODS_TIMETABLE',
    )
    op.add_column(
        'ods_link_timetable_teacher',
        sa.Column(
            'event_id',
            sa.UUID(),
            nullable=True,
            comment='Идентификатор события, полученного в результате парсинга ras.phys.msu',
        ),
        schema='ODS_TIMETABLE',
    )
    op.alter_column(
        'ods_link_timetable_teacher',
        'id',
        existing_type=sa.INTEGER(),
        type_=sa.UUID(),
        nullable=False,
        schema='ODS_TIMETABLE',
    )
    op.alter_column(
        'ods_link_timetable_teacher',
        'teacher_id',
        existing_type=sa.INTEGER(),
        type_=sa.UUID(),
        existing_nullable=True,
        schema='ODS_TIMETABLE',
    )
    op.alter_column(
        'ods_timetable_act', 'id', existing_type=sa.INTEGER(), type_=sa.UUID(), nullable=False, schema='ODS_TIMETABLE'
    )
    op.drop_table('ods_link_timetable_cabinet', schema='ODS_TIMETABLE')


def downgrade():
    # alembic cannot do it properly, so you need to manually handle columns
    # ods_link_timetable_lesson
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_group drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_group add COLUMN IF not EXISTS id INTEGER')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_group drop COLUMN IF EXISTS group_id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_group add COLUMN IF not EXISTS group_id INTEGER')
    # ods_link_timetable_group
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_lesson drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_lesson add COLUMN IF not EXISTS id INTEGER')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_lesson drop COLUMN IF EXISTS lesson_id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_lesson add COLUMN IF not EXISTS lesson_id INTEGER')
    # ods_link_timetable_teacher
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_teacher drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_teacher add COLUMN IF not EXISTS id INTEGER')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_teacher drop COLUMN IF EXISTS teacher_id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_link_timetable_teacher add COLUMN IF not EXISTS teacher_id INTEGER')
    # ods_timetable_act
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_timetable_act drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "ODS_TIMETABLE".ods_timetable_act add COLUMN IF not EXISTS id INTEGER')
    op.create_table(
        'ods_link_timetable_cabinet',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('group', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('event_tr', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column('cabinet_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name='ods_link_timetable_cabinet_pkey'),
        schema='ODS_TIMETABLE',
    )
    op.create_index(
        'ix_ODS_TIMETABLE_ods_timetable_act_id', 'ods_timetable_act', ['id'], unique=False, schema='ODS_TIMETABLE'
    )
    op.alter_column(
        'ods_timetable_act', 'id', existing_type=sa.UUID(), type_=sa.INTEGER(), nullable=True, schema='ODS_TIMETABLE'
    )
    op.create_index(
        'ix_ODS_TIMETABLE_ods_link_timetable_teacher_id',
        'ods_link_timetable_teacher',
        ['id'],
        unique=False,
        schema='ODS_TIMETABLE',
    )
    op.alter_column(
        'ods_link_timetable_teacher',
        'teacher_id',
        existing_type=sa.UUID(),
        type_=sa.INTEGER(),
        existing_nullable=True,
        schema='ODS_TIMETABLE',
    )
    op.alter_column(
        'ods_link_timetable_teacher',
        'id',
        existing_type=sa.UUID(),
        type_=sa.INTEGER(),
        nullable=True,
        schema='ODS_TIMETABLE',
    )
    op.drop_column('ods_link_timetable_teacher', 'event_id', schema='ODS_TIMETABLE')
    op.drop_column('ods_link_timetable_teacher', 'timetable_alias', schema='ODS_TIMETABLE')
    op.add_column(
        'ods_link_timetable_lesson',
        sa.Column('event_tr', sa.VARCHAR(), autoincrement=False, nullable=True),
        schema='ODS_TIMETABLE',
    )
    op.add_column(
        'ods_link_timetable_lesson',
        sa.Column('group', sa.VARCHAR(), autoincrement=False, nullable=True),
        schema='ODS_TIMETABLE',
    )
    op.create_index(
        'ix_ODS_TIMETABLE_ods_link_timetable_lesson_id',
        'ods_link_timetable_lesson',
        ['id'],
        unique=False,
        schema='ODS_TIMETABLE',
    )
    op.alter_column(
        'ods_link_timetable_lesson',
        'lesson_id',
        existing_type=sa.UUID(),
        type_=sa.INTEGER(),
        existing_nullable=True,
        schema='ODS_TIMETABLE',
    )
    op.alter_column(
        'ods_link_timetable_lesson',
        'id',
        existing_type=sa.UUID(),
        type_=sa.INTEGER(),
        nullable=True,
        schema='ODS_TIMETABLE',
    )
    op.drop_column('ods_link_timetable_lesson', 'event_id', schema='ODS_TIMETABLE')
    op.drop_column('ods_link_timetable_lesson', 'timetable_alias', schema='ODS_TIMETABLE')
    op.create_index(
        'ix_ODS_TIMETABLE_ods_link_timetable_group_id',
        'ods_link_timetable_group',
        ['id'],
        unique=False,
        schema='ODS_TIMETABLE',
    )
    op.alter_column(
        'ods_link_timetable_group',
        'group_id',
        existing_type=sa.UUID(),
        type_=sa.INTEGER(),
        existing_nullable=True,
        schema='ODS_TIMETABLE',
    )
    op.alter_column(
        'ods_link_timetable_group',
        'id',
        existing_type=sa.UUID(),
        type_=sa.INTEGER(),
        nullable=True,
        schema='ODS_TIMETABLE',
    )
    op.drop_column('ods_link_timetable_group', 'event_id', schema='ODS_TIMETABLE')
    op.drop_column('ods_link_timetable_group', 'timetable_alias', schema='ODS_TIMETABLE')
    op.grant_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_link_timetable_cabinet',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_link_timetable_cabinet',
    )
    op.grant_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_link_timetable_cabinet',
    )
    op.create_index(
        'ix_ODS_TIMETABLE_ods_link_timetable_cabinet_id',
        'ods_link_timetable_cabinet',
        ['id'],
        unique=False,
        schema='ODS_TIMETABLE',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_manual_timetable_constraints',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_manual_timetable_constraints',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_manual_timetable_constraints',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_all",
        ['ALL'],
        '"ODS_TIMETABLE".ods_link_timetable_room',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_TIMETABLE".ods_link_timetable_room',
    )
    op.revoke_on_table(
        "test_dwh_ods_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_timetable_read",
        ['SELECT'],
        '"ODS_TIMETABLE".ods_link_timetable_room',
    )
    op.drop_table('ods_manual_timetable_constraints', schema='ODS_TIMETABLE')
    op.drop_table('ods_link_timetable_room', schema='ODS_TIMETABLE')
