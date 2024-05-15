"""dm timetable

Revision ID: 4f83a891c676
Revises: 7a18bd9ff633
Create Date: 2024-05-15 18:26:05.695683

"""

from alembic import op
import sqlalchemy as sa
import os

revision = '4f83a891c676'
down_revision = '7a18bd9ff633'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'dim_class_act',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='DM_TIMETABLE',
    )
    op.create_table(
        'dim_group_act',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('api_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('number', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='DM_TIMETABLE',
    )
    op.create_table(
        'dim_lecturer_act',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('api_id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('middle_name', sa.String(), nullable=True),
        sa.Column('last_name', sa.String(), nullable=True),
        sa.Column('avatar_id', sa.Integer(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='DM_TIMETABLE',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dim_lecturer_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dim_lecturer_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dim_lecturer_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dim_group_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dim_group_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dim_group_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dim_class_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dim_class_act',
    )
    op.grant_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dim_class_act',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dim_class_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dim_class_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dim_class_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dim_group_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dim_group_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dim_group_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_all",
        ['ALL'],
        '"DM_TIMETABLE".dim_lecturer_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_TIMETABLE".dim_lecturer_act',
    )
    op.revoke_on_table(
        "test_dwh_dm_timetable_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_timetable_read",
        ['SELECT'],
        '"DM_TIMETABLE".dim_lecturer_act',
    )
    op.drop_table('dim_lecturer_act', schema='DM_TIMETABLE')
    op.drop_table('dim_group_act', schema='DM_TIMETABLE')
    op.drop_table('dim_class_act', schema='DM_TIMETABLE')
