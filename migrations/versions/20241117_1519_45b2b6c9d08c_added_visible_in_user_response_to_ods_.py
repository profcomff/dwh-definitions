"""Added visible_in_user_response to ODS_INFO.param_hist

Revision ID: 45b2b6c9d08c
Revises: 175a3aee3e1a
Create Date: 2024-11-17 15:19:06.216964

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '45b2b6c9d08c'
down_revision = '175a3aee3e1a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('param_hist', sa.Column('visible_in_user_response', sa.Boolean(), nullable=True), schema='ODS_INFO')


def downgrade():
    op.drop_column('param_hist', 'visible_in_user_response', schema='ODS_INFO')
