"""rental-fix

Revision ID: 83a86d9e5c9b
Revises: 00dc9eb31a18
Create Date: 2025-04-29 23:14:06.433484

"""

import os

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '83a86d9e5c9b'
down_revision = '00dc9eb31a18'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('ALTER TABLE "DWH_RENTAL".item DROP COLUMN IF EXISTS type')
    op.drop_column('item', 'type', schema='ODS_RENTAL')
    op.add_column('event', sa.Column('id', sa.Integer(), nullable=False), schema='STG_RENTAL')
    op.drop_column('event', 'api_id', schema='STG_RENTAL')
    op.add_column('item', sa.Column('id', sa.Integer(), nullable=False), schema='STG_RENTAL')
    op.drop_column('item', 'type', schema='STG_RENTAL')
    op.drop_column('item', 'api_id', schema='STG_RENTAL')
    op.add_column('item_type', sa.Column('id', sa.Integer(), nullable=False), schema='STG_RENTAL')
    op.drop_column('item_type', 'api_id', schema='STG_RENTAL')
    op.add_column('rental_session', sa.Column('id', sa.Integer(), nullable=False), schema='STG_RENTAL')
    op.drop_column('rental_session', 'api_id', schema='STG_RENTAL')
    op.add_column('strike', sa.Column('id', sa.Integer(), nullable=False), schema='STG_RENTAL')
    op.drop_column('strike', 'api_id', schema='STG_RENTAL')


def downgrade():
    op.add_column('strike', sa.Column('api_id', sa.INTEGER(), autoincrement=True, nullable=False), schema='STG_RENTAL')
    op.drop_column('strike', 'id', schema='STG_RENTAL')
    op.add_column(
        'rental_session', sa.Column('api_id', sa.INTEGER(), autoincrement=True, nullable=False), schema='STG_RENTAL'
    )
    op.drop_column('rental_session', 'id', schema='STG_RENTAL')
    op.add_column(
        'item_type', sa.Column('api_id', sa.INTEGER(), autoincrement=True, nullable=False), schema='STG_RENTAL'
    )
    op.drop_column('item_type', 'id', schema='STG_RENTAL')
    op.add_column('item', sa.Column('api_id', sa.INTEGER(), autoincrement=True, nullable=False), schema='STG_RENTAL')
    op.add_column('item', sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=False), schema='STG_RENTAL')
    op.drop_column('item', 'id', schema='STG_RENTAL')
    op.add_column('event', sa.Column('api_id', sa.INTEGER(), autoincrement=True, nullable=False), schema='STG_RENTAL')
    op.drop_column('event', 'id', schema='STG_RENTAL')
    op.add_column(
        'item',
        sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=False, comment='Тип вещи'),
        schema='ODS_RENTAL',
    )
