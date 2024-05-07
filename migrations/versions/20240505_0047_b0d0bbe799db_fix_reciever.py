"""Fix reciever

Revision ID: b0d0bbe799db
Revises: a80b250420e4
Create Date: 2024-05-05 00:47:59.974405

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = 'b0d0bbe799db'
down_revision = 'a80b250420e4'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('achievement_receiver', 'achievement_reciever', schema='STG_ACHIEVEMENT')


def downgrade():
    op.rename_table('achievement_reciever', 'achievement_receiver', schema='STG_ACHIEVEMENT')
