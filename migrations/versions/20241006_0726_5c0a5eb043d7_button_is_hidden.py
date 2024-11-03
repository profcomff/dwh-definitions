"""button_is_hidden

Revision ID: 5c0a5eb043d7
Revises: 0e97fd76b68a
Create Date: 2024-10-06 07:26:54.197863

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '5c0a5eb043d7'
down_revision = '0e97fd76b68a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'button',
        sa.Column('is_hidden', sa.Boolean(), nullable=False, server_default=sa.false()),
        schema='STG_SERVICES',
    )


def downgrade():
    op.drop_column('button', 'is_hidden', schema='STG_SERVICES')
