"""dm_rental_refactor_and_strike_datamart

Revision ID: 3ac342622c64
Revises: 1a383420f47f
Create Date: 2025-09-19 21:26:39.203543

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


revision = '3ac342622c64'
down_revision = '1a383420f47f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'dm_strike',
        sa.Column('strike_id', sa.Integer(), nullable=False, comment='Идентификатор страйка'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя'),
        sa.Column('user_segment', sa.String(), nullable=True, comment='Сегмент пользователя (опционально)'),
        sa.Column('session_id', sa.Integer(), nullable=False, comment='Идентификатор сессии аренды'),
        sa.Column('item_id', sa.Integer(), nullable=False, comment='Идентификатор вещи'),
        sa.Column('item_type_id', sa.Integer(), nullable=False, comment='Идентификатор типа вещи'),
        sa.Column('item_type_name', sa.String(), nullable=True, comment='Название типа вещи'),
        sa.Column('item_name', sa.String(), nullable=False, comment='Название вещи'),
        sa.Column('strike_reason', sa.String(), nullable=True, comment='Причина страйка'),
        sa.Column('strike_date', sa.DateTime(), nullable=False, comment='Дата и время начисления страйка'),
        sa.Column('admin_id', sa.Integer(), nullable=False, comment='Идентификатор администратора, вынесшего страйк'),
        sa.Column('admin_name', sa.String(), nullable=True, comment='Имя администратора (де-normalized)'),
        sa.Column('total_strikes_user', sa.Integer(), nullable=False, comment='Общее количество страйков пользователя'),
        sa.Column('total_strikes_session', sa.Integer(), nullable=False, comment='Общее количество страйков в сессии'),
        sa.Column('rental_start_ts', sa.DateTime(), nullable=False, comment='Начало аренды'),
        sa.Column('rental_end_ts', sa.DateTime(), nullable=False, comment='Планируемое окончание аренды'),
        sa.Column('return_ts', sa.DateTime(), nullable=True, comment='Фактическое время возврата'),
        sa.Column('session_status', sa.String(), nullable=True, comment='Статус сессии аренды'),
        sa.PrimaryKeyConstraint('strike_id'),
        schema='DM_RENTAL',
        comment='\n    Витрина страйки\n    ',
        info={'sensitive': False},
    )
    op.add_column(
        'dm_rentals_events',
        sa.Column('session_duration_minutes', sa.DateTime(), nullable=True, comment='Длительность аренды в мин'),
        schema='DM_RENTAL',
    )
    op.add_column(
        'dm_rentals_events',
        sa.Column('overdue_minutes', sa.DateTime(), nullable=True, comment='Просрочка времени аренды в мин'),
        schema='DM_RENTAL',
    )
    op.add_column(
        'dm_rentals_events',
        sa.Column('strikes_count', sa.Integer(), nullable=False, comment='Количество страйков за сессию'),
        schema='DM_RENTAL',
    )
    op.create_table_comment(
        'dm_rentals_events',
        '\n    Витрина данных арендных сессий\n    ',
        existing_comment='\n    Данные арендных сессий\n    ',
        schema='DM_RENTAL',
    )
    op.drop_column('dm_rentals_events', 'strike_date', schema='DM_RENTAL')
    op.drop_column('dm_rentals_events', 'strike_reason', schema='DM_RENTAL')
    op.drop_column('dm_rentals_events', 'admin_strike_id', schema='DM_RENTAL')


def downgrade():
    op.add_column(
        'dm_rentals_events',
        sa.Column('admin_strike_id', sa.INTEGER(), autoincrement=False, nullable=True, comment='Идентификаор админа'),
        schema='DM_RENTAL',
    )
    op.add_column(
        'dm_rentals_events',
        sa.Column('strike_reason', sa.VARCHAR(), autoincrement=False, nullable=True, comment='Причина страйка'),
        schema='DM_RENTAL',
    )
    op.add_column(
        'dm_rentals_events',
        sa.Column(
            'strike_date',
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=True,
            comment='Timestamp начисления страйка, мск',
        ),
        schema='DM_RENTAL',
    )
    op.create_table_comment(
        'dm_rentals_events',
        '\n    Данные арендных сессий\n    ',
        existing_comment='\n    Витрина данных арендных сессий\n    ',
        schema='DM_RENTAL',
    )
    op.drop_column('dm_rentals_events', 'strikes_count', schema='DM_RENTAL')
    op.drop_column('dm_rentals_events', 'overdue_minutes', schema='DM_RENTAL')
    op.drop_column('dm_rentals_events', 'session_duration_minutes', schema='DM_RENTAL')
    op.drop_table('dm_strike', schema='DM_RENTAL')
