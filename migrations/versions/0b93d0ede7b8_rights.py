"""rights

Revision ID: 0b93d0ede7b8
Revises: 0a24041f09d1
Create Date: 2023-08-23 18:25:50.795465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b93d0ede7b8'
down_revision = '0a24041f09d1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("STG_TEST")
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='STG_TEST'
    )
    op.create_group("dwh_STG_TEST_read")
    op.create_group("dwh_STG_TEST_write")
    op.create_group("dwh_STG_TEST_all")


def downgrade():
    op.delete_group("dwh_STG_TEST_all")
    op.delete_group("dwh_STG_TEST_write")
    op.delete_group("dwh_STG_TEST_read")
    op.drop_table('test', schema='STG_TEST')
    op.drop_table_schema("STG_TEST")
