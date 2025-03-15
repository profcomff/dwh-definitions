"""add_union_member_card_table

Revision ID: 9dcc2999fec1
Revises: c335441a4bf8
Create Date: 2025-03-15 16:03:11.521835

"""

from alembic import op
import sqlalchemy as sa
import os
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9dcc2999fec1'
down_revision = 'c335441a4bf8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'union_member_card',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('card_id', sa.Integer(), nullable=True),
        sa.Column(
            'card_number', sa.String(), nullable=True, comment="card number - number of user's card from ODS.user.info"
        ),
        sa.PrimaryKeyConstraint('user_id'),
        schema='DM_USER',
        info={'sensitive': False},
    )
    op.grant_on_table(
        "test_dwh_dm_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_read",
        ['SELECT'],
        '"DM_USER".union_member_card',
    )
    op.grant_on_table(
        "test_dwh_dm_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_USER".union_member_card',
    )
    op.grant_on_table(
        "test_dwh_dm_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_all",
        ['ALL'],
        '"DM_USER".union_member_card',
    )
    op.create_index(
        op.f('ix_DM_USER_union_member_card_user_id'), 'union_member_card', ['user_id'], unique=False, schema='DM_USER'
    )


def downgrade():
    op.drop_index(op.f('ix_DM_USER_union_member_card_user_id'), table_name='union_member_card', schema='DM_USER')
    op.revoke_on_table(
        "test_dwh_dm_user_read" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_read",
        ['SELECT'],
        '"DM_USER".union_member_card',
    )
    op.revoke_on_table(
        "test_dwh_dm_user_write" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_write",
        ['SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'INSERT'],
        '"DM_USER".union_member_card',
    )
    op.revoke_on_table(
        "test_dwh_dm_user_all" if os.getenv("ENVIRONMENT") != "production" else "prod_dwh_dm_user_all",
        ['ALL'],
        '"DM_USER".union_member_card',
    )
    op.drop_table('union_member_card', schema='DM_USER')
