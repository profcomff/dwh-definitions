"""added column to fetch with back data

Revision ID: 066fd36bb01c
Revises: f8908a4837a5
Create Date: 2025-04-12 15:04:33.204263

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '066fd36bb01c'
down_revision = 'f8908a4837a5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('param', sa.Column('is_public', sa.Boolean(), nullable=True), schema='STG_USERDATA')


def downgrade():
    op.drop_column('param', 'is_public', schema='STG_USERDATA')
