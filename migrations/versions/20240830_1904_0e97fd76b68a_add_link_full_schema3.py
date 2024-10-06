"""add_link_full_schema3

Revision ID: 0e97fd76b68a
Revises: 11461790578a
Create Date: 2024-08-30 19:04:02.502893

"""

from alembic import op
import sqlalchemy as sa
import os
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0e97fd76b68a'
down_revision = '11461790578a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'link_new_with_dates',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('subject', sa.String(), nullable=True),
        sa.Column('odd', sa.Boolean(), nullable=True),
        sa.Column('even', sa.Boolean(), nullable=True),
        sa.Column('weekday', sa.Integer(), nullable=True),
        sa.Column('num', sa.Integer(), nullable=True),
        sa.Column('start', sa.String(), nullable=True),
        sa.Column('end', sa.String(), nullable=True),
        sa.Column('place', sa.ARRAY(sa.Integer()), nullable=False),
        sa.Column('group', sa.ARRAY(sa.Integer()), nullable=False),
        sa.Column('teacher', sa.ARRAY(sa.Integer()), nullable=False),
        sa.Column('events_id', sa.ARRAY(sa.Integer()), nullable=True),
        schema='STG_RASPHYSMSU',
    )
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
        schema='STG_RASPHYSMSU',
    )
    op.grant_on_table(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read",
        ['SELECT'],
        '"STG_RASPHYSMSU".link_new_with_dates',
    )
    op.grant_on_table(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RASPHYSMSU".link_new_with_dates',
    )
    op.grant_on_table(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        ['ALL'],
        '"STG_RASPHYSMSU".link_new_with_dates',
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
    op.revoke_on_table(
        "test_dwh_stg_rasphysmsu_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_all",
        ['ALL'],
        '"STG_RASPHYSMSU".link_new_with_dates',
    )
    op.revoke_on_table(
        (
            "test_dwh_stg_rasphysmsu_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_stg_rasphysmsu_write"
        ),
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_RASPHYSMSU".link_new_with_dates',
    )
    op.revoke_on_table(
        "test_dwh_stg_rasphysmsu_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_rasphysmsu_read",
        ['SELECT'],
        '"STG_RASPHYSMSU".link_new_with_dates',
    )
    op.drop_table('new_with_dates', schema='STG_RASPHYSMSU')
    op.drop_table('link_new_with_dates', schema='STG_RASPHYSMSU')