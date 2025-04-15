"""fix viribus ods

Revision ID: 40d72f2dd950
Revises: 2685b42bfef5
Create Date: 2025-04-15 21:54:58.257996

"""

from alembic import op
import sqlalchemy as sa
import os
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '40d72f2dd950'
down_revision = '2685b42bfef5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'viribus_chat',
        sa.Column('uuid', sa.Uuid(), nullable=False, comment='Техническое поле в dwh'),
        sa.Column('thread_name', sa.String(), nullable=True, comment='Название ветки в сообществе, например Frontend'),
        sa.Column('message_text', sa.String(), nullable=True, comment='Текст сообщения в телеграме'),
        sa.Column('sender_telegram_login', sa.String(), nullable=True, comment='Логин пользователя в телеграме'),
        sa.Column('message_ts', sa.DateTime(), nullable=False, comment='Таймстемп записи в social-api'),
        sa.PrimaryKeyConstraint('uuid'),
        schema='ODS_SOCIAL',
        comment='\n    Преподаватели в rating-api\n    ',
        info={'sensitive': False},
    )
    op.drop_table('lecturer', schema='ODS_SOCIAL')


def downgrade():
    op.create_table(
        'lecturer',
        sa.Column('uuid', sa.UUID(), autoincrement=False, nullable=False, comment='Техническое поле в dwh'),
        sa.Column(
            'thread_name',
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
            comment='Название ветки в сообществе, например Frontend',
        ),
        sa.Column(
            'message_text', sa.VARCHAR(), autoincrement=False, nullable=False, comment='Текст сообщения в телеграме'
        ),
        sa.Column(
            'sender_telegram_login',
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
            comment='Логин пользователя в телеграме',
        ),
        sa.Column(
            'message_ts',
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=False,
            comment='Таймстемп записи в social-api',
        ),
        sa.PrimaryKeyConstraint('uuid', name='lecturer_pkey'),
        schema='ODS_SOCIAL',
        comment='\n    Преподаватели в rating-api\n    ',
    )
    op.drop_table('viribus_chat', schema='ODS_SOCIAL')
