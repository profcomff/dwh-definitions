"""add col in dm_marketing

Revision ID: 018159bb0cfc
Revises: b9c1ac6c4360
Create Date: 2025-04-17 19:34:42.627766

"""

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '018159bb0cfc'
down_revision = 'b9c1ac6c4360'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'frontend_actions_services',
        sa.Column(
            'service_from_name', sa.String(), nullable=True, comment='Назввание сервиса, откуда пользователь перешел'
        ),
        schema='DM_MARKETING',
    )
    op.add_column(
        'frontend_actions_services',
        sa.Column(
            'service_to_name', sa.String(), nullable=True, comment='Назввание сервиса, куда пользователь перешел'
        ),
        schema='DM_MARKETING',
    )
    op.drop_column('frontend_actions_services', 'service_name', schema='DM_MARKETING')


def downgrade():
    op.add_column(
        'frontend_actions_services',
        sa.Column(
            'service_name',
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
            comment='Назввание сервиса, куда пользователь перешел',
        ),
        schema='DM_MARKETING',
    )
    op.drop_column('frontend_actions_services', 'service_to_name', schema='DM_MARKETING')
    op.drop_column('frontend_actions_services', 'service_from_name', schema='DM_MARKETING')
