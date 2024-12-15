"""dm_timetable

Revision ID: d079efc107f5
Revises: f62898bb3315
Create Date: 2024-12-14 13:41:34.642251

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'd079efc107f5'
down_revision = 'f62898bb3315'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'dm_timetable_act',
        sa.Column(
            'event_id',
            sa.UUID(),
            nullable=False,
            comment='Идентификатор события, из таблицы ODS_TIMETABLE.ods_timetable_act',
        ),
        sa.Column('name', sa.String(), nullable=False, comment='Название события'),
        sa.Column('odd', sa.Boolean(), nullable=False, comment='Флаг: событие относится к нечетной неделе'),
        sa.Column('even', sa.Boolean(), nullable=False, comment='Флаг: событие относится к четной неделе'),
        sa.Column('weekday', sa.Integer(), nullable=False, comment='Номер недели'),
        sa.Column('num', sa.Integer(), nullable=False, comment='Номер события'),
        sa.Column('start', sa.String(), nullable=False, comment='Время начала события (в строке)'),
        sa.Column('end', sa.String(), nullable=False, comment='Время конца события (в строке)'),
        sa.Column('group', sa.String(), nullable=False, comment='Академическая группа, к которой относится событие'),
        sa.Column(
            'event_name', sa.String(), nullable=True, comment='Название события из справочника. Заполняется всегда'
        ),
        sa.Column(
            'group_name',
            sa.String(),
            nullable=True,
            comment='Название группы из справочника. Заполняется если в событии есть информация о группе',
        ),
        sa.Column(
            'lecturer_name',
            sa.String(),
            nullable=True,
            comment='Имя преподавателя из справочника. Заполняется если в событии есть информация о преподавателе',
        ),
        sa.Column(
            'room_name',
            sa.String(),
            nullable=True,
            comment='Название аудитори из справочника. Заполняется если в событии есть информация об аудитории',
        ),
        sa.PrimaryKeyConstraint('event_id'),
        schema='DM_TIMETABLE',
        comment='\n    Витрина событий расписания.\n    Строится на справочниках групп, предметов, преподавателей и аудиторий.\n    Гранулярность витрины - event_id - идентична гранулярности источника ODS_TIMETABLE.ods_timetable_act\n    ',
    )
    op.add_column(
        'dim_event_act',
        sa.Column(
            'timetable_alias',
            sa.String(),
            nullable=True,
            comment='Техническое поле для построения пайплайна сборки расписания',
        ),
        schema='DM_TIMETABLE',
    )
    op.alter_column('dim_event_act', 'id', existing_type=sa.UUID(), nullable=False, schema='DM_TIMETABLE')
    op.create_table_comment(
        'dim_event_act', '\n    Справочник событий в расписании\n    ', existing_comment=None, schema='DM_TIMETABLE'
    )
    op.add_column(
        'dim_group_act',
        sa.Column(
            'timetable_alias',
            sa.String(),
            nullable=True,
            comment='Техническое поле для построения пайплайна сборки расписания',
        ),
        schema='DM_TIMETABLE',
    )
    op.alter_column('dim_group_act', 'id', existing_type=sa.UUID(), nullable=False, schema='DM_TIMETABLE')
    op.create_table_comment(
        'dim_group_act', '\n    Справочник групп\n    ', existing_comment=None, schema='DM_TIMETABLE'
    )
    op.add_column(
        'dim_lecturer_act',
        sa.Column(
            'timetable_alias',
            sa.String(),
            nullable=True,
            comment='Техническое поле для построения пайплайна сборки расписания',
        ),
        schema='DM_TIMETABLE',
    )
    op.alter_column('dim_lecturer_act', 'id', existing_type=sa.UUID(), nullable=False, schema='DM_TIMETABLE')
    op.create_table_comment(
        'dim_lecturer_act', '\n    Справочник преподавателей\n    ', existing_comment=None, schema='DM_TIMETABLE'
    )
    op.add_column(
        'dim_room_act',
        sa.Column(
            'timetable_alias',
            sa.String(),
            nullable=True,
            comment='Техническое поле для построения пайплайна сборки расписания',
        ),
        schema='DM_TIMETABLE',
    )
    op.alter_column('dim_room_act', 'id', existing_type=sa.UUID(), nullable=False, schema='DM_TIMETABLE')
    op.create_table_comment(
        'dim_room_act', '\n    Справочник аудиторий\n    ', existing_comment=None, schema='DM_TIMETABLE'
    )
    op.drop_column('ods_link_timetable_group', 'timetable_alias', schema='ODS_TIMETABLE')
    op.drop_column('ods_link_timetable_lesson', 'timetable_alias', schema='ODS_TIMETABLE')
    op.drop_column('ods_link_timetable_room', 'timetable_alias', schema='ODS_TIMETABLE')
    op.drop_column('ods_link_timetable_teacher', 'timetable_alias', schema='ODS_TIMETABLE')


def downgrade():
    op.add_column(
        'ods_link_timetable_teacher',
        sa.Column(
            'timetable_alias',
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
            comment='Техническое поле для построения пайплайна сборки расписания',
        ),
        schema='ODS_TIMETABLE',
    )
    op.add_column(
        'ods_link_timetable_room',
        sa.Column(
            'timetable_alias',
            sa.VARCHAR(),
            autoincrement=False,
            nullable=True,
            comment='Техническое поле для построения пайплайна сборки расписания',
        ),
        schema='ODS_TIMETABLE',
    )
    op.add_column(
        'ods_link_timetable_lesson',
        sa.Column(
            'timetable_alias',
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
            comment='Техническое поле для построения пайплайна сборки расписания',
        ),
        schema='ODS_TIMETABLE',
    )
    op.add_column(
        'ods_link_timetable_group',
        sa.Column(
            'timetable_alias',
            sa.VARCHAR(),
            autoincrement=False,
            nullable=True,
            comment='Техническое поле для построения пайплайна сборки расписания',
        ),
        schema='ODS_TIMETABLE',
    )
    op.drop_table_comment('dim_room_act', existing_comment='\n    Справочник аудиторий\n    ', schema='DM_TIMETABLE')
    op.alter_column('dim_room_act', 'id', existing_type=sa.UUID(), nullable=True, schema='DM_TIMETABLE')
    op.drop_column('dim_room_act', 'timetable_alias', schema='DM_TIMETABLE')
    op.drop_table_comment(
        'dim_lecturer_act', existing_comment='\n    Справочник преподавателей\n    ', schema='DM_TIMETABLE'
    )
    op.alter_column('dim_lecturer_act', 'id', existing_type=sa.UUID(), nullable=True, schema='DM_TIMETABLE')
    op.drop_column('dim_lecturer_act', 'timetable_alias', schema='DM_TIMETABLE')
    op.drop_table_comment('dim_group_act', existing_comment='\n    Справочник групп\n    ', schema='DM_TIMETABLE')
    op.alter_column('dim_group_act', 'id', existing_type=sa.UUID(), nullable=True, schema='DM_TIMETABLE')
    op.drop_column('dim_group_act', 'timetable_alias', schema='DM_TIMETABLE')
    op.drop_table_comment(
        'dim_event_act', existing_comment='\n    Справочник событий в расписании\n    ', schema='DM_TIMETABLE'
    )
    op.alter_column('dim_event_act', 'id', existing_type=sa.UUID(), nullable=True, schema='DM_TIMETABLE')
    op.drop_column('dim_event_act', 'timetable_alias', schema='DM_TIMETABLE')
    op.drop_table('dm_timetable_act', schema='DM_TIMETABLE')
