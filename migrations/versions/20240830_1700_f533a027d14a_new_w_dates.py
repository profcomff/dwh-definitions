"""new_w_dates

Revision ID: f533a027d14a
Revises: f9426dfd57e2
Create Date: 2024-08-30 17:00:34.182208

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'f533a027d14a'
down_revision = 'f9426dfd57e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'new_with_dates',
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
        sa.Column('events_id', sa.ARRAY(sa.Integer()), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_RASPHYSMSU',
    )
    op.grant_on_table(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read",
        ['SELECT'],
        '"STG_RASPHYSMSU".new_with_dates',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RASPHYSMSU".new_with_dates',
    )
    op.grant_on_table(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        ['ALL'],
        '"STG_RASPHYSMSU".new_with_dates',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        ['ALL'],
        '"STG_RASPHYSMSU".new_with_dates',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RASPHYSMSU".new_with_dates',
    )
    op.revoke_on_table(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read",
        ['SELECT'],
        '"STG_RASPHYSMSU".new_with_dates',
    )
    op.drop_table('new_with_dates', schema='STG_RASPHYSMSU')
