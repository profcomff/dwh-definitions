"""Fix tg chat int type

Revision ID: d71054079206
Revises: b0d0bbe799db
Create Date: 2024-05-05 01:35:47.729652

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'd71054079206'
down_revision = 'b0d0bbe799db'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'telegram_channel',
        'channel_id',
        existing_type=sa.Integer,
        type_=sa.BIGINT,
        nullable=True,
        schema='STG_SOCIAL',
    )
    op.alter_column(
        'telegram_chat',
        'chat_id',
        existing_type=sa.Integer,
        type_=sa.BIGINT,
        nullable=True,
        schema='STG_SOCIAL',
    )


def downgrade():
    op.alter_column(
        'telegram_channel',
        'channel_id',
        existing_type=sa.BIGINT,
        type_=sa.Integer,
        nullable=True,
        schema='STG_SOCIAL',
    )
    op.alter_column(
        'telegram_chat',
        'chat_id',
        existing_type=sa.BIGINT,
        type_=sa.Integer,
        nullable=True,
        schema='STG_SOCIAL',
    )
