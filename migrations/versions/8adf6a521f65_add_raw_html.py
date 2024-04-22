"""add_raw_html

Revision ID: 8adf6a521f65
Revises: 1e868db5c6ea
Create Date: 2024-04-22 15:14:34.070346

"""

from alembic import op
import sqlalchemy as sa
import os


revision = '8adf6a521f65'
down_revision = '1e868db5c6ea'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('raw_html', 'url', existing_type=sa.VARCHAR(length=256), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('raw_html', 'raw_html', existing_type=sa.TEXT(), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('raw_html_old', 'url', existing_type=sa.VARCHAR(length=256), nullable=False, schema='STG_TIMETABLE')
    op.alter_column('raw_html_old', 'raw_html', existing_type=sa.TEXT(), nullable=False, schema='STG_TIMETABLE')
    op.grant_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
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
        '"STG_TIMETABLE".raw_html',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".raw_html_old',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".raw_html',
    )
    op.grant_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".raw_html_old',
    )


def downgrade():
    op.alter_column('raw_html_old', 'raw_html', existing_type=sa.TEXT(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('raw_html_old', 'url', existing_type=sa.VARCHAR(length=256), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('raw_html', 'raw_html', existing_type=sa.TEXT(), nullable=True, schema='STG_TIMETABLE')
    op.alter_column('raw_html', 'url', existing_type=sa.VARCHAR(length=256), nullable=True, schema='STG_TIMETABLE')
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".raw_html',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_all",
        ['ALL'],
        '"STG_TIMETABLE".raw_html_old',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".raw_html',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"STG_TIMETABLE".raw_html_old',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".raw_html',
    )
    op.revoke_on_table(
        "test_dwh_stg_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_stg_timetable_read",
        ['SELECT'],
        '"STG_TIMETABLE".raw_html_old',
    )
