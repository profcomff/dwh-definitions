"""alter_timetable_dim_columns

Revision ID: c1312de67d70
Revises: 3b78055a2018
Create Date: 2024-08-18 08:18:31.806411

"""

import sqlalchemy as sa
from alembic import op


revision = 'c1312de67d70'
down_revision = '3b78055a2018'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('dim_event_act', sa.Column('event_api_id', sa.Integer(), nullable=True), schema='DM_TIMETABLE')
    op.alter_column(
        'dim_group_act',
        'group_number',
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=True,
        schema='DM_TIMETABLE',
    )
    op.drop_column('dim_room_act', 'room_is_deleted', schema='DM_TIMETABLE')


def downgrade():
    op.add_column(
        'dim_room_act',
        sa.Column('room_is_deleted', sa.BOOLEAN(), autoincrement=False, nullable=False),
        schema='DM_TIMETABLE',
    )
    # @mixx3 alembic does not support alter column string->int, so you need to specify USING
    op.execute(
        """
        alter table "DM_TIMETABLE".dim_group_act alter column group_number set data type int using (group_number::int)
        """
    )
    op.drop_column('dim_event_act', 'event_api_id', schema='DM_TIMETABLE')
