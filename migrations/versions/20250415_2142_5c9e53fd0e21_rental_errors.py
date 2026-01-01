"""rental-errors

Revision ID: 5c9e53fd0e21
Revises: 6bdc4e13362e
Create Date: 2025-04-15 21:42:22.382998

"""

import sqlalchemy as sa
from alembic import op


revision = '5c9e53fd0e21'
down_revision = '6bdc4e13362e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'rating_actions',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле в dwh'),
        sa.Column('action', sa.String(), nullable=False, comment='Совершенное действие'),
        sa.Column('path_to', sa.String(), nullable=True, comment='Назначение перехода'),
        sa.Column('response_status_code', sa.Integer(), nullable=False, comment='Код статуса ответа от сервера'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя, отправившего запрос'),
        sa.Column('query', sa.String(), nullable=False, comment='Переданные параметры запроса'),
        sa.Column('create_ts', sa.DateTime(), nullable=False, comment='Таймстемп создания (московское время)'),
        sa.Column('count_100', sa.Integer(), nullable=False, comment='Количество 100 ошибок'),
        sa.Column('count_200', sa.Integer(), nullable=False, comment='Количество 200 ошибок'),
        sa.Column('count_300', sa.Integer(), nullable=False, comment='Количество 300 ошибок'),
        sa.Column('count_400', sa.Integer(), nullable=False, comment='Количество 400 ошибок'),
        sa.Column('count_500', sa.Integer(), nullable=False, comment='Количество 500 ошибок'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='DM_RENTAL',
        comment='\n    Логи и ошибки. Тянутся из рейтинга\n    ',
        info={'sensitive': False},
    )
    op.create_table(
        'rating_actions',
        sa.Column('uuid', sa.Uuid(), nullable=False),
        sa.Column('action', sa.String(), nullable=False, comment='Совершенное действие'),
        sa.Column('path_to', sa.String(), nullable=True, comment='Назначение перехода'),
        sa.Column('response_status_code', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('query', sa.String(), nullable=False, comment='Переданные параметры запроса'),
        sa.Column('create_ts', sa.DateTime(), nullable=False, comment='Таймстемп создания (московское время)'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='ODS_RENTAL',
        comment='\n    События в рейтинге\n    ',
        info={'sensitive': False},
    )
    op.add_column(
        'dm_rentals_events',
        sa.Column('activity_max_time', sa.Integer(), nullable=False, comment='Час пиковой активности'),
        schema='DM_RENTAL',
    )
    op.add_column(
        'dm_rentals_events',
        sa.Column('activity_max', sa.Integer(), nullable=False, comment='Количество активности в час пиковой нагрузки'),
        schema='DM_RENTAL',
    )


def downgrade():
    op.drop_column('dm_rentals_events', 'activity_max', schema='DM_RENTAL')
    op.drop_column('dm_rentals_events', 'activity_max_time', schema='DM_RENTAL')
    op.drop_table('rating_actions', schema='ODS_RENTAL')
    op.drop_table('rating_actions', schema='DM_RENTAL')
