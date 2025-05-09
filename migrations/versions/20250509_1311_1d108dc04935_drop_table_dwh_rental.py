"""drop_table_dwh_rental

Revision ID: 1d108dc04935
Revises: 83a86d9e5c9b
Create Date: 2025-05-09 13:11:08.101214

"""

import os

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '1d108dc04935'
down_revision = '83a86d9e5c9b'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('rating_actions', schema='ODS_RENTAL')


def downgrade():
    op.create_table(
        'rating_actions',
        sa.Column('uuid', sa.UUID(), autoincrement=False, nullable=False),
        sa.Column('action', sa.VARCHAR(), autoincrement=False, nullable=False, comment='Совершенное действие'),
        sa.Column('path_to', sa.VARCHAR(), autoincrement=False, nullable=True, comment='Назначение перехода'),
        sa.Column('response_status_code', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('query', sa.VARCHAR(), autoincrement=False, nullable=False, comment='Переданные параметры запроса'),
        sa.Column(
            'create_ts',
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=False,
            comment='Таймстемп создания (московское время)',
        ),
        sa.PrimaryKeyConstraint('uuid', name='rating_actions_pkey'),
        schema='ODS_RENTAL',
        comment='\n    События в рейтинге\n    ',
    )
