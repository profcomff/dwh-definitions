"""scd2 tables for auth

Revision ID: dc5fba8fbf1d
Revises: 7f2cd21e0509
Create Date: 2024-11-03 17:08:03.545748

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'dc5fba8fbf1d'
down_revision = '7f2cd21e0509'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("ODS_AUTH")
    op.create_table(
        'auth_method',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('auth_method', sa.String(), nullable=True),
        sa.Column('param', sa.String(), nullable=True),
        sa.Column('value', sa.String(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('update_ts', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.Column('valid_from_dt', sa.Date(), nullable=True),
        sa.Column('valid_to_dt', sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_AUTH',
        comment='\n    Historical table for STG_AUTH.auth_method\n    ',
    )
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('update_ts', sa.DateTime(), nullable=True),
        sa.Column('valid_from_dt', sa.Date(), nullable=True),
        sa.Column('valid_to_dt', sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_AUTH',
        comment='\n    Historical table for STG_AUTH.user\n    ',
    )
    op.create_group("test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read")
    op.create_group(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write"
    )
    op.create_group("test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all")
    op.grant_on_schema(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read", "ODS_AUTH"
    )
    op.grant_on_schema(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write", "ODS_AUTH"
    )
    op.grant_on_schema(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all", "ODS_AUTH"
    )
    op.grant_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".auth_method',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".user',
    )
    op.grant_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".user',
    )
    # lol I'll keep it here)
    op.create_table_comment(
        'comment',
        '\n    Comments from dubinushka\n    Because this data is downloaded from .sql query, the order of columns is significant\n    ',
        existing_comment='Comments from dubinushka\n    Because this data is downloaded from .sql query, the order of columns is significant',
        schema='STG_DUBINUSHKA_MANUAL',
    )
    op.create_table_comment(
        'lecturer',
        '\n    Lecturers from dubinushka\n    Because this data is downloaded from .sql query, the order of columns is significant\n    ',
        existing_comment='Lecturers from dubinushka\n    Because this data is downloaded from .sql query, the order of columns is significant',
        schema='STG_DUBINUSHKA_MANUAL',
    )


def downgrade():
    op.create_table_comment(
        'lecturer',
        'Lecturers from dubinushka\n    Because this data is downloaded from .sql query, the order of columns is significant',
        existing_comment='\n    Lecturers from dubinushka\n    Because this data is downloaded from .sql query, the order of columns is significant\n    ',
        schema='STG_DUBINUSHKA_MANUAL',
    )
    op.create_table_comment(
        'comment',
        'Comments from dubinushka\n    Because this data is downloaded from .sql query, the order of columns is significant',
        existing_comment='\n    Comments from dubinushka\n    Because this data is downloaded from .sql query, the order of columns is significant\n    ',
        schema='STG_DUBINUSHKA_MANUAL',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".user',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all",
        ['ALL'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_table(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read",
        ['SELECT'],
        '"ODS_AUTH".auth_method',
    )
    op.revoke_on_schema(
        "test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all", "ODS_AUTH"
    )
    op.revoke_on_schema(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write", "ODS_AUTH"
    )
    op.revoke_on_schema(
        "test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read", "ODS_AUTH"
    )
    op.drop_table('user', schema='ODS_AUTH')
    op.drop_table('auth_method', schema='ODS_AUTH')
    op.delete_group("test_dwh_ods_auth_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_all")
    op.delete_group(
        "test_dwh_ods_auth_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_write"
    )
    op.delete_group("test_dwh_ods_auth_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_auth_read")
    op.drop_table_schema("ODS_AUTH")
