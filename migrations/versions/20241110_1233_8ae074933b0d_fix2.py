"""fix2

Revision ID: 8ae074933b0d
Revises: d56e230e4da9
Create Date: 2024-11-10 12:33:32.317036

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '8ae074933b0d'
down_revision = 'd56e230e4da9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("DM_MONITORING")
    op.create_table(
        'db_monitoring_snp',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column(
            'table_name',
            sa.String(),
            nullable=False,
            comment='Table name with schema name, ex. "STG_TIMETABLE"."events_groups"',
        ),
        sa.Column(
            'table_schema',
            sa.String(),
            nullable=False,
            comment='Table schema, need for detalization, ex."STG_TIMETABLE"',
        ),
        sa.Column('table_size_mb', sa.Integer(), nullable=False, comment='Table size in MB (int), ex. 8'),
        sa.Column('indexes_size_mb', sa.Integer(), nullable=False, comment='Table indexes size in MB(int), ex.5'),
        sa.Column('total_size_mb', sa.Integer(), nullable=False, comment='Table total size in MB(int), ex. 13'),
        sa.Column('state_dt', sa.Date(), nullable=False, comment='Date of snapshot, ex. 2024-11-12'),
        schema='DM_MONITORING',
        comment='\n    Snapshot table that shows sizes for all tables in DWH\n    ',
    )
    op.create_group(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read"
    )
    op.create_group(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write"
    )
    op.create_group(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all"
    )
    op.grant_on_schema(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read",
        "DM_MONITORING",
    )
    op.grant_on_schema(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write",
        "DM_MONITORING",
    )
    op.grant_on_schema(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all",
        "DM_MONITORING",
    )
    op.grant_on_table(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read",
        ['SELECT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.grant_on_table(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.grant_on_table(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all",
        ['ALL'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.grant_on_table(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read",
        ['SELECT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.grant_on_table(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.grant_on_table(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all",
        ['ALL'],
        '"DM_MONITORING".db_monitoring_snp',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all",
        ['ALL'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.revoke_on_table(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.revoke_on_table(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read",
        ['SELECT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.revoke_on_table(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all",
        ['ALL'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.revoke_on_table(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.revoke_on_table(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read",
        ['SELECT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.revoke_on_schema(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all",
        "DM_MONITORING",
    )
    op.revoke_on_schema(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write",
        "DM_MONITORING",
    )
    op.revoke_on_schema(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read",
        "DM_MONITORING",
    )
    op.drop_table('db_monitoring_snp', schema='DM_MONITORING')
    op.delete_group(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all"
    )
    op.delete_group(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write"
    )
    op.delete_group(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read"
    )
    op.drop_table_schema("DM_MONITORING")
    # ### end Alembic commands ###
