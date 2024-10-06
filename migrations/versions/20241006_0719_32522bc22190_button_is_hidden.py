"""button_is_hidden

Revision ID: 32522bc22190
Revises: 0e97fd76b68a
Create Date: 2024-10-06 07:19:02.218304

"""

from alembic import op
import sqlalchemy as sa
import os


# revision identifiers, used by Alembic.
revision = '32522bc22190'
down_revision = '0e97fd76b68a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('button', sa.Column('is_hidden', sa.Boolean(), nullable=True))
    conn = op.get_bind()
    conn.execute(sa.text(f"""UPDATE "button" SET "is_hidden"='false'"""))
    op.alter_column('button', 'is_hidden', nullable=False)


def downgrade():
    op.drop_column('button', 'is_hidden', schema='STG_SERVICES')
