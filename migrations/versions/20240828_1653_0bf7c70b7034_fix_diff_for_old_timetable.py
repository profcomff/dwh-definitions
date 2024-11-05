"""fix_diff_for_old_timetable

Revision ID: 0bf7c70b7034
Revises: 009029ff68e2
Create Date: 2024-08-28 16:53:06.541063

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '0bf7c70b7034'
down_revision = '009029ff68e2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('diff', sa.Column('action', sa.String(), nullable=True), schema='STG_RASPHYSMSU')


def downgrade():
    op.drop_column('diff', 'action', schema='STG_RASPHYSMSU')
