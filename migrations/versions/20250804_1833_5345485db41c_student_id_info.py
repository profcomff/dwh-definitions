"""student-id-info

Revision ID: 5345485db41c
Revises: 80e114fe1399
Create Date: 2025-08-04 18:33:51.347044

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '5345485db41c'
down_revision = '80e114fe1399'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('union_member', sa.Column('student_id', sa.String(), nullable=True), schema='STG_UNION_MEMBER')


def downgrade():
    op.drop_column('union_member', 'student_id', schema='STG_UNION_MEMBER')
