"""old+new_stg

Revision ID: eba63ac1dd15
Revises: 0bf7c70b7034
Create Date: 2024-08-29 19:50:21.475003

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'eba63ac1dd15'
down_revision = '0bf7c70b7034'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'new',
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
    op.create_table(
        'old',
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
        '"STG_RASPHYSMSU".new',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RASPHYSMSU".new',
    )
    op.grant_on_table(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        ['ALL'],
        '"STG_RASPHYSMSU".new',
    )
    op.grant_on_table(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read",
        ['SELECT'],
        '"STG_RASPHYSMSU".old',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RASPHYSMSU".old',
    )
    op.grant_on_table(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        ['ALL'],
        '"STG_RASPHYSMSU".old',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        ['ALL'],
        '"STG_RASPHYSMSU".old',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RASPHYSMSU".old',
    )
    op.revoke_on_table(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read",
        ['SELECT'],
        '"STG_RASPHYSMSU".old',
    )
    op.revoke_on_table(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        ['ALL'],
        '"STG_RASPHYSMSU".new',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RASPHYSMSU".new',
    )
    op.revoke_on_table(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read",
        ['SELECT'],
        '"STG_RASPHYSMSU".new',
    )
    op.drop_table('old', schema='STG_RASPHYSMSU')
    op.drop_table('new', schema='STG_RASPHYSMSU')
