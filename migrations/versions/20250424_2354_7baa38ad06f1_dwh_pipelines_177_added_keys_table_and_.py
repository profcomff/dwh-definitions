"""dwh-pipelines#177: added keys table and encrypted userdata.info

Revision ID: 7baa38ad06f1
Revises: 32883c034be8
Create Date: 2025-04-24 23:54:50.129638

"""

import os

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '7baa38ad06f1'
down_revision = '32883c034be8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'encrypted_info',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('param_id', sa.Integer(), nullable=True),
        sa.Column('source_id', sa.Integer(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=True),
        sa.Column('value', sa.LargeBinary(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.Column('modify_ts', sa.DateTime(), nullable=True),
        sa.Column('is_deleted', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_USERDATA',
        info={'sensitive': False},
    )
    op.create_table(
        'info_keys',
        sa.Column('id', sa.Integer(), nullable=False, comment='key id (maps to)'),
        sa.Column('key', sa.String(), nullable=False, comment='symmetric encryption key'),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_USERDATA',
        info={'sensitive': True},
    )
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")


def downgrade():
    op.drop_table('info_keys', schema='STG_USERDATA')
    op.drop_table('encrypted_info', schema='STG_USERDATA')
    op.execute("DROP EXTENSION pgcrypto")
