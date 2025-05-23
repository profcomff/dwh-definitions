"""fix redirector

Revision ID: 5edf7206774e
Revises: eefb1c66dcfe
Create Date: 2025-03-15 19:49:21.495527

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '5edf7206774e'
down_revision = 'eefb1c66dcfe'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('redirect_fact', 'link_id', existing_type=sa.INTEGER(), nullable=True, schema='STG_REDIRECTOR')


def downgrade():
    op.alter_column('redirect_fact', 'link_id', existing_type=sa.INTEGER(), nullable=False, schema='STG_REDIRECTOR')
