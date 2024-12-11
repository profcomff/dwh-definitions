"""fix

Revision ID: d56e230e4da9
Revises: 14b92d839a9b
Create Date: 2024-11-10 12:16:30.479609

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'd56e230e4da9'
down_revision = '14b92d839a9b'
branch_labels = None
depends_on = None


def upgrade():
    op.revoke_on_table(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read",
        ['SELECT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.revoke_on_table(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.revoke_on_table(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all",
        ['ALL'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.revoke_on_schema(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read",
        "DM_MONITORING",
    )
    op.revoke_on_schema(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write",
        "DM_MONITORING",
    )
    op.revoke_on_schema(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all",
        "DM_MONITORING",
    )
    op.drop_table('db_monitoring_snp', schema='DM_MONITORING')
    op.delete_group(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read"
    )
    op.delete_group(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write"
    )
    op.delete_group(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all"
    )
    op.drop_table_schema("DM_MONITORING")


def downgrade():
    op.create_table_schema("DM_MONITORING")
    op.create_table(
        'db_monitoring_snp',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            'table_name',
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
            comment='Table name with schema name, ex. "STG_TIMETABLE"."events_groups"',
        ),
        sa.Column(
            'table_schema',
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
            comment='Table schema, need for detalization, ex."STG_TIMETABLE"',
        ),
        sa.Column(
            'table_size_mb', sa.INTEGER(), autoincrement=False, nullable=False, comment='Table size in MB (int), ex. 8'
        ),
        sa.Column(
            'indexes_size_mb',
            sa.INTEGER(),
            autoincrement=False,
            nullable=False,
            comment='Table indexes size in MB(int), ex.5',
        ),
        sa.Column(
            'total_size_mb',
            sa.INTEGER(),
            autoincrement=False,
            nullable=False,
            comment='Table total size in MB(int), ex. 13',
        ),
        sa.Column(
            'state_dt', sa.DATE(), autoincrement=False, nullable=False, comment='Date of snapshot, ex. 2024-11-12'
        ),
        sa.PrimaryKeyConstraint('id', name='db_monitoring_snp_pkey'),
        schema='DM_MONITORING',
        comment='\n    Snapshot table that shows sizes for all tables in DWH\n    ',
    )
    op.create_group(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all"
    )
    op.create_group(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write"
    )
    op.create_group(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read"
    )
    op.grant_on_schema(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all",
        "DM_MONITORING",
    )
    op.grant_on_schema(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write",
        "DM_MONITORING",
    )
    op.grant_on_schema(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read",
        "DM_MONITORING",
    )
    op.grant_on_table(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all",
        ['ALL'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.grant_on_table(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.grant_on_table(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read",
        ['SELECT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.grant_on_table(
        "test_dwh_dm_monitoring_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_all",
        ['ALL'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.grant_on_table(
        "test_dwh_dm_monitoring_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
    op.grant_on_table(
        "test_dwh_dm_monitoring_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_monitoring_read",
        ['SELECT'],
        '"DM_MONITORING".db_monitoring_snp',
    )
