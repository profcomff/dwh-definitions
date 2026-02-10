"""rental-and-social-struct-fix

Revision ID: 31293ac08820
Revises: 3c2c26d09969
Create Date: 2025-05-24 23:52:51.261700

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '31293ac08820'
down_revision = '3c2c26d09969'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('rating_actions', schema='DM_RENTAL'),
    op.drop_column("git_hub", "assignee_login", schema="ODS_SOCIAL")
    op.add_column("git_hub", sa.Column("assignee_login", sa.String()), schema="ODS_SOCIAL")


def downgrade():
    op.create_table(
        'rating_actions',
        sa.Column('uuid', sa.UUID(), autoincrement=False, nullable=False, comment='Техническое поле в dwh'),
        sa.Column('action', sa.VARCHAR(), autoincrement=False, nullable=False, comment='Совершенное действие'),
        sa.Column('path_to', sa.VARCHAR(), autoincrement=False, nullable=True, comment='Назначение перехода'),
        sa.Column(
            'response_status_code',
            sa.INTEGER(),
            autoincrement=False,
            nullable=False,
            comment='Код статуса ответа от сервера',
        ),
        sa.Column(
            'user_id',
            sa.INTEGER(),
            autoincrement=False,
            nullable=False,
            comment='Идентификатор пользователя, отправившего запрос',
        ),
        sa.Column('query', sa.VARCHAR(), autoincrement=False, nullable=False, comment='Переданные параметры запроса'),
        sa.Column(
            'create_ts',
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=False,
            comment='Таймстемп создания (московское время)',
        ),
        sa.Column('count_100', sa.INTEGER(), autoincrement=False, nullable=False, comment='Количество 100 ошибок'),
        sa.Column('count_200', sa.INTEGER(), autoincrement=False, nullable=False, comment='Количество 200 ошибок'),
        sa.Column('count_300', sa.INTEGER(), autoincrement=False, nullable=False, comment='Количество 300 ошибок'),
        sa.Column('count_400', sa.INTEGER(), autoincrement=False, nullable=False, comment='Количество 400 ошибок'),
        sa.Column('count_500', sa.INTEGER(), autoincrement=False, nullable=False, comment='Количество 500 ошибок'),
        sa.PrimaryKeyConstraint('uuid', name='rating_actions_pkey'),
        schema='DM_RENTAL',
        comment='\n    Логи и ошибки. Тянутся из рейтинга\n    ',
    )
    op.drop_column("git_hub", "assignee_login", schema="ODS_SOCIAL")
    op.add_column("git_hub", sa.Column("assignee_login", sa.Integer()), schema="ODS_SOCIAL")
