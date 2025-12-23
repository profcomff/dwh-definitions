"""ods_userdata-card-table

Revision ID: 1a383420f47f
Revises: 6c633eace8bc
Create Date: 2025-09-18 21:24:21.418474

"""

import sqlalchemy as sa
from alembic import op


revision = '1a383420f47f'
down_revision = '6c633eace8bc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'card',
        sa.Column('card_id', sa.String(), nullable=False, comment='Идентификатор профсоюзного билета'),
        sa.Column('card_status', sa.String(), nullable=False, comment='Статус профсоюзного билета'),
        sa.Column('card_date', sa.String(), nullable=False, comment='Дата выдачи профсоюзного билета'),
        sa.Column('card_number', sa.String(), nullable=False, comment='Номер профсоюзного билета'),
        sa.Column('card_user', sa.String(), nullable=False, comment='Владелец профсоюзного билета'),
        sa.Column('user_id', sa.Integer(), nullable=False, comment='Идентификатор пользователя'),
        sa.Column('source', sa.String(), nullable=False, comment='Источник данных'),
        sa.Column('created', sa.DateTime(), nullable=True, comment='Дата создания записи'),
        sa.Column('modified', sa.DateTime(), nullable=True, comment='Дата последнего изменения записи'),
        sa.Column('is_deleted', sa.Boolean(), nullable=True, comment='Флаг удаления записи'),
        sa.PrimaryKeyConstraint('card_id', 'user_id'),
        schema='ODS_USERDATA',
        info={'sensitive': False},
    )


def downgrade():
    op.drop_table('card', schema='ODS_USERDATA')
