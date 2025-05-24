"""ods-gitstat

Revision ID: 3c2c26d09969
Revises: 1d108dc04935
Create Date: 2025-05-22 13:36:04.211966

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '3c2c26d09969'
down_revision = '1d108dc04935'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'git_hub',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле в dwh'),
        sa.Column('status', sa.String(), nullable=False, comment='Статус issue'),
        sa.Column('url', sa.String(), nullable=False, comment='Ссылка на issue'),
        sa.Column('issue_id', sa.Integer(), nullable=True, comment='Идентификатор issue'),
        sa.Column('user_id', sa.Integer(), nullable=True, comment='Идентификатор пользователя открывшего issue'),
        sa.Column('user_login', sa.String(), nullable=True, comment='Логин пользователя открывшего issue'),
        sa.Column('issue_title', sa.String(), nullable=True, comment='Название issue'),
        sa.Column('repository_id', sa.Integer(), nullable=True, comment='Идентификатор репозитория'),
        sa.Column('assignee_id', sa.Integer(), nullable=True, comment='Идентификатор назначенного исполнителем issue'),
        sa.Column('assignee_login', sa.Integer(), nullable=True, comment='Логин назначенного исполнителем issue'),
        sa.Column('created_at', sa.DateTime(), nullable=True, comment='Временная метка создания issue'),
        sa.Column('updated_at', sa.DateTime(), nullable=True, comment='Временная метка апдейта issue'),
        sa.Column('closed_at', sa.DateTime(), nullable=True, comment='Временная метка закрытия issue'),
        sa.Column('organization_id', sa.Integer(), nullable=False, comment='Идентификатор организации'),
        sa.Column('organizatin_login', sa.String(), nullable=True, comment='Логин организации'),
        sa.Column('event_ts', sa.DateTime(), nullable=False, comment='Временная метка данного события'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='ODS_SOCIAL',
        comment='\n    Статистика GitHub\n    ',
        info={'sensitive': False},
    )


def downgrade():
    op.drop_table('git_hub', schema='ODS_SOCIAL')
