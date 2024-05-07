"""add_raw_html

Revision ID: 4892e78eb989
Revises: 1e868db5c6ea
Create Date: 2024-04-22 16:24:05.795444

"""

import os

from alembic import op


revision = '4892e78eb989'
down_revision = '1e868db5c6ea'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS "STG_TIMETABLE".raw_html (url varchar(256) NULL, raw_html text NULL);
        CREATE TABLE IF NOT EXISTS "STG_TIMETABLE".raw_html_old (url varchar(256) NULL, raw_html text NULL);
        """
    )  # this table is produced in dwh-pipelines
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".raw_html',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".raw_html',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".raw_html',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".raw_html_old',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".raw_html_old',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".raw_html_old',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".raw_html_old',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".raw_html_old',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".raw_html_old',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".raw_html',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".raw_html',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".raw_html',
    )
