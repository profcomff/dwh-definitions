"""dm_marketing

Revision ID: f8908a4837a5
Revises: 5edf7206774e
Create Date: 2025-04-12 00:02:16.283426

"""

from alembic import op
import sqlalchemy as sa
import os


revision = 'f8908a4837a5'
down_revision = '5edf7206774e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("DM_MARKETING")
    op.create_table(
        'frontend_actions_services',
        sa.Column('uuid', sa.Uuid(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('action', sa.String(), nullable=False, comment='Совершенное действие'),
        sa.Column('path_from', sa.String(), nullable=True, comment='Откуда совершен переход'),
        sa.Column('path_to', sa.String(), nullable=True, comment='Назначение перехода'),
        sa.Column('user_agent', sa.String(), nullable=True, comment='Информация об операционной системе и браузере'),
        sa.Column('is_bot', sa.Boolean(), nullable=False, comment='Флаг бот или нет'),
        sa.Column('create_ts', sa.DateTime(), nullable=False, comment='Таймстемп создания'),
        sa.Column('service_name', sa.String(), nullable=False, comment='Назввание сервиса, куда пользователь перешел'),
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
        '"DM_MARKETING".frontend_actions_services',
    )
    op.grant_on_table(
        "test_dwh_dm_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_MARKETING".frontend_actions_services',
    )
    op.grant_on_table(
        "test_dwh_dm_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_all",
        ['ALL'],
        '"DM_MARKETING".frontend_actions_services',
    )


def downgrade():
    op.revoke_on_table(
        "test_dwh_dm_marketing_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_all",
        ['ALL'],
        '"DM_MARKETING".frontend_actions_services',
    )
    op.revoke_on_table(
        "test_dwh_dm_marketing_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_MARKETING".frontend_actions_services',
    )
    op.revoke_on_table(
        "test_dwh_dm_marketing_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_marketing_read",
        ['SELECT'],
        '"DM_MARKETING".frontend_actions_services',
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
    op.drop_table('frontend_actions_services', schema='DM_MARKETING')
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
