"""add_ods_timetable

Revision ID: 09416a9fa7cc
Revises: 91cf4b4d68eb
Create Date: 2024-11-30 17:42:06.544423

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '09416a9fa7cc'
down_revision = '91cf4b4d68eb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'ods_timetable_act',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False, comment='Название события'),
        sa.Column('odd', sa.Boolean(), nullable=False, comment='Флаг: событие относится к нечетной неделе'),
        sa.Column('even', sa.Boolean(), nullable=False, comment='Флаг: событие относится к четной неделе'),
        sa.Column('weekday', sa.Integer(), nullable=False, comment='Номер недели'),
        sa.Column('num', sa.Integer(), nullable=False, comment='Номер события'),
        sa.Column('start', sa.String(), nullable=False, comment='Время начала события (в строке)'),
        sa.Column('end', sa.String(), nullable=False, comment='Время конца события (в строке)'),
        sa.Column('group', sa.String(), nullable=False, comment='Академическая группа, к которой относится событие'),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_TIMETABLE',
        comment='\n    Таблица содержит десериализованные события с сайта ras.phys.msu\n    Выделяется блок текста из общей таблицы, нужна для обновления расписания в приложении ТвойФФ\n    ',
    )
    op.create_index(
        op.f('ix_ODS_TIMETABLE_ods_timetable_act_id'), 'ods_timetable_act', ['id'], unique=False, schema='ODS_TIMETABLE'
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


def downgrade():
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
    op.drop_index(op.f('ix_ODS_TIMETABLE_ods_timetable_act_id'), table_name='ods_timetable_act', schema='ODS_TIMETABLE')
    op.drop_table('ods_timetable_act', schema='ODS_TIMETABLE')
