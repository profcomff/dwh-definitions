"""stg.union_member middle name add

Revision ID: 4744a389ff0b
Revises: 8ae074933b0d
Create Date: 2024-11-10 13:21:39.696651

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '4744a389ff0b'
down_revision = '8ae074933b0d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('union_member', sa.Column('middle_name', sa.String(), nullable=True), schema='STG_UNION_MEMBER')


def downgrade():
    op.drop_column('union_member', 'middle_name', schema='STG_UNION_MEMBER')
