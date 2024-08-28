"""add_diff_for_old_timetable

Revision ID: 009029ff68e2
Revises: c1312de67d70
Create Date: 2024-08-28 16:18:39.844668

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '009029ff68e2'
down_revision = 'c1312de67d70'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'diff',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('subject', sa.String(), nullable=False),
        sa.Column('odd', sa.Boolean(), nullable=False),
        sa.Column('even', sa.Boolean(), nullable=False),
        sa.Column('weekday', sa.Integer(), nullable=True),
        sa.Column('num', sa.Integer(), nullable=True),
        sa.Column('start', sa.String(), nullable=False),
        sa.Column('end', sa.String(), nullable=False),
        sa.Column('place', sa.ARRAY(sa.Integer()), nullable=False),
        sa.Column('group', sa.ARRAY(sa.Integer()), nullable=False),
        sa.Column('teacher', sa.ARRAY(sa.Integer()), nullable=False),
        sa.Column('events_id', sa.ARRAY(sa.Integer()), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_RASPHYSMSU',
    )
    op.grant_on_table(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read",
        ['SELECT'],
        '"STG_RASPHYSMSU".diff',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RASPHYSMSU".diff',
    )
    op.grant_on_table(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        ['ALL'],
        '"STG_RASPHYSMSU".diff',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        ['ALL'],
        '"STG_RASPHYSMSU".diff',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RASPHYSMSU".diff',
    )
    op.revoke_on_table(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read",
        ['SELECT'],
        '"STG_RASPHYSMSU".diff',
    )
    op.drop_table('diff', schema='STG_RASPHYSMSU')
