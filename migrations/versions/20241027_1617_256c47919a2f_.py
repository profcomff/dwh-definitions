"""empty message

Revision ID: 256c47919a2f
Revises: 8253b11f2c82
Create Date: 2024-10-27 16:17:22.730586

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '256c47919a2f'
down_revision = '8253b11f2c82'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table_schema("ODS_USER")
    op.create_table(
        'info',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('phone_number', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='ODS_USER',
    )


def downgrade():
    op.drop_table('info', schema='ODS_USER')
    op.drop_table_schema("ODS_USER")
