"""scds for userdata

Revision ID: cf7557c43271
Revises: 8253b11f2c82
Create Date: 2024-11-03 11:14:37.093594

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'cf7557c43271'
down_revision = '8253b11f2c82'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'info_hist',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('param_id', sa.Integer(), nullable=True),
        sa.Column('source_id', sa.Integer(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=True),
        sa.Column('value', sa.String(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('modify_ts', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.Column('valid_from_dt', sa.Date(), nullable=True),
        sa.Column('valid_to_dt', sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_INFO',
        comment='\n    SCD2 historical table based on STG_USERDATA.info\n    ',
    )
    op.create_table(
        'param_hist',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('category_id', sa.Integer(), nullable=True),
        sa.Column('is_required', sa.Boolean(), nullable=True),
        sa.Column('changeable', sa.Boolean(), nullable=True),
        sa.Column('type', sa.String(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('modify_ts', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.Column('validation', sa.String(), nullable=True),
        sa.Column('valid_from_dt', sa.Date(), nullable=True),
        sa.Column('valid_to_dt', sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_INFO',
        comment='\n    SCD2 historical table based on STG_USERDATA.param\n    ',
    )
    op.grant_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".param_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".param_hist',
    )
    op.grant_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".param_hist',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".param_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_all",
        ['ALL'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"ODS_INFO".info_hist',
    )
    op.revoke_on_table(
        "test_dwh_ods_info_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_ods_info_read",
        ['SELECT'],
        '"ODS_INFO".info_hist',
    )
    op.drop_table('param_hist', schema='ODS_INFO')
    op.drop_table('info_hist', schema='ODS_INFO')
