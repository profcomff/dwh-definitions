"""STG.userdata.param.validation

Revision ID: 75df3cab6f2f
Revises: 5c0a5eb043d7
Create Date: 2024-10-08 03:38:00.033463

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '75df3cab6f2f'
down_revision = '5c0a5eb043d7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('param', sa.Column('validation', sa.String(), nullable=True), schema='STG_USERDATA')


def downgrade():
    op.drop_column('param', 'validation', schema='STG_USERDATA')
