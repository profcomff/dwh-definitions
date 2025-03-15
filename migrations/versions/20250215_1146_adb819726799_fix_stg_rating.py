"""fix stg rating

Revision ID: adb819726799
Revises: cfbe67fec54d
Create Date: 2025-02-15 11:46:07.544400

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'adb819726799'
down_revision = 'cfbe67fec54d'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('comment', 'subject', existing_type=sa.VARCHAR(), nullable=True, schema='STG_RATING')


def downgrade():
    op.alter_column('comment', 'subject', existing_type=sa.VARCHAR(), nullable=False, schema='STG_RATING')
