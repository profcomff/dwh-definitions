"""text

Revision ID: 071bd12e355e
Revises: 5edf7206774e
Create Date: 2025-04-07 16:49:21.806789

"""

from alembic import op
import sqlalchemy as sa
import os


revision = '071bd12e355e'
down_revision = '5edf7206774e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("DM_MARKETING")
    op.create_table(
        'frontend_actions',
        sa.Column('uuid', sa.Uuid(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('action', sa.String(), nullable=False, comment='Совершенное действие'),
        sa.Column('path_from', sa.String(), nullable=True, comment='Откуда совершен переход'),
        sa.Column('path_to', sa.String(), nullable=True, comment='Назначение перехода'),
        sa.Column('user_agent', sa.String(), nullable=True, comment='Информация об операционной системе и браузере'),
        sa.Column('is_bot', sa.Boolean(), nullable=False, comment='Флаг бот или нет'),
        sa.Column('create_ts', sa.DateTime(), nullable=False, comment='Таймстемп создания'),
        sa.Column('service_name', sa.Boolean(), nullable=False, comment='Назввание сервиса, куда пользователь перешел'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='DM_MARKETING',
        comment='\n    Фронтендовые события\n    ',
        info={'sensitive': False},
    )
    op.create_group(
        "test_dwh_dm_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_read"
    )
    op.create_group(
        "test_dwh_dm_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_write"
    )
    op.create_group(
        "test_dwh_dm_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_all"
    )
    op.grant_on_schema(
        "test_dwh_dm_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_read",
        "DM_MARKETING",
    )
    op.grant_on_schema(
        "test_dwh_dm_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_write",
        "DM_MARKETING",
    )
    op.grant_on_schema(
        "test_dwh_dm_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_all",
        "DM_MARKETING",
    )
    op.grant_on_table(
        "test_dwh_dm_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_read",
        ['SELECT'],
        '"DM_MARKETING".frontend_actions',
    )
    op.grant_on_table(
        "test_dwh_dm_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_MARKETING".frontend_actions',
    )
    op.grant_on_table(
        "test_dwh_dm_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_all",
        ['ALL'],
        '"DM_MARKETING".frontend_actions',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_dm_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_all",
        ['ALL'],
        '"DM_MARKETING".frontend_actions',
    )
    op.revoke_on_table(
        "test_dwh_dm_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_MARKETING".frontend_actions',
    )
    op.revoke_on_table(
        "test_dwh_dm_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_read",
        ['SELECT'],
        '"DM_MARKETING".frontend_actions',
    )
    op.revoke_on_schema(
        "test_dwh_dm_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_all",
        "DM_MARKETING",
    )
    op.revoke_on_schema(
        "test_dwh_dm_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_write",
        "DM_MARKETING",
    )
    op.revoke_on_schema(
        "test_dwh_dm_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_read",
        "DM_MARKETING",
    )
    op.drop_table('frontend_actions', schema='DM_MARKETING')
    op.delete_group(
        "test_dwh_dm_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_all"
    )
    op.delete_group(
        "test_dwh_dm_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_write"
    )
    op.delete_group(
        "test_dwh_dm_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_read"
    )
    op.drop_table_schema("DM_MARKETING")
