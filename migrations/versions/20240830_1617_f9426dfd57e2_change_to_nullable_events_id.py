"""change to nullable events_id

Revision ID: f9426dfd57e2
Revises: eba63ac1dd15
Create Date: 2024-08-30 16:17:30.062783

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'f9426dfd57e2'
down_revision = 'eba63ac1dd15'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'diff', 'events_id', existing_type=postgresql.ARRAY(sa.INTEGER()), nullable=True, schema='STG_RASPHYSMSU'
    )
    op.alter_column(
        'new', 'events_id', existing_type=postgresql.ARRAY(sa.INTEGER()), nullable=True, schema='STG_RASPHYSMSU'
    )
    op.alter_column(
        'old', 'events_id', existing_type=postgresql.ARRAY(sa.INTEGER()), nullable=True, schema='STG_RASPHYSMSU'
    )


def downgrade():
    op.alter_column(
        'old', 'events_id', existing_type=postgresql.ARRAY(sa.INTEGER()), nullable=False, schema='STG_RASPHYSMSU'
    )
    op.alter_column(
        'new', 'events_id', existing_type=postgresql.ARRAY(sa.INTEGER()), nullable=False, schema='STG_RASPHYSMSU'
    )
    op.alter_column(
        'diff', 'events_id', existing_type=postgresql.ARRAY(sa.INTEGER()), nullable=False, schema='STG_RASPHYSMSU'
    )
