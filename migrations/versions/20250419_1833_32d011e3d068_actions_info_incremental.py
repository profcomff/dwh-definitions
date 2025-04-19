"""actions info incremental

Revision ID: 32d011e3d068
Revises: d43d62fb3748
Create Date: 2025-04-19 18:33:55.880870

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '32d011e3d068'
down_revision = 'd43d62fb3748'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'actions_info_incremental',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('action', sa.String(), nullable=True),
        sa.Column('path_from', sa.String(), nullable=True),
        sa.Column('path_to', sa.String(), nullable=True),
        sa.Column('additional_data', sa.String(), nullable=True),
        sa.Column('create_ts', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema='STG_MARKETING',
        info={'sensitive': False},
    )


def downgrade():
    op.drop_table('actions_info_incremental', schema='STG_MARKETING')
