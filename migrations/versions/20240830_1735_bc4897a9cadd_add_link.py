"""add_link

Revision ID: bc4897a9cadd
Revises: f533a027d14a
Create Date: 2024-08-30 17:35:21.209445

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'bc4897a9cadd'
down_revision = 'f533a027d14a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'link_new_with_dates',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('subject', sa.String(), nullable=True),
        sa.Column('start', sa.String(), nullable=False),
        sa.Column('end', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
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


def downgrade():
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
    op.drop_table('link_new_with_dates', schema='STG_RASPHYSMSU')
