"""DM infra logs

Revision ID: 1100c470c547
Revises: 33f7db929809
Create Date: 2024-05-07 07:42:31.134852

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '1100c470c547'
down_revision = '33f7db929809'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("DM_INFRA_LOGS")
    op.create_table(
        'container_log_cube',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('container_name', sa.String(), nullable=False, comment='Название контейнера'),
        sa.Column('create_date', sa.String(), nullable=False, comment='Дата лога'),
        sa.Column('debug_cnt', sa.Integer(), nullable=False, comment='Количество записей с типом DEBUG'),
        sa.Column('warn_cnt', sa.Integer(), nullable=False, comment='Количество записей с типом WARN'),
        sa.Column('info_cnt', sa.Integer(), nullable=False, comment='Количество записей с типом INFO'),
        sa.Column('error_cnt', sa.Integer(), nullable=False, comment='Количество записей с типом ERROR'),
        sa.Column('critical_cnt', sa.Integer(), nullable=False, comment='Количество записей с типом CRITICAL'),
        sa.Column('other_cnt', sa.Integer(), nullable=False, comment='Количество записей с другими типами'),
        sa.PrimaryKeyConstraint('id'),
        schema='DM_INFRA_LOGS',
        comment='Куб типов логов контейнера',
    )
    op.create_group(
        "test_dwh_dm_infra_logs_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_read"
    )
    op.create_group(
        "test_dwh_dm_infra_logs_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_write"
    )
    op.create_group(
        "test_dwh_dm_infra_logs_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_all"
    )
    op.grant_on_schema(
        "test_dwh_dm_infra_logs_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_read",
        "DM_INFRA_LOGS",
    )
    op.grant_on_schema(
        "test_dwh_dm_infra_logs_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_write",
        "DM_INFRA_LOGS",
    )
    op.grant_on_schema(
        "test_dwh_dm_infra_logs_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_all",
        "DM_INFRA_LOGS",
    )
    op.grant_on_table(
        "test_dwh_dm_infra_logs_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_read",
        ['SELECT'],
        '"DM_INFRA_LOGS".container_log_cube',
    )
    op.grant_on_table(
        "test_dwh_dm_infra_logs_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_INFRA_LOGS".container_log_cube',
    )
    op.grant_on_table(
        "test_dwh_dm_infra_logs_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_all",
        ['ALL'],
        '"DM_INFRA_LOGS".container_log_cube',
    )
    op.alter_column(
        'container_log',
        'record',
        existing_type=sa.JSON(),
        comment='Данные из строки лога',
        existing_nullable=False,
        schema='ODS_INFRA_LOGS',
    )
    op.alter_column(
        'container_log',
        'container_name',
        existing_type=sa.String(),
        comment='Название контейнера, породившего строку лога',
        existing_nullable=False,
        schema='ODS_INFRA_LOGS',
    )
    op.alter_column(
        'container_log',
        'create_ts',
        existing_type=sa.DateTime(),
        comment='Время создания записи лога',
        existing_nullable=False,
        schema='ODS_INFRA_LOGS',
    )
    op.create_table_comment(
        'container_log', 'Логи запущенных контейнеров с приложениями', existing_comment=None, schema='ODS_INFRA_LOGS'
    )


def downgrade():
    op.revoke_on_schema(
        "test_dwh_dm_infra_logs_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_all",
        "DM_INFRA_LOGS",
    )
    op.revoke_on_schema(
        (
            "test_dwh_dm_infra_logs_write"
            if os.getenv("ENVIRONMENT") != "production"
            else "prod_dwh_dm_infra_logs_write"
        ),
        "DM_INFRA_LOGS",
    )
    op.revoke_on_schema(
        ("test_dwh_dm_infra_logs_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_read"),
        "DM_INFRA_LOGS",
    )
    op.drop_table('container_log_cube', schema='DM_INFRA_LOGS')
    op.delete_group(
        "test_dwh_dm_infra_logs_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_all"
    )
    op.delete_group(
        "test_dwh_dm_infra_logs_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_write"
    )
    op.delete_group(
        "test_dwh_dm_infra_logs_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_infra_logs_read"
    )
    op.drop_table_schema("DM_INFRA_LOGS")
    op.drop_table_comment(
        'container_log', existing_comment='Логи запущенных контейнеров с приложениями', schema='ODS_INFRA_LOGS'
    )
    op.alter_column(
        'container_log',
        'create_ts',
        existing_type=sa.DateTime(),
        comment=None,
        existing_comment='Время создания записи лога',
        existing_nullable=False,
        schema='ODS_INFRA_LOGS',
    )
    op.alter_column(
        'container_log',
        'container_name',
        existing_type=sa.String(),
        comment=None,
        existing_comment='Название контейнера, породившего строку лога',
        existing_nullable=False,
        schema='ODS_INFRA_LOGS',
    )
    op.alter_column(
        'container_log',
        'record',
        existing_type=sa.JSON(),
        comment=None,
        existing_comment='Данные из строки лога',
        existing_nullable=False,
        schema='ODS_INFRA_LOGS',
    )
