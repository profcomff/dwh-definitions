"""add ids

Revision ID: f86ba4919842
Revises: d079efc107f5
Create Date: 2024-12-15 16:21:24.119917

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'f86ba4919842'
down_revision = 'd079efc107f5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'dm_timetable_act',
        sa.Column(
            'event_api_id',
            sa.Integer(),
            nullable=True,
            comment='Идентификатор события из справочника. Заполняется всегда',
        ),
        schema='DM_TIMETABLE',
    )
    op.add_column(
        'dm_timetable_act',
        sa.Column(
            'group_api_id',
            sa.Integer(),
            nullable=True,
            comment='Идентификатор группы из справочника. Заполняется если в событии есть информация о группе',
        ),
        schema='DM_TIMETABLE',
    )
    op.add_column(
        'dm_timetable_act',
        sa.Column(
            'lecturer_api_id',
            sa.Integer(),
            nullable=True,
            comment='Идентификатор преподавателя из справочника. Заполняется если в событии есть информация о преподавателе',
        ),
        schema='DM_TIMETABLE',
    )
    op.add_column(
        'dm_timetable_act',
        sa.Column(
            'room_api_id',
            sa.Integer(),
            nullable=True,
            comment='Идентификатор аудитори из справочника. Заполняется если в событии есть информация об аудитории',
        ),
        schema='DM_TIMETABLE',
    )
    op.drop_column('ods_link_timetable_group', 'event_tr', schema='ODS_TIMETABLE')
    op.drop_column('ods_link_timetable_group', 'group', schema='ODS_TIMETABLE')
    op.drop_column('ods_link_timetable_teacher', 'event_tr', schema='ODS_TIMETABLE')
    op.drop_column('ods_link_timetable_teacher', 'group', schema='ODS_TIMETABLE')


def downgrade():
    op.add_column(
        'ods_link_timetable_teacher',
        sa.Column('group', sa.VARCHAR(), autoincrement=False, nullable=True),
        schema='ODS_TIMETABLE',
    )
    op.add_column(
        'ods_link_timetable_teacher',
        sa.Column('event_tr', sa.VARCHAR(), autoincrement=False, nullable=True),
        schema='ODS_TIMETABLE',
    )
    op.add_column(
        'ods_link_timetable_group',
        sa.Column('group', sa.VARCHAR(), autoincrement=False, nullable=True),
        schema='ODS_TIMETABLE',
    )
    op.add_column(
        'ods_link_timetable_group',
        sa.Column('event_tr', sa.VARCHAR(), autoincrement=False, nullable=True),
        schema='ODS_TIMETABLE',
    )
    op.drop_column('dm_timetable_act', 'room_api_id', schema='DM_TIMETABLE')
    op.drop_column('dm_timetable_act', 'lecturer_api_id', schema='DM_TIMETABLE')
    op.drop_column('dm_timetable_act', 'group_api_id', schema='DM_TIMETABLE')
    op.drop_column('dm_timetable_act', 'event_api_id', schema='DM_TIMETABLE')
