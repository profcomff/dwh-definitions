"""update usersesssion_schema

Revision ID: cfbe67fec54d
Revises: f86ba4919842
Create Date: 2025-02-08 06:26:16.969161

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'cfbe67fec54d'
down_revision = 'f86ba4919842'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user_session', sa.Column('is_unbounded', sa.Boolean(), nullable=True), schema='STG_AUTH')


def downgrade():
    op.drop_column('user_session', 'is_unbounded', schema='STG_AUTH')
