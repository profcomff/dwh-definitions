"""bots-actions-fix

Revision ID: 11e73bb19e82
Revises: d1a22199f353
Create Date: 2025-07-05 14:58:14.733682

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '11e73bb19e82'
down_revision = 'd1a22199f353'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'printer_bots_actions',
        'user_id',
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_comment='Айди юзера в соответствующей соцсети(tg/vk)',
        existing_nullable=False,
        schema='ODS_MARKETING',
    )
    op.alter_column(
        'printer_bots_actions',
        'number',
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_comment='Номер',
        existing_nullable=False,
        schema='ODS_MARKETING',
    )


def downgrade():
    op.alter_column(
        'printer_bots_actions',
        'number',
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_comment='Номер',
        existing_nullable=False,
        schema='ODS_MARKETING',
    )
    op.alter_column(
        'printer_bots_actions',
        'user_id',
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_comment='Айди юзера в соответствующей соцсети(tg/vk)',
        existing_nullable=False,
        schema='ODS_MARKETING',
    )
