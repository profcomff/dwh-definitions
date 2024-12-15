"""uids_to_dims

Revision ID: f62898bb3315
Revises: 0d462525c992
Create Date: 2024-12-12 15:43:14.642986

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = 'f62898bb3315'
down_revision = '0d462525c992'
branch_labels = None
depends_on = None


def upgrade():
    # alembic cannot do it properly, so you need to manually handle columns
    # dim_event_act
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_event_act drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_event_act add COLUMN IF not EXISTS id UUID')
    # dim_group_act
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_group_act drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_group_act add COLUMN IF not EXISTS id UUID')
    # dim_lecturer_act
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_lecturer_act drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_lecturer_act add COLUMN IF not EXISTS id UUID')
    # dim_room_act
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_room_act drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_room_act add COLUMN IF not EXISTS id UUID')


def downgrade():
    # alembic cannot do it properly, so you need to manually handle columns
    # dim_event_act
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_event_act drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_event_act add COLUMN IF not EXISTS id INTEGER')
    # dim_group_act
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_group_act drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_group_act add COLUMN IF not EXISTS id INTEGER')
    # dim_lecturer_act
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_lecturer_act drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_lecturer_act add COLUMN IF not EXISTS id INTEGER')
    # dim_room_act
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_room_act drop COLUMN IF EXISTS id')
    op.execute('ALTER TABLE "DM_TIMETABLE".dim_room_act add COLUMN IF not EXISTS id INTEGER')
