"""Docker ps table

Revision ID: 33f7db929809
Revises: 45fc3ad3a4db
Create Date: 2024-05-07 04:54:00.011194

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '33f7db929809'
down_revision = '45fc3ad3a4db'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'container_processes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('record', sa.String(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_INFRA',
    )
    op.grant_on_table(
        "test_dwh_stg_infra_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_read",
        ['SELECT'],
        '"STG_INFRA".container_processes',
    )
    op.grant_on_table(
        "test_dwh_stg_infra_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_INFRA".container_processes',
    )
    op.grant_on_table(
        "test_dwh_stg_infra_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_infra_all",
        ['ALL'],
        '"STG_INFRA".container_processes',
    )
    op.alter_column('container_log', 'container_name', new_column_name='logfile', schema='STG_INFRA')


def downgrade():
    op.drop_table('container_processes', schema='STG_INFRA')
    op.alter_column('container_log', 'logfile', new_column_name='container_name', schema='STG_INFRA')
