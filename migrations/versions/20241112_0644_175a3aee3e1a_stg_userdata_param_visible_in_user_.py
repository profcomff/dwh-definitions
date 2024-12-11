"""stg_userdata.param +visible_in_user_response

Revision ID: 175a3aee3e1a
Revises: 4744a389ff0b
Create Date: 2024-11-12 06:44:42.995965

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '175a3aee3e1a'
down_revision = '4744a389ff0b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('param', sa.Column('visible_in_user_response', sa.Boolean(), nullable=True), schema='STG_USERDATA')


def downgrade():
    op.drop_column('param', 'visible_in_user_response', schema='STG_USERDATA')
