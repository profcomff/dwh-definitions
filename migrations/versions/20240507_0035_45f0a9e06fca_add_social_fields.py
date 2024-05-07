"""Add social fields

Revision ID: 45f0a9e06fca
Revises: d71054079206
Create Date: 2024-05-07 00:35:19.238888

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '45f0a9e06fca'
down_revision = 'd71054079206'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('group', sa.Column('name', sa.String(), nullable=True), schema='STG_SOCIAL')
    op.add_column('group', sa.Column('description', sa.String(), nullable=True), schema='STG_SOCIAL')
    op.add_column('group', sa.Column('invite_link', sa.String(), nullable=True), schema='STG_SOCIAL')
    op.add_column('group', sa.Column('hidden', sa.Boolean(), nullable=True), schema='STG_SOCIAL')


def downgrade():
    op.drop_column('group', 'hidden', schema='STG_SOCIAL')
    op.drop_column('group', 'invite_link', schema='STG_SOCIAL')
    op.drop_column('group', 'description', schema='STG_SOCIAL')
    op.drop_column('group', 'name', schema='STG_SOCIAL')
