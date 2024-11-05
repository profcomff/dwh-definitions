"""add_link_full_schema2

Revision ID: da280c5f1dac
Revises: eebd0dbc6839
Create Date: 2024-08-30 18:06:18.480250

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = 'da280c5f1dac'
down_revision = 'eebd0dbc6839'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'link_new_with_dates', 'subject', existing_type=sa.VARCHAR(), nullable=True, schema='STG_RASPHYSMSU'
    )
    op.alter_column('link_new_with_dates', 'odd', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_RASPHYSMSU')
    op.alter_column('link_new_with_dates', 'even', existing_type=sa.BOOLEAN(), nullable=True, schema='STG_RASPHYSMSU')
    op.alter_column('link_new_with_dates', 'start', existing_type=sa.VARCHAR(), nullable=True, schema='STG_RASPHYSMSU')
    op.alter_column('link_new_with_dates', 'end', existing_type=sa.VARCHAR(), nullable=True, schema='STG_RASPHYSMSU')


def downgrade():
    op.alter_column('link_new_with_dates', 'end', existing_type=sa.VARCHAR(), nullable=False, schema='STG_RASPHYSMSU')
    op.alter_column('link_new_with_dates', 'start', existing_type=sa.VARCHAR(), nullable=False, schema='STG_RASPHYSMSU')
    op.alter_column('link_new_with_dates', 'even', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_RASPHYSMSU')
    op.alter_column('link_new_with_dates', 'odd', existing_type=sa.BOOLEAN(), nullable=False, schema='STG_RASPHYSMSU')
    op.alter_column(
        'link_new_with_dates', 'subject', existing_type=sa.VARCHAR(), nullable=False, schema='STG_RASPHYSMSU'
    )
