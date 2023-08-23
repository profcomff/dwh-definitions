"""empty message

Revision ID: def60a611899
Revises: 0b93d0ede7b8
Create Date: 2023-08-23 18:30:13.305201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'def60a611899'
down_revision = '0b93d0ede7b8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_group("dwh_STG_TEST_read")
    op.create_group("dwh_STG_TEST_write")
    op.create_group("dwh_STG_TEST_all")


def downgrade():
    op.delete_group("dwh_STG_TEST_all")
    op.delete_group("dwh_STG_TEST_write")
    op.delete_group("dwh_STG_TEST_read")
