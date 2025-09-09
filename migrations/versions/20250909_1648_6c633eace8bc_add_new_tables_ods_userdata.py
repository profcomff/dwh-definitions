"""add-new-tables-ods-userdata

Revision ID: 6c633eace8bc
Revises: 2a352723139d
Create Date: 2025-09-09 16:48:16.573058

"""

import os

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


revision = '6c633eace8bc'
down_revision = '2a352723139d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'rzd',
        sa.Column('rzd_number', sa.String(), nullable=False, comment='Номер в системе РЖД'),
        sa.Column('rzd_status', sa.String(), nullable=False, comment='Статус в системе РЖД'),
        sa.Column('rzd_datetime', sa.String(), nullable=False, comment='Дата в системе РЖД'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя'),
        sa.Column('source', sa.String(), nullable=False, comment='Источник данных'),
        sa.Column('created', sa.DateTime(), nullable=True, comment='Дата создания записи'),
        sa.Column('modified', sa.DateTime(), nullable=True, comment='Дата последнего изменения записи'),
        sa.Column('is_deleted', sa.Boolean(), nullable=True, comment='Флаг удаления записи'),
        sa.PrimaryKeyConstraint('rzd_number', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'status',
        sa.Column('status', sa.String(), nullable=False, comment='Текущий статус пользователя'),
        sa.Column('status_gain_date', sa.String(), nullable=False, comment='Дата получения текущего статуса'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя'),
        sa.Column('source', sa.String(), nullable=False, comment='Источник данных'),
        sa.Column('created', sa.DateTime(), nullable=True, comment='Дата создания записи'),
        sa.Column('modified', sa.DateTime(), nullable=True, comment='Дата последнего изменения записи'),
        sa.Column('is_deleted', sa.Boolean(), nullable=True, comment='Флаг удаления записи'),
        sa.PrimaryKeyConstraint('status', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )


def downgrade():
    op.alter_column(
        'git_hub_username',
        'is_deleted',
        existing_type=sa.BOOLEAN(),
        comment=None,
        existing_comment='Флаг удаления записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'modified',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата последнего изменения записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'created',
        existing_type=postgresql.TIMESTAMP(),
        comment=None,
        existing_comment='Дата создания записи',
        existing_nullable=True,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'source',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Источник данных',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'user_id',
        existing_type=sa.INTEGER(),
        comment=None,
        existing_comment='Идентификатор пользователя',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.alter_column(
        'git_hub_username',
        'username',
        existing_type=sa.VARCHAR(),
        comment=None,
        existing_comment='Имя пользователя GitHub',
        existing_nullable=False,
        schema='ODS_USERDATA',
    )
    op.drop_table('status', schema='ODS_USERDATA')
    op.drop_table('rzd', schema='ODS_USERDATA')
