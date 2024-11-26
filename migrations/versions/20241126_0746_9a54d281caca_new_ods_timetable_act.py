"""new ODS_timetable_act

Revision ID: 9a54d281caca
Revises: e39e8d93e4d9
Create Date: 2024-11-26 07:46:58.120924

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '9a54d281caca'
down_revision = 'e39e8d93e4d9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'ods_timetable_act',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('odd', sa.Boolean(), nullable=False),
        sa.Column('even', sa.Boolean(), nullable=False),
        sa.Column('weekday', sa.Integer(), nullable=False),
        sa.Column('num', sa.Integer(), nullable=False),
        sa.Column('start', sa.String(), nullable=False),
        sa.Column('end', sa.String(), nullable=False),
        sa.Column('group', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_TIMETABLE',
        comment='\n    Сырая информация спаршенная из html страниц расписания, хранит данные о времени, дне недели и периодичности пары(каждая неделя или через неделю)\n    ',
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
    op.drop_table('ods_timetable_act', schema='ODS_TIMETABLE')
